---
type: moc
aliases:
  - Wiki Index
  - Master Index
description: Master index of the LLM Wiki. Central navigation hub listing all Wiki pages organized by category (Concepts, Entities, Guides, Maps). Updated automatically on every ingest operation.
author:
  - "[[김규태]]"
date created: 2026-07-07
date modified: 2026-09-23
tags:
  - index
  - moc
  - system
status: active
---

# 📖 LLM Wiki — Master Index

> **Architecture**: Karpathy LLM Wiki Pattern
> Raw Sources → **LLM Compiler** → This Wiki

이 볼트는 LLM 이 직접 작성하고 관리하는 **persistent knowledge wiki** 입니다.
매번 query 마다 재합성하지 않고, 한 번 컴파일된 지식이 계속 성장합니다.

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| Raw Sources | 50 |
| Wiki Pages | 78 |
| Concepts | 40 |
| Entities | 14 |
| Guides | 18 |
| MOCs | 6 |
| Queries | 64 |

> *Stats 는 `/ingest` 실행 시 자동 갱신됩니다. 본인 컨텐츠를 채워나가면서 업데이트.*

---

## 🗂 Wiki Pages

아래는 현재 Wiki 페이지 목록입니다. 새 소스를 ingest 할 때마다 이 목록이 자라납니다.

### Concepts

> 추상 개념, 기술, 방법론

- [[LLM Wiki Pattern]] — LLM 이 raw source 를 컴파일하여 persistent wiki 를 관리하는 패턴
- [[RAG vs Compiled Wiki]] — RAG(매번 재검색) vs Compiled Wiki(한 번 컴파일)의 비교
- [[3-Layer Architecture]] — Raw Sources / Wiki / Schema 3층 구조
- [[Ingest-Query-Lint Cycle]] — Wiki 운영의 세 가지 핵심 작업 (Ingest, Query, Lint)
- [[LLM Wiki as Learning Base]] — 관심 있지만 아직 모르는 source를 공부 가능한 지식 지도로 만드는 관점
- [[Mothership-Satellite Vault Pattern]] — 메인 지식 볼트와 LLM-managed Wiki 볼트의 역할 분리
- [[Agent-Readable Metadata]] — 에이전트가 먼저 읽는 YAML metadata 설계
- [[Human-AI Knowledge Boundary]] — AI가 생성한 지식과 사용자가 실제로 아는 지식의 경계
- [[AI-Augmented Developer Positioning]] — AI 의존이 아니라 AI를 개발 역량의 증폭기로 설명하는 포트폴리오 프레임
- [[레버리지를 당하지 않고 사용하는 삶]] — 자본·AI·콘텐츠·제품·사람 레버리지를 직접 사용하는 개인 전략
- [[자본 레버리지는 자유의 핵심 엔진이다]] — 1억 임계점, 현금 20%, 2배 ETF, DCA, 암호화폐 비중을 정리한 투자 운영 가설
- [[AI 자동화는 개인 생산성 레버리지다]] — Codex, harness, Threads, 멀티 에이전트 workflow를 개인 생산성 레버리지로 보는 관점
- [[독서는 판단력과 자산관리의 기반이다]] — 지식 복리, 자산관리 판단력, 논픽션/픽션 균형 독서 프레임
- [[Book Ingest Pattern]] — 긴 책과 문서를 index/stub/promotion 방식으로 점진 인제스트하는 패턴
- [[Cohort Token Economy]] — 조직형 LLM 활용에서 토큰 비용과 지식 재사용을 관리하는 관점
- [[External Pre-processing Pattern]] — 외부 도구에서 전처리한 자료를 LLM Wiki로 연결하는 패턴
- [[Idea Generation Pipeline]] — 축적된 지식에서 아이디어 후보를 만드는 흐름
- [[Track Classification and Research Gap Detection]] — 자료를 트랙으로 분류하고 연구 공백을 찾는 방식
- [[김규태 Motivation and Execution Pattern]] — 빠른 시작, 인정욕구, 돈, 가시적 피드백과 유지보수 난점
- [[김규태 Breadth-to-Depth Development Pattern]] — 넓은 관심을 T자형 전문성으로 바꾸는 성장 과제
- [[김규태 Stress and Recovery Pattern]] — 문제 좌절 뒤 회피·휴식·복귀 패턴
- [[김규태 Leadership Pattern]] — 비전 주도 강점과 일정·행정·타인 결과 관리의 약점
- [[김규태 Attachment and Romantic Pacing Pattern]] — 오래 지속되는 호감, 반추, 빠른 감정 속도와 상호성 기준
- [[김규태 Taste and Intellectual Intimacy]] — 영화·음악·책·토론을 정체성과 친밀감으로 쓰는 방식
- [[Schema Engineering for LLM Wiki]] — agent가 일관되게 Wiki를 유지보수하도록 page type, metadata, workflow 규칙을 설계하는 기술 영역
- [[Personal Context Layer for LLM Wiki]] — LLM에게 나에 대한 고품질 맥락을 제공해 개인 맞춤형 답변을 가능하게 하는 위키 관점
- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]] — 코딩테스트를 AI 시대의 문제해결력, 컴퓨팅 사고력, 비-AI 구현 기본기 증거로 해석하는 관점
- [[컴퓨팅 사고의 추상화와 분해]] — 현실 문제를 입력·출력·제약으로 추상화하고 블랙박스 내부를 하위 문제·의존성·예외 상황으로 분해하는 개발자 사고 원칙
- [[AI 시대의 개발자 학습 전략]] — 기초 CS, 문제 구조화, 도메인 지식, AI 협업, 검증, 메타인지를 결합한 개인 학습 프레임
- [[메타인지 학습 루프]] — 모르는 지점과 오답 원인을 진단하고 직접 시도·수정·재검증하는 반복 학습 체계
- [[일반 지식보다 도메인 지식이 중요해지는 이유]] — 일반 지식의 상품화 속에서 현장 제약과 구체 도메인 판단의 가치를 탐색하는 커리어 가설
- [[능력 조합으로 희소성을 만드는 전략]] — 개발을 중심축으로 성능·도메인·AI·리더십·커뮤니케이션 능력을 증거 기반으로 결합하는 전략
- [[겸손과 자기표현의 균형]] — 자기축소가 아니라 근거 있는 자기표현과 수정 가능성을 함께 유지하는 지적 겸손 프레임
- [[AI 팩토리와 토큰 생산 인프라]] — AI를 전력·반도체·네트워크·모델·애플리케이션이 연결된 토큰 생산 시스템으로 보는 인프라 관점
- [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]] — 시장 관찰을 반증 가능한 가설, 시점 보존 데이터, 비용 포함 백테스트와 미사용 구간 검증으로 연결하는 학습 지도
- [[백테스트 과적합과 편향]] — 생존·룩어헤드·선택·다중 검정·비용·공매도 가능성 오류를 점검하는 체크리스트
- [[시장중립은 무위험이 아니다]] — 측정 beta를 줄여도 factor·유동성·레버리지·모델·실행 위험이 남는다는 경계
- [[변동성 트레이딩과 델타 헤징]] — 델타 중립과 beta 중립을 구분하고 gamma·theta·변동성·비용을 함께 보는 학습 지도
- [[AI와 머신러닝 시대의 퀀트 리서치]] — 고차원 데이터·비선형 모델·신호 자동화·주문 실행과 모델 리스크의 변화
- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]] — AI 초안을 분해·테스트·도메인 규칙·성능 검증을 거쳐 직접 인수하는 개발 원칙

### Entities

> 사람, 조직, 제품, 모델

- [[Andrej Karpathy]] — AI 연구자, LLM Wiki 패턴 제안자
- [[Vannevar Bush]] — Memex 개념 제안자 (1945)
- [[Memex]] — 문서 간 associative trail 을 가진 개인 지식 저장소 구상
- [[김규태]] — 이 standalone LLM Wiki의 소유자이자 운영자
- [[financial-order-latency-lab]] — 금융 주문 서버 p99 latency 성능 실험 프로젝트
- [[Graduation-elasticsearch]] — JavaParser 기반 Elasticsearch source-test traceability 분석 프로젝트
- [[cuee]] — 노인 모빌리티 예약 길잡이 접근성 앱 프로젝트
- [[harness]] — Codex CLI 기반 개인화 개발 workflow harness
- [[qmd]] — LLM Wiki의 Wiki/Raw Sources/Queries를 로컬에서 검색하는 markdown 검색 엔진
- [[TMU Global Leadership Program]] — 2026년 TMU 영어 몰입·SDG 프로그램 참여 기록과 증빙·기여 표현 경계
- [[FPT Vietnam Global Big Data AI Program]] — 다낭 FPT에서 다국적 팀을 이끌고 금융·반도체 위험 GraphRAG을 진행한 4주 PBL 기록
- [[GNU Buddy]] — 2026-1학기 외국인 유학생의 학업·생활·문화 적응을 지원한 44.23시간 활동
- [[계약랩]] — ROS 2 드론 환경, 자율착륙 판단 구조, 협업·특허 비교 과업의 사용자 작성 프로젝트 기록
- [[2026 넥토리얼 지원]] — 2026 넥토리얼 서류 합격, AI면접 응시 완료, 결과 대기와 후속 학습 기록

### Guides

> How-to, 튜토리얼, 실전 가이드

- [[Obsidian Tooling for LLM Wiki]] — Web Clipper, Dataview, qmd 등 실용 도구 가이드
- [[Web Clipper to Inbox Workflow]] — Web Clipper capture에서 purpose-gated ingest까지의 실전 절차
- [[Citation Manager Integration for LLM Wiki]] — Zotero/Bookends 서지정보와 Raw Source/Wiki를 연결하기 위한 가이드 stub
- [[개발자 커리어로 경제적 자유에 가까워지기]] — 개발자 취업과 고소득 커리어를 경제적 자유의 1순위 수단으로 정리한 가이드
- [[LLM Wiki Token Optimization Strategies]] — LLM Wiki 운영에서 토큰을 절약하는 전략
- [[김규태 Career Narrative]] — 자기소개, 목표 도메인, 성장 과제, 면접용 내러티브 정리
- [[김규태 금융 시스템 개발자 취업 로드맵]] — 지방 국립대 소프트웨어공학과 4학년 관점의 금융권·핀테크 Java 주문 시스템 개발 취업 계획
- [[김규태 Java-Spring-AWS 금융 포트폴리오 기초 학습 트랙]] — 두 Spring Boot 교재의 질문·오개념·재시험을 금융 주문 프로젝트 전의 Java·Spring Boot·AWS 기초로 누적하는 중심 학습 축
- [[김규태 Leadership and Teaching Evidence]] — 실리콘밸리 대표, 멋쟁이사자처럼 부대표, 백엔드 세션, 해커톤 템플릿 증거
- [[개발자 롤모델을 GitHub에서 공부하는 법]] — 공개 commit·issue·PR·README·agent gate를 자신의 프로젝트 습관으로 전환하는 관찰 가이드
- [[김규태 Personal Operating Manual]] — 정체성, 동기, 일, 관계, 취향, 성장 위험을 통합한 사용설명서
- [[김규태 Work and Learning Operating Guide]] — 마감·알고리즘·반복 개선·유지보수를 위한 학습 운영 가이드
- [[김규태 Career Values and Success Vision]] — 직업 우선순위, 보상 기준, 원하는 환경과 성공상
- [[김규태 Relationship Values]] — 자율성, 신뢰, 애정 표현, 속도, 끌림, 동의에 관한 현재 가치
- [[김규태 AI Mentor Response Contract]] — AI가 근거 기반 멘토로 답하기 위한 개인화 계약
- [[김규태 개발 도메인 영어 성장 계획]] — 영어 몰입 경험을 기술 문서 읽기·영어 README·설명·협업 증거로 전환하는 계획
- [[UAV 정밀착륙 특허 검색 가이드]] — KIPRIS·Google Patents·PATENTSCOPE·Espacenet을 이용한 반복 가능한 특허 검색·검증 절차
- [[EvolvingTraceDB Neo4j 구축 및 검증 가이드]] — JavaParser 결과를 Neo4j 그래프로 적재하고 Browser에서 검증하는 재현 절차

### Maps (MOC)

> 주제별 Map of Content

- [[MOC-Knowledge Management]] — 지식 관리 개념, 패턴, 역사 종합
- [[MOC-LLM Wiki Guide]] — 이 볼트 사용 온보딩 가이드
- [[MOC-Portfolio]] — 취업 포트폴리오 Evidence Wiki 운영 허브
- [[경제적 자유는 나의 북극성이다]] — 개발자 커리어, 자본 레버리지, AI 자동화, 독서, 제품화를 경제적 자유로 연결하는 개인 MOC
- [[MOC-김규태 Self Knowledge]] — 자기이해와 AI 개인화 페이지를 연결하는 허브
- [[MOC-UAV 정밀착륙 연구]] — 영상·마커리스·의미 표식·제어·안전·특허를 연결하는 한 학기 정밀착륙 연구 중심축

---

## 🔎 Queries (Synthesized Answers)

> 질의 결과가 wiki 에 역피드백된 합성 페이지. [[Ingest-Query-Lint Cycle|Karpathy 원문 권장]]: "good answers can be filed back into the wiki as new pages."

- [[2026-07-07-Q-LLM-Wiki-vault-academic-value]] — LLM Wiki 볼트의 학술적 가치와 Zotero/Bookends 인용 연동 방향
- [[2026-07-14-Q-sales-psychology-book-recommendations]] — 세일즈와 심리학을 상위 25% 보조 능력으로 쌓기 위한 책 추천 경로
- [[2026-07-14-Q-how-to-read-sales-psychology-books]] — 세일즈와 심리학 책을 행동 실험으로 바꾸는 독서 방법
- [[2026-07-14-Q-yohan-koo-llm-wiki-usage-insights]] — 구요한 대표의 Obsidian LLM Wiki 사용법, 팁, 강의 인사이트 정리
- [[2026-08-04-Q-korean-developer-role-model-github-study-map]] — 한국 개발자 롤모델의 agent, commit, PR·issue, README·문서, 유지보수 패턴과 8주 적용 계획
- [[2026-07-16-Q-how-to-use-llm-wiki-well]] — LLM Wiki를 취업 포트폴리오, 프로젝트 증거, 학습, Codex 워크플로 산출물 생성 시스템으로 활용하는 방법
- [[2026-07-16-Q-llm-wiki-sharing-demo-strategy]] — LLM Wiki와 Obsidian 지식 그래프를 GitHub README, 배포 사이트, 시연 영상으로 공유하는 전략
- [[2026-07-16-Q-obsidian-graph-demo-script]] — Obsidian graph 녹화, Web Clipper ingest, Query, explored 검토까지 보여주는 LLM Wiki 데모 시나리오
- [[2026-07-16-Q-index-rag-agent-read-write-schema-engineering]] — index.md 작동 방식, RAG와 LLM Wiki의 상호보완, agent 읽기/쓰기와 schema engineering의 의미
- [[2026-07-16-Q-personal-context-knowledge-compounding-query-feedback]] — 개인 맞춤형 LLM 맥락층, 지식 복리, Query result의 Graph View 반영과 Wiki 승격 기준
- [[2026-07-16-Q-coding-test-ai-era-problem-solving]] — 코딩테스트가 AI 시대에 문제해결력, 컴퓨팅 사고력, 검증 능력, 비-AI 기본기 증거로 갖는 의미
- [[2026-07-16-Q-ai-assisted-coding-test-learning-loop]] — 코딩테스트 풀이 중 막힘, 디버깅, 엣지케이스 실패 상황에서 AI를 학습 보조로 쓰는 루프
- [[2026-07-20-Q-shin-jinseo-katago-opponent-model-strategy]] — 카타고의 상대 인식, 인간 오류 유도 전략, 블루스팟의 해석
- [[2026-08-31-Q-pureundeungdae-scholarship-fit]] — 학업·소득구간·AI/데이터 프로젝트를 반영한 2026년 2학기 푸른등대 장학금 적합도
- [[2026-08-31-Q-nice-scholarship-essay-evidence-map]] — NICE 장학금 자기소개서의 문항별 소재·평가기준·증빙 공백 지도
- [[2026-09-04-Q-finance-backend-ai-era-job-preparation]] — AI 시대 금융권·핀테크 Java 백엔드 취업을 위한 책, 자격증, 프로젝트, 코딩테스트, 지원 전략과 1년 실행 계획
- [[2026-09-05-Q-ai-era-developer-job-readiness-priority]] — AI 시대 금융권·핀테크 개발자 취업을 위한 Java·SQL·프로젝트·검증 역량의 현실적인 학습 우선순위
- [[2026-09-05-Q-world-literature-for-love-career-and-city]] — 그리움, 진로 선택, 연애의 외로움, 서울 생활에 대한 바람을 위한 세계문학 네 권
- [[2026-09-06-Q-output-first-personal-reading-priority]] — 보유한 구판 스프링 책의 현대화 실습, Java 프로젝트 output, 정서 회복을 위한 개인화 구매·독서 우선순위
- [[2026-09-06-Q-personal-self-help-reading-priority]] — 진로 실험, 조급함 완화, output 중심 학습과 관계 대화를 위한 자기계발서 우선순위
- [[2026-09-09-Q-kb-securities-java-backend-starting-plan]] — Java·SQL 시작 단계에서 금융 주문 MVP와 설명 가능한 포트폴리오를 만드는 첫 8주 실행안
- [[2026-08-25-Q-recent-ai-era-essential-books]] — 공동지능 이후 AI 판별력·산업 권력·반도체 인프라를 보완하는 최근 명저 독서 경로
- [[2026-08-29-Q-vault-audit]] — 70개 전 페이지 검증 후 eligibility, consistency, confirmability 최종 감사와 조건부 재검증 큐
- [[2026-09-10-Q-ai-hint-deep-problem-focus]] — AI를 정답 지름길이 아닌 단계별 힌트로 제한해 깊은 문제 몰입과 재풀이 능력을 훈련하는 2주 실험
- [[2026-09-11-Q-Nexon-Tutorial-AI-Interview-Preparation]] — 2026 신규 넥토리얼 AI면접의 답변 구조, 예상 질문군, 장비 점검표
- [[2026-09-11-Q-Nexon-Tutorial-AI-Interview-Answer-Strategy]] — 넥슨태그·제출 자료·자가답변을 대조한 문항별 진단, 오개념 교정, 학습 우선순위
- [[2026-09-11-Q-Nexon-Tutorial-Motivation-and-Game-Answers]] — 넥슨 게임의 개인적 기억, 지원동기, 게임 포트폴리오 부재와 AI 학습 사례를 연결한 면접 답변
- [[2026-09-11-Q-AI-Assessment-Problem-Solving-Template]] — 정의·정렬·분해·선택·실행·검증·제출을 위한 AI 평가 참고 템플릿
- [[2026-09-12-Q-Nexon-Tutorial-Mock-Interview-Session-1]] — 동시성·멱등성·stack/heap 재시험과 1분 자기소개 평가를 포함한 넥토리얼 모의면접 1차 기록
- [[2026-09-12-Q-Nexon-Tutorial-AI-Interview-Retrospective]] — 실제 AI면접 복기 기반 문항별 교정, C++·자료구조·공간 탐색 학습 우선순위
- [[2026-09-13-Q-bank-backend-entry-readiness-gap]] — 은행권 백엔드 인턴·신입 채용선, 공개 합격 사례와 김규태의 핵심 역량 격차 진단
- [[2026-09-13-Q-java-bank-transfer-ledger-portfolio-design]] — Java·Spring Boot로 동시성·멱등성·원장 정합성을 증명하는 은행 백엔드 대표 프로젝트 설계
- [[2026-09-14-Q-modoo-startup-second-cuee-application-draft]] — CUEE 모두의 창업 2차 지원을 위한 증거 경계형 문항 초안, 실행 일정과 이미지 구성
- [[2026-09-01-Q-software-engineering-semester-project-selection]] — 소프트웨어개발론의 12주 범위에 맞춘 무인기 추적성과 Upbit 투자 시스템 후보 비교
- [[2026-09-01-Q-emerging-traceability-technology-selection]] — 최신 논문·오픈소스와 12주 제약을 반영한 경량 GraphRAG형 추적 기술 선정
- [[2026-09-01-Q-upbit-financial-decision-traceability-project]] — 사용자 의도부터 Upbit test order까지 재현하는 금융 AI Decision Receipt 프로젝트
- [[2026-09-01-Q-team-meeting-two-project-proposals]] — Agentic UAV Digital Thread와 Upbit Decision Provenance를 같은 기준으로 비교한 팀 회의용 2안
- [[2026-09-01-Q-whybuy-agentic-finance-technology-selection]] — Google AP2의 signed mandate를 투자 권한에 변형한 WhyBuy Agentic Finance 기술안
- [[2026-09-02-Q-semester-project-concrete-team-brief]] — WhyBuy와 TracePilot을 사용자 시나리오·연구 질문·12주 범위·팀 설명문으로 구체화한 회의 자료
- [[2026-09-02-Q-traceability-project-reselection-without-domain-data]] — 외부 도메인 데이터 없이 AI 작업·코드·테스트·빌드를 연결하는 TraceForge와 C2PA 대안 재선정
- [[2026-09-02-Q-upbit-order-traceability-project-redesign]] — Upbit 호가·체결 기반 paper OMS에서 주문 장애를 추적·재현하고 MCP agent가 근거로 진단하는 OrderScope AI
- [[2026-09-02-Q-three-person-upbit-drone-traceability-proposals]] — 3인 팀의 OrderScope 금융 주문 추적과 FlightProof 무인기 실행형 안전 증거 추적을 동일 기준으로 비교한 최종 회의안
- [[2026-09-02-Q-graphify-fit-for-traceability-project]] — Graphify를 PX4 요구사항·ULog용 domain extension과 선택적 재시험에 적용한 FlightGraph 적합성·범위·baseline 판단
- [[2026-09-03-Q-developer-job-preparation-starting-plan]] — Java·SQL·코딩테스트·주문 API를 병렬로 시작하는 김규태의 첫 4주 취업 공부 계획
- [[2026-09-03-Q-from-coding-tests-to-software-development]] — 콘솔 주문 프로그램에서 API·DB·실패 처리로 확장하며 실제 개발 전체 주기를 익히는 방법
- [[2026-09-03-Q-GNU-개척리더스-창업서포터즈-지원서-초안]] — CUEE 창업 경험과 창업지원단 활동을 연결한 개척리더스 창업서포터즈 지원서 초안
- [[2026-09-01-Q-nice-scholarship-five-question-coherence-audit]] — NICE 자기소개서 1~5번의 평가기준 충족도·중복·일관성·증거 공백 감사
- [[2026-09-01-Q-nice-scholarship-essay-draft-v1]] — 증거 경계와 문항별 글자 수를 반영한 NICE 자기소개서 5문항 1차 초안
- [[2026-09-08-Q-nice-scholarship-selection-benchmark]] — 공식 1·2차 평가 구조와 성적·소득·자소서·스펙의 현실적 경쟁력 기준
- [[2026-09-09-Q-nice-scholarship-essay-draft-v2]] — 제출 전 점검 완료: 학기 평점, 52개 중 72시간 완료 50개, 예상 예산과 모의 주문 실험을 명시한 NICE 자기소개서
- [[2026-09-09-Q-nice-2025-winner-pattern-research]] — 공개 범위를 구분한 NICE 1기 합격자 특징·자소서 평가축 조사와 질문→축적→실험 연결성 진단
- [[2026-09-09-Q-nice-no-certification-selection-readiness-audit]] — 데이터 분석 자격증·관련 수상 없이 NICE 최종 선발을 노리는 현재 5문항의 모의점수·증거 취약점·수정 우선순위
- [[2026-09-10-Q-nice-five-criteria-readiness-rescore]] — 수정된 NICE 자기소개서를 다섯 선발 기준으로 재채점한 88점 평가와 직접 분석 증거 중심의 보완 순서
- [[2026-09-10-Q-threads-followup-experiment-and-nice-evidence-needs]] — Threads 1.01%→0.37% 재현, 6쌍 후속 형식 실험 준비와 NICE 예산·시간축에 필요한 정보
- [[2026-09-03-Q-gnu-scholarship-internship-opportunity-map]] — 경상국립대 재학생이 현재 노릴 장학금·지원금·현장실습·기술 활동 우선순위
- [[2026-09-03-Q-the-jaram-and-2027-spring-internship-plan]] — 기존 활동의 The(더)자람 포인트 매핑과 2027년 1학기 개발 인턴 준비 일정
- [[2026-09-07-Q-nextorial-game-programming-application-draft]] — 공식 지원요건 대조, A안 문항별 소재 재배치와 기술·동기·졸업요건 공백
- [[2026-09-07-Q-nextorial-self-introduction-final]] — 거래 검증 자동화 목표·매몰비용과 솔직한 피드백·간결한 개발 문서화 원칙을 반영한 네 문항 최종본
- [[2026-09-08-Q-precision-landing-patent-fit-and-team-loop]] — 5번 의미 아이콘 기반 최소 장비 기준선과 재완·관호·규태 반복 실험 구조
- [[2026-09-08-Q-linkedin-silicon-valley-student-strategy]] — 한국 학부생이 검색 적합성·프로젝트 증거·신뢰를 중심으로 실리콘밸리 기회를 준비하는 LinkedIn 전략
- [[2026-09-14-Q-korea-backend-industry-finance-sector-comparison]] — 한국 백엔드 언어 범용성과 금융 세부 업권의 채용·보상·문화·워라밸 경향 비교
- [[2026-09-14-Q-korea-non-finance-backend-employer-comparison]] — 금융 외 일반기업 백엔드 유형과 보상·워라밸·개발환경·회사 선택 기준 비교
- [[2026-09-14-Q-korea-financial-java-employer-comparison]] — 주요 은행·인터넷은행·증권사의 Java 신입 채용 입구, 보상·워라밸 경향, 현직자 평가 신호와 근무 거점 비교
- [[2026-09-18-Q-current-scholarship-global-hackathon-opportunity-map]] — 소득 9구간을 반영한 현재 장학금·해외·금융/개발·해커톤·일경험 후보와 지원 순서
- [[2026-09-21-Q-GNU-UNLV-application-draft-v1]] — FPT GraphRAG·Threads workflow·CUEE 피벗과 수상·해외 수학 증거를 연결한 GNU-UNLV 세 문항 1차 초안
- [[2026-09-21-Q-GNU-UNLV-application-draft-v2]] — Docker·CUEE를 문제해결 철학으로 연결하고 Threads 10건 검증·고령 사용자 10명 관찰·네 단계 학업계획을 반영한 2차 초안
- [[2026-09-21-Q-GNU-UNLV-selection-competitiveness-audit]] — 초안을 수정하지 않고 학적·이중 접수·사용자 관찰·AI 검증·영어 발표·단일 증빙 PDF의 보강 우선순위를 정리한 선발 준비 진단
- [[2026-09-21-Q-GNU-UNLV-AI-startup-evidence-PDF-checklist]] — 선택 제출용 AI·창업 활동실적 PDF의 7쪽 구성, 확보 자료, 추가로 필요한 증빙을 정리한 제작 체크리스트

---

## 📥 Recent Ingests

| Date | Source | Pages Touched |
|------|--------|---------------|
| 2026-09-21 | [[2026-09-21-GNU-FPT-Vietnam-GraphRAG-Program-Record]] | [[FPT Vietnam Global Big Data AI Program]], [[김규태]], [[MOC-Portfolio]] |
| 2026-09-21 | [[2026-09-21-Kim-Gyutae-GNU-Buddy-2026-1-Record]] | [[GNU Buddy]], [[김규태]], [[MOC-Portfolio]] |
| 2026-09-12 | [[2026-09-12-Kim-Gyutae-Java-Spring-AWS-Study-Declaration]] | [[김규태 Java-Spring-AWS 금융 포트폴리오 기초 학습 트랙]], [[김규태 금융 시스템 개발자 취업 로드맵]], [[MOC-Portfolio]], [[Core Context]] |
| 2026-09-12 | [[2026-09-12-Nexon-Tutorial-AI-Interview-Recollection]] | [[2026 넥토리얼 지원]], [[2026-09-12-Q-Nexon-Tutorial-AI-Interview-Retrospective]] |
| 2026-09-12 | [[2026-09-11-Gemini-Lauren-Tan-Agent-Lecture-Chat]] | Raw Source only; claims remain unverified |
| 2026-09-11 | [[2026-09-11-Nexon-Tutorial-AI-Interview-Preparation-Bundle]] | [[2026 넥토리얼 지원]], [[MOC-Portfolio]], [[2026-09-11-Q-Nexon-Tutorial-AI-Interview-Preparation]] |
| 2026-09-10 | [[2026-09-02-to-09-Kim-Gyutae-Contract-Lab-Work-Notes]] | [[계약랩]], [[MOC-Portfolio]] |
| 2026-09-09 | [[2026-09-09-Codex-KB-Securities-Java-Backend-Career-Conversation]] | 1 guide + 1 MOC + 1 query |
| 2026-09-08 | [[2026-09-08-EvolvingTraceDB-Neo4j-local-build-record]] | [[EvolvingTraceDB Neo4j 구축 및 검증 가이드]], [[Graduation-elasticsearch]] |
| 2026-09-08 | [[2026-09-08-UAV-precision-landing-patent-search-pilot]] | [[MOC-UAV 정밀착륙 연구]], [[UAV 정밀착륙 특허 검색 가이드]] |
| 2026-08-24 | [[2026-08-17-Gemini-Quant-Research-Conversation]] + [[2026-08-24-Kim-Gyutae-TMU-SDG-Portfolio-Record]] + [[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]] | 14 pages + TMU PDF schedule |
| 2026-07-26 | [[2026-07-26-Kim-Gyutae-AI-Era-Developer-Reflection]] + 11 Clippings | 14 pages |
| 2026-07-23 | [[2026-07-23-Kim-Gyutae-Self-Understanding-Interview-v1]] | 15 pages |
| 2026-07-23 | [[2026-07-23-Kim-Gyutae-Romantic-Self-Reflection-v1]] | 5 pages |
| 2026-07-23 | [[2026-07-23-Kim-Gyutae-Personal-Operating-Manual-v1]] | 7 pages |
| 2026-07-16 | [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]] | 7 pages |
| 2026-07-13 | [[2026-07-13-YouTube-Shorts-몸값-높이는-독서법]] | 3 pages |
| 2026-07-12 | [[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]] + 13 YouTube transcripts | 8 pages |
| 2026-07-12 | [[2026-07-12-Velog-Leadership-Product-Hackathon-Bundle]] | 4 pages |
| 2026-07-12 | [[2026-07-12-Kim-Gyutae-Leadership-Product-Context-v2]] | 6 pages |
| 2026-07-11 | [[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]] | 7 pages |
| 2026-07-07 | [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]] | 13 pages |
| 2026-04-12 | [[2026-04-12-Karpathy-LLM-Wiki\|Karpathy LLM Wiki Gist]] | 10 pages (예시) |

→ [[log]] 참조

---

## 📦 Shared Project Proposals

- [Rotor Engineering Knowledge Agent 제안서](Propeller%20Evidence%20Agent%201.md) — 전문가 검토 절차·과거 증거 재사용·승인형 프로펠러 해석 데모를 통합하는 팀 기준안
- [Rotor Engineering Knowledge Agent PRD](70.%20Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller%20Evidence%20Agent%20PRD.md) — 자연어 요청부터 시각적 점검·승인형 Fluent 실행·근거 보고서까지의 MVP 요구사항

## 📝 Application Drafts

- [GNU 유학생 튜터링 신청서 문안](70.%20Outputs/2026-09-23-GNU-International-Tutoring/application-plan.md) — 지원동기, 활동목표, CLIL 기반 10~12월 진단·개선·재측정 계획

## 🔗 Quick Links

- [[log]] — 전체 변경 이력
- [[CODEX]] — Schema (볼트 규칙서)
- [[Core Context]] — 사용자 맥락 (채워서 사용)

---

## 🚀 시작하기

1. [[Core Context]] 에 본인 정체성·목적·철학 채우기
2. Obsidian Web Clipper 로 관심 소스를 `00. Inbox/` 에 저장
3. `/ingest` — 목적 질문에 답하면 Raw Sources + Wiki 페이지 자동 생성
4. `/query` — 쌓인 Wiki 를 바탕으로 질문 답변
5. `/lint` — 주기적으로 건강도 체크

자세한 가이드는 [[LLM-Wiki-Starter-Kit]] 참조.
