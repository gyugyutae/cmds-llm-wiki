---
type: wiki-page
aliases:
  - Token Optimization Guide
  - LLM Wiki 토큰 절감
  - Cohort Token Survival Guide
description: Evidence-aware guide for measuring and reducing LLM Wiki usage through context control, task routing, effort selection, capacity planning, and safe local-model experiments.
author:
  - Claude
date created: 2026-04-29
date modified: 2026-08-29
tags:
  - guide
  - token-optimization
  - cohort
  - claude-code
  - llm-wiki
  - cost-engineering
source:
  - https://support.claude.com/en/articles/9797557-usage-limit-best-practices
  - https://code.claude.com/docs/en/model-config
  - https://code.claude.com/docs/en/permission-modes
  - https://support.claude.com/en/articles/11049762-choose-a-claude-plan
  - https://developers.openai.com/api/docs/guides/deep-research
  - https://github.com/QwenLM/Qwen3.6
  - https://ai.google.dev/gemma/docs/get_started
related:
  - "[[Cohort Token Economy]]"
  - "[[External Pre-processing Pattern]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
confidence: medium
layer: guides
status: active
explored: false
claimType: prescriptive
evidenceScope: multi-source-primary
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# LLM Wiki Token Optimization Strategies

> [!tip] Key Insight
> 먼저 작업별 사용량과 결과 품질을 측정한다. 그다음 (1) 불필요한 컨텍스트 축소, (2) 작업 라우팅, (3) 모델·effort 조정, (4) 용량·로컬 실행 검토 순서로 한 변수씩 비교한다. 요금제나 vendor 이름만으로 최적 조합을 확정하지 않는다.

---

## Overview

본 가이드는 [[Cohort Token Economy]] 가설을 실제 운영 실험으로 바꾸기 위한 체크리스트다. 정규 강의·연구 cohort와 개인 사용자가 LLM Wiki 작업의 사용량, 시간, 품질을 함께 비교하도록 돕는다.

대상: 정규 강의 cohort, 연구실 그룹, 학습자 본인.

---

## Verification Boundary

### 공식 문서로 확인됨

- Claude 사용량은 메시지·첨부 파일·현재 대화 길이, 도구, 모델, effort level 등의 영향을 받는다.
- Claude Code의 현재 effort level은 모델에 따라 `low`, `medium`, `high`, `xhigh`, `max`를 지원한다. 낮은 effort는 단순 작업의 사용량과 지연을 줄일 수 있다.
- 2026-08-29 기준 Claude 개인용 상위 용량 명칭은 `Max 5x`, `Max 20x`다.
- OpenAI Deep Research 모델은 여러 출처를 탐색·분석·종합하는 복잡한 연구 과제용이다.
- `bypassPermissions`와 `--dangerously-skip-permissions`는 보호 기능을 끄므로 격리된 container·VM에서만 사용해야 한다.

### 아직 확인되지 않음

- 외부 전처리가 모든 Wiki 작업에서 가장 큰 절감 효과를 낸다는 순위
- Haiku/Sonnet/Opus를 특정 Wiki 작업에 고정하면 품질 대비 비용이 최적이라는 매핑
- cohort가 특정 주차에 특정 전략을 배워야 한다는 커리큘럼 효과
- 멀티 플랫폼 분산이나 로컬 모델이 실제 학습 지속률을 높인다는 인과관계

---

## 단계 1 — 기준선 측정

최적화 전에 최소 1주 동안 다음을 기록한다.

| Field | 기록 내용 |
|---|---|
| Task | ingest, query, lint, verify 등 |
| Input | 파일 수, 대략적인 길이, 이미지·첨부 여부 |
| Runtime | 사용 제품, 모델, effort, 도구 |
| Cost signal | 한도 도달 여부, 대기 시간, 표시되는 사용량 |
| Quality | Raw Source 보존, 사실 오류, 재작업 횟수, 최종 채택 여부 |

토큰 수를 직접 제공하지 않는 구독 제품에서는 한도 도달 여부와 작업 완료율을 대체 지표로 사용한다.

---

## 단계 2 — 컨텍스트와 작업 분해

### 2-1. 불필요한 컨텍스트 줄이기

- 서로 다른 작업은 새 대화로 분리한다.
- 사용하지 않는 첨부·도구·connector는 작업에서 제외한다.
- 저장소 상시 지침은 공통 규칙만 남기고, 상세 workflow는 필요할 때 로드되는 skill로 분리한다.
- 같은 자료를 다시 ingest하기 전에 Raw Sources와 `log.md`를 검색한다.

### 2-2. 외부 전처리 실험

긴 입력은 [[External Pre-processing Pattern]] 후보로 비교할 수 있다.

| 무거운 입력            | 외부 도구                           | 결과                            |
| ----------------- | ------------------------------- | ----------------------------- |
| 장편 논문 (40+ pages) | OpenAI Deep Research 같은 연구 도구 | 출처가 표시된 파생 리포트 후보          |
| 외국어 영상·강의         | Whisper STT + GPT/Gemini 번역     | 모국어 정제 스크립트                   |
| 대용량 텍스트 다수        | Google AI Studio (long context) | 요약·재구성                        |
| 웹 페이지 다수          | 옵시디언 Web Clipper                | Inbox 의 standardized markdown |

전처리 결과는 원문을 대체하는 Raw Source가 아니라 파생물이다. 원문·전사본을 보존하고, 같은 입력의 직접 처리와 비교해 비용·누락·왜곡을 측정한다. Deep Research 모델은 여러 출처를 종합하는 복잡한 조사에 적합하지만 단순 파일 변환의 기본 선택으로 고정하지 않는다.

---

## 단계 3 — 모델과 effort 선택

### 3-1. 고정 매핑 대신 파일럿

동일한 짧은 작업 표본으로 후보 모델을 비교한다. 정확성, Raw Source 보존, 링크 품질, 수정 횟수가 허용 범위에 들어온 가장 낮은 비용 조합을 선택한다. 모델 계열만으로 "단순=Haiku, 복잡=Opus"를 영구 규칙으로 두지 않는다.

### 3-2. Claude Code effort

지원 모델에서 다음처럼 설정할 수 있다.

```
/effort low
/effort medium
/effort high
```

`minimal`은 현재 공식 level이 아니다. 지원 level과 기본값은 모델·버전에 따라 달라지므로 `/effort` UI와 공식 문서를 확인한다. 정형 ingest=`low`, lint=`high` 같은 매핑도 실제 품질 표본을 통과한 뒤 채택한다.

---

## 단계 4 — 인프라 결정 (필요 시)

### 4-1. Claude 요금제 업그레이드 (서비스 출시 목표 시)

| 요금제 | 공식 설명 기준 |
|------|-----------|
| Pro | 정기적인 개인 사용을 위한 표준 용량 |
| Max 5x | Pro보다 높은 세션 용량이 필요한 빈번한 개인 사용자 |
| Max 20x | 대부분 작업에서 Claude를 매일 쓰는 개인 사용자 |

이는 개인용 공식 설명이지 cohort 배정 공식이 아니다. 실제 한도 도달 빈도와 추가 비용을 측정한 뒤 결정한다.

### 4-2. 로컬 모델 도입 (선택적)

| 모델 예시 | 공식 배포 정보 | 운영 판단 |
|------|-----|------|
| Qwen3.6 | 공식 open-weight는 27B dense와 35B-A3B 등 | `Qwen 3.6 32B` 표기는 부정확 |
| Gemma 4 | 31B는 large server/server cluster 대상 | 일반 노트북 기본 권장으로 두지 않음 |
| Gemma 4 소형 variant | E4B·12B 등 | 실제 RAM/VRAM과 quantization별 측정 필요 |

Ollama 같은 runtime 사용 여부와 별개로 모델 크기, quantization, context length, RAM/VRAM을 먼저 확인한다. "로컬=무한 ingest"가 아니라 전력·속도·메모리·품질 비용이 다른 실행 방식이다.

### 4-3. 권한과 안전

`--dangerously-skip-permissions`는 토큰 절감 옵션이 아니다. 공식 문서는 이 모드가 permission prompt와 안전 검사를 비활성화하며 prompt injection이나 의도하지 않은 작업을 막지 못한다고 경고한다. 민감 정보·중요 파일·host 접근이 없는 격리 container/VM 외에는 사용하지 않는다.

### 4-4. 멀티 플랫폼 분산

플랫폼은 정적 "강점" 표보다 다음 기준으로 선택한다.

- 필요한 기능과 현재 계정에서의 접근 가능성
- source citation과 결과 검토 방식
- 데이터 보존·민감 정보 정책
- 표시되는 사용량·추가 비용
- 같은 표본에서의 품질과 재작업 횟수

---

## 커리큘럼 설계 권장 (Cohort 운영자용)

Cohort가 LLM Wiki를 도입할 때 실험할 순서:

1. **기준선**: 1주간 작업·사용량·품질 기록
2. **컨텍스트 실험**: 불필요한 파일·도구·긴 대화 제거
3. **effort 실험**: 동일 작업을 낮은 effort와 기본값으로 비교
4. **전처리 실험**: 원문 직접 처리와 파생 요약 처리 비교
5. **인프라 실험**: 반복적으로 한도에 막힐 때만 상위 용량 또는 로컬 모델 비교

---

## 정책 변동 대비

LLM 플랫폼은 요금·모델·기능·한도를 바꿀 수 있다. 제품별 사실에는 확인일과 공식 URL을 남기고, 특정 vendor 사용을 강제하기보다 Raw Source 보존·검증·재현이라는 공통 학습 목표를 유지한다.

---

## 의사결정 흐름 (요약)

```
새 작업 도착
  ↓
기준선 기록 있음? — No → [단계 1] 측정
  ↓
불필요한 컨텍스트 있음? — Yes → [단계 2] 축소
  ↓
낮은 effort 표본 통과? — Yes → [단계 3] 채택
  ↓
반복적으로 한도 도달? — Yes → [단계 4] 용량·로컬 비교
                         ↓ No
                         현재 조합 유지
```

> [!note] Bias Check
> Counter-argument: 토큰 절감에 집중하면 더 싼 결과를 만들면서도 사실 오류, Raw Source 손상, 재작업 시간을 늘릴 수 있다.
> Data gap: 이 vault에는 전략별 실제 사용량, 완료율, 오류율, 재작업 횟수를 비교한 cohort 로그가 없다. 따라서 단계 순서는 안전한 실험 설계이며 최적 조합으로 검증된 결과가 아니다.

---

## Related

- [[Cohort Token Economy]] — 본 가이드가 해결하는 문제
- [[External Pre-processing Pattern]] — 단계 2의 비교 실험 후보
- [[Obsidian Tooling for LLM Wiki]] — 인프라 측 가이드

## Sources

- [Anthropic — Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- [Claude Code — Model configuration and effort](https://code.claude.com/docs/en/model-config)
- [Claude Code — Permission modes](https://code.claude.com/docs/en/permission-modes)
- [Anthropic — Choose a Claude plan](https://support.claude.com/en/articles/11049762-choose-a-claude-plan)
- [OpenAI Docs — Deep research API guide](https://developers.openai.com/api/docs/guides/deep-research)
- [Qwen Team — Qwen3.6 official repository](https://github.com/QwenLM/Qwen3.6)
- [Google AI for Developers — Get started with Gemma models](https://ai.google.dev/gemma/docs/get_started)

---

## Open Questions

> [!question] Edu 라이선스 가능성
> Anthropic edu license · Cursor edu plan 등 학생 대상 할인 프로그램 여부 추적. 단체 신청 가능한 옵션이 있다면 token economy 문제 근본 해결.

> [!question] Token-aware 자동 routing
> `/ingest` 가 입력 크기 보고 "이 source 는 외부 전처리 권장" 자동 출력하는 skill 확장. Cohort 가 실험할 수 있는 학습 과제로도 좋음.

> [!question] Cohort 토큰 통계 수집
> 학습자들이 자기 토큰 소비를 자발적 공유하면 cohort 평균·중앙·최대 통계 작성 가능 → 신입 cohort 에게 정확한 사전 안내.
