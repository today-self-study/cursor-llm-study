---
layout: default
title: cursor-llm-study
---

# cursor-llm-study (GitHub Pages)

최신 LLM 벤치마크, 프롬프트 엔지니어링 등 실전 자료를 한눈에!

---

## Repository 구조

- `images/` : LLM 벤치마크 등 시각화 이미지
- `codes/`  : 데이터 처리 및 시각화 코드

---

## 최신 이슈 목록 (자동 반영)

{% assign issues = site.static_files | where_exp: "file", "file.path contains '/docs/issues/' and file.extname == '.md'" %}
{% for issue in issues %}
- [{{ issue.name | remove: '.md' }}]({{ issue.path | relative_url }})
{% endfor %}

---

## LLM 항목별 벤치마크 차트

### 코딩
![코딩](/images/llm_barchart_코딩.png)

### 수리
![수리](/images/llm_barchart_수리.png)

### 추론
![추론](/images/llm_barchart_추론.png)

### 멀티모달
![멀티모달](/images/llm_barchart_멀티모달.png)

### 속도/비용
![속도/비용](/images/llm_barchart_속도_비용.png)

---

> 자세한 내용과 rule 예시는 위 이슈 링크를 참고하세요! 