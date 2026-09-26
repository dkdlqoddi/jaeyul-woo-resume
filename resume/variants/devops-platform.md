# 우제율 (Jae-Yul Woo) — DevOps · 플랫폼 엔지니어

dkdlqoddi@gmail.com · https://github.com/dkdlqoddi · 대한민국

> 마스터 이력서([../resume.md](../resume.md))의 사실을 DevOps·플랫폼 관점으로 재구성한 요약본입니다. 새로운 사실은 없습니다.

## 요약

삼성전자 파운드리사업부에서 Docker · Jenkins · GitHub Actions · Coverity · Checkpatch를 연계한 반도체 소프트웨어 CI/CD를 구축·운영해 온 엔지니어입니다. 2026년에는 WSL2에 셀프호스팅 GitHub Actions 러너 20여 개를 구성해 CI와 AI 에이전트 헤드리스 실행을 분리 운영하고, 사람의 개입을 PR 머지 승인 하나로 줄인 자율 개발 스택을 설계했습니다. 폐쇄망(사내 pip 미러, 외부 API 없는 자체 호스팅)부터 Google Cloud Run까지 배포 환경을 가리지 않으며, 임베디드 출신답게 hook·가드·정책으로 "집행되는" 자동화를 선호합니다.

## 핵심 역량

- **CI/CD**: Jenkins, GitHub Actions(셀프호스팅 러너 라벨 분리·재실행 전략·캐시 정책), Coverity·Checkpatch·semgrep 정적 분석, husky + lint-staged 로컬 게이트, Playwright e2e·vitest·Stryker 뮤테이션 테스트·Lighthouse 예산을 필수 체크로 연결.
- **자율 개발 스택 설계** (R14-V2): 이슈 → 스펙 → 구현 → 검증 → 리뷰 → 출하를 서브에이전트가 무중단으로 수행. guard hook이 보호 경로·위험 명령을 차단하고, CODEOWNERS·브랜치 보호·rulesets, 워크플로 액션 커밋 SHA 고정(공급망 강화), AMEND 마커 기반 자기 개조 게이트로 집행.
- **컨테이너·배포**: Docker / Compose, nginx 리버스 프록시(사내 스킬 허브), Google Cloud Run + Cloud Storage(청첩장·교회 홈페이지), Streamlit 기반 kasm VNC 컨테이너 매니저(포트 풀 할당, sqlite 해시 점유, `docker exec` 접속자 감시 후 유휴 자동 회수, FastAPI 게이트웨이).
- **폐쇄망·보안 운영**: 사내 pip 미러 배포, 외부 API 없는 자체 호스팅 벡터 DB, fail-closed SAML 인증, 디렉터리별 read/write/command 정책의 MCP 서버, 릴리스 불변성(버전·ZIP·체크섬)과 감사 로그, ZIP 경로 순회 검증, 헤드리스 에이전트 권한 deny 목록.
- **인프라 자동화**: Ubuntu 서버 + Trace32 + Arduino로 원격 하드웨어 보드 무인 운영, tmux 세션·러너 부트스트랩 스크립트, Python·SQL 반복 분석 자동화, Grafana 모니터링.
- **AI 에이전트 운영**: Claude Code 전용 셀프호스팅 러너 3대에서 `claude -p` 헤드리스 실행(OAuth 토큰), 토큰 사용률 임계치에 따른 도구 전환 기준, 세 가지 에이전트 도구의 로컬 사용 기록을 전수 집계하는 스크립트.

## 경력

**삼성전자 파운드리사업부 고객디자인지원팀 · 임베디드 소프트웨어 엔지니어 · 2022.03 – 현재**

- Docker, Jenkins, GitHub Actions, Coverity, Checkpatch를 연계한 CI/CD 파이프라인 구축·유지보수로 반도체 소프트웨어 검증 주기 단축과 정적 분석 자동화.
- Python·SQL 기반 반복 분석 워크플로 자동화, 온프레미스(인터넷 차단) 환경용 설계 데이터 웹 뷰어 단독 구축(Next.js, PostgreSQL).
- 현재 사내 LLM API를 활용한 EDA 툴 실행 자동화, 설계 파라미터 값 수집, 툴 로그 파싱·저장 파이프라인 등 반도체 설계 자동화 업무 수행.
- Ubuntu 서버 + Trace32 + Arduino/서보모터로 원격 보드 통합 제어·디버깅 시스템 구축(무인 운영).
- 2026년 AI 인프라 운영: 정책 기반 MCP 서버와 LLM 게이트웨이 API 서버(폐쇄망 pip 미러 배포), Agent Skill 허브(Docker + nginx, SQLite, 감사 로그), LLM 위키(헤드리스 인제스트 권한 제한), fail-closed SAML 랜딩 페이지, 이메일 아카이빙 플랫폼(서킷 브레이커·중단 복구 수집 클라이언트).
- **GAIA 2.0** 풀스택 대시보드(Next.js 16, Prisma/PostgreSQL, 커밋 850건 이상) 운영: 러너 2대 병렬 CI(품질·e2e 잡), 워크트리 기반 스크래치 빌드, 릴리스·DB 마이그레이션 절차 문서화, 10인 동시 개발을 위한 결정 기록 체계.
- ARM Cortex-A/M 포팅과 Linux 디바이스 드라이버 개발(임베디드 본연 업무).

**SEC 연구소 시스템개발팀 · 소프트웨어 개발자 · 2018.01 – 2019.06**

- 전국에 분산 배치된 원격 서버·안테나 자원을 중앙에서 통제·모니터링하는 실시간 제어 자동화 작성, 저자원 장비의 데이터 흐름·전송 효율 최적화.

## DevOps 프로젝트

- **셀프호스팅 GitHub Actions 러너 20여 개** (WSL2): 프로젝트별 러너 디렉터리와 `run.sh` 부트스트랩, 라벨 없는 러너 간 재실행 배정 특성, `clean:false` 작업 폴더 캐시 오염(`git clean -xfd`), npm 캐시 제거, Turbopack dev 캐시 이슈 등 운영 노하우를 결정 기록으로 축적. 요금 한도 블록·PR 충돌로 run이 생성되지 않는 두 원인을 진단 절차로 문서화.
- **자율 개발 스택 레퍼런스** (`machine-manager`, `stocker-trade`, `gaia-parser`): AI-DLC × SDD × TDD × BDD. 사람은 PR 머지만, 나머지는 서브에이전트 8종·스킬 7종. 모든 워크플로 액션을 커밋 SHA로 고정, 게이트 잡 필수화, 무중단 운영 원칙.
- **dev-env-blindspot** (공개): 서브모듈 한 줄 설치 스크립트(`install.sh`)가 심링크·settings hook·ANTIGRAVITY.md import를 멱등하게 구성. 15개 이상 프로젝트에 배포, 검증 스크립트 `test/check.sh`.
- **cheap-agent**: 파일 기반 IPC와 상태 폴링으로 headless CLI 워커를 병렬 스폰하는 오케스트레이터, 비용 상한·재시도·작업 큐 데몬, GitHub Actions CI(py3.10/3.12), 태그 릴리스.
- **custom-llm-api**: Antigravity CLI를 OpenAI 호환 API로 노출하는 FastAPI 서버와 자동 검증 스위트(pre-flight 진단).
- **클라우드 배포**: Next.js 앱을 Docker 이미지로 Google Cloud Run에 배포하고 미디어는 Cloud Storage로 분리(모바일 청첩장, 교회 홈페이지 + Flutter 앱).
- **발표 사이트 운영** (dkdlqoddi.github.io): 빌드 없는 정적 사이트, 정적 자산 무결성 검증 스크립트, Playwright 브라우저 회귀 검증(탐색·모바일·오프라인·PDF), CDN 의존성 배제.

## 기술 스택

- **CI/CD·품질**: GitHub Actions(셀프호스팅), Jenkins, Coverity, Checkpatch, semgrep, husky / lint-staged, Playwright, vitest, Stryker, Lighthouse CI
- **컨테이너·클라우드**: Docker / Compose, nginx, Google Cloud Run / Cloud Storage, AWS, Kubernetes, Streamlit 컨테이너 매니저
- **런타임·패키징**: Node.js(nvm, pnpm, npm, bun), Python(uv, pip 미러), Ruby gems, WSL2, tmux
- **데이터·백엔드**: PostgreSQL(Prisma, Drizzle), SQLite, MySQL, MongoDB, FastAPI, Next.js Route Handlers
- **관측·자동화**: Grafana, Python·SQL·Bash 스크립팅, 로컬 사용 기록 집계(JSONL·SQLite·protobuf 파싱)
- **AI 운영**: Claude Code 헤드리스, Codex CLI, Antigravity CLI, OpenCode, MCP, LangGraph, 모델 배치·토큰 비용 정책

## 학력·배경

성균관대학교 반도체시스템공학 학사(2014 – 2022), IRIS Lab 학부 연구생. 임베디드·AI 관점은 [펌웨어·임베디드](firmware-embedded.md)와 [AI 네이티브 개발자](ai-native-engineer.md) 요약본을 참고하세요.
