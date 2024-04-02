
1. 가상 환경 세팅
```bash
python -m venv venv
```

2. 가상 환경 활성화
```bash
. ./venv/bin/activate
```

3. requirements.txt 명시된 패키지 설치
```bash
pip install -r requirements.txt
```

4. main.py 실행
```bash
python ./src/main.py
```

(작업 완료 후) 가상 환경 비활성화
```bash
deactivate
```

---

- title: Review 제목
- contents_en: Review 내용(영문 원본)
- contents_ko: Review 내용(한글 번역)
- created_at: Review 작성일
- rating: Review 작성자가 입력한 LC 서비스에 대한 등급(0.0~5.0)
- helpful: '좋아요' 개수
- not_helpful: '싫어요' 개수
- s_compound: 종합 감정 분석 지수 (-1.0~1.0)
- s_positive: 긍정 감정 분석 지수 (-1.0~1.0)
- s_neutral: 중립 감정 분석 지수 (-1.0~1.0)
- s_negative: 부정 감정 분석 지수 (-1.0~1.0)