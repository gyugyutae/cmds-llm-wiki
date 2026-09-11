---
type: wiki-page
aliases:
  - AI-Era Developer Learning Strategy
  - AI 시대 개발자 공부법
description: "A personal learning strategy that combines foundations, abstraction, decomposition, domain knowledge, metacognition, AI collaboration, and verification."
author:
  - Codex
date created: 2026-07-26
date modified: 2026-08-29
tags:
  - ai
  - developer-learning
  - computer-science
  - problem-solving
  - career
source:
  - "[[2026-07-25-YouTube-AI시대-컴퓨터공학-교육]]"
  - "[[2026-07-13-YouTube-AI시대-공부법]]"
  - "[[2026-07-13-YouTube-Shorts-AI시대-도메인-지식]]"
  - "[[2026-07-25-Gemini-Computational-Thinking-Abstraction]]"
  - "[[2026-07-25-Gemini-Computational-Thinking-Decomposition]]"
  - "[[2026-07-26-Kim-Gyutae-AI-Era-Developer-Reflection]]"
  - "[[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]]"
related:
  - "[[컴퓨팅 사고의 추상화와 분해]]"
  - "[[메타인지 학습 루프]]"
  - "[[일반 지식보다 도메인 지식이 중요해지는 이유]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]"
confidence: medium
layer: concepts
explored: false
claimType: interpretive
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: Codex
disputed: false
status: active
---

# AI 시대의 개발자 학습 전략

## Core Idea

AI가 코드와 설명을 빠르게 생성할수록 개발자 학습의 목표는 문법 암기에서 **좋은 문제를 선택하고 구조화하며 결과를 검증하는 능력**으로 이동한다. 그렇다고 기초지식이 불필요해지는 것은 아니다. 머릿속 기초지식은 질문의 방향, AI 답변의 오류 감지, 낯선 문제의 전이 학습을 가능하게 한다.

이 페이지는 여러 클리핑의 주장을 검증된 교육 이론으로 확정하지 않고, 김규태가 앞으로 실험할 개인 학습 전략으로 컴파일한다.

## Learning Stack

| 층 | 배울 것 | 결과물 |
|---|---|---|
| Foundations | 자료구조, 알고리즘, DB, OS, 네트워크, 언어 기본기 | AI 없이 설명·구현한 풀이와 작은 기능 |
| Problem Framing | 사용자 문제, 목표, 제약, 입력과 출력 | 문제정의 문서와 acceptance criteria |
| Computational Thinking | [[컴퓨팅 사고의 추상화와 분해|추상화와 분해]] | 설계도, 데이터 흐름, 모듈 경계 |
| Domain | 금융·백엔드·드론·반도체의 현장 지식 | 도메인별 기술 노트와 프로젝트 판단 |
| AI Collaboration | 질문, 대안 탐색, 코드·테스트 보조 | AI가 한 것과 내가 판단한 것의 분리 로그 |
| Verification | 테스트, 복잡도, 성능, 반례, 사용자 피드백 | 재현 명령, 측정값, 실패·수정 기록 |
| Metacognition | 무엇을 알고 모르는지 진단 | [[메타인지 학습 루프|오답·학습 회고]] |

## Why Foundations Still Matter

AI 시대 공부를 “무엇을 외웠는가”만으로 평가할 수는 없다. 그러나 사전지식이 전혀 없으면 다음 문제가 생긴다.

- 중요한 질문과 사소한 질문을 구분하기 어렵다.
- AI가 그럴듯하게 만든 오류를 발견하기 어렵다.
- 도메인 제약과 시스템 trade-off를 설명하기 어렵다.
- 다른 문제에서 재사용할 추상 패턴을 만들기 어렵다.

따라서 목표는 모든 사실의 암기가 아니라, 문제를 이해하고 검증할 수 있는 **작동하는 내부 모델**을 만드는 것이다.

## Weekly Practice

1. 이번 주에 해결할 실제 문제 하나를 고른다.
2. 코드를 보기 전에 문제의 입력·출력·제약·성공 기준을 쓴다.
3. 블랙박스를 하위 문제와 의존성으로 분해한다.
4. 핵심 한 조각은 AI 없이 직접 구현한다.
5. AI에는 대안, 반례, 테스트, 설명을 요청하되 정답 소유권을 넘기지 않는다.
6. 실제 실행, 테스트, 성능 또는 사용자 반응으로 검증한다.
7. `AI gave / I decided / I verified / I learned`를 분리해 기록한다.

## Portfolio Meaning

이 전략은 “AI를 잘 쓴다”와 “개발 기본기가 있다”를 경쟁시키지 않는다. [[MOC-Portfolio]]에서는 다음 조합으로 증거를 남긴다.

> 실제 프로젝트로 문제 정의와 운영 판단을 보여주고, 코딩테스트와 기초 구현으로 비-AI 기본기를 보여주며, AI 작업 경계와 검증 로그로 도구 활용 능력을 보여준다.

[[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]는 이 학습 전략을 구현 단계로 연결한다. AI가 만든 초안을 작은 단위로 나누고 정상·경계·실패 테스트, 도메인 규칙, 성능과 운영 조건을 확인한 뒤 직접 설명·수정 가능한 상태로 인수한다.

> [!note] Bias Check
> Counter-argument: AI 도구의 발전으로 필요한 세부 기술은 계속 바뀔 수 있으며, 모든 개발 직무가 같은 학습 우선순위를 갖지는 않는다.
> Data gap: 이 전략이 김규태의 코딩테스트 성과, 프로젝트 품질, 학습 유지율을 개선하는지는 아직 측정하지 않았다.

## Related

- [[컴퓨팅 사고의 추상화와 분해]]
- [[메타인지 학습 루프]]
- [[일반 지식보다 도메인 지식이 중요해지는 이유]]
- [[AI-Augmented Developer Positioning]]
- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
- [[김규태 Career Narrative]]
- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]
