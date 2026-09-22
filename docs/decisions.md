# 결정 기록

<!-- Append-only: one decision per row, one line per row, newest at the bottom; supersede a row by appending a new one instead of editing it. 영역: frontend, backend, core, or a module name. 결정 주체: 사용자 or 자체. Every row starts with "| 20" so grep finds it. -->

| 날짜 | 영역 | 결정 | 근거 | 기각한 대안 | 결정 주체 |
|---|---|---|---|---|---|
| 2026-09-22 | token-metrics | Claude Code, Codex, Antigravity 3개 도구의 누적 토큰 사용량을 로컬 DB/로그(stats-cache.json, rollout jsonl, conversations/*.db)에서 직접 전수 집계하기로 결정 | 로컬 파일에 각 도구의 턴별/모델별 정밀 토큰 메타데이터(입력, 캐시, 출력, 추론)가 100% 보관되어 있어 외부 API나 웹 스크래핑 없이 정확한 집계 가능 | 웹 대시보드 눈대중 확인, 단순 추정치 기재 | 자체 |
| 2026-09-22 | resume-metric | 이력서에 총 컨텍스트 처리량(약 114억 토큰)과 순수 생성/추론량(약 7,200만 토큰)을 병기 표기하기로 결정 | 에이전트 오케스트레이션 컨텍스트 규모와 실제 코드/추론 산출 규모를 입체적으로 증명하여 신뢰성과 임팩트 극대화 | 총 처리량 단독 표기, 순수 생성량 단독 표기 | 사용자 |
| 2026-09-22 | tooling | 3개 도구의 로컬 데이터를 분석해 누적 토큰을 자동 계산하는 통합 집계 스크립트(scripts/aggregate_tokens.py)를 생성하기로 결정 | 향후 지속적인 이력서 업데이트 및 최신 토큰 현황 파악을 자동화하고 데이터 신뢰성을 보장하기 위함 | 일회성 수동 계산 후 텍스트 하드코딩 | 사용자 |
