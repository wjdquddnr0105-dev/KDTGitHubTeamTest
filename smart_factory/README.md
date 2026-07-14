# Smart Factory Dashboard

AI Iris와 분리된 독립 실행형 Smart Factory 대시보드 데모입니다.

데이터베이스, 로그인, 머신러닝 모델, 외부 API 없이 대시보드 화면을 실행할 수 있습니다.

## 주요 기능

- 생산 현황 KPI
- 공장 운영 상태
- 금일 생산 목표
- 품질 요약
- 주요 이상 알림 및 최근 이벤트
- 품질 관리 화면
- 설비 및 자원 관리 화면
- 분석 리포트 화면
- Smart Factory AI Assistant UI
- 반응형 화면 구성

현재 버전의 모든 화면 데이터는 화면 확인을 위한 고정 데모 데이터입니다.

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
│     ├─ dashboard.html
│     ├─ quality.html
│     ├─ equipment.html
│     └─ reports.html
├─ static/
│  ├─ css/
│  │  └─ smart_factory.css
│  └─ js/
│     ├─ smart_factory.js
│     ├─ smart_factory_quality.js
│     ├─ smart_factory_equipment.js
│     └─ smart_factory_reports.js
└─ tests/
   └─ test_app.py
```

## 동작 로직

1. 사용자가 Smart Factory 페이지 중 하나에 접속합니다.
2. Flask가 해당 HTML 템플릿을 렌더링합니다.
3. `base.html`이 공통 레이아웃, 네비게이션, Assistant UI를 제공합니다.
4. `smart_factory.css`가 공통 화면 스타일을 구성합니다.
5. 페이지별 JavaScript가 선택, 탭, 필터, 임계값 입력 등 화면 동작을 처리합니다.
6. 화면 데이터는 현재 화면 표시용 고정 데모 데이터입니다.

## 제공 페이지

| 페이지 | URL | 프로토타입 동작 |
| --- | --- | --- |
| Dashboard | `/smart-factory/dashboard` | KPI, 운영 현황, 목표, 품질 요약, 이벤트 표시 |
| Quality | `/smart-factory/quality` | 생산 라인 및 AGV 선택에 따른 상세 상태 표시 |
| Equipment | `/smart-factory/equipment` | 설비 상태와 센서 정보 표시, 임계값 설정 버튼 UI |
| Reports | `/smart-factory/reports` | 기간 선택, 추이 차트, 공정 비교, 리포트 내보내기 UI |

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
