---
type: wiki-page
aliases:
  - LLM Wiki
  - Karpathy Wiki Pattern
  - LLM-Maintained Wiki
description: The LLM Wiki pattern proposed by Andrej Karpathy — LLMs incrementally build and maintain a persistent, structured markdown wiki from raw sources instead of using RAG for every query.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-10-12
tags:
  - llm-wiki
  - knowledge-management
  - design-pattern
source:
  - "[[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]"
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - "[[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]"
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
related:
  - "[[RAG vs Compiled Wiki]]"
  - "[[3-Layer Architecture]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Andrej Karpathy]]"
  - "[[Memex]]"
  - "[[qmd]]"
  - "[[LLM Wiki as Learning Base]]"
  - "[[Mothership-Satellite Vault Pattern]]"
  - "[[Agent-Readable Metadata]]"
  - "[[Human-AI Knowledge Boundary]]"
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

# LLM Wiki Pattern

> [!tip] Key Insight
> LLM이 raw source를 읽고 persistent wiki를 직접 작성·관리한다. 매 질문마다 재검색하는 RAG가 아니라, 한 번 컴파일된 지식이 계속 성장하는 **compounding artifact**.

---

## Overview

**LLM Wiki Pattern**은 [[Andrej Karpathy]]가 2026년 4월 제안한 개인 지식 베이스 구축 패턴이다. 핵심 아이디어는 간단하다:

> LLM에게 raw source를 주면, LLM이 직접 structured markdown wiki를 작성하고 유지한다.

기존 [[RAG vs Compiled Wiki|RAG 방식]]에서는 질문 시점에 문서를 검색하고 합성한다. LLM Wiki에서는 source를 Wiki 페이지로 컴파일하고 새 source가 들어올 때 기존 페이지를 **incremental update**한다. Cross-reference, 모순 표시, 누적 synthesis는 자동으로 보장되는 결과가 아니라 ingest·verify·lint가 계속 유지해야 하는 목표 상태다.

## 검증 경계

- Karpathy의 X thread와 Gist는 raw-to-Wiki 점진 컴파일, Obsidian 기반 탐색, 질의 결과의 재파일링, health check를 실제 운영 아이디어와 개인 경험으로 설명한다.
- `~100 articles / ~400K words`는 Karpathy가 공개한 한 사례이며 embedding search가 필요해지는 일반 임계값이 아니다.
- `한 source가 10-15개 Wiki page를 건드릴 수 있다`, `maintenance cost가 near zero`는 Gist의 표현이다. 이 볼트의 보편적 성능이나 보장된 비용 절감으로 검증된 수치가 아니다.
- 현재 감사에서 stale claim, broken link, 미검증 페이지가 발견된 사실은 LLM 유지보수도 별도 검증 절차와 사람의 감독이 필요함을 보여준다.

---

## Details

### 역할 분담

| 역할 | 담당 |
|------|------|
| Source 큐레이션 | 인간 |
| 질문, 방향 설정, 의미 해석 | 인간 |
| 요약, cross-referencing, 파일링, 북키핑 | LLM |
| Wiki 작성 및 유지보수 | LLM |

Karpathy의 비유: **Obsidian은 IDE, LLM은 프로그래머, Wiki는 코드베이스.**

### 적용 분야

- **Personal**: 목표, 건강, 자기계발 추적
- **Research**: 논문·기사를 읽으며 evolving thesis를 가진 comprehensive wiki 구축
- **Reading a Book**: 챕터별 캐릭터·테마·플롯 페이지 생성 (팬 위키처럼)
- **Business/Team**: Slack, 회의록, 프로젝트 문서를 LLM이 wiki로 유지
- **기타**: 경쟁 분석, 실사, 여행 계획, 코스 노트, 취미 deep-dive

### 핵심 특성

1. **Persistent**: 대화가 끝나도 wiki는 남는다
2. **Compounding**: source가 추가될수록 wiki가 더 풍부해진다
3. **Pre-synthesized**: cross-reference와 모순 플래그가 이미 완료되어 있다
4. **Human-readable**: Obsidian 등에서 직접 탐색 가능
5. **Version-controllable**: Git 저장소로 운영할 경우 변경 이력을 추적 가능

### 공개된 한 운영 사례

Karpathy 본인의 deployment (2026-04-02 X 공개): **~100 articles, ~400K words**. 이 규모에서:

- Karpathy는 이 규모에서 별도의 복잡한 RAG가 필요하지 않았다고 보고했다.
- index와 짧은 summary를 에이전트가 유지하며 관련 자료를 읽는 방식이 잘 작동했다고 설명했다.
- 이는 단일 사용자 사례이며 다른 문서 구조·모델·질의 유형에 그대로 일반화할 수 없다.

이 수치는 검색 전략을 비교할 출발점일 뿐 embedding search의 경계선을 확정하지 않는다(→ [[Obsidian Tooling for LLM Wiki|qmd 도입 시점 논의]]).

### 확장 방향

- X thread의 kepano 답글은 agent-generated content와 원출처가 분명한 개인 vault를 분리하는 contamination 완화 관점을 제안한다.
- Karpathy는 Wiki 콘텐츠를 synthetic data와 fine-tuning으로 확장하는 아이디어를 향후 탐색 항목으로 제시한다.
- 이 저장소는 `AGENTS.md`와 repo-scoped skills를 schema/harness로 사용하지만, 이것은 Karpathy 패턴의 로컬 구현 선택이다.

### 왜 작동하는가

Karpathy의 Gist는 위키 유지의 어려운 부분을 cross-reference 업데이트, 요약 최신화, 모순 감지 같은 **북키핑**으로 설명하고 LLM이 이를 낮은 비용으로 수행할 수 있다고 제안한다. 그러나 유지보수 비용이 거의 0이라는 표현은 운영 가설에 가깝다. 이 볼트에서도 audit·verify·lint와 사람의 판단이 계속 필요하다.

2026-07-16 WikiDocs 해설은 이 지점을 학습용으로 더 쉽게 설명한다. RAG에서는 LLM이 질문할 때마다 "검색 엔진 + 요약기"처럼 작동하지만, LLM Wiki에서는 source가 들어오는 순간부터 "편집자 + 사서"처럼 작동한다. 따라서 LLM Wiki의 핵심은 답변 생성보다 **지식 유지보수의 비용을 낮추는 운영 패턴**에 있다.

### 학습 전초기지로서의 LLM Wiki

이 vault에서는 LLM Wiki를 [[LLM Wiki as Learning Base|학습 전초기지]]로 사용한다. 사용자가 어떤 자료를 캡처했다는 것은 그 자료를 이미 아는 것이 아니라, 적어도 그 주제에 관심을 보였다는 신호다. LLM Wiki는 이 관심 신호를 source-backed 개념 페이지로 바꾸어, 나중에 사용자가 직접 읽고 검증할 수 있는 학습 지도로 만든다.

이 관점에서는 [[Human-AI Knowledge Boundary]]가 중요하다. LLM이 쓴 Wiki page는 사용자가 이해한 지식과 동일하지 않다. `explored`, `verificationStatus`, `confidence` 같은 필드는 이 경계를 드러내기 위한 장치다.

### 개인 맞춤형 context layer로서의 LLM Wiki

이 vault에서는 LLM Wiki를 [[Personal Context Layer for LLM Wiki|개인 맞춤형 LLM 맥락층]]으로도 본다. 모델 성능이 상향 평준화될수록 차이는 "어떤 LLM을 쓰는가"보다 "LLM에게 나에 대한 어떤 맥락을 제공하는가"에서 생길 수 있다. [[Core Context]], owner entity, 프로젝트 page, Query result는 모두 다음 LLM 세션이 읽을 수 있는 개인 맥락 자산이다.

---

## 증거 기록과 실행 평가의 연결

이 볼트의 Evidence Wiki 운영은 원본 근거·판단·본인 기여·검증 상태를 연결하는 방식이다. Markdown에 기록했다는 사실만으로 AI 출력이나 구현 결과가 검증되지는 않는다.

- 실행용 입력·정답·금지 주장과 평가 스크립트는 프로젝트 저장소에 두고, Wiki에서 버전·실행 결과·실패 사례로 연결한다.
- 숫자·필수 필드·JSON 스키마 검증과 문장 의미·출처의 주장 지원 여부 검증을 구분한다.
- 동일 데이터·프롬프트·모델 설정·검색 설정을 기록해 개선 전후를 비교한다. 출력의 완전한 동일성은 보장하지 않는다.
- 아직 없는 실행 결과를 계획만으로 통과·개선으로 표시하지 않는다.

작은 평가 제안과 도구 후보는 [[2026-10-12-Q-unlv-networking-evidence-wiki-and-ai-tools]]에 둔다. 이는 실행 전 계획이며 이 볼트의 정확도 개선을 측정한 결과는 아니다.

---

## Historical Context

이 패턴은 정신적으로 [[Vannevar Bush]]의 [[Memex]] (1945)와 연결된다. Bush는 문서 간 associative trail을 가진 개인 지식 저장소를 구상했지만, 유지보수 문제를 해결하지 못했다. 80년 후, LLM이 그 역할을 맡는다.

> [!note] Bias Check
> 이 페이지는 Karpathy가 공개한 설계와 개인 운영 사례를 중심으로 컴파일되어 있어, 장기 정확도·총 유지비용·RAG 대비 검색 품질을 독립 비교한 연구가 아니다. 원문이 제시한 장점과 이 저장소에서 실제로 확인된 동작을 구분한다. LLM 생성 Wiki는 원문 보존, claim-level 검증, 사람의 탐색 여부를 대체하지 않는다.

---

## Related

- [[RAG vs Compiled Wiki]] — 두 접근의 차이와 trade-off
- [[3-Layer Architecture]] — Raw Sources / Wiki / Schema 구조
- [[Ingest-Query-Lint Cycle]] — wiki 운영의 세 가지 작업
- [[Obsidian Tooling for LLM Wiki]] — 실용 도구 가이드
- [[qmd]] — 스케일업 시 권장 검색 도구
- [[LLM Wiki as Learning Base]] — 아직 모르는 관심 개념을 공부 가능한 형태로 컴파일하는 사용법
- [[Mothership-Satellite Vault Pattern]] — 메인 지식 볼트와 LLM Wiki 볼트의 역할 분리
- [[Agent-Readable Metadata]] — 에이전트가 먼저 읽는 YAML metadata 설계
- [[Human-AI Knowledge Boundary]] — AI가 생성한 지식과 사용자가 아는 지식의 경계
- [[Personal Context Layer for LLM Wiki]] — 개인 맞춤형 LLM을 위한 사용자 맥락층 관점

---

## Sources

- [[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]] — 원조 X 스레드 (2026-04-02)
- [[2026-04-12-Karpathy-LLM-Wiki]] — 확장된 Gist (2026-04-06)
- [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]] — LLM Wiki 활용 강의 transcript
- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]] — RAG와 LLM Wiki의 차이를 한국어로 설명한 학습용 article

---

## Open Questions

> [!question] Open Question
> 이 패턴이 수백 개 source, 수천 개 wiki 페이지 규모에서도 index.md 기반 네비게이션만으로 충분한가? 어느 시점에 embedding-based search가 필요해지는가?
