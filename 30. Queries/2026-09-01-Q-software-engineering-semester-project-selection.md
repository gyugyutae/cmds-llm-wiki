---
type: query-result
aliases:
  - 소프트웨어개발론 학기 프로젝트 주제 선정
description: "A portfolio-oriented comparison of feasible 12-week software engineering projects in drone traceability and Upbit-based investment systems."
author:
  - Codex
date created: 2026-09-01
date modified: 2026-09-01
tags:
  - query
  - semester-project
  - traceability
  - drone
  - finance
source:
  - gnu-lee-se-w01-syllabus_v022.pdf
  - "[[Core Context]]"
  - "[[Graduation-elasticsearch]]"
  - "[[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]"
  - "[[백테스트 과적합과 편향]]"
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 프로젝트 증거
  - 학부연구생/학술
confidence: medium
status: active
---

# 소프트웨어개발론 3개월 프로젝트 주제 선정

## 결론

1순위는 **무인기 임무 디지털 스레드 및 안전 추적성 플랫폼**이다. 요구사항, 비행 계획, 텔레메트리 이벤트, 안전 규칙, 테스트 결과를 하나의 trace graph로 연결하고 변경 영향과 미충족 항목을 보여주는 웹 시스템이다.

2순위는 **Upbit 공개 시세 기반 맞춤형 적립식 투자 정책 시뮬레이터**다. 자동 실거래가 아니라 사용자가 정한 적립 규칙의 비용 포함 백테스트, paper portfolio, 실행 설명과 위험 경고를 제공한다.

순수 알고리즘 자동매매 봇은 실거래 안전·성과 검증·과적합·보안 범위가 한 학기 프로젝트의 소프트웨어공학 산출물을 압도하므로 우선순위가 낮다.

## 강의 적합 기준

강의계획서가 요구하는 핵심은 인터뷰 가능한 사용자, 8주차 작동 데모, 요구사항명세·계획·기술 프로토타입, 내부 구조, UML, SOLID, 테스트, CI, 최종 시험 보고서다. 따라서 모델 정확도나 투자수익보다 여러 행위자와 검증 가능한 workflow가 있는 주제가 유리하다.

| 후보 | 수업 적합 | 12주 완수 | 사업 가치 | 포트폴리오 차별성 | 위험 |
|---|---:|---:|---:|---:|---:|
| 무인기 임무 디지털 스레드 | 5 | 4 | 4 | 5 | 3 |
| 맞춤형 적립식 정책 시뮬레이터 | 4 | 5 | 4 | 4 | 2 |
| Upbit 자동 실거래 알고리즘 봇 | 3 | 2 | 3 | 3 | 5 |
| 범용 요구사항-코드 추적 SaaS | 4 | 4 | 3 | 4 | 3 |

## 1순위 MVP

### 사용자와 문제

- 1차 사용자: SEALAB 연구자, 무인기 프로젝트 학생팀, 시험 담당자
- 문제: 요구사항이 어느 비행 계획·로그·테스트로 검증됐는지 흩어져 있어 변경 영향과 누락을 찾기 어렵다.
- 핵심 가치: `REQ → mission rule → telemetry evidence → TEST → result`를 한 화면에서 추적한다.

### 8주차 데모

1. CSV/JSON 요구사항과 MAVLink 형식의 시뮬레이션 비행 로그를 업로드한다.
2. 고도·배터리·geofence 규칙을 자동 평가한다.
3. 지도와 타임라인에서 위반 시점을 재생한다.
4. 요구사항별 연결된 테스트와 증거를 보여주고 미검증 항목을 표시한다.
5. 한 요구사항을 변경하면 영향받는 규칙·테스트·임무를 보여준다.

### 기술과 경계

- React/TypeScript UI, Java Spring Boot 또는 Python FastAPI, PostgreSQL/PostGIS
- MAVLink/PX4 SITL 또는 미리 생성한 로그; 실제 드론 하드웨어와 실외 비행은 MVP에서 제외
- trace link는 규칙 기반 명시 연결부터 구현하고, LLM은 후보 링크·사고 요약을 제안할 뿐 자동 확정하지 않는다.
- Neo4j는 프로토타입에서 관계 질의가 실제로 단순해질 때만 도입한다. 초기에는 PostgreSQL 관계 테이블로 충분하다.
- 최신 기술은 MAVLink telemetry, geospatial DB, OpenTelemetry, GitHub Actions와 artifact provenance를 선택적으로 연결한다.

### 검증 지표

- 사전에 만든 위반 20건의 탐지 precision/recall
- 요구사항 변경 영향 분석의 정답 대비 정확도
- 로그 업로드부터 결과 표시까지 처리시간과 p95
- 사용자 3~5명이 특정 위반의 근거를 찾는 데 걸린 시간 및 SUS 또는 과업 성공률
- 주요 도메인 규칙 단위 테스트, 핵심 use case 통합 테스트, CI 통과율

## 2순위 MVP

맞춤형 적립식 투자 정책 시뮬레이터는 `매주/매월 기본 매수 + 이동평균·하락률 조건별 추가 매수 + 현금 한도 + 수수료`를 정책 객체로 만들고, 동일 기간의 단순 DCA와 비교한다.

- 공개 시세 수집, 정책 작성 UI, 비용 포함 백테스트, paper portfolio, 실행 근거 audit log
- walk-forward 또는 고정된 미사용 기간, 실패한 설정 기록, 수수료·슬리피지 포함
- 실제 주문은 제외하거나 마지막 stretch goal로 두며 기본값은 test order/paper mode
- 수익 보장·매수 추천이 아니라 정책 재현성과 위험 비교를 제품 가치로 둔다.

## 12주 범위

| 기간 | 완료 기준 |
|---|---|
| 1~2주 | 사용자 3명 인터뷰, 문제·데모 시나리오, context/use-case diagram, GitHub 이슈 |
| 3~4주 | 요구사항명세, 데이터 모델, 기술 spike, walking skeleton |
| 5~6주 | 핵심 업로드/판정/조회 vertical slice, sequence/class diagram |
| 7~8주 | 작동 데모, 품질 시나리오, 중간 발표, 범위 동결 |
| 9~10주 | 2차 기능, SOLID 리팩터링, observability, CI |
| 11주 | 핵심 규칙 단위·통합 테스트와 오류 주입 |
| 12주 | 사용자 평가, 시험 보고서, 최종 데모와 회고 |

## 포트폴리오 증거 설계

- 직접 작성한 핵심 도메인 규칙과 테스트를 별도 표시한다.
- AI가 생성한 코드, 본인이 수정한 판단, 검증 결과를 주별로 분리 기록한다.
- 요구사항 ID와 issue, commit, test, demo evidence를 연결한다.
- 성공 화면뿐 아니라 잘못된 로그·누락 링크·규칙 변경이 어떻게 실패하고 복구되는지 시연한다.

이 선택은 [[Graduation-elasticsearch]]의 traceability 연구를 실제 사용자 workflow로 확장하고, 아직 부족한 직접 구현 증거를 만들 수 있다는 점에서 현재 포트폴리오 공백과 가장 잘 맞는다.

신기술 선정과 구현 경계는 [[2026-09-01-Q-emerging-traceability-technology-selection]]에서 구체화했다.

> [!note] Bias Check
> 무인기 주제의 사업성은 실제 연구실·운영자 인터뷰 전까지 가설이다. 규제 준수 제품이나 실제 비행 안전 시스템으로 주장하지 않으며, 학기 MVP는 시뮬레이션 데이터 기반 의사결정 지원 도구로 한정한다. 금융 후보 역시 과거 수익률이 미래 성과를 보장하지 않고, 현재 Wiki의 퀀트 문서는 `unverified/low` 상태이므로 투자 성과 주장을 피한다.

## External References

- Upbit Developer Center: https://docs.upbit.com/
- Upbit rate limits: https://docs.upbit.com/kr/reference/rate-limits
- MAVLink Developer Guide: https://mavlink.io/en/
- FAA Remote ID: https://www.faa.gov/uas/getting_started/remote_id
- OpenTelemetry observability primer: https://opentelemetry.io/docs/concepts/observability-primer/
- GitHub artifact attestations: https://docs.github.com/en/actions/concepts/security/artifact-attestations

이 답변은 강의/수업/교육과 취업/포트폴리오에 활용 가능합니다 — 학기 프로젝트의 범위·검증 지표·포트폴리오 증거를 하나의 실행안으로 연결합니다.
