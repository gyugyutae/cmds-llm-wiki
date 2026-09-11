---
type: wiki-page
aliases:
  - LLM Wiki Tools
  - Obsidian LLM Wiki Setup
description: Practical guide to optional Obsidian and CLI tooling for this LLM Wiki, with current capability claims separated from local installation state.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - guide
  - obsidian
  - tooling
  - llm-wiki
source:
  - "[[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]"
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - "[[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]"
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
  - "[[2026-07-14-GitHub-qmd-README]]"
  - https://obsidian.md/help/web-clipper
  - https://obsidian.md/help/plugins/graph
  - https://github.com/tobi/qmd
related:
  - "[[LLM Wiki Pattern]]"
  - "[[3-Layer Architecture]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[qmd]]"
  - "[[Web Clipper to Inbox Workflow]]"
  - "[[Agent-Readable Metadata]]"
confidence: medium
layer: guides
status: active
explored: false
claimType: prescriptive
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# Obsidian Tooling for LLM Wiki

> [!tip] Key Insight
> LLM Wiki는 도구 없이도 작동하지만, 적절한 Obsidian 도구를 활용하면 source 수집, 탐색, 시각화가 훨씬 효율적이다.

---

## Overview

[[LLM Wiki Pattern]]은 기본적으로 markdown 파일과 LLM만으로 작동한다. 하지만 [[Andrej Karpathy]]가 소개한 실용 도구들을 활용하면 워크플로가 크게 개선된다.

---

## Source 수집

### Obsidian Web Clipper

- **용도**: 웹 기사를 markdown으로 변환하여 Raw Sources에 추가
- **설치**: Obsidian 공식 Web Clipper 브라우저 확장
- **워크플로**: 브라우저에서 기사 발견 → 클리핑 → `00. Inbox/`에 저장 → LLM에게 ingest 요청

이 vault에서는 Web Clipper가 곧바로 Wiki page를 만드는 도구가 아니다. 먼저 `00. Inbox/`에 capture하고, `$inbox`와 `$ingest`를 통해 목적 질문을 받은 뒤 Raw Source와 Wiki로 승격한다. 상세 절차는 [[Web Clipper to Inbox Workflow]]에 정리한다.

### 이미지 로컬 다운로드

클리핑한 기사의 이미지를 로컬에 보관하면 URL 깨짐을 방지할 수 있다.

**설정 방법**:
1. Obsidian Settings → Files and links → "Attachment folder path" → 고정 디렉토리 지정 (예: `80. References/Attachments/`)
2. Settings → Hotkeys → "Download attachments for current file" → 단축키 지정 (예: `Ctrl+Shift+D`)
3. 기사 클리핑 후 단축키로 이미지 일괄 다운로드

> [!note] Image boundary
> Markdown의 image link와 실제 image content는 다르다. 사용 가능한 vision/file 도구로 이미지를 별도 열어 확인하고, 링크 존재만으로 이미지 내용을 읽었다고 주장하지 않는다.

---

## 탐색 및 시각화

### Graph View

- **용도**: wiki의 형태를 시각적으로 파악 — 허브, 고립 노드, 클러스터
- **활용**: Lint 작업 시 orphan 페이지 식별에 유용
- **Query 반영**: `30. Queries/`에 저장된 query result도 wikilink가 있으면 graph node와 edge로 나타난다. Graph View 필터에서 `30. Queries/`를 제외하면 보이지 않을 수 있다.
- Obsidian 기본 기능 (플러그인 불필요)

### Dataview

- **용도**: frontmatter를 기반으로 동적 테이블/리스트 생성
- **활용 예**: 모든 wiki 페이지를 confidence별로 정렬, 최근 ingest 목록, tag별 그룹핑
- **전제**: YAML frontmatter가 일관되어야 함. 기본 note 필드와 operation별 verification 필드는 `AGENTS.md` 및 해당 skill을 따른다.

---

## 검색

### index.md (기본)

- `index.md`는 작은 Wiki의 기본 탐색 표면
- LLM이 query 시 index를 먼저 읽고 관련 페이지로 drill down
- 검색 품질이 충분한지는 실제 질의로 확인하며, 규모만으로 embedding 필요 여부를 결정하지 않음

### qmd (확장)

→ 상세: [[qmd]] (별도 엔티티 페이지)

- **용도**: markdown 파일 전용 로컬 검색 엔진
- **특징**: 캡처된 공식 README 기준 BM25/vector search + LLM re-ranking을 온디바이스에서 결합. node-llama-cpp와 GGUF 모델 사용
- **인터페이스**: CLI (LLM이 shell out 가능) + MCP server (LLM native tool)
- **시점**: 정확한 제목 검색과 `rg`만으로 근거 회수가 부족하다는 실제 평가가 있을 때 도입
- **이 볼트의 현재 상태**: 세 collections와 Qwen3 embedding 설정이 template/skill에 기록되어 있지만, 2026-08-29 현재 이 Mac에는 `qmd` 실행 파일이 없고 hook에는 Windows path placeholder가 남아 있어 자동 재인덱싱은 검증되지 않음
- **실사용자**: [[Andrej Karpathy|Karpathy]], Beomsu (@BeromArtDev, 2026-04-03 X에서 공개 확인)

학습용 ingest 관점에서는 qmd가 "기억 안 나는 페이지 찾기"에 특히 유용하다. 정확한 제목 대신 "RAG와 LLM Wiki 차이", "AI 활용 경계", "포트폴리오 약점"처럼 의미 중심으로 검색해도 Raw Source, Wiki, Query 결과를 함께 탐색할 수 있다.

> [!warning] Version boundary
> qmd 명령, 옵션, 기본 모델은 릴리스에 따라 바뀔 수 있다. [[2026-07-14-GitHub-qmd-README]]는 캡처 시점의 원문이므로 실행 전 현재 `qmd --help`와 upstream README를 확인한다.

> [!note] Bias Check
> 도구가 설치되어 있거나 기능 목록이 존재한다는 사실은 이 vault의 검색 정확도·속도 향상을 증명하지 않는다. Graph View의 연결도 파일 내 wikilink 구조를 보여줄 뿐 claim의 진실성이나 사용자의 이해도를 검증하지 않는다.

---

## 출력 형식

### Marp

- **용도**: markdown 기반 슬라이드 생성
- **활용**: wiki 콘텐츠에서 직접 프레젠테이션 생성
- Obsidian Marp 플러그인 사용 가능

---

## Related

- [[LLM Wiki Pattern]] — 이 도구들이 지원하는 패턴
- [[3-Layer Architecture]] — 도구가 각 층과 어떻게 연결되는지
- [[Ingest-Query-Lint Cycle]] — 도구가 각 operation을 어떻게 개선하는지
- [[Web Clipper to Inbox Workflow]] — capture에서 ingest까지의 실전 절차
- [[Agent-Readable Metadata]] — frontmatter를 에이전트용 routing surface로 쓰는 법

---

## Sources

- [[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]
- [[2026-04-12-Karpathy-LLM-Wiki]]
- [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]
- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
- [[2026-07-14-GitHub-qmd-README]]
- [Obsidian Web Clipper help](https://obsidian.md/help/web-clipper)
- [Obsidian Graph view help](https://obsidian.md/help/plugins/graph)
- [tobi/qmd current README](https://github.com/tobi/qmd)
