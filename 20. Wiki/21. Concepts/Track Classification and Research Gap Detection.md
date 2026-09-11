---
type: wiki-page
aliases:
  - Track Classification
  - Research Gap Detection
description: Unimplemented collection-coverage proposal that classifies sources into user-defined tracks; low coverage indicates a collection gap candidate, not a demonstrated research gap.
author:
  - Claude
date created: 2026-04-29
date modified: 2026-08-29
tags:
  - concept
  - command-pattern
  - skill-extension
  - research
  - systematic-review
source:
  - "[[AGENTS]]"
  - .codex/commands/ingest.md
related:
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Idea Generation Pipeline]]"
confidence: low
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

# Track Classification and Research Gap Detection

> [!tip] Key Insight
> Wiki 안에서 **어떤 분류의 수집량이 적은지**는 계산할 수 있다. 그러나 가장 빈 track은 collection gap 후보일 뿐이며, 외부 문헌의 research gap을 자동으로 뜻하지 않는다.

---

## Overview

**Track Classification and Research Gap Detection**은 LLM Wiki의 표준 `$ingest`를 확장할 수 있는 **미구현 보조 패턴**이다.

1. **트랙 분류 명령어** — 논문·자료 ingest 시 미리 정의된 thematic track 으로 분류
2. **수집 공백 보고** — 트랙별 비중을 비교해 현재 vault에서 덜 수집된 영역 표시

현재 repo에는 `track` frontmatter 규칙이나 `$track` skill이 없고, 실제 분류 정확도 측정도 없다.

---

## 작동 원리

### Step 1: Track 정의
사용자가 도메인의 thematic track 을 사전 정의:

```
예시 — 어떤 헬스케어 도메인의 5 트랙:
- 인지 자극 (cognitive stimulation)
- 신체 활동 (physical activity)
- 사회적 상호작용 (social engagement)
- 영양 개선 (nutrition)
- 기술 보조 (assistive technology)
```

### Step 2: Ingest 시 분류
향후 구현한다면 `$ingest` 뒤 별도 단계에서 agent가 raw source를 후보 track으로 분류하고, 사용자가 확인한 뒤 새 schema 필드에 기록한다. 현재 `track`은 정식 schema가 아니다.

### Step 3: 그래프 적재
트랙별 wiki 페이지 (혹은 MOC) 에 backlink 생성. 트랙 노드에서 그 트랙에 속한 모든 raw source 가 한눈에 보임.

### Step 4: Gap 분석
별도 명령으로 트랙별 raw source 비중을 집계할 수 있다.

```
트랙 A: 45%
트랙 B: 30%
트랙 C: 12%   ← Collection Gap Candidate
트랙 D: 8%    ← Collection Gap Candidate
트랙 E: 5%    ← Collection Gap Candidate
```

이 값은 vault의 수집 편향, 분류 체계, 중복 자료의 영향을 받는다. 따라서 수집 우선순위 후보로는 쓸 수 있지만 연구 방향을 자동 확정해서는 안 된다.

---

## 구현 권장 사항

### Backlink as primary signal
트랙 분류가 단순 frontmatter 필드만 채우는 게 아니라, **트랙별 개념 노트에 해당 트랙 정보가 멘션 (backlink)** 으로 기록되어야 그래프 쿼리 분석이 가능. Frontmatter 만으로는 옵시디언 그래프 뷰가 연결 인식 안 함.

### Ingest 통합 vs 별도 명령
- 옵션 A: `$ingest` 자체에 분류 통합
- 옵션 B: `$track classify <file>` 별도 명령
- 권장: 둘 다 — 처음 ingest 시 자동 분류, 나중에 트랙 정의 변경되면 재분류 가능

### Track 정의 후보 추천
LLM이 도메인에 대한 track 후보를 제안할 수는 있지만, 분류의 완전성·상호배타성·목적 적합성은 사용자가 검토해야 한다.

---

## 적용 가능 도메인

| 도메인 | Track 예시 |
|------|----------|
| 문헌 수집 관리 | 주제·방법·대상별 사용자 정의 분류 |
| 헬스케어 mechanism | 분자·세포·조직·시스템·임상 |
| 시장 분석 | 지역 (Korea·Japan·China) × 차원 (특허·매출·인력) |
| 콘텐츠 기획 | 사용자 segment × 채널 × 주제 |
| 학습 분야 | 입문·중급·고급·전문가 단계 |

→ **typology 가 명확한** 모든 도메인.

---

## Systematic Review와의 경계

이 패턴은 systematic review나 PRISMA flow의 자동화가 아니다. Track별 수집량은 검색 전략, 중복 제거, eligibility 기준, inclusion/exclusion 판단, 비뚤림 평가를 대체하지 못한다. 체계적 문헌고찰에 사용하려면 별도의 프로토콜과 사람이 확인 가능한 판정 근거가 필요하다.

---

## 제안 — `$track` skill (미구현 예시)

```
$track init [domain]      # 새 도메인의 트랙 정의 wizard
$track classify <raw>     # 단일 raw source 트랙 분류 후보
$track coverage           # 트랙별 비중 + collection gap 후보
$track migrate            # 기존 raw sources 트랙 일괄 분류 후보
```

→ 위 명령은 설계 예시일 뿐 현재 사용할 수 없다.

> [!note] Bias Check
> 낮은 내부 비중은 외부 연구 공백의 증거가 아니다. 사용자의 수집 습관과 초기 taxonomy가 결과를 만들 수 있고, LLM 분류 오류도 비중을 왜곡한다. 중요한 연구 판단에는 재현 가능한 외부 검색 전략과 명시적 포함·제외 기준이 필요하다.

---

## Related

- [[Ingest-Query-Lint Cycle]] — 확장 대상
- [[Idea Generation Pipeline]] — 보완 패턴 (수집 vs 발산)
- [[LLM Wiki Pattern]]

---

## Open Questions

> [!question] 트랙 정의의 자동화
> Domain 만 입력 (예: "치매 예방") 하면 LLM 이 적절한 트랙 5-7 개를 추천하는 메타 skill 가능?

> [!question] 멀티 트랙 Source
> 한 논문이 여러 트랙에 속할 때 어떻게 비중 계산? 0.5 씩 분배 vs 우선순위 1 트랙만 vs 모든 트랙에 1.0.

> [!question] Cohort 표준화
> Cohort 학습자 전원이 자기 도메인의 트랙 5-7 개를 정의하고 LLM Wiki 에 등록하면, **도메인 간 비교** 가 가능 — 트랙 구조 자체가 학습 outcome.
