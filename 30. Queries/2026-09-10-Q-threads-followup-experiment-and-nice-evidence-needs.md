---
type: query-result
aliases:
  - NICE Threads 후속 실험 실행 기록
  - 질문축적실험 시간축·예산 증거 질문
description: "Execution record for the prospective Threads format experiment and the remaining budget and timeline evidence needed for the NICE essay."
author:
  - Codex
date created: 2026-09-10
date modified: 2026-09-10
tags:
  - query
  - scholarship
  - data-analysis
  - experiment
  - threads
source:
  - https://github.com/gyutaetae/threads-agentic-editor-workflow
  - "[[harness]]"
  - "[[2026-09-09-Q-nice-scholarship-essay-draft-v2]]"
  - "[[2026-09-10-Q-nice-five-criteria-readiness-rescore]]"
reusableFor:
  - 장학금 자기소개서
  - 프로젝트 증거
  - 취업/포트폴리오
confidence: medium
---

# Threads 후속 실험 실행과 NICE 추가 증거 질문

## 현재 실행 결과

2026-09-10 원격 `master`의 최신 커밋 `5cd9f61`과 `threads-post-metrics.csv`를 확인했다. CSV는 53개 행이며, 이 중 50개가 조회수 양수이면서 72시간 관측을 완료했다. 공개 permalink에서 형식을 확인한 7월 15일 글을 override로 더해 `나쁜 요청·좋은 요청` 대비 형식 32개를 다시 계산했다.

- 초기 16개 중앙 독자 참여율: `1.0054%`
- 후기 16개 중앙 독자 참여율: `0.3700%`
- 중앙값 변화: `-63.2%`
- 계산식: `(좋아요 + 독자답글 + 재게시 + 인용) / 조회수 × 100`

기존 수치는 재현됐다. 그러나 이는 시간순 초기·후기 비교이며 주제, 도달 범위, 플랫폼 노출이 달라 형식 피로를 원인으로 확정할 수 없다.

## 후속 실험 상태

저장소에 다음 산출물을 추가했다.

- `experiments/nice_followup/analyze.py`: 기존 결과 재현과 후속 쌍 비교
- `experiments/nice_followup/experiment-plan.csv`: 6쌍·12개 교차 게시 계획
- `experiments/nice_followup/classification-overrides.csv`: 공개 본문으로 확인한 분류 override
- `experiments/nice_followup/drafts/pair01-contrast.txt`: 대비 형식 첫 문안
- `experiments/nice_followup/drafts/pair01-direct.txt`: 직접 체크리스트 형식 첫 문안
- `experiments/nice_followup/validate_drafts.py`: 4개 part, 500자, 출처 위치, 형식 차이, 길이 차이 검증
- `experiments/nice_followup/results/`: 재현 표·차트·보고서
- `tests/test_nice_followup_analysis.py`: 6쌍 판정과 분류 테스트

검증 결과는 테스트 `2 passed`, 첫 쌍의 전체 길이 차이 `2.5%`다. 현재 새 실험 라벨로 72시간 수집을 끝낸 게시물은 `0개`, 완성된 쌍은 `0/6`이다. 따라서 현재 정확한 표현은 `후속 실험을 설계하고 첫 비교 문안을 준비했다`다. 공개 게시와 72시간 수집 전에는 완료했다고 쓰지 않는다.

## 실험 규칙

- A: `나쁜 요청·좋은 요청`을 명시적으로 대비
- B: 같은 문제를 대비 문구 없이 진단표·체크리스트로 직접 제시
- 같은 주제 축, 같은 저녁 시간, 같은 72시간 관측창, 비슷한 길이와 출처 수준 유지
- 6개 쌍 중 한 형식이 4쌍 이상 이기고 참여율 차이 중앙값이 `0.20%p` 이상일 때만 우선 형식을 변경
- 기준을 넘지 못하면 결론을 보류하고 두 형식을 주제에 따라 병행

이는 플랫폼이 사용자 무작위 분할 A/B를 제공하는 실험이 아니라 한 계정의 순차 교차 게시 준실험이다.

## 예산 산출 근거를 만들기 위해 필요한 사용자 정보

### 2026년 2학기 200만 원

1. 실제 수강할 데이터 분석·SQL 교육의 과정명, 가격, 수강 기간
2. 수집·정제·시각화 환경에서 사용할 서비스명과 월 비용·개월 수
3. 전문가 멘토링 횟수와 회당 예상 금액 또는 실제 견적
4. 보고서·대시보드·배포에 사용할 도메인, 호스팅, 디자인·출력 항목의 단가
5. 교통·식비 60만 원의 이동 구간, 월 이동 횟수, 왕복 교통비, 1회 식비

### 2027년 1학기 300만 원

1. 금융 데이터 교육 과정명과 수강료
2. DB·클라우드·모니터링의 제품명, 월 비용, 운영 개월 수
3. 주문 장애 실험에 실제 비용이 드는 항목과 무료 Upbit 공개 API를 구분한 내역
4. 사용자 검증 인원, 방식, 사례비와 전문가 피드백 횟수
5. 대시보드·배포·포트폴리오의 도메인·서버·출력 단가
6. 교통·식비는 2학기와 같은 월 20만 원 근거를 쓰는지 여부

## 질문·축적·실험의 시간축에 필요한 사용자 정보

다음 다섯 날짜 또는 학기를 순서대로 확인하면 된다.

1. 학기 학점 `3.42`를 받은 연도·학기
2. Gemini Gem을 힌트 튜터로 쓰기 시작한 연도·학기
3. 학기 학점 `4.10`을 받은 연도·학기
4. LLM Wiki를 처음 만들고 기록을 축적하기 시작한 연월
5. Threads 자동화와 Upbit 주문 추적 프로젝트를 각각 시작한 연월

추가로 `3.42 이후 공부 방식에서 실제로 바꾼 것`을 Gemini 외에 1~2개만 확인해야 한다. 그래야 Gemini 하나가 성적 상승의 단일 원인처럼 보이지 않고 `질문 방식 변화→지식 축적→프로젝트 실험`의 발전 순서를 만들 수 있다.

> [!note] Bias Check
> 분석 코드·실험 계획·첫 비교 문안은 Codex가 작성했다. 사용자는 기존 52개 원자료를 직접 Python·Pandas로 정제했다고 보고했지만 이번 후속 실험 코드를 직접 작성한 것으로 간주하지 않는다. 사용자가 코드, 분류 기준, 계산식과 결과를 직접 검산하고 설명해야 본인 분석 증거가 된다. 공개 게시물은 아직 생성하지 않았으며 72시간 후속 결과도 없다.

## Reuse Axis

- 장학금 자기소개서: 완료된 분석과 진행 중 실험의 경계를 지킨 4번 문항
- 프로젝트 증거: 재현 코드·계획표·첫 비교 문안·자동 판정 보고서
- 취업/포트폴리오: AI 작성 범위와 사용자 검증 범위를 분리한 데이터 실험 사례
