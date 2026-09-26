# 우제율 (Jae-Yul Woo) — AI 네이티브 개발자 · 에이전트 오케스트레이션 (Vibe Coding)

dkdlqoddi@gmail.com · https://github.com/dkdlqoddi · https://dkdlqoddi.github.io · 대한민국

> 마스터 이력서([../resume.md](../resume.md))의 사실을 AI 네이티브 개발 관점으로 재구성한 요약본입니다. 새로운 사실은 없습니다.

## 요약

2026년부터 Claude Code, Codex CLI, Antigravity 세 가지 코딩 에이전트를 실무의 기본 개발 방식으로 전환한 엔지니어입니다. 5개월 동안 약 114억 토큰의 컨텍스트를 처리하며 사내 풀스택 대시보드, MCP 서버, LLM 게이트웨이, GraphRAG 위키, 스킬 허브 같은 AI 인프라를 에이전트 주도로 구축했고, 그 과정에서 얻은 방법론을 공개 개발 하네스(dev-env-blindspot)와 팀 세미나 7편으로 정리했습니다. 임베디드·DevOps 배경 덕분에 에이전트가 만든 결과를 hook, CI, 정책으로 집행하는 데 익숙합니다.

## 지표 (2026-09-22 로컬 전수 집계)

| 지표 | 값 |
|---|---|
| 총 컨텍스트 처리량 | 약 114억 토큰 (11,401,278,027) |
| 순수 생성·추론 산출량 | 약 7,251만 토큰 (72,513,989) |
| 도구별 | Claude Code 101.0억 · Antigravity 9.3억 · Codex CLI 3.6억 |
| 산출 | 신규 저장소 46개 · 고유 커밋 1,800건 이상 · 사내 프로젝트 12개 이상 · 발표 7편 (2026-04 ~ 09) |

집계 스크립트는 세 도구의 로컬 사용 기록(통계 캐시, rollout JSONL, 대화 DB)을 직접 읽어 계산하며, 이 저장소(`scripts/aggregate_tokens.py`)에 공개되어 있습니다.

## 하네스 엔지니어링

- **dev-env-blindspot** (공개 저장소, 커밋 98건): 코드를 쓰기 전에 모르는 것(unknown unknowns)을 결정 가능한 질문으로 바꾸는 `blindspot-pass` 스킬, 읽기 전용 `codebase-scanner` 에이전트, 세션 시작 hook으로 주입되는 5줄 MANDATE, append-only 결정 기록. 서브모듈 한 줄로 설치되어 15개 이상 프로젝트에 적용. 풀 버전(요구사항 인터뷰·설계 문서·머지 전 퀴즈·3계층 문서)의 토큰·시간·사용자 턴 비용을 실측한 뒤 lite로 축소.
- **2-하네스 스웜 워크플로** (`claude-antigravity-cowork`): Claude Code가 Opus/Fable xhigh로 계획·리뷰(`swarm-plan`, `swarm-review`, `swarm-auditor`)를 맡고, Antigravity가 Gemini Flash로 워커·체커 서브에이전트를 병렬 실행. 상태 파일을 단일 writer 상태 기계로 관리하고 작업당 라운드 상한 적용.
- **자율 개발 스택** (R14-V2): `/issue → /spec → G1 → /bolt → /verify → /review → /ship`을 서브에이전트 8종·스킬 7종이 무중단으로 수행하고 사람은 PR 머지만 담당. guard hook, CODEOWNERS, CI 필수 체크로 집행.
- **팀 협업 설계**: 10명이 동시에 Claude Code로 개발하는 저장소를 위해 ADR 66건·요구사항 137건을 3계층 문서(규칙·지도·명세)로, 다시 한 줄짜리 결정 기록 표로 전환해 컨텍스트 비용을 낮춤.
- **모델 배치 원칙**: 판단(계획·리뷰·머지 게이트)은 Opus/Fable xhigh, 탐색·기계 검사는 Sonnet/Haiku, 대량 병렬 실행은 Gemini Flash. 토큰은 판단에만 쓰고 검사·실행은 hook과 CI에 맡김.

## AI 인프라 구축 (삼성전자 파운드리사업부, 2026)

- **GAIA 2.0 대시보드** (커밋 850건 이상): Next.js 16, Prisma/PostgreSQL 모델 23개, Route Handler 41개, 모듈 19개, LangGraph 어시스턴트, Playwright e2e. 설계 사인오프 진행을 마일스톤 Score·Gantt·Run 트리·floorplan·리포트 이메일로 추적.
- **정책 기반 MCP 서버**: 공용 서버의 파일·명령·DB 질의·내부 API를 디렉터리 정책으로 노출(툴 17개), LangGraph 파일 분석 툴, OpenCode·Claude Code·Codex 클라이언트.
- **LLM 게이트웨이 API 서버**: FastAPI, OpenAI 호환 프록시 + MCP REST 릴레이 + 투명 MCP 프로토콜 프록시.
- **LLM 위키** (커밋 120건): 원문 불변 보존, Claude Code가 위키를 유지, GraphRAG + BM25 하이브리드 검색, 헤드리스 인제스트 권한 제한으로 프롬프트 인젝션 방어.
- **Agent Skill 허브** (커밋 108건): OpenCode 호환 스킬 공유 플랫폼. 릴리스 불변성, 감사 로그, ZIP 경로 검증, Docker + nginx.
- **EDA MCP 하네스**: OpenCode에 EDA 벤더 MCP 3종을 연결해 프롬프트로 부리는 반도체 지식 자동화, 사내 이메일 아카이빙 플랫폼, 사내 LLM(Gemma 4)·BGE-M3 임베딩 기반 의미 검색 설계.
- **설계 자동화 현업**: 사내 LLM API로 EDA 툴 실행 자동화, 설계 파라미터 값 수집, 툴 로그 파싱·저장을 수행. 넷리스트 파싱·DB 적재 파이프라인과 LangGraph 로그 분석 플로우가 관련 산출물.

## 개인 AI 도구 (github.com/dkdlqoddi)

- **cheap-agent** (v0.4.1): 구독 중인 CLI(Claude Code, Codex, OpenCode, Antigravity)의 headless 모드를 실행 엔진으로 재활용하는 자기학습 오케스트레이터. 의존성 0, 파일 기반 IPC, best-of-N·세션 재개·비용 상한·작업 큐 등 19개 토글, 회고로 lesson 축적.
- **custom-llm-api**: Antigravity CLI를 API 키 없이 OpenAI 호환 API로 노출하는 FastAPI 서버.
- **custom-llm-wiki**: Claude Code 스킬 + Next.js 16 RAG 웹(BM25 + e5-small 하이브리드).
- **skill-verifier**: 스킬 정적 검사 + LLM 리뷰 파이프라인. **librarian-mcp**: 락파일 동기화 스킬 라이브러리 36개. **paper-review**: 논문 지식 베이스.
- **모델 A/B 벤치마크** (공개): 동일 프롬프트 시퀀스로 Next.js 앱을 구축해 Opus vs Fable의 시간·토큰·품질 비교.
- **에이전트 파이프라인 서비스**: 라쿠텐 → Claude 번역 → Gemini 이미지 번역 → 스마트스토어 등록(`pycommerce`), Claude 대본 → Gemini·Veo 영상 → 업로드 YouTube Shorts 파이프라인, AI 해커톤 스타터 킷(DEMO_MODE mock).

## 발표 (https://dkdlqoddi.github.io)

설계 AX 전환(2026-07-31) · 안전한 AI 설계 자동화 아키텍처(08-03) · Python Automation: DX vs AX(08-19, 팀 세미나 1부) · AI Agent Skills Philosophy(08-19, 2부) · 나만의 돌쇠 AI 만들기(09-01) · AI, 한 걸음 더(09-20) · 내 자료가 이해가 되는 순간: NotebookLM(09-21)

## 도구·환경

Claude Code(Fable 5.1 1M, effort max, 서브에이전트 Opus, 공식 플러그인 9종, claude-mem) · Codex CLI(세션 580건 이상) · Antigravity CLI(대화 500건 이상) · OpenCode · GitHub Copilot · MCP 서버/클라이언트 · LangGraph/LangChain · Claude·Gemini·OpenAI 호환 API · Playwright MCP · 셀프호스팅 GitHub Actions 러너에서 `claude -p` 헤드리스 실행

## 배경

삼성전자 파운드리사업부 임베디드 소프트웨어 엔지니어(2022.03 – 현재, ARM Cortex 포팅·Linux 드라이버·CI/CD, 현재 사내 LLM API 기반 설계 자동화). SEC 연구소 소프트웨어 개발자(2018.01 – 2019.06, SDR 신호처리). 성균관대학교 반도체시스템공학 학사(2014 – 2022), IRIS Lab 학부 연구생. 자세한 내용은 [펌웨어·임베디드 관점](firmware-embedded.md)과 [DevOps 관점](devops-platform.md)을 참고하세요.
