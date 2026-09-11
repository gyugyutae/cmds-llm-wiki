---
type: wiki-page
aliases:
  - Memory Extender
  - 메멕스
description: Memex — Vannevar Bush's 1945 conceptual device for storing and consulting personal records through associative trails; links to hypertext and LLM Wikis are later interpretations.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - concept
  - knowledge-management
  - historical
source:
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/
related:
  - "[[Vannevar Bush]]"
  - "[[LLM Wiki Pattern]]"
confidence: high
layer: entities
status: active
explored: false
claimType: historical
evidenceScope: multi-source-primary
verificationStatus: verified
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# Memex

> [!tip] Key Insight
> 1945년 구상된 "개인 기억 확장 장치". 문서 간 associative trail(연상적 연결)을 핵심으로 했으며, 하이퍼텍스트와 LLM Wiki의 사상적 선조.

---

## Overview

**Memex** (Memory Extender)는 [[Vannevar Bush]]가 1945년 에세이 "As We May Think" (The Atlantic)에서 제안한 개념적 장치이다. 마이크로필름에 저장된 책, 기록, 통신 자료를 담고, 사용자가 **associative trail** — 문서 간 연상적 연결 — 을 만들어 탐색하는 시스템이었다.

---

## Details

### 핵심 특성

- **개인적(Private)**: 개인이 소유하고 큐레이션하는 지식 저장소
- **연상적 연결(Associative Trails)**: 인덱스가 아닌, 문서 간 의미적 연결로 탐색
- **능동적 큐레이션**: 사용자가 trail을 만들고 유지
- **축적적**: 사용할수록 trail이 풍부해짐

### Memex와 LLM Wiki의 비교

| 차원 | Memex (1945) | LLM Wiki (2026) |
|------|-------------|-----------------|
| 저장 매체 | 마이크로필름 | Markdown 파일 |
| 연결 방식 | Associative trail | Wikilinks + cross-reference |
| 큐레이션 | 인간 수동 | LLM 자동 |
| 유지보수 | 사용자가 trail 구성 | agent가 보조할 수 있으나 검증 필요 |
| 탐색 | lever·code 기반 연상 경로 구상 | 검색·wikilink·graph 등 구현 선택 |
| 실현 여부 | 당시의 개념적 장치 | 파일 기반 운영 패턴으로 구현 가능 |

### 미해결 과제

Bush의 원문은 사용자가 trail을 만들고 공유하는 장치를 구상한다. 새 정보의 모순 감지와 자동 Wiki 일관성 유지를 핵심 문제로 명시하지는 않는다. [[LLM Wiki Pattern]]은 이 구상을 현대의 agent-assisted maintenance와 연결하는 후대의 해석이다.

> [!note] Bias Check
> Memex를 Web이나 LLM Wiki의 직접 선조로 부르는 것은 유용한 계보적 비유지만 단선적인 기술 발전 사실은 아니다. 이 페이지는 Bush 원문의 장치 설명과 Karpathy의 현대적 연결을 구분한다.

---

## Related

- [[Vannevar Bush]] — Memex의 제안자
- [[LLM Wiki Pattern]] — Memex 비전의 현대적 구현

---

## Sources

- [[2026-04-12-Karpathy-LLM-Wiki]]
- [Vannevar Bush, "As We May Think," The Atlantic, July 1945](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)
