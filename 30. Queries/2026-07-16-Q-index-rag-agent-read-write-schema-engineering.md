---
type: query-result
aliases:
  - Index RAG Agent Read Write Schema Engineering
  - LLM Wiki Index RAG Agent Synthesis
description: Synthesis of how index.md works in an LLM Wiki, how RAG and LLM Wiki differ and complement each other, and how agent read/write capabilities can reduce complex vector or graph infrastructure for many knowledge workflows.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - query
  - llm-wiki
  - rag
  - schema-engineering
  - agent-workflow
source:
  - "[[LLM Wiki Pattern]]"
  - "[[RAG vs Compiled Wiki]]"
  - "[[3-Layer Architecture]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[qmd]]"
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
reusableFor:
  - 독서/책/학습
  - Codex 개발 워크플로
  - 에세이/블로그
  - 취업/포트폴리오
confidence: medium
---

# Index, RAG, Agent Read/Write, Schema Engineering

## Query

LLM Wiki는 인간이 하기 어려웠던 위키 유지보수를 LLM/agent가 대신하면서 유지보수 비용을 낮추는 점이 의미 있다. 이 관점에서 `index.md`는 어떻게 작동하는가? RAG와 LLM Wiki는 어떻게 다르고, 어떻게 상호보완할 수 있는가? 에이전트의 읽기/쓰기 능력만으로 어떻게 복잡한 embedding/vector/graph DB 과정을 대체하거나 줄일 수 있는가?

## Core Thesis

LLM Wiki의 핵심은 "검색을 잘하는 시스템"보다 **지식을 계속 유지보수하는 시스템**에 가깝다. 기존 인간 위키가 실패한 이유는 지식을 쓰는 것보다 연결, 갱신, 중복 제거, 모순 표시, 인덱스 정리 같은 유지보수 비용이 너무 빨리 커졌기 때문이다. [[LLM Wiki Pattern]]은 이 반복 작업을 LLM/agent에게 맡겨 유지보수 비용을 낮춘다.

인간의 역할은 사라지는 것이 아니라 더 선명해진다. 인간은 어떤 source를 볼지 큐레이션하고, 분석 방향을 정하고, 좋은 질문을 던지고, 그 결과가 자기 삶·프로젝트·학습에 무엇을 의미하는지 판단한다. 나머지 파일링, cross-reference, 요약 갱신, lint, query result 저장은 LLM이 맡는다.

## 1. `index.md`는 어떻게 작동하는가

`index.md`는 LLM Wiki의 "작은 지도"다. 모든 본문을 한 번에 읽지 않고, 먼저 한 줄 요약과 카테고리 목록을 보고 어떤 페이지를 열지 결정하게 만든다.

작동 흐름:

1. Query가 들어온다.
2. Agent가 `index.md`를 먼저 읽는다.
3. Concepts, Entities, Guides, Maps, Queries 목록에서 관련 후보를 찾는다.
4. 후보 페이지를 full read한다.
5. 필요한 경우 Raw Source나 Query Result로 drill down한다.
6. 답변을 만들고, 중요한 답변은 다시 `30. Queries/`에 저장한다.

이 방식은 [[Ingest-Query-Lint Cycle]]의 progressive disclosure다. `index.md`는 전체 지식의 압축된 routing table이고, 개별 Wiki page는 자세한 source-backed body다. 사람이 책의 목차와 색인을 먼저 보고 필요한 장을 여는 것과 같다.

중요한 점은 `index.md`가 단순 목록이 아니라 **agent-readable interface**라는 점이다. 에이전트는 파일명만 보는 것이 아니라, 짧은 설명을 보고 "이 페이지가 지금 질문에 관련 있는가"를 판단한다. 그래서 index의 품질은 query 품질에 직접 영향을 준다.

한계도 있다. source가 수백 개, wiki page가 수천 개로 커지면 `index.md`만으로 모든 관련 페이지를 안정적으로 찾기 어렵다. 이때 [[qmd]] 같은 검색 계층이나 RAG-style retrieval이 자연스럽게 붙는다.

## 2. RAG와 LLM Wiki는 어떻게 다른가

[[RAG vs Compiled Wiki]] 기준으로 가장 큰 차이는 **지식 처리 시점**이다.

| 차원     | RAG                               | LLM Wiki                                     |
| ------ | --------------------------------- | -------------------------------------------- |
| 작동 시점  | 질문할 때                             | source가 들어올 때                                |
| 기본 역할  | 검색 + 답변 생성                        | 편집 + 유지보수 + 답변 생성                            |
| 지식 상태  | 매번 재조립                            | 누적/갱신                                        |
| 결과 지속성 | 대화가 끝나면 사라짐                       | Wiki/Query로 남음                               |
| 인프라    | chunking, embedding DB, retriever | markdown, wikilink, schema, agent read/write |
| 장점     | 대규모 문서 검색에 강함                     | 장기 학습과 누적에 강함                                |

RAG는 나쁘고 LLM Wiki가 무조건 좋다는 뜻이 아니다. RAG는 아직 컴파일되지 않은 거대한 외부 문서 더미에서 후보를 찾는 데 강하다. LLM Wiki는 반복해서 쓸 지식을 누적하고 정리하는 데 강하다.

현명한 조합은 이렇다.

1. **초기 탐색은 RAG/search**
	- 큰 문서 집합, 웹, 논문 묶음에서 관련 후보를 찾는다.
2. **좋은 source는 LLM Wiki로 ingest**
	- Raw Source에 보존하고, Wiki page로 컴파일한다.
3. **반복 질문은 Wiki에서 답한다**
	- 매번 chunk를 다시 조립하지 않고, 이미 정리된 page를 읽는다.
4. **규모가 커지면 Wiki 위에 qmd/RAG를 얹는다**
	- `index.md` + wikilink를 기본으로 두고, qmd/vector search는 routing 보조 계층으로 쓴다.

즉 RAG는 "넓게 찾기", LLM Wiki는 "깊게 축적하기"에 강하다. 둘은 경쟁 관계라기보다 **retrieval -> compilation -> reuse** pipeline의 서로 다른 단계다.

## 3. 에이전트의 읽기/쓰기 능력은 어떻게 embedding/vector 과정을 줄이는가

전통적 RAG는 문서를 chunk로 쪼개고 embedding을 만들고 vector DB에서 유사 chunk를 찾은 뒤, LLM이 그 조각들을 다시 조립한다. 이 방식은 대규모 검색에는 강하지만, 지식이 매번 query-time에 재구성된다.

LLM Wiki는 다른 전제를 둔다.

> 에이전트가 파일을 읽고 쓸 수 있다면, 지식 구조 자체를 파일로 유지보수하게 만들 수 있다.

여기서 대체되는 것은 "모든 검색 기술"이 아니라, **반복적으로 같은 종합을 다시 계산하는 비용**이다. 예를 들어 RAG에서는 "LLM Wiki와 RAG의 차이"를 물을 때마다 관련 chunk를 다시 찾아야 한다. LLM Wiki에서는 그 차이가 이미 [[RAG vs Compiled Wiki]]에 정리되어 있고, 새 source가 들어오면 그 페이지가 업데이트된다.

구체적으로는 다음 구조가 vector DB 일부 역할을 대신한다.

| Vector/RAG 구성요소      | LLM Wiki 대응                          |
| -------------------- | ------------------------------------ |
| Chunk metadata       | YAML frontmatter                     |
| Retriever index      | `index.md`, MOC, wikilinks           |
| Graph DB edges       | `[[wikilinks]]`, `source`, `related` |
| Query-time synthesis | Ingest-time compiled Wiki page       |
| Relevance routing    | agent가 index/page description을 읽고 선택 |
| Result cache         | `30. Queries/` saved query result    |

Neo4j 같은 graph DB가 없어도 Obsidian의 wikilink graph는 기본적인 연결 구조를 만든다. Vector DB가 없어도 `index.md`, MOC, qmd search, `rg`는 agent가 관련 파일을 찾는 데 충분한 출발점을 준다. 그리고 가장 중요한 차이는, agent가 검색 결과를 보고 끝내는 것이 아니라 **파일을 수정해 다음 검색의 출발점을 개선한다**는 점이다.

다만 "완전 대체"라고 말하면 과장이다. 수천/수만 source, 정교한 권한 관리, 실시간 업데이트, 통계적 similarity ranking, graph traversal analytics가 필요하면 vector DB나 graph DB가 다시 필요해진다. LLM Wiki의 강점은 복잡한 인프라 없이도 개인/소규모 팀의 지식 축적 문제를 먼저 해결한다는 점이다.

## 4. 스키마 엔지니어링이 왜 중요해지는가

[[3-Layer Architecture]]에서 Schema는 LLM의 행동 규칙이다. 즉 스키마는 위키의 "편집 방침"이자 "타입 시스템"이다.

좋은 스키마는 다음을 정한다.

- Raw Source는 어디에 저장하고 얼마나 보존할지
- Wiki page는 어떤 frontmatter를 가져야 하는지
- `source`, `related`, `confidence`, `verificationStatus`를 어떻게 쓸지
- Query 결과를 언제 저장할지
- Lint가 무엇을 문제로 볼지
- 인간이 직접 검토한 지식과 LLM이 정리한 지식을 어떻게 분리할지

그래서 위키가 커질수록 품질을 결정하는 것은 단순히 "LLM이 똑똑한가"가 아니라, **LLM이 어떤 규칙 아래에서 읽고 쓰는가**가 된다. 이것이 네가 말한 "스키마 엔지니어링"의 핵심이다.

LLM Wiki에서 schema engineering은 프롬프트 엔지니어링보다 지속적이다. 프롬프트는 한 번의 대화를 제어하지만, schema는 수십 번의 ingest/query/lint 사이클을 제어한다. 따라서 schema engineering은 개인 지식 시스템에서 "에이전트가 계속 일관되게 유지보수하도록 만드는 기술"이 될 수 있다.

## Practical Position

네 관점은 이렇게 정리할 수 있다.

> LLM Wiki는 RAG를 부정하는 것이 아니라, RAG가 query-time에 반복하던 synthesis를 ingest-time 유지보수로 옮기는 패턴이다. 인간은 source 큐레이션과 의미 판단에 집중하고, LLM은 cross-reference, update, lint, query result filing을 맡는다. 작은 규모에서는 `index.md`와 wikilink만으로도 충분하고, 규모가 커지면 qmd/RAG/vector search를 routing 보조 계층으로 붙이면 된다. 이때 전체 품질을 결정하는 핵심은 schema engineering이다.

## Quality Gaps

- [[RAG vs Compiled Wiki]]는 아직 contradiction callout을 유지하고 있다. RAG와 LLM Wiki의 상호보완 관계를 더 정교하게 검증하려면 `/verify`가 필요하다.
- [[qmd]]는 새로 만든 단일-source 페이지라 `verificationStatus: unverified`다. 실제 qmd 공식 문서나 GitHub source를 추가 ingest하면 confidence를 올릴 수 있다.
- `Schema Engineering for LLM Wiki`는 현재 사용자 해석과 기존 Wiki synthesis 기반이므로, 외부 source가 더 들어오면 강화할 수 있다.

## Reuse Axis

이 답변은 독서/책/학습, Codex 개발 워크플로, 에세이/블로그, 취업/포트폴리오에 활용 가능합니다 — LLM Wiki가 왜 의미 있는지, RAG와 어떻게 다른지, 스키마 설계가 왜 중요한지 설명하는 핵심 논리이기 때문입니다.
