---
type: query-result
aliases:
  - 정밀착륙 특허 적합성 및 팀 실험 루프
description: "A system-level decision on the precision-landing patent pattern and team workflow best suited to a PX4, ROS, MAVSDK, QGroundControl, and Gazebo research environment."
author:
  - Codex
date created: 2026-09-08
date modified: 2026-09-08
tags:
  - query-result
  - uav
  - precision-landing
  - px4
  - gazebo
  - team-workflow
source:
  - "[[MOC-UAV 정밀착륙 연구]]"
  - "[[UAV 정밀착륙 특허 검색 가이드]]"
  - "[[2026-09-08-UAV-precision-landing-patent-search-pilot]]"
reusableFor:
  - 학부연구생/학술
  - 프로젝트 증거
  - 실험 설계
confidence: medium
verificationStatus: partial
---

# 정밀착륙 특허 적합성 및 팀 실험 루프

## Decision

현재 `ROS + MAVSDK + QGroundControl + Gazebo + PX4 SITL` 환경과 최소 장비 조건에는 조사한 5개 중 **5번 의미 아이콘 기반 방식**이 가장 적합하다. 단, 특허의 전체 구성을 복제하는 것이 아니라 `단일 하향 RGB 카메라 → 표적 검출·식별 → 상대 위치/자세와 신뢰도 출력 → MAVLink LANDING_TARGET → PX4 정밀착륙 제어`로 단순화한 기준선을 먼저 구현한다.

4번의 학습 객체·장애물 판단은 두 번째 단계에서 결합하고, 3번의 자연 특징 방식은 표식 기준선이 안정된 뒤 비교군으로 확장한다. 1번 능동 표식과 2번 이중 카메라·IR 방식은 추가 장비가 필요하므로 첫 학기 기준선으로 부적합하다.

## Why Number 5 Fits

- Gazebo에 인쇄 표식과 하향 RGB 카메라만 추가하면 되어 능동 비콘·IR 카메라·카메라 2대가 필요 없다.
- 표적 검출, 식별, pose 추정, 필터링을 관호의 독립 ROS 노드로 만들 수 있다.
- 출력 계약을 상대좌표·yaw·confidence로 고정하면 규태의 시뮬레이션 환경에서 알고리즘 버전만 교체해 반복 평가할 수 있다.
- PX4 Precision Landing은 offboard positioning system이 보내는 MAVLink `LANDING_TARGET`을 받을 수 있고, 임무의 `MAV_CMD_NAV_LAND`에서 정밀착륙을 시작할 수 있다.
- PX4가 접근·하강·최종 접근과 표적 유실 처리를 담당하게 하면 강화학습이 비행 안전 전체를 처음부터 책임지지 않아도 된다.

## Recommended System Boundary

```text
재완
QGC .plan 작성·미션 조건 정의
	↓
규태
.plan 검증·업로드 → PX4 SITL/Gazebo 실행
	↓
Gazebo 하향 카메라 영상
	↓
관호
표적 검출/식별 → pose/상대좌표 → 필터 또는 학습 모델
	↓
규태 통합 계층
좌표계·시간·신뢰도 검사 → MAVLink LANDING_TARGET
	↓
PX4 Precision Landing
수평 접근 → 표적 위 하강 → 최종 접근
	↓
로그·지표를 관호에게 반환 → 모델 개선
```

## Interface Correction

내부 ROS 인터페이스와 PX4로 보내는 MAVLink 메시지를 구분한다.

- ROS 내부 `TargetObservation`: 상대 `x,y,z`, 회전 또는 yaw, detector confidence, position variance, timestamp, valid
- MAVLink `LANDING_TARGET`: PX4 기준 `MAV_FRAME_LOCAL_NED`의 표적 위치 `x,y,z`, `time_usec`, `target_num`, `position_valid`
- 카메라가 계산한 값은 기체 기준 상대 pose이므로 그대로 보내지 않는다. 기체의 local pose와 카메라 장착 변환을 이용해 `target_local_ned = vehicle_local_ned + rotated(target_relative)`로 변환한다.
- `LANDING_TARGET`에는 별도 confidence 필드가 없다. confidence와 분산은 통합 노드가 전송 여부를 결정하고 연구 로그에 기록한다.
- 기본선에서는 yaw를 내부 평가값으로 보존한다. PX4 yaw 정렬을 쓸 때는 VTE의 orientation 경로와 펌웨어 설정을 별도로 검증하며, 단순 `LANDING_TARGET` quaternion 전송만으로 동작한다고 가정하지 않는다.

```text
if confidence >= threshold
and pose_age <= max_age
and reprojection_error <= limit
and position_jump <= limit:
	position_valid = 1
	LANDING_TARGET(x, y, z) 전송
else:
	LANDING_TARGET 전송 중단 또는 position_valid = 0
	PX4 timeout/search/failsafe 동작 확인
```

## Two Comparable Interfaces

서로 다른 계층의 알고리즘을 한 표에서 직접 우열 비교하지 않는다.

### A. Perception Interface

아래 방식들은 모두 같은 영상에서 `TargetObservation`을 생성하도록 비교한다.

- ArUco/AprilTag + solvePnP
- 의미 아이콘 검출 + pose 추정 + Kalman filter
- YOLO keypoint/segmentation + pose 추정
- 자연 특징점 매칭 + homography/PnP

### B. Control Interface

아래 방식들은 같은 `TargetObservation`을 받아 속도·위치 명령을 생성하도록 비교한다.

- PX4 기본 Precision Landing controller
- PID controller
- 강화학습 controller

따라서 강화학습은 표적 검출 방식과 같은 종류가 아니다. 강화학습을 perception에 사용할 수도 있지만, 직접 제어에 쓴다면 PX4/PID와 별도의 controller 비교군으로 둔다.

## Team Responsibilities

| 담당 | 소유할 산출물 | 완료 기준 |
|---|---|---|
| 재완 | `.plan`, 시나리오 ID, waypoint·고도·속도·착륙 명령 | 같은 계획을 반복 실행할 수 있고 변경 이력이 남음 |
| 관호 | ROS 인식 노드, 모델 버전, 출력 메시지 | 영상 입력마다 상대 `x,y,z`, yaw, confidence, timestamp를 출력 |
| 규태 | SITL/Gazebo/QGC/MAVSDK 통합, 실행 자동화, 로그·평가 | 한 명령으로 시나리오 실행 후 공통 지표표를 생성 |

## Control Ownership Rule

QGC·MAVSDK·ROS Offboard가 동시에 위치나 속도 setpoint를 보내면 제어권 충돌과 재현성 저하가 생길 수 있다. 첫 기준선에서는 다음처럼 분리한다.

- QGC 또는 MAVSDK: 미션 업로드와 시작·중지
- ROS 알고리즘: 착륙 표적 관측값 생성
- PX4: 실제 비행·착륙 제어
- MAVSDK: 상태 모니터링, 실행 자동화, 로그 수집

강화학습이 속도 명령을 직접 출력하는 실험은 별도 branch로 두고, 그때만 PX4 Offboard 제어권을 명시적으로 인계한다.

## Minimal Equipment

### SITL 단계

- 기존 PC
- PX4 SITL, Gazebo, ROS, MAVSDK, QGroundControl
- Gazebo 하향 RGB 카메라
- Gazebo 착륙 표식 모델

### 실제 비행 단계

- 기존 기체와 Pixhawk
- 하향 RGB 카메라 1대
- Jetson 또는 Raspberry Pi 중 1대
- 인쇄 표식 1장 또는 복수 의미 아이콘 패드
- 안전조종기와 kill switch

초기에는 IR 비콘, IR 카메라, 카메라 2대, LiDAR를 필수 장비로 두지 않는다. 고도 오차가 병목으로 확인될 때만 rangefinder를 추가한다.

## Experimental Ladder

1. Gazebo 기본 ArUco/AprilTag와 고전적 pose 추정으로 end-to-end 연결을 검증한다.
2. 위치 노이즈·지연·표적 가림 조건을 추가하고 PX4 기본 착륙 성공률을 측정한다.
3. 관호 모델을 같은 입출력 계약으로 교체해 기준선과 비교한다.
4. 4번 방식의 일반 로고/객체 검출과 장애물 veto를 추가한다.
5. 이후 3번 자연 특징 기반 모델을 넣어 마커 기반 기준선과 비교한다.
6. 강화학습 직접 제어는 마지막 단계에서 PID/PX4 제어와 분리 비교한다.

## Metrics

- 착륙 중심 XY 오차(cm)
- 성공률과 착륙장 이탈률
- 표적 최초 검출 고도
- 표적 유실 횟수와 재획득 시간
- 영상 입력부터 표적 좌표 출력까지의 p50/p95 지연
- 잘못된 표적 선택률
- 장애물 존재 시 착륙 중단 성공률
- 시나리오별 seed, plan hash, model version, PX4 parameter set

## Patent Interpretation Boundary

이 판단은 기술 구조 적합성에 관한 연구 설계이며 특허 침해·실시 가능성에 관한 법률 의견이 아니다. 실제 구현 전에는 살아 있는 독립항과 연구·상용 사용 범위를 별도로 검토해야 한다.

> [!note] Bias Check
> 마커 기반 방식은 시뮬레이션 성공률과 재현성에서 유리해 보일 수 있지만 자연환경 일반화 능력을 과대평가하게 만들 수 있다. 반대로 강화학습은 연구적으로 매력적이어도 고전적 pose 추정+PX4 기준선을 이기지 못할 수 있으므로 동일 시나리오와 지표로 비교해야 한다.

이 답변은 학부연구생/학술 및 프로젝트 증거에 활용 가능합니다 — 팀 인터페이스와 반복 실험 기준을 명시해 연구 기여와 검증 과정을 분리해 보여주기 때문입니다.
