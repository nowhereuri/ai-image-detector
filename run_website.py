# -*- coding: utf-8 -*-
"""
AI 이미지 분류기 웹사이트 실행 스크립트
이 스크립트를 실행하여 웹 애플리케이션을 시작할 수 있습니다.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_requirements():
    """필요한 패키지들이 설치되어 있는지 확인"""
    print("필요한 패키지 확인 중...")
    
    required_packages = [
        'flask', 'torch', 'transformers', 'PIL', 'numpy', 'pandas'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                import PIL
            else:
                __import__(package)
            print(f"OK {package} 설치됨")
        except ImportError:
            missing_packages.append(package)
            print(f"ERROR {package} 누락")
    
    if missing_packages:
        print(f"\nWARNING 누락된 패키지: {', '.join(missing_packages)}")
        print("다음 명령어로 설치하세요:")
        print("pip install -r requirements.txt")
        return False
    
    print("OK 모든 필요한 패키지가 설치되어 있습니다!")
    return True

def check_model():
    """훈련된 모델이 존재하는지 확인"""
    print("\nAI 모델 확인 중...")
    
    model_path = Path('./ai_vs_real_image_detection')
    
    if model_path.exists():
        print("OK 훈련된 모델을 찾았습니다!")
        return True
    else:
        print("WARNING 훈련된 모델을 찾을 수 없습니다.")
        print("사전 훈련된 모델을 사용합니다.")
        return True  # 사전 훈련된 모델을 사용할 수 있으므로 True로 변경

def create_directories():
    """필요한 디렉토리 생성"""
    print("\n디렉토리 생성 중...")
    
    directories = [
        'static/uploads',
        'static/results', 
        'data/feedback',
        'templates'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"OK {directory} 디렉토리 생성됨")

def main():
    """메인 실행 함수"""
    print("AI 이미지 분류기 웹사이트 시작 중...")
    print("=" * 60)
    
    # 1. 패키지 확인
    if not check_requirements():
        sys.exit(1)
    
    # 2. 모델 확인
    if not check_model():
        print("\n💡 모델 훈련 방법:")
        print("1. 터미널에서 다음 명령어 실행:")
        print("   python ai_image_detector_model_vit.py")
        print("2. 훈련 완료 후 다시 이 스크립트 실행")
        sys.exit(1)
    
    # 3. 디렉토리 생성
    create_directories()
    
    # 4. 웹 애플리케이션 시작
    print("\n웹 애플리케이션 시작 중...")
    print("=" * 60)
    print("브라우저에서 http://localhost:5000 으로 접속하세요!")
    print("종료하려면 Ctrl+C를 누르세요")
    print("=" * 60)
    
    try:
        # Flask 앱 실행
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\n웹사이트가 종료되었습니다.")
    except Exception as e:
        print(f"\nERROR 오류 발생: {e}")
        print("문제 해결 방법:")
        print("1. 모든 패키지가 설치되어 있는지 확인하세요")
        print("2. 모델이 훈련되어 있는지 확인하세요")
        print("3. 포트 5000이 사용 중이 아닌지 확인하세요")

if __name__ == '__main__':
    main()
