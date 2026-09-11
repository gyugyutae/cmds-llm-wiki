---
type: raw-source
aliases:
  - "계약랩 프로젝트 작업 메모"
  - "Contract Lab Work Notes"
description: "User-authored project notes on a ROS 2 drone environment, autonomous-landing decision axes, collaboration routines, and patent comparison tasks."
author:
  - "[[김규태]]"
date created: 2026-09-02
date modified: 2026-09-09
date ingested: 2026-09-10
tags:
  - raw-source
  - clippings
  - project-evidence
  - drone
  - autonomous-landing
source: "User-authored vault-root note: 계약랩.md"
category: "Clippings"
status: ingested
collectionPurpose: "프로젝트 증거 — 계약랩 활동에서 다룬 ROS 2·MAVSDK·QGroundControl 환경 구축, 드론 구동 확인, 자율착륙 판단 구조, 협업 방식, 특허 비교 과업을 보존해 포트폴리오와 면접 근거로 재사용하기 위해 수집."
mainVaultRelated: []
mainVaultCmds: ""
---

# 계약랩 프로젝트 작업 메모

## Source Notes

- Capture method: 프로젝트 루트에 있던 사용자 작성 Markdown 메모.
- Authorship boundary: 아래 내용은 [[김규태]]의 작업·회의 메모이며, 제3자 확인이나 실행 로그가 아니다.
- Evidence boundary: 환경 구축과 드론 구동 확인은 원문에 적힌 자기보고다. 구현 코드, 명령, 로그, 영상, 특허 문헌은 이 소스에 포함되지 않았다.
- Attribution boundary: 원문이 특정 인물의 판단·구현·검증 주체를 명시하지 않은 항목은 개인 기여로 확정하지 않는다.

---

## Original Content

9/2 
가제보 ros2 mavsdk qgc 이거 환경구축하기 
wsl로 하면 안되는경우가 있어서 듀얼부팅을 쓰던가 서버를 쓰는것임 좋다 
이거 구축다했고 드론 띄우는거까지 확인 

테스크 하나끝날때마다 검토하는게 좋다 
산출물이나 과업끝날때마다 연락으로 보고하기 

재완형은 동윤형님한테 연락해서 협업하기 
5명에서 뭉쳐서 한번 해보도록 하자 

9/9 
dof늘리려면 동역학모델써야함
의미 기하 연속이 세개의 축으로 가야한다 
의미: 마커나 그런것들이 지금 잘 위치해있나 
기하 : 착륙할수있는지 수학적으로 
연속은 의미 기하 이거두개가 앤드로 두개모두 반복적으로 참일때 착륙 지시를 내리는 것임 

모든 발표자료에는 써머리가 있어야함 
특허가 급한데 다음주에 이거를 특허를 낼수있는가? 가 나와야함 
민근형님이 자료보내주면 피규어2를 내가보고 피규어1을 관호형님이봄 
피규어 2에서 유사도 순서로 내림차순으로 정리되어있는데 

이거 유사도와 차별성을 중심으로 정리되어야함 
차별성이 있어야 특허를 하나 낼수가있다. 
앞에서 피규어 이거를 보고 우리 모델이랑 뭐가 유사한지 뭐가 다른지 Q102이런거를 보고 하나씩 말할수있어햐나다 
지금까지 진도나간거를 보내줄테니까 그거를 보고 우리가 어떤지를 공부하고 
3번4번을 보고 우리거랑 뭐가 다르고 뭐가 같은지 공부하기 
