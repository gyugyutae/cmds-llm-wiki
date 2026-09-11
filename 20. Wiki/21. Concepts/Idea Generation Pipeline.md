---
type: wiki-page
aliases:
  - Idea Generation Pipeline
  - Source-to-Idea Trigger
description: Unimplemented workflow proposal for using a newly ingested source and selected domain context as an optional idea-divergence prompt.
author:
  - Claude
date created: 2026-04-29
date modified: 2026-08-29
tags:
  - concept
  - workflow
  - idea-generation
  - creativity
  - research
  - llm-wiki
source:
  - "[[AGENTS]]"
  - .codex/commands/ingest.md
related:
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Track Classification and Research Gap Detection]]"
  - "[[LLM Wiki Pattern]]"
confidence: medium
layer: concepts
status: active
explored: false
claimType: prescriptive
evidenceScope: synthesis-only
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: Codex
disputed: false
---

# Idea Generation Pipeline

> [!tip] Key Insight
> **"새 자료를 선택적 아이디어 trigger로 사용할 수 있다"**. 현재 ingest가 자동으로 아이디어를 생성하는 것은 아니며, 사용자가 원할 때 새 source와 관련 도메인 컨텍스트를 함께 읽혀 발산을 시도하는 제안이다.

---

## Overview

**Idea Generation Pipeline**은 source ingest 뒤에 선택적으로 아이디어 발산을 붙이는 LLM Wiki 워크플로 제안이다. 현재 저장소의 `$ingest` skill에는 이 단계가 구현되어 있지 않으며, 아이디어의 신규성이나 품질을 입증한 cohort 측정도 확인되지 않았다.

핵심은 source 보존과 Wiki 컴파일을 유지한 채, 별도 요청에서 **창의적 발산**을 시도하는 것이다.

---

## 작동 원리

### Step 1: 도메인 시드 (seed) 컨텍스트 정의
사용자가 자기 연구 도메인의 핵심 framework·문제·관심을 wiki 에 미리 등록 (concept 페이지 들로).

```
예시 — 의학 연구 시드:
- 분야 기초 개념
- 현재 기술 현황
- 핵심 문제·한계
```

### Step 2: 새 raw source ingest
표준 `$ingest` 흐름을 먼저 완료한다. 이후 사용자가 원할 때 source와 선택한 시드 컨텍스트를 함께 검토한다.

### Step 3: 아이디어 생성 trigger
ingest 완료 뒤 agent에게 별도로 명시할 수 있는 prompt:

```
"이 새 raw source 가 [도메인 시드] 와 결합하면 어떤 새 아이디어가 가능한가?
- 기존에 없던 application
- 기존 문제의 새 해결 angle
- 기존 framework 의 확장
이미 wiki 에 있는 아이디어와 중복 없이 1-3 개 제시."
```

### Step 4: 아이디어 노트 생성
출력된 아이디어는 우선 `30. Queries/`에 가설로 저장한다. 반복 사용 가치와 근거가 확인된 경우에만 기존 `20. Wiki/21. Concepts/` 구조로 승격한다. 현재 vault에는 `20. Wiki/Ideas/` 폴더가 없다.

### Step 5: 누적 효과
시간이 흐르며 참조 가능한 컨텍스트가 늘어날 수는 있다. 그러나 컨텍스트 양이 아이디어 품질 향상으로 이어지는지는 별도 평가가 필요하다.

---

## 기본 워크플로와의 차이

| 축 | 기본 ingest/query | 선택적 아이디어 발산 |
|---|---|---|
| 목적 | source 보존, Wiki 컴파일, 질의 | 새 적용·가설 후보 생성 |
| 출력 | Raw Source, Wiki, Query | 검증 전 아이디어 후보 |
| 실행 시점 | 현재 skill에 구현됨 | 필요할 때 별도 요청 |

요약·검색 도구도 아이디어 발산에 사용할 수 있으므로, 이 패턴의 차이는 제품 자체가 아니라 **사용자가 추가한 워크플로 단계**에 있다.

---

## 적용 가능 도메인

| 도메인 | 시드 | 아이디어 형태 |
|------|-----|----------|
| 헬스케어 | 메커니즘 · 임상 | 새 콘텐츠 앵글, 신서비스 |
| 비즈니스 | 회사 강점·약점·시장 | 신제품 idea, 경쟁 우위 발견 |
| 스포츠 | 종목·전술 | 새 분석 방법 |
| 학술 | 논문 분야 | 연구 갭 + 신가설 |
| 창업·창작 | 도메인 + 페르소나 | 콘텐츠 기획, 스토리 idea |

---

## 제안 — `$idea` skill (미구현 예시)

```
$idea seed [domain]        # 시드 컨텍스트 정의
$idea trigger <raw>        # 새 raw source 로부터 아이디어 도출
$idea list                 # 누적 아이디어 보기
$idea promote <id>         # 검증된 아이디어를 정식 concept 후보로 승격
```

[[Track Classification and Research Gap Detection]] 와 보완:
- Track Classification: **수집 방향** 안내 (어디가 비어있나)
- Idea Generation Pipeline: **창의 발산** 안내 (지금 자료로 무엇을 새로 할 수 있나)

---

## 위험·한계

1. **Hallucination 위험** — "새 아이디어" 가 사실은 기존 idea 의 표현 변경일 뿐일 수 있음. 중복 검사 + lint 필요.
2. **품질 변동** — 시드 컨텍스트 빈약하면 아이디어도 빈약. 초기 학습자에겐 어려움.
3. **Query 토큰 추가** — ingest 마다 idea generation prompt 추가 → [[Cohort Token Economy]] 압박. 옵션으로 제공 + on-demand 호출 권장.

> [!note] Bias Check
> LLM이 생성한 표현의 낯섦은 실제 신규성의 증거가 아니다. 기존 Wiki 중복 검사만으로도 선행 연구·제품·특허와의 중복을 배제할 수 없으므로, 중요한 아이디어는 외부 1차 자료와 prior-art 검색으로 별도 검증해야 한다. 이 vault에는 아이디어 수나 품질 향상을 입증하는 측정이 없다.

---

## Related

- [[Ingest-Query-Lint Cycle]] — 본 패턴이 확장하는 cycle
- [[Track Classification and Research Gap Detection]] — 보완 skill
- [[LLM Wiki Pattern]]
- [[Cohort Token Economy]] — 비용 trade-off

---

## Open Questions

> [!question] 아이디어 노드의 wiki 적재 방식
> 현재는 검증 전 산출물을 `30. Queries/`에 두고, 반복 사용 가치가 확인된 항목만 Concept로 승격하는 편이 기존 구조와 맞는다.

> [!question] 시드 풍부화 모니터링
> 시드 컨텍스트가 시간에 따라 두꺼워지는 정도를 측정 가능한 지표 — concept page 수, 백링크 밀도, embedding cluster size 등.

> [!question] 아이디어 검증 통합
> 생성된 아이디어를 그대로 두지 말고 외부 검색 (학술 DB, 특허 DB) 과 cross-check 해 "이미 누가 했는지" 확인하는 후속 skill.
