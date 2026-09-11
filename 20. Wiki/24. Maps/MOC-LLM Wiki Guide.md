---
type: moc
aliases:
  - LLM Wiki 사용 가이드
  - Getting Started
description: Onboarding guide for the CMDS LLM Wiki vault. Explains the 3-layer architecture, how to ingest sources, query knowledge, and maintain wiki health. Start here if you are new to this vault.
author:
  - Claude
  - Codex
date created: 2026-04-10T21:30
date modified: 2026-08-29
tags:
  - moc
  - guide
  - onboarding
topic:
  - llm-wiki
  - knowledge-management
source:
  - "[[AGENTS]]"
  - .agents/skills/ingest/SKILL.md
  - .agents/skills/query/SKILL.md
  - .agents/skills/lint/SKILL.md
  - .codex/commands/ingest.md
related:
  - "[[index]]"
  - "[[AGENTS]]"
  - "[[log]]"
  - "[[MOC-Knowledge Management]]"
  - "[[LLM Wiki Pattern]]"
  - "[[LLM Wiki as Learning Base]]"
  - "[[Web Clipper to Inbox Workflow]]"
status: active
explored: false
confidence: high
claimType: prescriptive
evidenceScope: multi-source-primary
verificationStatus: verified
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
operationMode: standalone
source-vault: null
---

# MOC-LLM Wiki Guide

> 이 볼트는 LLM이 Raw Source를 보존하면서 재사용 가능한 Wiki로 컴파일하는 지식 베이스다. 현재 운영 기준은 `AGENTS.md`와 저장소 범위의 `.agents/skills/`, 세부 실행 절차는 `.codex/commands/`에 있다.

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────┐
│                Schema Layer                  │
│ AGENTS.md → .agents/skills → .codex/commands │
├─────────────────────────────────────────────┤
│              Wiki Layer                      │
│   20. Wiki/ (LLM이 관리하는 지식 페이지)       │
│   ┌──────────┬──────────┬────────┬────────┐ │
│   │ Concepts │ Entities │ Guides │  Maps  │ │
│   └──────────┴──────────┴────────┴────────┘ │
├─────────────────────────────────────────────┤
│           Raw Sources Layer                  │
│   10. Raw Sources/ (불변 원본 자료)            │
│   ┌──────────┬────────┬───────┬───────────┐ │
│   │ Articles │ Papers │ Books │Transcripts│ │
│   └──────────┴────────┴───────┴───────────┘ │
└─────────────────────────────────────────────┘
```

---

## 📥 How to Ingest

1. 새 자료를 `00. Inbox/`에 드롭
2. `$inbox`로 대상을 확인하거나 자료를 지정해 `$ingest` 요청
3. 수집 목적 질문에 답해 `collectionPurpose` 확정
4. Codex가:
	- 원문을 `10. Raw Sources/`의 `## Original Content` 아래 보존
	- 필요한 관련 Wiki 페이지만 생성·증분 갱신
	- 변경이 있으면 `[[index]]`를 동기화하고 `[[log]]`에 기록
	- 최종 diff와 원문 보존 여부를 확인

`$inbox`는 발견·선택 단계이고 `$ingest`는 근거 보존·컴파일·검증 단계다.

---

## 🔍 How to Query

- Wiki 페이지를 직접 탐색하거나 `$query {질문}`을 요청
- Codex가 관련 Wiki와 Raw Source를 검색하고, 검증 상태가 낮은 페이지는 헤지하여 답변
- 재사용 가치가 큰 합성 결과는 `30. Queries/`에 저장하고 내구성 있는 결론이나 빈틈을 Wiki에 피드백

---

## 🔧 How to Maintain (Lint)

주기적으로 다음 저장소 스킬을 사용한다.

| 목적 | 스킬 | 결과 |
|---|---|---|
| 빠른 현황 | `$status` | 개수, Inbox backlog, 필드 커버리지, 인덱스 drift |
| 건강 검사 | `$lint` | orphan, broken link, stale page, 스키마 문제 |
| 전체 지식 감사 | `$audit` | eligibility·consistency·confirmability와 Top 10 verify queue |
| 단일 페이지 확인 | `$verify {page}` | 근거 대조와 v5 검증 메타데이터 갱신 |
| 검색 인덱스 재구축 | `$reindex` | Wiki·Raw Sources·Queries의 qmd index/embedding 갱신 |
| 사용자 맥락 갱신 | `$refresh-context` | `Core Context.md` 스냅샷 갱신 |

Broken link는 자동으로 새 개념을 만들지 않는다. 오타·이동이면 링크를 고치고, 실제 지식 공백이면 생성 후보로 남긴다.

---

## 🔗 Standalone Mode

이 vault는 현재 Mode A로 단독 운영한다. 별도 mothership vault를 연결하지 않으므로 `/ingest`는 `mainVaultRelated` 검색을 건너뛰고, 이 vault 내부의 Raw Source / Wiki / Query 결과만 사용한다.

나중에 Mode B로 전환하면 [[Mothership-Satellite Vault Pattern]]에 따라 메인 볼트와 cross-reference를 추가할 수 있다.

> [!note] Bias Check
> 이 페이지는 현재 저장소의 Codex 운영 규칙을 설명하며 외부 도구 전체의 보편적 모범 사례를 주장하지 않는다. 스킬이나 디렉터리 구조가 바뀌면 `AGENTS.md`와 `.codex/commands/`를 우선 기준으로 다시 검증해야 한다. `CLAUDE.md`와 `.claude/`는 명시적으로 요청될 때만 유지하는 legacy mirror다.

## 📚 Study Path

- [[LLM Wiki Pattern]] — 전체 패턴
- [[LLM Wiki as Learning Base]] — 앞으로 공부할 source를 다루는 관점
- [[Personal Context Layer for LLM Wiki]] — 개인 맞춤형 LLM을 위한 사용자 맥락층 관점
- [[Agent-Readable Metadata]] — 에이전트가 읽기 좋은 note 설계
- [[Web Clipper to Inbox Workflow]] — 캡처부터 ingest까지
- [[Citation Manager Integration for LLM Wiki]] — 학술 인용을 위한 Zotero/Bookends 연동 설계

---

## Sources

- [AGENTS.md](../../AGENTS.md)
- [.agents/skills/ingest/SKILL.md](../../.agents/skills/ingest/SKILL.md)
- [.agents/skills/query/SKILL.md](../../.agents/skills/query/SKILL.md)
- [.agents/skills/lint/SKILL.md](../../.agents/skills/lint/SKILL.md)
- [.agents/skills/verify/SKILL.md](../../.agents/skills/verify/SKILL.md)
- [.codex/commands/ingest.md](../../.codex/commands/ingest.md)
