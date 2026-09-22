# 결정 기록

<!-- Append-only: one decision per row, one line per row, newest at the bottom; supersede a row by appending a new one instead of editing it. 영역: frontend, backend, core, or a module name. 결정 주체: 사용자 or 자체. Every row starts with "| 20" so grep finds it. -->

| 날짜 | 영역 | 결정 | 근거 | 기각한 대안 | 결정 주체 |
|---|---|---|---|---|---|
| 2026-09-22 | token-metrics | Claude Code, Codex, Antigravity 3개 도구의 누적 토큰 사용량을 로컬 DB/로그(stats-cache.json, rollout jsonl, conversations/*.db)에서 직접 전수 집계하기로 결정 | 로컬 파일에 각 도구의 턴별/모델별 정밀 토큰 메타데이터(입력, 캐시, 출력, 추론)가 100% 보관되어 있어 외부 API나 웹 스크래핑 없이 정확한 집계 가능 | 웹 대시보드 눈대중 확인, 단순 추정치 기재 | 자체 |
| 2026-09-22 | resume-metric | 이력서에 총 컨텍스트 처리량(약 114억 토큰)과 순수 생성/추론량(약 7,200만 토큰)을 병기 표기하기로 결정 | 에이전트 오케스트레이션 컨텍스트 규모와 실제 코드/추론 산출 규모를 입체적으로 증명하여 신뢰성과 임팩트 극대화 | 총 처리량 단독 표기, 순수 생성량 단독 표기 | 사용자 |
| 2026-09-22 | tooling | 3개 도구의 로컬 데이터를 분석해 누적 토큰을 자동 계산하는 통합 집계 스크립트(scripts/aggregate_tokens.py)를 생성하기로 결정 | 향후 지속적인 이력서 업데이트 및 최신 토큰 현황 파악을 자동화하고 데이터 신뢰성을 보장하기 위함 | 일회성 수동 계산 후 텍스트 하드코딩 | 사용자 |
| 2026-09-22 | routing | 이력서를 서브 경로(/resume/index.html)에 독립 페이지로 배치하고 상단 네비게이션으로 발표자료와 상호 연결하기로 결정 | 기존 발표 아카이브와 회귀 테스트(verify_theme.cjs) 무결성을 보존하고 다중 콘텐츠 진입점 분리 | 루트(/) 이력서 전면 전환, 단일 페이지 통합 | 사용자 |
| 2026-09-22 | i18n | 이력서 본문(경력, 프로젝트, 자기소개 등)을 한국어로 자연스럽게 번역 및 정돈하여 발표 사이트와 언어 일관성을 확보하기로 결정 | 발표 사이트(html lang="ko") 및 기 결정된 한국어 토큰 메트릭과의 톤앤매너 일치 및 국내 채용 가독성 최적화 | 영문 원본 단독 유지, 한영 전환 탭 구성 | 사용자 |
| 2026-09-22 | privacy | 공개 웹 이력서에서 개인 휴대전화 번호는 제외하고 이메일(dkdlqoddi@gmail.com)과 GitHub 프로필만 공개하기로 결정 | 공개 GitHub Pages 호스팅 시 웹 크롤러의 무차별 수집 및 개인정보 유출, 스팸 위험 차단 | 휴대전화 번호 평문 노출, 마스킹 노출 | 사용자 |
| 2026-09-22 | styling | dkdlqoddi.github.io의 공통 디자인 토큰(assets/theme.css)과 Pretendard 로컬 글꼴, Light 모드 체계를 엄격히 준수하고 외부 CDN 의존성을 완전 배제하기로 결정 | verify_deck.py 정적 자산 무결성 검증 통과 및 사이트 전체 시각적 일관성 유지 | 원본 Jekyll 이력서의 다크모드(darkmode: true) 유지, FontAwesome 외부 CDN 로드 | 자체 |
| 2026-09-22 | export-print | 이력서 전용 @media print 인쇄 스타일(A4 맞춤 여백, 페이지 분할 방지, 네비게이션 숨김) 및 상단 'PDF 인쇄/저장' 버튼을 기본 제공하기로 결정 | 채용 담당자의 인쇄 및 PDF 저장 니즈를 충족하고 출력 시 레이아웃 깨짐 방지 | 인쇄 전용 스타일 미지원, 별도 수동 PDF 업로드 관리 | 자체 |
| 2026-09-22 | asset-optimization | 원본 프로필 사진(jaeyul_woo_image.jpg)을 웹 규격에 맞게 500x500 WebP/압축 JPG로 최적화하여 dkdlqoddi.github.io/assets/images/에 배치하기로 결정 | 2.4MB 원본 고용량으로 인한 페이지 로딩 지연 및 CLS 저해 방지 | 2.4MB 원본 직접 참조, 사진 생략 | 자체 |
| 2026-09-22 | metrics-automation | aggregate_tokens.py에 JSON 산출 기능 및 Antigravity DB 읽기 전용 모드(mode=ro)를 적용하고 이력서 UI에 2026-09-22 집계 기준 시점을 명시하기로 결정 | 활성 에이전트 동시성 락(locked) 오류 방지 및 정적 사이트 내 토큰 수치 최신화 신뢰성 확보 | 활성 세션 DB 무시 오류 방치, 수동 텍스트 주입 | 자체 |
