---
type: wiki-page
aliases:
  - "AI 시대 주니어의 문제 진단과 좋은 코드 판단 기준"
description: "Source-grounded finance backend career preparation guidance with explicit evidence and planning boundaries."
author:
  - Codex
date created: 2026-10-05
date modified: 2026-10-05
tags:
  - llm-wiki
  - career
  - portfolio
source:
  - "[[2026-10-05-YouTube-요즘 개발자 채용 현실]]"
  - "[[2026-10-05-YouTube-요즘 주니어 개발자들에게 부족한 것]]"
related:
  - "[[MOC-Portfolio]]"
explored: false
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: unverified
disputed: false
status: active
---

# AI 시대 주니어의 문제 진단과 좋은 코드 판단 기준

## 영상의 주장과 적용 범위

「요즘 개발자 채용 현실」은 스스로 일을 찾고 문제를 진단하는 능력을 강조한다. 「요즘 주니어 개발자들에게 부족한 것」은 AI 생성 코드에 의존할 때 코드 냄새와 좋은 코드 기준을 체득할 기회가 줄어들 수 있다고 말한다. 두 주장 모두 발표자의 경험적 의견이며 일반화된 채용 통계는 아니다.

## 직접 쌓을 판단 기준

- 입력·출력·불변조건과 실패 조건을 먼저 정의한다.
- 생성 코드나 예제를 읽고 책임이 섞인 부분, 중복, 잘못된 오류 처리를 자신의 말로 설명한다.
- 작은 기능을 직접 작성하고 정상·예외 상황을 확인한다.
- 책임 분리나 리팩터링 전후에 동작이 보존되는지 확인하고 대안의 비용을 기록한다.
- AI 조언을 채택한 이유와 본인이 이해·수정·검증한 범위를 구분한다.

[[financial-lab]]의 메모리 저장 책임 분리와 이체 실패 조건은 기존 기록에 있는 학습 사례다. 이번 인제스트는 새 구현 완료나 일일 작업을 기록하지 않는다. [[AI 시대의 개발자 학습 전략]]과 [[AI-Augmented Developer Positioning]]으로 연결한다.

> [!note] Bias Check
> Counter-argument: AI를 쓰면서도 리뷰·실험·직접 수정으로 판단 기준을 쌓을 수 있다. 사용 여부만으로 역량을 판정하지 않는다.
> Data gap: 코드 작성 대체 비용과 주니어 집단의 역량 저하를 뒷받침하는 데이터는 제공되지 않았다.

## Related

- [[MOC-Portfolio]]
