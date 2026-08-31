---
type: wiki-page
aliases:
  - CUEE
  - 배우담
description: Kotlin Android accessibility overlay app helping users navigate KorailTalk booking flows.
author:
  - Codex
date created: 2026-07-10
date modified: 2026-08-31
tags:
  - project
  - android
  - kotlin
  - startup
source:
  - https://github.com/gyutaetae/cuee
  - https://raw.githubusercontent.com/gyutaetae/cuee/main/README.md
  - "[[2026-07-12-Kim-Gyutae-Leadership-Product-Context-v2]]"
  - "[[2026-07-12-Velog-Leadership-Product-Hackathon-Bundle]]"
  - "[[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]]"
  - https://velog.io/@gyutaetae/%EB%B0%B0%EC%9A%B0%EB%8B%B4-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%801
related:
  - "[[김규태]]"
  - "[[MOC-Portfolio]]"
  - "[[김규태 Leadership and Teaching Evidence]]"
  - "[[harness]]"
  - "[[경제적 자유는 나의 북극성이다]]"
confidence: medium
layer: entities
explored: false
claimType: project-evidence
evidenceScope: multi-source-mixed
verificationStatus: partial
status: active
---

# cuee

## Overview

`cuee`는 코레일톡에서 예매나 표 확인에 실패하는 사용자가 다음에 눌러야 할 곳만 보고 직접 누를 수 있게 돕는 접근성 오버레이 앱이다. 사용자를 대신해 예매하는 앱이 아니라, 복잡한 화면에서 선택지를 줄여 사용자가 직접 거래를 이어가게 돕는 방향이다.

전신은 `배우담`이다. `배우담`은 노인에게 듀오링고처럼 앱 사용법을 학습시키는 앱으로 출발했다. 실제 노인을 관찰하거나 인터뷰한 것은 아니며, 사용자의 어머니가 이런 기능이 필요하다고 말한 것이 최초 문제 신호였다. 이를 바탕으로 학습보다 실제 사용 순간의 안내가 낫다는 가설을 세우고 `cuee`로 방향을 전환했다. `cuee`는 사용자가 현재 화면에서 다음에 눌러야 할 버튼을 마스킹/안내로 보여주는 접근성 오버레이 앱이다.

---

## Product Signal

- GitHub 기준 Kotlin 중심 Android 프로젝트다.
- `배우담`에서 `cuee`로 전환한 핵심 판단은 "사용법을 학습시키는 것"보다 "실제 앱 사용 순간의 마찰을 바로 줄이는 것"이 더 적합하다는 점이다.
- 이 판단의 출발점은 어머니의 문제 제안이며, 실제 노인 인터뷰·관찰로 검증된 결과는 아니다.
- 사용자 제공 맥락 기준으로 김규태는 팀장으로 참여해 초기 콘셉트, 앱의 핵심 역할, 주 타깃 사용자와 마스킹 기술 전략을 제안·결정했다. 실제 코드는 AI가 작성했으므로 Android·Kotlin 기능을 직접 구현했다고 표현하지 않는다.
- 팀 규모는 5명이며, 디자이너 2명, 기획 2명, 김규태 1명(개발자/팀장)으로 구성된다.
- 타깃은 고령자만이 아니라 모바일 거래 실패율이 높은 사용자 전체다.
- README의 검증 목표는 완료시간 50% 감소, 도움 요청 횟수 70% 감소, 실패율 30%p 감소다.
- 장기 비전은 보호자 대상 B2C 검증 후 코레일 같은 기업 대상 B2B 접근성 솔루션으로 확장하는 것이다.
- 향후 목표는 Play Store 출시다.
- 사용자는 `cuee`를 아직 0에서 1로 만든 경험이라고 보지 않는다. 현재는 0 to 1 후보 또는 초기 제품화 경험으로 기록한다.
- 사용자는 [[harness]]를 사용해서 만든 것이 `cuee`라고 정리했다.
- 사용자 제공 상장 확인 결과, 김규태를 포함한 5인 팀 `큐`는 경상국립대학교 창업지원단 주최 `2026 경남권 대학생 창업동아리 창업역량강화 심화교육`에서 2026-06-16 대상을 받았다.
- 사용자 제공 상장 확인 결과, 5인 팀 `CUEE`는 `2026 학생창업유망팀 300+ 연계 G-대학생 창업유망팀 동아리 챌린지`에서 2026-08-11 우수상을 받았다.
- 사용자는 대상 대회에서 팀 리더·개발 담당으로 주요 아이디어와 콘셉트를 제안하고 발표했다고 보고했다. 이 개인 기여는 상장 자체가 아니라 사용자 자기보고 범위다.

---

## Portfolio Use

백엔드 중심 포트폴리오에서는 보조 프로젝트로 둔다. 현재는 Android/Kotlin 구현 경험이 아니라 사용자 문제 정의, 제품 방향 전환, 타깃과 기술 전략 결정, 팀 리딩 경험을 보여준다.

면접 핵심 문장:

> cuee는 노인과 모바일 거래 취약 사용자가 코레일톡에서 다음 행동을 찾지 못하는 문제를 접근성 오버레이로 줄이려 한 앱 프로젝트입니다.

제품 전환 핵심 문장:

> 처음에는 노년층의 앱 학습을 돕는 `배우담`으로 출발했습니다. 어머니가 사용 순간의 직접적인 안내가 필요하다고 말한 것을 계기로 `cuee` 접근성 오버레이 가설로 전환했으며, 실제 노인 사용자 검증은 아직 진행하지 못했습니다.

---

## Evidence Gaps

- 상장으로 확인되지 않는 개인 기여 범위와 발표자료
- `모두의 창업` 1차 탈락 이후 실제로 바꾼 행동과 경쟁사 분석 피드백의 정확한 시간 순서
- 구현한 Android 기능의 코드/화면 증거
- AI 생성 코드에서 본인이 이해·검증한 범위
- 타깃 사용자 결정과 제품 전환의 관찰·인터뷰·테스트 근거
- 실제 사용자 테스트 결과
- 발표자료와 심사 피드백
- Play Store 출시 계획과 출시 전 검증 항목
- Android accessibility 권한 심사 통과 가능성과 정책 검토

---

## Sources

- https://github.com/gyutaetae/cuee
- https://raw.githubusercontent.com/gyutaetae/cuee/main/README.md
- [[2026-07-12-Kim-Gyutae-Leadership-Product-Context-v2]]
- [[2026-07-12-Velog-Leadership-Product-Hackathon-Bundle]]
- [[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]]
- https://velog.io/@gyutaetae/%EB%B0%B0%EC%9A%B0%EB%8B%B4-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%801
