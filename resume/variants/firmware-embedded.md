# 우제율 (Jae-Yul Woo) — 임베디드 소프트웨어 · 펌웨어 엔지니어

dkdlqoddi@gmail.com · https://github.com/dkdlqoddi · 대한민국

> 마스터 이력서([../resume.md](../resume.md))의 사실을 펌웨어·임베디드 관점으로 재구성한 요약본입니다. 새로운 사실은 없습니다.

## 요약

반도체시스템공학 전공(VLSI·SoC 설계, 임베디드 시스템)을 바탕으로 삼성전자 파운드리사업부에서 ARM Cortex-A/M 플랫폼 포팅, Linux 디바이스 드라이버, NPU용 RTOS 개발을 수행해 온 임베디드 소프트웨어 엔지니어입니다. SDR 신호처리(GNU Radio + C-API 바인딩)부터 Trace32 기반 원격 보드 무인 디버깅, Jetson 온디바이스 에이전트까지 하드웨어와 맞닿은 소프트웨어를 다뤄 왔고, 최근에는 AI 코딩 에이전트와 셀프호스팅 CI로 펌웨어 주변의 도구와 검증 환경을 자동화하고 있습니다.

## 핵심 역량

- **플랫폼 포팅·드라이버**: ARM Cortex-A/M 타깃 펌웨어·소프트웨어 포팅과 최적화, 주변장치 인터페이스 제어, Linux 커널 디바이스 드라이버 작성과 안정성 이슈 분석.
- **RTOS**: FreeRTOS · Zephyr, Rebellions REBEL Quad(4칩렛 통합 NPU)용 RTOS 포팅·커널 최적화·드라이버 구현 참여.
- **디버깅·검증 인프라**: Lauterbach Trace32, GDB / Ghidra, QEMU. Ubuntu 서버 + Trace32 드라이버 + Arduino·서보모터로 원격지 보드의 전원·리셋까지 무인 제어하는 통합 디버깅 시스템 구축.
- **신호처리·네이티브 연동**: GNU Radio 기반 SDR 실시간 처리, 레거시 C 모듈을 CPython C-API와 공유 라이브러리로 결합, 저자원 장비의 데이터 흐름·메모리·전송 효율 최적화.
- **엣지 AI·로보틱스**: NVIDIA Jetson 오프라인 온디바이스 에이전트 실증, Isaac Sim + ROS 2 Humble 로봇 시뮬레이션 환경(URDF/USD) 구축.
- **정적 분석·CI**: Coverity, Checkpatch, Jenkins, GitHub Actions를 펌웨어 검증 주기에 연계.

## 경력

**삼성전자 파운드리사업부 고객디자인지원팀 · 임베디드 소프트웨어 엔지니어 · 2022.03 – 현재**

- ARM Cortex-A/M 플랫폼 타깃 펌웨어·소프트웨어 포팅·최적화와 주변장치 인터페이스 제어.
- Linux 디바이스 드라이버 개발과 커널 레벨 안정성 이슈 분석·해결.
- Ubuntu Server + Trace32 + Arduino/서보모터 원격 보드 통합 제어·디버깅 시스템 구축(무인 원격 운영).
- Docker · Jenkins · GitHub Actions · Coverity · Checkpatch 연계 CI/CD와 정적 분석 자동화로 검증 주기 단축.
- 설계 엔지니어용 온프레미스 데이터 뷰어(Next.js, PostgreSQL)와 PyQt 데스크톱 분석 도구 개발.
- 현재 사내 LLM API를 활용한 EDA 툴 실행 자동화, 설계 파라미터 값 수집, 툴 로그 파싱·저장 등 반도체 설계 자동화 업무 수행.
- 2026년: AI 코딩 에이전트(Claude Code · Codex · Antigravity) 기반으로 사내 대시보드·MCP 서버·LLM 게이트웨이 등 12개 이상의 프로젝트 구축, 셀프호스팅 CI 러너 20여 개 운영, 팀 세미나 7편 발표.

**SEC 연구소 시스템개발팀 · 소프트웨어 개발자 · 2018.01 – 2019.06**

- GNU Radio + CPython으로 SDR 실시간 디지털 신호처리 시스템 설계·구현.
- 레거시 C 파일을 CPython 바인딩·동적 라이브러리로 GNU Radio에 결합.
- 전국 분산 서버·안테나 자원의 중앙 제어·모니터링 자동화, 저자원 환경 성능 최적화.

## 임베디드 프로젝트

- **REBEL Quad RTOS·디바이스 드라이버** (Rebellions): 4칩렛 단일 패키지 NPU의 안정적 제어와 하드웨어-소프트웨어 고속 상호작용을 위한 RTOS 포팅, 커널 최적화, 드라이버 구현.
- **원격 하드웨어 보드 통합 제어·디버깅 시스템**: 순수 소프트웨어 신호로 제어할 수 없는 물리 버튼을 Arduino·서보 암으로 무인화.
- **Jetson 오프라인 온디바이스 자율 에이전트**: 클라우드 연결이 불가능한 엣지 환경에서 소형 로컬 언어 모델(SLM/VLM)로 주변 상태를 인지하고 행동하는 독립형 구조 설계·실증.
- **Isaac Sim + ROS 2 로봇 시뮬레이션 환경**: 디지털 트윈에서 로봇 조립·구동·센서(카메라·LiDAR) 테스트.
- **QEMU 테스트 환경** (2023) · **C++ 클래스 의존성 그래프 생성 스크립트** (공개).

## 학력

**성균관대학교 반도체시스템공학과 공학학사 · 2014 – 2022**

- IRIS Lab 학부 연구생(지도교수 고종환, 2020.03 – 2022.02). 논문: *A Proposal for a Weight Changeable Model corresponds to Network Packet Errors*.
- 반도체물성·소자·공정, 디지털논리회로, 아날로그·혼성신호 회로, VLSI 설계(Verilog/SystemVerilog), SoC 설계, 임베디드 시스템, 마이크로프로세서, C/C++ 시스템 모델링, 신뢰성·고장 분석, EDA(Cadence, Synopsys).

## 기술 스택

- **언어**: C / C++, ARM·x86 Assembly, Python, Bash, TypeScript
- **RTOS·커널**: FreeRTOS, Zephyr, Linux Kernel & Device Driver, ARM Cortex-A/M
- **디버깅·검증**: Lauterbach Trace32, GDB, Ghidra, QEMU, Coverity, Checkpatch
- **보드·플랫폼**: NVIDIA Jetson, Arduino, Raspberry Pi, GNU Radio(SDR), ROS 2 Humble, Isaac Sim
- **빌드·CI**: CMake / Make, Docker, Jenkins, GitHub Actions(셀프호스팅 러너)
- **HW 설계 이해**: Verilog / SystemVerilog, SoC 설계, Cadence / Synopsys EDA

## AI 도구 활용

Claude Code · Codex CLI · Antigravity를 실무 도구로 사용합니다(5개월 누적 컨텍스트 약 114억 토큰). 공용 개발 하네스 dev-env-blindspot(공개)을 설계·배포했고, 계획·리뷰는 고성능 모델에, 병렬 실행은 경량 모델에 배치해 비용을 관리합니다. 자세한 내용은 [AI 네이티브 개발자 관점](ai-native-engineer.md)을 참고하세요.
