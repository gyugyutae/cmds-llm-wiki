---
type: query-result
aliases:
  - Personal Context Knowledge Compounding Query Feedback
  - LLM Wiki Personal Context Layer Query
description: Synthesis on how an LLM Wiki compounds personal knowledge, how saved query results appear in Obsidian Graph View, and when query insights should be promoted into durable Wiki concepts.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - query
  - llm-wiki
  - personalization
  - knowledge-compounding
  - obsidian
source:
  - "[[Core Context]]"
  - "[[김규태]]"
  - "[[LLM Wiki Pattern]]"
  - "[[RAG vs Compiled Wiki]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[LLM Wiki as Learning Base]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[Agent-Readable Metadata]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
  - "[[Schema Engineering for LLM Wiki]]"
reusableFor:
  - Codex 개발 워크플로
  - 독서/책/학습
  - 에세이/블로그
  - 취업/포트폴리오
confidence: medium
---

# Personal Context, Knowledge Compounding, Query Feedback

## Query

LLM Wiki의 가장 큰 장점은 나에 대한 가장 양질의 정보를 LLM에게 줄 수 있다는 점이다. LLM 모델 성능은 상향 평준화되고 있지만, 개인에게 맞춤화된 LLM은 아직 부족하다. 그 이유는 개인의 맥락과 정보를 충분히 제공하지 못하기 때문이다. LLM Wiki는 이 문제를 해결할 수 있고, 위키를 구성하면서 사용자가 자기 생각을 더 잘 파악하게 된다. 이 관점에서 지식을 어떻게 복리로 쌓을 수 있는가? Query 결과는 Obsidian Graph View에 추가되는가? Query가 새 Wiki 개념을 만드는가? Query 내용을 Wiki에 추가할지 판단 기준은 무엇인가?

## Core Answer

LLM Wiki의 가장 큰 가치는 단순한 지식 저장이 아니라 **개인 맞춤형 LLM을 위한 고품질 context layer**를 만든다는 점이다. 모델 성능이 좋아질수록 차이는 "어떤 모델을 쓰는가"보다 "모델에게 나에 대해 얼마나 좋은 맥락을 줄 수 있는가"에서 생긴다.

이 vault에서는 그 맥락이 [[Core Context]], [[김규태]], 프로젝트 Wiki 페이지, 학습 개념, Query 결과, Raw Source 근거로 누적된다. 즉 LLM Wiki는 "나를 기억하는 프롬프트"가 아니라, LLM이 읽고 쓸 수 있는 **개인 지식 코드베이스**에 가깝다.

## 1. 지식을 복리로 쌓는 방법

지식 복리는 좋은 source 하나가 한 번 쓰이고 끝나는 것이 아니라, 다음 source와 다음 질문의 출발점이 될 때 생긴다. [[RAG vs Compiled Wiki]]의 표현처럼 RAG의 일회성 답변은 단리에 가깝고, LLM Wiki의 저장된 Wiki/Query 결과는 복리에 가깝다.

복리 구조는 다음 루프로 만든다.

| 단계 | 해야 할 일 | 복리 효과 |
|------|------------|-----------|
| Source 큐레이션 | 감명받은 글, 프로젝트 로그, 회고, 책 메모를 Inbox에 넣는다 | 좋은 재료가 쌓인다 |
| Purpose gate | 왜 수집했는지 `collectionPurpose`로 남긴다 | 나중에 재사용 방향이 보존된다 |
| Ingest | Raw Source는 보존하고 Wiki page로 컴파일한다 | 원문과 해석이 분리된다 |
| Cross-link | 관련 개념, 프로젝트, MOC와 연결한다 | Graph View에서 생각의 구조가 보인다 |
| Query | 쌓인 Wiki에 좋은 질문을 던진다 | 단순 검색이 아니라 새 합성이 생긴다 |
| Save Query | 중요한 답변을 `30. Queries/`에 저장한다 | 질문 자체도 지식 자산이 된다 |
| Promote | 반복 가능한 insight는 Wiki page로 승격한다 | 다음 질문의 출발점이 더 좋아진다 |
| Lint/Verify | orphan, 모순, 검증 부족, `explored` 상태를 점검한다 | 품질이 무너지지 않는다 |

핵심은 "많이 넣기"보다 **다음 질문을 더 좋은 질문으로 만드는 구조**다. 좋은 Query 결과가 다시 Wiki에 들어가면, 다음 Query는 더 깊은 맥락에서 시작한다. 이것이 LLM Wiki의 지식 복리다.

## 2. Query 결과는 Graph View에 추가되는가

조건부로 추가된다.

`/query` 결과가 `30. Queries/`에 markdown 파일로 저장되고, 그 안에 `[[LLM Wiki Pattern]]`, `[[김규태]]` 같은 wikilink가 있으면 Obsidian Graph View에서 하나의 노드로 보일 수 있다. 이 query 파일이 다른 Wiki 페이지를 링크하면 graph edge도 생긴다.

다만 다음 경우에는 안 보이거나 약하게 보일 수 있다.

- Query 결과를 파일로 저장하지 않고 대화로만 끝낸 경우
- Obsidian Graph View 필터에서 `30. Queries/` 폴더를 제외한 경우
- Query 결과 안에 wikilink가 거의 없는 경우
- Obsidian이 새 파일을 아직 indexing하지 않은 경우

즉 Query는 자동으로 "생각의 흔적" 노드가 될 수 있지만, graph에서 의미 있게 보이려면 저장된 Query 안에 관련 Wiki 링크가 충분히 있어야 한다.

## 3. Query를 하면 새 Wiki 개념도 자동으로 추가되는가

모든 Query가 새 Wiki 개념을 만들지는 않는다. 이 harness의 원칙은 다음에 가깝다.

> Query result는 기본적으로 `30. Queries/`에 저장하고, 그 안에서 발견된 durable insight만 `20. Wiki/`로 승격한다.

판단 기준은 다음과 같다.

| 상황 | 처리 |
|------|------|
| 일회성 답변, 데모 문구, 발표 스크립트 | Query Result로만 저장 |
| 기존 개념을 더 정확하게 만드는 내용 | 기존 Wiki page 업데이트 |
| 여러 페이지를 연결하는 새 추상 개념 | 새 Concept page 생성 |
| 특정 제품/사람/도구에 대한 안정적 정보 | 새 Entity page 생성 |
| 반복 가능한 절차나 사용법 | 새 Guide page 생성 |
| 사용자의 정체성, 목표, 운영 원칙 변화 | [[Core Context]] 업데이트 후보 |
| 원문 증거나 외부 자료 | Raw Source로 별도 ingest |

새 Wiki 개념을 만들 만한 신호는 네 가지다.

1. 앞으로 여러 번 다시 쓸 이름이 있다.
2. 기존 페이지 3개 이상을 연결한다.
3. 일회성 문장이 아니라 운영 원칙이나 패턴이다.
4. 다음 Query의 검색/추론 출발점이 될 수 있다.

이번 Query에서는 "LLM Wiki가 개인 맞춤형 LLM을 위한 고품질 맥락층이 된다"는 관점이 반복 사용 가능한 개념이므로 [[Personal Context Layer for LLM Wiki]]로 승격했다.

## 4. 나에 대한 양질의 정보가 왜 중요한가

LLM 모델이 점점 좋아질수록, 일반 지식 답변은 상향 평준화된다. 그때 차이를 만드는 것은 사용자의 개인 맥락이다.

LLM에게 필요한 개인 맥락은 단순 프로필이 아니다.

- 지금 어떤 프로젝트를 하고 있는가
- 어떤 문제의식으로 자료를 모으는가
- 어떤 기술과 도메인에 관심이 있는가
- 무엇을 직접 판단했고 무엇을 AI에게 맡겼는가
- 어떤 표현은 과장이고 어떤 증거는 강한가
- 장기적으로 어떤 삶의 방향을 보고 있는가
- 어떤 글과 질문에 반복해서 감명받는가

이 정보는 한 번에 프롬프트로 쓰기 어렵다. 그래서 Wiki에 외부화해야 한다. [[Core Context]]는 압축된 자기 맥락이고, [[김규태]] 페이지는 owner entity이며, 프로젝트와 개념 페이지는 사용자의 경험과 관심사를 분산 저장한다. Query 결과는 그 맥락을 실제 산출물로 바꾼 흔적이다.

이렇게 쌓인 Wiki를 읽은 LLM은 일반적인 조언보다 "김규태에게 맞는" 답변을 줄 가능성이 높아진다. 이 점이 LLM Wiki의 personalization 가치다.

## 5. 자기 이해 도구로서의 Graph View

Obsidian Graph View는 단순히 예쁜 시각화가 아니다. 사용자의 머릿속에 흩어져 있던 생각이 어떤 클러스터로 묶이는지 보여준다.

예를 들어 이 vault에서는 다음 클러스터가 보인다.

- 취업/포트폴리오: [[김규태]], [[MOC-Portfolio]], 프로젝트 entity들
- LLM Wiki 운영: [[LLM Wiki Pattern]], [[Ingest-Query-Lint Cycle]], [[Schema Engineering for LLM Wiki]]
- 학습/독서/지식 복리: [[LLM Wiki as Learning Base]], [[독서는 판단력과 자산관리의 기반이다]]
- 개인 레버리지: [[AI 자동화는 개인 생산성 레버리지다]], [[레버리지를 당하지 않고 사용하는 삶]]

Graph View에서 중요한 것은 노드 수가 아니라 연결의 해석이다. 어떤 클러스터가 커지는지, 어떤 페이지가 고립되는지, 어떤 주제가 자주 서로 연결되는지를 보면 "내가 실제로 반복해서 생각하는 것"이 보인다.

## Operational Rule

앞으로 Query를 운영할 때는 다음 규칙이 좋다.

1. 중요한 질문은 반드시 저장한다.
2. 저장된 Query에는 관련 Wiki 링크를 충분히 넣어 graph edge를 만든다.
3. Query 안에서 나온 새 개념은 바로 새 페이지로 만들지 말고, durable insight인지 판단한다.
4. 새 개념이면 Concept/Entity/Guide 중 어디인지 정한다.
5. 사용자의 장기 운영 원칙이면 [[Core Context]]에도 반영할지 검토한다.
6. `explored: false`, `verificationStatus: unverified`를 보고 "아직 내가 완전히 이해한 지식인지"를 구분한다.

## Quality Gaps

- "모델 성능이 상향 평준화될수록 개인 맥락이 차별점이 된다"는 주장은 사용자 해석과 일반적 관찰에 기반한 synthesis다. 외부 연구 source로 검증된 claim은 아니다.
- [[Personal Context Layer for LLM Wiki]]는 이번 Query에서 만든 synthesis-only 개념이므로 `verificationStatus: unverified`로 시작한다.
- Obsidian Graph View 표시 여부는 실제 Obsidian 필터, 폴더 제외 설정, wikilink 수에 따라 달라질 수 있다.
- [[Persistent Knowledge Base]], [[Progressive Disclosure Pattern]], [[Context Engineering]]은 여러 페이지에서 링크되지만 아직 이 vault에 독립 Wiki page가 없어 추후 보강 후보다.

## Reuse Axis

이 답변은 Codex 개발 워크플로, 독서/책/학습, 에세이/블로그, 취업/포트폴리오에 활용 가능합니다 — LLM Wiki를 개인 맞춤형 LLM context layer이자 지식 복리 시스템으로 설명하는 핵심 논리를 정리했기 때문입니다.
