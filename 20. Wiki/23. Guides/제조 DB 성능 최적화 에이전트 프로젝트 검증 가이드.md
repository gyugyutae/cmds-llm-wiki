---
type: wiki-page
aliases:
  - 제조 DB 튜닝 에이전트 프로젝트
  - Manufacturing Database Tuning Agent Project
description: "A verification-first guide for turning a Gemini-generated manufacturing database tuning idea into measurable backend and database engineering evidence."
author:
  - Codex
date created: 2026-09-22
date modified: 2026-09-22
tags:
  - llm-wiki
  - database-performance
  - manufacturing
  - agentic-ai
  - portfolio
topic:
  - database-performance
  - project-design
source:
  - "[[2026-09-22-Gemini-Manufacturing-Database-Performance-Agent-Conversation]]"
related:
  - "[[MOC-Portfolio]]"
  - "[[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]"
  - "[[김규태 금융 시스템 개발자 취업 로드맵]]"
status: active
explored: false
claimType: prescriptive
evidenceScope: single-source
verificationStatus: unverified
disputed: false
---

# 제조 DB 성능 최적화 에이전트 프로젝트 검증 가이드

## 핵심 판단

Gemini 대화에서 가장 재사용 가치가 높은 후보는 `자율형 슬로우 쿼리 진단 및 인덱스 튜닝 에이전트`다. 다만 지금 확보된 것은 아이디어뿐이다. 포트폴리오 증거가 되려면 LLM의 설명보다 재현 가능한 데이터셋, 실행계획, 부하 조건, 안전장치, 전후 측정값이 중심이어야 한다.

제조 도메인은 설비·작업지시·정비 이력을 제공하는 실험 맥락으로 사용한다. 실제 공장 적용이나 현업 효과가 검증된 것처럼 표현하지 않는다.

## 최소 프로젝트 범위

| 구성 | 최소 구현 |
|---|---|
| 데이터 | 설비, 생산 라인, 작업지시, 정비 이력, 센서 요약 테이블을 가진 합성 데이터 |
| 병목 | 인덱스 부재, 잘못된 조인 순서, 낮은 선택도, 정렬 spill 중 2개 이상 |
| 관찰 | PostgreSQL slow query log와 `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` 수집 |
| 판단 | 규칙 기반 진단을 기준선으로 두고 LLM은 설명·후보 생성에 제한 |
| 조치 | SQL rewrite 또는 `CREATE INDEX CONCURRENTLY` 제안 |
| 안전 | 읽기 전용 분석 계정, 허용 DDL 목록, 비용 상한, 사람 승인, rollback 문서 |
| 출력 | 원본 plan, 진단 근거, 변경 제안, 적용 전후 결과를 하나의 evidence report로 저장 |

## 에이전트 경계

에이전트가 직접 운영 DB를 임의 변경하게 만들지 않는다. 먼저 아래 순서로 제한한다.

1. slow query를 수집한다.
2. 실행계획의 실제 행 수, 예상 행 수, buffer hit/read, loop 수를 구조화한다.
3. 결정론적 규칙으로 병목 후보를 표시한다.
4. LLM은 근거를 인용해 설명하고 SQL·인덱스 후보를 만든다.
5. 격리된 복제 DB에서 후보를 적용하고 같은 부하를 재실행한다.
6. 성능과 쓰기 비용이 모두 기준을 통과할 때만 사람에게 승인을 요청한다.

이 구조에서 LLM 출력은 제안이며, 성능 개선 판정은 반복 측정 결과가 담당한다.

## 검증 설계

단일 실행 시간이나 optimizer의 `cost`만으로 개선을 주장하지 않는다. 동일한 데이터 스냅샷과 부하 스크립트에서 warm-up 뒤 여러 번 반복하고 다음을 함께 기록한다.

- p50·p95·p99 latency와 throughput
- shared buffer hit/read, temp read/write
- 계획 행 수와 실제 행 수의 오차
- CPU·메모리·디스크 사용량
- 인덱스 크기와 `INSERT`·`UPDATE` 지연 증가
- 동시 사용자 수와 락 대기 시간
- 개선되지 않거나 회귀한 쿼리

비교군은 최소 `원본`, `사람이 만든 규칙 기반 튜닝`, `에이전트 제안` 세 가지로 둔다. 그래야 LLM이 실제로 추가 가치를 만들었는지 분리할 수 있다.

## 완료 기준

- 데이터 생성과 부하 재현 명령을 새 환경에서 실행할 수 있다.
- 동일 query set에 대한 before/after 실행계획과 원시 측정값이 남는다.
- 추천이 틀린 사례와 거부 사유가 최소 1개 기록된다.
- DDL은 승인 없이는 실행되지 않으며 rollback이 검증된다.
- 본인이 plan node, 복합 인덱스 열 순서, write amplification, lock 위험을 설명하고 코드를 수정할 수 있다.
- README의 성능 수치는 원시 로그나 결과 파일로 추적된다.

## 포트폴리오 표현 경계

현재 말할 수 있는 것은 “Gemini와 대화하며 제조 AI 아이디어를 DB 성능 최적화 실험 후보로 구체화했다”까지다. 구현·측정 전에는 `자동 튜닝 시스템을 구축했다`, `성능을 94% 개선했다`, `초당 10,000건을 처리했다` 같은 문장을 사용하지 않는다.

구현 후에는 다음 형식으로 쓴다.

> 합성 제조 데이터와 고정 부하에서 PostgreSQL 실행계획을 분석하고, 안전한 튜닝 후보를 격리 환경에서 재검증하는 시스템을 구현했다. `[측정 조건]`에서 `[지표]`가 `[전]`에서 `[후]`로 변했으며, 쓰기 비용과 실패 사례도 함께 공개했다.

> [!note] Bias Check
> Counter-argument: 규칙 기반 진단만으로도 대부분의 교육용 병목을 해결할 수 있어 LLM 에이전트가 불필요할 수 있다.
> Data gap: 실제 제조 스키마·운영 부하·장기 안정성 자료가 없으며, 현재 페이지는 단일 Gemini 대화에서 출발한 미구현 설계다.

## Related

- [[2026-09-22-Gemini-Manufacturing-Database-Performance-Agent-Conversation]] — 아이디어가 좁혀진 원문 대화
- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]] — 생성 결과를 증거로 인수하는 원칙
- [[MOC-Portfolio]] — 구현·측정 이후 연결할 포트폴리오 허브
