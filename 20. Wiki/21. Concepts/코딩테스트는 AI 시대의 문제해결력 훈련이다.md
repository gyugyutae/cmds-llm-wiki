---
type: wiki-page
aliases:
  - Coding Test As AI-Era Problem Solving Training
  - 코딩테스트와 AI 시대 기본기
description: "Concept page framing coding test preparation as evidence of AI-era problem solving, computational thinking, and non-AI implementation fundamentals."
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-26
tags:
  - coding-test
  - problem-solving
  - computational-thinking
  - career
  - ai
source:
  - "[[Core Context]]"
  - "[[김규태 Career Narrative]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[개발자 커리어로 경제적 자유에 가까워지기]]"
  - "Microsoft Careers Technical Interviewing"
  - "NACE Career Readiness Competencies 2024"
  - "[[2026-07-25-Gemini-Computational-Thinking-Abstraction]]"
  - "[[2026-07-25-Gemini-Computational-Thinking-Decomposition]]"
  - "[[2026-07-25-YouTube-AI시대-컴퓨터공학-교육]]"
related:
  - "[[김규태]]"
  - "[[MOC-Portfolio]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[AI 자동화는 개인 생산성 레버리지다]]"
  - "[[개발자 커리어로 경제적 자유에 가까워지기]]"
  - "[[컴퓨팅 사고의 추상화와 분해]]"
  - "[[메타인지 학습 루프]]"
confidence: medium
layer: concepts
explored: false
claimType: interpretive
evidenceScope: mixed
verificationStatus: partial
status: active
---

# 코딩테스트는 AI 시대의 문제해결력 훈련이다

## Core Idea

코딩테스트 준비는 단순히 취업 필터를 통과하기 위한 문제 풀이가 아니라, AI 시대에도 변하지 않는 문제해결력과 컴퓨팅 사고력을 훈련하는 방법이다.

특히 김규태에게 코딩테스트는 [[AI-Augmented Developer Positioning]]의 약한 고리를 보강한다. Codex와 AI workflow를 적극 활용하더라도, AI 없이 문제를 분해하고, 자료구조를 선택하고, 복잡도와 엣지케이스를 검증할 수 있다는 증거가 필요하다.

[[컴퓨팅 사고의 추상화와 분해]] 관점에서 코딩테스트는 현실 문제 전체를 대신하지는 않지만, 입력·출력·제약을 읽고 문제를 추상 구조로 바꾸며 블랙박스 내부를 작은 단계로 나누는 제한된 훈련장이다. [[메타인지 학습 루프]]를 붙이면 정답 개수보다 오답 원인과 수정 능력을 기록할 수 있다.

---

## What It Trains

| 훈련 대상 | 의미 | AI 시대 차별점 |
|---|---|---|
| 문제 분해 | 입력, 출력, 제약, 목표를 분리한다 | AI에게 맡길 작업을 정확히 정의한다 |
| 추상화 | 문제를 배열, 그래프, 트리, DP, 해시 같은 구조로 바꾼다 | 겉보기 다른 문제의 공통 구조를 본다 |
| 복잡도 감각 | 시간/공간 복잡도를 계산하고 병목을 예상한다 | AI 출력의 비효율을 잡아낸다 |
| 구현 소유권 | 제한 시간 안에 직접 동작하는 코드를 만든다 | AI 없이도 최소 구현이 가능하다는 신뢰를 준다 |
| 엣지케이스 | 빈 입력, 중복, 최대 크기, 경계값을 확인한다 | 생성 코드의 환각과 누락을 검증한다 |
| 기술 커뮤니케이션 | 접근법, trade-off, 실패와 수정을 설명한다 | 면접과 협업에서 사고 과정을 드러낸다 |

---

## What Not To Overclaim

코딩테스트만 잘한다고 좋은 개발자가 되는 것은 아니다. 실제 개발에는 요구사항 이해, 기존 코드 읽기, 테스트, 배포, 장애 대응, 사용자 문제 정의, 팀 협업이 필요하다.

따라서 코딩테스트는 [[MOC-Portfolio]]의 프로젝트 증거를 대체하는 것이 아니라 보완해야 한다. 가장 좋은 포지셔닝은 `프로젝트로 실제 문제 해결을 보여주고, 코딩테스트로 비-AI 기본기와 계산적 사고를 증명한다`는 조합이다.

---

## Evidence Shape

코딩테스트 풀이를 포트폴리오 증거로 남기려면 단순 정답 수보다 풀이 회고가 중요하다.

권장 로그 형식:

```text
Problem:
Constraint:
First idea:
Chosen data structure / algorithm:
Complexity:
Edge cases:
Mistake / fix:
AI use:
Project transfer:
```

`AI use`는 처음 풀이에서는 `none`으로 두고, 풀이 후 리뷰나 대안 비교에 AI를 사용했다면 그 경계를 기록한다.

---

## AI-Assisted Learning Loop

문제 풀이 중 막혔을 때 AI는 정답 생성기가 아니라 학습 보조 역할로 제한한다.

| 상황 | AI 역할 | 남겨야 할 본인 소유권 |
|---|---|---|
| 문제 이해가 막힘 | 요구사항과 제약을 다시 설명하게 한다 | 내가 이해한 문제를 다시 쓴다 |
| 접근법이 안 떠오름 | 단계별 힌트를 받는다 | 최종 알고리즘 선택은 직접 한다 |
| 디버깅이 막힘 | 실패 입력에서 변수 변화를 추적하게 한다 | 수정 코드는 직접 작성한다 |
| 엣지케이스 실패 | 반례와 테스트 유형을 생성하게 한다 | 반례가 왜 깨지는지 직접 설명한다 |
| 풀이 후 | 복잡도, 더 나은 풀이, 회고 포인트를 리뷰받는다 | 내가 배운 패턴을 한 문장으로 기록한다 |

권장 프롬프트:

```text
정답이나 코드 말고, 내가 다음으로 생각해야 할 질문 3개만 줘.
```

```text
아래 코드를 고쳐주지 말고, 이 입력에서 변수 값이 어떻게 변하는지 단계별로 추적해줘.
```

```text
내 접근법이 실패할 수 있는 엣지케이스를 유형별로 만들어줘. 정답 코드는 주지 마.
```

이 루프의 핵심은 [[Human-AI Knowledge Boundary]]를 유지하는 것이다. AI가 제공한 것은 `hint`, `trace`, `edge-case`, `review`로 기록하고, 최종 판단과 수정은 본인이 한 것으로 분리한다.

---

## Bias Check

> [!note] Bias Check
> Counter-argument: AI-assisted interview와 실무형 codebase task가 늘어나면 전통적인 알고리즘 문제만으로는 충분하지 않다.
> Data gap: 김규태의 실제 코딩테스트 풀이 로그, 목표 회사별 최신 전형, AI-assisted coding interview 경험은 아직 Raw Source로 수집되지 않았다.

---

## Related

- [[AI-Augmented Developer Positioning]]
- [[김규태 Career Narrative]]
- [[MOC-Portfolio]]
- [[개발자 커리어로 경제적 자유에 가까워지기]]
- [[Human-AI Knowledge Boundary]]
- [[컴퓨팅 사고의 추상화와 분해]]
- [[메타인지 학습 루프]]

## External Sources

- Microsoft Careers, Technical Interviewing: https://careers.microsoft.com/v2/global/en/hiring-tips/technical-interviewing
- NACE Career Readiness Competencies 2024: https://www.naceweb.org/docs/default-source/default-document-library/2024/resources/nace-career-readiness-competencies-revised-apr-2024.pdf
