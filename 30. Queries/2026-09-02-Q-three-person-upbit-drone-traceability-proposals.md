---
type: query-result
aliases:
  - 3인 팀 Upbit 무인기 추적성 프로젝트 2안
  - OrderScope FlightProof 팀 회의안
description: "Two comparable three-person semester proposals: Upbit order-incident traceability and PX4 executable safety-evidence traceability without real drone data."
author:
  - Codex
date created: 2026-09-02
date modified: 2026-09-02
tags:
  - query
  - semester-project
  - team-proposal
  - upbit
  - drone
  - traceability
source:
  - "[[2026-09-02-Q-upbit-order-traceability-project-redesign]]"
  - "[[2026-09-01-Q-emerging-traceability-technology-selection]]"
  - "[[2026-09-01-Q-software-engineering-semester-project-selection]]"
  - https://docs.upbit.com/kr/reference/websocket-orderbook
  - https://docs.px4.io/main/en/simulation/px4_sitl_prebuilt_packages
  - https://docs.px4.io/main/en/simulation/failsafes
  - https://docs.px4.io/main/en/dev_log/logging
  - https://docs.px4.io/main/en/test_and_ci/integration_testing_mavsdk
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 백엔드/성능/금융 시스템
  - 학부연구생/학술
  - 프로젝트 증거
confidence: high
status: active
---

# 3인 팀 Upbit·무인기 추적성 프로젝트 2안

## 공통 선정 조건

두 안 모두 다음 조건을 지킨다.

- 3명, 12주
- 8주차에 AI 없이도 핵심 end-to-end demo가 작동
- 실제 자금과 실제 드론 하드웨어 사용 안 함
- 외부에서 구하기 어려운 데이터셋에 의존하지 않음
- 추적성이 부가 시각화가 아니라 문제 해결의 핵심
- 최신 기술은 headline 한 개, stretch 한 개
- baseline과 정량 평가가 있음
- 요구사항·UML·SOLID·패턴·테스트·CI 산출물이 자연스럽게 나옴

---

# A안 — OrderScope AI

## 한 문장

> Upbit 알고리즘 주문이 왜 실패·중복·미체결됐는지 신호부터 호가·위험 검사·paper 체결까지 추적하고, MCP agent가 근거 event를 인용해 장애 원인을 진단하는 금융 주문 블랙박스다.

## 사용자와 문제

- 사용자: 개인 퀀트 개발자, 자동매매를 개발하는 학생, 소규모 금융 개발팀
- 문제: 주문 장애가 발생하면 전략 로그, Upbit 시장 데이터, 주문 상태를 수동으로 맞춰봐야 한다.
- 가치: 주문 하나의 전체 생명주기를 재현해 원인 파악 시간과 중복 주문 위험을 줄인다.

## 3인 MVP 범위

- `KRW-BTC` 한 페어만 지원
- Upbit 공개 WebSocket 호가·체결 recorder
- 시장가 매수와 지정가 매수 paper OMS
- 주문 상태 머신과 idempotency key
- signal → snapshot → risk → order → execution trace timeline
- 장애 네 종류: stale orderbook, duplicate request, unfilled limit, stream gap
- MCP read-only 도구 네 개와 LLM structured incident report
- 사람의 진단 승인·수정
- raw text log baseline과 비교

실제 주문, 출금, 멀티코인, 수익 예측, 백테스트 엔진은 제외한다. Upbit Strategy Toolkit의 전략 JSON 한 개를 입력 형식으로 재사용하거나 단순 이동평균 신호 하나만 직접 구현한다.

## 최신 기술

- Headline: **MCP 기반 evidence-grounded 금융 포렌식 에이전트**
- Stretch: **OpenTelemetry GenAI형 agent/tool-call trace**

에이전트는 `get_order_timeline`, `get_market_snapshot`, `check_order_invariants`, `replay_paper_order`만 호출한다. 보고서는 `rootCause`, `evidenceEventIds`, `confidence`, `recommendedAction` JSON으로 반환하고 사람이 승인한다.

## 8주차 데모

1. Upbit 실시간 호가를 저장한다.
2. `KRW-BTC 5만 원 매수` paper 주문을 정상 처리한다.
3. timeout을 주입하고 같은 요청을 다시 보낸다.
4. idempotency key가 중복 주문을 차단한다.
5. 두 주문의 차이를 trace timeline에서 보여준다.

AI 진단은 9주차 이후에 붙인다.

## 연구 질문

> Structured trace와 evidence-grounded MCP agent가 일반 text log보다 주문 장애 원인을 더 빠르고 정확하게 찾는가?

평가:

- 장애 4종 × 8회 = 32개 scenario의 macro-F1
- 존재하지 않는 event 인용률
- 원인 파악 시간과 정답률
- replay 상태 일치율
- 중복 paper order 수
- WebSocket 수집·저장 p95 latency

## 3명 역할

### 1번 — Market Data

- Upbit REST/WebSocket
- 호가·체결 snapshot
- 재연결과 stream gap 탐지
- rate limit·data freshness test

### 2번 — Paper OMS & Trace

- 주문 상태 머신
- idempotency
- paper matching
- fault injector와 deterministic replay

### 3번 — Agent & Review UI

- trace timeline UI
- MCP server와 structured diagnosis
- 사람 승인 workflow
- baseline 사용자 실험

공통으로 API contract, 통합 테스트, CI, 발표를 맡는다.

## 포트폴리오 문장

> Upbit 실시간 호가·체결을 이용한 paper OMS에서 주문 상태 머신과 멱등성을 설계하고, 장애 네 종류를 반복 주입해 MCP 기반 근거 진단의 macro-F1·환각률·원인 파악 시간을 일반 로그와 비교했습니다.

---

# B안 — FlightProof Twin

## 한 문장

> 무인기 안전 요구사항을 실행 가능한 규칙으로 만들고 PX4 가상 드론에 고장을 주입해, 요구사항부터 시뮬레이션·비행 로그·판정 결과까지 연결하고 변경 시 필요한 시험만 재실행하는 Executable Digital Thread다.

쉬운 표현:

> 실제 드론 없이 가상 드론으로 안전 요구사항을 시험하고, 각 요구사항이 어떤 비행 증거로 통과했는지 보여주는 시스템이다.

## 사용자와 문제

- 사용자: 무인기 프로젝트 학생팀, 연구실 연구자, 시험 담당자
- 문제: 요구사항 문서, 시뮬레이션 설정, 비행 로그, 시험 결과가 분리되어 요구사항이 실제로 검증됐는지와 변경 후 무엇을 재시험해야 하는지 찾기 어렵다.
- 가치: 요구사항을 정적 문서가 아니라 반복 실행할 수 있는 시뮬레이션 증거와 연결한다.

## 데이터가 없는 문제 해결

PX4 SITL/SIH가 가상 비행 데이터와 ULog를 직접 생성한다.

- lightweight SIH container를 기본으로 사용
- GPS off/stuck/wrong 고장 주입
- 배터리 감소 속도와 최소 잔량 설정
- data-link loss failsafe 실행
- PX4가 생성하는 ULog에서 위치·배터리·비행 모드·failsafe event 추출

PX4 setup이 늦어지면 공식 Flight Review의 CC-BY 공개 ULog를 fallback fixture로 사용한다. 3D Gazebo는 최종 시각적 데모용 stretch이고, 핵심 테스트는 headless SIH로 실행한다.

## 실제 시나리오

요구사항:

```text
REQ-ALT-01: 임무 중 상대 고도는 50m를 넘지 않아야 한다.
REQ-BAT-01: 배터리가 20% 미만이면 복귀 또는 착륙해야 한다.
REQ-GPS-01: GPS 위치가 유효하지 않으면 임무를 계속하면 안 된다.
REQ-LINK-01: 데이터 링크를 잃으면 설정된 failsafe가 실행돼야 한다.
```

실행 흐름:

```text
Natural-language Requirement
→ Approved Safety Contract JSON
→ PX4 version + parameters + mission scenario
→ SITL execution + fault injection
→ ULog telemetry segment
→ deterministic rule verdict
→ requirement evidence link
→ signed Evidence Packet
```

`REQ-ALT-01`이 50m에서 40m로 변경되면 시스템은 altitude contract를 사용하는 시나리오만 찾아 다시 실행한다. 이전 결과와 새 결과를 비교하고 어떤 비행이 PASS에서 FAIL로 바뀌었는지 보여준다.

## 최신 기술

### Headline — Executable Digital Twin Assurance Thread

일반 trace matrix는 요구사항과 test 문서만 연결한다. FlightProof는 요구사항을 가상 드론에서 반복 실행 가능한 contract와 test scenario에 연결한다. 각 증거에는 PX4 version, parameter set, mission, injected failure, ULog hash, verdict를 포함한다.

### Stretch — LLM Safety Contract Compiler

LLM이 자연어 요구사항을 다음 JSON 후보로 변환한다.

```json
{
  "requirementId": "REQ-ALT-01",
  "signal": "vehicle_local_position.z",
  "operator": "LTE",
  "threshold": 50,
  "unit": "m",
  "durationMs": 0,
  "expectedAction": "NONE"
}
```

LLM은 초안만 만들고 사람이 signal, 단위, threshold를 승인해야 실행된다. 실제 PASS/FAIL은 LLM이 아니라 deterministic rule engine이 판정한다.

## 3인 MVP 범위

- 요구사항 네 개만 지원
- PX4 SIH quadrotor 한 모델
- mission template 한 개
- altitude, low battery, GPS failure, data-link loss 네 scenario
- Safety Contract JSON editor와 사람 승인
- SIH scenario runner와 ULog parser
- 요구사항 → scenario → log segment → verdict trace graph
- 지도 또는 비행 경로 + event timeline
- 요구사항 version diff와 영향받는 test 선택 재실행
- Evidence Packet export

실제 드론, ROS 2, 자율주행 vision, multi-drone, GNN, 규제 인증은 제외한다.

## 8주차 데모

1. `고도 50m 이하` 요구사항과 contract를 등록한다.
2. 정상 임무와 55m 상승 임무를 SIH에서 실행한다.
3. ULog를 파싱해 정상 PASS, 위반 FAIL과 정확한 시간 구간을 표시한다.
4. 요구사항을 `40m 이하`로 변경한다.
5. 영향받은 두 scenario만 재실행하고 변경 전후 verdict를 비교한다.

GPS·배터리 고장과 LLM contract 변환은 이후에 추가한다.

## 연구 질문

- RQ1. trace-based selective retest가 전체 회귀시험보다 실행 수와 시간을 줄이면서 영향받은 실패를 모두 발견하는가?
- RQ2. Executable Evidence Packet이 원본 ULog와 문서를 따로 볼 때보다 요구사항 검증 근거를 빠르고 정확하게 찾게 하는가?
- RQ3. LLM+사람 승인 contract 작성이 수동 JSON 작성보다 시간을 줄이면서 의미 오류를 통제할 수 있는가?

평가:

- 변경 영향 test recall: 실제 영향받은 test를 빠뜨리지 않은 비율
- 전체 재실행 대비 test 수·실행시간 감소율
- 네 안전 규칙의 위반 탐지 precision/recall
- requirement-evidence trace completeness
- 근거 탐색 시간과 사용자 정답률
- LLM contract 초안의 field accuracy와 사람 수정률

요구사항 version 5개 × scenario 4개 × 정상/고장 seed 2개로 40개 실행을 만들 수 있다.

## 3명 역할

### 1번 — Simulation & Flight Data

- PX4 SIH container
- mission 실행과 failure injection
- ULog 수집·parser
- 재현 가능한 scenario fixture

### 2번 — Requirement & Trace Engine

- Safety Contract schema
- deterministic rule engine
- trace graph와 change-impact algorithm
- selective retest scheduler

### 3번 — Evidence UI & AI

- 요구사항/contract 승인 UI
- 비행 경로·event timeline·version diff
- LLM structured contract 후보
- 사용자 실험과 Evidence Packet

공통으로 simulation-to-backend contract, 통합 테스트, CI, 발표를 맡는다.

## 포트폴리오 문장

> PX4 SIH에서 GPS·배터리·링크 고장을 주입해 재현 가능한 ULog fixture를 생성하고, 버전된 무인기 안전 요구사항과 시험·telemetry evidence를 연결해 변경 영향 기반 선택적 재시험의 recall과 시간 절감률을 검증했습니다.

---

# 두 안 비교

## Graphify 제안 반영

교수의 Graphify 제안을 채택한다면 B안 이름과 headline을 다음처럼 바꾼다.

> **FlightGraph — Graphify 기반 PX4 실행형 안전 추적성 플랫폼**

Graphify의 범용 code/document graph 위에 팀이 `Requirement`, `SafetyContract`, `FlightRun`, `TelemetryEvidence`, `Verdict`를 추출하는 PX4/ULog domain adapter를 개발한다. 명시된 관계는 `EXTRACTED`, LLM 후보는 `INFERRED` 또는 `AMBIGUOUS`로 분리하고 사람이 승인한다. 요구사항 변경 시 graph traversal로 영향받는 scenario만 찾아 재실행한다.

단순 `graph.html` 시연은 프로젝트 기여로 인정하지 않는다. 수동 trace matrix와 vanilla Graphify를 baseline으로 두고, domain adapter를 추가했을 때 trace-link F1, change-impact test recall, 재시험 시간, 사람 검토 시간이 얼마나 달라지는지 측정한다. 상세 판단과 1주 spike 조건은 [[2026-09-02-Q-graphify-fit-for-traceability-project]]를 따른다.

| 기준 | OrderScope AI | FlightProof Twin |
|---|---:|---:|
| 12주·3인 완수 가능성 | 4.5 | 3.5 |
| 외부 데이터 독립성 | 5 | 4.5 |
| 수업 산출물 적합성 | 5 | 5 |
| 최신 기술 체험 | MCP·agent observability | executable digital twin·LLM contract |
| 중간 데모 명확성 | 5 | 4 |
| 금융권 취업 연결 | 5 | 2.5 |
| 연구실·졸업연구 연결 | 3 | 5 |
| 환경 설정 위험 | 낮음~중간 | 중간~높음 |
| 대표 기술 위험 | paper 체결 모델 정확성 | PX4 SITL 자동화 안정성 |

## 현재 추천

김규태의 금융권 백엔드 취업을 최우선으로 보면 `OrderScope AI`를 추천한다. 주문 상태 머신, 멱등성, WebSocket, event replay, 장애 대응, p95 측정은 금융 시스템 면접에서 직접 설명하기 좋다.

학부연구와 무인기 도메인의 깊이를 선택하면 `FlightProof Twin`이 더 독창적인 연구 서사를 만든다. 실제 드론 데이터가 없어도 공식 simulator와 failure injection으로 데이터를 생성한다는 점에서 이전 DroneTrace 안보다 실행 가능성이 높다.

## 팀 회의에서 확인할 세 질문

1. 팀원들이 Upbit/WebSocket과 PX4/simulation 중 어느 환경을 더 배우고 싶은가?
2. 2주 안에 OrderScope의 실시간 호가 저장 또는 FlightProof의 SIH ULog 한 건 생성을 누가 책임질 수 있는가?
3. 금융권 취업 포트폴리오와 연구실 연계 중 팀의 공동 우선순위는 무엇인가?

말로만 투표하지 말고 1주 기술 spike를 한다.

- OrderScope spike 성공: `KRW-BTC` 호가 10분 저장 + paper market order 1건 replay
- FlightProof spike 성공: PX4 SIH 1회 이륙·착륙 + ULog에서 고도 추출

둘 중 spike 완료도가 높은 프로젝트를 최종 선택한다.

> [!note] Bias Check
> 두 프로젝트의 개별 구성 기술은 이미 존재한다. 독창성은 OrderScope의 evidence-bound 주문 장애 진단과 FlightProof의 실행 가능한 requirement-evidence thread를 실제 baseline으로 검증하는 응용에 있다. Paper 체결과 SITL 결과를 각각 실제 거래소 운영 안정성이나 실제 무인기 안전 인증으로 과장하지 않는다.

## Sources

- Upbit WebSocket orderbook: https://docs.upbit.com/kr/reference/websocket-orderbook
- Upbit MyOrder: https://docs.upbit.com/kr/reference/websocket-myorder
- PX4 pre-built SITL packages: https://docs.px4.io/main/en/simulation/px4_sitl_prebuilt_packages
- PX4 failsafe simulation: https://docs.px4.io/main/en/simulation/failsafes
- PX4 logging/ULog: https://docs.px4.io/main/en/dev_log/logging
- PX4 MAVSDK integration testing: https://docs.px4.io/main/en/test_and_ci/integration_testing_mavsdk
- PX4 public logs: https://docs.px4.io/main/en/dev_log/flight_log_analysis_statistical

이 답변은 강의/수업/교육, 취업/포트폴리오, 백엔드/성능/금융 시스템, 학부연구생/학술에 활용 가능합니다 — 3명이 동일 기준으로 금융 주문 trace와 무인기 executable safety trace 중 하나를 기술 spike 후 선택하게 합니다.
