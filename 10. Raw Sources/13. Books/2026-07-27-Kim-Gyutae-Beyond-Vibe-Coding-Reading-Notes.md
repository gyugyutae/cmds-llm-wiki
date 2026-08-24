---
type: raw-source
aliases:
  - 바이브 코딩 너머 개발자 생존법 독서 메모
  - Beyond Vibe Coding Reading Notes
description: "User-authored reading notes on moving from one-shot vibe coding toward testable, decomposed, and maintainable AI-assisted engineering."
author:
  - "[[김규태]]"
date created: 2026-07-27
date modified: 2026-07-27
date ingested: 2026-08-24
tags:
  - raw-source
  - books
  - ai-assisted-engineering
  - testing
  - software-engineering
source: "User-authored reading notes; book bibliographic details not recorded"
category: "Books"
status: ingested
collectionPurpose: "Codex 개발 워크플로 및 취업/포트폴리오 — 빠른 AI 코드 생성을 테스트·엣지케이스·문제 분해·도메인 규칙·성능 검증이 있는 AI 보조 엔지니어링으로 전환하는 개인 개발 원칙에 재사용하기 위해 수집."
mainVaultRelated: []
mainVaultCmds: ""
---

# 바이브 코딩 너머 개발자 생존법 독서 메모

## Source Notes

- Capture method: 프로젝트 루트에 있던 사용자 작성 독서 메모.
- Authorship boundary: 아래 내용은 [[김규태]]가 책을 읽고 중요하다고 판단한 요점이다.
- Bibliographic gap: 책의 저자·출판사·판본·정확한 인용 페이지가 원문에 없어 추가하지 않았다.
- Verification boundary: 구체적 기술 주장은 독립 검증 전까지 독서 메모 수준으로 유지한다.

---

## Original Content

다음은 바이브코딩너머 개발자 생존법 이책을 일고나서 내가 중요하다고 생각한부분들을 정리한 글이다 
중요하다고 생각한글과 collectionpurpose 가 함께 있다. 

테스트 케이스 생성하는것을 요구하기 엣지케이스들을 제시하면서 코드리뷰를 하기 
- 이자율이 0이면 어떻게돼? 
- 트래픽이 100배가 되면 어떻게돼? 
- 함수에 대한 단위테스트도 진행해줘

바이브 코딩은 단기적인 속도에 집중하고 ai 보조엔지니어링은  지속가능한 속도와 신뢰성에 집중한다. 

한 번에 전체 해결책을 요청하는 대신, 문제를 여러 단위로 세분화하여 각 단위를 AI에 개별적으로 제공하는 방법을 익히기

ai 보조 엔지니어링은 엣지케이스를 처리하고 참고무결 유지, 조직의 확립된 패턴을 따르도록 보장 
바이브코딩으로 초기 crud생성후 엔지니어 모드로 도메인별 규칙구현하여 빠른생성에서 정제단계로 전환하기
유사한 엔드포인트, 스키마각 유형에대한 클래스처럼 유사한 코드생성

복잡한 알고리즘 구현에는 보조엔지니어링이 유리 아키텍처와 최적화결정은 사람이내리고 구현의 정확성과 알고리즘적접근방식은 ai 
성능최적화는 보조엔지니어링이 유리 메모리관리 캐시최적화 병렬처리 지연시간감소 

ai가잘못하는것들 매우복잡한 시스템, 저수준 최적화 및 시스템 프로그래밍, 생소한 프레임워크 창의적인 ui, 비즈니스 규칙

나는솔로 성훈식 : ~하는 파이썬 스크립트를만들어줘 라고 요청하기 

원샷 프롬프트 정확한예시 한가지 제공 퓨샷2~5개 제공 데이터형식 정리하는데유용 
