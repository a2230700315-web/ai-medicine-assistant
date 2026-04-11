import urllib.request
import urllib.error
import json
import os
import socket
import base64

VOLC_APP_KEY = "8636573250"
VOLC_ACCESS_KEY = "TBd8NadSYc_OK17mLnnQk0NN8WflbZWJ"
VOLC_RESOURCE_ID = "volc.bigasr.auc_turbo"

print("=" * 50)
print("豆包语音识别配置测试")
print("=" * 50)
print(f"VOLC_APP_KEY: {VOLC_APP_KEY}")
print(f"VOLC_ACCESS_KEY: {VOLC_ACCESS_KEY[:10]}...")
print(f"VOLC_RESOURCE_ID: {VOLC_RESOURCE_ID}")
print("=" * 50)

if not VOLC_APP_KEY or not VOLC_ACCESS_KEY:
    print("❌ 配置错误：缺少API密钥")
    print("请检查.env文件中的配置")
else:
    print("✅ 配置检查通过")
    print("\n正在测试API连接...")
    
    try:
        import uuid
        test_url = "https://openspeech.bytedance.com/api/v3/auc/bigmodel/recognize/flash"
        
        headers = {
            "X-Api-App-Key": VOLC_APP_KEY,
            "X-Api-Access-Key": VOLC_ACCESS_KEY,
            "X-Api-Resource-Id": VOLC_RESOURCE_ID,
            "X-Api-Request-Id": str(uuid.uuid4()),
            "X-Api-Sequence": "-1",
            "Content-Type": "application/json"
        }
        
        test_payload = {
            "user": {
                "uid": VOLC_APP_KEY
            },
            "audio": {
                "data": "UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA="
            },
            "request": {
                "model_name": "bigmodel"
            }
        }
        
        print(f"正在发送请求到: {test_url}")
        print(f"请求头: {json.dumps({k: v for k, v in headers.items() if 'Access' not in k}, indent=2)}")
        
        req = urllib.request.Request(
            test_url,
            data=json.dumps(test_payload).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        socket.setdefaulttimeout(60)
        
        print("等待API响应...")
        with urllib.request.urlopen(req, timeout=60) as response:
            print(f"收到响应，状态码: {response.status}")
            
            status_code = response.headers.get('X-Api-Status-Code', '')
            status_msg = response.headers.get('X-Api-Message', '')
            logid = response.headers.get('X-Tt-Logid', '')
            
            print(f"X-Api-Status-Code: {status_code}")
            print(f"X-Api-Message: {status_msg}")
            print(f"X-Tt-Logid: {logid}")
            
            response_data = response.read().decode('utf-8')
            result = json.loads(response_data)
            
            print(f"API响应内容: {json.dumps(result, indent=2, ensure_ascii=False)}")
            
            if status_code == "20000000":
                print("\n✅ API连接测试成功！")
                print("豆包语音识别功能配置正确")
                
                if "result" in result and "text" in result["result"]:
                    print(f"识别结果: {result['result']['text']}")
            else:
                print(f"\n❌ API连接测试失败")
                print(f"错误代码: {status_code}")
                print(f"错误信息: {status_msg}")
                
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP错误: {e.code}")
        try:
            error_data = json.loads(e.read().decode('utf-8'))
            print(f"错误详情: {json.dumps(error_data, indent=2, ensure_ascii=False)}")
        except:
            print(f"错误信息: {e.reason}")
    except urllib.error.URLError as e:
        print(f"❌ URL错误: {e.reason}")
        print("可能的原因:")
        print("1. 网络连接问题")
        print("2. 豆包API服务暂时不可用")
    except socket.timeout:
        print("❌ 请求超时")
        print("可能的原因:")
        print("1. 网络连接缓慢")
        print("2. 豆包API服务响应缓慢")
    except Exception as e:
        print(f"❌ API连接测试失败: {str(e)}")
        print("可能的原因:")
        print("1. 网络连接问题")
        print("2. API密钥配置错误")
        print("3. 豆包API服务暂时不可用")

print("\n" + "=" * 50)