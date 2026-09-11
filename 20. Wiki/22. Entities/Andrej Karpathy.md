---
type: wiki-page
aliases:
  - Karpathy
  - 카르파시
description: Andrej Karpathy — AI researcher, former Tesla AI Director, OpenAI founding member, creator of the LLM Wiki pattern. Known for making deep learning education accessible.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - person
  - ai-researcher
  - educator
source:
  - "[[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]]"
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - https://karpathy.ai/
  - https://github.com/karpathy
related:
  - "[[LLM Wiki Pattern]]"
  - "[[qmd]]"
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

# Andrej Karpathy

> [!tip] Key Insight
> AI 연구자이자 교육자. Tesla AI Director를 거쳐, 딥러닝의 대중화와 LLM 활용 패턴을 선도하고 있다.

---

## Overview

Andrej Karpathy는 슬로바키아 출신의 AI 연구자, 교육자, 엔지니어이다. Stanford에서 Fei-Fei Li 지도하에 박사 학위를 받았으며, OpenAI 창립 멤버, Tesla AI Director (Autopilot)를 역임했다. 딥러닝 교육 콘텐츠(YouTube 강의, 블로그, nanoGPT 등)로 널리 알려져 있다.

---

## Details

### 주요 이력

- **Stanford CS PhD**: Computer Vision, Fei-Fei Li 연구실
- **OpenAI**: 창립 멤버 (2015)
- **Tesla**: AI Director, Autopilot 리드 (2017-2022)
- **OpenAI 복귀**: 2023-2024, midtraining·synthetic data generation 팀 구축
- **2024 이후**: 본인 공식 사이트 기준 AI 교육 영상과 오픈소스 활동

### LLM Wiki와의 관계

2026년 4월, [[LLM Wiki Pattern]]을 두 단계로 공개:

| 시점 | 형태 | 비고 |
|------|------|------|
| **2026-04-02** | X 포스트 → [[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]] | 825 words, 패턴의 최초 공개 |
| **2026-04-06** | 공식 Gist → [[2026-04-12-Karpathy-LLM-Wiki]] | X 버전을 확장, "Optional CLI tools"에서 [[qmd]] 권장 추가 |

이 볼트(cmds-llm-wiki)가 그 패턴의 구현체이다.

**Karpathy의 실사용 방식**:
- LLM 에이전트를 한쪽에, Obsidian을 다른 쪽에 열어놓고 작업
- LLM이 대화 기반으로 wiki를 편집하면 Obsidian에서 실시간 탐색
- "Obsidian은 IDE, LLM은 프로그래머, Wiki는 코드베이스"
- **개인 deployment 규모**: ~100 articles / ~400K words (자가 공개, 2026-04-02)
- **확장 구상**: Wiki 기반 synthetic data와 fine-tuning을 향후 탐색 방향으로 언급

### 커뮤니티 반응

X 스레드에서 주목할 답글:
- **kepano (Steph Ango)**: 원출처가 분명한 개인 vault와 agent playground를 분리하는 관점 제시
- **Beomsu** (@BeromArtDev): [[qmd]] 실사용 확인

### 교육 기여

- **YouTube**: "Neural Networks: Zero to Hero" 시리즈
- **nanoGPT**: 교육용 미니멀 GPT 구현
- **micrograd**: 자동미분 교육 라이브러리
- **cs231n**: Stanford Computer Vision 강의 (조교 → 교수)

> [!note] Bias Check
> 이 페이지의 경력 정보는 Karpathy 본인 사이트와 공개 저장소로 확인했지만, LLM Wiki의 효과와 영향력 평가는 그의 자기보고와 이 vault의 해석에 의존한다. `~100 articles / ~400K words`는 개인 사례이며 일반적 성능 보장이 아니다.

---

## Related

- [[LLM Wiki Pattern]] — Karpathy가 제안한 핵심 패턴
- [[qmd]] — Karpathy가 권장한 search tool

---

## Sources

- [[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread]] — 원조 X 스레드
- [[2026-04-12-Karpathy-LLM-Wiki]] — 확장된 Gist
- [Andrej Karpathy official site](https://karpathy.ai/)
- [Andrej Karpathy on GitHub](https://github.com/karpathy)

---

## Open Questions

> [!question] Open Question
> Karpathy 자신이 이 패턴을 어떤 도메인에서 실제로 사용하고 있는지, 그 결과물은 공개되어 있는지?
