---
type: wiki-page
aliases:
  - Wiki Operations
  - Ingest Query Lint
  - IQL Cycle
description: The three core operations of an LLM Wiki — Ingest (absorb new sources), Query (search and synthesize answers), and Lint (health-check for contradictions, orphans, and staleness).
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - llm-wiki
  - operations
  - workflow
source:
  - "[[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]"
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - "[[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]"
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
related:
  - "[[LLM Wiki Pattern]]"
  - "[[3-Layer Architecture]]"
  - "[[qmd]]"
  - "[[Web Clipper to Inbox Workflow]]"
  - "[[Agent-Readable Metadata]]"
  - "[[Personal Context Layer for LLM Wiki]]"
confidence: medium
layer: concepts
status: active
explored: false
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# Ingest-Query-Lint Cycle

> [!tip] Key Insight
> Wiki를 살아있게 만드는 세 가지 작업: **Ingest**(새 지식 흡수), **Query**(검색+합성), **Lint**(자가 정화). 세 작업 모두 wiki를 더 풍부하게 만든다.

---

## Overview

[[LLM Wiki Pattern]]은 세 가지 핵심 operation으로 운영된다. Ingest와 Query는 지식을 추가할 수 있고, Lint는 오류·중복·낡은 내용을 표시하거나 줄여 무결성을 높인다.

---

## Details

### 1. Ingest (새 자료 흡수)

새 source를 wiki에 통합하는 과정.

**워크플로**:
1. 새 source가 `00. Inbox/`에 도착
2. LLM이 source를 읽고 핵심 takeaway 추출
3. `10. Raw Sources/`에 원본 저장 (불변)
4. 근거가 실제로 영향을 주는 Wiki 페이지만 incremental update:
	- 기존 페이지가 있으면 → 새 정보 추가/업데이트
	- 새 개념이면 → 새 페이지 생성
5. `index.md` 업데이트
6. `log.md`에 기록

**Karpathy의 선호**: source를 하나씩 ingest하면서 관여하기 (요약 확인, 방향 제시). 단, batch ingest도 가능.

Karpathy Gist의 `10-15 pages`는 한 source가 여러 페이지를 건드릴 수 있다는 예시이지 이 저장소의 생성 목표나 품질 기준이 아니다.

**Purpose gate**: 이 vault는 ingest 전에 "왜 수집했는가"를 묻는 절차를 강조한다. 이 질문은 단순한 확인이 아니라, source를 미래의 학습·연구·제품·에세이 맥락으로 재사용하기 위한 metadata 생성 단계다. 이 vault에서는 그 답을 `collectionPurpose`에 기록한다.

### 2. Query (지식 검색+합성)

wiki에 대해 질문하고 답변을 받는 과정.

**워크플로**:
1. `index.md`에서 관련 페이지 탐색
2. 관련 Wiki 페이지 읽기
3. 정보 종합하여 답변 생성

**답변 형태**: markdown 페이지, 비교 표, 슬라이드 (Marp), 차트 (matplotlib), canvas 등.

**핵심 인사이트**: 좋은 답변은 wiki에 다시 저장할 수 있다. 비교 분석, 발견한 연결, 합성 결과 — 이것들은 chat history에서 사라지면 안 된다. Wiki에 저장하면 탐색도 source처럼 **compounding**된다.

학습용으로 보면 Query는 "답변 받기"가 아니라 "질문 과정 자체를 지식으로 남기기"다. 따라서 중요한 질문은 `30. Queries/`에 저장해 이후 면접 답변, README 문장, 블로그 초안, 학습 복습 자료로 재사용한다.

저장된 Query result는 `30. Queries/`의 markdown 파일이므로 wikilink를 포함하면 Obsidian Graph View에서도 하나의 노드와 edge로 나타날 수 있다. 단, 모든 Query가 새 Wiki 개념이 되는 것은 아니다. 일회성 산출물은 Query로만 보존하고, 여러 페이지를 연결하는 반복 가능한 insight만 [[Personal Context Layer for LLM Wiki|durable Wiki concept]]로 승격한다.

### 3. Lint (자가 정화)

wiki의 건강 상태를 점검하는 과정.

**점검 항목**:
- **Contradictions**: 페이지 간 상충하는 정보
- **Stale claims**: 새 source로 대체된 오래된 주장
- **Orphan pages**: 어디에도 링크되지 않은 페이지
- **Missing pages**: 언급되었지만 아직 페이지가 없는 개념
- **Missing cross-references**: 연결되어야 할 링크 누락
- **Data gaps**: 웹 검색으로 채울 수 있는 정보 공백

### Indexing and Logging

두 가지 시스템 파일이 wiki 네비게이션을 지원한다:

| 파일 | 목적 | 특성 |
|------|------|------|
| `index.md` | 콘텐츠 카탈로그 | 페이지 목록 + 1줄 요약. Query 시 LLM이 먼저 읽음 |
| `log.md` | 시간순 이력 | Append-only. 무엇이 언제 일어났는지 기록 |

`index.md`는 작은 Wiki의 탐색 표면이지만, 충분한 규모와 검색 품질의 경계는 이 볼트에서 측정되지 않았다.

> [!info] Scale Calibration
> Karpathy는 **~100 articles, ~400K words** 규모에서 별도의 복잡한 RAG 없이 index와 brief summary를 에이전트가 유지하는 방식이 잘 작동했다고 보고했다. 이는 qmd 도입의 보편적 임계값이 아니라 단일 운영 사례다.

> [!note] Bias Check
> 이 cycle은 원문의 운영 설계와 이 저장소의 로컬 절차를 합친 것이다. 세 명령을 실행했다는 사실만으로 원문 보존, 정확한 synthesis, 모순 해소가 보장되지 않는다. 각 operation의 최종 산출물과 diff를 별도로 검증해야 한다.

---

## Related

- [[LLM Wiki Pattern]] — 이 operations가 속한 전체 패턴
- [[3-Layer Architecture]] — operations가 작동하는 구조
- [[Web Clipper to Inbox Workflow]] — Web Clipper capture에서 ingest까지의 practical route
- [[Agent-Readable Metadata]] — ingest가 metadata를 채우는 이유
- [[Personal Context Layer for LLM Wiki]] — Query와 Wiki가 개인 맞춤형 LLM 맥락층을 만드는 방식

---

## Sources

- [[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]
- [[2026-04-12-Karpathy-LLM-Wiki]]
- [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]
- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
