import os
import urllib.request
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_model_direct():
    model_url = "https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip"
    model_zip = "vosk-model-small-cn-0.22.zip"
    model_dir = "vosk-model-small-cn"
    
    if os.path.exists(model_dir):
        logger.info(f"模型目录已存在: {model_dir}")
        return True
    
    logger.info(f"正在下载Vosk中文模型...")
    logger.info(f"下载地址: {model_url}")
    logger.info("这可能需要几分钟时间，请耐心等待...")
    
    try:
        urllib.request.urlretrieve(model_url, model_zip)
        logger.info("模型下载完成")
        
        import zipfile
        logger.info("正在解压模型...")
        with zipfile.ZipFile(model_zip, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        logger.info("模型解压完成")
        
        os.remove(model_zip)
        logger.info(f"清理临时文件: {model_zip}")
        
        if os.path.exists(model_dir):
            logger.info(f"✅ Vosk中文模型安装完成: {model_dir}")
            return True
        else:
            logger.error(f"模型目录未创建: {model_dir}")
            return False
            
    except Exception as e:
        logger.error(f"模型下载失败: {e}")
        return False

if __name__ == "__main__":
    success = download_model_direct()
    if success:
        print("\n" + "=" * 50)
        print("Vosk中文模型安装成功！")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("Vosk中文模型安装失败！")
        print("\n手动下载步骤:")
        print("1. 访问: https://alphacephei.com/vosk/models")
        print("2. 下载: vosk-model-small-cn-0.22.zip")
        print("3. 解压到项目目录")
        print("4. 重命名文件夹为: vosk-model-small-cn")
        print("=" * 50)