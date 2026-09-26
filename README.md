# jaeyul-woo-resume

우제율(Jae-Yul Woo)의 이력서 저장소입니다. 웹 이력서 원본과 관점별 변형본, 그리고 AI 코딩 에이전트 사용량 집계 스크립트를 담고 있습니다.

## 구성

| 경로 | 내용 |
|---|---|
| `resume/resume.md` | 마스터 이력서 (한국어, 모든 사실의 단일 원천) |
| `resume/index.html` · `resume/resume.css` | 웹 이력서. `dkdlqoddi.github.io/resume/`에 복사해 배포하며 공통 테마(`../assets/theme.css`)와 Pretendard 글꼴을 사용 |
| `resume/variants/firmware-embedded.md` | 펌웨어·임베디드 소프트웨어 엔지니어 관점 |
| `resume/variants/ai-native-engineer.md` | AI 네이티브 개발자(에이전트 오케스트레이션·바이브 코딩) 관점 |
| `resume/variants/devops-platform.md` | DevOps·플랫폼 엔지니어 관점 |
| `resume/portfolio.html` · `resume/portfolio/우제율_포트폴리오.pdf` | 신청서용 포트폴리오(문제→도구→결과물 사례 5건)와 A4 PDF 출력본 |
| `resume/application/application-form.md` | 신청서 양식 답변(AI 활용 경험 2000자 이내, 경력사항, 활동 내역). 휴대폰 번호는 기재하지 않음 |
| `scripts/aggregate_tokens.py` | Claude Code · Codex CLI · Antigravity 누적 토큰 집계 (`--json assets/token-metrics.json`) |
| `assets/token-metrics.json` | 집계 결과 (2026-09-22 기준) |
| `docs/decisions.md` | 결정 기록 (append-only) |

## 갱신 절차

1. 사실 변경은 `resume/resume.md`에 먼저 반영하고, 같은 내용을 `resume/index.html`과 변형본에 옮깁니다. 변형본은 강조 순서만 다르며 새로운 사실을 추가하지 않습니다.
2. 토큰 지표는 활성 에이전트 세션을 모두 종료한 뒤 `python3 scripts/aggregate_tokens.py --json assets/token-metrics.json`으로 재집계합니다.
3. 웹 이력서는 `resume/index.html`, `resume/portfolio.html`, `resume/resume.css`를 `dkdlqoddi.github.io/resume/`에 복사한 뒤 그 저장소의 검증 스크립트를 통과시키고 배포합니다.
4. 포트폴리오 PDF는 발표 사이트의 공통 자산이 필요하므로 사이트 저장소를 로컬 HTTP 서버로 띄운 뒤 Chrome 헤드리스로 인쇄합니다:

   ```bash
   # dkdlqoddi.github.io/resume/ 에 세 파일을 복사한 상태에서
   (cd ~/dkdlqoddi.github.io && python3 -m http.server 8138 --bind 127.0.0.1 &)
   google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
     --virtual-time-budget=8000 --print-to-pdf=resume/portfolio/우제율_포트폴리오.pdf \
     http://127.0.0.1:8138/resume/portfolio.html
   ```
