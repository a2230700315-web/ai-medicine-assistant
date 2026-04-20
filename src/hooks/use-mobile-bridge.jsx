import { useEffect } from 'react'
import { App } from '@capacitor/app'
import { StatusBar, Style } from '@capacitor/status-bar'
import { Keyboard } from '@capacitor/keyboard'
import { Toast } from '@capacitor/toast'

const useMobileBridge = (navigationCallbacks = {}) => {
  const { onBackButton, onKeyboardShow, onKeyboardHide } = navigationCallbacks

  useEffect(() => {
    let backButtonListener = null

    const setupListeners = async () => {
      try {
        backButtonListener = await App.addListener('backButton', ({ canGoBack }) => {
          if (onBackButton) {
            onBackButton(canGoBack)
          } else if (canGoBack) {
            window.history.back()
          } else {
            App.exitApp()
          }
        })

        if (onKeyboardShow) {
          Keyboard.addListener('keyboardWillShow', (info) => {
            onKeyboardShow(info.keyboardHeight)
          })
        }

        if (onKeyboardHide) {
          Keyboard.addListener('keyboardWillHide', () => {
            onKeyboardHide()
          })
        }
      } catch (error) {
        console.log('Mobile bridge setup skipped (not running in native app)')
      }
    }

    setupListeners()

    return () => {
      if (backButtonListener) {
        backButtonListener.remove()
      }
    }
  }, [onBackButton, onKeyboardShow, onKeyboardHide])

  const setStatusBarStyle = async (style = 'light') => {
    try {
      await StatusBar.setStyle({
        style: style === 'dark' ? Style.Dark : Style.Light
      })
    } catch (error) {
      console.log('StatusBar not available')
    }
  }

  const setStatusBarColor = async (color) => {
    try {
      await StatusBar.setBackgroundColor({ color })
    } catch (error) {
      console.log('StatusBar not available')
    }
  }

  const showToast = async (message, duration = 'short') => {
    try {
      await Toast.show({
        text: message,
        duration: duration
      })
    } catch (error) {
      console.log('Toast not available')
    }
  }

  return {
    setStatusBarStyle,
    setStatusBarColor,
    showToast
  }
}

export default useMobileBridge

export function useHardwareBackButton(callback) {
  useEffect(() => {
    let listener = null

    const setup = async () => {
      try {
        listener = await App.addListener('backButton', () => {
          if (callback) callback()
        })
      } catch (error) {
        console.log('Hardware back button not available')
      }
    }

    setup()

    return () => {
      if (listener) listener.remove()
    }
  }, [callback])
}

export function isNativeApp() {
  return typeof window !== 'undefined' && 
         window.Capacitor && 
         window.Capacitor.isNativePlatform()
}

export function getPlatform() {
  if (typeof window === 'undefined') return 'web'
  if (!window.Capacitor) return 'web'
  return window.Capacitor.getPlatform()
}
