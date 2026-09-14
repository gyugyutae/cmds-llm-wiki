---
type: query-result
aliases:
  - Upbit 주문 추적성 프로젝트 재설계
  - OrderScope AI
description: "A semester-scale Upbit project proposal for tracing, replaying, and diagnosing algorithmic order incidents with a paper OMS and an evidence-grounded MCP forensic agent."
author:
  - Codex
date created: 2026-09-02
date modified: 2026-09-02
tags:
  - query
  - upbit
  - order-traceability
  - fintech-backend
  - mcp
  - incident-replay
source:
  - "[[2026-09-01-Q-software-engineering-semester-project-selection]]"
  - "[[2026-09-01-Q-upbit-financial-decision-traceability-project]]"
  - "[[2026-09-02-Q-semester-project-concrete-team-brief]]"
  - "[[김규태 금융 시스템 개발자 취업 로드맵]]"
  - https://docs.upbit.com/kr/kr/changelog/upbit-strategy-toolkit
  - https://docs.upbit.com/kr/docs/upbit-agent-skills
  - https://docs.upbit.com/kr/reference/websocket-orderbook
  - https://docs.upbit.com/kr/reference/websocket-myorder
  - https://docs.upbit.com/kr/reference/order-test
  - https://modelcontextprotocol.io/specification/2025-06-18/server/tools
  - https://github.com/open-telemetry/semantic-conventions-genai
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 백엔드/성능/금융 시스템
  - 프로젝트 증거
confidence: high
status: active
---

# Upbit 주문 추적성 프로젝트 재설계

## 최종 제안

> **OrderScope AI — Upbit 알고리즘 주문의 전 과정을 추적하고 장애 원인을 재현하는 금융 주문 블랙박스**

짧은 설명:

> 자동매매 프로그램이 주문을 냈는데 왜 체결되지 않았는지, 왜 예상 가격과 달라졌는지, 같은 주문이 왜 두 번 처리됐는지를 주문 당시 호가와 시스템 이벤트로 재현하고 AI가 근거와 함께 진단하는 개발자 도구다.

이 프로젝트는 수익을 내는 알고리즘을 만드는 것이 아니다. **알고리즘 매매 시스템을 안전하게 개발하고 디버깅하는 도구**를 만든다.

## 왜 기존 WhyBuy보다 낫나

- WhyBuy의 질문: 개인 투자자가 `왜 매수했는가?`
- OrderScope의 질문: 금융 개발자가 `주문이 왜 실패하거나 예상과 다르게 처리됐는가?`

전자는 투자 의도와 권한이 중심이라 추상적으로 느끼기 쉽다. 후자는 주문 상태, 호가, 체결, 지연, 중복이라는 명확한 백엔드 문제와 화면 데모가 있다.

2026-07 Upbit는 AI agent용 Strategy Toolkit을 공개해 자연어 전략 JSON 생성과 백테스트를 지원하기 시작했다. Upbit Skills도 실시간 시세와 주문 도구를 제공한다. 따라서 또 하나의 전략 생성·백테스트 앱을 만드는 것보다 **AI agent가 낸 주문을 관측하고 사고를 재현하는 계층**이 더 분명한 차별점이다.

## 해결하려는 실제 문제

알고리즘 주문 시스템에서는 다음 문제가 생길 수 있다.

1. 전략은 BUY를 냈지만 위험 검사에서 차단됐다.
2. 주문 직전 호가가 바뀌어 예상 가격과 paper 체결 가격이 달라졌다.
3. API 응답이 늦어 주문 실패로 생각하고 재요청해 중복 주문 위험이 생겼다.
4. 지정가가 시장 가격과 멀어 계속 체결 대기 상태로 남았다.
5. WebSocket이 끊겨 중간 체결 이벤트 일부를 놓쳤다.
6. 요청 수 제한으로 429가 발생했는데 단순 주문 실패로 기록됐다.

보통은 여러 로그와 시장 데이터를 개발자가 직접 맞춰봐야 한다. OrderScope는 주문 하나에 `correlationId`를 부여해 모든 사건을 연결한다.

## 주문 한 건의 trace

```text
StrategySignal
BUY KRW-BTC 50,000원
    ↓
MarketSnapshot
당시 매도 1호가·매수 1호가·잔량·최근 체결
    ↓
RiskCheck
최소 주문 금액·예산·데이터 신선도 검사
    ↓
OrderRequest
clientOrderId와 주문 유형 기록
    ↓
Paper OMS
CREATED → ACCEPTED → PARTIAL → FILLED / CANCELLED / UNKNOWN
    ↓
ExecutionResult
평균 체결 가격·수수료·slippage·지연
    ↓
IncidentReport
원인·근거 event ID·신뢰도·권장 조치
    ↓
Human Review
개발자가 진단 승인 또는 수정
```

`OMS`는 Order Management System, 즉 주문의 접수부터 체결·취소까지 상태를 관리하는 시스템이다. 학기 프로젝트에서는 실제 거래소 OMS가 아니라 공개 호가·체결 데이터 위에서 움직이는 작은 paper OMS를 구현한다.

## 핵심 데모

### 정상 주문

1. 간단한 적립식 규칙이 `KRW-BTC 5만 원 매수` 신호를 만든다.
2. 시스템이 Upbit 호가 snapshot을 저장한다.
3. 위험 검사를 통과한다.
4. paper OMS가 당시 매도 호가와 잔량을 사용해 모의 체결한다.
5. 전략 신호부터 체결까지 타임라인을 보여준다.

### 장애 주문

1. 시스템이 주문 요청을 보냈지만 의도적으로 timeout을 발생시킨다.
2. 사용자는 실패로 생각해 같은 주문을 다시 보낸다.
3. OrderScope가 같은 `clientOrderId` 또는 idempotency key를 찾아 두 번째 주문을 막는다.
4. AI 포렌식 에이전트가 관련 trace를 조회한다.
5. `ORDER_STATUS_AMBIGUOUS`라는 구조화된 진단과 근거 event ID를 제시한다.
6. 사람이 진단을 승인한다.

최종 발표에서는 정상 주문보다 이 장애·복구 장면이 더 중요하다.

## 최신 기술 적용

### Headline — MCP 기반 금융 포렌식 에이전트

OrderScope는 trace DB를 읽는 전용 MCP server를 만든다. MCP는 LLM이 외부 도구를 발견하고 호출하는 방식을 표준화한다. 에이전트가 임의 SQL이나 Upbit 주문을 직접 실행하게 하지 않고 아래 읽기·시뮬레이션 도구만 제공한다.

- `get_order_timeline(correlationId)`
- `get_market_snapshot(snapshotId)`
- `check_order_invariants(correlationId)`
- `compare_signal_and_execution(correlationId)`
- `replay_paper_order(correlationId)`

에이전트 출력은 자유형 문장이 아니라 다음과 같은 JSON schema로 제한한다.

```json
{
  "rootCause": "STALE_ORDERBOOK",
  "evidenceEventIds": ["evt-21", "evt-24"],
  "confidence": 0.91,
  "explanation": "주문 판단에 사용한 호가가 제출 시점보다 2.4초 오래되었습니다.",
  "recommendedAction": "호가 최대 허용 나이를 500ms로 제한하세요."
}
```

모든 설명은 존재하는 event ID를 인용해야 하며, 사람이 승인하기 전에는 확정 원인으로 저장하지 않는다.

### Supporting — OpenTelemetry형 end-to-end trace

전략 계산, Upbit API, 위험 검사, paper 주문, AI tool call을 하나의 trace로 연결한다. OpenTelemetry의 GenAI conventions는 agent와 tool 실행을 위한 span·attribute 표준을 개발하고 있어 최신 agent observability를 경험할 수 있다.

MVP에서는 OpenTelemetry backend 전체를 구축하지 않고 trace ID, span ID, operation, start/end, status, evidence reference의 최소 schema부터 구현한다.

## 실제로 사용하는 Upbit API

인증 불필요:

- WebSocket/REST 호가: 모의 주문 당시 매수·매도 가격과 잔량
- 최근 체결: 시장에서 실제 거래된 가격과 수량
- 현재가·캔들: 단순 신호와 시장 상황
- 페어·호가 정책: 지원 거래쌍과 주문 가격 단위

인증 필요하지만 실제 주문이 발생하지 않는 선택 기능:

- 주문 생성 테스트: 요청 형식, 최소 주문 조건 등 검증

실제 주문·출금·입금은 구현 범위에서 제외한다. 2026-09-02 공개 API 호출로 `KRW-BTC` 30단계 호가와 최근 체결을 인증 없이 정상 수신할 수 있음을 확인했다.

Upbit는 `KRW-BTC`처럼 결제 화폐가 앞에 오는 페어 형식을 쓰며, WebSocket으로 호가·체결을 실시간 구독할 수 있다. `myOrder`는 실제 주문 상태와 부분 체결, 평균 체결가, 수수료, 클라이언트 주문 식별자 등을 제공하지만 인증과 실제 주문이 필요하므로 MVP에서는 해당 schema를 참고한 paper event를 사용한다.

## 필수 기능

1. `KRW-BTC`, `KRW-ETH` 공개 호가·체결 수집
2. 시장 snapshot의 시점과 원본 hash 보존
3. 시장가 매수와 지정가 매수를 지원하는 paper OMS
4. 주문 상태 머신과 idempotency key
5. 전략 신호부터 모의 체결까지 trace timeline
6. 다섯 가지 장애 시나리오 주입
7. MCP read-only forensic tools
8. 근거 event를 인용하는 LLM structured incident report
9. 사람의 진단 승인·수정
10. raw log baseline과 진단 정확도·시간 비교

## 다섯 가지 장애만 다룬다

- `RISK_REJECTED`: 위험 규칙에 의해 주문 차단
- `STALE_ORDERBOOK`: 오래된 호가로 인한 잘못된 체결 예상
- `DUPLICATE_REQUEST`: timeout 뒤 동일 주문 재요청
- `UNFILLED_LIMIT`: 시장에서 멀어진 지정가 주문
- `STREAM_GAP`: WebSocket 단절로 상태 이벤트 누락

429 rate limit은 여력이 있으면 여섯 번째 stretch scenario로 추가한다.

## 연구 질문과 baseline

### 연구 질문

- RQ1. evidence-grounded MCP agent가 raw log만 사용할 때보다 주문 장애 원인을 더 정확하게 분류하는가?
- RQ2. trace timeline과 replay가 개발자의 장애 원인 파악 시간을 줄이는가?
- RQ3. event-sourced paper OMS가 누락 또는 중복 이벤트 이후 주문 최종 상태를 정확하게 재구성하는가?

### 비교

| Baseline | 제안 방식 |
|---|---|
| timestamp가 있는 일반 text log | correlation ID로 연결된 structured trace |
| 개발자가 여러 로그를 수동 탐색 | timeline + deterministic replay |
| LLM에 raw log 전체 입력 | MCP tool로 필요한 증거만 조회 |
| 자유형 LLM 설명 | root cause enum + evidence ID JSON |

### 평가 지표

- 5개 장애 유형 분류 accuracy와 macro-F1
- 보고서 evidence precision: 인용한 event가 실제 원인을 지지하는 비율
- hallucination rate: 존재하지 않는 event 인용 비율
- 학생 개발자 5명의 원인 파악 시간과 정답률
- 동일 event stream replay 시 주문 최종 상태 일치율
- 중복 paper order 발생 건수
- 호가 수신부터 trace 저장까지 p95 latency
- WebSocket 재연결 후 event gap 탐지율

각 장애를 10회씩 주입한 50개 scenario면 학기 수업용 비교 실험이 가능하다. 산업 일반화나 실제 거래 안전성을 증명한다고 주장하지 않는다.

## 수업 취지와 연결

| 소프트웨어공학 활동 | 산출물 |
|---|---|
| 사용자 요구분석 | 개인 퀀트 개발자·학생 개발자 인터뷰와 장애 시나리오 |
| 요구사항 명세 | 주문 추적, 재현, 근거 인용, 안전 범위 |
| UML | 주문 state diagram, incident diagnosis sequence diagram |
| SOLID | MarketDataAdapter, RiskPolicy, PaperBroker, TraceStore, ForensicTool 분리 |
| 디자인 패턴 | State, Strategy, Adapter, Repository |
| 협업 | API·OMS·AI/MCP·프론트/실험의 독립 모듈 |
| 테스트 | 상태 전이, 중복 주문, stream gap, stale data, LLM schema contract |
| CI | 고정 market snapshot으로 50개 장애 회귀 테스트 |
| 중간 데모 | 정상 주문 1건과 timeout 중복 주문 1건의 추적·진단 |
| 최종 시험 | baseline 대비 macro-F1, 진단시간, p95, replay 일치율 |

## 금융권 포트폴리오 가치

이 프로젝트에서는 다음을 구체적으로 설명할 수 있다.

- 주문 상태 머신과 부분 체결 개념
- idempotency를 이용한 중복 주문 방지
- WebSocket 끊김과 event gap 복구
- REST/WebSocket rate limit 대응
- event sourcing과 replay
- p95/p99 지연 측정
- LLM의 근거 강제와 human-in-the-loop
- API Key를 실제 주문에 노출하지 않는 안전 경계

이는 `코인 가격을 예측했다`보다 은행·증권·핀테크 백엔드 면접에서 시스템 설계와 장애 대응 역량을 보여주기 좋다.

## 4명 협업 예시

- A: Upbit REST/WebSocket 수집, 재연결, snapshot 저장
- B: paper OMS, 상태 머신, idempotency, fault injection
- C: MCP server, forensic agent, structured output 평가
- D: trace UI, timeline/replay UX, 사용자 실험과 CI dashboard

각 팀원은 자기 모듈의 단위 테스트와 통합 테스트까지 담당한다. 팀장은 end-to-end trace schema, API contract, 8주차 vertical slice를 관리한다.

## 12주 범위

| 주차 | 완료 기준 |
|---|---|
| 1~2주 | 사용자 3명 인터뷰, 주문 trace schema, 장애 5개 확정 |
| 3~4주 | Upbit 실시간 호가·체결 recorder와 snapshot DB |
| 5~6주 | paper OMS, 주문 상태 머신, idempotency |
| 7~8주 | trace timeline, 정상·중복 주문 장애 데모 |
| 9주 | MCP read-only tools와 LLM structured report |
| 10주 | 5개 fault injector와 deterministic replay |
| 11주 | 50개 scenario 자동 평가와 사용자 baseline 실험 |
| 12주 | 결과 보고서, 성능 그래프, 최종 발표·회고 |

8주차까지 AI 없이도 주문 trace와 replay가 작동해야 한다. MCP agent는 핵심 시스템 위에 추가하는 분석 계층이다.

## 같은 축의 대안 두 개

### StrategyGap

Upbit Strategy Toolkit의 백테스트 결과와 실시간 paper execution 결과를 연결해 수익률 차이가 전략 버전, 미래 데이터 누수, 수수료, slippage, 시장 변화 중 어디에서 발생했는지 추적한다. 흥미롭지만 의미 있는 paper 기간이 짧고 백테스트 엔진을 중복 구현할 위험이 있어 2순위다.

### AgentOrder Firewall

AI agent가 Upbit tool을 호출할 때 읽기, 주문 테스트, 실제 주문 권한을 분리하고 prompt injection이나 한도 초과 tool call을 차단·감사한다. 최신 MCP authorization·agent security와 맞지만 공격 benchmark 설계가 어렵고 기존 WhyBuy의 권한 위임 문제와 가까워 3순위다.

## 팀원에게 말할 60초 설명

> 저희가 만들려는 것은 수익을 내는 자동매매 봇이 아니라 자동매매 시스템을 디버깅하는 금융 개발자 도구입니다. 전략이 주문 신호를 냈는데 왜 체결되지 않았는지, 왜 예상 가격과 달랐는지, timeout 뒤 같은 주문이 두 번 들어갔는지를 보통은 여러 로그에서 직접 찾아야 합니다. OrderScope는 Upbit 실시간 호가와 체결 데이터를 저장하고, 전략 신호부터 위험 검사, paper 주문, 체결 결과까지 하나의 trace로 연결합니다. 장애가 나면 MCP 기반 AI 에이전트가 읽기 전용 도구로 근거를 조회해 event ID가 포함된 진단 보고서를 만들고 사람이 승인합니다. 실제 돈은 전혀 사용하지 않고 다섯 가지 장애를 반복 주입해 일반 로그보다 진단 정확도와 시간이 개선되는지 평가하겠습니다.

## 결론

세 후보 중 `OrderScope AI`를 추천한다. Upbit API는 단순 데이터 공급원이 아니라 호가·체결·주문 상태라는 trace의 핵심 증거가 된다. 추적성은 부가 화면이 아니라 장애를 재현하는 제품 핵심이고, MCP agent는 trace를 근거로 진단하는 최신 기술 계층이다. 수익률 경쟁을 피하면서도 금융 주문 백엔드, 실시간 데이터, 장애 대응, AI 활용을 하나의 포트폴리오 서사로 묶을 수 있다.

> [!note] Bias Check
> event sourcing, OpenTelemetry, MCP, paper trading은 각각 이미 존재한다. 독창성은 기술 발명보다 Upbit 주문의 signal-to-execution trace, 재현 가능한 장애 주입, evidence-bound agent diagnosis를 하나의 학기 제품으로 결합하고 baseline으로 검증하는 데 있다. paper OMS 결과는 실제 Upbit 체결 품질이나 운영 안전성을 증명하지 않는다.

## Sources

- Upbit Strategy Toolkit 출시: https://docs.upbit.com/kr/kr/changelog/upbit-strategy-toolkit
- Upbit Skills: https://docs.upbit.com/kr/docs/upbit-agent-skills
- Upbit WebSocket 호가: https://docs.upbit.com/kr/reference/websocket-orderbook
- Upbit WebSocket 체결: https://docs.upbit.com/kr/reference/websocket-trade
- Upbit MyOrder: https://docs.upbit.com/kr/reference/websocket-myorder
- Upbit rate limits: https://docs.upbit.com/kr/kr/reference/rate-limits
- MCP tools: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- OpenTelemetry GenAI conventions: https://github.com/open-telemetry/semantic-conventions-genai

이 답변은 강의/수업/교육과 백엔드/성능/금융 시스템에 활용 가능합니다 — Upbit 공개 시세를 이용한 paper OMS에서 금융 주문 장애를 직접 만들고 추적·재현·평가하는 포트폴리오를 설계합니다.
