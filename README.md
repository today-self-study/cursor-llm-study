# cursor-llm-study

**최신 LLM 벤치마크, 프롬프트 엔지니어링, 실전 이슈를 한눈에!**

- 이 저장소는 최신 LLM(대형 언어 모델) 관련 이슈, 벤치마크, 프롬프트 엔지니어링 사례를 실시간으로 모아 보여주는 웹 페이지를 제공합니다.
- GitHub Issues API를 활용하여 항상 최신 이슈 현황을 자동으로 반영합니다.

## 주요 기능
- **실시간 이슈 리스트**: GitHub API를 통해 열려있는 이슈만 자동으로 표시
- **심플하고 세련된 UI**: news.hada.io 스타일의 카드형 리스트, 본문 미리보기, 작성자/작성일/이슈번호 등 부가 정보 제공
- **클릭 시 원본 이슈로 이동**: 각 이슈 클릭 시 GitHub 이슈 페이지로 새 탭 이동

## 데모
- 👉 [GitHub Pages 바로가기](https://today-self-study.github.io/cursor-llm-study/)

## 기술 스택
- **Frontend**: HTML, CSS(Bootstrap 5), JavaScript(ES6)
- **Data**: GitHub Issues API (정적 json 파일 사용하지 않음)

## 프로젝트 구조
```
cursor-llm-study/
  ├─ docs/           # GitHub Pages 정적 파일 (index.html 등)
  ├─ codes/          # 데이터 처리/시각화 코드
  ├─ images/         # LLM 벤치마크 등 시각화 이미지
  └─ README.md
```

## 사용법
1. 이 저장소를 fork/clone 후, docs/index.html을 수정하여 원하는 이슈/스타일로 커스터마이즈할 수 있습니다.
2. GitHub Pages 설정에서 docs/ 폴더를 루트로 지정하면 바로 배포됩니다.

## 참고
- 이슈 데이터는 GitHub API를 통해 실시간으로 불러오므로, 별도의 데이터 파일 관리가 필요 없습니다.
- rate limit(비로그인 60회/시간) 내에서 자유롭게 사용 가능합니다.

---

문의/기여/피드백은 [Issues](https://github.com/today-self-study/cursor-llm-study/issues)로 남겨주세요.