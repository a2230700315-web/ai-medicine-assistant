import os
import urllib.request
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_model_alternative():
    model_url = "https://github.com/alphacep/vosk-api/raw/master/models/vosk-model-small-cn-0.22.zip"
    model_zip = "vosk-model-small-cn-0.22.zip"
    model_dir = "vosk-model-small-cn"
    
    if os.path.exists(model_dir):
        logger.info(f"模型目录已存在: {model_dir}")
        return True
    
    logger.info(f"正在下载Vosk中文模型（备用源）...")
    logger.info(f"下载地址: {model_url}")
    
    try:
        def download_progress(count, block_size, total_size):
            if total_size > 0:
                percent = int(count * block_size * 100 / total_size)
                if percent % 10 == 0:
                    logger.info(f"下载进度: {percent}%")
        
        urllib.request.urlretrieve(model_url, model_zip, download_progress)
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
    success = download_model_alternative()
    if success:
        print("\n" + "=" * 50)
        print("Vosk中文模型安装成功！")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("Vosk中文模型安装失败！")
        print("请手动下载模型:")
        print("https://alphacephei.com/vosk/models")
        print("下载后解压到项目目录")
        print("=" * 50)