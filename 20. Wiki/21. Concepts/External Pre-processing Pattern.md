---
type: wiki-page
aliases:
  - External Preprocessing
  - Pre-processing Pipeline
description: Optional pre-ingest pattern for costly transformations such as transcription or multi-source research. Preserves the original source, stores tool output as a derivative, and adopts the pattern only after comparing quality, cost, and time with direct ingest.
author:
  - Claude
date created: 2026-04-29
date modified: 2026-08-29
tags:
  - concept
  - workflow
  - token-optimization
  - llm-wiki
  - hybrid-pipeline
  - cost-engineering
source:
  - https://developers.openai.com/api/docs/guides/deep-research
  - https://developers.openai.com/api/docs/models/whisper-1
related:
  - "[[Cohort Token Economy]]"
  - "[[LLM Wiki Token Optimization Strategies]]"
  - "[[Ingest-Query-Lint Cycle]]"
confidence: medium
layer: concepts
status: active
explored: false
claimType: prescriptive
evidenceScope: synthesis-only
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# External Pre-processing Pattern

> [!tip] Key Insight
> 외부 전처리는 기본값이 아니라 **검증 가능한 선택지**다. 변환 비용이 큰 입력에서만 시험하고, 원문과 출처를 보존한 채 파생 결과를 별도 저장하며, 직접 인제스트 대비 품질·비용·시간이 나아질 때 채택한다.

---

## Overview

**External Pre-processing Pattern** 은 인제스트 전에 음성 인식·형식 변환·다중 출처 조사 같은 작업을 별도 도구로 수행하는 후보 워크플로다. [[Cohort Token Economy]] 에서 제기한 비용 압박을 줄일 가능성은 있지만, 이 저장소에는 절감률이나 품질 우위를 입증하는 비교 로그가 없다. 따라서 직접 인제스트와 비교하는 실험으로 취급한다.

## 검증 경계

- OpenAI 공식 문서는 Deep Research를 복수 출처를 검색·분석·종합하는 복잡한 조사 작업용으로 설명한다. 단일 장문 파일의 보편적 전처리 도구라는 근거는 아니다.
- Whisper는 다국어 음성 인식·번역·언어 식별을 수행하는 speech-to-text 모델이다. 전사문은 원본 음성의 대체 증거가 아니라 파생 자료다.
- `50-80%` 토큰 절감, 외부 도구가 항상 더 저렴하거나 빠르다는 주장, 특정 공급자의 품질 우위는 이 페이지의 근거로 확인되지 않았다.
- 이 패턴의 효과는 입력 유형, 모델·요금제, 출력 품질 기준에 따라 달라진다.

---

## 적용 가능한 외부 도구

| 입력 | 후보 처리 | 검증할 출력 |
|---|---|---|
| **음성·영상** | speech-to-text 도구 | 타임스탬프가 있는 전사문과 표본 대조 결과 |
| **복수 출처 조사** | Deep Research 계열 도구 | 출처 링크가 추적되는 조사 초안 |
| **단일 장문 문서** | 직접 추출·분할을 우선 시험 | 페이지 위치가 유지된 텍스트 |
| **웹 페이지 클리핑** | 웹 클리퍼 또는 직접 저장 | URL·제목·수집일이 있는 원문 캡처 |
| **공개 API 데이터** | 재현 가능한 스크립트 | 요청 조건과 스키마가 기록된 JSONL/Markdown |

도구의 결과물은 **파생 자료**로 취급한다. 원문 또는 안정적인 원문 URL을 함께 보존하지 못하면 정상적인 Raw Source로 승격하지 않는다.

---

## 워크플로 단계

### 1. 입력 분류
새 raw 자료 도착 시 즉시 판단:
- 짧고 정제된 텍스트 (e.g. 블로그 포스트, GitHub README) → 직접 LLM Wiki ingest
- 음성 인식·OCR·복수 출처 종합처럼 별도 변환이 필요한 입력 → 외부 전처리 후보
- 단일 장문·다국어라는 이유만으로 외부 전처리를 기본 선택하지 않음

### 2. 외부 전처리 실행
적합한 도구로 변환하되 다음 provenance를 함께 기록:
- 원문 파일 또는 안정적인 URL
- 사용 도구·모델·처리일
- 가능하면 프롬프트와 주요 설정
- 원문 위치를 추적할 수 있는 페이지·타임스탬프·출처 링크
- 요약·번역·전사 등 파생 자료의 유형

### 3. LLM Wiki 진입
원문은 `10. Raw Sources/` 의 `## Original Content` 보존 규칙을 따른다. 전처리 결과는 원문과 구분되는 파생 자료로 표시하여 `00. Inbox/` 에 넣고, `/ingest` 시 원문과 함께 연결한다. 파생 결과만으로 원문을 대체하지 않는다.

### 4. 비교·검증
표본 입력에서 **직접 ingest**와 **외부 전처리 후 ingest**를 비교한다. 누락·왜곡·인용 추적성·처리 시간·실제 비용을 기록하고, 이득이 재현될 때만 해당 입력 유형의 기본 경로로 채택한다.

---

## 트레이드오프

### 장점
- **입력 변환 분리**: 전사·OCR·API 정형화를 재사용 가능한 단계로 만들 수 있음
- **비용·시간 절감 가능성**: 직접 ingest 대비 측정으로 확인할 수 있음
- **도구 선택 유연성**: 입력 유형에 맞는 전문 기능을 시험할 수 있음

### 단점
- **워크플로 복잡도**: 도구 N 개 관리
- **결과 일관성 손상**: 외부 도구의 stylistic drift
- **자동화 어려움**: 다단계 → 사용자 수동 개입 많음
- **데이터 노출**: 민감 데이터를 여러 vendor 에 전달

### 잘 안 맞는 경우
- 인터랙티브 wiki query (사전 변환과 무관하게 query마다 모델 사용량 발생)
- 빠른 1회성 자료 처리 (멀티 플랫폼 셋업이 오버헤드)
- 매우 민감한 데이터 (vendor 분산 자체가 risk)

---

## [[Ingest-Query-Lint Cycle]] 과의 관계

External Pre-processing은 필요할 때만 **Ingest 단계 앞에** 배치되는 선택적 단계다:

```
[원문 보존] → [선택적 외부 변환] → [/ingest: 원문+파생자료] → [Wiki compile] → [query/lint]
```

각 단계에서 원문과 파생 자료의 경계를 유지해야 이후 검증과 재처리가 가능하다.

> [!note] Bias Check
> 이 패턴은 도구 분업이 비용을 줄일 것이라는 운영 가설에서 출발한다. 현재 저장소에는 직접 ingest와 비교한 토큰·비용·시간·정확도 데이터가 없으므로, 절감 효과나 특정 도구의 우위를 사실로 취급하지 않는다. 외부 요약은 원문 누락과 오류 전파를 만들 수 있어 원문 보존과 표본 대조가 필수다.

---

## Related

- [[Cohort Token Economy]] — 본 패턴이 다루려는 상위 운영 문제
- [[LLM Wiki Token Optimization Strategies]] — 종합 가이드
- [[Ingest-Query-Lint Cycle]] — 본 패턴이 확장하는 cycle

---

## Open Questions

> [!question] 자동 routing skill
> `/ingest` 가 입력 크기·언어·형식 보고 자동으로 "외부 전처리 권장" 출력하는 skill 확장 가치.

> [!question] 외부 전처리 결과 품질 보증
> 외부 조사 결과의 **정확성·hallucination** 검증 없이 ingest하면 오류가 누적될 수 있다. Lint 단계에서 외부 출처 자료의 인용 검증을 자동화할 가치가 있는가?

> [!question] 비용 정확 비교
> 외부 전처리 후 ingest와 직접 ingest의 실제 토큰·비용·시간 비교 데이터를 수집할 가치가 있는가?

---

## Sources

- [OpenAI Deep Research guide](https://developers.openai.com/api/docs/guides/deep-research)
- [OpenAI Whisper model](https://developers.openai.com/api/docs/models/whisper-1)
