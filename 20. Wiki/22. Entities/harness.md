---
type: wiki-page
aliases:
  - Codex harness
description: Python-based Codex CLI autonomous implementation harness customized for staged app development workflows.
author:
  - Codex
date created: 2026-07-10
date modified: 2026-09-10
tags:
  - project
  - codex
  - automation
  - python
source:
  - https://github.com/gyutaetae/harness
  - https://raw.githubusercontent.com/gyutaetae/harness/main/README.md
  - https://github.com/gyutaetae/threads-agentic-editor-workflow
  - "[[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]"
  - "[[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]]"
  - "[[2026-07-12-YouTube-코딩몰라도-가능한-앱개발-클로드코드-하네스]]"
  - "[[2026-07-23-Kim-Gyutae-Self-Understanding-Interview-v1]]"
related:
  - "[[김규태]]"
  - "[[MOC-Portfolio]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[AI 자동화는 개인 생산성 레버리지다]]"
  - "[[경제적 자유는 나의 북극성이다]]"
confidence: medium
layer: entities
explored: true
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: Codex
disputed: false
status: active
---

# harness

## Overview

`harness`는 Codex CLI 기반 자율 구현 하네스다. 사용자의 한 줄 요구를 받아 단계별 sub-agent가 artifact를 통해 결과를 전달하고, phase 파일을 따라 직렬 구현까지 진행하는 파이프라인이다.

사용자 제공 원본 맥락에 따르면, 김규태는 Codex를 토큰 효율적이고 자동화 workflow를 만들기에 적합한 도구로 보았다. 이 관점은 harness뿐 아니라 Threads 자동 리서치/업로드 workflow에도 이어진다.

2026-07-12 YouTube inspiration bundle reflection에서 사용자는 바이브마피아의 하네스 레포를 보고 Codex 맞춤형으로 변형한 것이 자신의 `harness`이며, 이 `harness`를 사용해서 만든 것이 [[cuee]]라고 정리했다.

---

## Workflow Signal

- Python 기반 `scripts/run_phases.py` runner를 사용한다.
- `initial-plan`, `clarify`, `context-gather`, `plan`, `generate`, `evaluate` 단계로 작업을 나눈다.
- `.codex/skills/plan-and-build`, stage별 sub-agent prompt, task/phase artifact 구조를 갖는다.
- Codex CLI 실행 권한 플래그와 timeout, git skip 등을 환경 변수로 제어한다.
- 앱 개발과 제품화 실험에 맞게 개인화한 workflow로 이해한다.

---

## Threads Automation Evidence

김규태는 Codex와 토큰 기반 자동화 흐름을 활용해 Threads 계정에서 매일 저녁 6시에 AI agent 논문 활용 예시를 리서치하고 업로드하는 workflow를 구축했다고 기록했다.

- **Account**: https://www.threads.com/@arxiv.ai?hl=koo
- **Content concept**: 논문 작성에 AI agent를 어떻게 사용할 수 있는지 매일 설명하고, 좋은 예시와 나쁜 예시를 제시해 흥미를 유도
- **Reported outcome**: 2026-08-31 사용자 자기보고 기준 팔로워 650명 달성
- **Operation period**: 2026-05-25부터 매일 1개 게시물이 자동 발행되도록 운영 중이라고 보고
- **Data-informed iteration**: 좋아요·댓글·팔로워 유입이 큰 게시물을 Excel로 옮겨 반응이 좋은 글 형식을 참고해 개선했다고 보고
- **Repository verification**: 공개 저장소의 2026-08-31 스냅샷에서 게시물 성과 CSV 52행과 `metrics_feedback()` 구현을 확인했다. 최근 engagement를 형식·콘텐츠축·게시시간·실험군별로 집계해 다음 생성의 약한 신호로 사용한다.
- **Observed metrics**: 조회수가 있는 51행의 총 조회수 131,868회, 중앙값 1,147회. `tiny_source_case` 13개의 중앙 조회수는 4,033회, `research_checklist` 20개는 280.5회였으나 시기·주제 차이가 있어 인과 효과로 단정하지 않는다.
- **User decision evidence**: 여러 글 형식을 시험하고 논문 작성 방식의 반응이 좋자 템플릿으로 고정한 뒤 GitHub Actions 자동화와 반복 운영으로 연결
- **Verification status**: 사용자 제공 원문 기반. 실제 계정 분석 화면, 코드, 스케줄러 설정, 실패 처리 로그는 추가 ingest 필요

### 2026-09-10 Follow-up Format Experiment

원격 `threads-agentic-editor-workflow`의 53개 지표 행 중 72시간 관측과 조회수 조건을 만족한 50개를 재분석했다. 공개 permalink 확인 override를 포함한 대비 형식 32개에서 초기 16개 중앙 독자 참여율은 1.0054%, 후기 16개는 0.3700%로 기존 결과가 재현됐다. 다만 시간·주제·노출 차이가 있어 형식 피로를 원인으로 확정하지 않는다.

Codex는 대비 형식과 직접 체크리스트 형식을 같은 시간·관측창에서 비교하는 6쌍 준실험 코드, 계획표, 첫 비교 문안과 테스트를 작성했다. 현재 새 게시물은 0/12개이므로 상태는 `designed`, 결론은 `incomplete`다. 자세한 실행 기록은 [[2026-09-10-Q-threads-followup-experiment-and-nice-evidence-needs]]에 있다.

이 사례는 `harness`와 별개 프로젝트로 분리할 수도 있지만, 현재는 Codex 기반 자동화와 AI 활용 포지셔닝을 보여주는 보조 증거로 연결한다.

---

## Portfolio Use

백엔드 취업 포트폴리오에서는 보조 프로젝트로 둔다. 직접 제품 기능보다 "AI를 활용해 개발 프로세스를 구조화하고, 요구사항에서 구현까지의 흐름을 artifact로 남기는 개발 습관"을 보여주는 프로젝트다.

면접 핵심 문장:

> Codex를 단순 코드 생성 도구로 쓰는 데서 그치지 않고, 요구사항 정리부터 phase별 구현까지 이어지는 Python 기반 개발 harness로 구조화했습니다.

---

## Evidence Gaps

- 커서맛피아님 harness에서 어떤 구조를 참고했는지
- 앱 개발에 맞게 수정한 구체 지점
- 개발 시간, 오류 감소, 문서화 품질 같은 효과
- Threads 자동 리서치/업로드 workflow의 코드 위치는 확인했으나, 사용자가 직접 작성·설명 가능한 범위의 구분
- 2026-05-25~06-22 게시 이력과 현재 650명 팔로워의 계정 분석 화면
- 6쌍·12개 후속 교차 게시와 72시간 지표 수집 완료
- 토큰 발급, 예약 실행, 업로드 실패 처리, 계정 성장 지표 증빙
- AI agent 논문 활용 콘텐츠에서 본인이 직접 기획한 부분과 자동화가 처리한 부분의 분리
- 2026-08-29 현재 이 Mac에 local harness checkout이 없고 공개 GitHub/Raw README도 이번 검증에서 불러오지 못했으므로, 현재 코드 상태는 재확인하지 못함

---

## Sources

- https://github.com/gyutaetae/harness
- https://raw.githubusercontent.com/gyutaetae/harness/main/README.md
- https://github.com/gyutaetae/threads-agentic-editor-workflow
- [[2026-09-10-Q-threads-followup-experiment-and-nice-evidence-needs]]
- [[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]
- [[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]]
- [[2026-07-12-YouTube-코딩몰라도-가능한-앱개발-클로드코드-하네스]]
- https://www.threads.com/@arxiv.ai?hl=koo
