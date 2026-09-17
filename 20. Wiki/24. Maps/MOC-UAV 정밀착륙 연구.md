---
type: moc
aliases:
  - 정밀착륙 연구 중심축
  - UAV Precision Landing MOC
description: "A semester-long research hub for UAV precision landing, covering vision, markerless localization, semantic landmarks, control, patents, experiments, and evidence."
author:
  - Codex
date created: 2026-09-08
date modified: 2026-09-08
tags:
  - moc
  - uav
  - precision-landing
  - semester-research
topic:
  - uav-precision-landing
related:
  - "[[MOC-Portfolio]]"
  - "[[UAV 정밀착륙 특허 검색 가이드]]"
  - "[[2026-09-08-UAV-precision-landing-patent-search-pilot]]"
  - "[[2026-09-08-Q-precision-landing-patent-fit-and-team-loop]]"
status: active
explored: false
verificationStatus: partial
---

# MOC-UAV 정밀착륙 연구

> 이 페이지를 정밀착륙 질문, 특허·논문 조사, 구현 판단, 실험 결과가 모이는 한 학기 연구 중심축으로 사용한다.

## Research Goal

카메라 기반 UAV 정밀착륙에서 표적을 어떻게 인식하고 상대 위치를 추정하며, PX4 제어와 안전 로직까지 연결할지 조사·구현·검증한다. 현재 관심 범위는 영상 기반 정밀착륙, 마커리스 자연 특징, 로고·의미 표식 인식이다.

## Research Tracks

| 트랙 | 핵심 질문 | 현재 상태 |
|---|---|---|
| 비전 기반 정밀착륙 | 카메라 영상에서 착륙 오차를 어떻게 산출·보정하는가? | 특허 파일럿 시작 |
| 마커 기반 | ArUco·AprilTag·능동 표식의 고도별 인식 한계는 무엇인가? | 기존 엑셀 자료 있음 |
| 마커리스 | 자연 특징·기존 구조물로 재식별과 자세 추정이 가능한가? | 특허 후보 1건 |
| 의미론적 랜드마크 | 로고·문양·아이콘을 식별·검증해 잘못된 착륙을 막을 수 있는가? | 특허 후보 1건 |
| 위치·자세 추정 | PnP, optical flow, visual odometry, sensor fusion 중 무엇이 적합한가? | 조사 필요 |
| 제어·PX4 연계 | LANDING_TARGET과 Offboard 중 어떤 폐루프가 적합한가? | 조사 필요 |
| 안전·실험 | 인식 실패, 조명, 가림, 이동 표적에서 어떤 fail-safe와 지표를 쓸 것인가? | 조사 필요 |
| 특허 지형 | 독립항의 필수 구성과 회피 설계 포인트는 무엇인가? | [[UAV 정밀착륙 특허 검색 가이드]] |

## Current Evidence

- [[2026-09-08-UAV-precision-landing-patent-search-pilot]] — 세 검색식별 대표 특허 3건
- [[2026-09-08-Q-precision-landing-patent-fit-and-team-loop]] — 5번 의미 아이콘 방식 중심의 최소 장비 기준선과 재완·관호·규태 반복 실험 구조
- 외부 작업 파일: `C:\Users\user\Desktop\4. 관련연구조사 - AI_ML 활용 SW.xlsx`

## Current Architecture Decision

- 기준선: 단일 하향 RGB 카메라와 인쇄 표식으로 상대 pose를 추정하고 `LANDING_TARGET`을 PX4에 전달
- 확장: 학습 객체·장애물 판단을 추가한 뒤 자연 특징 기반 마커리스 방식과 비교
- 제어권: QGC/MAVSDK는 미션, ROS는 관측, PX4는 착륙 제어를 담당하며 동시 setpoint 송신을 금지

## Next Questions

- 한국 등록특허만으로 동일 검색식을 재실행하면 어떤 독립항 패턴이 반복되는가?
- 자연 로고를 쓰는 방식과 설계 마커를 쓰는 방식의 오인식·권리범위 차이는 무엇인가?
- 현재 PX4/Pixhawk/Jetson 또는 Raspberry Pi 구성에서 가장 작은 검증 실험은 무엇인가?
- 착륙 XY 오차, 성공률, 검출 지연, 재식별 실패율의 측정 프로토콜은 어떻게 설계할 것인가?

## Operating Rule

앞으로 정밀착륙 관련 질문이 들어오면 먼저 이 MOC와 연결 자료를 읽고, 새 근거가 생기면 Raw Source → Wiki/Query → 이 MOC 순서로 연결한다. 특허 상태와 기술 효과는 확인일을 기록하고, 사용자 구현 결과와 문헌 주장을 분리한다.

> [!note] Bias Check
> 현재 시작점은 검색식별 대표 사례 1건뿐이라 기술 지형 전체를 대표하지 않는다. 이후 한국·미국·PCT·중국 패밀리와 비특허문헌을 함께 확장해야 한다.
