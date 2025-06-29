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

{% for file in site.static_files %}
  {% if file.path contains 'docs/issues/' and file.extname == '.md' %}
- [{{ file.name | remove: '.md' }}]({{ file.path | relative_url }})
  {% endif %}
{% endfor %}

---

> 자세한 내용과 rule 예시는 위 이슈 링크를 참고하세요! 