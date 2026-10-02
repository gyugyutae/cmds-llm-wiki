---
type: wiki-page
aliases:
  - 2025 글로벌 빅데이터 AI 베트남 FPT
  - FPT Vietnam AI Program
  - VIK Financial GraphRAG
description: "Four-week GNU and FPT University project-based program in Da Nang where Kim Gyutae led a multinational team building a financial semiconductor-risk GraphRAG."
author:
  - Codex
date created: 2026-09-21
date modified: 2026-09-21
tags:
  - vietnam
  - fpt
  - graphrag
  - generative-ai
  - financial-analysis
  - international-collaboration
source:
  - "[[2026-09-21-GNU-FPT-Vietnam-GraphRAG-Program-Record]]"
  - "https://github.com/VIK-GraphRAG/Finance_GraphRAG"
related:
  - "[[김규태]]"
  - "[[MOC-Portfolio]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[GNU Buddy]]"
  - "[[TMU Global Leadership Program]]"
confidence: medium
layer: entities
explored: false
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-09-21
verifiedBy: Codex
disputed: false
status: active
---

# FPT Vietnam Global Big Data AI Program

## Overview

김규태는 경상국립대학교가 주관한 `2025 글로벌 빅데이터·AI 교육 및 실무 체험 프로그램(베트남 FPT)`에 참여했다. 공식 교육 일정은 2025-12-29~2026-01-23이고, FPT 수료증은 전체 체류·PBL 범위를 2025-12-28~2026-01-24로 기록한다. 장소는 베트남 다낭 FPT University였다.

공식 Project 2는 Python·LLM·Graph science·Streamlit을 사용해 데이터의 관계를 질의할 수 있는 GraphRAG 앱을 만드는 4주 과제였다. 팀은 이 과제를 금융 및 반도체 공급망 위험 분석으로 구체화했다.

## Team And Role

- 사용자 자기보고 기준 팀 구성: 한국인 3명, 인도인 1명, 베트남인 1명.
- 공통 업무 언어: 영어.
- 김규태의 역할: 팀장, 문제 정의, 시스템 설계, 프롬프트, 생성형 AI를 활용한 코드 생성·실행, 개발 리드.
- 인도인 팀원은 UI를 담당했다.
- 개발 환경: Windows와 macOS가 섞인 팀에서 빌드가 되지 않는 문제가 발생하자 김규태가 Docker 환경을 구성했다. 이후 한국·인도·베트남 팀원들이 같은 명령으로 프로젝트를 빌드하고 실행할 수 있었다.
- 개인 핵심 제안: 분석 범위를 전체 시장에서 변동성·사이클·공급망 외부 위험에 민감한 반도체 산업으로 좁히고, 거시 요인과 기업 단위 요인을 지식 그래프에 연결해 잠재 위험 경로를 보여주는 방향.
- 최종 영어 발표는 팀이 수행했지만 김규태가 직접 발표하지는 않았다.

## Project Evidence

공개 저장소 `VIK AI - Privacy-First Financial GraphRAG`에서 다음 산출물을 확인했다. Git 기록은 `gyugyu <zn7034@gnu.ac.kr>` 55개와 `kim gyutae` 1개, 총 56개 commit이며 2026-09-21 사용자는 두 identity가 모두 본인이라고 확인했다.

- Neo4j 기반 금융 지식 그래프
- PDF·CSV·JSON 데이터 통합
- 기업·국가·산업·거시지표·재무지표 노드
- 2~3 hop 추론과 경로 시각화
- `Taiwan Strait Tension → Taiwan → TSMC → Nvidia` 공급망 위험 예시
- Streamlit 질의·데이터 적재·그래프 시각화 인터페이스
- 반도체 ontology seed, 금융 데이터 seed, 멀티홉 시스템 테스트

수료증은 김규태가 FPT Education Global·FPT University의 국제학생 PBL 프로그램을 수료했음을 증명한다. 수료증에 개별 점수나 프로젝트 평가는 없다.

## Cross-Cultural Collaboration Story

김규태는 2주 안에 기본 구현을 끝내고 남은 기간을 개선에 쓰고 싶었으나, 해외 팀원은 4주 전체 일정 안에 완성하는 방식을 선호했다고 술회했다. 영어로 자신의 의도와 일정 기대를 정확히 전달하기 어려웠다.

2026-10-03 추가 자기보고에서 사용자는 일부 팀원이 한 달 일정 안에서 천천히 개발하려고 했으며, 맡은 일을 제때 끝내지 못한 팀원도 있었다고 설명했다. 이 때문에 초반 진행이 더디다고 느꼈고, 스크럼에서 각자의 진행 정도를 공유하고 당일 업무를 정하며 서로 피드백했다고 한다. 국적에 따른 일반적 성향으로 해석하지 않고 당시 개별 팀원의 일정 기대와 실행 차이로 다룬다. 사용자는 이후 스크럼 빈도를 `매일 아침`으로 명확히 확인했다. 스크럼 후 완료율이나 갈등 해소 결과는 아직 확인되지 않았다.

이를 해결하기 위해 매일 업무 시작 전 스크럼을 두고, 각자의 당일 과업과 진행 상태를 공유했다. 자소서에서는 국적에 따른 성향으로 일반화하지 않고, `속도와 일정에 대한 기대가 다른 다국적 팀에서 일일 소통 루틴을 만든 경험`으로 표현한다.

## Portfolio Use

이 활동은 `생성형 AI에 관심이 있다`는 선언보다 다음을 증명하는 사례로 쓴다.

1. 생성형 AI·GraphRAG을 문제 정의에서 설계·프롬프트·코드 생성·실행까지 국제 팀 프로젝트에서 실행해 본 경험
2. 넓은 금융 시장 문제를 반도체 시장의 위험 추적으로 좁힌 타깃 설정
3. 영어 소통의 한계를 일일 스크럼과 진행 공유로 보완한 협업
4. Windows·macOS 차이를 Docker 공통 환경으로 통일한 협업 기반 구축
5. 수료 후 Threads 자동화·CUEE·AI workflow 활동으로 이어진 2026년 AI 실행 서사

## Evidence Gaps

- 프롬프트별 생성 코드와 본인의 직접 수정·디버깅 내역
- 코드 생성 후 본인이 직접 설명·재현·검증할 수 있는 범위
- 멘토 평가, 최종 발표자와 팀원별 산출물
- GraphRAG 답변의 정확도·인용·환각 평가 결과

> [!note] Bias Check
> 공식 계획서·수료증·저장소·56개 commit은 프로그램 참여와 결과물, 반복 개발 기록을 보여준다. 다만 코드는 본인이 설계·프롬프트하고 생성형 AI로 생성했으므로 `모든 코드를 독자적으로 직접 작성했다`고 표현하지 않는다.

## Related

- [[김규태]]
- [[GNU Buddy]]
- [[TMU Global Leadership Program]]
- [[AI-Augmented Developer Positioning]]
- [[MOC-Portfolio]]
