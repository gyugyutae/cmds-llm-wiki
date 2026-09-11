---
type: moc
aliases:
  - 지식 관리
  - KM MOC
  - PKM MOC
description: Map of Content for the knowledge-management pages that currently exist in this vault, including the LLM Wiki pattern, RAG comparison, provenance boundaries, operational guides, and Memex history.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - moc
  - knowledge-management
topic:
  - knowledge-management
  - personal-knowledge-management
source:
  - "[[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]"
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - AGENTS.md
related:
  - "[[MOC-LLM Wiki Guide]]"
  - "[[index]]"
status: active
explored: false
confidence: medium
claimType: definition
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# MOC-Knowledge Management

> 지식 관리(Knowledge Management)에 관한 개념, 패턴, 도구, 역사를 정리하는 Map of Content.

---

## Core Pattern

- [[LLM Wiki Pattern]] — LLM이 raw source를 컴파일하여 persistent wiki를 관리하는 패턴
- [[3-Layer Architecture]] — Raw Sources / Wiki / Schema 3층 구조
- [[Ingest-Query-Lint Cycle]] — Wiki 운영의 세 가지 핵심 작업
- [[LLM Wiki as Learning Base]] — 관심 있지만 아직 모르는 개념을 학습 가능한 형태로 컴파일하는 관점

## Key Concepts

- [[RAG vs Compiled Wiki]] — 매번 재검색 vs 한 번 컴파일의 차이
- [[Mothership-Satellite Vault Pattern]] — 메인 지식 볼트와 LLM-managed Wiki 볼트의 역할 분리
- [[Agent-Readable Metadata]] — LLM이 먼저 읽는 YAML metadata 설계
- [[Human-AI Knowledge Boundary]] — AI가 쓴 지식과 사용자가 아는 지식의 경계
- [[Cohort Token Economy]] — 강의·연구 cohort에서 LLM Wiki 운영 시 토큰 예산을 관리하는 관점
- [[External Pre-processing Pattern]] — 긴 source를 외부 도구로 전처리한 뒤 Wiki 컴파일에 투입하는 패턴
- [[Idea Generation Pipeline]] — 새 source ingest를 도메인 아이디어 생성 트리거로 확장하는 워크플로
- [[Track Classification and Research Gap Detection]] — thematic track 분류로 연구 gap을 찾는 패턴
- [[Schema Engineering for LLM Wiki]] — agent가 일관되게 Wiki를 유지보수하도록 규칙과 metadata를 설계하는 기술 영역
- [[Personal Context Layer for LLM Wiki]] — LLM에게 나에 대한 고품질 맥락을 제공해 개인 맞춤형 답변을 가능하게 하는 위키 관점

## People & History

- [[Andrej Karpathy]] — LLM Wiki 패턴 제안자
- [[김규태]] — 이 standalone LLM Wiki의 소유자이자 운영자
- [[Vannevar Bush]] — Memex 개념 제안자 (1945)
- [[Memex]] — 문서 간 associative trail을 가진 개인 지식 저장소 구상

## Tools

- [[qmd]] — 이 볼트에서 사용하는 로컬 Markdown 검색 도구

## Practical Guides

- [[Obsidian Tooling for LLM Wiki]] — 실용 도구 가이드
- [[Web Clipper to Inbox Workflow]] — Web Clipper capture에서 purpose-gated ingest까지
- [[Citation Manager Integration for LLM Wiki]] — Zotero/Bookends 서지정보와 LLM Wiki source metadata 연결
- [[Book Ingest Pattern]] — 책과 장문 자료를 단계적으로 컴파일하는 패턴
- [[LLM Wiki Token Optimization Strategies]] — 토큰 제약 환경의 운영 최적화 가이드

---

## Related MOCs

- [[MOC-LLM Wiki Guide]] — 이 볼트 사용 온보딩 가이드

## Unmaterialized Candidates

이전 버전에는 `Persistent Knowledge Base`, `Contamination Mitigation`, `Sovereign PKM`, `Harness Literacy`, `Synthetic Data Generation for Wiki`를 직접 Wiki 링크로 나열했지만 현재 대응 파일이 없다. 필요성이 확인되기 전까지 broken link를 만들지 않고 생성 후보로만 유지한다.

> [!note] Bias Check
> 이 MOC는 현재 파일을 찾기 위한 탐색 지도이며, 항목 수나 링크 배치가 개념의 중요도 또는 사실 검증 수준을 뜻하지 않는다. 각 페이지의 `verificationStatus`, `confidence`, source를 별도로 확인해야 한다. 파일이 없는 후보 개념은 존재하는 지식 페이지처럼 표시하지 않는다.
