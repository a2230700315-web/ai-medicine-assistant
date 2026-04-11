#!/usr/bin/env python3
"""
Vercel 部署前检查脚本
验证所有必要的文件和配置是否存在
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """检查文件是否存在"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} (未找到)")
        return False

def check_file_content(filepath, required_content, description):
    """检查文件内容是否包含必要的内容"""
    if not os.path.exists(filepath):
        print(f"❌ {description}: 文件不存在")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        for item in required_content:
            if item in content:
                print(f"✅ {description}: 包含 '{item}'")
            else:
                print(f"❌ {description}: 缺少 '{item}'")
                return False
    return True

def main():
    print("=== Vercel 部署前检查 ===\n")
    
    all_checks_passed = True
    
    # 检查核心文件
    print("1. 检查核心文件:")
    all_checks_passed &= check_file_exists("backend.py", "FastAPI 后端")
    all_checks_passed &= check_file_exists("api/index.py", "Vercel Python 入口")
    all_checks_passed &= check_file_exists("vercel.json", "Vercel 配置")
    all_checks_passed &= check_file_exists("requirements.txt", "Python 依赖")
    all_checks_passed &= check_file_exists("package.json", "前端依赖")
    all_checks_passed &= check_file_exists("runtime.txt", "Python 运行时版本")
    
    print("\n2. 检查数据文件:")
    all_checks_passed &= check_file_exists("public/cases.json", "案例数据")
    all_checks_passed &= check_file_exists("knowledge/industry_standard.json", "知识库")
    
    print("\n3. 检查配置文件:")
    all_checks_passed &= check_file_exists(".env.example", "环境变量模板")
    all_checks_passed &= check_file_exists(".gitignore", "Git 忽略文件")
    
    print("\n4. 检查文档:")
    all_checks_passed &= check_file_exists("README.md", "项目说明")
    all_checks_passed &= check_file_exists("VERCEL_DEPLOYMENT.md", "部署指南")
    
    print("\n5. 检查 vercel.json 配置:")
    vercel_checks = [
        '"rewrites"',
        '"/api/',
        '"/api/index.py"'
    ]
    all_checks_passed &= check_file_content("vercel.json", vercel_checks, "Vercel 配置")
    
    print("\n6. 检查 requirements.txt:")
    req_checks = [
        "fastapi",
        "uvicorn",
        "python-dotenv",
        "pydantic",
        "sse-starlette",
        "mangum"
    ]
    all_checks_passed &= check_file_content("requirements.txt", req_checks, "Python 依赖")
    
    print("\n7. 检查 runtime.txt:")
    runtime_checks = [
        "python-3.11"
    ]
    all_checks_passed &= check_file_content("runtime.txt", runtime_checks, "Python 运行时版本")
    
    print("\n8. 检查 api/index.py:")
    api_checks = [
        "from backend import app",
        "from mangum import Mangum",
        "handler = Mangum(app)"
    ]
    all_checks_passed &= check_file_content("api/index.py", api_checks, "API 入口")
    
    print("\n9. 检查 backend.py:")
    backend_checks = [
        "app = FastAPI",
        "os.getenv",
        "VOLC_API_KEY",
        "VOLC_ENDPOINT_ID"
    ]
    all_checks_passed &= check_file_content("backend.py", backend_checks, "后端配置")
    
    print("\n10. 检查前端构建配置:")
    if os.path.exists("package.json"):
        with open("package.json", 'r', encoding='utf-8') as f:
            package_content = f.read()
            if '"build"' in package_content and '"vite build"' in package_content:
                print("✅ package.json: 包含构建脚本")
            else:
                print("❌ package.json: 缺少构建脚本")
                all_checks_passed = False
    else:
        print("❌ package.json: 文件不存在")
        all_checks_passed = False
    
    print("\n11. 检查前端 API 请求路径:")
    if os.path.exists("src/components/ChatInterface.jsx"):
        with open("src/components/ChatInterface.jsx", 'r', encoding='utf-8') as f:
            chat_content = f.read()
            if "'/api/chat/stream'" in chat_content and "'/api/chat/review'" in chat_content:
                print("✅ ChatInterface.jsx: 使用相对路径 /api/*")
            else:
                print("❌ ChatInterface.jsx: API 路径配置错误")
                all_checks_passed = False
    else:
        print("❌ ChatInterface.jsx: 文件不存在")
        all_checks_passed = False
    
    print("\n12. 检查环境变量:")
    env_file = ".env"
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            env_content = f.read()
            if "VOLC_API_KEY" in env_content and "VOLC_ENDPOINT_ID" in env_content:
                print("✅ .env: 环境变量已配置")
            else:
                print("⚠️  .env: 环境变量未完全配置 (部署时需要在 Vercel 中设置)")
    else:
        print("⚠️  .env: 文件不存在 (部署时需要在 Vercel 中设置环境变量)")
    
    print("\n" + "="*50)
    if all_checks_passed:
        print("✅ 所有检查通过！项目已准备好部署到 Vercel")
        print("\n下一步:")
        print("1. 在 Vercel 项目设置中添加环境变量:")
        print("   - VOLC_API_KEY")
        print("   - VOLC_ENDPOINT_ID")
        print("2. 运行: git commit && git push (触发 Vercel 自动部署)")
        return 0
    else:
        print("❌ 部分检查失败，请修复上述问题后再部署")
        return 1

if __name__ == "__main__":
    sys.exit(main())
