# Smart Factory Dashboard

AI Iris와 분리된 독립 실행형 Smart Factory 대시보드 데모입니다.

데이터베이스, 로그인, 머신러닝 모델, 외부 API 없이 대시보드 화면을 실행할 수 있습니다.

## 주요 기능

- 생산 현황 KPI
- 공장 운영 상태
- 금일 생산 목표
- 품질 요약
- 주요 이상 알림 및 최근 이벤트
- Smart Factory AI Assistant UI
- 반응형 화면 구성

현재 버전의 대시보드 데이터는 화면 확인을 위한 고정 데모 데이터입니다.

## 사용된 언어 및 기술

- Python 3
- Flask 3.x
- HTML5
- CSS3
- JavaScript
- Python `unittest`

## 실행 방법

PowerShell에서 `smart_factory` 폴더로 이동합니다.

```powershell
cd smart_factory
```

가상환경을 생성합니다.

```powershell
python -m venv .venv
```

가상환경을 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

필요한 패키지를 설치합니다.

```powershell
pip install -r requirements.txt
```

Flask 서버를 실행합니다.

```powershell
python app.py
```

브라우저에서 아래 주소로 접속합니다.

```text
http://127.0.0.1:8000/smart-factory/dashboard
```

## 프로젝트 구조

```text
smart_factory/
├─ app.py
├─ requirements.txt
├─ README.md
├─ templates/
│  └─ smart_factory/
│     ├─ base.html
│     └─ dashboard.html
├─ static/
│  ├─ css/
│  │  └─ smart_factory.css
│  └─ js/
│     └─ smart_factory.js
└─ tests/
   └─ test_app.py
```

## 동작 로직

1. 사용자가 `/smart-factory/dashboard`에 접속합니다.
2. Flask가 `dashboard.html`을 렌더링합니다.
3. `base.html`이 공통 레이아웃과 Assistant UI를 제공합니다.
4. `smart_factory.css`가 대시보드의 화면 스타일을 구성합니다.
5. `smart_factory.js`가 Assistant 열기/닫기 및 탭 전환을 처리합니다.
6. 대시보드의 KPI와 이벤트 정보는 현재 화면 표시용 고정 데모 데이터입니다.

## AI Iris와의 분리

Smart Factory 독립 앱은 다음 기능을 사용하지 않습니다.

- AI Iris 예측 모델
- 데이터베이스
- 로그인 및 사용자 인증
- 기존 루트 Flask 앱
- 외부 API

따라서 `smart_factory` 폴더만 별도로 복사하거나 GitHub 저장소에 업로드하여 실행할 수 있습니다.

## 테스트

### 저장소 루트에서 실행

```powershell
python -m unittest discover -s smart_factory/tests -v
```

### Smart Factory 폴더 내부에서 실행

```powershell
cd smart_factory
python -m unittest discover -s tests -v
```

## GitHub 업로드 위치

이 프로젝트는 팀 저장소의 `cnn` 개발 브랜치에서 관리합니다.

```text
origin/cnn
```
