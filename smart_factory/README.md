# Smart Factory Dashboard Demo

AI Iris와 분리된 독립 실행용 Smart Factory 대시보드 데모입니다. 데이터베이스, 로그인, 머신러닝 모델, 외부 API 없이 실행됩니다.

## 실행

```powershell
cd smart_factory
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

브라우저에서 <http://127.0.0.1:8000/smart-factory/dashboard>를 여세요.

## GitHub에 올리기

이 `smart_factory` 폴더의 파일만 별도 저장소에 업로드하면 됩니다. 저장소 루트에서 `python app.py`를 실행할 수 있도록 폴더 내부 파일을 저장소 루트로 옮겨도 됩니다.
