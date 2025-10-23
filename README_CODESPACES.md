# 🚀 AI 이미지 분류기 - GitHub Codespaces

GitHub Codespaces에서 바로 실행할 수 있는 AI 이미지 분류기입니다.

## 🌐 Codespaces로 실행하기

### 1단계: Codespaces 시작
1. GitHub 저장소 페이지에서 **"Code"** 버튼 클릭
2. **"Codespaces"** 탭 선택
3. **"Create codespace on main"** 클릭
4. Codespaces 환경이 자동으로 설정됩니다

### 2단계: 웹 애플리케이션 실행
```bash
# Codespaces 터미널에서
python start_codespaces.py
```

### 3단계: 웹사이트 접속
1. **"Ports"** 탭 클릭
2. **Port 5000** 옆의 **"Open in Browser"** 클릭
3. 또는 **"Public"** 버튼으로 공개 URL 생성

## 🎯 주요 기능

### 📱 웹 인터페이스
- **이미지 업로드**: 드래그 앤 드롭 또는 파일 선택
- **실시간 분석**: AI 모델로 즉시 분류
- **결과 표시**: REAL/FAKE 예측 및 신뢰도
- **피드백 시스템**: 예측 정확도 개선

### 📊 관리자 기능
- **통계 확인**: `/stats` 페이지
- **프로젝트 정보**: `/about` 페이지
- **피드백 수집**: 사용자 피드백 자동 저장

## 🔧 기술 스택

- **Backend**: Python Flask
- **AI Model**: Vision Transformer (ViT)
- **Frontend**: HTML, CSS, JavaScript
- **Hosting**: GitHub Codespaces

## 📈 성능 지표

- **전체 정확도**: 67.23%
- **REAL 정확도**: 55.07%
- **FAKE 정확도**: 75.00%
- **테스트 이미지**: 354개

## 🚀 공개 URL 생성

### 방법 1: Codespaces Public URL
1. **"Ports"** 탭에서 Port 5000 찾기
2. **"Public"** 버튼 클릭
3. 공개 URL 생성됨 (예: `https://xxx-5000.preview.app.github.dev`)

### 방법 2: ngrok 사용 (고급)
```bash
# Codespaces 터미널에서
pip install pyngrok
ngrok http 5000
```

## 💡 사용 팁

### 1. 최적의 이미지
- **지원 형식**: JPG, PNG, JPEG, GIF, BMP, TIFF
- **권장 크기**: 32x32 ~ 1024x1024
- **품질**: 고해상도, 선명한 이미지

### 2. 정확한 결과를 위한 팁
- **FAKE 탐지**: AI 생성 이미지 탐지에 특화 (75% 정확도)
- **신뢰도 확인**: 낮은 신뢰도 결과는 주의 깊게 검토
- **피드백 제공**: 오분류 사례에 대한 피드백 수집

## 🔄 자동 업데이트

### GitHub 연동
- 코드 수정 후 GitHub에 푸시
- Codespaces에서 자동으로 새 버전 반영
- 실시간 개발 및 테스트 가능

### 환경 설정
- **Python 3.9+** 자동 설치
- **의존성 패키지** 자동 설치
- **포트 포워딩** 자동 설정

## 🛠️ 문제 해결

### 1. 서버 시작 실패
```bash
# 의존성 재설치
pip install -r requirements.txt

# 포트 확인
netstat -tulpn | grep 5000
```

### 2. 이미지 업로드 오류
- 파일 크기 확인 (16MB 이하)
- 지원 형식 확인 (JPG, PNG 등)
- 브라우저 캐시 삭제

### 3. AI 모델 로드 실패
- 인터넷 연결 확인
- Hugging Face 모델 다운로드 상태 확인
- 메모리 사용량 확인

## 📊 모니터링

### Codespaces 리소스
- **CPU 사용량**: Codespaces 대시보드에서 확인
- **메모리 사용량**: 터미널에서 `htop` 명령어
- **네트워크**: 포트 포워딩 상태 확인

### 애플리케이션 로그
- **실시간 로그**: 터미널에서 확인
- **에러 로그**: Flask 디버그 모드
- **사용자 활동**: `/stats` 페이지에서 확인

## 🎉 완료!

이제 GitHub Codespaces에서 AI 이미지 분류기를 웹사이트처럼 운영할 수 있습니다!

**접속 URL**: Codespaces Ports 탭에서 확인

---

**GitHub Codespaces로 언제 어디서나 AI 이미지 분류기를 사용하세요!** 🚀
