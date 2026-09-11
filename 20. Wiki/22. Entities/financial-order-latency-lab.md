---
type: wiki-page
aliases:
  - Financial Order Latency Lab
description: Python-based backend performance experiment measuring p99 order latency under CPU, disk, and GPU contention.
author:
  - Codex
date created: 2026-07-10
date modified: 2026-08-29
tags:
  - project
  - backend
  - performance
  - python
source:
  - https://github.com/gyutaetae/financial-order-latency-lab
  - https://raw.githubusercontent.com/gyutaetae/financial-order-latency-lab/main/README.md
  - "[[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]"
  - "[[Core Context]]"
related:
  - "[[김규태]]"
  - "[[MOC-Portfolio]]"
  - "[[김규태 Career Narrative]]"
confidence: medium
layer: entities
explored: true
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
status: active
---

# financial-order-latency-lab

## Overview

`financial-order-latency-lab`는 금융 실시간 주문 처리 서버에서 CPU 계산, 동기식 거래 로그 flush, GPU risk scoring이 p99 latency에 어떤 영향을 주는지 측정한 운영체제/백엔드 성능 분석 프로젝트다.

사용자 확인에 따르면, 이 프로젝트는 데이터베이스 수업에서 관련 아이디어와 개념을 공부한 뒤 2026년 5~6월 학기말 개인 프로젝트로 진행한 실험이다. 김규태는 CPU·GPU·disk의 속도와 latency 차이를 금융 관점에서 보고 싶다는 최초 문제를 제시했다. p99와 구체적인 실험 조건은 AI가 제안했고 모든 코드·실행·재실험을 AI가 수행했다. 김규태는 별도 검증을 하지 않았으며 현재 코드를 설명·수정·재현할 수 없다고 밝혔다.

---

## Backend Signal

- Python 기반 Windows-local order server와 TCP load generator를 사용했다.
- CPU risk check, sync log + fsync, PyTorch CUDA scoring server 호출을 각각 scenario로 분리했다.
- 공개 저장소의 결과 파일과 README는 100 rps 기준 baseline p99 `25.60 ms`, gpu-scoring p99 `45.11 ms`, combined p99 `48.36 ms`를 기록한다.
- 저장소 해석에 따르면 mitigation은 disk pressure proxy를 `10.95 -> 1.49`로 낮췄지만 p99 개선은 제한적이었고, GPU call과 Python request-per-connection overhead가 더 큰 병목 후보였다.

> [!note] Verification Boundary
> 2026-08-29 현재 공개 GitHub README와 저장소 구조에서 코드·실행 명령·결과 표의 존재와 위 수치를 확인했다. 이번 Wiki 검증은 Windows 11/GTX 1060 환경에서 실험을 재실행하지 않았으므로 측정의 재현성, proxy metric의 타당성, 병목 인과관계까지 독립 검증한 것은 아니다.

---

## Origin Story

- **Trigger**: 데이터베이스 수업에서 관련 아이디어와 개념을 공부한 뒤 금융 주문 처리 지연을 학기말 주제로 선택
- **Domain interest**: 금융
- **User role**: CPU·GPU·disk latency를 금융 관점에서 비교한다는 최초 문제 제시와 AI 제안 채택
- **AI role**: p99와 CPU·disk·GPU 조건 제안, 전체 코드 생성, 실험 설계·그래프·결과 해석 지원
- **Verification**: 별도 검증하지 않음
- **Current limitation**: 사용자는 현재 코드를 설명·수정·재현할 수 없음
- **Portfolio risk**: 직접 구현한 개발 경험으로 표현하면 사실과 다르며 기술 면접에서 방어할 수 없음

---

## Portfolio Use

현재 상태에서는 백엔드 구현력의 대표 프로젝트로 사용하지 않는다. 금융 시스템에서 tail latency를 중요하게 본 문제의식과 AI 활용 경계를 설명하는 학습 경험으로만 둔다. 새 Java 주문 시스템에서 관련 실험을 직접 재현하고 설명할 수 있게 된 뒤 보조 근거로 다시 평가한다.

면접 핵심 문장:

> 데이터베이스 수업의 학기말 프로젝트에서 CPU·GPU·disk latency를 금융 관점에서 비교하는 문제를 제시하고 AI로 실험 결과를 만들었습니다. 당시 코드와 결과를 직접 검증하지 못한 한계를 인정하고, 다음 Java 주문 시스템에서는 AI를 사용하더라도 코드 설명·수정·테스트와 검증 근거를 남기겠습니다.

---

## Evidence Gaps

- 수업 과제 요구사항과 평가 기준
- AI에게 처음 제시한 문제와 본인이 최종 선택한 실험 범위
- 명령 실행, 오류 대응, 데이터 수집과 재실험의 실제 수행 주체
- 직접 구현한 코드는 없음
- Linux 환경에서 재측정했는지 여부
- 발표자료 또는 교수/팀 피드백
- AI 결과를 검증하지 않았다는 회고
- 새 Java 프로젝트에서 설명·수정·검증 가능한 형태로 다시 구현할 최소 실험

> [!note] Bias Check
> 공개 저장소에 코드와 결과가 존재한다는 사실은 김규태가 직접 구현·실행·검증했다는 증거가 아니다. 2026-07-11 원문에는 사용자가 기획과 개발을 했다는 초기 진술이 있지만, 이후 사용자 확인을 반영한 [[Core Context]]는 AI가 p99 조건·전체 코드·실행·재실험을 담당했고 사용자는 별도 검증하지 못했다고 명시한다. 이 페이지는 더 구체적이고 최신인 확인을 적용한다.

---

## Sources

- https://github.com/gyutaetae/financial-order-latency-lab
- https://raw.githubusercontent.com/gyutaetae/financial-order-latency-lab/main/README.md
- [[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]
- [[Core Context]]
