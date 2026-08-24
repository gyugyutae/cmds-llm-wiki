---
type: wiki-page
aliases:
  - AI and Machine Learning in Quant Research
  - 현대 퀀트 리서처의 AI 역할
description: "A provisional map of how machine learning changes quant data, modeling, signal research, execution, and model-risk responsibilities."
author:
  - Codex
date created: 2026-08-24
date modified: 2026-08-24
tags:
  - quant
  - machine-learning
  - ai
  - model-risk
source:
  - "[[2026-08-17-Gemini-Quant-Research-Conversation]]"
related:
  - "[[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]"
  - "[[백테스트 과적합과 편향]]"
  - "[[AI-Augmented Developer Positioning]]"
confidence: low
layer: concepts
explored: false
claimType: mixed
evidenceScope: single-source
verificationStatus: unverified
status: active
---

# AI와 머신러닝 시대의 퀀트 리서치

## 변화 지도

| 영역 | 가능성 | 함께 커지는 위험 |
|---|---|---|
| 데이터 | 텍스트·이미지·호가 등 비정형·고차원 데이터 처리 | 시점 누수, 라이선스, 품질, 재현성 |
| 모델 | 비선형 상호작용과 조건부 패턴 탐색 | 과적합, 불안정성, 설명 곤란 |
| 연구 | 많은 신호 후보 생성과 실험 자동화 | 다중 검정과 우연한 알파 증가 |
| 실행 | 주문 분할·시장 충격 예측·동적 정책 | regime 변화, 안전 제약, 운영 실패 |
| 모니터링 | drift와 이상 징후 탐지 | 잘못된 경보와 모델 의존 |

## 퀀트 리서처의 남는 책임

AI가 후보를 많이 만들수록 리서처의 역할은 줄어들기보다 **데이터 계보, 반증 기준, 비용 모델, 재현성, 배포 후 감시** 쪽으로 이동한다. 생성된 신호를 선택한 이유와 폐기한 이유를 함께 남겨야 한다.

김규태에게 이 주제는 장기 퀀트 진로뿐 아니라 주문·체결 백엔드의 데이터 파이프라인, latency, 모델 호출 경계, 장애 대응을 연결해 보는 학습 축이다.

> [!note] Bias Check
> Counter-argument: 실제 금융사는 규제, 데이터 접근권, latency, 설명 가능성 때문에 최신 AI를 모든 전략에 적용하지 않는다.
> Data gap: 현재 source는 Gemini의 개괄 설명뿐이며 실제 조직의 기술 스택이나 성과를 증명하지 않는다.

## Related

- [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]
- [[백테스트 과적합과 편향]]
- [[AI-Augmented Developer Positioning]]
- [[김규태 금융 시스템 개발자 취업 로드맵]]
