---
type: wiki-page
aliases:
  - qmd
  - Query Markup Documents
description: qmd is an on-device Markdown search engine that supports BM25, vector, and reranked hybrid retrieval; this vault contains configuration templates but the qmd executable is not currently available on this Mac.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-08-29
tags:
  - llm-wiki
  - search
  - tooling
source:
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
  - "[[2026-07-14-GitHub-qmd-README]]"
  - https://github.com/tobi/qmd
related:
  - "[[LLM Wiki Pattern]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
  - "[[Ingest-Query-Lint Cycle]]"
confidence: medium
layer: entities
status: active
explored: false
claimType: mixed
evidenceScope: multi-source-primary
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# qmd

> [!tip] Key Insight
> qmd는 LLM Wiki가 커졌을 때 `index.md` 기반 탐색을 보완하는 로컬 markdown 검색 엔진이다. Wiki, Raw Sources, Queries를 대상으로 키워드·벡터·하이브리드 검색을 제공한다.

---

## Overview

qmd는 markdown 파일을 대상으로 하는 로컬 검색 도구다. [[LLM Wiki Pattern]]에서는 초기 규모에서는 `index.md`와 wikilink 기반 탐색만으로도 충분하지만, source와 page 수가 늘어나면 더 강한 검색 계층이 필요해진다. 이때 qmd는 [[Obsidian Tooling for LLM Wiki]]의 확장 검색 도구로 쓰인다.

2026-07-14에 캡처한 공식 README 스냅샷에 따르면 qmd는 BM25 full-text search, vector semantic search, LLM reranking을 로컬에서 결합하며 CLI, SDK, MCP server interface를 제공한다. 세부 명령과 기본 모델은 이후 릴리스에서 바뀔 수 있으므로 실제 사용 전 현재 README와 `qmd --help`를 확인한다.

---

## LLM Wiki에서의 역할

| 용도 | 의미 |
|------|------|
| BM25 검색 | 정확한 키워드나 파일명을 빠르게 찾는다 |
| Vector search | 같은 단어가 없어도 의미상 가까운 문서를 찾는다 |
| Hybrid query | 키워드와 의미 검색을 섞어 Wiki/Raw/Query 결과를 찾는다 |
| CLI/MCP interface | LLM agent가 shell 또는 MCP를 통해 검색 결과를 가져올 수 있다 |
| Context tree | collection과 경로에 맥락을 붙여 agent의 문서 선택을 돕는다 |
| Local model runtime | node-llama-cpp와 GGUF 모델을 사용해 검색 계층을 로컬에서 운영한다 |

이 vault의 reindex skill과 configuration template은 `wiki`, `raw_sources`, `queries` 세 collection, 즉 `20. Wiki`, `10. Raw Sources`, `30. Queries`를 검색 대상으로 정의한다.

## Current Runtime Boundary

2026-08-29 현재 이 Mac에서 `command -v qmd`와 `qmd --version`은 실행 파일을 찾지 못했다. 또한 `.codex/hooks/qmd-reindex.sh`와 `90. Settings/qmd-config-template.yml`에는 Windows 경로 placeholder가 남아 있다. 따라서 다음을 구분한다.

- **Upstream capability verified**: BM25, vector search, LLM reranking, CLI, SDK, MCP server
- **Repository configuration present**: 세 collection, Qwen3 embedding model, reindex skill/hook template
- **Current local operation not verified**: qmd 설치, collection index, embeddings, automatic reindex

## When To Use

- 정확한 페이지 제목이 기억나지 않을 때
- `index.md` 목록만으로 관련 페이지를 찾기 어려울 때
- Raw Source와 Query 결과까지 함께 검색해야 할 때
- `/query` 전에 관련 근거 후보를 넓게 찾고 싶을 때

예시:

```bash
qmd search "LLM Wiki Pattern" -n 3
qmd vsearch "포트폴리오에 쓸 AI 활용 경계" -n 3
qmd query "RAG와 LLM Wiki의 차이를 설명하는 학습 자료" -n 3
```

위 명령은 upstream 문법 예시다. 현재 Mac에서는 qmd를 설치하고 실제 경로로 configuration/hook을 수정한 뒤에만 실행할 수 있다.

> [!note] Bias Check
> Counter-argument: 작은 vault에서는 qmd 없이 `index.md`, `rg`, Obsidian 검색만으로 충분할 수 있다.
> Data gap: 이 vault에서 qmd가 실제 Query 정확도와 검색 시간을 얼마나 개선하는지는 아직 정량 평가하지 않았다. 캡처한 README는 특정 시점의 스냅샷이다.

---

## Related

- [[Obsidian Tooling for LLM Wiki]] — qmd가 포함된 실용 도구 가이드
- [[Ingest-Query-Lint Cycle]] — Query 단계에서 qmd 검색을 사용할 수 있다
- [[LLM Wiki Pattern]] — qmd가 보완하는 compiled wiki 패턴

---

## Sources

- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
- [[2026-07-14-GitHub-qmd-README]]
- [tobi/qmd current README](https://github.com/tobi/qmd)
