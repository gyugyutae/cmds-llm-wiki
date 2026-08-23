---
type: wiki-page
aliases:
  - GitHub Developer Role Model Study Method
  - 개발자 롤모델 관찰법
description: "A repeatable evidence-based method for learning development judgment, maintenance, collaboration, documentation, and AI boundaries from public GitHub activity."
author:
  - Codex
date created: 2026-08-04
date modified: 2026-08-04
tags:
  - developer-growth
  - github
  - open-source
  - maintenance
  - documentation
source:
  - "[[2026-08-04-Q-korean-developer-role-model-github-study-map]]"
  - "[[MOC-Portfolio]]"
  - "[[AI-Augmented Developer Positioning]]"
related:
  - "[[AI 자동화는 개인 생산성 레버리지다]]"
  - "[[harness]]"
  - "[[Andrej Karpathy]]"
confidence: medium
layer: guides
explored: false
claimType: interpretive
evidenceScope: public-github-observation
verificationStatus: partial
status: active
---

# 개발자 롤모델을 GitHub에서 공부하는 법

## Core Principle

롤모델의 직함이나 star 수를 따라가는 것이 아니라, 공개된 결정 흔적을 관찰하고 자신의 작은 프로젝트에 재현한다. GitHub에서 확인 가능한 것은 코드, commit, issue, PR, review, test, release, README이다. 작성자의 내면이나 비공개 AI 사용법은 추측하지 않는다.

## Five Observation Axes

| Axis | Evidence To Read | Question |
|---|---|---|
| Problem choice | README, roadmap, first issue | 왜 이 문제를 풀었나? |
| Change size | commit history, diff, release note | 한 번에 어디까지 바꾸는가? |
| Judgment | rejected issue, review comment, design doc | 무엇을 안 하기로 결정했나? |
| Verification | tests, CI, reproduction steps, metrics | 완료를 어떤 근거로 주장하나? |
| Maintenance | changelog, compatibility, deprecation, response | 사용자와 기존 코드를 어떻게 보호하나? |

AI/agent 활용을 공개한 프로젝트에는 두 축을 추가한다.

| Axis | Question |
|---|---|
| Agent work | 에이전트가 조사·구현·테스트·문서 중 무엇을 했나? |
| Human gate | 사람이 scope, architecture, merge, release를 어떤 증거로 통제했나? |

## Weekly Study Loop

1. 한 사람의 대표 저장소 하나를 선택한다.
2. README와 CONTRIBUTING/AGENTS/ROADMAP을 먼저 읽고 프로젝트의 경계를 한 문장으로 쓴다.
3. 최근 commit 20개를 `feature`, `fix`, `test`, `docs`, `release`, `merge`로 분류한다.
4. 채택된 issue/PR 하나와 거절·보류된 issue 하나를 대조한다.
5. PR의 problem, approach, alternatives, tests, compatibility, evidence를 6줄로 요약한다.
6. 그 패턴 하나만 자신의 현재 프로젝트에 적용한다.
7. 1주 뒤에 변경이 실제로 버그, 설명력, 검증 시간을 개선했는지 회고한다.

## Observation Card

```markdown
### 이름 / 저장소 / 관찰일

- 이 프로젝트가 푸는 문제:
- 명시된 비목표/non-goal:
- commit 크기와 메시지 패턴:
- issue에서 먼저 묻는 정보:
- PR이 완료라고 판단하는 증거:
- README의 순서와 독자:
- 에이전트가 했다고 공개된 일:
- 사람의 최종 판단과 merge gate:
- 내 프로젝트에 이번 주 적용할 한 가지:
- 적용 후 검증 결과:
```

## Anti-Patterns

- star 수를 코드 품질의 단일 지표로 취급하지 않는다.
- 최근 commit 하나만 보고 전체 개발 습관으로 일반화하지 않는다.
- bot/agent commit을 작성자가 직접 쓴 코드로 혼동하지 않는다.
- 교육용·아카이브 저장소의 오래된 활동을 현재 유지보수 능력의 부재로 단정하지 않는다.
- 그대로 복제한 거대한 에이전트 하네스를 학습이라고 착각하지 않는다. 현재 문제에 필요한 gate 하나만 이식한다.

> [!note] Bias Check
> 공개 GitHub은 개발자의 일부 결과만 보여 준다. 회사 내부 코드 리뷰, 사전 기획, 실패한 시도, AI 사용량은 안 보일 수 있다. 따라서 공개 행동을 설명하되 인물의 내면을 단정하지 않는다.

## Related

- [[2026-08-04-Q-korean-developer-role-model-github-study-map]]
- [[MOC-Portfolio]]
- [[AI-Augmented Developer Positioning]]
- [[AI 자동화는 개인 생산성 레버리지다]]
- [[harness]]
