---
type: log
aliases:
  - Change Log
  - Wiki Log
  - Ingest Log
description: Chronological log of all wiki operations — ingests, queries, lint fixes, and structural changes. Append-only; entries use `## [YYYY-MM-DD] operation | title` prefix for grep-based parsing.
author:
  - "[[김규태]]"
date created: 2026-07-07
date modified: 2026-09-04
tags:
  - system
  - log
status: active
---

# 📝 LLM Wiki — Change Log

> 모든 wiki 변경사항을 시간순으로 기록합니다. **Append-only** — 기존 항목을 수정하지 마세요.
>
> **Entry format (Karpathy-style)**: `## [YYYY-MM-DD] operation | title`
>
> **Quick scan**:
>
> ```bash
> grep "^## \[" log.md | tail -10   # 최근 10개 operation
> grep "^## \[.*\] ingest" log.md   # ingest만 필터
> ```
>
> **Operations**: `ingest`, `update`, `create`, `lint`, `query`, `restructure`, `cleanup`

---

## [2026-04-12] ingest | Karpathy LLM Wiki Gist (example)

- Source: [[2026-04-12-Karpathy-LLM-Wiki]]
- Origin: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Raw Source 저장: `10. Raw Sources/11. Articles/`
- Wiki 페이지 생성 (10):
	- Concepts (4): [[LLM Wiki Pattern]], [[RAG vs Compiled Wiki]], [[3-Layer Architecture]], [[Ingest-Query-Lint Cycle]]
	- Entities (3): [[Andrej Karpathy]], [[Vannevar Bush]], [[Memex]]
	- Guides (1): [[Obsidian Tooling for LLM Wiki]]
	- Maps (2): [[MOC-Knowledge Management]], [[MOC-LLM Wiki Guide]]
- **예시 ingest** — 이 볼트가 어떻게 성장하는지 보여주기 위한 샘플. 본인 소스 ingest 시작 시 이 entry 아래에 append.

## [2026-07-07] create | Vault initialized

- Cloned from [cmds-llm-wiki template](https://github.com/johnfkoo951/cmds-llm-wiki)
- Core Context 채움 완료 (§1 정체성, §2 재활용 축, ...)
- 첫 ingest 진행 예정

## [2026-07-07] ingest | 에이전트를 위한 지식 베이스 : LLM Wiki 활용

- Source: [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]
- Origin: https://www.youtube.com/watch?v=MRTQwBFURJs&t=1317s
- Collection purpose: 학술/CMDS 시스템 — 내가 앞으로 LLM Wiki를 공부하기 위한 학습 자료
- Raw Source 저장: `10. Raw Sources/11. Articles/`
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 생성 (7):
	- Concepts (4): [[LLM Wiki as Learning Base]], [[Mothership-Satellite Vault Pattern]], [[Agent-Readable Metadata]], [[Human-AI Knowledge Boundary]]
	- Entities (2): source-specific lecture entities later removed during local owner cleanup
	- Guides (1): [[Web Clipper to Inbox Workflow]]
- Wiki 페이지 업데이트 (6):
	- Concepts (3): [[LLM Wiki Pattern]], [[3-Layer Architecture]], [[Ingest-Query-Lint Cycle]]
	- Guides (1): [[Obsidian Tooling for LLM Wiki]]
	- Maps (2): [[MOC-Knowledge Management]], [[MOC-LLM Wiki Guide]]
	- Index (1): [[index]]

## [2026-07-07] query | LLM Wiki 볼트의 학술적 가치

- Query: LLM Wiki 볼트의 학술적 가치와 Zotero/Bookends 서지정보 인용 연동 가능성
- Saved: [[2026-07-07-Q-LLM-Wiki-vault-academic-value]]
- Source pages: [[LLM Wiki Pattern]], [[RAG vs Compiled Wiki]], [[3-Layer Architecture]], [[Ingest-Query-Lint Cycle]], [[LLM Wiki as Learning Base]], [[Agent-Readable Metadata]], [[Human-AI Knowledge Boundary]], [[Idea Generation Pipeline]], [[Track Classification and Research Gap Detection]], [[Obsidian Tooling for LLM Wiki]]
- Durable gap captured: [[Citation Manager Integration for LLM Wiki]] guide stub created
- Reuse axis: PhD / 학술 / CMDS 시스템

## [2026-07-07] update | Portfolio Evidence Wiki setup

- Updated: [[Core Context]]
- Created: [[MOC-Portfolio]]
- Purpose: 이 vault를 취업 포트폴리오 관리용 Evidence Wiki로 운영하기 위한 재활용 축, 프로젝트 spine, ingest/query 기준 정렬
- Portfolio spine: `financial-order-latency-lab -> cuee -> harness`
- Reuse axis: 취업/포트폴리오

## [2026-07-10] update | Local setup placeholders filled

- Updated: [[Core Context]], [[AGENTS]], [[CODEX]], [[index]], settings templates
- Replaced author placeholder with `김규태`
- Replaced local vault path placeholders with `C:\Users\kym70\OneDrive\Desktop\cmds-llm-wiki-work\cmds-llm-wiki`
- Copied qmd config to `C:\Users\kym70\.config\qmd\index.yml`
- Mode: A standalone — mothership placeholders intentionally left only in optional Mode B documentation/examples

## [2026-07-10] cleanup | Owner identity and inherited entities corrected

- Restored owner display name to [[김규태]]
- Removed inherited lecture/source entity pages from active Wiki
- Created [[김규태]] owner entity draft
- Updated [[index]] and [[MOC-Knowledge Management]] to point to [[김규태]]
- Left raw source transcripts intact unless a separate purge is requested

## [2026-07-10] update | 김규태 취업 포트폴리오 맥락 고도화

- Updated: [[Core Context]], [[김규태]], [[MOC-Portfolio]]
- Added current profile: 개발자 취업준비생, 대학교 3학년, 학부연구생, 경남 진주시 거주
- Added public profiles: GitHub, Velog, LinkedIn, Instagram
- Clarified portfolio purpose: 개발자 취업
- Expanded project spine:
	- `financial-order-latency-lab`: 데이터베이스 수업 프로젝트, 설계·성능 개발
	- `cuee`: 경남권 창업동아리 대상작, 노인 모빌리티 예약 길잡이 앱
	- `harness`: 커서맛피아님 harness를 참고해 앱 개발용으로 개인화한 Codex workflow
- Added positioning tone: 취업준비생 입장에서 열정과 성장가능성이 드러나되, 설계·성능·개발·팀 리딩 근거를 우선

## [2026-07-10] update | GitHub 기반 백엔드 포트폴리오 재정렬

- Updated: [[Core Context]], [[김규태]], [[MOC-Portfolio]], [[index]]
- Created project pages: [[financial-order-latency-lab]], [[Graduation-elasticsearch]], [[cuee]], [[harness]]
- Source reviewed: GitHub profile `gyutaetae` public repositories and README files
- Repositioned target role: 백엔드 개발자 취업, 장기적으로 풀스택 개발자로 성장
- Clarified primary language: Python
- GitHub-based stack: Python, Java, Kotlin, TypeScript/React, JavaScript, C, Shell/PowerShell, Dockerfile, PLpgSQL
- Added `Graduation-elasticsearch` as research/backend evidence between `financial-order-latency-lab` and `cuee`

## [2026-07-11] ingest | 김규태 Personal Raw Context v1

- Source: [[2026-07-11-Kim-Gyutae-Personal-Raw-Context-v1]]
- Origin: User-provided raw terminal/chat text in Codex session
- Collection purpose: 나에 대한 장기 컨텍스트를 축적해 이력서, 면접, 포트폴리오, 블로그, 프로젝트 설명에 반복 재사용하기 위한 개인 원본 프로필
- Raw Source 저장: `10. Raw Sources/15. Clippings/`
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 생성 (2):
	- Concepts (1): [[AI-Augmented Developer Positioning]]
	- Guides (1): [[김규태 Career Narrative]]
- Wiki 페이지 업데이트 (5):
	- [[Core Context]]
	- [[김규태]]
	- [[MOC-Portfolio]]
	- [[financial-order-latency-lab]]
	- [[harness]]
- Key context captured:
	- 목표 직무는 아직 단일 확정이 아니며 백엔드 / 금융 / 드론 / 반도체 도메인 탐색 중
	- 경상국립대학교 소프트웨어공학과 3학년, SEALAB 학부연구생
	- AI 의존 개발자가 아니라 AI를 개발 역량의 증폭기로 활용하는 개발자로 포지셔닝
	- `financial-order-latency-lab`의 시작 동기: 운영체제 수업 CPU latency와 금융 주문 처리 관심
	- Codex 기반 Threads 자동 리서치/업로드 workflow와 팔로워 약 400명 성과는 추가 증빙 필요
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 에세이/블로그

## [2026-07-12] ingest | 김규태 Leadership Product Context v2

- Source: [[2026-07-12-Kim-Gyutae-Leadership-Product-Context-v2]]
- Origin: User-provided raw chat text in Codex session, plus public Velog/GitHub links
- Collection purpose: 취업/포트폴리오 — 리더십, 교육, 창업/제품 문제정의, 해커톤 템플릿, 향후 보강할 증거를 원본 맥락으로 보존해 이력서와 면접 답변에 재사용
- Raw Source 저장: `10. Raw Sources/15. Clippings/`
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 생성 (1):
	- Guides (1): [[김규태 Leadership and Teaching Evidence]]
- Wiki 페이지 업데이트 (5):
	- [[Core Context]]
	- [[김규태]]
	- [[cuee]]
	- [[MOC-Portfolio]]
	- [[index]]
- Key context captured:
	- `cuee`는 `배우담`의 후속 방향이며, 학습 과정 자체가 고통스럽다는 문제를 보고 현재 화면의 다음 버튼을 마스킹/안내하는 접근성 오버레이로 전환
	- `cuee` 팀 규모는 5명: 디자이너 2명, 기획 2명, 김규태 1명(개발자/팀장)
	- 김규태는 2026년 `실리콘밸리` 취업동아리 대표(20명: 학부생 15명, 교수 5명)
	- 김규태는 2026년 경상국립대학교 멋쟁이사자처럼 14기 부대표
	- GNU 해커톤 템플릿은 다음 달 대회에서 사용할 예정이며, 실제 결과/피드백은 추후 보강
	- 회의록, 예산/지원금 자료, 책 수요조사, 교수 피드백, 백엔드 세션 자료는 추후 Raw Source로 보강 예정
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 강의/수업/교육, 제품/창업

## [2026-07-12] ingest | Velog Leadership Product Hackathon Bundle

- Source: [[2026-07-12-Velog-Leadership-Product-Hackathon-Bundle]]
- Origin: Public Velog posts and GitHub README
- Collection purpose: 취업/포트폴리오 — 리더십, 제품 문제정의, 해커톤 준비, 백엔드 교육, 실제 고객 문제 해결 경험을 원문 증거로 보존해 이력서와 면접 답변에 재사용
- Raw Source 저장: `10. Raw Sources/15. Clippings/`
- Included sources:
	- `what is leadership?`
	- `실리콘밸리 1주차`
	- `실리콘밸리2`
	- `week2. silicon valley`
	- `멋쟁이사자 아이디어톤(1)`
	- `배우담 개발일지1`
	- `크몽 외주 일지`
	- `GNU_hackathon_templete` README
- Wiki 페이지 업데이트 (4):
	- [[김규태 Leadership and Teaching Evidence]]
	- [[cuee]]
	- [[MOC-Portfolio]]
	- [[index]]
- Reuse axis: 취업/포트폴리오, 강의/수업/교육, 제품/창업, 프로젝트 증거

## [2026-07-12] maintenance | Status count and wiki metadata coverage

- Updated status command docs to exclude `.gitkeep` placeholders from Inbox pending counts
- Added `explored: false` and `verificationStatus: unverified` to 17 legacy Wiki/MOC pages missing Exploration Gate and verification fields
- Updated `date modified` on touched Wiki pages to `2026-07-12`
- Result:
	- Inbox pending count now reports 0 real files when only `.gitkeep` placeholders exist
	- `explored` coverage: 31/31 Wiki pages
	- `verificationStatus` coverage: 31/31 Wiki pages
- Note: verification values were set conservatively to `unverified`; run `/verify` for claim-level confirmation

## [2026-07-12] context | Economic freedom, leverage, and reading axes

- Source: user-provided clarification in Codex session
- Updated: [[Core Context]]
- Purpose: 영상 transcript ingest 전에 취업 포트폴리오 증거와 개인 삶의 운영 지식을 분리하고, 경제적 자유/FIRE/레버리지 및 독서/책/학습 축을 쿼리 라우팅용으로 추가
- Key context captured:
	- 경제적 자유는 단기 은퇴 계획이 아니라 완전한 자유를 향한 북극성
	- 1순위 수단은 개발자 취업과 고연봉 커리어, 2순위는 투자와 자산관리
	- 자본 레버리지를 가장 큰 레버리지로 보며, 현재 약 7천만 원, 1억 원을 첫 임계점으로 인식
	- 투자 운영 가설은 반도체/기술주 2배 레버리지 ETF를 디벨롭몽의 웅덩이 매수법으로 장기 분할매수하는 전략
	- 현금 20% 유지, 생활비 대출은 내년까지 추가 400만 원 범위로 제한
	- 암호화폐는 고위험 성장자산으로 보며 전체 자산의 약 5%를 차지하고, 현재 기록 기준 비트코인 약 215만 원과 이더리움 약 113만 원을 보유
	- Threads는 Codex 자동화 시스템으로 만든 콘텐츠/브랜드 레버리지 사례이며 반복 운영까지 포함
	- `cuee`는 U300 전국 400개 팀 선정, 경남권 창업동아리대회 대상, 교내 창업대회 최우수상 이력이 있으며 Android accessibility 권한 심사가 주요 blocker이고 제품화 경험으로 우선 설명
	- 상위 Wiki 제목 후보는 `경제적 자유는 나의 북극성이다`를 우선으로 둠
	- 최근 감명 깊게 읽은 책은 롭 무어 `레버리지`와 이선 몰릭 `공동지능`
- Reuse axis: 경제적 자유/FIRE/레버리지, 독서/책/학습, Codex 개발 워크플로, 제품/창업

## [2026-07-12] inbox | YouTube inspiration bundle user reflections

- Source: user-provided per-video reflections in Codex session
- Created Inbox note: [[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]]
- Purpose: 13개 YouTube transcript ingest 전에 영상별로 사용자가 가져가고 싶은 생각을 분리 보존해, 나중에 Raw Source/Wiki 컴파일 시 영상 요약보다 사용자 해석을 중심에 두기 위함
- Key context captured:
	- AI는 기존 업무 보조를 넘어 암 치료 같은 인간의 궁극적 문제 해결로 갈 수 있다는 관점
	- 지식도 복리처럼 쌓이며, 매일 공부해 점을 만들고 나중에 연결하려는 독서 태도
	- 첫 1억 이전의 생활습관, 소비습관, 투자습관이 이후 자산 증가의 기초가 된다는 생각
	- FIRE 가능성을 염두에 두면 오히려 일을 더 잘할 수 있다는 관점
	- 바이브마피아 하네스 레포를 Codex 맞춤형으로 변형한 것이 `harness`이고, 그 하네스로 만든 것이 `cuee`
	- 멀티 에이전트 workflow에서는 직책 부여, 작은 단위 작업 분해, 추상화가 중요하다는 생각
	- 논픽션 중심 독서에서 픽션까지 섞어 읽어야 한다는 독서 균형 과제
	- 아직 0에서 1로 만든 것은 없지만, 개발 커리어와 제품이 세상에 알려지고 실제 사용되는 경험을 하고 싶다는 목표
	- `경제적 자유는 나의 북극성이다`를 이번 묶음의 상위 Wiki 페이지로 확정
	- 샘 올트먼 1인 유니콘 영상은 미래 1인 제품 가능성으로 연결
	- 픽션 독서 후보는 `은하수를 여행하는 히치하이커를 위한 안내서`, `이방인`, `변신`
	- `cuee`는 아직 0에서 1로 만든 경험이 아니라 0 to 1 후보 또는 초기 제품화 경험으로 기록
- Reuse axis: 경제적 자유/FIRE/레버리지, 독서/책/학습, Codex 개발 워크플로, 제품/창업, 취업/포트폴리오

## [2026-07-13] ingest | YouTube Shorts 몸값 높이는 독서법

- Source: [[2026-07-13-YouTube-Shorts-몸값-높이는-독서법]]
- Origin: `00. Inbox/01. Articles/몸값 높이는 독서법.md`
- Collection purpose: 독서와 학습을 취업 포트폴리오보다 경제적 자유/FIRE/레버리지 축에 더 강하게 연결하기 위해 수집. 사용자는 영상의 메시지에 동의하며, 자본주의 사회에서 능력과 시장가치를 키우는 태도를 장기 자유의 기반으로 기록하려고 함
- Raw Source 저장:
	- `10. Raw Sources/11. Articles/2026-07-13-YouTube-Shorts-몸값-높이는-독서법.md`
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 업데이트 (3):
	- [[경제적 자유는 나의 북극성이다]]
	- [[독서는 판단력과 자산관리의 기반이다]]
	- [[레버리지를 당하지 않고 사용하는 삶]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 이 쇼츠는 독서를 단순 취미나 취업 스펙이 아니라, 능력과 시장가치를 키워 선택권을 넓히는 수단으로 해석한다
	- 사용자는 개발자 취업 축보다 경제적 자유/FIRE/레버리지 축에 더 강하게 연결하기를 원했다
- Verification boundary:
	- 영상의 시장/능력주의 주장은 외부 관점이므로 검증된 사회과학 명제가 아니라 개인 운영 관점으로 보존한다
- Reuse axis: 경제적 자유/FIRE/레버리지, 독서/책/학습

## [2026-07-16] query | Index, RAG, agent read/write, and schema engineering

- Source query: 사용자가 LLM Wiki의 의미를 유지보수 비용 붕괴, 인간의 source 큐레이션/질문 역할, RAG와의 상호보완, agent 읽기/쓰기 능력, index.md routing, schema engineering 가능성 관점에서 정리해 달라고 요청
- Saved query result: [[2026-07-16-Q-index-rag-agent-read-write-schema-engineering]]
- Wiki 페이지 생성 (1):
	- [[Schema Engineering for LLM Wiki]]
- Primary sources:
	- [[LLM Wiki Pattern]]
	- [[RAG vs Compiled Wiki]]
	- [[3-Layer Architecture]]
	- [[Ingest-Query-Lint Cycle]]
	- [[qmd]]
	- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
- Index 업데이트:
	- [[index]]
	- [[MOC-Knowledge Management]]
- Key context captured:
	- `index.md`는 agent가 전체 본문을 읽기 전에 관련 페이지를 찾는 routing table로 작동한다.
	- RAG는 "넓게 찾기", LLM Wiki는 "깊게 축적하기"에 강하며 retrieval -> compilation -> reuse pipeline으로 상호보완할 수 있다.
	- agent의 읽기/쓰기 능력은 embedding/vector DB를 완전히 대체한다기보다, 반복 synthesis와 유지보수를 파일 시스템 안에 externalize해 많은 개인/소규모 지식 워크플로에서 복잡한 인프라 필요를 줄인다.
	- schema engineering은 장기적으로 agent가 일관되게 지식을 유지하도록 page type, metadata, 검증 경계, workflow를 설계하는 기술 영역으로 볼 수 있다.
- Quality gaps:
	- [[Schema Engineering for LLM Wiki]]는 현재 synthesis-only / unverified 페이지다.
	- [[qmd]]는 single-source 기반이라 공식 source ingest 후 verification 강화가 필요하다.
	- [[RAG vs Compiled Wiki]]의 contradiction callout은 아직 `/verify` 대상이다.
- Reuse axis: 독서/책/학습, Codex 개발 워크플로, 에세이/블로그, 취업/포트폴리오

## [2026-07-16] query | Personal context layer and query feedback loop

- Source query: 사용자가 LLM Wiki의 가장 큰 장점을 "나에 대한 고품질 정보를 LLM에게 제공하는 개인 맞춤형 맥락층"으로 보고, 지식 복리, Query result의 Graph View 반영, Query에서 새 Wiki 개념을 만들지 판단하는 기준을 요청
- Saved query result: [[2026-07-16-Q-personal-context-knowledge-compounding-query-feedback]]
- Wiki 페이지 생성 (1):
	- [[Personal Context Layer for LLM Wiki]]
- Wiki 페이지 업데이트:
	- [[LLM Wiki Pattern]]
	- [[Ingest-Query-Lint Cycle]]
	- [[Obsidian Tooling for LLM Wiki]]
	- [[김규태]]
	- [[MOC-Knowledge Management]]
	- [[MOC-LLM Wiki Guide]]
	- [[index]]
	- [[Core Context]]
- Primary sources:
	- [[Core Context]]
	- [[김규태]]
	- [[LLM Wiki Pattern]]
	- [[RAG vs Compiled Wiki]]
	- [[Ingest-Query-Lint Cycle]]
	- [[LLM Wiki as Learning Base]]
	- [[Human-AI Knowledge Boundary]]
	- [[Agent-Readable Metadata]]
	- [[Obsidian Tooling for LLM Wiki]]
	- [[Schema Engineering for LLM Wiki]]
- Key context captured:
	- LLM Wiki는 일반 지식 저장소가 아니라 개인 맞춤형 LLM을 위한 고품질 context layer로 볼 수 있다.
	- 지식 복리는 source -> ingest -> wiki -> query -> saved query -> durable concept promotion 루프에서 생긴다.
	- Query result는 `30. Queries/`에 저장되고 wikilink가 있으면 Obsidian Graph View의 노드와 edge로 나타날 수 있다.
	- 모든 Query가 새 Wiki 개념이 되는 것은 아니며, 여러 페이지를 연결하고 반복 사용 가능한 insight만 Wiki page로 승격한다.
- Quality gaps:
	- [[Personal Context Layer for LLM Wiki]]는 synthesis-only / unverified 개념이다.
	- Obsidian Graph View 표시 여부는 실제 필터 설정과 wikilink 수에 따라 달라진다.
	- [[Persistent Knowledge Base]], [[Progressive Disclosure Pattern]], [[Context Engineering]]은 아직 독립 Wiki page가 없는 보강 후보다.
- Reuse axis: Codex 개발 워크플로, 독서/책/학습, 에세이/블로그, 취업/포트폴리오

## [2026-07-16] ingest | WikiDocs LLM Wiki RAG를 넘어서

- Source: [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
- Origin: `00. Inbox/01. Articles/LLM Wiki RAG를 넘어서, LLM이 직접 지식을 쌓아가는 개인 위키 패턴.md`
- Collection purpose: 독서/책/학습 - LLM Wiki가 RAG와 어떻게 다른지 직접 이해하고, 내 LLM Wiki 운영·데모·포트폴리오 설명의 학습 기반으로 재사용하기 위해 수집
- Raw Source 저장:
	- `10. Raw Sources/11. Articles/2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서.md`
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 생성 (1):
	- [[qmd]]
- Wiki 페이지 업데이트 (6):
	- [[LLM Wiki Pattern]]
	- [[RAG vs Compiled Wiki]]
	- [[3-Layer Architecture]]
	- [[Ingest-Query-Lint Cycle]]
	- [[Obsidian Tooling for LLM Wiki]]
	- [[index]]
- Key context captured:
	- 이 글은 LLM Wiki를 학습용으로 이해하기 쉽게 RAG와 대비한다.
	- RAG는 질문마다 조각을 다시 찾아 조립하지만, LLM Wiki는 한 번 컴파일한 결과를 계속 덧쌓는 구조다.
	- 학습 관점에서는 Raw Source/Wiki/Schema 분리가 "원본과 해석을 분리하는 장치"로 중요하다.
	- Query는 단순 답변이 아니라 질문 결과를 다시 지식으로 남기는 운영 단계다.
	- qmd는 Wiki가 커졌을 때 `index.md` 기반 탐색을 보완하는 로컬 markdown 검색 엔진으로 정리했다.
- Reuse axis: 독서/책/학습, Codex 개발 워크플로, 취업/포트폴리오

## [2026-07-16] query | Obsidian graph demo script

- Source query: Obsidian Publish 비용 여부, 비용이 들 경우 graph GIF/영상으로 보여주는 방법, Web Clipper -> Raw Source -> ingest -> Wiki -> Query -> explored까지 보여주는 데모 시나리오 요청
- Saved query result: [[2026-07-16-Q-obsidian-graph-demo-script]]
- Primary sources:
	- [[Core Context]]
	- [[MOC-Portfolio]]
	- [[2026-07-16-Q-llm-wiki-sharing-demo-strategy]]
	- [[Ingest-Query-Lint Cycle]]
	- [[Human-AI Knowledge Boundary]]
	- Obsidian pricing official page
	- ScreenToGif GitHub
	- OBS Studio official page
- Index 업데이트:
	- [[index]]
- Key context captured:
	- Obsidian Publish는 비용이 있으므로, 지금은 GitHub README와 Obsidian graph 녹화 GIF/MP4 조합이 현실적인 1차 제출 방식이다.
	- 데모 메시지는 "Raw Source를 보존하고 LLM이 Wiki와 Query 결과로 컴파일해 포트폴리오와 학습 자산으로 재사용한다"로 잡는다.
	- `explored: true`는 실제로 읽고 검토한 페이지에만 적용하고, 데모에서는 검토 전/후 경계를 보여주는 것이 신뢰를 준다.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 에세이/블로그

## [2026-07-16] query | LLM Wiki sharing and demo strategy

- Source query: 이 LLM Wiki와 만든 것들을 URL 형식으로 공유해야 할 때 GitHub README를 제출할지, 배포해서 보여줄지, Obsidian 지식 그래프를 데모에서 어떻게 보여주는 것이 효과적인지에 대한 사용자 질문
- Saved query result: [[2026-07-16-Q-llm-wiki-sharing-demo-strategy]]
- Primary sources:
	- [[Core Context]]
	- [[MOC-Portfolio]]
	- [[LLM Wiki Pattern]]
	- [[Obsidian Tooling for LLM Wiki]]
	- GitHub Pages official docs
	- Obsidian Publish official page
	- Quartz official docs
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 가장 좋은 공유 방식은 GitHub README를 중심 허브로 두고, 공개 데모 사이트와 60-90초 그래프 시연 영상/GIF를 연결하는 조합이다.
	- 전체 vault를 그대로 공개하지 말고 `public/` 또는 `docs/`용 subset을 만들어 민감한 개인 맥락과 미검증 주장을 제외해야 한다.
	- 데모에서는 `Raw Sources -> Wiki -> Queries`, Obsidian graph, `MOC-Portfolio`, Query result, `explored`/`verificationStatus`/`confidence` 경계를 보여주는 흐름이 효과적이다.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 에세이/블로그

## [2026-07-16] lint | LLM Wiki health check

- Ran `/lint` health check across Wiki, Raw Sources, Queries, `index.md`, and `Core Context.md`.
- Fixed index/MOC sync:
	- Added missing `index.md` entries for [[Book Ingest Pattern]], [[Cohort Token Economy]], [[External Pre-processing Pattern]], [[Idea Generation Pipeline]], [[Track Classification and Research Gap Detection]], and [[LLM Wiki Token Optimization Strategies]].
	- Added missing MOC coverage in [[MOC-Knowledge Management]] for the same pages.
- Key findings:
	- Raw Source `collectionPurpose` coverage is 19/21.
	- Wiki `explored` coverage is 37/37, but 34 pages remain `explored: false`.
	- Wiki `verificationStatus` coverage is 37/37; no disputed pages found.
	- v5 `claimType` / `evidenceScope` coverage is 20/37.
	- One contradiction callout remains in [[RAG vs Compiled Wiki]].
	- Two pre-v2 Karpathy raw sources still need `collectionPurpose` backfill.
- Reuse axis: Codex 개발 워크플로, 취업/포트폴리오, 독서/책/학습

## [2026-07-16] query | How to use LLM Wiki well

- Source query: `$query 이 llm-wiki를 어떻게 하면 가장잘활용할수있어? 잘쓰는방법을 알려주고 활용방안알려줘`
- Saved query result: [[2026-07-16-Q-how-to-use-llm-wiki-well]]
- Primary sources:
	- [[Core Context]]
	- [[index]]
	- [[LLM Wiki Pattern]]
	- [[3-Layer Architecture]]
	- [[Ingest-Query-Lint Cycle]]
	- [[LLM Wiki as Learning Base]]
	- [[Human-AI Knowledge Boundary]]
	- [[Obsidian Tooling for LLM Wiki]]
	- [[MOC-LLM Wiki Guide]]
	- [[MOC-Portfolio]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 이 vault의 핵심 용도는 자료 저장소가 아니라 취업/프로젝트/학습 증거를 재사용 가능한 산출물로 컴파일하는 시스템이다.
	- 프로젝트 자료는 "무엇을 만들었나"보다 "무엇을 판단했고 어떻게 검증했나" 중심으로 ingest해야 한다.
	- Query는 단순 답변이 아니라 이력서 bullet, STAR 답변, 자기소개서 문단, 블로그 초안, evidence gap 분석 같은 재사용 산출물을 만드는 인터페이스다.
- Quality gaps:
	- 프로젝트별 Raw Source 근거와 AI boundary evidence가 아직 부족하다.
	- `MOC-Portfolio`의 Query Result 템플릿 gap은 아직 별도 템플릿 파일로 해결되지 않았다.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 독서/책/학습, 에세이/블로그

## [2026-07-14] query | Sales and psychology book recommendations

- Source query: `Clippings/1등이 될 수 없다면 무기를 모아야 합니다 1.md`
- Saved query result: [[2026-07-14-Q-sales-psychology-book-recommendations]]
- Updated Wiki page:
	- [[독서는 판단력과 자산관리의 기반이다]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 사용자는 세일즈와 심리학을 사람을 모으는 능력, 사람과 사람을 설득하는 능력으로 공부하고 싶어 한다.
	- 이 관심사는 본업 위에 상위 25% 보조 능력을 쌓는 전략이며, 독서/책/학습, 경제적 자유/FIRE/레버리지, 제품/창업 축에 연결된다.
- Reuse axis: 독서/책/학습, 경제적 자유/FIRE/레버리지, 제품/창업

## [2026-07-14] query | How to read sales and psychology books

- Source query: 세일즈와 심리학 책들을 읽을 때 어떻게 해야 잘 읽을 수 있는지에 대한 사용자 질문
- Saved query result: [[2026-07-14-Q-how-to-read-sales-psychology-books]]
- Updated Wiki page:
	- [[독서는 판단력과 자산관리의 기반이다]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 세일즈/심리학 책은 요약보다 행동 실험으로 읽는다.
	- 한 권에서 하나의 실험만 뽑고, 실제 대화·팀 운영·제품 설명·글쓰기·면접 답변에 적용한 뒤 결과를 기록한다.
- Reuse axis: 독서/책/학습, 경제적 자유/FIRE/레버리지, 제품/창업

## [2026-07-14] query | Yohan Koo LLM Wiki usage insights

- Source query: 구요한 대표는 Obsidian LLM Wiki를 어떻게 사용하면 좋다고 말했는지, 강의 인사이트와 본인 활용 방식이 무엇인지에 대한 사용자 질문
- Saved query result: [[2026-07-14-Q-yohan-koo-llm-wiki-usage-insights]]
- Primary sources:
	- [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]
	- [[LLM Wiki as Learning Base]]
	- [[Mothership-Satellite Vault Pattern]]
	- [[Agent-Readable Metadata]]
	- [[Obsidian Tooling for LLM Wiki]]
	- [[Human-AI Knowledge Boundary]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- LLM Wiki는 이미 아는 지식 보관소보다, 관심은 있지만 아직 설명할 수 없는 자료를 공부 가능한 형태로 만드는 학습 전초기지다.
	- 구요한 대표는 메인 볼트와 LLM Wiki 볼트를 분리하고, Query 결과와 질문 자체를 `Queries` 폴더에 남기는 방식으로 활용한다.
	- 메타데이터와 폴더 구조는 노트가 많아져도 필터링과 라우팅을 가능하게 하는 핵심 장치다.
- Quality gaps:
	- 강의 transcript의 STT 품질 때문에 인명과 일부 기술명이 흔들린다.
	- 본 답변은 2026-07-07 강의 transcript와 기존 Wiki 컴파일 기준이며, 이후 운영 방식은 별도 확인 필요.
- Reuse axis: Codex 개발 워크플로, 독서/책/학습, 에세이/블로그

## [2026-07-12] ingest | YouTube Inspiration Bundle For Economic Freedom North Star

- Source: [[2026-07-12-YouTube-Inspiration-Bundle-User-Reflections]] plus 13 YouTube transcript raw sources
- Origin: YouTube transcript markdown files copied from Desktop into Inbox, then user reflection captured in Codex session
- Collection purpose: 개발자로 성장해 고소득 커리어를 만들고, 자본 레버리지·AI 자동화·제품화·독서와 학습을 통해 경제적 자유라는 북극성에 가까워지기 위해 수집. 취업 포트폴리오 증거라기보다 개인 삶의 운영 지식이며, 투자/FIRE/AI/창업 관련 주장은 검증 필요 상태로 보존
- Raw Source 저장:
	- `10. Raw Sources/14. Transcripts/` — 13 YouTube transcript files
	- `10. Raw Sources/15. Clippings/` — 1 user reflection file
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 생성 (6):
	- Maps (1): [[경제적 자유는 나의 북극성이다]]
	- Guides (1): [[개발자 커리어로 경제적 자유에 가까워지기]]
	- Concepts (4): [[레버리지를 당하지 않고 사용하는 삶]], [[자본 레버리지는 자유의 핵심 엔진이다]], [[AI 자동화는 개인 생산성 레버리지다]], [[독서는 판단력과 자산관리의 기반이다]]
- Wiki 페이지 업데이트 (2):
	- [[harness]]
	- [[cuee]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 경제적 자유는 장기 북극성이며 개발자 커리어가 1순위 수단, 자본 레버리지가 2순위 수단
	- 첫 1억 이전의 생활습관·소비습관·투자습관이 이후 자산 증가의 기초
	- 자본 레버리지 전략은 `USD`, `QLD` 같은 반도체/기술주 2배 레버리지 ETF와 DCA/웅덩이 매수법 중심의 개인 운영 가설
	- AI 자동화는 Codex, [[harness]], Threads 반복 운영, 멀티 에이전트 workflow와 연결
	- [[harness]]는 바이브마피아 하네스 레포를 보고 Codex 맞춤형으로 변형한 것이며, [[cuee]]는 그 harness를 사용해 만든 초기 제품화 경험
	- 독서는 지식 복리와 판단력의 기반이며, 논픽션 편향을 보완하기 위해 픽션도 섞어 읽을 계획
- Verification boundary:
	- 투자, FIRE, AI, 1인 유니콘, 파생상품 모델 관련 외부 주장은 `verificationStatus: unverified`로 보존
	- 사용자 동기와 개인 운영 가설은 `user-original` 또는 `user-provided` 맥락으로 분리
- Reuse axis: 경제적 자유/FIRE/레버리지, 독서/책/학습, Codex 개발 워크플로, 제품/창업, 취업/포트폴리오

## [2026-08-04] query | Korean developer role model GitHub study map

- Source query: 허예찬, 류기백, 김연규, 최준건, 최윤제, 전수열, 박상권, 김민준, 진유림, 이동욱의 개발·agent·commit·PR/issue·README·문서·유지보수 방식을 롤모델로 공부하는 법
- Saved query result: [[2026-08-04-Q-korean-developer-role-model-github-study-map]]
- Created Wiki guide: [[개발자 롤모델을 GitHub에서 공부하는 법]]
- Updated Wiki page:
	- [[MOC-Portfolio]]
- Index 업데이트:
	- [[index]]
- Evidence boundary:
	- 2026-08-04 GitHub API의 profile, owned non-fork repository stars, representative repository tree, recent commit, public issue/PR comment를 사용
	- AI/agent 사용은 저장소 README, AGENTS, bot-signed maintainer comment로 공개된 허예찬·김연규 사례만 직접 서술
	- 박상권은 동명인 식별 근거가 부족해 보류
	- star와 follower는 변하는 스냅샷이며 코드 품질의 단일 지표가 아님
- Reuse axis: Codex 개발 워크플로, 취업/포트폴리오, 독서/책/학습, 에세이/블로그

## [2026-08-11] wiki | Securities backend career roadmap

- Source discussion: 금융과 개발을 함께 다루는 서울 증권사 IT 취업 목표, 퀀트/HFT 장기 관심, AI 위임 경계, 리스크 및 리더십에 대한 사용자 답변
- Current external evidence:
	- KB증권 2025년 4급 신입직원 공개채용
	- 미래에셋자산운용 2026년 주문관리시스템 개발·운영 신입 채용
	- 교보증권 2026년 상반기 IT 채용연계형 인턴
	- 2025년 하반기 KB증권 IT 지원자 면접 후기는 개인 경험 자료로 별도 표시
- Created Wiki guide:
	- [[김규태 금융 시스템 개발자 취업 로드맵]]
- Updated Wiki page:
	- [[MOC-Portfolio]]
- Index 업데이트:
	- [[index]]
- Key context captured:
	- 현실적인 1차 목표는 서울 증권사 백엔드·거래 인프라 IT 직군이며 장기 관심은 퀀트/HFT 시스템 개발
	- 주문 정확성, 데이터 정합성, 장애 복구와 p99 latency를 하나의 대표 포트폴리오로 연결
	- Java를 새 주언어로 결정하고 Python은 부하 테스트·분석·자동화 강점으로 유지
	- 지방 국립대 소프트웨어공학과 3학년의 현재 조건에서 2027년 상반기 서울 증권사 IT 지원까지 이어지는 월별 계획을 핵심 논제로 설정
	- 2026년 KB증권·LS증권·하나증권·넥스트증권 경력 공고는 신입 자격요건이 아니라 FEP·OMS·원장·전략매매의 실제 업무 구조를 파악하는 근거로 사용
	- 김영한의 실전 자바 기본편에서 시작하고, 2019년 출간된 AWS 책은 당시 버전을 복제하지 않고 현재 Spring Boot 안정 버전에 맞춰 구조와 배포 흐름을 학습
	- AI는 How 탐색과 구현을 도울 수 있지만 문제 정의, 이해관계, 검증 기준과 최종 책임은 인간이 담당
- Evidence boundary:
	- 공고에 직접 명시된 요구사항과 Codex가 제안한 학습·포트폴리오 전략을 분리
	- 기술 요구는 실제 지원 전 최신 공고로 다시 검증
- Reuse axis: 취업/포트폴리오, 백엔드/성능/금융 시스템, Codex 개발 워크플로

### Follow-up clarification

- 2027년 8월 졸업예정, 주당 최소 20시간 학습 가능으로 확정
- 현재 알고리즘은 프로그래머스 2단계, SQL은 용어 중심의 수업 경험만 있어 SQL 실습을 초기 핵심 격차로 지정
- 2026년 하반기 인턴을 1차 목표, 2027년 상반기 인턴·신입을 2차 목표로 수정
- 2026년 하반기 교보증권 채용연계형 인턴 사례를 통해 졸업예정일과 즉시 입사 가능 조건을 지원 전 먼저 확인하도록 보완
- Java 주문 시스템은 기존 Python 저장소와 분리하고, 기존 저장소는 부하 생성·성능 비교 근거로 보존하기로 결정
- 주 20시간 기본 배분을 Java 7, SQL·DB 5, 알고리즘·CS 4, 프로젝트 3, 인턴 탐색·회고 1시간으로 설정
- 인턴 범위를 증권사뿐 아니라 은행·핀테크·거래소·금융 IT 솔루션 회사까지 확장하고, 좋은 인턴 합격 시 휴학 가능으로 확정
- 평일 연구실 중심, 주말 집 보완 방식에 맞춰 평일 15시간·주말 5시간의 기본 시간표와 첫 8주 실행안을 추가
- 첫 포트폴리오 범위를 국내주식 현물 주문으로 제한하고, Java 기본기의 첫 완료 기준을 AI 없이 주문 상태 모델·JUnit 테스트·설계 이유를 설명하는 것으로 확정
- 이번 학기는 약 15학점이며 교양 비중이 높아 시험 기간에도 취업 준비 시간을 충분히 유지할 수 있다고 확인
- 인턴 선택 기준은 실제 Java 개발·코드리뷰, 금융 도메인, 멘토, 전환 가능성, 회사 이름 순으로 설정
- 제출 가능한 이력서가 없으므로 이번 주 1페이지 기본 이력서 작성을 0단계로 추가
- 첫 이력서는 [[financial-order-latency-lab]], [[Graduation-elasticsearch]], [[cuee]] 순으로 구성하고 개인 기여와 AI 활용 경계를 확인한 뒤 bullet을 작성하기로 함
- SQL 첫 완료 기준을 프로그래머스 3단계, 주문 스키마, JOIN·윈도 함수, 제약·인덱스, 트랜잭션 정합성 설명으로 확정
- 졸업요건 130학점 중 105학점 이수, 두 학기 남음, 평점 3.7, 군필, TOEIC 730, 자격증 없음으로 이력서 기본 정보 보강
- 방학 또는 한 학기 풀타임 인턴이 가능하고 좋은 인턴을 위해 휴학할 수 있다고 확인
- [[financial-order-latency-lab]]은 개인 프로젝트, [[Graduation-elasticsearch]]는 선배 연구를 이어 JavaParser·AST 담당, [[cuee]]는 팀장으로 초기 콘셉트·핵심 역할·타깃·마스킹 기술 전략을 결정한 것으로 역할 구체화
- [[financial-order-latency-lab]]의 수업 맥락이 기존 운영체제 기록과 현재 데이터베이스 수업 답변 사이에서 충돌해 확인 전까지 보류
- 최신 신입 공고에서 자격증·영어는 우대, SQL·데이터 모델링·알고리즘·OOP는 필요한 역량으로 제시된 점을 근거로 첫 8주는 자격증보다 Java·SQL·이력서·지원에 집중
- 평점은 3.7/4.5로 확인
- [[financial-order-latency-lab]]은 데이터베이스 수업에서 아이디어·개념을 배운 뒤 학기말에 만든 개인 프로젝트이며 AI가 코드·실험 설계·그래프·결과 해석 전 영역을 도왔다고 확인
- 좋은 금융 Java 인턴이라면 졸업을 2028년 2월로 늦추는 것도 허용
- 남명학사 서울관은 수도권 소재 대학 재학생 대상이라 현재 조건에 맞지 않음을 확인하고, 회사 주거지원·학교 현장실습 지원·단기 임대 순으로 거주 전략을 추가
- 공개 Git 이력 기준 프로젝트 기간을 [[financial-order-latency-lab]] 2026-05-12~05-18, [[Graduation-elasticsearch]] 2026-06-24~07-07, [[cuee]] 2026-05-01~08-04로 기록하고 실제 활동 기간은 별도 확인 대상으로 유지

## [2026-08-13] wiki | Financial career roadmap AI contribution boundary

- [[financial-order-latency-lab]]의 p99와 CPU·disk·GPU 조건은 AI가 제안했고 모든 코드는 AI가 생성했으며, 사용자는 현재 코드를 AI 없이 설명·수정·재현할 수 없다고 확인
- 사용자는 금융 시스템에서 하위 1%의 느린 요청이 신뢰성을 해칠 수 있어 p99가 중요하다고 판단했고, AI·머신러닝의 GPU 사용이 주문 지연에 미치는 영향을 흥미로운 실험 문제로 채택
- 해당 프로젝트를 개발 구현력의 대표 증거에서 제외하고 AI 활용 학습·문제의식으로 재분류
- 첫 이력서 증거 순서를 [[Graduation-elasticsearch]], [[cuee]], 리더십 활동으로 수정하고 새 Java 주문 시스템 완성 후 1순위로 교체하기로 함
- [[Graduation-elasticsearch]]는 2026년 5월, [[cuee]]는 2026년 4월부터 현재까지 진행 중으로 실제 기간 보완
- 서울·판교 인턴 주거비 허용 범위를 월 40만~70만 원으로 확정
- [[financial-order-latency-lab]], [[김규태 Career Narrative]]의 과장된 직접 개발 표현을 함께 정정
- [[financial-order-latency-lab]]의 최초 사용자 문제는 CPU·GPU·disk 속도와 latency를 금융 관점에서 비교하는 것이었고, AI가 코드·실행·재실험을 모두 수행했으며 사용자는 검증만 했다고 확인
- [[Graduation-elasticsearch]]의 JavaParser·AST 코드와 [[cuee]]의 실제 코드도 전부 AI가 작성한 것으로 확인
- 직접 구현 증거가 없는 현재 상태에 맞춰 첫 이력서 순서를 [[cuee]] 제품·팀 리딩, 리더십 활동, [[Graduation-elasticsearch]] 연구 참여로 재조정
- [[Graduation-elasticsearch]]의 직접 분석·구현 표현과 [[cuee]]의 Android·Kotlin 직접 구현 표현을 정정하고 [[Core Context]]의 포트폴리오 spine도 AI 기여 경계에 맞게 갱신
- [[financial-order-latency-lab]] 실제 기간을 2026년 5~6월로 확정

## [2026-08-16] wiki | Final AI boundary and cuee validation clarification

- [[financial-order-latency-lab]]에서 사용자가 별도 검증을 하지 않았으며 AI가 코드·실행·재실험 전부를 수행했다고 최종 확인
- 현재 AI 없이 작성한 코드는 없다고 확인
- 앞으로 모든 학습·설계·코드·테스트 과정에서 AI 사용을 허용하되, 문제 정의·설명·수정·테스트·검증과 AI 기여 공개를 포트폴리오 기준으로 설정
- [[Graduation-elasticsearch]]의 현재 사용자 산출물은 논문 정리로 확인
- [[cuee]]는 실제 노인 인터뷰·관찰이 아니라 어머니의 문제 제안에서 시작한 미검증 가설로 정정
- Roadmap, project entities, Career Narrative, Core Context의 AI 비사용 중심 표현을 이해·설명·수정·검증 중심으로 동기화
## [2026-07-23] ingest | 김규태 Personal Operating Manual and Self-Understanding Interview

- Sources:
	- [[2026-07-23-Kim-Gyutae-Personal-Operating-Manual-v1]]
	- [[2026-07-23-Kim-Gyutae-Romantic-Self-Reflection-v1]]
	- [[2026-07-23-Kim-Gyutae-Self-Understanding-Interview-v1]]
- Origin:
	- 사용자가 약 한 달 동안 직접 작성한 `규태 사용설명서`
	- 특정인을 좋아하며 작성한 `새로 태어나기`에서 제3자 정보를 제거한 자기관찰 발췌
	- Codex 인제스트 목적·모호성 질문에 대한 사용자 직접 답변
- Collection purpose: 자기이해와 메타인지를 심화하고, 미래의 AI 에이전트가 김규태에 관한 질문에 빈말보다 사실 기반 멘토링과 행동 개선안을 제공하도록 개인화 지식으로 재사용
- Raw Source 저장: `10. Raw Sources/15. Clippings/`
- Privacy handling:
	- `규태 사용설명서` 원문 전체를 `## Original Content` 아래 보존
	- MBTI 비하 문장은 Raw Source에만 보존하고 Wiki에는 승격하지 않음
	- `새로 태어나기` 원본의 제3자 개인정보와 구체적인 성행위 지침은 저장소에 복사하지 않음
	- 사용자 관련 문장 47개를 원문 그대로 발췌하고 `redacted: true`로 표시
- Mode: A standalone — mothership search skipped, `mainVaultRelated` / `mainVaultCmds` left empty
- Wiki 페이지 생성 (12):
	- Concepts (6): [[김규태 Motivation and Execution Pattern]], [[김규태 Breadth-to-Depth Development Pattern]], [[김규태 Stress and Recovery Pattern]], [[김규태 Leadership Pattern]], [[김규태 Attachment and Romantic Pacing Pattern]], [[김규태 Taste and Intellectual Intimacy]]
	- Guides (5): [[김규태 Personal Operating Manual]], [[김규태 Work and Learning Operating Guide]], [[김규태 Career Values and Success Vision]], [[김규태 Relationship Values]], [[김규태 AI Mentor Response Contract]]
	- Maps (1): [[MOC-김규태 Self Knowledge]]
- Wiki 페이지 업데이트 (3):
	- [[김규태]]
	- [[harness]]
	- [[김규태 Leadership and Teaching Evidence]]
- System pages updated:
	- [[Core Context]]
	- [[index]]
- Key context captured:
	- 빠르게 시작하는 실행력은 강하지만 깊이, 유지보수, 마감 관리가 보완 과제
	- 성장, 돈, 인정, 가시적 사용자 반응이 강한 동기이며 지식 축적과 개발자 정체성도 독립 동기로 존재
	- Threads 자동화는 포맷 실험, 사용자 반응 선택, 템플릿화, GitHub Actions 반복 운영으로 이어졌고 2026-07-23 사용자 자기보고 기준 팔로워 500명
	- AI 에이전트 개발은 T자형 세로축 후보지만 아직 구체 분야가 확정되지 않음
	- 비전·제품 방향·최종 결정은 선호하지만 일정·행정·타인 결과 관리는 보완 과제
	- 관계에서는 솔직함, 자율성, 신뢰, 지적 친밀감을 중시하며 빠른 감정 속도와 장기 반추가 반복 패턴
	- 동의는 자유로운 명시적 긍정과 지속적 확인을 기준으로 정규화
	- AI는 사실, 자기보고, 해석, 본인 책임, 타인 영역, 재발 방지 행동을 분리하는 멘토 역할을 우선
- Open question:
	- T자형 개발 전문성의 세로축은 `AI 에이전트를 이용한 개발`로 탐색 중이며 세부 문제 영역은 미정
- Reuse axis: 자기이해, AI 개인화, 취업/포트폴리오, Codex 개발 워크플로, 관계 메타인지

## [2026-07-16] query | Coding test as AI-era problem-solving training

- Source query: 사용자가 AI 시대에도 문제해결력과 컴퓨팅 사고력이 변하지 않는 본질이라면 코딩테스트 준비가 중요한지, 코딩테스트를 통해 어떤 차별점을 기를 수 있는지 질문
- Saved query result: [[2026-07-16-Q-coding-test-ai-era-problem-solving]]
- Wiki 페이지 생성 (1):
	- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
- Wiki 페이지 업데이트:
	- [[AI-Augmented Developer Positioning]]
	- [[김규태 Career Narrative]]
	- [[개발자 커리어로 경제적 자유에 가까워지기]]
	- [[MOC-Portfolio]]
	- [[index]]
- Primary sources:
	- [[Core Context]]
	- [[MOC-Portfolio]]
	- [[김규태 Career Narrative]]
	- [[AI-Augmented Developer Positioning]]
	- [[개발자 커리어로 경제적 자유에 가까워지기]]
	- Microsoft Careers technical interviewing guide
	- NACE Career Readiness Competencies 2024
	- Meta Careers hiring process
- Key context captured:
	- 코딩테스트는 단순 취업 필터가 아니라 AI 없이 문제를 분해하고 직접 구현·검증할 수 있음을 보여주는 기본기 증거다.
	- AI 활용 경험이 강할수록 코딩테스트 풀이 로그는 AI 의존 리스크를 줄이는 counter-evidence가 된다.
	- 공부 방식은 처음 풀이 AI 금지, 풀이 후 AI 리뷰, 복잡도/엣지케이스/오답 수정 로그, 프로젝트 연결이 핵심이다.
- Quality gaps:
	- 실제 코딩테스트 풀이 로그와 목표 회사별 최신 전형 Raw Source는 아직 없다.
	- AI-assisted coding interview 변화는 별도 source ingest 후 강화할 수 있다.
- Reuse axis: 취업/포트폴리오, 독서/책/학습, Codex 개발 워크플로, 에세이/블로그

## [2026-07-20] query | Shin Jinseo vs KataGo opponent-model strategy

- Source query: 사용자가 신진서와 KataGo의 최근 두 점 접바둑에서 KataGo가 상대를 신진서라는 개인으로 인식했는지, 블루스팟보다 약간 손해를 보더라도 전투를 유도해 인간 실수를 기대하는 편이 더 높은 승률이었는지 질문
- Saved query result: [[2026-07-20-Q-shin-jinseo-katago-opponent-model-strategy]]
- Wiki search: 관련 컴파일 Wiki, Raw Source, 기존 Query 검색 결과 없음
- Primary sources:
	- 한국경제 1국 보도·해설 칼럼
	- KBC 광주방송 2국 결과 보도
	- KataGo 공식 README 및 Analysis Engine 문서
- Key context captured:
	- 두 점 접바둑의 판 상태는 KataGo가 보지만, 신진서 개인을 인식하도록 설정됐다는 공개 근거는 없다.
	- KataGo의 일반 인간 모델은 선택적으로 설정할 수 있으나, 특정 선수 식별 모델과는 구분해야 한다.
	- 인간 실수 유도는 별도의 상대 모델과 목적함수에서만 합리화되며, 화면의 블루스팟은 그 설정 아래의 후보 평가다.
- Quality gaps:
	- 실제 대국의 KataGo 버전, 네트워크, GTP 설정, human 모델 사용 여부, SGF 분석 로그가 공개 확인되지 않았다.
- Index 업데이트:
	- [[index]]
- Reuse axis: 독서/책/학습, 에세이/블로그, AI 전략

## [2026-07-16] query | AI-assisted coding test learning loop

- Source query: 사용자가 코딩테스트 문제 풀이 중 막히거나 디버깅하거나 엣지케이스에서 통과하지 못할 때 AI를 학습에 어떻게 활용할 수 있는지 질문
- Saved query result: [[2026-07-16-Q-ai-assisted-coding-test-learning-loop]]
- Wiki 페이지 업데이트:
	- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
	- [[index]]
- Primary sources:
	- [[Core Context]]
	- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
	- [[AI-Augmented Developer Positioning]]
	- [[Human-AI Knowledge Boundary]]
	- [[MOC-Portfolio]]
	- [[2026-07-16-Q-coding-test-ai-era-problem-solving]]
- Key context captured:
	- AI는 정답 생성기가 아니라 힌트 제공자, 실행 추적자, 반례 생성기, 풀이 리뷰어로 제한해 사용한다.
	- 막힘 단계별로 AI 사용 허용 범위를 나누면 학습 소유권을 유지할 수 있다.
	- 풀이 로그에는 `AI gave`와 `I changed`를 분리해 AI 활용과 본인 판단 경계를 남긴다.
- Quality gaps:
	- 실제 풀이 로그가 아직 없으므로 2-4주 기록 후 루프 효과를 확인해야 한다.
	- 실전 전형에서는 회사/플랫폼의 AI 사용 규칙을 별도 확인해야 한다.
- Reuse axis: 취업/포트폴리오, 독서/책/학습, Codex 개발 워크플로, 에세이/블로그

## [2026-07-26] ingest | AI-era developer learning and computational thinking clippings

- Sources: 11 markdown clippings from the vault-root `Clippings/` folder plus [[2026-07-26-Kim-Gyutae-AI-Era-Developer-Reflection]]
- Collection purpose:
	- AI·컴공·젠슨 황·도메인 전문성: AI 시대 개발자 역량과 커리어 방향 판단
	- 공부법·프리렌·추상화·분해: 메타인지와 컴퓨팅 사고 기반 학습법 구축
	- qmd: LLM Wiki 및 Codex 검색 시스템 개선
	- 능력 조합: 개발자 커리어와 경제적 자유를 위한 역량 포트폴리오 설계
	- 독서와 은유: 독서를 연결·아이디어 생성 능력으로 전환
	- 겸손: 리더십과 자기표현에 관한 개인 판단 기준 정립
- Raw Source 저장 (12): `10. Raw Sources/15. Clippings/`
	- [[2026-07-25-Gemini-Computational-Thinking-Abstraction]]
	- [[2026-07-25-Gemini-Computational-Thinking-Decomposition]]
	- [[2026-07-25-YouTube-AI시대-컴퓨터공학-교육]]
	- [[2026-07-26-YouTube-메타인지-공부법]]
	- [[2026-07-13-YouTube-AI시대-공부법]]
	- [[2026-07-13-YouTube-Shorts-AI시대-도메인-지식]]
	- [[2026-07-26-YouTube-젠슨황-AI-인프라]]
	- [[2026-07-14-GitHub-qmd-README]]
	- [[2026-07-14-YouTube-능력-조합으로-희소성-만들기]]
	- [[2026-07-13-YouTube-Shorts-독서-은유-연결]]
	- [[2026-07-13-YouTube-겸손과-자기표현]]
	- [[2026-07-26-Kim-Gyutae-AI-Era-Developer-Reflection]]
- Mode: A standalone — mothership search skipped; `mainVaultRelated` and `mainVaultCmds` left empty
- Wiki 페이지 생성 (7):
	- [[컴퓨팅 사고의 추상화와 분해]]
	- [[AI 시대의 개발자 학습 전략]]
	- [[메타인지 학습 루프]]
	- [[일반 지식보다 도메인 지식이 중요해지는 이유]]
	- [[능력 조합으로 희소성을 만드는 전략]]
	- [[겸손과 자기표현의 균형]]
	- [[AI 팩토리와 토큰 생산 인프라]]
- Wiki 페이지 업데이트 (7):
	- [[AI-Augmented Developer Positioning]]
	- [[독서는 판단력과 자산관리의 기반이다]]
	- [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
	- [[qmd]]
	- [[Obsidian Tooling for LLM Wiki]]
	- [[김규태 Career Narrative]]
	- [[MOC-Portfolio]]
- User-original context promoted:
	- 개발자는 단순한 코드 작성자가 아니라 현실 문제를 입력·출력·제약으로 추상화하고, 블랙박스 내부를 하위 문제와 의존성으로 분해해 구현·검증하는 사람이라는 개발자 사고 원칙
	- Gemini 답변은 독립적으로 검증된 권위가 아니라 사용자에게 의미 있었던 AI 생성 조언으로 명시
- Core Context 업데이트: [[Core Context]]
- Verification boundary:
	- 신규 Wiki 페이지는 `explored: false`
	- AI 생성 조언, 짧은 영상, 개인 경험, 번역 인터뷰는 `verificationStatus: unverified` 또는 `partial`로 유지
	- qmd README는 캡처 시점의 스냅샷으로 기록
- Index 업데이트: [[index]]
- Reuse axis: 취업/포트폴리오, 독서/책/학습, 강의/수업/교육, Codex 개발 워크플로, 경제적 자유/FIRE/레버리지, 제품/창업, 에세이/블로그

## [2026-08-24] ingest | Quant research, TMU SDG portfolio, and AI-assisted engineering notes

- Sources selected from Inbox and project root:
	- [[2026-08-17-Gemini-Quant-Research-Conversation]]
	- [[2026-08-24-Kim-Gyutae-TMU-SDG-Portfolio-Record]]
	- [[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]]
- Collection purpose inferred with user approval:
	- Gemini: 퀀트 연구·금융 시스템에서 알파, 가설, 백테스트 편향, 시장중립, 변동성, AI/ML 역할을 학습
	- TMU: 수료·성적·출석·영어 사용·SDG 학습을 근거와 표현 한계까지 취업 자료로 보존
	- 독서 메모: 빠른 코드 생성을 테스트·엣지케이스·분해·도메인 규칙·성능 검증으로 전환하는 개발 원칙 구축
- Mode: A standalone — mothership search skipped; `mainVaultRelated` and `mainVaultCmds` left empty
- Raw Source 저장 (3):
	- Clippings (2): [[2026-08-17-Gemini-Quant-Research-Conversation]], [[2026-08-24-Kim-Gyutae-TMU-SDG-Portfolio-Record]]
	- Books (1): [[2026-07-27-Kim-Gyutae-Beyond-Vibe-Coding-Reading-Notes]]
- Wiki 페이지 생성 (8):
	- Concepts (6): [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]], [[백테스트 과적합과 편향]], [[시장중립은 무위험이 아니다]], [[변동성 트레이딩과 델타 헤징]], [[AI와 머신러닝 시대의 퀀트 리서치]], [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]
	- Entities (1): [[TMU Global Leadership Program]]
	- Guides (1): [[김규태 개발 도메인 영어 성장 계획]]
- Wiki 페이지 업데이트 (6):
	- [[AI 시대의 개발자 학습 전략]]
	- [[컴퓨팅 사고의 추상화와 분해]]
	- [[AI-Augmented Developer Positioning]]
	- [[김규태 Career Narrative]]
	- [[김규태 금융 시스템 개발자 취업 로드맵]]
	- [[MOC-Portfolio]]
- Verification boundary:
	- Gemini의 금융·인물·도서·수익률 주장은 독립 검증 전까지 `unverified`로 유지
	- `시장중립 ≠ 무위험`, `델타 중립 ≠ beta 0`, `백테스트 ≠ live proof` 경계를 명시
	- TMU 수료·학습 기록과 Solutions Day 개인 기여 주장을 분리
	- 독서 메모에는 누락된 저자·출판사·판본·페이지를 추정하지 않음
- Preservation check:
	- 세 source 본문은 보존됨; SDG는 byte-identical, Gemini와 독서 메모는 내용이 동일하고 파일 끝 개행만 정규화됨
	- Inbox 원본은 Raw Source 저장 후 제거됨
- System pages updated: [[index]], [[log]]
- Reuse axis: 백엔드/성능/금융 시스템, 취업/포트폴리오, 강의/수업/교육, Codex 개발 워크플로, 독서/책/학습

## [2026-08-24] update | TMU Global Leadership Program full schedule from guidebook PDF

- Source document: `Session 2 (Korea) - Global Leadership Program - Summer 2026.pdf`
- Updated: [[2026-08-24-Kim-Gyutae-TMU-SDG-Portfolio-Record]]
- Schedule coverage:
	- Program schedule pages 7~10: 2026-07-27~2026-08-21의 오전 수업, Group Conversation, 필수·선택 활동, 장소, 등록 필요 표시
	- Toronto Happening Events page 11: 프로그램 외 도시 행사 8개를 별도 표로 분리
- Verification:
	- Poppler text extraction 후 PDF 7~11페이지 렌더링과 대조
	- 프로그램 편성과 김규태의 실제 참여를 분리
	- PDF 전체에는 Wi-Fi 접속 정보와 단체 채팅 QR이 포함되어 저장소에 원본 PDF를 복사하지 않음
- System page updated: [[index]]
- Reuse axis: 취업/포트폴리오, 강의/수업/교육, 개발 도메인 영어

## [2026-08-31] query | 2026년 2학기 푸른등대 장학금 적합도

- Query saved: [[2026-08-31-Q-pureundeungdae-scholarship-fit]]
- Inputs: 경상국립대학교 진주캠퍼스 소프트웨어공학과 3학년, 8학기 중 7번째 학기, 평점 4.1, 학자금 지원구간 9구간
- Sources: 사용자 제공 푸른등대 사업계획 PDF 2개, [[김규태]], 프로젝트 및 리더십 Wiki 페이지
- Conclusion: NICE그룹 1순위, 김재영 2순위; LH는 현재 거주 요건과 3구간 이하 요건 모두 불충족
- Verification boundary: 평점은 공식 백분위로 환산하지 않았고, 프로젝트의 AI 기여 경계와 Wiki verificationStatus를 반영
- System page updated: [[index]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술

## [2026-08-31] query update | NICE와 김재영 최종 선택

- Updated: [[2026-08-31-Q-pureundeungdae-scholarship-fit]]
- New inputs: 누적 평점 약 3.7/4.5, 직전학기 4.1/4.5, NICE 교육·오프라인 행사 참여 가능
- Decision: 누적 평점이 아니라 직전학기 백분위를 사용하는 평가 구조와 9구간의 소득점수 불리함을 함께 반영해 NICE그룹으로 최종 추천
- Remaining gap: 대학이 등록한 직전학기 공식 백분위와 미공개 지원자 수·합격선

## [2026-08-31] query update | NICE 신청 확정 및 자기소개서 사전 점검

- Updated: [[2026-08-31-Q-pureundeungdae-scholarship-fit]]
- Decision: NICE그룹 신청 확정
- New academic facts: 2026년 1학기 신청·취득 22학점, 평점계 82, 평점평균 4.1/4.5, 석차 5/10
- Ambiguity: 평점계 82와 22학점의 단순 나눗셈이 4.1과 일치하지 않아 P/F 과목 또는 평점 산입 학점 확인 필요
- Drafting gate: 공식 백분위, 진로 정합성, 데이터 활동 수치·증빙, 실패 극복 행동, 학기별 장학금 사용 계획을 확정한 뒤 자기소개서 작성

## [2026-08-31] query | NICE 자기소개서 증거 지도

- Query saved: [[2026-08-31-Q-nice-scholarship-essay-evidence-map]]
- Updated Wiki pages: [[김규태]], [[harness]], [[김규태 Motivation and Execution Pattern]]
- New user-reported evidence: 2026-05-25 Threads 운영 시작, 매일 1개 자동 게시, 참여지표가 큰 글을 Excel로 비교해 형식 개선, 2026-08-31 팔로워 650명
- Career direction under review: 기존 금융권 관심과 최근 빅데이터 관심을 연결한 금융 데이터 분석가
- Verification boundary: Threads 활동은 기초 참여지표 분석으로 한정하고, 계정 분석 화면·Excel 구조·전후 수치가 없으므로 고급 통계 또는 빅데이터 분석으로 과장하지 않음
- Evidence gap: 경남권 창업동아리 대상 공식 증빙, SEALAB 직접 수행 범위, 데이터 관련 교과목·성적, 학기별 장학금 예산, 공식 백분위
- System page updated: [[index]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술

## [2026-08-31] query update | NICE 자기소개서 외부 증빙 검토

- Updated: [[2026-08-31-Q-nice-scholarship-essay-evidence-map]], [[cuee]], [[harness]], [[Graduation-elasticsearch]]
- Threads evidence: 공개 저장소와 52행 metrics CSV 확인; 51개 유효 조회수의 총합 131,868, 중앙값 1,147, 형식별 지표 feedback 구현 확인
- Award evidence: 2026-06-16 경남권 창업역량강화 심화교육 대상, 2026-08-11 학생창업유망팀 300+ 연계 동아리 챌린지 우수상 확인
- Research evidence: CoDoc·Neo4j·JavaParser/Symbol Solver·source/test CSV 분석 흐름을 담은 사용자 연구 노트 확인
- Career decision: 장학금 진로는 금융 데이터 분석가, 퀀트 트레이더는 장기 확장 관심으로 분리
- Score update: 사용자 확인 백분율 91.8 기준 NICE 1차 예상점수 88.04
- Contradiction flagged: 8월 우수상 대회 피드백을 6월 대상에 반영했다는 시간 순서는 불가능해 별도 아이디어톤 확인 필요
- Attribution correction: LLM Wiki 강연자는 `KIST 고요한`이 아니라 CMDSPACE `구요한`으로 보이며 불확실한 소속은 자기소개서에서 제외

## [2026-09-04] query | AI 시대 금융권·핀테크 백엔드 취업 준비

- Source query: 금융권 백엔드 포트폴리오용 책, 18학점·다음 학기 캡스톤 3학점 조건의 1년 취업 준비, 자격증 로드맵 평가, AI로 어려워진 신입 채용에서 필요한 역량과 현실적인 지원 전략을 정리해 달라는 요청
- Saved query result: [[2026-09-04-Q-finance-backend-ai-era-job-preparation]]
- Wiki pages updated:
	- [[Core Context]] — 최신 자기보고 기준 4학년, 금융권·핀테크 Java 백엔드 1차 목표 반영
	- [[김규태 Career Narrative]] — 학년과 1차 목표 갱신
	- [[김규태 금융 시스템 개발자 취업 로드맵]] — 18학점·다음 학기 캡스톤 3학점, 금융권·핀테크 지원 범위 반영
	- [[MOC-Portfolio]] — 새 실행안 연결 및 최신 상태 반영
	- [[index]] — Query 16건으로 갱신
- Key context captured:
	- AI 시대에는 단순 코드 생성보다 문제 정의, Java·Spring·DB 기본기, 금융 정합성, 테스트·장애·성능 검증과 설명 책임이 중요하다.
	- 대표 포트폴리오는 계좌이체·거래원장 또는 국내주식 주문을 좁게 잡고 멱등성, 동시성, 대사, 복구와 p99를 증명한다.
	- 자격증은 토익스피킹 → SQLD → 정보처리기사 순서를 유지하되 2027년 2월 지원 준비 완료를 더 높은 우선순위로 둔다.
	- 지원 범위는 은행·대형 핀테크뿐 아니라 카드·증권·보험 IT, 금융 IT 자회사, PG·결제사, 금융 솔루션·SI와 인턴까지 넓힌다.
- External evidence:
	- 소프트웨어정책연구소의 생성형 AI와 SW 개발자 채용 전망
	- 신한은행 2026 디지털/ICT 채용의 알고리즘·SQL 전형
	- 토스뱅크 서버 개발 직무의 Java/Spring·정합성·금액 흐름 요구
- Quality gaps:
	- 현재 Java 직접 구현 수준, 프로젝트 최종 범위, 토익스피킹 목표 점수, 실제 코딩테스트·SQL 로그는 추가 확인이 필요하다.
	- 2027년 채용과 자격시험 일정은 공식 발표 후 재검증해야 한다.
- Reuse axis: 취업/포트폴리오, 백엔드/성능/금융 시스템, 독서/책/학습, Codex 개발 워크플로

## [2026-09-09] ingest | KB증권·금융권 Java 백엔드 취업 상담

- Raw Source: [[2026-09-09-Codex-KB-Securities-Java-Backend-Career-Conversation]]
- Collection purpose: 2027년 8월 졸업 전까지 인턴·취업을 마치기 위해 KB증권·금융권 Java 백엔드에 필요한 부족 역량과 프로젝트·학습·지원 계획을 지속적으로 관리
- Saved query result: [[2026-09-09-Q-kb-securities-java-backend-starting-plan]]
- Updated Wiki page: [[김규태 금융 시스템 개발자 취업 로드맵]] — 2026-09-09 현재 Java·SQL·포트폴리오 기준선과 첫 실행 순서 추가
- Updated MOC: [[MOC-Portfolio]] — 새 Java 모의 증권 주문 시스템을 직접 설명·수정·검증 가능한 최우선 대표 프로젝트 후보로 배치
- Key decision: 공모전 수상과 자격증 개수보다 Java·SQL·Spring으로 금융 정합성을 직접 구현하고 테스트한 증거를 우선
- AI boundary: 사람·AI의 키 입력 비율이 아니라 요구사항 정의, 설명, 수정, 테스트, 검증과 기여 공개로 학습 소유권을 판정
- Mothership links: standalone mode이므로 생략
- Verification boundary: 현재 역량은 사용자 자기보고이며 실제 Java 진단, 8주 산출물과 2027년 채용 자격은 후속 검증 필요
- System page updated: [[index]] — Raw Sources 41건, Queries 17건으로 갱신
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습
