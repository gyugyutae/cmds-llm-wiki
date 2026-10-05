---
type: wiki-page
aliases:
  - AI-Augmented Developer
  - AI 활용 개발자 포지셔닝
description: "Positioning frame for presenting AI use as leverage for developer capability rather than dependence on generated code."
author:
  - Codex
date created: 2026-07-11
date modified: 2026-10-05
tags:
  - ai
  - career
  - portfolio
  - developer-growth
source:
  - "[[2026-10-05-Kim-Gyutae-Finance-Backend-Portfolio-Purpose]]"
  - "[[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[2026-07-26-Kim-Gyutae-AI-Era-Developer-Reflection]]"
  - "[[2026-07-25-YouTube-AI시대-컴퓨터공학-교육]]"
  - "[[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]]"
related:
  - "[[김규태]]"
  - "[[김규태 Career Narrative]]"
  - "[[harness]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[코딩테스트는 AI 시대의 문제해결력 훈련이다]]"
  - "[[컴퓨팅 사고의 추상화와 분해]]"
  - "[[AI 시대의 개발자 학습 전략]]"
  - "[[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]"
confidence: medium
layer: concepts
explored: false
claimType: interpretive
evidenceScope: user-original
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: Codex
disputed: false
status: active
---

# AI-Augmented Developer Positioning

## Definition

AI-Augmented Developer Positioning은 AI를 개발 역량의 대체물이 아니라 증폭기로 설명하는 포트폴리오 프레임이다. 핵심은 "AI가 만들어줬다"가 아니라 "내가 현실 문제를 추상화하고, 블랙박스 내부를 분해하고, AI를 도구로 사용하고, 결과를 검증하고, 반복 가능한 워크플로로 만들었다"를 보여주는 것이다.

---

## Why It Matters For 김규태

김규태는 Codex, 자동화, 에이전트 워크플로를 적극적으로 사용한다. 동시에 GitHub 레포에 AI 생성 비중이 높다는 불안과, AI 없이도 개발할 수 있는 기본기를 채우고 싶다는 문제의식을 갖고 있다.

따라서 취업 포트폴리오에서는 AI 활용을 숨기기보다 다음 기준으로 분리해 설명해야 한다.

| Layer | What To Show |
|-------|--------------|
| Problem | 내가 어떤 문제를 정의했는가 |
| Abstraction | 현실 문제를 어떤 입력·출력·제약·인터페이스로 바꾸었는가 |
| Decomposition | 블랙박스를 어떤 하위 문제와 의존성으로 나누었는가 |
| Judgment | 내가 어떤 선택지를 비교하고 결정했는가 |
| AI Use | AI에게 어떤 작업을 맡겼는가 |
| Verification | 내가 결과를 어떻게 검증했는가 |
| Ownership | AI 없이도 설명하고 수정할 수 있는 부분은 무엇인가 |

---

## Strong Framing

> 저는 AI를 코드 생성 도구로만 쓰지 않고, 리서치, 실험 설계, 반복 작업 자동화, 문서화까지 연결하는 개발 워크플로 도구로 사용합니다. 동시에 AI가 만든 결과를 제 실력처럼 과장하지 않기 위해, 제가 직접 판단한 부분과 AI가 도운 부분을 분리해 기록하고 검증하려고 합니다.

---

## Weak Framing To Avoid

- "AI로 빠르게 만들었습니다"만 강조하기
- 코드 전체가 AI 생성인데 본인 설계처럼 말하기
- 수치, 테스트, 재현 방법 없이 결과만 보여주기
- AI 없이는 설명하지 못하는 프로젝트를 대표 포트폴리오로 내세우기

---

## Evidence Checklist

- AI 없이 직접 구현한 작은 기능 기록
- 코딩테스트 풀이 로그: 문제 정의, 알고리즘 선택, 복잡도, 엣지케이스, 오답 수정 과정을 AI 없이 기록
- 에이전트에게 맡긴 작업과 본인 판단의 분리 표
- 테스트 명령, 성능 수치, 재현 로그
- 실패한 AI 출력과 본인이 수정한 내역
- README에 "왜 이렇게 설계했는가"를 설명하는 문단
- 코드 작성 전 입력·출력·제약·하위 문제를 적은 설계 로그

---

## Problem-Solving Ownership

[[컴퓨팅 사고의 추상화와 분해]]는 AI 시대의 개발자 소유권을 코드 타이핑보다 앞단에 둔다. 생성형 AI가 구현 속도를 높여도 다음 질문은 개발자가 직접 답해야 한다.

- 어떤 현실 문제를 풀고 있는가?
- 성공을 어떤 출력과 지표로 판단하는가?
- 어떤 제약과 실패를 블랙박스 경계 안에 포함하는가?
- AI가 제안한 구현이 실제 목적을 만족하는지 어떻게 검증하는가?

이 관점에서 강한 AI 활용 증거는 생성 코드의 양이 아니라, 문제 구조와 검증 기준을 본인이 소유한 기록이다.

---

## From Generation To Engineering

[[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]는 초기 CRUD나 반복 코드를 빠르게 만든 다음 반드시 엔지니어링 단계로 넘어가야 한다는 사용자 원칙을 보강한다. 엣지케이스, 참조 무결성, 도메인 규칙, 트래픽 증가, 성능과 운영 실패를 테스트하지 않은 생성물은 포트폴리오의 구현 증거로 승격하지 않는다.

---

## Coding Test Link

[[코딩테스트는 AI 시대의 문제해결력 훈련이다]]는 이 포지셔닝의 기본기 증거 축이다. AI 활용 경험이 강할수록 코딩테스트 풀이 로그는 "AI 없이도 문제를 분해하고, 직접 구현하고, 복잡도와 엣지케이스를 검증할 수 있다"는 counter-evidence가 된다.

---

## Bias Check

> [!note] Bias Check
> Counter-argument: AI 활용 자체가 강점이 되려면 기본 개발 역량, 도메인 이해, 검증 능력이 같이 보여야 한다.
> Data gap: 현재는 AI 비의존 구현 증거와 코딩테스트/기초 CS 실력의 외부 검증 자료가 부족하다.

---

## Related

- [[김규태]]
- [[김규태 Career Narrative]]
- [[harness]]
- [[Human-AI Knowledge Boundary]]
- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
- [[컴퓨팅 사고의 추상화와 분해]]
- [[AI 시대의 개발자 학습 전략]]
- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]

## 2026-10-05 취업 준비 영상 인제스트 연결

[[AI 시대 주니어의 문제 진단과 좋은 코드 판단 기준]]의 발표자 의견을 추가 참고한다. AI 사용보다 본인의 문제 정의·설명·수정·검증 능력을 증거로 제시한다. [[포트폴리오 주제는 기술 문제와 도메인 가치를 함께 보여준다]]를 통해 기술적 판단이 사용자 자금·중복 거래·정합성에 주는 가치를 연결한다.

근거: [[2026-10-05-YouTube-요즘 개발자 채용 현실]], [[2026-10-05-YouTube-이력서 채용공고보고 지원동기 쓰는 방법 (보기만해도 합격률 UP)]], [[2026-10-05-YouTube-취준생 90%가 놓치는 이력서 ‘쓰기 전’ 4가지 (안 챙기면 시작부터 불리합니다)]], [[2026-10-05-YouTube-개발자 이력서만 수백개 검토하는 IT 회사 대표가 본 서류 합격 기준]], [[2026-10-05-YouTube-요즘 주니어 개발자들에게 부족한 것]], [[2026-10-05-YouTube-개발자 포폴은 OO가 전부입니다]], [[2026-10-05-YouTube-개발자 취업, 100% 성공하는 포트폴리오 작성법]], [[2026-10-05-Kim-Gyutae-Finance-Backend-Portfolio-Purpose]]. 영상에서 가져온 조언은 외부 검증을 완료하지 않은 참고 관점이다.
