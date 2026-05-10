import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json']
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false
      }
    }
  },
  build: {
    // 目标现代浏览器，减少 polyfill 体积
    target: 'es2015',
    // chunk 大小警告阈值
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        // 手动分割大依赖，让浏览器并行加载、且可被独立缓存
        manualChunks: {
          'vendor-react': ['react', 'react-dom'],
          'vendor-icons': ['lucide-react'],
          'vendor-charts': ['echarts', 'echarts-for-react'],
          'vendor-axios': ['axios'],
        },
        // 为每个 chunk 生成独立的 CSS 文件
        assetFileNames: 'assets/[name]-[hash][extname]',
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
      }
    },
    // 开启 CSS 代码分割
    cssCodeSplit: true,
    // 生产环境移除 console
    minify: 'esbuild',
  },
  // 预构建优化，加速开发/冷启动
  optimizeDeps: {
    include: ['react', 'react-dom', 'lucide-react', 'axios']
  }
})
