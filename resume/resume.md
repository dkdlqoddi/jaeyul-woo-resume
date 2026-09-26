# 우제율 (Jae-Yul Woo)

**Software Engineer — Embedded & Firmware · AI-Native Development · DevOps Automation**

- 이메일: dkdlqoddi@gmail.com
- GitHub: https://github.com/dkdlqoddi
- 발표 자료: https://dkdlqoddi.github.io
- 위치: 대한민국

> 이 문서는 모든 사실의 단일 원천(마스터)입니다. 직무별 요약본은 `variants/` 폴더에 있습니다: [펌웨어·임베디드](variants/firmware-embedded.md) · [AI 네이티브 개발자](variants/ai-native-engineer.md) · [DevOps·플랫폼](variants/devops-platform.md)

---

## 요약

반도체시스템공학을 전공하고 삼성전자 파운드리사업부 고객디자인지원팀에서 임베디드 소프트웨어, 설계 지원 도구, DevOps 자동화를 담당해 온 엔지니어입니다. ARM Cortex 플랫폼 포팅, Linux 디바이스 드라이버, NPU용 RTOS 개발처럼 하드웨어와 소프트웨어의 경계에서 출발했고, 현재는 사내 LLM API를 활용해 EDA 툴 실행 자동화, 설계 파라미터 값 수집, 툴 로그 파싱·저장 등 반도체 설계 자동화 업무를 수행하며 개발 방식 자체를 바꾸는 일을 합니다.

2026년부터 Claude Code, Codex CLI, Antigravity 세 가지 AI 코딩 에이전트를 실무의 기본 개발 방식으로 전환했습니다. 5개월 동안 사내 풀스택 대시보드(GAIA 2.0), MCP 서버, LLM 게이트웨이, LLM 위키, 에이전트 스킬 허브 같은 AI 인프라를 직접 구축했고, 셀프호스팅 CI 러너와 자율 개발 스택으로 그 과정을 자동화했으며, 팀 세미나 7편으로 방법론을 확산했습니다.

## 한눈에 보는 지표

| 지표 | 값 | 근거 |
|---|---|---|
| AI 에이전트 총 컨텍스트 처리량 | 약 114억 토큰 (11,401,278,027) | 로컬 사용 기록 전수 집계, 2026-09-22 |
| 순수 생성·추론 산출량 | 약 7,251만 토큰 (72,513,989) | 위와 같음 |
| 도구별 처리량 | Claude Code 101.0억 · Antigravity 9.3억 · Codex CLI 3.6억 | 위와 같음 |
| 신규 GitHub 저장소 | 46개 (2026-04 ~ 2026-09) | GitHub 계정 목록 |
| 고유 커밋 | 1,800건 이상 (2026-04 ~ 2026-09, 중복 클론 제외) | 로컬 저장소 git 로그 |
| 셀프호스팅 GitHub Actions 러너 | 20여 개 인스턴스 (CI 전용 + Claude Code 헤드리스 실행 전용) | WSL2 러너 설치 디렉터리 |
| 발표 자료 | 7편 (2026-07 ~ 2026-09, 팀 세미나 포함) | dkdlqoddi.github.io |

---

## 세 가지 관점

### 1. 펌웨어·임베디드 소프트웨어

- ARM Cortex-A/M 플랫폼 대상 소프트웨어 포팅·최적화, Linux 커널 디바이스 드라이버 개발과 안정성 디버깅.
- Rebellions의 4칩렛 통합 NPU **REBEL Quad**용 RTOS 포팅과 디바이스 드라이버 개발에 참여.
- Ubuntu 서버 + Lauterbach Trace32 + Arduino/서보모터로 원격지 개발 보드를 전원·리셋까지 무인 제어하는 디버깅 시스템 구축.
- GNU Radio와 CPython C-API로 레거시 C 모듈을 결합한 SDR 실시간 신호처리 시스템(SEC 연구소).
- NVIDIA Jetson 기반 오프라인 온디바이스 에이전트 실증, Isaac Sim + ROS 2 Humble 로봇 시뮬레이션 환경 구축.

### 2. AI 네이티브 개발 (에이전트 오케스트레이션 · 바이브 코딩)

- 세 가지 에이전트 도구를 병행 운용하며 5개월간 약 114억 토큰의 컨텍스트를 처리. 사내 프로젝트 12개 이상, 개인·오픈소스 프로젝트 20개 이상을 에이전트 주도로 설계·구현·검증.
- 개발 하네스 **dev-env-blindspot**(공개 저장소)을 설계해 15개 이상 프로젝트에 배포: 코드를 쓰기 전에 모르는 것을 질문으로 바꾸는 `blindspot-pass` 스킬, 읽기 전용 `codebase-scanner` 에이전트, 세션 시작 시 규칙을 주입하는 hook, append-only 결정 기록.
- Claude Code가 계획·리뷰(Opus/Fable xhigh)를 맡고 Antigravity(Gemini Flash)가 병렬 실행하는 2-하네스 스웜 워크플로를 설계해 토큰 비용을 판단 지점에만 집중.
- 사내 AI 인프라 구축: 정책 기반 MCP 서버, LLM 게이트웨이 프록시 API 서버, GraphRAG LLM 위키, Agent Skill 공유 허브, 이메일 아카이빙 플랫폼. 현업에서는 사내 LLM API로 EDA 툴 자동화, 파라미터 값 수집, 로그 파싱·저장을 수행.
- 개인 도구: 구독 중인 CLI를 실행 엔진으로 재활용하는 자기학습 오케스트레이터 `cheap-agent`, Antigravity CLI를 OpenAI 호환 API로 감싼 `custom-llm-api`, 스킬 정적·LLM 리뷰 파이프라인 `skill-verifier`.

### 3. DevOps · 플랫폼

- Docker, Jenkins, GitHub Actions, Coverity, Checkpatch를 연계한 반도체 소프트웨어 CI/CD와 정적 분석 자동화(삼성전자).
- WSL2 환경에 셀프호스팅 GitHub Actions 러너 20여 개를 구성·운영. CI 전용 러너와 Claude Code 헤드리스(`claude -p`) 실행 전용 러너를 라벨로 분리.
- 사람의 개입을 PR 머지 승인 하나로 줄인 자율 개발 스택(AI-DLC × SDD × TDD) 설계: 이슈 → 스펙 → 구현 → 검증 → 리뷰 → 출하를 서브에이전트가 수행하고, guard hook·CODEOWNERS·브랜치 보호·액션 SHA 고정으로 집행.
- 폐쇄망 배포(사내 pip 미러, 외부 API 없는 자체 호스팅 벡터 DB), Google Cloud Run + Cloud Storage 배포, Docker Compose + nginx, Streamlit 기반 컨테이너 매니저 운영.

---

## 경력

### 삼성전자 파운드리사업부 고객디자인지원팀 (Samsung Electronics, Foundry Business, Customer Design Support Team)

**임베디드 소프트웨어 엔지니어 · 2022.03 – 현재**

임베디드·시스템 소프트웨어

- ARM Cortex-A/M 플랫폼 타깃 펌웨어·소프트웨어 포팅과 최적화, 주변장치 인터페이스 제어.
- Linux 디바이스 드라이버 작성과 커널 레벨 안정성 이슈 분석·해결.
- Ubuntu 서버와 Trace32 드라이버를 결합한 원격 보드 통합 제어·디버깅 시스템 구축. 소프트웨어로 제어할 수 없는 물리 버튼은 Arduino와 서보모터 암으로 무인화.

설계 지원 도구·데이터 자동화

- 외부 인터넷이 차단된 온프레미스 환경용 반도체 설계 데이터 웹 뷰어를 단독 구축(Next.js, Tailwind CSS, Material-UI, PostgreSQL). 원격 서버 DB 탐색과 설계 데이터 생성·시각화를 지원해 설계 엔지니어의 작업 시간 단축.
- Python(PyQt) 데스크톱 도구와 웹 풀스택(React, TypeScript, Next.js, PostgreSQL)으로 고객사·설계 엔지니어용 칩 설계 분석 도구 개발.
- Python과 SQL로 수작업 반복 분석 워크플로를 자동화.
- **사내 LLM API 기반 반도체 설계 자동화 (현재 업무):** EDA 툴 실행 자동화, 설계 파라미터 값 수집, 툴 로그 파싱과 저장, 설계 자동화 워크플로 구축. 넷리스트 파싱·DB 적재 파이프라인, LangGraph 로그 분석 플로우, EDA 벤더 MCP 3종 하네스가 관련 산출물.

DevOps

- Docker, Jenkins, GitHub Actions, Coverity, Checkpatch를 연계한 CI/CD 파이프라인 구축·유지보수로 검증 주기 단축과 정적 분석 자동화.

2026년 AI 에이전트 기반 개발 전환 (주요 산출물)

- **GAIA 2.0 — 반도체 설계 사인오프 진행 추적 대시보드** (2026-06 ~, 커밋 850건 이상): Next.js 16 App Router 단일 앱, Prisma + PostgreSQL 모델 23개, Route Handler 41개, 모듈 19개. Dashboard(마일스톤별 Score·추세), Task Gantt(인라인 일정 편집), SOP 체크 이행 화면, Run 파생 트리, react-konva 기반 floorplan 편집기, SOP 워크스페이스(XLSX 적재·내보내기), Domain 리포트 이메일 발송, LangGraph 어시스턴트. Playwright e2e·vitest·husky 게이트. 10명이 동시에 Claude Code로 개발할 수 있도록 ADR 66건·요구사항 137건을 3계층 문서로, 다시 결정 기록 표로 단계적 전환.
- **정책 기반 MCP 서버**: 공용 원격 서버의 파일 읽기·쓰기, 관리자 등록 명령·DB 질의·내부 API를 디렉터리별 read/write/command 정책으로 노출하는 MCP 서버(툴 17개). LangGraph 기반 파일 분석 툴, 접근 정책 자체를 조회하는 툴 제공. OpenCode·Claude Code·Codex 클라이언트 지원, 폐쇄망 pip 미러 배포.
- **LLM 게이트웨이 API 서버**: FastAPI로 사내 LLM 게이트웨이(OpenAI 호환)에 자격증명·헤더를 주입하는 프록시, MCP 툴 REST 릴레이, 바이트를 그대로 전달하는 투명 MCP 프로토콜 프록시를 한 서버에 구현. 모델별 프로필·튜닝, mock 기반 소켓 없는 테스트.
- **LLM 위키** (커밋 120건): 원문(raw)은 불변으로 보존하고 Claude Code가 위키 마크다운을 유지하며, Next.js 앱이 GraphRAG + BM25 하이브리드 검색을 제공. 헤드리스 인제스트에 권한 deny 목록을 적용해 프롬프트 인젝션이 소스를 수정하지 못하게 차단.
- **Agent Skill 허브** (커밋 108건): OpenCode 호환 Agent Skill을 공유하는 사내 셀프호스팅 플랫폼. Node.js 22 + SQLite(Drizzle), 릴리스 불변성(버전·ZIP·체크섬), 관리 행위 감사 로그, ZIP 경로 순회 검증, Markdown 살균, Docker + nginx 배포.
- **랜딩 페이지**: Next.js 기반 사내 진입 페이지에 fail-closed SAML 인증과 VoC 워크플로, 3D 컨트롤 적용.
- **사내 이메일 아카이빙 플랫폼**: 로컬 PC의 `.mysingle`/`.eml`을 HTML로 변환·수집·검색하는 Next.js 풀스택 서비스와 Python 수집 클라이언트(서킷 브레이커, 중단 복구, 세션 재사용), XSS 살균·Sandboxed 뷰어.
- **사내 지식 검색**: 사내 Gemma 4 LLM과 BGE-M3 임베딩 엔드포인트, 자체 호스팅 벡터 DB를 전제로 한 하이브리드 의미 검색 설계와 Playwright 크롤링 수집.
- **운영·분석 도구**: LangGraph 로그 분석 플로우, 넷리스트 파싱·DB 파이프라인, 문서 파서 GUI, ASIC 설계 도메인별 SOP 체크리스트 프로토타입, kasm VNC 멀티유저 컨테이너 매니저(Streamlit, sqlite3 해시 점유, 유휴 자동 회수, FastAPI 게이트웨이, 커밋 78건).
- **OpenCode 에이전트 환경**: 에이전트 구성·프롬프트 표준화, EDA 벤더 MCP 3종을 프롬프트로 부리는 반도체 지식 자동화 하네스.
- **팀 세미나 7편** (아래 발표 항목): 설계 AX 전환, 안전한 AI 설계 자동화 아키텍처, DX vs AX, Agent Skills 철학, EDA MCP 하네스, AI 도구 입문, NotebookLM.

### SEC 연구소 시스템개발팀 (SEC Laboratory, System Development Team)

**소프트웨어 개발자 · 2018.01 – 2019.06**

- GNU Radio와 CPython으로 SDR(Software Defined Radio) 실시간 디지털 신호처리 시스템 설계·구현.
- 레거시 C 모듈을 CPython C-API 바인딩과 공유 라이브러리로 GNU Radio 프레임워크에 결합.
- 전국에 분산 배치된 원격 서버와 안테나 자원을 중앙에서 통제·모니터링하는 실시간 제어 자동화 작성.
- 제한된 컴퓨팅 자원의 현장 장비에서 데이터 흐름 병목 제거, 메모리·네트워크 전송 효율 최적화.

---

## 주요 프로젝트

### 오픈소스 · AI 개발 도구 (github.com/dkdlqoddi)

- **dev-env-blindspot** (공개, 2026-07 ~, 커밋 98건): Claude Code · Codex · Antigravity 공용 개발 하네스. `blindspot-pass` 스킬과 `codebase-scanner` 에이전트, SessionStart hook으로 주입되는 MANDATE, append-only `docs/decisions.md`. 서브모듈 한 줄로 설치되며 15개 이상 프로젝트에 적용. 풀 버전(요구사항 인터뷰·설계 문서·머지 전 퀴즈·3계층 문서)에서 비용 실측 후 lite 버전으로 축소, Claude Code가 계획하고 Antigravity가 스웜 실행하는 `claude-antigravity-cowork` 브랜치 운영. 출발점은 Anthropic Thariq의 "A Field Guide to Fable: Finding Your Unknowns".
- **cheap-agent** (v0.4.1): 이미 구독 중인 코딩 에이전트 CLI(Claude Code, Codex, OpenCode, Antigravity)의 headless 모드를 실행 엔진으로 재활용하는 자기학습 오케스트레이터. Python 표준 라이브러리만 사용, 프로세스 간 통신은 파일만, 19개 기능 개별 토글(best-of-N, 세션 재개, 비용 상한, 작업 큐, 회고 기반 lesson 축적), GitHub Actions CI.
- **custom-llm-api**: API 키 없이 로컬 Antigravity CLI(`agy`)를 실행해 Cursor·Continue·LangGraph 등 OpenAI 규격 도구에 연결하는 FastAPI 호환 서버와 검증 스위트.
- **custom-llm-wiki**: raw → wiki 마크다운을 Claude Code 스킬(`/wiki-save`, `/wiki-ask` 등)로 관리하고 Next.js 16 앱이 BM25 + 로컬 e5-small 임베딩 하이브리드 검색과 RAG 채팅을 제공하는 개인 LLM 위키.
- **skill-verifier**: Agent Skill의 정적 검사와 LLM 리뷰를 결합한 스킬 리뷰 파이프라인 v1·v2.
- **librarian-mcp · paper-review**: 락파일로 동기화되는 스킬 라이브러리(36개), 논문 PDF → 메타·요약·개념 노트를 양방향 추적하는 지식 베이스.
- **모델 A/B 벤치마크** (공개 `benchmark-nextjs-opus`, `benchmark-nextjs-fable`, `benchmark-result`): 동일 프롬프트 시퀀스로 Next.js 앱을 구축해 Opus와 Fable의 소요 시간·토큰·결과 품질을 비교·문서화.
- **자율 개발 스택 레퍼런스** (`machine-manager`, `stocker-trade`, `gaia-parser`): AI-DLC × SDD × TDD × BDD 스택(R14-V2). `/issue → /spec → G1 → /bolt → /verify → /review → /ship`을 무중단으로 수행하고 사람은 PR 머지만 담당. 서브에이전트 8종·스킬 7종, guard hook, CI 게이트 필수화, 워크플로 액션 커밋 SHA 고정, 뮤테이션 테스트(Stryker)·Lighthouse 예산.

### 임베디드 · 시스템

- **REBEL Quad RTOS 및 디바이스 드라이버** (Rebellions): 4개 칩렛을 단일 패키지로 집적한 NPU의 안정적 제어와 하드웨어-소프트웨어 고속 상호작용을 위한 RTOS 포팅, 커널 최적화, 드라이버 구현.
- **원격 하드웨어 보드 통합 제어·디버깅 시스템**: Ubuntu Server, Trace32, Arduino, 서보모터.
- **Jetson 기반 오프라인 온디바이스 자율 에이전트**: 클라우드 연결이 불가능한 엣지 환경에서 소형 로컬 언어 모델로 주변 상태를 인지하고 행동하는 독립형 에이전트 구조 설계·실증.
- **로봇 시뮬레이션 환경** (`my-gemini-robotics`): NVIDIA Isaac Sim + ROS 2 Humble 워크스페이스, URDF/USD 기반 디지털 트윈 구성.
- **QEMU 테스트 환경** (2023, C), C++ 클래스 의존성 그래프 생성 스크립트(공개).

### 서비스 · 자동화 (개인)

- **모바일 청첩장**: Next.js, Docker, Google Cloud Run, Cloud Storage. 뉴모피즘 디자인, 제스처 갤러리, BGM 자동재생 처리.
- **교회 홈페이지와 모바일 앱**: Next.js(Cloud Run)와 Flutter 앱을 같은 콘텐츠 모듈로 동기화, 유튜브 라이브 자동 갱신.
- **해외 구매대행 스토어 자동화** (`pycommerce`): 라쿠텐 상품 수집 → Claude API 상품 설명 번역 → Gemini 이미지 내 텍스트 번역 → 네이버 스마트스토어 등록, 중복 등록 차단과 실패 처리.
- **YouTube Shorts 제작 파이프라인** (`pycommerce-youtube`): Claude 대본·제목, Gemini·Veo 영상 생성, Python 합성·자막·업로드, Google AI Studio·Vertex 비용 분리.
- **트레이딩 연구**: TradingView Pine Script 전략 5종(CVD·경계 조건 분석), PyTorch Seq2Seq 30분 OHLC 예측 모델(MongoDB·Parquet), 거래소 API(코인원·바이낸스) 자동매매, Solana 분석 워크스페이스.
- **AI 해커톤 스타터 킷**: Next.js 16, Drizzle/PostgreSQL, 키가 없어도 mock으로 동작하는 DEMO_MODE, 모듈 단위 기능 추가 구조.

---

## 발표 · 세미나 (https://dkdlqoddi.github.io)

| 날짜 | 제목 | 내용 |
|---|---|---|
| 2026-07-31 | 설계 AX 전환 | 프롬프트 엔지니어링에서 Harness 엔지니어링으로 |
| 2026-08-03 | 안전한 AI 설계 자동화 아키텍처 | 망 연동 보안 아키텍처와 AI 파이프라인 작동 구조 |
| 2026-08-19 | Python Automation: DX vs AX (팀 세미나 1부) | 파이프라인의 진화와 사내 LLM 연동 6가지 방법 |
| 2026-08-19 | AI Agent Skills Philosophy (팀 세미나 2부) | 하네스가 결과의 폭을 조이는 원리와 도구 철학 |
| 2026-09-01 | 나만의 돌쇠 AI 만들기 | OpenCode에 연결된 EDA MCP 3종을 프롬프트로 부리는 반도체 지식 자동화 하네스 |
| 2026-09-20 | AI, 한 걸음 더 | Codex · Claude Code · Antigravity 입문 (큰 글씨와 그림으로 배우는 실습) |
| 2026-09-21 | 내 자료가 이해가 되는 순간 | NotebookLM / Gemini Notebook 활용 예시 네 가지와 실습 |

발표 사이트 자체도 빌드 없는 정적 HTML·Reveal.js로 구축했고, Playwright 회귀 검증(탐색·목차·모바일·오프라인·PDF)을 스크립트로 자동화했습니다.

---

## 학력

**성균관대학교 반도체시스템공학과 공학학사** · 2014 – 2022

- 학부 연구생, IRIS Lab (지능형 신뢰성 집적 시스템 연구실, 지도교수 고종환) · 2020.03 – 2022.02
- 연구 논문: *A Proposal for a Weight Changeable Model corresponds to Network Packet Errors* (네트워크 패킷 에러에 대응하는 가중치 가변 신경망 모델 제안) — 코드: https://github.com/dkdlqoddi/Weight-Changable-Model
- 주요 이수: 반도체물성·소자·공정, 디지털논리회로, 아날로그·혼성신호 회로, VLSI 설계(Verilog/SystemVerilog), SoC 설계, 임베디드 시스템, 마이크로프로세서, C/C++ 시스템 모델링, 신뢰성·고장 분석, EDA 설계 자동화(Cadence, Synopsys), 캡스톤 디자인.

---

## 기술 스택

| 분야 | 기술 |
|---|---|
| 언어 | C / C++, Python, TypeScript / JavaScript, Bash, ARM·x86 Assembly, SQL, Dart, Pine Script |
| 임베디드·시스템 | FreeRTOS, Zephyr, Linux Kernel & Device Driver, ARM Cortex-A/M, Lauterbach Trace32, GDB / Ghidra, QEMU, NVIDIA Jetson, Arduino / Raspberry Pi, GNU Radio, ROS 2 Humble / Isaac Sim |
| 웹·애플리케이션 | React, Next.js 16 (App Router / RSC), Tailwind CSS, shadcn/Radix, Prisma, Drizzle, PostgreSQL, SQLite, MySQL, FastAPI, Streamlit, PyQt, Flutter, Playwright, vitest |
| AI·에이전트 | Claude Code, Codex CLI, Antigravity CLI, OpenCode, MCP 서버·클라이언트, LangGraph / LangChain, RAG · GraphRAG (BM25 + 임베딩 하이브리드), Claude · Gemini · OpenAI 호환 API, PyTorch / TensorFlow, 스킬·에이전트·hook 설계 |
| DevOps·클라우드 | Docker / Compose, nginx, Jenkins, GitHub Actions (셀프호스팅 러너), Coverity, Checkpatch, semgrep, Google Cloud Run / Cloud Storage, AWS, Kubernetes, Grafana, WSL2, tmux, uv / pnpm / npm, husky |
| 기타 | Apache Kafka, n8n, Cassandra, Selenium, OpenGL / Panda3D, CMake / Make |

## AI 개발 환경

- 기본 세션: Claude Code (Fable 5.1, 1M 컨텍스트, effort max), 서브에이전트는 Opus. 공식 플러그인 9종(frontend-design, code-review, skill-creator, code-simplifier, playwright, claude-md-management, typescript-lsp, feature-dev, firecrawl)과 claude-mem 사용.
- 병행 도구: Codex CLI(2026-07 ~, 세션 580건 이상), Antigravity CLI(대화 500건 이상), OpenCode, GitHub Copilot.
- 모델 배치 원칙: 계획·리뷰·머지 게이트처럼 판단이 필요한 자리는 Opus/Fable xhigh, 탐색·기계 검사는 Sonnet/Haiku, 대량 병렬 실행은 Gemini Flash. 토큰은 판단에만 쓰고 검사·실행은 hook과 CI(CPU)에 맡깁니다.
- 작업 방식: 계획 → 모르는 것을 결정 가능한 질문으로 정리(최대 4개 일괄) → 승인 → 구현. 결정은 append-only 표에 남겨 다시 묻지 않고, 머지 게이트는 PR 리뷰입니다.
