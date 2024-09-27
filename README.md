# Lending Club 기업 서비스에 대한 일반인 리뷰 분석

## 프로젝트 개요

### 데이터 수집 대상 URL
> https://www.creditkarma.com/reviews/personal-loan/single/id/lending-club-personal-loans
- 동적 페이지 > Selenium 사용

### 다음 내용을 수집 및 가공하여 엑셀로 추출
- title: Review 제목
- contents_en: Review 내용(영문 원본)
- contents_ko: Review 내용(한글 번역)
- created_at: Review 작성일
- rating: Review 작성자가 입력한 LC 서비스에 대한 평가 등급(0.0~5.0)
- helpful: '좋아요' 개수
- not_helpful: '싫어요' 개수
- s_compound: 종합 감정 분석 지수 (-1.0~1.0) - Review 내용(영문) 
- s_positive: 긍정 감정 분석 지수 (-1.0~1.0) - Review 내용(영문) 
- s_neutral: 중립 감정 분석 지수 (-1.0~1.0) - Review 내용(영문) 
- s_negative: 부정 감정 분석 지수 (-1.0~1.0) - Review 내용(영문) 

### 활용 예시
- [서비스 평가 등급]과 [종합 감정 분석 지수]를 비교하여 
평가 등급이 낮음에도 감정 지수가 높을 경우 잘못된 수치로 평가하여 
평균 평가 등급 산출에서 제외 or 평가 등급 보정

---

## 환경 세팅

1. 프로젝트 클론
```bash
git clone https://github.com/minuzai/credit-karma_review-scraper
```

2. 가상 환경 세팅
```bash
python -m venv venv
```

3. 가상 환경 활성화
```bash
source ./venv/bin/activate  # Mac
.\venv\Scripts\activate  # Windows
```

4. 패키지 설치
```bash
pip install -r requirements.txt
```

5. 작업 실행
```bash
python ./src/main.py
```

(작업 완료 후) 가상 환경 비활성화
```bash
deactivate
```
