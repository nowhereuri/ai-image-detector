# -*- coding: utf-8 -*-
"""
GitHub Codespaces용 실행 스크립트
"""

import os
import sys
from pathlib import Path

# 필요한 디렉토리 생성
directories = [
    'static/uploads',
    'static/results', 
    'data/feedback',
    'templates'
]

for directory in directories:
    Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"OK {directory} directory created")

print("\n" + "="*60)
print("🚀 AI 이미지 분류기 - GitHub Codespaces")
print("="*60)
print("📱 접속 방법:")
print("   1. Codespaces에서 'Ports' 탭 클릭")
print("   2. Port 5000 옆의 'Open in Browser' 클릭")
print("   3. 또는 'Public' 버튼으로 공개 URL 생성")
print("="*60)
print("🔧 관리자 기능:")
print("   - /stats: 통계 확인")
print("   - /about: 프로젝트 정보")
print("="*60)

try:
    from app import app
    
    # Codespaces 환경에서 실행
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'  # 외부 접속 허용
    
    print(f"🌐 서버 시작: http://localhost:{port}")
    print("⏹️  중지하려면 Ctrl+C")
    print("="*60)
    
    app.run(debug=False, host=host, port=port)
    
except KeyboardInterrupt:
    print("\n\n🛑 서버가 중지되었습니다.")
except Exception as e:
    print(f"\n❌ 오류 발생: {e}")
    print("🔧 문제 해결:")
    print("   1. requirements.txt 설치 확인")
    print("   2. Python 버전 확인 (3.9+ 권장)")
    print("   3. 포트 5000 사용 가능 여부 확인")
