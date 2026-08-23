---
type: query-result
aliases:
  - How to Use LLM Wiki Well
  - LLM Wiki 활용법
description: Practical synthesis on how Kim Gyutae can use this standalone LLM Wiki for portfolio evidence, project learning, query reuse, and Codex workflow compounding.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - query
  - llm-wiki
  - portfolio
  - workflow
  - learning
source:
  - "[[Core Context]]"
  - "[[index]]"
  - "[[LLM Wiki Pattern]]"
  - "[[3-Layer Architecture]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[LLM Wiki as Learning Base]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
  - "[[MOC-LLM Wiki Guide]]"
  - "[[MOC-Portfolio]]"
reusableFor:
  - 취업/포트폴리오
  - 프로젝트 증거
  - Codex 개발 워크플로
  - 독서/책/학습
  - 에세이/블로그
confidence: medium
---

# 이 LLM Wiki를 잘 활용하는 방법

## Query

이 LLM Wiki를 어떻게 하면 가장 잘 활용할 수 있는가? 잘 쓰는 방법과 활용 방안은 무엇인가?

## Core Answer

이 vault의 가장 좋은 용도는 "자료 저장소"가 아니라, 김규태의 프로젝트, 학습, 의사결정, 취업 준비 증거를 계속 재사용 가능한 산출물로 컴파일하는 시스템이다. 핵심 흐름은 `Raw Sources -> Wiki -> Queries`다.

| Layer | 역할 | 잘 쓰는 법 |
|-------|------|------------|
| `10. Raw Sources/` | 원본 증거 | README, 회고, 성능 수치, 발표자료, 회의록, 면접 초안을 원문으로 보존 |
| `20. Wiki/` | 컴파일된 지식 | 프로젝트, 개념, 가이드, MOC를 연결해 반복 사용 가능한 설명 구조로 유지 |
| `30. Queries/` | 바로 쓰는 산출물 | 이력서 bullet, STAR 답변, 자기소개서 문단, 비교 분석, 약점 보강 계획을 저장 |

## Operating Principle

### 1. 넣기 전에 목적을 먼저 정한다

`/ingest`할 때는 "왜 수집했는가?"가 제일 중요하다. 목적 없는 클리핑은 나중에 검색 쓰레기가 되기 쉽다. 이 vault에서는 `collectionPurpose`를 남겨야 하므로, 자료마다 아래 중 하나를 먼저 고른다.

- 취업/포트폴리오
- 프로젝트 증거
- 백엔드/성능/금융 시스템
- 학부연구생/학술
- 강의/수업/교육
- Codex 개발 워크플로
- 제품/창업
- 에세이/블로그
- 경제적 자유/FIRE/레버리지
- 독서/책/학습

추천 문장:

```text
취업/포트폴리오 - 이 자료를 프로젝트 증거로 보존하고 이력서/면접 답변에 재사용하기 위해 수집
```

### 2. 프로젝트는 "무엇을 만들었나"보다 "무엇을 판단했나"로 저장한다

포트폴리오에서 강한 증거는 구현 목록이 아니라 판단과 검증이다. 프로젝트 자료를 넣을 때는 아래 구조로 정리하게 한다.

| 항목 | 질문 |
|------|------|
| Problem | 어떤 문제를 풀었나? |
| My Judgment | 내가 직접 판단한 것은 무엇인가? |
| Agent Work | 에이전트에게 맡긴 것은 무엇인가? |
| Implementation | 무엇을 만들었나? |
| Verification | 어떻게 검증했나? |
| Metric | 전후 수치나 결과는 무엇인가? |
| Failure | 실패와 수정은 무엇이었나? |
| Interview Line | 면접에서 1문장으로 어떻게 말할 것인가? |
| Evidence | 근거 파일, GitHub, Raw Source는 어디인가? |

AI 활용 프로젝트는 `Non-AI Core`와 `AI Boundary`를 반드시 추가한다. 이것이 AI 의존 개발자로 보이지 않게 만드는 핵심 장치다.

### 3. Query는 답을 받는 도구가 아니라 산출물을 만드는 도구로 쓴다

좋은 `/query`는 "설명해줘"보다 "어디에 쓸 산출물인지"가 분명하다.

나쁜 프롬프트:

```text
/query financial-order-latency-lab 설명해줘
```

좋은 프롬프트:

```text
/query 금융권 백엔드 신입 면접에서 financial-order-latency-lab을 2분 안에 설명할 수 있게 STAR 형식으로 정리해줘. p99 latency, 부하 테스트, 병목 분석, 내가 판단한 부분과 Codex가 도운 부분을 분리해줘.
```

### 4. Lint로 위키를 건강하게 만든다

자료를 많이 넣을수록 중요한 것은 더 많이 저장하는 것이 아니라, 중복, 낡은 주장, 약한 근거, orphan page를 제거하는 것이다. 주 1회 또는 큰 ingest 후에는 `/lint`를 돌려야 한다.

점검할 것:

- 근거 없는 포트폴리오 주장
- 수치가 없는 성능 개선 주장
- `explored: false`인데 면접 답변처럼 쓰고 있는 페이지
- `verificationStatus: unverified`인데 확정적으로 말하는 페이지
- Raw Source와 연결되지 않은 Wiki 주장

### 5. LLM Wiki는 "내가 아는 것"이 아니라 "공부할 지도"다

`explored: false`와 `verificationStatus: unverified`는 부끄러운 표시가 아니라 안전장치다. LLM이 컴파일한 페이지를 읽고, 직접 설명할 수 있을 때 `explored`를 올리는 식으로 써야 한다.

## Best Use Cases For This Vault

### 취업/포트폴리오

가장 높은 우선순위다. 현재 spine은 `financial-order-latency-lab -> Graduation-elasticsearch -> cuee -> harness`다. 이 순서로 증거를 채우면 된다.

바로 쓸 query:

```text
/query 내 포트폴리오에서 가장 강한 증거와 약한 증거를 취업 관점으로 구분해줘. 각 약점마다 어떤 Raw Source를 추가해야 하는지 알려줘.
```

```text
/query 이력서 프로젝트 bullet 5개 만들어줘. 수치, 검증 방법, 내가 직접 판단한 부분을 포함하고 과장은 제거해줘.
```

### 프로젝트 회고와 증거화

프로젝트가 끝난 뒤 README만 남기지 말고, 실패와 판단을 Raw Source로 남긴다. 특히 성능 실험, parser 검증, Android 접근성 권한 문제, Codex workflow 개선은 나중에 면접에서 설명할 재료다.

바로 쓸 query:

```text
/query financial-order-latency-lab의 evidence gap을 기준으로 다음에 추가해야 할 실험 로그, 그래프, README 섹션을 우선순위로 정리해줘.
```

### 학습

어려운 논문, GitHub repo, 기술 글은 완전히 이해한 뒤 넣는 것이 아니라, 관심이 생긴 시점에 넣고 학습 지도로 컴파일한다. 다만 나중에 직접 읽고 검증해야 한다.

바로 쓸 query:

```text
/query 내가 아직 잘 모르는 주제 중 백엔드/성능/금융 시스템 취업 준비에 가장 도움이 되는 학습 순서를 Wiki 기준으로 정리해줘.
```

### Codex 개발 워크플로

Codex와 한 중요한 개발 대화는 그냥 흘려보내지 말고, 설계 판단, 디버깅 과정, 검증 명령, 실패 원인을 Raw Source로 남긴다. 그러면 `harness`와 `AI-Augmented Developer Positioning`이 강해진다.

바로 쓸 query:

```text
/query 최근 Codex와 작업한 내용 중 포트폴리오에 쓸 수 있는 개발 판단과 단순 자동화 작업을 분리해줘.
```

### 블로그/에세이

Wiki는 Velog 글감 저장소로도 쓸 수 있다. 단순 요약 글보다 "내 프로젝트에서 배운 판단"으로 바꾸면 좋다.

바로 쓸 query:

```text
/query financial-order-latency-lab 경험을 바탕으로 'p99 latency를 처음 측정하며 배운 것'이라는 Velog 글 초안을 만들어줘. 과장 없이 취업준비생 톤으로.
```

## Weekly Routine

1. 이번 주 만든 자료를 `00. Inbox/`에 넣는다.
2. `/inbox`로 처리할 자료를 고른다.
3. `/ingest`에서 재활용 축을 명확히 답한다.
4. `/query`로 이력서 bullet, STAR 답변, 글감, 약점 보강 계획을 만든다.
5. 쓸만한 Query 결과는 `30. Queries/`에 저장한다.
6. `/lint`로 근거 없는 주장, 오래된 내용, 누락 링크를 잡는다.
7. `/reindex`로 qmd 검색을 최신화한다.

## Quality Bar

이 vault를 잘 쓰고 있는지 판단하는 기준:

- 새 자료마다 `collectionPurpose`가 있는가?
- 프로젝트마다 Raw Source 근거가 있는가?
- Query 결과가 실제 이력서/면접/블로그에 재사용 가능한가?
- "내가 판단한 것"과 "AI가 도운 것"이 분리되어 있는가?
- 수치, 검증 명령, 실패 기록이 남아 있는가?
- `explored`와 `verificationStatus`를 보고 확신도를 조절하는가?

## Current Gaps

- 프로젝트별 README, 성능 결과, 발표자료, 회고가 아직 충분히 ingest되지 않았다.
- 이력서 bullet, STAR 답변, 자기소개서 문단을 위한 전용 템플릿이 없다.
- 목표 직무가 백엔드/금융/드론/반도체 중 아직 확정되지 않아 query 산출물이 넓게 퍼질 수 있다.
- AI가 만든 부분과 본인이 직접 판단·검증한 부분의 증거가 더 필요하다.

## Reuse Axis

이 답변은 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 독서/책/학습, 에세이/블로그에 활용 가능합니다 — LLM Wiki를 단순 저장소가 아니라 재사용 가능한 산출물 생성 시스템으로 운영하는 기준을 정리했기 때문입니다.
