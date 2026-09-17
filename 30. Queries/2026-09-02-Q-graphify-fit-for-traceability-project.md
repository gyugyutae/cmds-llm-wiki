---
type: query-result
aliases:
  - Graphify 무인기 추적성 프로젝트 적합성
  - FlightGraph 학기 프로젝트 판단
description: "Evaluation of Graphify as the graph engine for a three-person PX4 safety-traceability semester project, with scope, architecture, baselines, and risks."
author:
  - Codex
date created: 2026-09-02
date modified: 2026-09-02
tags:
  - query
  - graphify
  - traceability
  - drone
  - px4
  - semester-project
source:
  - "[[2026-09-02-Q-three-person-upbit-drone-traceability-proposals]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Andrej Karpathy]]"
  - https://graphify.com/docs
  - https://github.com/geteatpos/graphify/blob/main/ARCHITECTURE.md
  - https://graphify.com/docs/mcp-tools
  - https://graphify.com/docs/verification
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 학부연구생/학술
  - 프로젝트 증거
confidence: high
status: active
---

# Graphify를 추적성 학기 프로젝트에 쓰는 것이 좋은가

## 결론

**좋은 선택이다. 단, Graphify를 설치해 `graph.html`을 보여주는 프로젝트로 만들면 부족하다.**

추천 주제는 다음과 같다.

> **FlightGraph — Graphify 기반 PX4 실행형 안전 추적성 플랫폼**<br>
> 자연어 안전 요구사항을 실행 가능한 contract로 바꾸고, PX4 가상 비행에서 생성한 ULog 증거와 코드·시험·판정을 하나의 typed knowledge graph로 연결한다. 요구사항이 바뀌면 영향을 받는 시험만 찾아 다시 실행한다.

Graphify는 코드·문서·SQL 등의 산출물에서 노드와 관계를 추출하고, 로컬 `graph.json`, 보고서, 대화형 그래프를 생성한다. 관계마다 `EXTRACTED`, `INFERRED`, `AMBIGUOUS`를 표시하며 MCP로 경로 탐색도 제공한다. 따라서 요구사항과 코드·시험·증거의 연결을 다루는 추적성 프로젝트의 **기반 엔진**으로 적합하다. 다만 현재 공개 핵심은 범용 코드/문서 그래프이므로, 팀의 기여는 **PX4·ULog·안전 요구사항이라는 도메인 의미를 추가하는 것**이어야 한다.

## 먼저 바로잡을 점

Graphify 자체를 Andrej Karpathy가 만든 것은 아니다. Karpathy가 2026년 4월 제안한 것은 원천 자료를 LLM이 지속적인 Markdown wiki로 컴파일하고 관리하는 더 넓은 `LLM Wiki` 패턴이다. Graphify는 그 문제의식에서 영감을 받은 별도의 오픈소스 지식 그래프 구현으로 보는 것이 정확하다.

팀원에게는 다음처럼 말한다.

> “Karpathy가 제안한 지속형 LLM 지식베이스 아이디어에서 영감을 받은 최신 오픈소스 Graphify를 쓰되, 우리는 단순 사용자가 아니라 무인기 요구사항과 ULog 증거를 이해하는 도메인 추적성 계층을 직접 개발한다.”

## Graphify가 실제로 제공하는 것

- 여러 코드 언어와 Markdown·PDF·SQL 등의 파일을 로컬에서 graph로 변환
- `graph.html`, `GRAPH_REPORT.md`, `graph.json` 출력
- 파일과 줄 위치를 포함한 graph query와 path 탐색
- `EXTRACTED`, `INFERRED`, `AMBIGUOUS` 관계 신뢰도 구분
- `query_graph`, `get_neighbors`, `shortest_path`, PR impact 같은 read-only MCP 도구
- Python dict와 NetworkX를 이용하는 비교적 단순한 pipeline

공개 architecture의 extractor 반환 형식은 다음처럼 단순하다.

```json
{
  "nodes": [
    {"id": "REQ-ALT-01", "label": "Maximum altitude", "source_file": "requirements.yaml", "source_location": "L8"}
  ],
  "edges": [
    {"source": "REQ-ALT-01", "target": "SC-ALT-01", "relation": "COMPILED_TO", "confidence": "EXTRACTED"}
  ]
}
```

이 확장 가능한 schema 때문에 학부생 3명이 Graphify 전체를 재구현하지 않고 도메인 adapter와 평가에 집중할 수 있다.

## 우리가 직접 만들어야 독창적인 부분

### 1. PX4/ULog domain adapter

`.ulg` 바이너리를 Graphify가 직접 이해하도록 억지로 넣지 않는다. `pyulog`로 필요한 구간을 먼저 요약한 뒤 다음 typed node와 edge로 변환한다.

노드:

- `Requirement`
- `SafetyContract`
- `Scenario`
- `Test`
- `FlightRun`
- `TelemetryEvidence`
- `Verdict`
- `CodeSymbol`

관계:

- `COMPILED_TO`: 요구사항 → safety contract
- `EXECUTED_BY`: contract → scenario/test
- `PRODUCED`: flight run → telemetry evidence
- `VERIFIED_BY`: requirement → verdict/evidence
- `VIOLATED_BY`: requirement → 위반 구간
- `IMPLEMENTED_BY`: contract/rule → code symbol
- `AFFECTS`: 변경된 requirement/code → 재시험 대상

### 2. 신뢰도와 사람 승인

- 파일에 ID가 명시된 관계는 `EXTRACTED`
- LLM이 의미상 연결한 후보는 `INFERRED`
- 단위·신호·요구사항 해석이 불확실하면 `AMBIGUOUS`
- `INFERRED`와 `AMBIGUOUS` 관계는 승인 전 회귀시험 선택에 사용하지 않음

이렇게 하면 LLM을 썼다는 사실보다 **추론과 검증 가능한 사실을 분리한 설계**가 포트폴리오에 남는다.

### 3. 변경 영향 기반 선택적 재시험

예를 들어 `REQ-ALT-01`이 `최대 50m`에서 `40m`로 변경되면 다음 graph path를 탐색한다.

```text
REQ-ALT-01
→ SC-ALT-01
→ altitude_fault_scenario
→ flight-run-023
→ telemetry-segment-8.2s-12.5s
→ FAIL
```

고도 contract에 연결된 시나리오만 PX4 SIH에서 재실행하고, 변경 전후 PASS/FAIL을 비교한다. 이것이 단순 그래프 시각화와 다른 실제 제품 가치다.

## 3인·12주 MVP

범위를 아래에서 더 늘리지 않는다.

- quadrotor 한 모델과 mission template 한 개
- 고도 제한, 저전압, GPS 실패, data-link loss 요구사항 네 개
- 요구사항 version 5개 × scenario 4개 × seed 2개 = 최대 40회 실행
- Graphify 버전 고정
- real drone, ROS 2, Gazebo 3D, multi-drone, GNN 제외
- 실제 안전 인증 및 Graphify Enterprise formal verification 제외

Graphify 문서의 formal verification은 공개 graph/query core가 아니라 Enterprise 계층이다. 이를 핵심 기능으로 계획하면 비용·접근성·지원 범위에 프로젝트가 막힐 수 있다.

## 역할 분담

### 1번 — PX4와 데이터

- SIH mission 및 failure injection
- ULog 수집과 `pyulog` parser
- 재현 가능한 40개 이하의 fixture

### 2번 — Graphify domain extension

- Requirement/Contract/ULog adapter
- typed node·edge schema와 confidence policy
- change-impact traversal과 selective retest

### 3번 — 제품과 평가

- graph·flight timeline·승인 UI
- MCP query와 evidence citation
- baseline 실험, CI, 발표 자료

세 명 모두 schema/API contract, 통합 테스트, architecture decision record를 공동 리뷰한다.

## baseline이 있어야 연구가 된다

| 실험군 | 설명 | 확인할 것 |
|---|---|---|
| Baseline A | 수동 trace matrix 또는 keyword/TF-IDF 검색 | 일반 방식보다 근거 탐색이 나아졌는가 |
| Baseline B | 도메인 확장 없는 vanilla Graphify | 단순 도입보다 UAV adapter가 실제 가치를 더하는가 |
| Proposed | Graphify + PX4/ULog typed adapter + 사람 승인 | 독창적 기여의 효과 |

지표:

- trace-link precision, recall, F1
- 변경 영향 test recall
- 전체 회귀시험 대비 선택적 재시험 시간 감소율
- 요구사항 근거 탐색 시간과 정답률
- `INFERRED`/`AMBIGUOUS` 후보의 사람 승인율과 수정 시간
- 잘못된 evidence path 제시율

Graphify 저장소가 제시하는 token 절감치는 corpus 크기에 따라 크게 달라지므로 주 성과로 삼지 않는다. 우리 프로젝트에서는 정확성, 영향 test 누락 여부, 검토 시간이 핵심이고 token cost는 부지표다.

## 수업과 포트폴리오 적합성

소프트웨어공학 수업의 요구사항 분석, UML, SOLID, parser/adapter 패턴, 상태 관리, 테스트, CI, 변경 영향 분석을 억지 없이 보여줄 수 있다. 오픈소스 전체를 새로 만드는 대신 adapter, confidence policy, selective-retest scheduler, 실험 설계를 팀의 구현물로 남길 수 있다.

포트폴리오 문장:

> Graphify를 단순 적용하는 데 그치지 않고 PX4 안전 요구사항과 ULog evidence를 typed graph로 변환하는 domain adapter를 설계했습니다. 명시적 관계와 LLM 추론 관계를 분리하고, 요구사항 변경 시 선택적 재시험의 recall·실행시간·사람 검토 비용을 수동 trace matrix 및 vanilla Graphify와 비교했습니다.

## OrderScope와 최종 비교

| 판단 기준 | OrderScope AI | FlightGraph |
|---|---:|---:|
| Graphify와의 자연스러운 결합 | 2/5 | 5/5 |
| 금융권 백엔드 직접 연결 | 5/5 | 2.5/5 |
| 교수 제안·최신성 활용 | 3/5 | 5/5 |
| 추적성 연구 깊이 | 4/5 | 5/5 |
| 12주 실행 위험 | 낮음~중간 | 중간 |

OrderScope의 호가·체결·주문은 지속적으로 발생하는 runtime event이므로 event store와 deterministic replay가 중심이어야 한다. Graphify를 억지로 핵심 저장소로 쓰면 도구와 문제의 형태가 맞지 않는다. 반면 FlightGraph의 요구사항·contract·code·test·요약 evidence는 버전된 산출물이어서 graph traversal과 매우 잘 맞는다.

따라서 **교수의 Graphify 제안을 살리고 추적성 자체를 깊게 하고 싶다면 FlightGraph를 추천**한다. 금융권 취업 직접성을 최우선으로 한다면 Graphify를 빼고 OrderScope를 선택하는 편이 더 정직하다.

## 1주 기술 spike 합격 조건

본 개발 전에 다음이 모두 되어야 FlightGraph를 선택한다.

1. PX4 SIH 1회 실행 및 ULog 생성
2. ULog에서 고도 timestamp와 최대값 추출
3. requirement YAML 한 개와 ULog 요약 JSON을 Graphify schema로 변환
4. `Requirement → Contract → FlightRun → Evidence → Verdict` path 출력
5. 50m를 40m로 바꿨을 때 영향 scenario 두 개 이하를 선택

3번까지 실패하면 즉시 OrderScope로 전환한다. 4~5번은 작은 fixture로 구현 가능해야 한다.

> [!note] Bias Check
> Graphify는 2026년에 빠르게 변하는 초기 도구이므로 문서 기능과 package 동작이 달라질 수 있다. 버전을 고정하고 핵심 trace schema와 adapter는 Graphify 내부 구현에 과도하게 결합하지 않는다. Graphify 도입 자체를 독창성이나 안전성 향상으로 주장하지 않고, vanilla baseline 대비 domain extension의 측정 결과로만 주장한다.

## Sources

- Graphify quickstart and outputs: https://graphify.com/docs
- Graphify pipeline, schema, confidence labels: https://github.com/geteatpos/graphify/blob/main/ARCHITECTURE.md
- Graphify MCP tools: https://graphify.com/docs/mcp-tools
- Open-source core and Enterprise formal verification boundary: https://graphify.com/docs/verification
- Existing semester proposals: [[2026-09-02-Q-three-person-upbit-drone-traceability-proposals]]

이 답변은 강의/수업/교육, 취업/포트폴리오, 학부연구생/학술, 프로젝트 증거에 활용 가능합니다 — Graphify를 도구 시연이 아니라 PX4/ULog 추적성 domain extension과 비교 실험으로 전환합니다.
