import os
import zipfile
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_model():
    model_zip = "vosk-model-small-cn-0.22.zip"
    model_dir = "vosk-model-small-cn"
    
    if not os.path.exists(model_zip):
        logger.error(f"模型压缩包不存在: {model_zip}")
        return False
    
    if os.path.exists(model_dir):
        logger.info(f"模型目录已存在: {model_dir}")
        return True
    
    logger.info("正在解压模型...")
    
    try:
        with zipfile.ZipFile(model_zip, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        logger.info("模型解压完成")
        
        if os.path.exists(model_dir):
            logger.info(f"✅ 模型解压成功: {model_dir}")
            return True
        else:
            logger.error(f"模型目录未创建: {model_dir}")
            return False
            
    except Exception as e:
        logger.error(f"解压失败: {e}")
        return False

if __name__ == "__main__":
    success = extract_model()
    if success:
        print("\n" + "=" * 50)
        print("Vosk中文模型解压成功！")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("Vosk中文模型解压失败！")
        print("=" * 50)