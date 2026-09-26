---
type: moc
aliases:
  - Portfolio MOC
  - 취업 포트폴리오
  - Portfolio Evidence Wiki
description: Map of Content for using this LLM Wiki as a job-search portfolio evidence backend, centered on project proof, interview stories, resume bullets, and reusable career artifacts.
author:
  - Codex
date created: 2026-07-07
date modified: 2026-09-26
tags:
  - moc
  - portfolio
  - career
  - evidence
topic:
  - portfolio
  - career
  - project-evidence
source:
  - "[[2026-09-12-Kim-Gyutae-Java-Spring-AWS-Study-Declaration]]"
  - "[[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]"
  - "[[2026-07-23-Kim-Gyutae-Self-Understanding-Interview-v1]]"
  - "[[2026-07-12-Velog-Leadership-Product-Hackathon-Bundle]]"
  - "[[2026-08-24-Kim-Gyutae-TMU-SDG-Portfolio-Record]]"
  - "[[2026-09-02-to-09-Kim-Gyutae-Contract-Lab-Work-Notes]]"
related:
  - "[[김규태 Java-Spring-AWS 금융 포트폴리오 기초 학습 트랙]]"
  - "[[Core Context]]"
  - "[[김규태]]"
  - "[[financial-order-latency-lab]]"
  - "[[financial-lab]]"
  - "[[경제적 자유는 나의 북극성이다]]"
  - "[[MOC-김규태 Self Knowledge]]"
  - "[[MOC-UAV 정밀착륙 연구]]"
  - "[[Graduation-elasticsearch]]"
  - "[[cuee]]"
  - "[[harness]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[김규태 Career Narrative]]"
  - "[[김규태 금융 시스템 개발자 취업 로드맵]]"
  - "[[김규태 Leadership and Teaching Evidence]]"
  - "[[개발자 롤모델을 GitHub에서 공부하는 법]]"
  - "[[코딩테스트는 AI 시대의 문제해결력 훈련이다]]"
  - "[[컴퓨팅 사고의 추상화와 분해]]"
  - "[[AI 시대의 개발자 학습 전략]]"
  - "[[일반 지식보다 도메인 지식이 중요해지는 이유]]"
  - "[[능력 조합으로 희소성을 만드는 전략]]"
  - "[[TMU Global Leadership Program]]"
  - "[[FPT Vietnam Global Big Data AI Program]]"
  - "[[GNU Buddy]]"
  - "[[김규태 개발 도메인 영어 성장 계획]]"
  - "[[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]"
  - "[[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]"
  - "[[2026-09-04-Q-finance-backend-ai-era-job-preparation]]"
  - "[[2026-09-09-Q-kb-securities-java-backend-starting-plan]]"
  - "[[AI와 머신러닝 시대의 퀀트 리서치]]"
  - "[[백테스트 과적합과 편향]]"
  - "[[변동성 트레이딩과 델타 헤징]]"
  - "[[시장중립은 무위험이 아니다]]"
  - "[[AI 팩토리와 토큰 생산 인프라]]"
  - "[[메타인지 학습 루프]]"
  - "[[겸손과 자기표현의 균형]]"
  - "[[계약랩]]"
  - "[[2026 넥토리얼 지원]]"
  - "[[2026-09-18-Q-worldjob-overseas-entry-level-developer-resume-strategy]]"
status: active
explored: false
confidence: medium
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# MOC-Portfolio

> 이 Map of Content는 이 vault를 취업 포트폴리오 Evidence Wiki로 쓰기 위한 운영 허브다.

---

## Target Profile

- **Owner**: [[김규태]]
- **Current status**: 개발자 취업준비생, 경상국립대학교 소프트웨어공학과 학사원장상 4학년(2026-2학기 7번째 정규학기), SEALAB 학부연구생
- **Expected graduation**: 2027년 8월 예정, 졸업 후 출국 시점 제약 없음(사용자 자기보고)
- **Overseas role range**: Backend를 중심축으로 QA Automation과 Data 직무까지 지원 가능
- **English baseline**: TOEIC 730점 사용자 자기보고, TMU 4주·100시간 영어 몰입 과정, 베트남 1개월 AI 프로그램 GraphRAG 팀 프로젝트 경험
- **Portfolio objective**: 금융권·핀테크 Java 백엔드·거래 인프라 취업을 1차 목표로 하며, 드론·반도체 도메인도 장기 관심사로 탐색
- **Preferred tone**: 열정과 성장가능성이 드러나되, 성능·데이터 처리·설계·개발·팀 리딩·AI 활용 검증 근거가 있는 취업준비생 톤
- **Primary language direction**: Java를 새 주언어로 학습하고, Python은 부하 테스트·분석·자동화에 활용
- **GitHub-based stack**: Python, Java, Kotlin, TypeScript/React, JavaScript, C, Shell/PowerShell, Dockerfile, PLpgSQL
- **Public profiles**: [GitHub](https://github.com/gyutaetae), [Velog](https://velog.io/@gyutaetae/posts), [LinkedIn](https://www.linkedin.com/in/%EA%B7%9C%ED%83%9C-%EA%B9%80-90763b407/), [Instagram](https://www.instagram.com/kyu_tae_/)

---

## Portfolio Spine

현재 포트폴리오 spine은 아래 순서를 기본값으로 둔다.

| Priority | Project | Portfolio Role |
|----------|---------|----------------|
| 1 | [[financial-lab]] (`Reliable Bank Transfer Ledger Lab`) | 구현을 시작한 대표 학습 프로젝트. 메모리 기반 계좌 API와 이체를 만들었으며, 이후 DB 트랜잭션·원장·동시성·멱등성을 직접 검증한다 |
| 2 | [[financial-order-latency-lab]] | 백엔드 성능 문제의식과 p99 latency 실험 기록. 기존 코드는 AI 작성 범위가 커 보조 증거로 둔다 |
| 3 | [[Graduation-elasticsearch]] | 학부연구생/연구 경험, JavaParser, Elasticsearch Java source-test traceability |
| 4 | [[cuee]] | 경남권 창업동아리 대상작, 노인 모빌리티 예약 길잡이 앱 |
| 5 | [[harness]] | 커서맛피아님 harness를 참고해 앱 개발에 맞게 개인화한 Codex 개발 workflow |

새 Java 계좌이체·거래원장 시스템은 기존 프로젝트의 직접 구현 증거 공백을 채우는 최우선 프로젝트로 진행 중이다. 코드 저장소는 `C:\Users\kym70\financial-lab`이며 현재는 메모리 기반 API와 이체 테스트 단계다. 진행 상태와 기여 경계는 [[financial-lab]], 원래 목표와 확장 순서는 [[2026-09-13-Q-java-bank-transfer-ledger-portfolio-design]]을 따른다. 아직 대표 포트폴리오 완성본은 아니다.

그 전 단계의 공식 학습 spine은 [[김규태 Java-Spring-AWS 금융 포트폴리오 기초 학습 트랙]]이다. 두 권의 Spring Boot 교재를 병렬로 공부하며 생기는 질문, 오개념, 직접 구현과 테스트를 누적하고, 반복 약점을 우선 보완한 뒤 주문 시스템 증거로 연결한다.

---

## Career Narrative Pages

- [[2026 넥토리얼 지원]] — 2026-09-11 서류 합격 자기보고와 신규 AI면접 준비·증거 경계
- [[김규태 Career Narrative]] — 자기소개, 목표 회사/도메인, 성장 과제, 면접용 내러티브
- [[김규태 금융 시스템 개발자 취업 로드맵]] — 지방 국립대 소프트웨어공학과 4학년 관점의 Java 전환과 금융권·핀테크 주문 시스템 취업 준비
- [[김규태 Java-Spring-AWS 금융 포트폴리오 기초 학습 트랙]] — 두 Spring Boot 교재의 질문·오개념·재시험을 Java 주문 시스템 전의 직접 구현 기초로 누적하는 중심 학습 축
- [[AI-Augmented Developer Positioning]] — AI 의존이 아니라 AI를 활용해 개발 역량을 증폭하는 사람으로 설명하는 프레임
- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]] — AI 없이 문제를 분해하고 직접 구현·검증할 수 있음을 보여주는 기본기 증거 축
- [[컴퓨팅 사고의 추상화와 분해]] — 현실 문제를 입력·출력·제약으로 바꾸고 블랙박스 내부를 하위 문제로 나누는 개발자 사고 원칙
- [[AI 시대의 개발자 학습 전략]] — 기초 CS, 도메인 지식, AI 협업, 검증, 메타인지를 결합한 학습 프레임
- [[일반 지식보다 도메인 지식이 중요해지는 이유]] — 백엔드·금융·반도체·드론의 구체 제약을 포트폴리오 차별점으로 만드는 가설
- [[능력 조합으로 희소성을 만드는 전략]] — 개발 중심축에 성능·도메인·AI·리더십·커뮤니케이션 능력을 증거 기반으로 결합하는 전략
- [[김규태 Leadership and Teaching Evidence]] — 실리콘밸리 대표, 멋쟁이사자처럼 부대표, 백엔드 세션, 해커톤 템플릿 증거
- [[TMU Global Leadership Program]] — 4주·100시간 영어 몰입 과정과 SDG 학습의 증빙·표현 경계
- [[FPT Vietnam Global Big Data AI Program]] — 다국적 팀 일정 조율, 반도체 위험 타깃 설정, 금융 GraphRAG 결과물과 개인 기여 경계
- [[GNU Buddy]] — 외국인 유학생 적응 지원 44.23시간과 문화간 일정 조율 경험
- [[김규태 개발 도메인 영어 성장 계획]] — 수료 경험을 영어 README·기술 문서·설명 증거로 전환하는 계획
- [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]] — 장기 퀀트/HFT 관심을 가설·데이터·비용·검증 문제로 구체화하는 학습 지도
- [[AI와 머신러닝 시대의 퀀트 리서치]] — AI 활용 가능성과 model-risk 책임을 함께 보는 탐색 지도
- [[백테스트 과적합과 편향]] — 누수·선택·비용·다중 검정 위험을 점검하는 학습 체크리스트
- [[시장중립은 무위험이 아니다]] — beta·delta 중립과 잔여 위험을 구분하는 검증 페이지
- [[변동성 트레이딩과 델타 헤징]] — gamma·theta·비용을 포함한 옵션 학습 지도
- [[AI 팩토리와 토큰 생산 인프라]] — 반도체·전력·네트워크·모델을 잇는 NVIDIA의 인프라 프레임
- [[메타인지 학습 루프]] — 오류 원인과 재검증을 기록하는 개인 학습 실험
- [[겸손과 자기표현의 균형]] — 기여 경계를 밝히면서 근거 있게 표현하는 포트폴리오 원칙
- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]] — AI 초안을 테스트·도메인 규칙·성능 검증으로 인수하는 개발 원칙
- [[2026-09-04-Q-finance-backend-ai-era-job-preparation]] — 책·자격증·금융 거래 프로젝트·AI 검증·코딩테스트·지원 전략을 통합한 2026–2027 실행안
- [[2026-09-09-Q-kb-securities-java-backend-starting-plan]] — Java·SQL이 시작 단계인 현재 기준선에서 모의 증권 주문 MVP까지 가는 첫 8주 계획

---

## Project Evidence Map

| Project | What To Prove | Missing Evidence |
|---------|---------------|------------------|
| [[financial-lab]] | 사용자가 Java/Spring Boot 계좌 API와 메모리 기반 이체 흐름을 직접 구현하고, 정상·잔액 부족 이체 테스트를 작성했다. 현재 코드와 최근 Gradle 테스트 결과를 확인했다 | 존재하지 않는 수취 계좌·동일 계좌 실패 테스트, DB/JPA 영속성, rollback, 거래 원장, 동시성·멱등성, 성능·운영 증거 |
| [[financial-order-latency-lab]] | 사용자가 CPU·GPU·disk latency를 금융 관점에서 비교한다는 문제를 제시했고, AI가 p99 조건·전체 코드·실행·재실험·해석을 수행했다. 현재는 구현력 증거가 아니라 문제의식과 미검증 AI 활용의 한계 기록이다 | 수업 요구사항, 사용자 판단 범위, 직접 재현·설명·수정 가능한 구현, 발표자료, Linux 재측정 |
| [[Graduation-elasticsearch]] | 공개 저장소에 JavaParser AST/Symbol Solver 기반 TEST FILE -> SOURCE FILE artifact가 있고, 사용자는 AI 생성 parser 결과의 분류 불일치를 발견해 개선 방향을 도출했다. [[EvolvingTraceDB Neo4j 구축 및 검증 가이드]]에는 그래프 적재·검증 기록이 있다. 사용자 직접 구현은 아직 증명되지 않았다 | 연구실/졸업 연구 맥락, 본인 기여율, 직접 작성·재실행한 parser, 개선안 재실행, 교수 지도·피드백 증빙 |
| [[cuee]] | `배우담`에서 `cuee`로 전환한 사용자 판단과 접근성 overlay fixture demo가 존재한다 | 사용자 직접 구현 범위, 실제 사용자 테스트, live Korail 검증, 발표자료·심사 피드백, Play Store 심사 |
| [[harness]] | 기존 harness를 앱 개발에 맞는 Codex workflow로 개인화했다는 사용자 기록과 구조 설명이 있다 | 현재 공개 코드, 원본 대비 diff, 자동화 흐름과 사용 예시, 실제 개발 시간·오류·품질 효과, 한계와 개선 계획 |
| [[harness]] / Threads automation | Codex와 토큰 기반 자동화 workflow를 이용해 AI agent 논문 활용 예시를 Threads에 반복 발행했다. 팔로워 수는 2026-07-23 사용자 진술 기준 500명이다 | 실제 코드/스크립트 위치, 토큰 발급 방식, 스케줄러 설정, 실패 처리, API 또는 화면 기반 팔로워 증빙 |
| [[계약랩]] | 사용자 메모에 ROS 2·MAVSDK·QGroundControl 환경 구축, 드론 구동 확인, 자율착륙 판단 분해, 특허 비교 과업이 기록되어 있다 | 공식 프로젝트 맥락, 본인 기여 범위, 저장소·명령·로그·영상, 알고리즘 상세, 선행특허 비교표와 출원 결과 |
| [[김규태 Leadership and Teaching Evidence]] | 실리콘밸리 취업동아리 대표와 멋쟁이사자처럼 14기 부대표로 운영/교육/해커톤 준비를 수행했다 | 회의록, 예산/지원금 자료, 백엔드 세션 수업 자료, 팀원 피드백, GNU 해커톤 템플릿 실제 사용 결과 |

---

## Evidence To Ingest

`00. Inbox/`에 넣고 `/ingest`할 우선 자료:

- 프로젝트 README, docs, architecture note
- 성능 측정 결과, 그래프, before/after 수치
- 트러블슈팅 로그와 실패 기록
- GitHub issue, PR, commit 설명
- 발표자료, 회고, TIL
- 자기소개서 초안, 이력서 초안, 면접 답변 초안
- Codex와 같이 작업한 대화 중 중요한 기술 판단
- AI가 생성한 코드와 본인이 직접 판단/구현/검증한 부분을 분리한 기록
- 창업동아리 대상 수상/평가 자료
- 연구실 활동 기록, 연구 주제 메모, 담당 업무 기록
- GitHub README, 주요 commit, issue, PR, release note
- [[코딩테스트는 AI 시대의 문제해결력 훈련이다|코딩테스트 풀이 로그]]와 AI 없이 구현한 작은 기능 기록
- 개발 도메인 영어 학습 기록과 영어 README/기술 설명
- [[2026-08-24-Kim-Gyutae-TMU-SDG-Portfolio-Record]] — TMU 수료·학습·영어 성장과 공개 증빙 경계
- [[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]] — AI 보조 엔지니어링 독서 메모
- 실리콘밸리 동아리 회의록, 예산/지원금 자료, 책 수요조사, 교수 피드백
- 멋쟁이사자처럼 백엔드 세션 자료와 GNU 해커톤 템플릿 실제 사용 결과
- Velog/GitHub 원문 근거 묶음: [[2026-07-12-Velog-Leadership-Product-Hackathon-Bundle]]

권장 `collectionPurpose`:

```text
취업/포트폴리오 - 이 자료를 프로젝트 증거로 보존하고 이력서/면접 답변에 재사용하기 위해 수집
```

---

## Evidence Page Shape

프로젝트 관련 Wiki page나 Query result는 가능한 한 아래 구조로 정리한다.

| Field | Question |
|-------|----------|
| Problem | 어떤 문제를 풀었나? |
| Abstraction | 현실 문제를 어떤 입력·출력·제약·인터페이스로 바꾸었나? |
| Decomposition | 블랙박스를 어떤 하위 문제와 의존성으로 나누었나? |
| My Judgment | 내가 직접 판단한 것은 무엇인가? |
| Agent Work | 에이전트에게 맡긴 것은 무엇인가? |
| Implementation | 무엇을 만들었나? |
| Verification | 어떻게 검증했나? |
| Metric | 전후 수치나 결과는 무엇인가? |
| Failure | 실패와 수정은 무엇이었나? |
| Interview Line | 면접에서 1문장으로 어떻게 말할 것인가? |
| Evidence | Raw Source, GitHub, log, graph 등 근거는 어디인가? |

AI 활용 프로젝트는 아래 두 항목을 추가한다.

| Field | Question |
|-------|----------|
| Non-AI Core | AI 없이도 직접 설명하고 수정할 수 있는 핵심은 무엇인가? |
| AI Boundary | AI가 만든 부분을 어디까지 검증했는가? |

---

## Resume Positioning

현재 기본 포지셔닝:

> Codex를 적극 활용해 앱 개발, 자동화, 프로젝트 증거화를 수행하는 개발자 취업준비생. AI에 의존하는 개발자가 아니라 AI를 개발 역량의 증폭기로 활용하는 사람으로 성장하기 위해, 직접 판단한 부분과 AI가 도운 부분을 분리해 기록하고 검증한다.

백엔드 중심으로 다듬은 기본 포지셔닝:

> 금융 latency, 데이터 처리, Android 접근성, Codex 자동화 문제를 탐색해 온 개발자 취업준비생. Java를 새 주언어로 학습하고 Python을 분석·자동화에 활용하며, 현재 프로젝트 상당 부분이 AI 생성 코드에 의존했다는 한계를 공개하고 직접 설명·수정·재현 가능한 Java 백엔드 증거를 보강하고 있다.

이 문장은 아직 초안이다. 실제 이력서에는 지원 직무와 회사 유형에 맞춰 더 날카롭게 다듬는다.

### Overseas Entry-Level Route

해외 신입 지원은 선호 국가와 실제 진입 경로를 분리한다. 장기 선호는 미국 → 캐나다 → 유럽이지만, 2027년 8월 졸업예정을 기준으로 캐나다 IEC, 미국 J-1/WEST의 졸업 전후 12개월 창구, 독일 기회카드·신규 졸업자 EU Blue Card 요건을 각각 확인한다. 상위 직무 정체성은 `신뢰할 수 있는 데이터 시스템을 만드는 신입 소프트웨어 엔지니어`로 두고 Backend·QA Automation·Data 지원본을 분리한다. 월드잡 공개 이력서는 국가 중립형으로 유지하고 지원 공고마다 미국·캐나다·독일 버전을 별도로 사용한다. 상세 조사와 5축 100점 준비도 기준은 [[2026-09-18-Q-worldjob-overseas-entry-level-developer-resume-strategy]]를 따른다.

---

## Query Prompts

자주 쓸 query:

- [[개발자 롤모델을 GitHub에서 공부하는 법]] — 유명세보다 공개된 개발 판단을 관찰하고 현재 프로젝트에 한 가지씩 이식하는 방법

```text
/query 금융권 백엔드/시스템 직무에 맞게 내 프로젝트 3개를 STAR 형식으로 정리해줘
```

```text
/query 개발자 취업준비생 톤으로 financial-order-latency-lab을 면접에서 2분 안에 설명할 수 있게 정리해줘
```

```text
/query Graduation-elasticsearch를 학부연구생 연구 경험으로 백엔드/데이터 직무에 맞게 설명해줘
```

```text
/query 내 포트폴리오에서 가장 강한 증거와 약한 증거를 취업 관점으로 구분해줘
```

```text
/query 이력서 프로젝트 bullet 5개 만들어줘. 수치와 검증 중심으로.
```

```text
/query 내가 판단한 것과 에이전트에게 맡긴 것을 프로젝트별로 분리해서 정리해줘
```

```text
/query AI 의존 개발자로 보이지 않게, 내 프로젝트별로 비-AI 핵심 역량과 AI 활용 경계를 정리해줘
```

```text
/query KB국민은행/네이버/SK하이닉스/삼성전자 중 어디에 맞춰 포트폴리오를 다듬을지 현재 증거 기준으로 비교해줘
```

```text
/query cuee를 노인 모빌리티 예약 문제 해결 앱으로 설명하는 자기소개서 문단을 만들어줘
```

```text
/query harness 프로젝트를 Codex 기반 개발 생산성 개선 경험으로 정리해줘
```

```text
/query 실리콘밸리 동아리 대표와 멋쟁이사자처럼 부대표 경험을 신입 개발자 리더십 답변으로 정리해줘
```

---

## Quality Gate

포트폴리오에 쓰기 전에 확인할 기준:

- 수치가 있는가?
- 검증 명령이나 재현 방법이 있는가?
- 내가 직접 판단한 내용이 분리되어 있는가?
- 에이전트가 한 작업을 과장하지 않았는가?
- 실패 기록이 삭제되지 않고 설명되어 있는가?
- GitHub/Raw Source/Query Result 근거가 연결되어 있는가?
- 면접에서 2분 안에 설명 가능한가?
- AI가 만든 부분과 내가 직접 판단/검증한 부분이 분리되어 있는가?
- AI 없이도 설명 가능한 최소 구현/기초 역량 증거가 있는가?
- 현실 문제에서 코드 구조로 넘어가는 추상화·분해 과정이 기록되어 있는가?

> [!note] Bias Check
> 이 MOC는 취업 포트폴리오를 설계하는 운영 지도이므로 사용자 진술, 저장소 기록, AI가 정리한 해석이 함께 섞여 있다. 프로젝트 존재와 관심사를 실제 구현 기여·재현 능력·성과 증명으로 확대 해석하지 않는다. 특히 `financial-order-latency-lab`의 수치와 코드는 AI가 생성·실행했고 사용자가 별도 검증하지 못했으며, Threads 팔로워 500명도 현재는 사용자 진술로만 확인된다.

---

## Current Gaps

> [!question] Project evidence ingest
> `financial-order-latency-lab`, `Graduation-elasticsearch`, `cuee`, `harness`의 README, docs, 성능 결과, 회고를 아직 이 vault에 체계적으로 ingest하지 않았다.

> [!question] Resume output template
> 이력서 bullet, STAR 답변, 자기소개서 문단을 저장할 Query Result 템플릿을 별도로 만들지 않았다.

> [!question] Target role sharpening
> 현재 현실적인 1차 목표는 서울 증권사의 백엔드·거래 인프라 IT 직군이며, 장기 탐색 방향은 퀀트/HFT 시스템 개발이다. 계정계, 주문 FEP, 주전산 인프라, 정보계 중 첫 지원 직무의 우선순위는 [[김규태 금융 시스템 개발자 취업 로드맵]]에서 계속 구체화한다.

> [!question] Quantified results
> 프로젝트별 성능 수치, 팀 규모, 기간, 수상 증빙, 사용자/테스트 결과가 아직 부족하다.

> [!question] AI boundary evidence
> GitHub 레포에서 AI가 만든 부분과 본인이 직접 판단·구현·검증한 부분을 분리한 증거가 부족하다. AI 비의존 구현 기록을 의도적으로 채워야 한다.

> [!question] Leadership operation evidence
> 실리콘밸리 동아리 회의록, 예산/지원금 관리 자료, 책 수요조사, 교수 피드백, 멋쟁이사자처럼 백엔드 세션 자료는 추후 사용자가 제공하기로 했다.

> [!question] Hackathon template outcome
> `GNU_hackathon_templete`는 다음 달 대회에서 사용할 예정이므로, 실제 사용 결과와 팀원 피드백은 아직 없다.

---

## Related

- [[Core Context]]
- [[김규태]]
- [[financial-order-latency-lab]]
- [[Graduation-elasticsearch]]
- [[cuee]]
- [[harness]]
- [[LLM Wiki Pattern]]
- [[Ingest-Query-Lint Cycle]]
- [[Human-AI Knowledge Boundary]]
- [[AI-Augmented Developer Positioning]]
- [[김규태 Career Narrative]]
- [[김규태 금융 시스템 개발자 취업 로드맵]]
- [[김규태 Leadership and Teaching Evidence]]
- [[TMU Global Leadership Program]]
- [[김규태 개발 도메인 영어 성장 계획]]
- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]
- [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]]
- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
- [[2026-09-18-Q-worldjob-overseas-entry-level-developer-resume-strategy]]
