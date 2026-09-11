---
type: wiki-page
aliases:
  - AI and Machine Learning in Quant Research
  - 현대 퀀트 리서처의 AI 역할
description: "A provisional map of how machine learning changes quant data, modeling, signal research, execution, and model-risk responsibilities."
author:
  - Codex
date created: 2026-08-24
date modified: 2026-08-29
tags:
  - quant
  - machine-learning
  - ai
  - model-risk
source:
  - "[[2026-08-17-Gemini-Quant-Research-Conversation]]"
  - https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm
related:
  - "[[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]"
  - "[[백테스트 과적합과 편향]]"
  - "[[AI-Augmented Developer Positioning]]"
confidence: medium
layer: concepts
explored: false
claimType: mixed
evidenceScope: mixed-source
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: Codex
disputed: false
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

AI가 후보를 많이 만드는 연구 환경에서는 **데이터 계보, 반증 기준, 비용 모델, 재현성, 배포 후 감시**가 중요해진다. 2026년 미국 연방은행 감독기관의 모델 위험 지침도 전통적 통계·비생성형 AI 모델에 대해 목적 적합성, 검증, 성능 모니터링, 한계 문서화, 거버넌스를 강조한다. 이 지침은 생성형·에이전틱 AI에는 직접 적용되지 않지만, 위험 기반 통제의 참고 경계가 된다.

김규태에게 이 주제는 장기 퀀트 진로뿐 아니라 주문·체결 백엔드의 데이터 파이프라인, latency, 모델 호출 경계, 장애 대응을 연결해 보는 학습 축이다.

> [!note] Bias Check
> Counter-argument: 실제 금융사는 규제, 데이터 접근권, latency, 설명 가능성 때문에 최신 AI를 모든 전략에 적용하지 않는다.
> Data gap: 공식 모델 위험 지침은 통제 원칙을 뒷받침하지만, 표의 모든 활용 사례가 특정 퀀트 조직에서 구현됐거나 성과를 냈다는 증거는 아니다.

## Related

- [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]
- [[백테스트 과적합과 편향]]
- [[AI-Augmented Developer Positioning]]
- [[김규태 금융 시스템 개발자 취업 로드맵]]
