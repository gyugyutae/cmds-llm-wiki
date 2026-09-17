---
type: wiki-page
aliases:
  - 드론 정밀착륙 특허 검색법
description: "A repeatable workflow for finding and validating UAV precision-landing patents across Korean and international patent databases."
author:
  - Codex
date created: 2026-09-08
date modified: 2026-09-08
tags:
  - llm-wiki
  - patent-search
  - uav
  - precision-landing
topic:
  - patent-research
  - computer-vision
related:
  - "[[MOC-UAV 정밀착륙 연구]]"
source:
  - "[[2026-09-08-UAV-precision-landing-patent-search-pilot]]"
claimType: prescriptive
evidenceScope: multi-source-primary
explored: false
verificationStatus: partial
---

# UAV 정밀착륙 특허 검색 가이드

## 데이터베이스 역할

| 목적 | 우선 검색처 | 쓰임 |
|---|---|---|
| 한국 특허 원문·법적 상태 | KIPRIS | 국문 키워드, 출원·등록번호, 청구항, 심사·등록 상태 확인 |
| 빠른 전 세계 선행기술 탐색 | Google Patents | 자연어·긴 Boolean 검색, 유사 문헌, 패밀리와 인용관계 탐색 |
| 국제 PCT 출원 확인 | WIPO PATENTSCOPE | PCT 원문, 국제공개번호, 국제단계 서지정보 확인 |
| 유럽·글로벌 패밀리/분류 탐색 | Espacenet | INPADOC 패밀리, CPC/IPC 분류, 국가별 문헌 확장 |
| 미국 권리 상태 최종 확인 | USPTO Patent Center | 미국 출원 경과와 최신 원부 확인 |

탐색은 Google Patents에서 넓게 시작하고, 한국 건은 KIPRIS, PCT 건은 PATENTSCOPE, 미국 건은 USPTO에서 최종 확인한다. Google Patents의 legal status는 법적 결론이 아니라 탐색 보조값으로 취급한다.

## 검색식 개선

한국어 동의어만으로는 해외 특허를 놓치므로 검색식별 영문 축을 함께 사용한다.

1. 비전 정밀착륙: `(UAV OR drone OR unmanned aircraft) AND (precision landing OR autonomous landing) AND (vision OR camera OR image)`
2. 마커리스: `(UAV OR drone) AND landing AND (markerless OR natural feature OR pre-existing feature OR visual landmark)`
3. 의미 표식: `(UAV OR drone) AND landing AND (logo OR symbol OR semantic icon OR visual landmark) AND (recognition OR identification OR verification OR authentication)`

결과가 많으면 `B64U70/95` 같은 착륙 유도 CPC와 `G05D1/10`, `G01S5/16`을 결합한다. 결과가 너무 적으면 `precision`을 빼고 `docking`, `landing target`, `landing platform`을 추가한다.

## 엑셀 기록 최소 기준

- 공개번호와 출원번호를 구분한다.
- 공개일과 우선일을 혼동하지 않는다.
- 요약은 초록이 아니라 독립항을 기준으로 쓴다.
- `마커리스 포함`과 `마커리스 전용`을 구분한다.
- 출원 공개, 등록, 소멸을 분리하고 상태 확인처와 확인일을 비고에 남긴다.
- 연구 적용성은 현재 시스템의 카메라, PX4, companion computer, 착륙 표적 조건에 맞춰 판단한다.

> [!note] Bias Check
> 검색어와 번역어에 따라 중국·미국 특허가 과대표집될 수 있다. 제목·초록 적합성만으로 권리범위를 판단하지 말고 독립항, 패밀리, 최신 법적 상태를 다시 확인해야 한다.
