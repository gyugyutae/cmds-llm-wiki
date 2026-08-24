---
type: wiki-page
aliases:
  - AI-Assisted Engineering Beyond Vibe Coding
  - 검증 가능한 AI 개발
description: "A user-derived engineering loop that turns rapid AI code generation into decomposed, testable, domain-aware, and maintainable software work."
author:
  - Codex
date created: 2026-08-24
date modified: 2026-08-24
tags:
  - ai-assisted-engineering
  - testing
  - software-engineering
  - developer-workflow
source:
  - "[[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]]"
related:
  - "[[AI-Augmented Developer Positioning]]"
  - "[[컴퓨팅 사고의 추상화와 분해]]"
  - "[[AI 시대의 개발자 학습 전략]]"
  - "[[Human-AI Knowledge Boundary]]"
confidence: medium
layer: concepts
explored: false
claimType: prescriptive
evidenceScope: user-original
verificationStatus: unverified
status: active
---

# AI 보조 엔지니어링은 생성보다 검증이 중요하다

## Core Idea

김규태의 독서 메모는 바이브 코딩을 초기 생성 속도에 집중한 방식으로, AI 보조 엔지니어링을 지속 가능한 속도와 신뢰성을 만드는 방식으로 구분한다. 핵심 전환은 프롬프트 기교 자체가 아니라 **문제 분해, 도메인 규칙, 테스트, 비기능 요구사항, 결과 소유권**을 다시 사람이 붙잡는 데 있다.

## 전환 루프

```text
빠른 초안
→ 입력·출력·제약 명시
→ 작은 검증 단위로 분해
→ 정상·경계·실패 테스트
→ 도메인 규칙과 참조 무결성 확인
→ 성능·동시성·운영 조건 검증
→ 설명·수정 가능한 상태로 인수
```

## AI에 요청할 검증 질문

- 이자율이나 수량이 0이면 어떻게 되는가?
- 트래픽이 100배 늘면 어디서 병목이 생기는가?
- 함수 단위 테스트와 실패 테스트는 무엇인가?
- 기존 스키마·엔드포인트·조직 패턴과 충돌하지 않는가?
- 생성된 구현 중 내가 직접 설명하거나 수정하지 못하는 부분은 어디인가?

## 포트폴리오 증거

강한 증거는 “AI로 만들었다”는 설명이 아니라 `내가 정한 제약 / AI가 만든 초안 / 실패한 테스트 / 내가 수정한 판단 / 재현 명령과 결과`가 연결된 기록이다.

> [!note] Bias Check
> Counter-argument: AI 보조 엔지니어링이라는 이름만 붙여도 설계·기본기·도메인 이해가 자동으로 생기지는 않는다.
> Data gap: 이 루프가 실제 프로젝트의 결함률, lead time, 유지보수성을 개선했는지는 아직 측정하지 않았다.

## Related

- [[AI-Augmented Developer Positioning]]
- [[컴퓨팅 사고의 추상화와 분해]]
- [[AI 시대의 개발자 학습 전략]]
- [[Human-AI Knowledge Boundary]]
