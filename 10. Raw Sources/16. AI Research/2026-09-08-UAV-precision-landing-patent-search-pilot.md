---
type: raw-source
aliases:
  - UAV 정밀착륙 특허 3건 파일럿 조사
description: "A three-query pilot patent search for vision-based, markerless, and semantic-landmark UAV precision landing."
author:
  - Codex
date created: 2026-09-08
date modified: 2026-09-08
date ingested: 2026-09-08
tags:
  - raw-source
  - patent-research
  - uav
  - precision-landing
source:
  - "https://patents.google.com/patent/WO2019036361A1/en"
  - "https://patents.google.com/patent/US20170308100A1/en"
  - "https://patents.google.com/patent/CN110221625A/en"
category: AI Research
status: ingested
collectionPurpose: "학부연구생/학술·프로젝트 증거 - 정밀착륙 관련 연구·특허 조사와 학기 프로젝트의 지속적 지식 축적에 재사용하기 위해 수집"
mainVaultRelated: []
mainVaultCmds: ""
---

# UAV 정밀착륙 특허 3건 파일럿 조사

## Source Boundary

- 검색일: 2026-09-08
- 범위: 사용자 제공 검색식 3개에서 각각 대표 특허 1건
- 근거: 공개 특허공보의 서지정보, 초록, 명세서, 청구항
- 법적 상태: Google Patents 표시는 참고값이며 침해·무효·존속 판단은 각 관할 특허청 원부 확인이 필요하다.

## Original Content

### 검색식 1 — 영상 기반 정밀착륙

- 선정: `WO2019036361A1`, *Methods and systems for improving the precision of autonomous landings by drone aircraft on landing targets*
- 출원인: American Robotics, Inc.
- 공개일: 2019-02-21
- 연결 이유: 기체 카메라로 능동 표식을 촬영하고 저장 모델과 비교해 검증한 뒤 상대 위치·자세를 산출하여 연속적으로 착륙 유도를 보정한다.
- 주의: 능동 표식 기반이므로 마커리스 계열은 아니다. PCT 공개 건의 절차 상태와 국가별 패밀리 상태를 분리해야 한다.

### 검색식 2 — 마커리스·자연 특징

- 선정: `US20170308100A1` / `US10423167B2`, *System and method for automated landing of an unmanned aerial vehicle*
- 출원인: Uvionix Aerospace Corporation
- 공개일: 2017-10-26
- 연결 이유: 랜드마크가 별도 설치물이 아니라 착륙 구역에 이미 존재하는 특징일 수 있다고 설명하며, 카메라로 이를 식별·추적해 자동 하강한다.
- 주의: 자연 특징 사용을 포함하지만 인쇄 표식, 2D 코드, LED 실시예도 함께 포함하므로 마커리스 전용 특허는 아니다.

### 검색식 3 — 의미 아이콘 식별·검증

- 선정: `CN110221625A` / `CN110221625B`, *Autonomous landing guidance method for precise position of unmanned aerial vehicle*
- 출원인: Beijing Jiaotong University
- 공개일: 2019-09-10
- 연결 이유: 복수 의미 아이콘을 규칙과 데이터베이스로 식별·검증하고, 표적 중심·동적 상태를 산출해 3중 PID로 착륙한다.
- 주의: 자연 로고·상표 인식이 아니라 사전에 설계되고 의미가 알려진 아이콘 체계다.

## Compiled Links

- [[MOC-UAV 정밀착륙 연구]]
- [[UAV 정밀착륙 특허 검색 가이드]]
