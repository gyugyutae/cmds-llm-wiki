---
type: wiki-page
aliases:
  - "김규태 Python 코딩테스트 교차 학습 가이드"
description: "Personal reading or study guide compiled from supplied video evidence and explicit user purpose."
author:
  - Codex
date created: 2026-10-05
date modified: 2026-10-05
tags:
  - llm-wiki
  - learning
source:
  - "[[2026-10-05-Kim-Gyutae-Reading-and-Interleaved-Learning-Purpose]]"
  - "[[2026-10-05-YouTube-뇌과학이 증명한 무엇이든 누구보다 빠르게 배우는 방법]]"
related:
  - "[[MOC-김규태 Self Knowledge]]"
explored: false
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: unverified
disputed: false
status: active
---

# 김규태 Python 코딩테스트 교차 학습 가이드

## 사용자 목적

김규태는 Python 코딩테스트 문제를 유형별로 교차해서 풀며 학습 효과를 높이고 싶다고 밝혔다. 아래 유형 묶음과 일정은 영상의 교차 연습 개념을 코딩테스트에 적용한 Codex의 실험 설계다. 영상의 수학 실험이 Python 학습에서도 같은 성과를 보장한다는 뜻은 아니다.

## 유형을 섞는 기준

처음 접하는 유형은 예제와 같은 유형의 쉬운 문제로 기본 접근을 익힌다. 스스로 한 번 설명·구현할 수 있게 된 유형 두세 개부터 섞는다. 아직 배우지 않은 고난도 유형을 한꺼번에 섞지 않는다.

| 비교 묶음 | 선택할 때 구별할 조건 | 시작 시점 |
|---|---|---|
| 해시 집계·집합 vs 정렬 후 비교 | 순서가 필요한가, 빈도/존재만 필요한가 | Python 기본 자료구조부터 |
| 완전 탐색 vs 투 포인터/슬라이딩 윈도우 | 입력 크기, 정렬, 구간 조건의 단조성 | 각 접근을 한 번 익힌 뒤 |
| DFS vs BFS | 연결·경로 탐색인가, 동일 비용 최단 거리인가 | 그래프 기본 구현 뒤 |
| 이분 탐색 vs 선형 탐색 | 정렬/단조 판단 조건이 있는가 | 탐색의 불변조건을 설명한 뒤 |
| 그리디 vs DP | 국소 선택의 정당성을 증명 가능한가, 상태가 필요한가 | 두 유형의 기본 문제 뒤 |

이는 모든 문제의 정답 분류표가 아니다. 예를 들어 음수가 포함된 합 조건에서는 단순 투 포인터의 단조 가정이 깨질 수 있다. BFS 최단 거리 조건도 간선 비용에 따라 달라진다.

## 한 회차 운영안

1. 분류 태그를 보지 않고 익힌 유형에서 세 문제를 고른다. 쉬운 재풀이, 비슷하지만 다른 전략 문제, 새 적용 문제를 섞는다.
2. 코딩 전에 입력 크기·목표·후보 두 개·선택 이유·예상 복잡도를 적는다.
3. 직접 풀고 실패 입력과 정답/해설로 피드백을 받는다. AI를 썼다면 힌트 범위를 기록한다.
4. 답을 가린 채 핵심 흐름과 반례를 설명한다.
5. 다음 날, 3일 뒤, 일주일 뒤 중 가능한 시점에 재풀이한다. 간격은 출발점이며 기억 상태에 맞춰 조절한다.

## 무엇으로 효과를 판단할까

문제 수보다 전략 선택의 정확성, 도움 없이 구현한 비율, 유형 선택 오류와 구현 오류의 구분, 며칠 뒤 새 유사 문제의 성공 여부를 기록한다. 교차 전후 난이도와 시간을 비슷하게 맞춰 2주 뒤 운영을 조정한다. 아직 사용자의 실제 결과는 없다.

연결: [[메타인지 학습 루프]], [[코딩테스트는 AI 시대의 문제해결력 훈련이다]], [[김규태 Work and Learning Operating Guide]].

> [!note] Bias Check
> Counter-argument: 영상 조언의 효과는 과제·기존 지식·상황에 따라 다를 수 있다. 직접 시도한 결과와 반례를 함께 기록한다.
> Data gap: 책/논문 원문 및 사용자의 실제 적용 성과는 이번 인제스트에서 검증하지 않았다.
