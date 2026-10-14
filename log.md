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
date modified: 2026-10-12
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

## [2026-09-01] query update | NICE 초안 전 최종 모호성 감사

- Confirmed actual academic-term living cost: monthly commute 10만 원 plus campus meals 20 days × 1만~2만 원 = 30만~50만 원 per month, or 120만~200만 원 for four months.
- The budgeted living costs, 133만 4,500원 for 2026-2 and 155만 2,000원 for 2027-1, fall within the confirmed range; the 2027-1 amount remains an assumption until the final-semester timetable is known.
- User confirmed that an official GNU transcript can be issued; the current MyGNU grade-check PDF remains non-submittable.
- Remaining non-blocking checks before final submission: user review of the Threads classification/formula/chart, official transcript issuance, and final 2027-1 timetable/actual course prices.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술

## [2026-09-01] query correction | Threads 지표·NICE 일정·증빙 문서

- Corrected 2026-07-15 Threads metrics from an incorrectly associated public-page payload to the user-provided screen and matching 72-hour CSV: likes 19, raw replies 3, author chain replies 3, audience replies 0, reposts 8; screen-only shares 2 are excluded from cross-post engagement comparisons.
- Official NICE plan confirms 2026-2 200만 원, 2027-1 300만 원, with offline events split across 2026-11, 2026-12, 2027-01, and 2027-02; the 70만 원 travel estimate should therefore be split 35만 원 per semester.
- NICE itself provides online Python, Pandas, and financial-data-analysis training, so outside courses should fill statistics, experiment design, and backtesting gaps instead of duplicating the program.
- Git evidence confirms README update commit `be8a878` on 2026-07-14; the professor-feedback date remains unknown and must not be inferred as an exact date.
- `report (2).pdf` was issued on 2026-09-01 and shows academic-record status `4학년`, but it is a MyGNU `성적확인표` explicitly marked as not valid supporting evidence; an official transcript is still required if course grades are submitted in the optional portfolio.
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

## [2026-09-05] query | AI 시대 개발자 취업 공부 우선순위

- Source query: AI 시대에 좋은 개발 직장에 취업하기 위해 현실적으로 무엇을 공부하고 어떤 역량을 어떤 순서로 준비해야 하는지에 대한 개인화 요청
- Saved query result: [[2026-09-05-Q-ai-era-developer-job-readiness-priority]]
- Updated Wiki page: [[김규태 금융 시스템 개발자 취업 로드맵]] — 우리은행 2026년 하반기 TECH 전형의 알고리즘·SQL 코딩테스트와 포트폴리오 면접 근거 추가
- Key decision: 현재 가장 큰 병목을 자격증이나 AI 도구가 아니라 직접 설명·수정·검증 가능한 Java·SQL 구현 증거의 부족으로 확정
- Execution order: 2주 진단 → 8주 금융 주문 MVP → 2026년 12월 지원 가능한 v1 → 2027년 1~2월 동시성·장애·성능 심화 → 2027년 3월 지원 병행
- Weekly floor: 18학점 학기에는 주 12시간을 최소선으로 유지하고 가능한 주에는 16~20시간으로 확장
- Verification boundary: 계획은 Wiki의 partial·medium 자료와 일부 2025~2026 채용 공고를 바탕으로 하며, Java 진단 결과와 2027년 실제 채용 일정은 아직 확인되지 않음
- System page updated: [[index]] — Query 17건으로 갱신
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-05] query | 네 가지 삶의 고민을 위한 세계문학

- Saved query: [[2026-09-05-Q-world-literature-for-love-career-and-city]]
- Recommendations: 《백야》, 《스토너》, 《전망 좋은 방》, 《브루클린》
- Personalization: 관계·취향·진로 Wiki와 현재 대화를 함께 참고하고 현재 안정·워라밸 욕구를 과거 성장 우선순위보다 낮게 취급하지 않음
- Quality boundary: 개인화 페이지는 unverified이며 작품의 적합성은 AI 해석. 상대의 의도나 관계 변화의 원인을 확정하지 않음
- Feedback gap: 직업 가치 우선순위의 변화 가능성과 실제 독후 반응은 Query에 남기고 기존 성격·가치 페이지에는 확정 반영하지 않음
- System page updated: [[index]] — Query 18건으로 갱신
- Reuse axis: 독서/책/학습, 개인 삶의 의사결정

## [2026-09-06] query | Output-first 개인 독서 우선순위

- Saved query: [[2026-09-06-Q-output-first-personal-reading-priority]]
- Cart reviewed: 선택된 8종 13권과 253,180원 결제 예정 금액을 확인하고 개인 소장용일 때 중복 수량을 줄이는 안을 제시
- First queue: 《스프링 부트 4 개발자 되기 + AI: 자바 편》, 《4000주》, 《프로그래머의 뇌》, 《앨저넌에게 꽃을》, 《남아 있는 나날》, 《객체지향의 사실과 오해》
- Bias diagnosis: 남성 저자·개인 성공·부·레버리지·실리콘밸리·AI 전망 편향을 지적하고 일 밖의 정체성, 사랑의 책임, 공동체, 사회적 정상성 관점의 보완 도서를 추가
- Wiki feedback: [[독서는 판단력과 자산관리의 기반이다]]에 기술서·자기계발서·문학별 output 규칙과 동시 진행 3권 제한을 추가
- Quality boundary: Java 진단, 자격시험 상태, 기존 완독 여부가 미확인이므로 일부 순위는 조건부이며 개인화 페이지의 unverified 상태를 유지
- System page updated: [[index]] — Query 19건으로 갱신
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 독서/책/학습, 에세이/블로그

## [2026-09-06] query update | 보유 도서와 재고 상태 반영

- Updated query: [[2026-09-06-Q-output-first-personal-reading-priority]]
- Ownership correction: 이미 보유한 《스프링 부트와 AWS로 혼자 구현하는 웹 서비스》를 첫 기술서로 사용하고 《스프링 부트 4 개발자 되기 + AI》는 조건부 구매로 변경
- Reading method: 2019년판의 구조는 활용하되 새 프로젝트는 지원 중인 안정 버전으로 만들고 버전 차이를 마이그레이션 로그와 테스트로 증거화
- Availability correction: 《4000주》 종이책 재고가 없을 때 eBook·도서관·타 서점을 이용하도록 구매안을 수정
- Literature clarification: 민음사 세계문학전집의 삼각관계 소설을 《브람스를 좋아하세요…》로 확인하고, 《앨저넌에게 꽃을》 → 《남아 있는 나날》 → 《종의 기원담》 순서를 추가
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 독서/책/학습

## [2026-09-06] query | 현재 상황에 맞춘 자기계발서

- Saved query: [[2026-09-06-Q-personal-self-help-reading-priority]]
- First queue: 《디자인 유어 라이프》 → 《4000주》 → 《메이크 잇 스틱》 → 《열정의 배신》 → 《비폭력대화》
- Key decision: 추가 성공 동기보다 진로 프로토타입, 유한성 수용, 인출 연습, 커리어 자산, 관찰·감정·욕구·요청의 구분을 우선
- Reading boundary: 동시에 자기계발서 한 권만 읽고 책마다 7일 행동 실험 하나를 완료한 뒤 다음 책을 구매
- Deferred cluster: 부·레버리지·실리콘밸리·개인 성공 서적의 연속 독서는 현재 편향과 조급함을 강화할 수 있어 뒤로 배치
- System page updated: [[index]] — Query 20건으로 갱신
- Reuse axis: 독서/책/학습, 개인 삶의 의사결정, 취업/포트폴리오, 에세이/블로그

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
- System page updated: [[index]] — Raw Sources 41건, Queries 21건으로 갱신
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-08-25] query | Recent essential books for the AI era

- Query saved: [[2026-08-25-Q-recent-ai-era-essential-books]]
- Wiki pages consulted:
	- [[독서는 판단력과 자산관리의 기반이다]]
	- [[AI 시대의 개발자 학습 전략]]
	- [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]]
	- [[일반 지식보다 도메인 지식이 중요해지는 이유]]
- Current publication and recognition checks:
	- `AI Snake Oil` (2024; Korean edition `AI 버블이 온다`, 2025)
	- `Empire of AI` (2025; Korean edition `AI 제국`, 2026; 2025 NBCC nonfiction winner)
	- `The Thinking Machine` (2025; 2025 FT and Schroders Business Book of the Year)
	- `Supremacy` (2024; 2024 FT and Schroders Business Book of the Year)
	- `Code Dependent` (2024; Women's Prize for Non-Fiction shortlist)
- Durable feedback: linked the reading path from [[독서는 판단력과 자산관리의 기반이다]]
- Quality boundary: recent books are described as acclaimed candidates with durable potential, not already established classics
- Reuse axis: 독서/책/학습, 취업/포트폴리오, 백엔드/성능/금융 시스템, Codex 개발 워크플로

## [2026-08-29] audit | Whole-vault knowledge integrity

- Report saved: [[2026-08-29-Q-vault-audit]]
- Scope: Wiki 70 pages, MOCs 5, Raw Sources 40, pre-audit Queries 14
- Scores: eligibility 90, consistency 60, confirmability 73, composite health 74/100
- Material conflicts: 2 MOC clusters (`MOC-Portfolio`, `MOC-LLM Wiki Guide`)
- Clear high-confidence overclaims: 4 source-empty pages
- Verification state: unverified 58, partial 12, verified 0, disputed 0
- Audit orphans: 7 pages outside direct MOC membership
- Write boundary: no Wiki page mutated; Top 10 follow-up targets queued for `/verify`

## [2026-08-29] verify | Cohort Token Economy

- Page verified: [[Cohort Token Economy]]
- Eligibility: added `claimType: mixed`, `evidenceScope: synthesis-only`, verification metadata, and official source links
- Consistency: preserved the cohort-operations concept but removed unsupported certainty from the related token-optimization narrative
- Confirmability: no Raw Source or cohort log supports `80%+`, `1-2 weeks`, or "Pro is sufficient for hobby use"
- Official boundary: Anthropic documents session/weekly limits and variable usage factors, not cohort incidence or timing
- Confidence: `high` → `low`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify LLM Wiki Token Optimization Strategies`, `/verify External Pre-processing Pattern`

## [2026-08-29] verify | LLM Wiki Token Optimization Strategies

- Page verified: [[LLM Wiki Token Optimization Strategies]]
- Eligibility: added prescriptive claim type, primary-source scope, verification metadata, Sources, and Bias Check
- Consistency: aligned the guide with the now-partial [[Cohort Token Economy]] hypothesis and standalone Raw Source preservation rules
- Corrected current facts: `/effort low` replaces unsupported `minimal`; Claude plans use Max 5x/20x; Qwen3.6 official open weights are 27B and 35B-A3B; Gemma 4 31B targets large servers
- Safety correction: removed `--dangerously-skip-permissions` as a general optimization and limited bypass permissions to isolated environments
- OpenAI boundary: official Deep Research models target complex multi-source research and are not treated as a universal preprocessing default
- Confidence: `high` → `medium`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify External Pre-processing Pattern`

## [2026-08-29] verify | External Pre-processing Pattern

- Page verified: [[External Pre-processing Pattern]]
- Eligibility: added prescriptive claim type, synthesis-only evidence scope, verification metadata, official sources, and Bias Check
- Consistency: restored the vault boundary between preserved Raw Sources and tool-generated derivative material
- Confirmability: no Raw Source or comparison log supports the prior `50-80%` token saving estimate or a universal cost, speed, or vendor-quality advantage
- OpenAI boundary: Deep Research is documented for complex multi-source research; Whisper is documented for speech-to-text, not as proof that the resulting derivative can replace the original source
- Workflow correction: direct ingest and external preprocessing must be compared on omissions, distortion, traceability, time, and actual cost before adoption
- Confidence: `high` → `medium`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify MOC-Portfolio`

## [2026-08-29] verify | MOC-Portfolio

- Page verified: [[MOC-Portfolio]]
- Eligibility: added four linked Raw Sources, mixed claim type, mixed-source scope, confidence, verification metadata, and Bias Check
- Consistency: corrected the four-project count and synchronized [[financial-order-latency-lab]] with [[Core Context]] and its entity page
- Contribution boundary: the user proposed the financial latency question; AI selected the p99 setup and performed the code, execution, re-execution, and interpretation, which the user did not independently verify
- Portfolio correction: replaced implementation-strength wording with a transparent plan to build directly explainable, modifiable, and reproducible Java backend evidence
- Threads boundary: the latest linked user interview reports 500 followers on 2026-07-23, but independent API or screenshot proof remains missing
- Confidence: unset → `medium`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify MOC-LLM Wiki Guide`, `/verify financial-order-latency-lab`

## [2026-08-29] verify | MOC-LLM Wiki Guide

- Page verified: [[MOC-LLM Wiki Guide]]
- Eligibility: added prescriptive claim type, primary repo-document scope, confidence, verification metadata, Sources, and Bias Check
- Consistency: replaced the legacy Claude-first schema with the current `AGENTS.md` → `.agents/skills/` → `.codex/commands/` Codex priority
- Ingest correction: removed the fixed `10-15 pages` update claim and documented the collection-purpose gate, Original Content preservation, targeted compilation, index/log sync, and final review
- Operations: documented `$status`, `$lint`, `$audit`, `$verify`, `$reindex`, and `$refresh-context`; broken links are classified instead of automatically generating pages
- Standalone mode: confirmed against [[Core Context]] with `source-vault: null`
- Confidence: unset → `high`
- Verification status: `unverified` → `verified`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify Book Ingest Pattern`, `/verify LLM Wiki Pattern`

## [2026-08-29] verify | Book Ingest Pattern

- Page verified: [[Book Ingest Pattern]]
- Eligibility: added the Karpathy Raw Source and current Codex command, hook, and changelog evidence with verification metadata and Bias Check
- Attribution correction: Karpathy describes raw-to-Wiki incremental compilation and filing useful outputs back into the Wiki, but does not state a "compile when read, not when scraped" rule or chapter-stub workflow
- Local-design boundary: classified Progressive Stubs as this repository's prescriptive harness design rather than an external principle
- Hook correction: current Codex validation requires the Original Content heading, checks substantive bodies for normal sources, and explicitly exempts `status: stub` from the body-length gate
- Confirmability: no completed Book Ingest case currently demonstrates lower token cost, less contamination, or better learning outcomes
- Confidence: `high` → `medium`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify LLM Wiki Pattern`, collect one real Book Ingest comparison

## [2026-08-29] verify | LLM Wiki Pattern

- Page verified: [[LLM Wiki Pattern]]
- Eligibility: added mixed claim type, mixed-source scope, verification metadata, verification boundary, and Bias Check
- Source integrity: removed two cited Raw Sources and multiple related concept links that do not exist in the current vault
- Attribution: retained Karpathy's raw-to-Wiki compilation, query filing, health checks, use cases, and `~100 articles / ~400K words` personal deployment report
- Generalization boundary: the disclosed scale is one case, not an embedding-search threshold; `10-15 pages` and near-zero maintenance are source claims, not independently demonstrated performance guarantees
- Operational correction: cross-references, contradiction flags, and complete synthesis are maintenance goals, not automatic properties
- Confidence: `high` → `medium`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify MOC-Knowledge Management`, `/verify RAG vs Compiled Wiki`

## [2026-08-29] verify | MOC-Knowledge Management

- Page verified: [[MOC-Knowledge Management]]
- Eligibility: added definition claim type, mixed-source scope, linked sources, confidence, verification metadata, and Bias Check
- Link integrity: removed five direct Wiki links with no current target (`Persistent Knowledge Base`, `Contamination Mitigation`, `Sovereign PKM`, `Harness Literacy`, `Synthetic Data Generation for Wiki`)
- Preservation: retained those names as unmaterialized candidates rather than inventing pages or silently discarding the knowledge gaps
- Tool wording: changed qmd from a broad "Karpathy recommendation" to the local Markdown search tool used by this vault
- Confidence: unset → `medium`
- Verification status: `unverified` → `partial`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify RAG vs Compiled Wiki`, decide candidate creation only when evidence and reuse justify it

## [2026-08-29] verify | financial-order-latency-lab

- Page verified: [[financial-order-latency-lab]]
- Eligibility: changed the non-schema `project-evidence` claim type to `mixed`, added current verification metadata, Core Context evidence, Verification Boundary, and Bias Check
- Repository check: the public GitHub repository currently contains the Python server/load generator, result directory, run commands, and README values baseline `25.60 ms`, gpu-scoring `45.11 ms`, combined `48.36 ms`, and disk-pressure proxy `10.95 → 1.49`
- Reproduction boundary: this verification did not rerun the Windows 11/GTX 1060 experiment, so measurement reproducibility and causal bottleneck interpretation remain partial
- Contribution boundary: repository artifacts do not establish personal implementation; the latest user-confirmed [[Core Context]] says AI performed the p99 setup, code, execution, and re-execution and the user did not independently verify them
- Confidence: `high` → `medium`
- Verification status: remains `partial`
- `explored: true` preserved; `disputed: false`
- Follow-up: directly reimplement and rerun a minimal Java/Linux experiment before portfolio promotion

## [2026-08-29] verify | 시장중립은 무위험이 아니다

- Page verified: [[시장중립은 무위험이 아니다]]
- Eligibility: expanded the AI-only source into mixed evidence with a current SEC filing, Federal Reserve stability analysis, and OCC delta-neutral definition
- Consistency: confirmed market neutrality targets measured general-market exposure but does not guarantee removal of style, industry, short-position, leverage, liquidity, or execution risk
- Delta boundary: OCC defines delta neutrality around incremental underlying-price sensitivity; it is not identical to regression beta neutrality or a persistent risk-free state
- Leverage boundary: the Federal Reserve documents how leveraged funds can be forced to sell into stressed liquidity, so low measured directionality does not make high leverage safe
- Confidence: `low` → `high`
- Verification status: `unverified` → `verified`
- `explored: false` preserved; `disputed: false`
- Follow-up: `/verify 변동성 트레이딩과 델타 헤징`, `/verify 백테스트 과적합과 편향`

## [2026-08-29] verify | LLM Wiki core operations batch

- Pages verified: [[3-Layer Architecture]], [[Ingest-Query-Lint Cycle]], [[RAG vs Compiled Wiki]], [[LLM Wiki as Learning Base]], [[Agent-Readable Metadata]], [[Human-AI Knowledge Boundary]], [[Mothership-Satellite Vault Pattern]], [[Schema Engineering for LLM Wiki]]
- Current architecture: confirmed six Raw Source subfolders and the Codex priority `AGENTS.md` → `.agents/skills/` → `.codex/commands/`; Claude files remain legacy mirrors
- Source preservation: replaced absolute immutability wording with Original Content preservation plus explicit ingest/source-update exception
- Scale calibration: treated `10-15 pages` and `~100 articles / ~400K words` as Karpathy examples, not local targets or universal search thresholds
- RAG boundary: clarified that retrieval systems can persist outputs and compiled Wikis can use retrieval; neither side automatically guarantees synthesis, contradiction detection, or scale
- Human boundary: agent verification updates `verificationStatus` but never flips `explored: true` without explicit user confirmation
- Standalone boundary: confirmed `operationMode: standalone` and `source-vault: null`; mothership behavior remains an inactive design
- Verification results: [[3-Layer Architecture]] and [[Schema Engineering for LLM Wiki]] → `verified`; the other six → `partial`
- Follow-up: verify tooling guides and entity/history pages against current primary sources

## [2026-08-29] verify | LLM Wiki tooling and history batch

- Pages verified: [[Andrej Karpathy]], [[Vannevar Bush]], [[Memex]], [[qmd]], [[Obsidian Tooling for LLM Wiki]], [[Web Clipper to Inbox Workflow]], [[Citation Manager Integration for LLM Wiki]]
- Primary sources: added Karpathy's official site and GitHub, Bush's 1945 Atlantic essay, current qmd README, and official Obsidian Web Clipper/Graph documentation
- Link integrity: removed nonexistent Sovereign PKM, contamination, synthetic-data, kepano, and persistent-knowledge page links while retaining supported ideas as attributed prose where useful
- Historical boundary: separated Bush's Memex description from Karpathy's later interpretation that agent maintenance extends it; LLMs have not "solved" Wiki maintenance automatically
- qmd runtime: upstream BM25/vector/reranking/CLI/MCP features are current, but `qmd` is absent on this Mac and repo hook/config still contain Windows path placeholders
- Web Clipper: local JSON templates and Inbox routes exist; browser-extension installation/import state was not claimed
- Citation manager: confirmed the page is an unimplemented proposal and found no current citation fields in Raw Sources or templates
- Verification results: [[Andrej Karpathy]], [[Vannevar Bush]], [[Memex]], [[Web Clipper to Inbox Workflow]] → `verified`; qmd/tooling/citation pages → `partial`
- Follow-up: install and configure qmd only if semantic retrieval is needed; test citation integration before schema adoption

## [2026-08-29] verify | LLM Wiki proposal batch

- Pages verified: [[Idea Generation Pipeline]], [[Track Classification and Research Gap Detection]], [[Personal Context Layer for LLM Wiki]]
- Implementation boundary: confirmed that idea generation, `track` metadata, and `$idea`/`$track` skills are proposals rather than current ingest behavior
- Evidence correction: removed the unsupported `3 sources → 7 ideas` cohort measurement and the claim that more context necessarily improves idea quality
- Product boundary: replaced broad NotebookLM/RAG comparisons with a comparison between this vault's implemented workflow and an optional divergence stage
- Research-gap boundary: low track coverage now means a collection-gap candidate, not an external literature gap or PRISMA/systematic-review result
- Personal-context boundary: existing files influence an answer only when actually retrieved or selected; Graph View reflects recorded wikilinks, not the user's complete thought structure
- Verification results: all three pages → `partial`; `explored: false` preserved; `disputed: false`
- Follow-up: implement and test proposal skills before claiming automation, and externally validate important ideas or research gaps

## [2026-08-29] verify | personal self-knowledge batch

- Pages verified: [[MOC-김규태 Self Knowledge]], [[김규태 Personal Operating Manual]], [[김규태 Relationship Values]], [[김규태 Work and Learning Operating Guide]], [[김규태 Career Values and Success Vision]], [[김규태 Career Narrative]], and six linked behavior-pattern concepts
- Source check: confirmed the cited 2026-07-23 personal manual, romantic reflection, and self-understanding interview Raw Sources and their Original Content
- Evidence boundary: treated preferences, memories, and goals as user self-report; retained AI-organized patterns as interpretations rather than diagnoses or independently observed traits
- Confidence: the twelve pages now use `medium` where interpretation extends beyond literal source wording
- Leadership correction: aligned the page with the source's self-reported `우승` wording and explicitly left the result and teammate perspective independently unconfirmed
- Verification results: all twelve pages → `partial`; `explored: false` preserved; `disputed: false`
- Follow-up: update changing preferences through a new user-confirmed source and add external artifacts only where outcome claims matter

## [2026-08-29] verify | quant research and leverage batch

- Pages verified: [[AI와 머신러닝 시대의 퀀트 리서치]], [[퀀트 리서치는 가설에서 검증까지 이어지는 과정이다]], [[백테스트 과적합과 편향]], [[변동성 트레이딩과 델타 헤징]], [[자본 레버리지는 자유의 핵심 엔진이다]]
- Primary evidence: added the 2026 interagency model-risk guidance, Bailey et al.'s backtest-overfitting paper, the SEC hypothetical-performance rule, OCC/CME option materials, and SEC/ProShares leveraged-ETF disclosures
- Model-risk boundary: validation, monitoring, limitations, and governance are supported for traditional statistical and non-generative AI models; the guidance excludes generative and agentic AI from its direct scope
- Backtest boundary: overfitting and hindsight risk are supported, while the research sequence and checklist remain learning synthesis rather than a universal industry process
- Option result: delta-hedging concepts were confirmed as local first-order exposure management with gamma, theta, jumps, discrete rebalancing, and cost residuals; page → `verified`
- Personal-finance boundary: converted asset balances to a dated 2026-07-12 self-report snapshot; clarified that QLD/USD target daily multiples and that borrowing plus leveraged ETFs compounds risk
- Verification results: option page → `verified`; the other four → `partial`; `explored: false` preserved; `disputed: false`
- Follow-up: do not promote the personal investment hypothesis without current balances, cash-flow constraints, and a reproducible path-dependent backtest

## [2026-08-29] verify | career, learning, and personal strategy batch

- Pages verified: fourteen remaining career, learning, AI workflow, reading, leverage, and economic-freedom pages
- User-source boundary: career goals, English confidence, reading preferences, mentor rules, and economic-freedom strategy remain user-original or prescriptive records rather than externally proven outcomes
- Evidence correction: marked current career facts as a July-August 2026 snapshot and changed productivity, domain-value, and skill-stack language to hypotheses where no outcome measurement exists
- Project boundary: linked project pages locate evidence but do not automatically certify the user's implementation depth, productivity gain, leadership quality, or skill level
- AI factory result: Jensen Huang's energy/data-center-to-token framing was confirmed against NVIDIA's official 2024 keynote and 2025 recap; the page is `verified` as attribution, not as an independent endorsement of NVIDIA's market thesis
- Safety boundary: people are not reduced to personal leverage, and investment, career, learning, and AI automation effects remain subject to their stated evidence gaps
- Verification results: [[AI 팩토리와 토큰 생산 인프라]] → `verified`; the other thirteen → `partial`; `explored: false` preserved; `disputed: false`
- Follow-up: measure actual learning retention, AI workflow net productivity, and portfolio outcomes before raising confidence

## [2026-08-29] verify | legacy partial metadata and project boundary batch

- Pages re-verified: eleven previously partial career, learning, project, program, and owner pages
- Schema migration: replaced unsupported `project-evidence` and `identity` claim types with `mixed`; added `verifiedAt`, `verifiedBy`, and `disputed` to every legacy partial page
- Repository evidence: confirmed the current public Graduation-elasticsearch README and its repository-reported `3460 / 114 / 5486 / 3479 / 2007 / 1 / 694` summary without rerunning the parser
- CUEE boundary: confirmed a clean local `main` README with build/test commands, fixture E2E, demo artifacts, and payment safety stop; did not treat `mock-korail` as live Korail proof or AI-written Kotlin as user implementation
- Harness boundary: retained the documented workflow and user intent but lowered confidence because no local checkout exists and the public README was unavailable during this verification
- Owner correction: updated [[김규태]] toward financial Java backend/trading infrastructure and removed blanket project implementation claims; project artifacts, AI work, user decisions, and independent verification are now separated
- Verification results: all eleven remain `partial`; existing `explored` values preserved; `disputed: false`
- Follow-up: rerun project-specific builds/tests and ingest contribution artifacts before raising any project or personal-skill claim to verified

## [2026-08-29] audit | post-verification whole-vault audit

- Report updated: [[2026-08-29-Q-vault-audit]]
- Scope: 70 Wiki pages; Concepts 40, Entities 10, Guides 15, MOCs 5
- Status: `verified` 10, `partial` 60, `unverified` 0, `disputed` 0
- Eligibility: 70/70 v5 metadata, H1, source, and Related surface; YAML errors 0; invalid claim types 0
- Consistency: broken wikilinks 0, direct MOC orphans 0, deterministic material conflicts 0
- Confirmability: all 10 high-confidence pages have Bias Check; partial pages retain explicit user-report, fixture, repository, implementation, and unimplemented-design boundaries
- Vault Health: Eligibility 100, Consistency 98, Confirmability 94, Composite `97/100`
- Resolved during final sweep: removed a code-example false wikilink, connected seven MOC orphans, refreshed MOC-Portfolio's Java/AI contribution boundary, and added explicit sources to [[MOC-LLM Wiki Guide]]
- Remaining work is evidence-triggered re-verification, not an unprocessed page queue

## [2026-09-10] ingest | 계약랩 프로젝트 작업 메모

- Raw Source saved: [[2026-09-02-to-09-Kim-Gyutae-Contract-Lab-Work-Notes]]
- Collection purpose: 프로젝트 증거 — ROS 2·MAVSDK·QGroundControl 환경 구축, 드론 구동 확인, 자율착륙 판단 구조, 협업 방식, 특허 비교 과업을 포트폴리오와 면접 근거로 재사용
- Wiki page created: [[계약랩]]
- Map updated: [[MOC-Portfolio]]
- User contribution boundary: 원문에서 김규태의 명시적 개인 과업은 Figure 2 검토이며, 환경 구축·드론 구동·설계 판단의 개인 기여 주체는 추가 증거가 필요
- Verification boundary: 환경 구축과 드론 구동은 사용자 작성 메모의 자기보고이며 저장소, 명령, 로그, 영상, 시험 조건은 미확인
- Patent boundary: 유사도·차별성 비교 과업만 기록되어 있고 대상 문헌, 비교표, 신규성 판단, 출원 여부는 미확인
- Standalone mode: mothership search skipped; `mainVaultRelated` and `mainVaultCmds` left empty

## [2026-09-10] query | AI 힌트로 깊은 문제 몰입 회복

- Query saved: [[2026-09-10-Q-ai-hint-deep-problem-focus]]
- User self-report: 어려운 문제를 약 5분 이상 붙잡기 어렵고 AI로 빠르게 답을 찾는 습관 때문에 생각하는 힘이 약해진 것 같다고 느낌
- Interpretation boundary: 인지 능력 저하로 진단하지 않고, 조기 정답 요청이 독립 탐색 시간을 줄였다는 검증 가능한 가설로 기록
- Experiment: `12분 독립 시도 → 질문 힌트 → 8분 시도 → 제약·반례 힌트 → 10분 시도 → 방향 확인`을 2주간 측정
- Evidence boundary: 프로그래밍 교육의 힌트 조건 연구는 참고 근거이며, 개인 효과는 풀이 로그와 다음 날 백지 재풀이로 별도 검증
- Reuse axis: 독서/책/학습, 취업/포트폴리오, Codex 개발 워크플로

## [2026-09-11] ingest + query | 2026 넥토리얼 서류 합격 및 AI면접 준비

- Raw Source saved: [[2026-09-11-Nexon-Tutorial-AI-Interview-Preparation-Bundle]]
- Application record created: [[2026 넥토리얼 지원]]
- Query saved: [[2026-09-11-Q-Nexon-Tutorial-AI-Interview-Preparation]]
- User self-report: 2026 넥토리얼 서류전형 합격; 합격 메일 또는 MY PAGE 증빙은 아직 미첨부
- Official AI interview: 2026-09-12 오후, AI와 약 50분간 1:1 대화, 게임 프로그래머 기본기·공통역량 평가, 개인 장비 문제로 인한 재응시 불가
- Historical boundary: 넥토리얼은 2021년 시작했지만 AI면접·AI활용 역량평가는 2026년 신규 도입이므로 전년도 동일 전형 합격 후기는 없음
- Preparation focus: 제출 지원서 방어, CS·C++/C# 기본기, 게임 관점, AI 활용의 문제 정의·검증·책임, 장비 사전 점검
- Collection purpose: 취업/포트폴리오 — 서류 합격 진행 기록과 AI면접·후속 면접 준비에 재사용
- Standalone mode: mothership search skipped; `mainVaultRelated` and `mainVaultCmds` left empty

## [2026-09-11] update + reindex | 넥토리얼 지원서 대조 및 qmd 설치

- Submitted application answers added to [[2026-09-11-Nexon-Tutorial-AI-Interview-Preparation-Bundle]]; phone number, detailed address, and birth date were not duplicated
- Portfolio reviewed: 4-page PDF at the user-provided Desktop path; Threads, LLM Wiki, and CUEE claims were compared with the application
- Study plan updated: transaction/idempotency/concurrency, Threads evidence defense, C/C++·PX4 scope, data structures, and common competency stories
- qmd installed from the official npm package: @tobilu/qmd 2.8.3
- Collections configured: wiki, raw_sources, queries
- Repository qmd template and auto-reindex hook changed from stale Windows paths to the current macOS vault and npm paths

## [2026-09-11] query | 넥슨태그 기반 넥토리얼 AI면접 답변 전략

- Query saved: [[2026-09-11-Q-Nexon-Tutorial-AI-Interview-Answer-Strategy]]
- Video criteria: problem definition, structured solution process, verification, learning ability, fundamentals, communication, game motivation, and problem-solving over portfolio polish
- User-reported strengths: Codex context management, Threads feedback automation, rapid AI-assisted learning, CUEE pivot communication, and long-term MapleStory memory
- Critical weakness: no game portfolio, weak C++/C# and CS foundations, and inability to explain all AI-written code
- Positioning: do not claim AI output as implementation skill; distinguish problem definition, user feedback, team judgment, test execution, current knowledge boundary, and concrete relearning
- Repository check: current Threads checkout passed 71 unit tests, but test success was not treated as proof of user authorship or understanding
- Immediate code scope: study and rewrite extract_json and fallback_provider_chain before claiming a code-ownership improvement

## [2026-09-11] query | AI 활용 역량평가 문제 해결 템플릿

- Query saved: [[2026-09-11-Q-AI-Assessment-Problem-Solving-Template]]
- Reusable loop: 정의 → 정렬 → 분해 → 선택 → 실행 → 검증 → 제출
- Alignment correction: ask AI for omissions, errors, ambiguity, and counterexamples instead of asking only for agreement
- Ownership rule: the user selects or rejects AI suggestions using task conditions, supplied data, and test results
- Efficiency rule: reduce meaningless turns through bundled constraints, fixed output formats, scoped edits, and smallest-risk-first verification
- Scoring boundary: token count is not recorded as a confirmed direct scoring criterion

## [2026-09-11] query | 넥토리얼 지원동기와 게임 답변 정리

- Query saved: [[2026-09-11-Q-Nexon-Tutorial-Motivation-and-Game-Answers]]
- Motivation axis: 겨울에 형제들과 메이플스토리를 즐긴 기억을 다른 이용자에게 오래 남는 경험을 돌려주고 싶다는 개발 동기로 연결
- Skill boundary: 게임 프로젝트와 C++·C# 실전 숙련도 부족을 인정하고, C 자료구조 수업과 Python 알고리즘 학습을 출발점으로 설명
- AI learning evidence: Gemini Gem을 정답 생성기가 아닌 단계별 힌트 교사로 사용한 자물쇠와 열쇠 사례를 `막힘 → 질문 → 직접 적용 → 검증`으로 구성
- Overclaim correction: 오래 플레이한 개인 경험을 전체 이용자 요구의 증거로 확대하지 않고, 이용자 의견과 행동 데이터를 함께 확인하는 태도로 조정
- Technical correction: Python이 1초에 항상 1억 번 연산한다는 고정 가정을 사용하지 않고, 입력 크기·알고리즘 복잡도·실행 환경을 함께 판단하도록 기록
- Evidence boundary: 학습 기록과 구현물은 독립 확인되지 않은 사용자 자기보고이며 게임 개발 구현력의 대체 증거가 아님

## [2026-09-11] query update | 넥토리얼 7~26번 자가답변 진단

- Query updated: [[2026-09-11-Q-Nexon-Tutorial-AI-Interview-Answer-Strategy]]
- Strong areas: 모르는 범위를 인정하는 태도, CUEE 방향 전환, Threads 포맷 가설, 모르는 질문 대응
- Critical misconceptions: stack/heap과 stack/queue 혼동, process/thread 정의 부족, TCP handshake와 DB 동시성·중복 거래 처리 혼동
- AI evidence gaps: 실제 AI 오류 발견 사례, 직접 설명·재작성 가능한 함수, 생산성 전후 측정, fallback 테스트 29개의 구체 범위
- Portfolio number boundary: 제출 포트폴리오의 fallback 테스트 29개와 현재 checkout 전체 테스트 71개를 구분
- Immediate sequence: race condition → transaction/lock → idempotency, stack/heap → pointer/reference, 자물쇠와 열쇠 백지 재풀이, fallback 함수·테스트 인수
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-12] query | 넥토리얼 모의면접 1차 학습 기록

- Query saved: [[2026-09-12-Q-Nexon-Tutorial-Mock-Interview-Session-1]]
- Passed: 동일 아이템 동시 구매, 응답 유실과 idempotency, transaction atomicity
- Partial: stack/heap의 수명은 일부 이해했지만 heap 소유·해제, memory leak, dangling pointer, queue와의 구분을 추가 학습해야 함
- Introduction assessment: 메이플스토리의 어린 시절 기억은 강한 동기지만 반복을 줄이고 왜 기획자가 아닌 프로그래머인지 보강해야 함
- Remaining queue: 대표 프로젝트, AI 오류·검증, 협업, C++/C#, 자료구조, OOP/SOLID, 동시성, network, 게임 분석, 빠른 학습 경험
- Resume point: 왜 게임 기획자가 아니라 게임 프로그래머인가
- Reuse axis: 취업/포트폴리오, 독서/책/학습

## [2026-09-12] ingest | Java·Spring Boot·AWS 금융 포트폴리오 기초 학습 선언

- Raw Source saved: [[2026-09-12-Kim-Gyutae-Java-Spring-AWS-Study-Declaration]]
- Collection purpose: 취업/포트폴리오·프로젝트 증거·백엔드/성능/금융 시스템·독서/책/학습 — 금융 포트폴리오 프로젝트를 시작하기 전에 Java·Spring Boot·AWS 기초를 쌓고, 이후 질문과 공부 노트에서 반복되는 약점을 추적해 직접 설명·수정·검증 가능한 구현력으로 전환
- New guide: [[김규태 Java-Spring-AWS 금융 포트폴리오 기초 학습 트랙]]
- Core Context update: 두 Spring Boot 교재의 병렬 학습을 현재 중심 학습 트랙으로 설정
- Portfolio bridge: 책 예제 복제와 완독률은 구현력 증거로 보지 않고, 최소 예제 재작성·JUnit 실패 조건·로그 기반 오류 추적·자기 말 설명을 통과한 내용만 미래 Java 금융 주문 시스템 증거로 승격
- Weakness tracking: 같은 원인이 두 번 나타나면 반복 약점 후보, 재시험에서도 실패하면 우선 보완 약점으로 기록
- Initial verification boundary: 실제 질문·코드·테스트 로그가 아직 없으므로 Java·Spring Boot·AWS 세부 약점과 병렬 학습 속도는 미확정
- Standalone mode: mothership search skipped; `mainVaultRelated` is empty and `mainVaultCmds` is null
- Qmd status: Wiki 1 new·2 updated, Raw Sources 1 new, Queries unchanged; keyword index updated successfully, 149 unique hashes still need vector embedding
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-12] ingest | Gemini Lauren Tan 에이전트 강연 대화

- Raw Source saved: [[2026-09-11-Gemini-Lauren-Tan-Agent-Lecture-Chat]]
- Original file: `C:/Users/kym70/OneDrive/Desktop/New chat.md`
- Collection purpose: 독서/책/학습 — 이후 AI agent 팀 구조, 검증 gate, memory/context 관리 주장을 공부하기 위한 원문 보존
- Related pages: [[AI 자동화는 개인 생산성 레버리지다]], [[AI 보조 엔지니어링은 생성보다 검증이 중요하다]], [[Human-AI Knowledge Boundary]]
- Verification boundary: 직접 확인 가능한 강연 URL·발언 원문·소속 근거가 없고, `SpaceXAI`, agent 수, PR 수 등의 주장을 독립 확인하지 않음
- Compilation decision: 사실성이 확인되지 않아 새 Wiki claim으로 승격하지 않고 Raw Source만 생성
- Standalone mode: mothership search skipped; `mainVaultRelated` is empty and `mainVaultCmds` is null
- Reuse axis: 독서/책/학습, Codex 개발 워크플로

## [2026-09-12] private ingest + query | 넥토리얼 AI면접 응시 복기

- Application page updated: [[2026 넥토리얼 지원]] — AI면접 응시 완료·결과 대기
- Public summary: 사용자 자기보고 기준 6개 주 질문, 답변별 최대 3개 꼬리질문, 질문당 약 5분 여유, 전체 40분 이내 종료
- Broad learning gaps: C++·C# memory/container, 요구 연산 기반 자료구조 선택, 확장 가능한 damage rule, monster entity update, 2D spatial query, TCP와 거래 정합성 구분
- Confidentiality boundary: GitHub repository를 private로 전환한 뒤 실제 문항·답변 원문은 `10. Raw Sources/`, 상세 평가는 `30. Queries/`의 표준 layer에 보관; 향후 public 전환 전 제거·검토 필요
- Evidence boundary: 진행 방식과 기술 영역은 사용자 면접 직후 복기이며 공식 문항·채점 기준·결과는 미확인
- Reuse axis: 취업/포트폴리오, 독서/책/학습

## [2026-09-12] ingest update | AI면접 recursion 꼬리질문과 표준 layer 이동

- Raw Source moved: `90. Private/10. Raw Sources/` → [[2026-09-12-Nexon-Tutorial-AI-Interview-Recollection]] in `10. Raw Sources/15. Clippings/`
- Query moved: `90. Private/30. Queries/` → [[2026-09-12-Q-Nexon-Tutorial-AI-Interview-Retrospective]] in `30. Queries/`
- Added recollection: 깊은 recursion이 이어질 때 call stack이 어떻게 동작하는지 묻는 추가 꼬리질문
- Technical correction: 호출마다 stack frame이 쌓이고 base case 이후 역순으로 제거되지만, depth가 지나치면 stack exhaustion과 stack overflow가 발생할 수 있음
- Mitigation: iterative conversion, explicit container, recursion-depth limit; C++ tail-call optimization은 보장으로 가정하지 않음
- Repository boundary: GitHub visibility remains private; these files must be reviewed before any future public transition
- Search maintenance: stale qmd collection paths and hard-coded macOS hook path were replaced with the current Windows collection paths and a repository-relative hook path
- Qmd status: BM25 indexed 147 files successfully (Wiki 72, Raw Sources 45, Queries 30); first vector build was stopped after partial progress because CPU embedding was long-running, leaving 130 documents pending for a later `/reindex`
- Reuse axis: 취업/포트폴리오, 독서/책/학습

## [2026-09-13] query | 은행권 백엔드 인턴·신입 준비도 진단

- Query saved: [[2026-09-13-Q-bank-backend-entry-readiness-gap]]
- Current hiring evidence: 2026년 우리은행 TECH, 신한은행 디지털·ICT, 하나은행 체험형 AI·ICT 공고의 Java·SQL·CS·코딩테스트·배치·졸업요건 비교
- Public pass cases: 2025년 KB국민은행 IT, 2025년 하나은행 디지털·ICT, 2026년 하나은행 AI·ICT 인턴 후기의 프로젝트·인턴·코딩테스트·자격증 조합을 편향 경계와 함께 정리
- Primary gap: 학점이나 TOEIC보다 Java·Spring·SQL로 직접 구현하고 CS 원리·실패 조건을 설명·수정·테스트하는 독립 백엔드 증거가 부족함
- Timeline correction: 2027년 8월 졸업예정자에게 맞지 않는 2026년 하반기 신입 목표를 2026년 동계~2027년 상반기 체험형 인턴과 2027년 자격 적합 신입·채용연계형 인턴으로 조정
- Role boundary: 은행 IT가 입사 즉시 순수 백엔드 배치를 보장하지 않으므로 영업점 순환, OJT와 실제 배치 정책을 공고별로 확인
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-13] query | Java 은행 백엔드 대표 포트폴리오 설계

- Query saved: [[2026-09-13-Q-java-bank-transfer-ledger-portfolio-design]]
- Selected project: `Reliable Bank Transfer Ledger Lab` — 동시 요청·중복 요청·중간 장애에도 출금·입금·원장 정합성을 보존하는 Java 계좌이체 시스템
- Why this project: 은행 계정계·코어뱅킹과 직접 연결되며 현재 부족한 Java·Spring·SQL·transaction·concurrency·testing 증거를 한 저장소에서 만들 수 있음
- Scope boundary: 로그인·프론트엔드·실제 은행 API와 초기 Kafka·Redis·Kubernetes·MSA를 제외하고 계좌·이체·원장·멱등성·대사에 집중
- Verification spine: rollback, 동시 출금, 동일 멱등성 키 재시도, 인덱스 전후 `EXPLAIN`과 p95·p99 실험
- Portfolio spine updated: 기존 증권 주문 중심 후보를 은행 계좌이체·거래원장 첫 버전으로 좁히고 증권 주문은 후속 확장으로 이동
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-13] query update | Spring Boot 4 교재 기반 탑다운 구현·학습 구조

- Query updated: [[2026-09-13-Q-java-bank-transfer-ledger-portfolio-design]]
- Top-down path: 계좌이체 요청의 API→Controller→Service→domain→repository→MySQL transaction→응답 전체 흐름을 먼저 세우고 막힌 개념만 아래로 학습
- Book mapping: 00~06장과 부록 A~C를 첫 MVP에 즉시 적용하고, 07장 Thymeleaf·08장 Spring AI·09~11장 인증은 연기, 12~13장 AWS·CI/CD는 로컬 정합성 완성 후 적용
- First implementation: Spring 없이 `Account`, `TransferService`, `InsufficientBalanceException`과 JUnit으로 정상 이체·잔액 부족·잘못된 금액을 먼저 검증
- Vertical stages: pure Java domain → Spring account API → MySQL/JPA → transfer happy path → rollback → concurrency → idempotency → reconciliation → index/performance → deployment
- Learning ownership: 기능마다 완료 문장·불변조건·실패 테스트·최소 구현·SQL 확인·개념 보강·직접 설명·AI 경계 기록을 반복
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-18] query | 현재 장학금·해외·금융/개발·해커톤 기회 지도

- Query saved: [[2026-09-18-Q-current-scholarship-global-hackathon-opportunity-map]]
- Eligibility filter: 한국장학재단 9구간을 중위소득 200% 초과~300% 이하로 적용하고, 3·6·8구간 이하 장학 및 국민취업지원 I유형 현금수당을 제외
- Highest funded global option: GNU–UNLV 7주 AI·창업 프로그램의 883만원 지원, 약 594만원 개인부담, 학기 잔여 요건을 분리 기록
- Active portfolio set: 핀테크 아이디어, 금융상품 포트폴리오, Data+AI, AI Championship, PAC, GovTech, Startup Water와 교내 협업 프로그램 정리
- Work-experience set: 경남신용보증재단, 백엔드, 금융 QA, NC AI, 클라우드 보안 등 미래내일 일경험을 일정·직무 적합성 기준으로 비교
- Timing boundary: 즉시 지원, 조건부, 소득 9구간 제외, 마감·졸업요건 제외, 다음 모집 감시 대상으로 분리
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 제품/창업, 경제적 자유/FIRE/레버리지

## [2026-08-31] query update | NICE 문항 1~4 만점 대비 증거 점검

- Updated: [[2026-08-31-Q-nice-scholarship-essay-evidence-map]]
- Grade trend verified: 누적 3.68/4.5·전공 3.52·백분율 91.8, 최근 정규학기 3.82 → 3.42 → 3.59 → 4.10; `계속 상승`이 아니라 하락 뒤 두 학기 연속 회복으로 표현
- Learning method added: 먼저 풀이, 정답 금지, 단계별 힌트, 시간복잡도·엣지케이스·데이터 흐름 검토, Pythonic 코드 비교를 수행하는 Gemini Gem 학습 루틴
- Harness framing strengthened: Threads 자동화를 게시물 형식·주제·실험군별 반응을 다음 생성에 반영하는 self-evolving feedback loop로 정의
- Startup chronology corrected: 2026-05-27 GNU 개척리더스 창업 아이디어톤 최우수상 → 2026-06-16 경남권 심화교육 대상 → 2026-08-11 G-대학생 창업유망팀 동아리 챌린지 우수상
- Remaining critical gap: 5월 경쟁사 분석 지적 뒤 6월 대상 전까지 실제로 바꾼 슬라이드·분석·의사결정과 본인의 주도 행동
- Source boundary: CMDSPACE 구요한 대표의 관련 공개 강연은 확인했으나 사용자가 말한 KIST 공식 유튜브 영상은 검색으로 확인하지 못해 채널 소속 표현은 보류

## [2026-08-31] query update | NICE 사업목적·진로 정합성과 문항별 보강

- Updated: [[2026-08-31-Q-nice-scholarship-essay-evidence-map]], [[김규태 Motivation and Execution Pattern]], [[cuee]]
- LLM Wiki positioned as a sustainable learning and knowledge-connection habit for question 1, not as data-analysis experience
- Career bridge established: AI system building → reaction-data feedback → interest in decisions based on evidence → financial data analyst
- Eligibility framing: past Threads data action, software/database foundation, explicit financial-data career goal, and NICE-to-portfolio plan
- Question 2: drafted a 2M/3M semester budget linked to attendance, credentials, education, Threads analysis, and an Upbit public-data project; free public API distinguished from cloud/storage costs
- Question 3: added three 1:1 mentoring sessions, competitor matrix, real-time in-context assistance differentiation, and team-lead responsibilities; mentoring dates and missing competitor image remain unresolved
- Question 4: repeated response patterns treated as stronger but still non-causal evidence
- Algorithm example: Programmers `자물쇠와 열쇠` selected; actual sticking point, hint, and user-written resolution still require confirmation

## [2026-08-31] query update | U300+ 진행 상태·경쟁사 비교·알고리즘 막힘 보강

- Updated: [[2026-08-31-Q-nice-scholarship-essay-evidence-map]], [[cuee]], [[코딩테스트는 AI 시대의 문제해결력 훈련이다]]
- Attachments preserved: [[2026-08-31-CUEE-competitor-analysis.jpg]], [[2026-08-31-U300-plus-mentoring-program.jpg]], [[2026-08-31-U300-plus-events-and-festival-review.jpg]]
- Mentoring chronology: U300+ 첫 1:1 멘토링일은 사용자 확인 2026-06-25; 2026-06-16 경남권 대상 이후이므로 대상 수상의 원인으로 표현하지 않음
- Competitor matrix: `실시간 실제 상황 보조 / 교육·학습 기반 접근 / 물리적 대면 거래 창구`로 동일 평가축을 적용한 발표자료 확인
- U300+ status: 사용자는 전국 400팀 선정, 온라인 전시관 등록·전시, 2026-08-11 오프라인 네트워킹 데이 참여, 학생창업 페스티벌 최종 40팀 심사 대기를 보고; 화면 증거와 자기보고 범위를 분리
- Algorithm evidence: `자물쇠와 열쇠`에서 90도 회전과 배열 경계 예외처리에 막혔고, Gemini의 Python list comprehension 회전 패턴을 보고 회전 로직을 쉽게 적용했다는 자기보고 추가
- Verification boundary: 최종 40팀 선정은 미확정, 경쟁사표는 포지셔닝 자료이지 성능 우위 검증이 아님, 배열 경계처리 최종 해결·전후 코드는 미확인
- System page updated: [[index]]
- Reuse axis: 취업/포트폴리오, 제품/창업, 독서/책/학습

## [2026-09-01] query | 소프트웨어개발론 학기 프로젝트 주제 선정

- Query saved: [[2026-09-01-Q-software-engineering-semester-project-selection]]
- Inputs: 2026 가을학기 소프트웨어개발론 강의계획서, [[Core Context]], [[Graduation-elasticsearch]], 퀀트 검증 Wiki 페이지
- Decision: 1순위 무인기 임무 디지털 스레드·안전 추적성 플랫폼, 2순위 Upbit 공개 시세 기반 맞춤형 적립식 정책 시뮬레이터
- Scope boundary: 실제 드론 비행과 자동 실거래를 MVP에서 제외하고, 8주차 시뮬레이션 데모와 12주차 검증 결과를 목표로 설정
- Evidence boundary: AI 기여와 직접 구현·수정·검증 범위를 주별로 분리 기록
- System page updated: [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술

## [2026-09-01] query | 최신 추적성 기술 학기 프로젝트 선정

- Query saved: [[2026-09-01-Q-emerging-traceability-technology-selection]]
- Research: 2024~2026 LLM trace-link, GraphRAG requirements compliance, heterogeneous graph transformer 논문과 관련 GitHub 저장소 비교
- GitHub observation: 2026-09-01 API 기준 GraphRAG 35,760, LangGraph 40,806, Neo4j 17,173, Qdrant 34,302 stars; stars는 변동하며 품질 근거가 아닌 관심도 신호로만 사용
- Decision: 지식 그래프 + embedding 후보 검색 + LLM 근거 생성 + 사람 승인의 경량 GraphRAG형 trace-link 추천기
- Scope boundary: GNN 학습, 완전 자율 agent, Microsoft GraphRAG 전체 pipeline, 실제 비행 제어, blockchain 제외
- Feasibility gate: 8주차까지 수동 trace graph·embedding top-k·승인 UI 완성, 12주차 baseline 대비 precision/recall/F1와 검토시간 평가
- Updated: [[2026-09-01-Q-software-engineering-semester-project-selection]], [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술
## 2026-09-01

- NICE 장학금 증거 지도에 Threads 공개 shortcode와 숫자형 API ID의 본문 대조 결과, 독자 참여율 정의, NICE 교육으로 이어지는 분석 간극을 추가했다.
- `Graduation-elasticsearch`에서 직접 구현과 결과 해석을 분리하고, unresolved 원인과 개선안이 아직 재실행되지 않았다는 경계를 반영했다.
## [2026-09-01] query | NICE 자기소개서 5문항 일관성 감사

- Query saved: [[2026-09-01-Q-nice-scholarship-five-question-coherence-audit]]
- Narrative spine: 질문·축적·실험의 학습 변화 → 데이터 분석 흥미 → 금융 데이터 분석가 → NICE 역량 보완 → 금융 서비스에 분석을 반영하는 금융 IT 인재
- Major risks: 1번의 2024~2025 시간축 부족, 2번 예산 현실성, 4번 당시 결정과 사후 분석 혼동, 5번 직접 구현·개선 완료 과장
- Duplication rule: Threads 활동은 1번에서 한 문장, 2번에서 미래 결과물, 4번에서 분석 과정, 5번에서 현재 수준으로 역할 분리
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술
## [2026-09-01] query update | NICE 증빙자료·3년 학습축·예산 확정

- Created Desktop evidence bundle: `NICE_장학금_증빙자료_2026-09-01`
- Threads: 72시간 독자 참여율 열, 확인 가능한 동일 패턴 초기·후기 비교표, SVG·PNG 차트, 미수집값·교란요인 목록 생성
- Corrected Threads signal: 2026-09-01 사용자 제공 화면과 72시간 CSV가 일치하며 7월 15일 글은 좋아요 19, raw replies 3(작성자 체인 3, 독자 답글 0), 재게시 8이다. 화면에만 있는 공유 2는 과거 CSV 비교식에서 제외한다.
- JavaParser: 1쪽 분석요약과 통합 증빙 작성; 교수의 높은 unresolved 비율 피드백 뒤 원인·개선 방향을 README에 정리했다는 사용자 확인 반영
- Learning timeline: 2024~2025 전통 학습 → 2025-1 전공 5과목·3.42 → 2025-2 AI 활용 시작·3.59 → 2026-1 Gemini Gem 설명·재검증 루틴·4.10
- Budget: NICE 일정에 따라 이동비를 학기당 35만 원으로 분리하고, 2026-09-01 표시가 기준 공공데이터 과정 66,000원, AB 테스트 49,500원, 금융 백테스트 Part1·2 각 99,000원, SQLD·ADsP 응시료 각 50,000원을 반영했다. 행사 개최지와 결제가는 추후 재확인한다.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술

## [2026-09-01] query | NICE 자기소개서 5문항 1차 초안

- Query saved: [[2026-09-01-Q-nice-scholarship-essay-draft-v1]]
- Draft bundle: Desktop `NICE_장학금_증빙자료_2026-09-01`에 `10_Threads_직접검산_가이드.md`, `11_NICE_자기소개서_1차초안.md` 추가
- Ambiguity decision: 행사 장소는 미확정이므로 특정 IDC센터·도시를 쓰지 않고 `NICE 행사`로 표현; 공식 성적증명서와 최신 일정·비용은 제출 전 확인
- Direct verification: 7월 15일 게시물의 독자 참여율은 `(19+0+8+0)÷2,456×100=1.10%`; 작성자 체인 답글과 화면에만 존재하는 공유 수를 비교식에서 제외
- Character limits: 1번 373/500자, 2번 약 794/1,000자, 3번 447/500자, 4번 448/500자, 5번 448/500자
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 학부연구생/학술

## [2026-09-01] query | Upbit 금융 의사결정 추적성 프로젝트 재설계

- Query saved: [[2026-09-01-Q-upbit-financial-decision-traceability-project]]
- User correction: 수동 trace graph·embedding·LLM 승인 조합은 기존 기술 재구현처럼 보여 독창성이 부족하다는 지적 반영
- Market boundary: Upbit가 Strategy Toolkit으로 자연어 전략 JSON과 백테스트를 이미 제공하므로 동일 기능을 핵심 차별점으로 삼지 않음
- Decision: 사용자 의도 → 전략 버전 → point-in-time 시장 snapshot → AI/규칙 제안 → risk gate → 사람 승인 → test/paper order를 `Decision Receipt`로 연결
- Emerging technology: OpenTelemetry GenAI agent observability, append-only hash-linked provenance, deterministic/counterfactual replay
- Scope boundary: 실제 자금 자동매매, 수익 예측 모델, GraphRAG, vector DB, blockchain, multi-agent 제외
- Feasibility gate: 8주차에 BUY/HOLD receipt와 한 가지 counterfactual replay 데모, 12주차에 결정 재현·중복 주문·hash 변조·미래 데이터 누수 테스트
- Updated: [[2026-09-01-Q-emerging-traceability-technology-selection]], [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 백엔드/성능/금융 시스템, 프로젝트 증거

## [2026-09-01] query | 팀 회의용 학기 프로젝트 2안

- Query saved: [[2026-09-01-Q-team-meeting-two-project-proposals]]
- Proposal A: `TracePilot AI` — Agentic Digital Thread와 Temporal Knowledge Graph 기반 무인기 요구사항·시험 추적
- Proposal B: `WhyBuy` — Decision Provenance, hash-linked receipt, counterfactual replay 기반 Upbit 적립식 결정 추적
- Presentation rule: 각 안은 문제·사용자·headline 신기술·8주차 데모·범위 위험을 동일 형식으로 90초 설명
- Decision rule: 사용자 접근성 30, 8주차 데모 25, 팀 흥미 20, 포트폴리오 15, 신기술 검증 10으로 익명 평가
- Scope rule: headline 기술 1개와 stretch 기술 1개만 유지
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 프로젝트 증거

## [2026-09-01] query | WhyBuy 최신 핀테크 기술 선정

- Query saved: [[2026-09-01-Q-whybuy-agentic-finance-technology-selection]]
- Trend: Google AP2, Visa Trusted Agent Protocol, Mastercard Agent Pay, x402의 agentic payments·agent authorization 흐름 비교
- GitHub observation: 2026-09-01 API 기준 Google AP2 3,164, x402 6,562 stars; 관심도 신호로만 사용
- Decision: AP2의 signed Mandate를 투자에 변형한 `Verifiable Investment Mandate`를 WhyBuy headline 신기술로 선정
- Core chain: 사용자 서명 mandate → 시장 snapshot → strategy proposal → deterministic policy/risk gate → Decision Receipt → 사람 승인 → Upbit test/paper order
- Scope boundary: AP2 전체 구현, x402/stablecoin, blockchain, 실제 자동 주문, 자체 암호 알고리즘, 가격 예측 제외
- Stretch: OpenTelemetry GenAI observability, passkey UX, counterfactual replay, receipt hash chain
- Updated: [[2026-09-01-Q-upbit-financial-decision-traceability-project]], [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 백엔드/성능/금융 시스템, 프로젝트 증거

## [2026-09-02] query | 학기 프로젝트 아이디어 구체화 및 팀 설명서

- Query saved: [[2026-09-02-Q-semester-project-concrete-team-brief]]
- Clarification: traceability를 `결과까지의 원인·권한·증거 연결`로 정의하고 WhyBuy와 TracePilot의 공통점과 차이를 초심자 관점에서 재설명
- Recommended default: signed Investment Mandate, deterministic risk gate, Decision Receipt, replay를 핵심으로 하는 WhyBuy
- Research design: 일반 JSON 설정·로그를 baseline으로 두고 위반 차단, 변조 탐지, 중복 주문, 결정 재현, 원인 탐색 시간을 평가
- Scope gate: 실제 자동매매·가격 예측·blockchain 제외, 8주차 core flow 이후에만 LLM·counterfactual 기능 추가
- Alternative gate: 실제 무인기 자료와 피드백 사용자 2명 이상을 확보할 수 있으면 TracePilot 재검토
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템

## [2026-09-02] query | 외부 데이터 없는 추적성 프로젝트 재선정

- Query saved: [[2026-09-02-Q-traceability-project-reselection-without-domain-data]]
- Trigger: 무인기 데이터 부재와 WhyBuy 문제 이해·확신 부족으로 기존 양자택일을 보류
- Recommended: issue/acceptance criteria → AI run → changed files → tests → human review → signed build를 연결하는 `TraceForge`
- Emerging technology: development 단계의 OpenTelemetry GenAI agent conventions를 headline으로, SLSA/GitHub artifact attestation을 stretch로 선정
- Data strategy: 외부 산업 데이터 대신 팀 자신의 GitHub issue, PR, commit, check run, AI trace를 학기 동안 축적
- Research design: 일반 GitHub 화면·자유형 AI 로그를 baseline으로 원인 탐색 시간, 답변 정확도, gap 탐지 precision/recall, trace overhead 비교
- Alternative: 시각적 일반 사용자 제품을 선호하면 C2PA Content Credentials 기반 `OriginLens`
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-02] query | Upbit 주문 추적성 프로젝트 재설계

- Query saved: [[2026-09-02-Q-upbit-order-traceability-project-redesign]]
- User correction: AI 코드 변경 추적성은 기각하고 Upbit API와 추적성이 함께 핵심이 되는 금융 프로젝트로 재탐색
- Recommended: signal → market snapshot → risk check → paper order state → execution → incident report를 연결하는 `OrderScope AI`
- Emerging technology: read-only MCP forensic tools, evidence-event ID를 강제한 LLM structured diagnosis, OpenTelemetry형 end-to-end trace
- Upbit verification: 2026-09-02 공개 API로 `KRW-BTC` 30단계 호가와 최근 체결 데이터를 인증 없이 수신 확인; 실제 주문은 제외
- Evaluation: 다섯 장애를 각 10회 주입해 raw-log baseline 대비 macro-F1, evidence precision, 원인 파악 시간, replay 상태 일치율, p95 측정
- Portfolio: 주문 상태 머신, idempotency, WebSocket gap, event sourcing/replay, 장애 대응과 금융 backend 설계 증거
- Updated: [[2026-09-01-Q-upbit-financial-decision-traceability-project]], [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 백엔드/성능/금융 시스템, 프로젝트 증거

## [2026-09-02] query | 3인 팀 Upbit·무인기 추적성 최종 2안

- Query saved: [[2026-09-02-Q-three-person-upbit-drone-traceability-proposals]]
- Team constraint: 3명·12주·8주차 AI 비의존 end-to-end demo·실제 자금/기체 없음으로 공통 범위 설정
- Proposal A: `OrderScope AI`를 KRW-BTC 한 페어, paper OMS, 장애 4종, MCP evidence diagnosis로 축소
- Proposal B: `FlightProof Twin`을 PX4 SIH가 생성한 ULog와 failure injection 기반 Executable Digital Thread로 재설계
- Drone data fallback: lightweight SIH를 기본으로 직접 생성하고, setup 지연 시 CC-BY PX4 public ULog를 fixture로 사용
- Research: OrderScope는 raw log 대비 장애 진단 macro-F1·시간, FlightProof는 full regression 대비 selective retest recall·시간을 비교
- Decision gate: 1주 spike로 Upbit 호가 저장/paper replay와 PX4 SIH ULog 고도 추출 중 완료도가 높은 안 선택
- Updated: [[2026-09-01-Q-team-meeting-two-project-proposals]], [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 백엔드/성능/금융 시스템, 학부연구생/학술

## [2026-09-02] query | Graphify 기반 무인기 추적성 적합성 판단

- Query saved: [[2026-09-02-Q-graphify-fit-for-traceability-project]]
- Attribution: Karpathy는 더 넓은 LLM Wiki 패턴을 제안했고 Graphify는 그 문제의식에서 영감을 받은 별도 오픈소스 구현으로 구분
- Decision: Graphify를 단순 시각화 도구가 아니라 PX4 requirement·contract·ULog evidence용 domain adapter의 기반 엔진으로 채택
- Product rename: `FlightProof Twin`을 `FlightGraph — Graphify 기반 PX4 실행형 안전 추적성 플랫폼`으로 구체화
- Original contribution: typed UAV nodes/edges, EXTRACTED/INFERRED/AMBIGUOUS 승인 정책, 변경 영향 기반 selective retest
- Baselines: 수동 trace matrix와 vanilla Graphify를 함께 비교해 domain extension의 trace F1·impact recall·재시험 시간·검토 비용 측정
- Scope boundary: 4개 안전 요구사항, 단일 SIH mission, 최대 40회 실행; real drone·ROS 2·GNN·Enterprise formal verification 제외
- Updated: [[2026-09-02-Q-three-person-upbit-drone-traceability-proposals]], [[index]]
- Reuse axis: 강의/수업/교육, 취업/포트폴리오, 학부연구생/학술, 프로젝트 증거

## [2026-09-03] query | 개발자 취업 공부 첫 4주 계획

- Query saved: [[2026-09-03-Q-developer-job-preparation-starting-plan]]
- Priority: 자격증·광범위한 강의보다 Java 구현, SQL 실습, 코딩테스트, 검증 가능한 작은 주문 API를 먼저 수행
- Four-week output: Java 문제 20개, SQL 문제 30개, 주문 생성·조회·취소 API와 자동 테스트, 공고 10개 요구역량 표
- Decision gate: 4주 뒤 직접 재풀이·수정·설명 가능성과 공고 격차를 근거로 금융 백엔드 적합성을 다시 판단
- Reuse axis: 취업/포트폴리오, 독서/책/학습, 백엔드/성능/금융 시스템

## [2026-09-03] query | 코딩테스트에서 실제 개발로 넘어가는 법

- Query saved: [[2026-09-03-Q-from-coding-tests-to-software-development]]
- Diagnosis: 문법·함수 구현보다 요구사항, 구조, 상태, 데이터, 테스트, 변경의 전체 개발 주기 경험이 부족한 상태로 해석
- Practice ladder: Java 콘솔 주문 프로그램 → Spring Boot API → DB 연결 → 중복·상태 전이·동시성 실패 처리
- Learning unit: 기능 한 개마다 완료 조건 작성, 직접 구현, 정상·경계·실패 테스트, commit, 다음 날 변경까지 수행
- First-week output: Order 모델·상태, 메모리 repository, 생성·조회·취소 service, JUnit 테스트, README와 2분 설명
- Reuse axis: 취업/포트폴리오, 독서/책/학습, 백엔드/성능/금융 시스템, 프로젝트 증거

## [2026-09-03] query | 경상국립대 장학금·인턴·지원기회 지도

- Query saved: [[2026-09-03-Q-gnu-scholarship-internship-opportunity-map]]
- Immediate priorities: The(더)자람 등록·포인트 확인, 푸른등대 NICE 제출, 희망사다리Ⅰ 의무종사 판단
- Career priority: 다음 현장실습학기제에서 Java·금융 IT·반도체 데이터·우주항공 SW 기업을 우선 탐색
- Project option: 국립공원 위성 모니터링 AI 챌린지는 범위를 제한할 때만 포트폴리오 후보
- Excluded: 자격 불일치 장학금, 이미 마감된 공고, 전공 연결이 약한 지원금 중심 활동
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 학부연구생/학술

## [2026-09-03] query | The(더)자람 활용과 2027년 1학기 인턴 계획

- Query saved: [[2026-09-03-Q-the-jaram-and-2027-spring-internship-plan]]
- Existing evidence: cuee 수상은 교외 공모전 50점 가능성이 높고, 취업동아리·연구·TMU·멋사 활동은 공식 주관·발표 여부에 따라 조건부
- Strong point sources: 공인영어 150~300점, 기사 200점, 15주 인턴십 450점, 학회·세미나 발표 50점
- Stage caveat: 2027년 8월 졸업예정자는 2027년 상반기 4단계 추가선발을 확인하고 변경될 최소 포인트 기준을 재검증해야 함
- Internship plan: 학교 현장실습과 기업 직접지원을 병행하고 Java/Spring·금융 IT·드론 SW·반도체 데이터 직무를 우선
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 학부연구생/학술

## [2026-09-07] query | 넥토리얼 게임 프로그래밍 지원서 1차 설계

- Query saved: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Positioning: 게임 경력 과장 없이 문제 분해·프로젝트 실행·AI workflow를 게임 프로그래밍 성장 가능성으로 연결
- Essay evidence: CUEE 방향 전환과 경쟁 분석, 실패 공개와 재도전, Python 기반 harness·Threads 자동화
- Guardrail: AI 작성 코드를 본인 C/C++·C#·엔진 구현 경험으로 표현하지 않음
- Required facts: 학력 월, 대학 입학 유형, 언어·엔진 실제 숙련도, 게임 지원동기, 직접 작성한 코드와 기술 문제
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-07] query update | Actions 장애 검증과 자기소개서 1차 초안

- Screenshot diagnosis: reserve chain 부재 → 게시 단계 미실행 → verify의 post_missing → daily objective failure
- GitHub Actions audit: 2026-08-27~2026-09-06 최근 공개 run은 모두 failure; end-to-end 해결 주장 제외
- Final material split: 2번은 Threads 포맷 실험과 반응 증가, 4번은 AI 코드 검토·provider fallback·단위 테스트·미해결 장애 경계
- Drafted: 지원동기, 프로젝트 문제 해결, 솔직한 피드백, AI 활용 역량 4문항 1차 초안
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거

## [2026-09-07] portfolio verification | 4페이지 PDF 재생성 및 시각 검수

- Final: `C:\Users\user\Desktop\김규태_개발_포트폴리오.pdf` (4 pages, about 484KB)
- Verified: 표지 통합 카드, Threads, LLM Wiki, CUEE 페이지의 잘림 없음과 원격 CUEE 이미지 로딩 확인
- Compatibility: 기존 PDF 파일명도 동일한 최신 HTML로 다시 출력해 구버전 업로드 위험을 줄임
- Reuse axis: 취업/포트폴리오

## [2026-09-07] query update | fallback·CI 오류·비동기 주장 검증

- Fallback precision: OpenRouter 실패 시 Groq provider의 `openai/gpt-oss-120b` 모델을 사용하는 코드와 테스트 확인
- Boundary: 실제 운영 발동 없음, 29개 단위 테스트 통과, 현재 workflow의 `LLM_FALLBACK_PROVIDER`는 비활성 값
- CI self-report: `Daily publication objective was not verified`, exit code 1 이후 Auto Publish workflow 수정·단위 테스트 시도; 현재 코드에서 과거 오류 문자열과 수정 diff는 미확인
- Async boundary: 논문 크롤링 비동기화 자기보고와 달리 현재 Python 코드에서 asyncio/ThreadPool 구현을 찾지 못해 제출본 보류
- Principle: 실패 조건을 먼저 묻고 fallback·재시도·예외처리를 설계하는 개발 태도를 중심 메시지로 채택
- CUEE clarification: 팀은 위기의식에 동의, 한 명이 경쟁사 분석 담당, PPT 개선 뒤 후속 대회 성과
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-07] query update | Threads 코드·fallback·성과 검증

- User judgment: 일반 논문 팁에서 `실수→나쁜 결과→나쁜 예시→좋은 예시` 포맷으로 변경
- AI collaboration: AI가 시작점·코드 완성을 제안하고 사용자가 의도 확인·선택·수정; 50:50은 사용자 자기평가
- Repository evidence: OpenRouter→Groq provider fallback과 테스트 존재, `tests.test_generate_auto_thread` 29개 통과
- Boundary: fallback 구간은 현재 미커밋이며 실제 운영 전환 여부·작성 주체 미확인; 비동기·동시성 구현은 검색에서 미확인
- Metrics: 사용자 기억은 좋아요 100+·재게시 약 40; 현재 CSV 최대는 좋아요 67·재게시 26·조회 11,349로 불일치
- Recommended allocation: 2번 Threads 운영 장애, 4번 Gemini Gem·AI 공동 코딩 원칙
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-07] query update | 넥토리얼 포트폴리오·수상·서사 옵션

- Recommended portfolio: Threads Agentic Editor Workflow, CUEE, Graduation-elasticsearch
- Excluded: 직접 설명·재현이 어려운 financial-order-latency-lab; harness는 Threads workflow의 보조 근거로 결합
- English level: TOEIC 730 L/R과 TMU 일상 영어 경험을 고려해 `의사소통 가능` 권장, 비즈니스 회화는 보류
- Awards verified from images: 2026-05-27 GNU 개척리더스 창업 아이디어톤 최우수상, 2026-06-16 경남권 창업동아리 심화교육 대상
- Essay options: AI-Augmented Developer, 사용자 경험·제품 전환, 시스템·성능 성장, 도구·파이프라인 개발
- Recommended narrative: AI-Augmented Developer를 중심으로 CUEE 사용자·팀 경험을 보조
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-07] query update | A안 공식 요건 대조와 문항 재배치

- Official source: https://www.nexon-tutorial.com/
- Correction: C++/C# 개발 가능은 기본요건이며 게임 포트폴리오는 선택; 2027-02 졸업요건과 사용자의 2027-08 기록 불일치로 지원 가능 단정 철회
- Evidence map: 1번 학습법·직무 동기, 2번 Threads 운영 개선, 3번 CUEE 솔직한 피드백, 4번 harness·지식 공유
- Gaps: 실제 게임 동기, 본인 코드 변경·검증 사례, 피드백 전달 내용과 상대 반응
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]], [[index]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거

## [2026-09-07] query update | 자비스·메이플스토리·Threads·CUEE 상세 반영

- JARVIS: 2025-2 팀 활동, Arduino 드론 자율주행 목표, AI 보조 PX4-Autopilot 수정, MAVLink·Pixhawk 모터 제어, 미테스트·현재 설명 곤란
- Coding test: 프로그래머스 Level 2 어려운 문제와 Level 3 쉬운 문제에 도전; `자물쇠와 열쇠` 회전·경계처리에서 Gemini 힌트 활용
- Game motivation: 메이플스토리 교환창·자유시장의 이용자 거래 경험에서 거래소·경매장·재화 흐름 개발 관심으로 연결
- Threads assessment: 공식 AI 활용·구조적 사고·자동화와 정합성이 높아 4번 핵심역량 우선 소재, 문제 해결 문항에는 포맷 선택 근거·수치 추가 필요
- CUEE: 모두의 창업 탈락 후 팀에 위기의식을 전달하고 수익구조·경쟁사 분석을 보완했다는 자기보고 추가
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로

## [2026-09-07] query correction | 교내 드론 동아리 C 경험

- Correction: NSquare 관련 경험은 지원서에서 제외
- C evidence candidate: 교내 드론 동아리에서 C를 사용한 개발 경험
- Required details: 동아리명·기간·드론/보드·직접 작성한 기능·AI 기여·실행 또는 시험 결과
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거

## [2026-09-07] query update | 메이플스토리 동기와 NSquare C 경험 후보

- Game motivation: 메이플스토리에서 유저 간 재화·아이템 거래로 생기는 상호작용에 흥미
- Desired work: 유저 간 상호작용 시스템과 개발 생산성 자동화 도구
- C evidence candidate: NSquare 관련 드론 활동에서 일부 사용했다고 자기보고했으나 Wiki·로컬 자료에서 미확인
- Next verification: NSquare 활동명·기간·직접 작성한 C 기능·AI 기여·실행 결과
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거

## [2026-09-07] query update | C·CS 학습 수준과 지원서 소재 정정

- C experience: 컴퓨터프로그래밍·자료구조 수업에서 사용한 수준
- Algorithms: 자료구조 수업 이후 Python 코딩테스트 준비를 통해 별도 학습 중
- Removed: 학점 소재와 새 C++ 프로젝트 준비 서사
- Current gaps: 게임 프로그래밍 지원동기, C 수업의 직접 구현 과제, 코딩테스트 풀이 수준
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거
## [2026-09-07] query update | 넥토리얼 알고리즘·드론 증거와 지원 자격 재확인

- Algorithm evidence: Gemini Gem의 단계별 힌트와 Python 컴프리헨션 회전 예시를 참고하되 직접 코드를 다시 작성해 Programmers `자물쇠와 열쇠` 통과
- Threads metric linkage: 새 문제·예시 포맷의 게시물이 좋아요 67·재게시 26을 기록했다는 사용자 확인
- Drone evidence: 공개 영상 `GNU campus autonomous flight with PPO algorithm #1`에서 PPO 자율비행 시뮬레이션 결과 확인; 코드 저장소가 없어 PX4 코드 기여는 자기보고 범위
- Eligibility warning: 2027-08 졸업예정 상태에서 졸업유예는 공식 `2027-02 졸업예정` 요건을 충족시키지 않으므로 채용 담당자 확인 필요
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거
## [2026-09-07] query update | Threads 전후 지표와 CUEE 수익모델 전환

- Threads self-report: 포맷 변경 전 좋아요 2·댓글 7, 직후 좋아요 63·재게시 28·전송 32, 이후 좋아요 100 이상 게시물 3개
- Verification boundary: 로컬 CSV 확인 범위와 사용자 자기보고 수치가 달라 제출 전 원본 화면 또는 내보낸 데이터 확인 필요
- CUEE feedback: 심사위원의 지불의사 질문에 사용자도 동의하고, B2C 건별 결제에서 개인 무료·기업 제휴 CPS 구조로 전환 제안
- Claim boundary: `이탈률 50% 감소`는 실제 사용자 검증 여부가 확인되기 전까지 목표 가설로 기록
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거
## [2026-09-07] query update | LLM Wiki AI 활용 역량과 CUEE 출시 상태

- Essay 4 pivot: Threads fallback 중심에서 여러 에이전트에 공통 맥락·증거·검증 규칙을 제공하는 LLM Wiki 운영 역량으로 교체
- Wiki evidence: `AGENTS.md`, `Core Context`, Raw Sources/Wiki/Queries 구분과 지속적 사용자 맥락 갱신
- Concrete use: 넥토리얼 지원서에서 저장된 근거와 실제 코드를 대조해 수치·기여 범위 과장을 제거
- CUEE: 코레일톡 KTX 예매 보조 앱, 초기 건별 결제에서 개인 무료·기업 CPS 구조로 전환, 현재 Play Store 심사 중
- Boundary: `이탈률 50% 감소`는 팀 목표치이며 사용자 실측 결과가 아님
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]], [[cuee]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로
## [2026-09-07] portfolio | 넥토리얼 게임 프로그래밍 제출용 PDF 생성

- Output: `C:\Users\user\Desktop\김규태_넥토리얼_게임프로그래밍_포트폴리오.pdf` (5 pages, about 505KB)
- Projects: Threads AI automation, personalized LLM Wiki, CUEE; CS/PX4 growth evidence and public links included
- AI boundary: user decisions, AI contributions, verified results, and unresolved limitations are separated
- Survey recommendation: select only `툴·파이프라인 개발`; deselect `서버·백엔드` and `멀티스레드·병렬 프로그래밍` under current evidence
- Source: `30. Queries/2026-09-07-nextorial-portfolio-kim-gyutae.html`
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로
## [2026-09-07] query correction | 넥토리얼 자기소개서 최종 사실성 점검

- Essay 1: `자물쇠와 열쇠` 풀이에서 불필요하고 설명 위험이 있는 방문 여부 표현을 제거하고 배열 경계·회전 로직으로 한정
- Essay 4: 복수의 일반 AI agent 표현을 실제 사용 범위인 서로 다른 Codex 세션으로 구체화하고 CUEE 맥락 재사용 사례 추가
- Language correction: C# 실제 사용 경험 없음으로 정정
- Attribution correction: GitHub fork 메타데이터가 없으므로 포트폴리오의 `fork` 표현을 제거하고 구요환/CMDSPACE 공개 패턴 기반 개인화로 표현
- Remaining required facts: 고등학교 입학·졸업 월, 대학교 입학 연월·입학 유형
- Updated: [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거
## [2026-09-07] portfolio revision | 범용 포트폴리오 4페이지 압축과 자기소개서 Markdown 생성

- Removed: 표지의 넥슨·넥토리얼·게임 프로그래밍 표기와 게임 지원동기, 별도 검증·경계·출처 박스, 마지막 FIT/GROWTH 페이지
- Merged: CS 기본기·PX4 기존 코드 경험·Links를 표지에 통합
- Project cards: Threads 검증/경계, LLM Wiki 출처/기여, CUEE 검증 경계를 기존 역할 카드에 병합
- Added: [[2026-09-07-Q-nextorial-self-introduction-final]]
- Updated: `30. Queries/2026-09-07-nextorial-portfolio-kim-gyutae.html`, [[index]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거
## [2026-09-07] portfolio revision | 프로젝트 역할·기여·기술 스택 가독성 강화

- Cover: 문구를 `김규태 포트폴리오`로 단순화하고 CS·PX4 경험 블록 제거
- Added: Threads, LLM Wiki, CUEE의 프로젝트 유형·담당 역할·기여·기술 스택 요약표
- Project pages: 각 페이지 상단에 유형·역할·기여·기술 스택 메타 바 추가
- Reuse axis: 취업/포트폴리오

## [2026-09-07] application revision | 거래 검증 자동화·솔직한 피드백·개발 문서화

- 1번: 거래 등록·구매·취소 검증 및 오류 기록 수집 도구를 희망 기여로 명시하고 C/C++ 기반 PX4 기존 코드 수정 경험 반영.
- 3번: CUEE를 노인의 앱 사용 길잡이로 설명하고 매몰비용에도 솔직하게 피드백해 방향을 수정하는 배움 반영.
- 4번: 기술적 결정·제품 요구사항 문서의 중요성, 사실과 가정 구분, 최소한의 명확한 맥락 관리 원칙 반영.
- Updated: [[2026-09-07-Q-nextorial-self-introduction-final]], [[2026-09-07-Q-nextorial-game-programming-application-draft]], [[index]]
- Character counts: 1번 922자, 3번 460자, 4번 445자. 2번 유지.
## [2026-09-07] application revision | 메이플스토리 실시간 거래 경험 구체화

- 1번 도입을 교환창에서 메소·아이템이 실시간으로 정확히 이전되는 경험으로 수정.
- 거래 중 연결 단절·중복 요청에서도 누락·중복 지급을 막는 관심을 거래 테스트·오류 기록 자동화 목표와 연결.
- Updated: [[2026-09-07-Q-nextorial-self-introduction-final]], [[2026-09-07-Q-nextorial-game-programming-application-draft]]
- Final character count: 1번 979자.
## [2026-09-08] ingest | UAV 정밀착륙 특허 3건 파일럿과 연구 중심축

- Purpose: 학부연구생/학술·프로젝트 증거 — 정밀착륙 관련 연구·특허 조사와 학기 프로젝트의 지속적 지식 축적
- Source: [[2026-09-08-UAV-precision-landing-patent-search-pilot]]
- Patent samples: `WO2019036361A1`, `US20170308100A1` / `US10423167B2`, `CN110221625A` / `CN110221625B`
- Updated workbook: `C:\Users\user\Desktop\4. 관련연구조사 - AI_ML 활용 SW.xlsx` 특허 시트 5~7행
- Backup: `C:\Users\user\Desktop\4. 관련연구조사 - AI_ML 활용 SW - backup-before-2026-09-08.xlsx`
- Created: [[MOC-UAV 정밀착륙 연구]], [[UAV 정밀착륙 특허 검색 가이드]]
- Mothership links: standalone mode, not applicable
- Caution: Google Patents legal status is a discovery aid; jurisdictional registers remain authoritative
- Reuse axis: 학부연구생/학술, 프로젝트 증거, 드론 도메인 탐색
## [2026-09-08] ingest | EvolvingTraceDB Neo4j 로컬 그래프 구축 검증

- Purpose: 학부연구생/학술·프로젝트 증거 — JavaParser 테스트-소스 추적 링크의 Neo4j 적재·재현 결과를 논문·랩미팅·포트폴리오에 재사용
- Source: [[2026-09-08-EvolvingTraceDB-Neo4j-local-build-record]]
- Created: [[EvolvingTraceDB Neo4j 구축 및 검증 가이드]]
- Updated: [[Graduation-elasticsearch]], [[index]]
- Evidence: Neo4j Browser 스크린샷 4장과 각 조회 Cypher를 `80. References/Attachments/`에 보존
- Verified result: `CODE 4,215`, `ISSUE 547`, `API_DOCUMENT 97`, `TEST_FILE 92`, `SOURCE_FILE 245`, `MODIFIES 52`, `EXPLAINS 34`, `TESTS 693`
- Gap: 694개 후보 중 `MultisearchBody.java` 1개 미매칭; path-contains-test 분류의 false positive 가능성 유지
- Mothership links: standalone mode, not applicable
- Reuse axis: 학부연구생/학술, 프로젝트 증거, 취업/포트폴리오

## [2026-09-08] query | 정밀착륙 특허 적합성과 팀 실험 루프

- Decision: 5번 의미 아이콘 방식을 단일 RGB 카메라·LANDING_TARGET 기반 기준선으로 선정
- Expansion: 4번 학습 객체·장애물 판단을 결합하고 3번 자연 특징 방식을 후속 비교군으로 설정
- Team boundary: 재완 `.plan`, 관호 인식 모델, 규태 SITL/Gazebo 통합·평가
- Control ownership: QGC/MAVSDK는 미션, ROS는 표적 관측, PX4는 착륙 제어 담당
- Added: [[2026-09-08-Q-precision-landing-patent-fit-and-team-loop]]
- Updated: [[MOC-UAV 정밀착륙 연구]], [[index]]
- Reuse axis: 학부연구생/학술, 프로젝트 증거, 실험 설계
## [2026-09-08] query correction | LANDING_TARGET 신뢰도와 비교 계층 구분

- Corrected: MAVLink `LANDING_TARGET`에는 별도 confidence 필드가 없으며 `position_valid`와 전송 중단으로 유효성을 표현
- Internal contract: ROS에서 pose·confidence·variance·timestamp를 유지하고 임계값 통과 관측만 PX4에 전달
- Comparison boundary: ArUco·semantic icon·YOLO·natural feature는 perception 비교, PX4·PID·RL은 controller 비교
- Updated: [[2026-09-08-Q-precision-landing-patent-fit-and-team-loop]]
- Reuse axis: 학부연구생/학술, 프로젝트 증거, 실험 설계

## [2026-09-08] query | 실리콘밸리 기회를 위한 학부생 LinkedIn 전략

- Finding: LinkedIn Recruiter의 직함·위치·학교·언어·skills·keyword 검색 구조를 기준으로 검색 적합성 우선
- Positioning: `경험 없는 학생`이 아니라 학부연구·리더십·교육·프로젝트 판단을 가진 early-career developer로 표현
- Evidence boundary: AI 생성 코드와 본인 판단·수정·검증 범위를 분리하고 GitHub·영어 README·측정 결과로 연결
- Added: [[2026-09-08-Q-linkedin-silicon-valley-student-strategy]]
- Updated: [[index]]
- Reuse axis: 취업/포트폴리오, 개발 도메인 영어, 글로벌 인턴 준비

## [2026-09-08] query edit | NICE 자기소개서 1번 AI 학습 표현 수정

- Removed: `2학기부터 AI를 쓰기 시작했다`는 사용 시점 중심 표현
- Revised: Gemini Gem을 정답 대신 단계별 힌트를 주는 튜터로 설정한 행동 중심 표현
- Updated: [[2026-09-01-Q-nice-scholarship-essay-draft-v1]]
- Verified: 1번 본문 공백 포함 342자, 500자 제한 충족
- Reuse axis: 취업/포트폴리오, 장학금 자기소개서

## [2026-09-08] query | NICE 장학생 선발 경쟁력 기준

- Official structure: 1차 가계소득 20점+성적 80점으로 3배수, 2차 자기소개서 100점으로 10명 선발
- Applicant estimate: 9구간에서 `91.8`이 직전학기 백분위일 때만 예상 88.04점
- Correction: `91.8`이 누적성적 백분율인지 직전학기 백분위인지 기존 기록이 충돌해 조건부 점수로 수정
- Added: [[2026-09-08-Q-nice-scholarship-selection-benchmark]]
- Updated: [[2026-08-31-Q-nice-scholarship-essay-evidence-map]], [[index]]
- Reuse axis: 취업/포트폴리오, 장학금 자기소개서

## [2026-09-09] query | NICE 자기소개서 1~4번 재구성

- 1번: 성적 상승 중심을 제거하고 Gemini Gem 질문, LLM Wiki 축적, Threads 실험의 세 키워드로 재구성
- 2번: 교통·식비를 68만 4,500원·70만 2,000원으로 낮추고 현재 Upbit 주문 추적 프로젝트의 개발·분석·검증·배포 산출물에 예산 확대
- 3번: `모두의 창업` 최종 심사의견과 사용자 자기보고를 바탕으로 개인 유료에서 개인 무료+B2B CPS로의 수익모델 전환 및 경남권 대상 연결
- 4번: 독자 참여율 계산식을 제거하고 가설 설정·데이터 비교·행동 수정 구조로 변경
- Evidence added: [[2026-09-08-CUEE-modoo-final-review.jpeg]]
- Added: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]]
- Updated: [[cuee]], [[2026-09-01-Q-nice-scholarship-five-question-coherence-audit]], [[index]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 장학금 자기소개서

## [2026-09-09] query edit | NICE 자기소개서 1·2·4번 2차 조정

- 1번: Gemini Gem의 코딩테스트 알고리즘 학습, 3.42→4.10 회복, LLM Wiki 기록을 Upbit 주문 추적 프로젝트에 재사용한 사례 추가
- 2번: 두 학기 모두 3개월 교통·식비 60만 원으로 통일하고 진로·프로젝트 배분을 140만 원·240만 원으로 확대
- 4번: `Threads 자동화 워크플로를 개발하면서`로 개발 맥락을 명확히 표현
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]], [[2026-09-01-Q-nice-scholarship-five-question-coherence-audit]], [[2026-08-31-Q-nice-scholarship-essay-evidence-map]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 장학금 자기소개서

## [2026-09-09] query | NICE 1기 합격자 특징·자소서 조사와 1번 연결성 진단

- Evidence boundary: 2025년 합격자 10명의 개인 스펙과 자기소개서 원문은 공개 자료에서 확인되지 않아 실제 공통점으로 단정하지 않음
- Official 2025 structure: 1차 소득 30점+성적 70점, 2차 자기소개서 100점, 진솔성·논리성·성실성·성장가능성·목적부합성 각 20점
- 2026 change: 1차 소득 20점+성적 80점으로 성적 비중 확대, 최종은 자기소개서 100점 유지
- Q1 diagnosis: 세 키워드의 개별 증거는 강하지만 현재는 병렬 사례에 가까워 `질문→축적→가설 실험→다음 행동 수정`의 인과 연결을 보강할 필요
- Added: [[2026-09-09-Q-nice-2025-winner-pattern-research]]
- Updated: [[index]]
- Reuse axis: 장학금 자기소개서, 취업/포트폴리오

## [2026-09-09] query | NICE 무자격증·무데이터수상 선발 준비도 감사

- Verdict: 경쟁력 있는 초안이지만 최종 10명 목표의 제출본으로는 미완성; 내부 모의점수 81/100(공식 합격점 아님)
- Strongest: 현재 역량·부족한 역량의 솔직한 구분, 학기별 장학금과 결과물 연결
- Weakest: 1번의 3년 증거와 세 키워드 인과, 4번의 분석 시점·효과값, 5번의 직접 분석 주체성
- Priority: Threads 시간 경계와 수치 보정 → 직접 분석 산출물 강화 → 질문·축적·실험 연쇄화 → 학기당 대표 결과물 집중 → CUEE 다음 검증 행동 추가
- Added: [[2026-09-09-Q-nice-no-certification-selection-readiness-audit]]
- Updated: [[index]]
- Reuse axis: 장학금 자기소개서, 취업/포트폴리오, 프로젝트 증거

## [2026-09-09] query edit | NICE 자기소개서 1~4번 선발형 재구성

- 1번: 질문→축적→실험→다음 행동 수정의 인과관계로 재작성
- 2번: 대표 결과물을 2026-2 Threads 분석 보고서, 2027-1 Upbit 주문 장애 분석 결과물로 학기당 하나씩 고정
- 3번: 개인 유료 이용 거부 이유, 개인 무료+B2B CPS 전환, Google Play 출시 후 실제 데이터 검증 추가
- 4번: 초기 형식 채택과 사후 52개 분석을 분리하고 중앙 참여율 1.01%→0.37%, 교란요인, 통제된 다음 실험을 포함한 논의용 문안으로 수정
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]], [[2026-09-01-Q-nice-scholarship-five-question-coherence-audit]]
- Reuse axis: 장학금 자기소개서, 프로젝트 증거

## [2026-09-09] query correction | NICE 5번 JavaParser 기여 경계와 교육 필요성

- Database PBL: `jungsan`은 A0 이수 프로젝트지만 전체 코드가 AI 작성이라 직접 구현 증거에서 제외
- Classification audit: 현재 Java 4,215개 중 실제 `src/test` 153개, `path contains test` 171개, `src/main` 소스 오분류 18개를 로컬 검증
- User contribution: AI 보고의 153·171 불일치를 발견하고 기준 재검토를 요청한 판단, unresolved 비율의 원형 그래프 표현 요구
- AI boundary: JavaParser 코드·재계수·README·도표는 AI 작성, `unresolved_calls.csv` 2,008개 행은 사용자 직접 미검토
- Q5 rewrite: 자격증·관련 수상 부재, 교육 이수, 분류 이상 발견, 현재 한계, Python·Pandas 금융 데이터 분석과 금융 백엔드 진로를 444자에 연결
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]], [[Graduation-elasticsearch]], [[2026-08-31-Q-nice-scholarship-essay-evidence-map]], [[2026-09-01-Q-nice-scholarship-five-question-coherence-audit]]
- Reuse axis: 장학금 자기소개서, 프로젝트 증거, 학부연구생/학술

## [2026-09-10] query | NICE 다섯 기준 최신 재채점

- Verdict: 수정된 2차 초안은 사용자가 제시한 다섯 기준에서 내부 모의점수 `88/100`(공식 합격점 아님)
- Improved: 질문→축적→실험 인과, 학기당 한 결과물, CUEE 후속 검증, Threads 1.01%→0.37%와 교란요인으로 이전 81점보다 개선
- Strongest: 현재 역량과 부족한 역량의 솔직한 구분, 장학금과 학기별 결과물 연결
- Remaining gap: 본인이 직접 재현한 Threads 분석물, 통제된 후속 실험, Upbit 최소 실행물, 예산 단가 근거
- Added: [[2026-09-10-Q-nice-five-criteria-readiness-rescore]]
- Updated: [[2026-09-09-Q-nice-no-certification-selection-readiness-audit]], [[index]]
- Reuse axis: 장학금 자기소개서, 취업/포트폴리오, 프로젝트 증거

## [2026-09-10] query edit | NICE 초안 직접 분석·CUEE 성과 반영

- 1번: 3.42→4.10이 누적 평점이 아니라 학기 학점임을 명시
- 3번: 큐를 시니어용 실시간 화면 안내 오버레이 비서 앱으로 설명하고 경남권 대상 뒤 U300+ 전국 400팀 선정을 추가
- 4번: 52개 원자료를 Python·Pandas로 직접 정제해 동일한 72시간 관측기간으로 비교했다는 수행 주체와 방법을 명시
- Consistency fix: 2번은 완료된 Threads 분석의 고도화로 수정하고, 5번은 기초 정제·비교 가능과 통계적 검정·금융 분석 부족을 구분
- Evidence boundary: 후속 비교 실험, Upbit 최소 실행물, 예산 근거는 완료 자기보고 상태이며 세부 결과·산출물 확인 전
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]], [[2026-09-10-Q-nice-five-criteria-readiness-rescore]]
- Reuse axis: 장학금 자기소개서, 프로젝트 증거, 취업/포트폴리오

## [2026-09-10] query + implementation | Threads 후속 형식 실험 준비

- Repository: `gyutaetae/threads-agentic-editor-workflow` 원격 `master` 최신 커밋 `5cd9f61` 확인
- Baseline reproduced: 53행 중 72시간·조회수 조건 50행, 대비 형식 32개의 초기 중앙 참여율 1.0054%·후기 0.3700%, -63.2%
- Experiment prepared: 6쌍·12개 교차 게시 계획, 대비/직접 형식 첫 문안, 분석·검증 코드, 자동 결과 보고서
- Verification: 첫 문안 총길이 차이 2.5%, 분석 테스트 `2 passed`; 새 72시간 완료 표본은 0개이므로 상태 `incomplete`
- Essay correction: 4번의 후속 실험 표현을 `진행`에서 `설계`로 수정해 완료 과장을 제거
- Added: [[2026-09-10-Q-threads-followup-experiment-and-nice-evidence-needs]]
- Updated: [[harness]], [[2026-09-09-Q-nice-scholarship-essay-draft-v2]], [[2026-09-10-Q-nice-five-criteria-readiness-rescore]], [[index]]
- Reuse axis: 장학금 자기소개서, 프로젝트 증거, 취업/포트폴리오

## [2026-09-10] query edit | NICE 제출 직전 시간축·예산 확정

- 1번: 2022-1 학기 학점 3.42, 2025-2 Gemini Gem 탑다운 질문 학습, 2026-1 학기 학점 4.10·LLM Wiki·Threads, 2026-2 Upbit 시작의 시간축 반영
- 2번 2026-2: 인프런 강의 2개 28만 원, AWS 3개월 30만 원, 멘토링 4회 32만 원, 도구·대시보드·보고서 50만 원, 교통·식비 60만 원으로 200만 원 확정
- 2번 2027-1: 인프런 금융분석·백테스트 강의 2개 28만 원, AWS 3개월 45만 원, 장애·부하환경 47만 원, 멘토링 4회 40만 원, 사용자 20명 검증 40만 원, 배포·포트폴리오 40만 원, 교통·식비 60만 원으로 300만 원 확정
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]]
- Reuse axis: 장학금 자기소개서, 프로젝트 증거

## [2026-09-10] query correction | NICE 1번 학점 시점과 3년 범위

- Corrected: 학기 학점 3.42는 2022-1이 아니라 2025-1이며, 2022-1 학기 학점은 3.61
- 1번: `지난 3년간`의 변화 방향을 먼저 제시하고 2025-1 학점 3.42를 공부법 전환점, 2025-2 Gemini 질문 학습, 2026-1 학점 4.10·Wiki·Threads, 2026-2 Upbit 시작으로 연결
- Boundary: 2022-1은 지난 3년 범위 밖이므로 자소서 본문에서 제외
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]]
- Reuse axis: 장학금 자기소개서

## [2026-09-10] NICE 제출 전 최종 점검

- 52개 원자료 중 72시간 완료 50개를 비교했음을 명시하고 후속 실험은 설계 상태 유지.
- 예산은 확인된 견적이 아닌 예상 배분으로 명시, 주문 장애는 모의 환경임을 명시.
- 학기 평점 표현과 Wiki·Threads 연결을 정리. 글자 수 461/786/471/461/430, 예산 합계 200/300만 원.
- Updated: [[2026-09-09-Q-nice-scholarship-essay-draft-v2]], [[index]]

## [2026-09-14] maintenance | 원격·로컬 Wiki 변경 통합

- 원격 `main`의 9개 커밋과 로컬 미커밋 Wiki 작업을 통합했다.
- 충돌한 프로젝트·프로필·포트폴리오 문서는 최신 원격 구조와 로컬 증거를 함께 보존하도록 병합했다.
- [[index]] 통계를 현재 파일 기준 Raw Sources 48, Wiki Pages 76, Queries 60으로 갱신했다.
- 동기화 직후 생성된 [[2026-09-14-Q-modoo-startup-second-cuee-application-draft]]를 추가 반영했다.
- 잘린 경로 문자열만 담긴 임시 파일 `30.`은 커밋 대상에서 제외했다.

## [2026-09-14] query | 한국 백엔드 업계와 금융권 업권 비교

- Query saved: [[2026-09-14-Q-korea-backend-industry-finance-sector-comparison]]
- Market boundary: 전국 백엔드 공고를 산업·언어별로 전수 집계한 공개 최신 통계가 없어 정확한 업계 1위와 언어 비율은 단정하지 않음
- Language conclusion: 한국 일반 백엔드와 금융·기업 시스템 이동성을 함께 확보하는 첫 주언어는 Java·Spring, 필수 병행 축은 SQL·RDB·테스트·Linux·네트워크
- Finance split: 전체 신입 단위는 은행이 상대적으로 크지만 순수 개발 배치가 불명확할 수 있고, 증권·핀테크·PG는 직무가 선명한 대신 소수·경력 수시채용 비중이 높음
- Sector expansion: 은행·증권뿐 아니라 보험, 카드·캐피탈, 핀테크·PG, 금융공기업·시장 인프라, 금융 IT 계열사·솔루션, 저축은행·상호금융까지 지원 지도를 확장
- Compensation boundary: 공개 평균급여는 개발자만 분리하지 않으므로 연봉·문화·워라밸은 업권 서열이 아니라 팀별 온콜·배치·시장시간·순환배치·상주·성과급 조건으로 재확인
- Reuse axis: 취업/포트폴리오, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-14] query | 한국 일반기업 백엔드 업계와 회사 선택 기준 비교

- Query saved: [[2026-09-14-Q-korea-non-finance-backend-employer-comparison]]
- Employer map: 대형 플랫폼·커머스, 대기업 IT서비스·제조 IT, B2B SaaS, 게임, 콘텐츠·교육·헬스케어, 초기 스타트업, SI/SM, 공공기관 전산으로 구분
- Compensation boundary: 2026 소규모 개발자 설문의 0~3년차 중앙 구간 4천만~5천만 원은 참고 표본일 뿐 한국 신입 평균으로 일반화하지 않음
- Selection criteria: 신입 멘토, 코드리뷰, 직접 배포·운영, 온콜 보상, 개발/운영 비율, 기술부채 개선 권한, 사업 안정성과 평가 투명성을 회사명보다 먼저 확인
- Application expansion: 금융 프로젝트를 버리지 않고 결제·정합성·성능·운영 안정성으로 번역해 대기업 IT서비스, 제조 IT와 Java 제품기업까지 지원
- Reuse axis: 취업/포트폴리오, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-14] query | 주요 금융사 Java 개발자 채용 비교

- Query saved: [[2026-09-14-Q-korea-financial-java-employer-comparison]]
- Scope: KB·우리·NH·신한·하나·IBK·카카오·케이·토스 은행과 미래에셋·KB·메리츠·한국투자·삼성·하나·키움·토스증권
- Hiring boundary: 회사별 연간 개발자 총원은 대부분 미공개이므로 2026 공개 공고의 신입 진입구, 공고상 인원, Java 직무를 분리
- Entry conclusion: IBK와 대형은행 TECH/ICT·금융 IT 계열사를 1군, 인터넷은행 신입과 증권사 신입 IT를 2군, 토스·증권 세부 경력직을 중기 목표로 구성
- Compensation boundary: 사업보고서 회사 평균급여를 신입 개발자 초봉으로 오인하지 않고 기본급·성과급·고용형태·온콜 보상 확인 항목으로 전환
- Location boundary: 본점 또는 공고상 대표 개발 거점을 기록하고 실제 팀 배치는 지원 시 재확인
- Reuse axis: 취업/포트폴리오, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-14] query update | 모두의 창업 2차 CUEE 지원서 구체화

- 목표 고객을 코레일톡 설치·자동 로그인을 마쳤지만 예매 중단 후 역 창구를 방문하는 65세 이상 Android 사용자로 좁혔다.
- 수익모델을 코레일 무료 실증 후 B2B 이용료와 이커머스 거래 귀속 후 CPS로 분리했다.
- 2026년 10월 전국 노선 입력 베타·65세 이상 5명 검증, 11월 Play 공개·코레일 제안, 12월 쿠팡 시제품 일정을 반영했다.
- 대표 주 10시간, 디자이너 각 주 10시간, 팀 주 1회 회의와 역할별 실행계획을 기록했다.
- AI 작성 코드를 실제 기기에서 검증한 범위와 Kotlin 독립 구현 역량의 한계를 분리했다.
- 10장 이미지를 Q2·Q3·Q4-1의 주장에 배치하고, 기존 19쪽 PDF에서 그대로 쓸 6쪽 경쟁사 분석과 수치·모델 충돌로 제외할 페이지를 구분했다.
- Updated: [[2026-09-14-Q-modoo-startup-second-cuee-application-draft]], [[cuee]]
- Reuse axis: 제품/창업, 프로젝트 증거

## [2026-09-15] query + implementation audit | 모두의 창업 성장성·우수성 보강

- 내부 모의평가를 준비된 증거 기준 성실성 19·성장성 27·우수성 36, 합계 82점으로 갱신했다.
- 제출 전 48시간 증거 확보안과 실제 코레일톡 45초 시연 영상 대본을 작성했다.
- 65세 이상 5명 관찰 설계, 코레일 무료 실증안, 구현 증거표를 제출 보조자료로 정리했다.
- `cuee-play-release`에서 앱 내 개인정보처리방침의 개발자 연락처와 정책 URL을 실제 정보로 수정했다.
- 수정 후 Gradle `test lint`가 성공했고 앱 JVM 단위 테스트 94개가 실패 없이 통과했다.
- 현재 제출 빌드와 소스는 `진주→서울·어른 2명·어린이 1명` 고정 데모이며 전국 노선·방언과 실제 사용자 효과는 미검증 상태로 유지했다.
- Updated: [[2026-09-14-Q-modoo-startup-second-cuee-application-draft]], [[cuee]]
- Added: `15-48-hour-score-sprint.md`, `16-modoo-demo-video-script.md`
- Reuse axis: 제품/창업, 프로젝트 증거, 사용자 검증

## [2026-09-15] evidence audit | 모두의 창업 PDF 원본 이미지 재선정

- 생성 도식 대신 기존 PDF 원본을 선호한다는 사용자 의견을 반영해 이미지 배치안을 수정했다.
- `.pdf` 19쪽 중 현재 지원서와 충돌 없이 그대로 쓸 페이지는 6쪽 경쟁사 분석으로 판단했다.
- U300+ 연계 우수상, 창업교육 20시간 수료증, 7월 마스킹·음성·안전 중단·통합 테스트 결과보고서를 고해상도 PNG로 추출했다.
- Q3-1에는 경쟁사 분석·마스킹·안전 중단, Q4-1에는 통합 테스트·우수상 원본을 우선 배치한다.
- 기존 PDF의 불명확한 통계, CPS 10%, TAM·SAM·SOM, 버스 앱 화면, 이전 로드맵과 검증되지 않은 팀 경력 페이지는 제외했다.
- Updated: [[2026-09-14-Q-modoo-startup-second-cuee-application-draft]]
- Added: `20-PDF-U300-challenge-award.png`~`25-PDF-July-integration-test-report.png`
- Reuse axis: 제품/창업, 수상·활동 증거

## [2026-09-21] ingest | 베트남 FPT Financial GraphRAG·GNU Buddy 활동 기록

- Sources: [[2026-09-21-GNU-FPT-Vietnam-GraphRAG-Program-Record]], [[2026-09-21-Kim-Gyutae-GNU-Buddy-2026-1-Record]]
- Collection purpose: 취업/포트폴리오·자기소개서·AI 프로젝트 증거·해외 협업·리더십에 재사용
- Added: [[FPT Vietnam Global Big Data AI Program]], [[GNU Buddy]]
- Updated: [[김규태]], [[MOC-Portfolio]], [[index]]
- Verified FPT facts: 공식 교육 2025-12-29~2026-01-23, FPT 수료증 2025-12-28~2026-01-24, 다낭 4주 PBL, GraphRAG 공식 프로젝트 범위, 공개 Finance GraphRAG 저장소
- Verified Buddy facts: 2026-02-25~06-11, 44.23시간, 유학생의 학교생활·한국문화 적응 지원
- Privacy: 학번·생년월일·성적 세부가 있는 GNU Buddy·TOEIC·TMU 원본은 git-ignore된 `80. References/Attachments/Private/`에 보존
- Evidence boundary: FPT 팀 구성·팀장·스크럼·타깃 설정과 GNU Buddy 개별 활동은 사용자 자기보고; 개인 코드·AI 기여 범위는 추가 확인 필요
- Mode: standalone — mothership search skipped

## [2026-09-21] update + query | FPT 기여 확정·공개 첨부 통합·GNU-UNLV 1차 초안

- FPT repository의 `gyugyu` 55개와 `kim gyutae` 1개 commit identity가 모두 김규태임을 사용자가 확인했다.
- FPT 기여 범위를 문제 정의·설계·프롬프트·생성형 AI 코드 생성·실행·Docker 공통 환경으로, 인도인 팀원의 기여를 UI로 기록했다.
- 사용자의 명시적 공개 허용에 따라 GNU Buddy, TOEIC 730, TMU Record of Study 증빙을 `80. References/Attachments/` 일반 폴더로 통합했다.
- Added query: [[2026-09-21-Q-GNU-UNLV-application-draft-v1]]
- Draft spine: FPT 국제 AI 실행 → 2026년 3월 Threads·CUEE 시작 → AI 검증·사용자 검증 격차 → UNLV 두 과목 통합 학습 → CUEE·동아리·Threads 확산
- Updated: [[FPT Vietnam Global Big Data AI Program]], [[김규태]], [[index]]
- Reuse axis: 해외 파견 지원서, AI·창업 자기소개서, 취업/포트폴리오

## [2026-09-21] query | GNU-UNLV 선발경쟁력 보강 진단

- 기존 자기소개·지원동기·학업계획서 초안은 수정하지 않았다.
- 공식 공고의 국제협력과 자격심사, 단과대학 수학능력 심사 70점 기준, IT공과대학 최대 2명, 활동실적 선택 제출과 이중 접수 요건을 재확인했다.
- Added: [[2026-09-21-Q-GNU-UNLV-selection-competitiveness-audit]]
- Highest-impact gaps: CUEE 실제 사용자 관찰, AI 결과 정확성·출처·환각 검증표, 본인 영어 발표 증거
- Immediate risks: 최종 학기 자격 해석, MY서비스·Google Form 이중 접수, 필수 서류 누락
- Reuse axis: 해외 파견 지원서, 선발 전 증빙 점검, AI·창업 포트폴리오

## [2026-09-21] update | GNU-UNLV 자기소개서 사실 보강

- Threads workflow에서 빈 논문 링크와 원문 확인 없이 자의적으로 인용한 AI 결과를 사용자가 직접 링크 대조로 발견한 사례를 기록했다.
- CUEE는 U300+ 도약과정 전국 400팀에 선정됐으나 학생창업 페스티벌 최종 40팀에는 선정되지 않은 것으로 충돌 기록을 정정했다.
- 멋쟁이사자처럼 14기 부대표로 7~8명에게 CRUD·TypeScript·Codex 사용법을 포함한 백엔드 세션을 매주 진행한 사실을 보강했다.
- Updated: [[김규태]], [[cuee]], [[김규태 Leadership and Teaching Evidence]]
- Reuse axis: 해외 파견 지원서, AI 검증, 창업·리더십, 교육 확산

## [2026-09-21] update | FPT Docker 결과·Threads 게시 후 오류 발견 확정

- FPT 다국적 팀의 Windows·macOS 환경 차이로 빌드가 실패한 뒤 Docker를 구성해 전원이 같은 명령으로 빌드·실행한 결과를 보강했다.
- Threads의 잘못된 논문 링크와 자의적 인용은 자동 게시 후 사용자가 원문 링크를 확인하며 발견한 것으로 확정했다.
- UNLV 팀 프로젝트는 별도 팀 아이디어로 수행하고, CUEE는 수업 내용을 개인적으로 적용하는 병행 프로젝트로 구분한다.
- Updated: [[FPT Vietnam Global Big Data AI Program]], [[김규태]]
- Reuse axis: 해외 파견 지원서, AI 검증, 국제 팀 리더십

## [2026-09-21] correction | Threads 근거 링크·후속 조치 정정

- 기존 기록의 `논문 링크`를 `논문 활용 콘텐츠의 참고자료로 제시된 GitHub 링크`로 바로잡았다.
- 게시 후 GitHub 링크의 404 오류와 저장소 존재 여부 미확인을 발견했고, 게시물을 삭제한 뒤 크롤링 과정을 점검하고 AI에 문제를 설명해 workflow를 수정한 것으로 기록했다.
- 구체적인 코드 변경과 예방 절차는 추후 Threads 환각·출처 검증표를 만들 때 확인한다.
- Updated: [[김규태]]
- Reuse axis: AI 검증, 해외 파견 지원서, Codex 개발 워크플로

## [2026-09-21] update | CUEE 피벗 순서·창업서포터즈 2기 보강

- 첫 모두의 창업 지원은 배우담으로 시작했으나 지원 과정 중 `실제로 노인이 사용할 것인가?`라는 질문으로 CUEE로 전환한 뒤 심사를 받아 탈락한 순서로 정정했다.
- 탈락 후 심사의견에 따라 제품개발계획, 초기 판로, 매출계획, 경쟁 서비스 분석과 사업모델을 보완한 후속 행동을 분리했다.
- CUEE는 harness로 요구사항을 분할하고 AI 구현을 지시해 실행·테스트한 개발 workflow로 기록하되 Kotlin 독립 작성으로 확대하지 않았다.
- GNU 개척리더스 창업서포터즈 2기 참여 사실을 추가하고, 실제 완료 활동 전에는 확산 채널로만 사용하도록 경계를 남겼다.
- Updated: [[cuee]], [[김규태]], [[김규태 Leadership and Teaching Evidence]]
- Reuse axis: 제품/창업, 해외 파견 지원서, 리더십·교육 확산

## [2026-09-21] query | GNU-UNLV 지원서 2차 초안

- 기존 1차 초안은 보존하고 문제해결 철학 중심 2차 초안을 별도 작성했다.
- 자기소개는 FPT Docker 공통 환경과 배우담→CUEE 전환·탈락 후 사업모델 보완을 `해결책보다 문제를 끝까지 붙드는 예비 창업가`로 연결했다.
- 지원동기는 Threads의 404 GitHub 근거 오류와 CUEE의 실제 고령 사용자 관찰 0명이라는 두 공백만 중심에 두었다.
- 학업계획서는 7주 나열을 진단·검증 설계·workflow/프로토타입·영어 발표/귀국 후 검증의 네 단계로 재구성했다.
- Planned outputs: Threads 10건 검증표, 고령 사용자 관찰표, 65세 이상 10명 예비 검증, CUEE 개선 프로토타입, 2027 창업중심대학 예비창업자 사업화 지원 자료
- Added: [[2026-09-21-Q-GNU-UNLV-application-draft-v2]]
- Reuse axis: 해외 파견 지원서, AI·창업 자기소개서, 창업중심대학 준비

## [2026-09-21] query | GNU-UNLV AI·창업 활동실적 PDF 자료 점검

- 공고의 선택 제출물 `AI·창업 등 관련 활동 실적 1부`를 7쪽 단일 PDF로 구성하는 안을 정리했다.
- FPT 수료·GraphRAG, CUEE MVP·심사의견·3회 수상·U300+·Play Console, Threads workflow, 교내 확산 자료의 기존 파일을 확인했다.
- 추가 필요 자료를 Threads 650명 프로필, 정확한 404 오류 근거, 모두의 창업 2차 제출완료, 테스트 모집 증거, 멋쟁이사자처럼·창업서포터즈 활동 증빙으로 좁혔다.
- workflow에 기록된 GitHub URL이 현재 정상 접속되고 당시 README 수집 로그도 존재해, Threads 404 사건은 정확한 URL·화면을 받기 전까지 학습 사례로만 제한하도록 [[김규태]]의 증거 경계를 보강했다.
- Added: [[2026-09-21-Q-GNU-UNLV-AI-startup-evidence-PDF-checklist]]
- Reuse axis: 해외 파견 지원서, AI·창업 활동실적, 창업 포트폴리오

## [2026-09-21] output | GNU-UNLV AI·창업 관련 활동실적 PDF

- 사용자가 제공한 Threads 632명, 모두의 창업 2차, Play Console 화면을 기존 FPT·CUEE·수상·U300+·GNU Buddy·TMU 증빙과 결합했다.
- 별도 설명문이나 표지 없이 원본 이미지 중심 10쪽 A4 PDF로 구성했다.
- Play Console 화면에서는 불필요한 계정명·계정 ID 영역을 제외하고 앱 등록 상태만 남겼다.
- 지원서의 Threads 수치는 제공된 현재 화면과 맞춰 650명에서 632명으로 정정했다.
- Output: `/mnt/c/Users/user/Desktop/GNU-UNLV_AI-창업_관련활동실적_김규태.pdf`
- Builder: `scripts/build_unlv_activity_evidence_pdf.py`
- Reuse axis: 해외 파견 지원서, AI·창업 활동실적, 창업 포트폴리오

## [2026-09-21] update | GNU-UNLV 활동실적 PDF 최종 재구성

- 상장 3종을 `대상 → 최우수상 → 우수상` 순서로 문서 맨 앞에 배치했다.
- GraphRAG GitHub 카드와 실제 코레일톡 위 CUEE MVP 화면, 기존 U300+ 활동 화면 2장을 제외했다.
- U300+ 최종선발·팀장 화면으로 교체하고 FPT 수료증, CUEE 지원·Play Console, GNU Buddy 증빙을 유지했다.
- TMU Record of Study와 Global Leadership 100 Hours, UN SDG Solutions Day 증명서까지 3종을 수록했다.
- Threads 632명 화면을 마지막 쪽으로 옮겨 이미지 전용 11쪽 PDF로 다시 생성했다.
- Output: `/mnt/c/Users/user/Desktop/GNU-UNLV_AI-창업_관련활동실적_김규태.pdf`
- Builder: `scripts/build_unlv_activity_evidence_pdf.py`
- Reuse axis: 해외 파견 지원서, AI·창업 활동실적, 창업 포트폴리오

## [2026-09-21] update | GNU-UNLV 활동실적 PDF 창업교육 증빙 추가

- 모두의 창업·Play Console 증빙 상단에 `모두의 창업 1차·2차 지원` 문구만 추가했다.
- 창업진흥원 온라인 창업교육 20시간 수료증을 Threads 직전 페이지에 삽입했다.
- 최종 문서는 이미지 기반 12쪽 PDF로 재생성하고 페이지별 이미지 포함 여부를 확인했다.
- Output: `/mnt/c/Users/user/Desktop/GNU-UNLV_AI-창업_관련활동실적_김규태.pdf`
- Builder: `scripts/build_unlv_activity_evidence_pdf.py`
- Reuse axis: 해외 파견 지원서, AI·창업 활동실적, 창업교육 증빙

## [2026-09-21] optimization | GNU-UNLV 활동실적 PDF 3MB 제한 대응

- 제출 용량 제한에 맞춰 문서를 A4 180dpi 수준, JPEG 품질 78로 재생성했다.
- 12쪽 구성과 페이지별 단일 이미지 구조를 유지하면서 최종 용량을 1,480,668바이트로 줄였다.
- 상장, U300+ 화면, 창업교육 수료증의 작은 글자 가독성을 표본 확인했다.
- Output: `/mnt/c/Users/user/Desktop/GNU-UNLV_AI-창업_관련활동실적_김규태.pdf`
- Builder: `scripts/build_unlv_activity_evidence_pdf.py`
- Reuse axis: 해외 파견 지원서, AI·창업 활동실적, 제출 파일 최적화

## [2026-09-23] create | Propeller Evidence Agent team proposal

- 실제 공개 프로펠러 시험 데이터 기반 후보 검토 에이전트의 팀 논의용 제안서를 추가했다.
- 데이터 한계, H200 지원 조건 미확인, 비교 불가 시 선정 보류, 비즈니스 가설과 검증 과제를 분리해 기록했다.
- Output: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/idea-proposal.md`

## [2026-09-23] create | GNU international student tutoring application draft

- 지원동기와 활동목표, CLIL 기반 10~12월 진단·개선·재측정 활동계획을 복사하기 쉬운 문장형으로 정리했다.
- 진단 기준을 표 대신 문장으로 바꾸고 월별 핵심 결과물을 각 2개로 유지했다.
- Output: `70. Outputs/2026-09-23-GNU-International-Tutoring/application-plan.md`

## [2026-09-23] update | Propeller Evidence Agent 평가축 및 E2E 제안 수정

- 제조현장 문제, 해결 적합성, 에이전트 배치와 E2E 자동화, 도입 경제성, 사용자 채택, 사업 가치, 대회 적합성, 심사 매력도의 8개 판단 기준을 제안서 앞부분에 추가했다.
- 전체 흐름도와 실제 측정값 예시 흐름도를 넣고, 문서 해석·오케스트레이션·검토 보고 에이전트와 Python 검증 도구의 역할을 나눴다.
- H200은 언어·비전 모델 추론과 시험문서 해석에 활용하도록 수정하고 데모 계획만 6번에 남겼으며, 기존 7~11번 내용을 삭제했다.
- Output: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent.md`

## [2026-09-23] update | 추출 신뢰성 검증 기준 보강

- 모델의 자체 확신도나 에이전트 간 합의만으로 자동 승인하지 않도록 명시했다.
- 사람 검수 표본으로 문서 필드 추출과 조건충돌 탐지 성능을 측정하고, 검증한 형식·조건 범위 밖은 담당자 검토로 넘기도록 추가했다.
- Output: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent.md`

## [2026-09-23] update | 사용 장면의 에이전트 개입과 예외 처리 구체화

- 담당자의 요청부터 오케스트레이션, 문서 조건 추출, Python 분석, 근거 보고서, 사람의 최종 확인까지 각 단계가 줄이는 일을 사용 장면 표와 흐름도에 추가했다.
- MVP의 수동 파일 업로드와 현장 데이터 연동 후의 시험번호 선택을 구분하고, 파일이 없거나 일부만 있을 때 분석 중지·부분 보고 원칙을 기록했다.
- TXT와 HDF5 형식의 역할, 오케스트레이터의 체크리스트 범위, 미확인 상황의 중단·사람 검토 절차를 설명했다.
- Output: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent.md`

## [2026-09-23] update | Propeller Evidence Agent LangGraph 선택 및 현재 평가 반영

- E2E 워크플로우 프레임워크를 LangGraph로 결정하고, 에이전트 추론과 고정된 그래프 제어·Python 계산·사람 승인의 책임을 분리했다.
- 입력 누락 확인, 문서·측정파일 병렬 처리, 조건 비교 가능성 분기, 사람 확인 후 재개, 실행 근거 보존을 적용안으로 정리했다.
- 현장 문제의 구체성, 해결 적합성, 비용·효용, 사용자 채택, 사업 가치, 에이전트 배치, 대회 취지, 심사 매력도의 8개 축으로 현재 평가를 추가했다.
- `Propeller Evidence Agent 1.md`를 이후 프로젝트 작업의 기준 문서로 지정하고 index 링크를 갱신했다.

## [2026-09-18] query | 월드잡 해외 신입 개발자 이력서 전략

- Query saved: [[2026-09-18-Q-worldjob-overseas-entry-level-developer-resume-strategy]]
- Case-study boundary: 미국 성공사례는 현지 STEM 학위·OPT, 캐나다 개발자 사례는 BCIT 과정, 독일 사례는 기존 경력이 있어 한국 학부 졸업 직행의 일반 사례로 보지 않음
- Route conclusion: 장기 선호는 미국 → 캐나다 → 유럽이지만 현재 실행 가능성은 캐나다 IEC → 미국 J-1/WEST → 독일 기회카드·직접 지원 순으로 판단
- Resume strategy: 국가 중립 공개본과 미국·캐나다·독일 지원본을 분리하고, 비자 경로·직무 증거·업무 영어·AI 검증 경계를 전면에 배치
- Updated: [[MOC-Portfolio]], [[index]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 개발 도메인 영어

## [2026-09-18] query update | 해외취업 5축 100점 준비도 설계

- Confirmed inputs: 2027년 8월 졸업예정, 졸업 후 즉시 출국 가능, TOEIC 730, Backend·QA·Data 지원 가능
- Added experience boundary: 베트남 1개월 AI 프로그램의 GraphRAG 팀 프로젝트와 갈등 회고는 확인했으나 프로그램명·기술·본인 구현·영어 사용·정량 결과는 미확인
- Current evidence-readiness estimate: 비자 4, 포트폴리오 9, 실무 적용 8, 직무 영어 11, 네트워크 7로 총 39/100
- Target design: Reliable Transaction System, Reliability Test Suite, Vietnam GraphRAG case study를 Backend·QA·Data 증거로 연결
- Updated: [[2026-09-18-Q-worldjob-overseas-entry-level-developer-resume-strategy]], [[MOC-Portfolio]], [[김규태 개발 도메인 영어 성장 계획]]
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 개발 도메인 영어

## [2026-09-26] project hub | 금융권 Java 백엔드 포트폴리오 진척 기준 수립

- Added [[financial-lab]] as the active project hub for the `financial-lab` repository and the `Reliable Bank Transfer Ledger Lab` portfolio objective.
- Recorded the inspected implementation boundary: in-memory account storage and transfer API/tests are underway; JPA persistence, database rollback, ledger, concurrency, and idempotency remain future work.
- Set the collaboration contract: the user writes implementation and test code; Codex teaches, decomposes tasks, diagnoses errors, and reviews submitted work.
- Updated [[MOC-Portfolio]] from a pre-repository candidate to an active early-stage project, marked the design Query in progress, and refreshed [[index]] counts.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-26] project milestone | 수취 계좌 미존재 이체 테스트

- Added by the user: a service test for a missing recipient account; it checks `AccountNotFoundException` and that the sender balance remains 27,000.
- Verification: `.\gradlew.bat test` completed successfully during review.
- Next: test rejection of a transfer where sender and recipient IDs are equal, including unchanged balance.
- Updated: [[financial-lab]], [[index]]
- Reuse axis: 프로젝트 증거, 백엔드/성능/금융 시스템, 취업/포트폴리오

## [2026-09-26] lint | index statistics reconciled after pull

- Reconciled [[index]] with the current inventory: 50 Raw Sources, 79 Wiki pages, and 69 Queries.
- Confirmed all Wiki pages and Query pages are listed in the index and no Wiki page is orphaned.
- Recorded remaining review backlog: two pre-v2 Raw Sources without `collectionPurpose`, four Wiki pages without MOC coverage, and one guide missing a Bias Check.
- Reuse axis: CMDS 시스템

## [2026-09-26] lint follow-up | purpose, MOC coverage, and Bias Check

- Backfilled `collectionPurpose` for the two April Karpathy LLM Wiki Raw Sources; set standalone-mode `mainVaultRelated` and `mainVaultCmds` to empty values without changing either `## Original Content` section.
- Connected the Neo4j verification guide and the UAV, Self Knowledge, and economic-freedom maps from [[MOC-Portfolio]].
- Added a Bias Check to [[개발자 커리어로 경제적 자유에 가까워지기]], identifying the trade-off between financial goals and broader career well-being and the outcome evidence still missing.
- Reuse axis: Codex 개발 워크플로, 취업/포트폴리오, 경제적 자유/FIRE/레버리지

## [2026-09-26] project milestone | 동일 계좌 이체 거부 테스트

- Added by the user: a test that transfers from an account to itself, expects `IllegalArgumentException`, and verifies the 10,000 balance remains unchanged.
- Learning recorded at the user's request: checking only the expected exception type (and, if relevant, its message) is insufficient; after a failed operation, re-query the original sender account by ID and verify its balance is unchanged. The same invariant check matters for failures such as `AccountNotFoundException` when the sender account already exists.
- Verification: the full `.\gradlew.bat test` suite passed during review.
- Next: move in-memory storage responsibility from `AccountService` behind a Repository boundary before introducing JPA.
- Updated: [[financial-lab]], [[index]]
- Reuse axis: 프로젝트 증거, 백엔드/성능/금융 시스템, 취업/포트폴리오
- [2026-10-02] query | 제4회 자랑스러운 개척인상 경쟁력 진단
  - Reviewed compiled portfolio evidence for CUEE team awards, leadership, GNU Buddy service, FPT collaboration, and eligibility context.
  - Conclusion: strong qualitative fit and worth applying; only the 44.23-hour volunteer component can currently be scored with confidence (estimated 4/5 within the activity rubric). Prize-money thresholds, certifications, and two-year leadership tenure remain unconfirmed or unqualified in available records.
  - Saved [[2026-10-02-Q-GNU-pioneering-award-competitiveness]] and updated [[index]].
  - Reuse axis: 취업/포트폴리오, 학부 리더십·공동체 활동, 교내 포상 지원서
- [2026-10-02] verification follow-up | CUEE 수상금 및 정량점수 조정
  - Downloaded the official GNU idea-thon plan and confirmed the 2026 GNU Pioneer Leaders Idea-thon best-excellence award is a team award with 500,000 KRW, meeting the 500,000 KRW student-activity threshold.
  - GNU's press release confirms CUEE won the regional startup club grand prize, but does not state a prize amount; the available G-300+ notice and certificate also do not establish a cash prize.
  - Flagged a mismatch between the user's expected volunteer total under 35 hours and the archived GNU Buddy activity confirmation of 44.23 hours; score it as 4 only if Student Affairs accepts the confirmation as qualifying volunteer evidence, otherwise use the user's under-35 estimate of 1.
  - Updated [[cuee]] and [[2026-10-02-Q-GNU-pioneering-award-competitiveness]].
  - Reuse axis: 취업/포트폴리오, 교내 포상 지원서, 리더십·공동체 활동
- [2026-10-02] query | 자랑스러운 개척인상 자기소개서 주도성·윤리 소재
  - Pulled `main` with `git pull --ff-only`; repository was already up to date and existing uncommitted work was preserved.
  - Added the user's LikeLion account of beginner coding barriers, Codex-based weekly idea-to-app lessons, seven of eight learners attending through the term, and one business student building an app in two weeks. Recorded the outcomes as user-reported, not independently verified.
  - Clarification: the student showed a shopping-related app on their own phone during the weekly pre-session sharing; the exact idea/features are not remembered, so no launch or usage outcome is claimed.
  - Found a CUEE integrity candidate in the Nexon interview-preparation recollection: the user told teammates his paid-use assumption was weak and proposed reconsidering the direction after a judge's question. Qualified it as honesty/accountability rather than a proven rule-violation dilemma.
  - Follow-up: recorded the user's fear of failure and sunk-cost concern during a pivot, while flagging that CUEE has two distinct pivots and the exact event/scope must be confirmed before essay use.
  - Further follow-up: assigned Q1 to the first-stage rejection, review-based improvements, and later awards; Q3 to Buddy/TMU/FPT with evidence boundaries; Q4 to CUEE product direction. Added provisional category ranges and calculated the present evidence-only total ceiling as 87 or 90 depending on volunteer-hour acceptance.
  - Saved [[2026-10-02-Q-GNU-award-essay-evidence-map]], updated [[김규태 Leadership and Teaching Evidence]], [[2026-10-02-Q-GNU-pioneering-award-competitiveness]], and [[index]].
  - Reuse axis: 교내 포상 자기소개서, 리더십·교육 경험, 윤리·책임 경험 점검
## [2026-10-02] ingest | 한기용 27년차 실리콘밸리 개발자 인생 이야기 1부

- Preserved the 80-line YouTube transcript verbatim under `## Original Content`; exact text comparison passed.
- Recorded the user's stated resonance with the principle that change comes from trying something new and trying again what one dislikes. The purpose is to use senior industry experience when choosing a post-graduation career and job, reducing avoidable trial and error and regret.
- Added [[변화는 새 시도와 불편한 경험의 재시도에서 온다]] with the quote treated as the user's remembered wording because ASR text is noisy; added a Bias Check and linked the idea to learning/recovery guidance.
- Updated [[김규태 Work and Learning Operating Guide]], [[MOC-김규태 Self Knowledge]], and [[index]]. Standalone mode: no mothership links.
- Reuse axis: 취업/포트폴리오, 독서/책/학습

## [2026-10-02] ingest | 교수 버튜버 진로 transcript 및 개인 활동·학습 메모

- Ingested four selected files into Raw Sources and confirmed each `## Original Content` ends with the exact source text.
- Added the professor VTuber transcript and the user's stated coding preference to [[AI 시대의 개발자 학습 전략]]: direct hand coding and AI tab completion at roughly a 50/50 split is a current user-reported practice, not a universal or measured optimum.
- Added the activity-report preparation record to [[김규태 Leadership and Teaching Evidence]], retaining its status as a working record that requires source-level confirmation before portfolio claims.
- Connected the user's flirting brainstorm to [[김규태 Attachment and Romantic Pacing Pattern]] and [[김규태 Relationship Values]], explicitly separating planned ideas from actual behavior and requiring consent before physical contact.
- Preserved the software development course notes as Raw Source only. The user deferred the AI-era student transcript and Peter Thiel career transcript; CUEE RISE and drone notes were excluded from this batch and their originals were left in place.
- Updated [[index]]. Standalone mode: no mothership links.
- Reuse axes: 취업/포트폴리오, 독서/책/학습, Codex 개발 워크플로, 제품/창업, 강의/수업/교육, 개인 삶의 운영 지식·관계 및 자기이해

## [2026-10-02] query follow-up | 자랑스러운 개척인상 지원동기와 동아리 활동 증거

- Reviewed [[cuee]] and [[김규태 Leadership and Teaching Evidence]] for the first-stage review feedback and subsequent changes before asking the user; the Wiki already records the three review gaps and some follow-up work, but not a complete one-to-one mapping for every gap.
- Added the user's Silicon Valley Employment Club activities to [[김규태 Leadership and Teaching Evidence]]: English LinkedIn resume, three-company research presentation, and an English mock interview using three actual questions from a chosen Silicon Valley company. Outcomes and the student need that prompted the design remain to be confirmed.
- Updated [[2026-10-02-Q-GNU-award-essay-evidence-map]] with an evidence-based motivation frame and the more specific Q6 activity sequence; no essay draft was written.
- The specified local PDF path `C:\Users\kym70\OneDrive\Desktop\1.pdf` was not present in the current workspace environment; exact item 2/7 wording still needs checking against the user's application form.
- Reuse axis: 교내 포상 자기소개서, 리더십·공동체·진로지원 활동

## [2026-10-02] query | 제조 AI 데이터 분석 교육 사전 준비

- Interpreted the user-provided two-day curriculum as 16 hours: manufacturing AI context, Python/VS Code setup, data preparation, preprocessing, visualization, prediction/classification, and a team or individual project.
- Personalized preparation to the user's existing Python experience, Java/Spring learning track, and financial data-analysis interest. Prioritized Pandas, basic visualization/statistics, classification metrics, train/test separation, and data leakage.
- Saved [[2026-10-02-Q-manufacturing-ai-data-course-preparation]] and updated [[index]]. The course's exact libraries, dataset, and grading criteria remain unknown from the image.
- Reuse axis: 독서/책/학습, 취업/포트폴리오

## [2026-10-02] query follow-up | 공식 자랑스러운 개척인상 서식과 문항 재배치

- Retrieved the 2026 official GNU selection notice attachment from the university page and extracted its full text/tables in a temporary directory. The attachment confirms the exact seven essay prompts and the quantitative scoring table; the linked desktop `1.pdf` is absent in this environment, so the official HWP is the primary prompt source.
- Confirmed prompt order: (1) growth background, values, adversity; (2) award motivation and fit; (3) post-award academic/career plan; (4) social contribution after career success; (5) strongest non-academic achievement; (6) school problem and solution; (7) ethical conduct despite disadvantage/sacrifice.
- Re-mapped the essay plan in [[2026-10-02-Q-GNU-award-essay-evidence-map]]. Added academic self-directed recovery as a Q1 candidate, LikeLion teaching as Q5, Silicon Valley club as Q6, and marked Q7 CUEE pivot as an unconfirmed fit rather than a proven ethical dilemma.
- Refined the quantitative assessment in [[2026-10-02-Q-GNU-pioneering-award-competitiveness]] using the official table. The Buddy 44.23-hour record is an International Office program certificate; it does not itself satisfy the notice's volunteer-portal certificate requirement. Baseline estimate is 2/15, with up to 2 additional contest points if the remaining team-award prize amounts meet the 500,000 KRW threshold. Current evidence-only arithmetic ceiling is 87 or 89, not a selection-probability prediction.
- GPA records (3.68 cumulative and 4.10 previous term) appear to meet the official 3.5 academic gate; disciplinary and duplicate-benefit eligibility still need user confirmation.
- No essay prose was drafted. The plan remains pending the user's confirmation and missing first-person details.
- Reuse axis: 교내 포상 자기소개서, 학업 회복, 창업·교육·진로 기여

## [2026-10-02] query follow-up | 학생활동 정량점수 상금·봉사 근거 재확인

- Downloaded and extracted the attached HWP from GNU's 2026-08-07 G-대학생 창업유망팀 동아리 챌린지 re-notice. The award table specifies 500,000 KRW per team for 최우수상 and 300,000 KRW per team for 우수상; the user's recorded U300+ linked 우수상 therefore does not meet this rubric's 500,000 KRW team-prize threshold.
- The 2026-09-03 GNU startup-supporters application draft records a 1365 total of 75 hours 30 minutes but does not break it down by the award's 2024-03 onward window. It includes an example from 2022, so the full total cannot be assigned to the current period. A period-specific portal record is still needed.
- Corrected [[2026-10-02-Q-GNU-pioneering-award-competitiveness]]: confirmed quantitative baseline remains 2/15; only the regional startup-club Grand Prize amount can add a known potential contest point. Arithmetic ceiling is 88 with the current volunteering assumption, or 91/92 if qualifying portal hours raise the volunteering tier and the regional prize qualifies.
- Updated [[2026-10-02-Q-GNU-award-essay-evidence-map]] and [[index]]. No essay prose was drafted; user confirmation and first-person details are still pending.
- Re-read the earlier GNU startup-supporters application and found a prior self-authored motivation about returning help received to aspiring teams. Kept it as a candidate for the award-motivation discussion only; the user has not confirmed that it is their reason for applying to this award.
- Reuse axis: 교내 포상 자기소개서, 봉사·수상 정량평가 증빙
## [2026-10-02] query | 금융권 취업을 위한 AI·데이터 대회 선택

- Read Core Context, finance career roadmap, portfolio map, recent bank-backend readiness review, and September opportunity map before comparing current contests.
- Verified current schedules for SNU Croche, KISTI DATA·AI, Data+AI data-safe-zone challenge, MOEL/KEIS Employment24 online hackathon, and KASA Space Hackathon. The supplied AI-idea contest closes 2026-10-02.
- Confirmed the data-safe-zone prize benefit applies only to 우수상 이상 winners applying to NICE지니데이타's 2027 entry-level hiring; the user still needs to verify center access and required team visits because the contest requires an in-person data-zone visit.
- Compared the conditional NICE hiring advantage with the user's higher-priority Java/Spring/SQL implementation gap. Saved [[2026-10-02-Q-hackathon-choice-for-finance-career]] and updated [[index]].
- No personal portfolio or career Wiki claims were changed; current contest-specific location and 2027 NICE role details remain to be confirmed.
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템, 제품/창업
## [2026-10-02] query follow-up | 데이터문제해결 vs 고용24 해커톤

- 팀원이 추천한 데이터문제해결은 데이터안심구역과 별도 부문이며, KDATA 데이터/분석 도구로 레시피 또는 문제해결 분석 결과를 제출하는 온라인 트랙으로 확인.
- NICE지니데이타 2027 채용 서류면제는 데이터안심구역 부문의 우수상 이상 조건으로 한정되고, 데이터문제해결 부문에는 적용 근거를 확인하지 못함.
- 사용자 목표의 직접 구현 격차에는 고용24 MVP가 더 직접적이나, 분석 강점 팀원이 있고 금융/사업 관련 데이터 주제와 사용자의 명확한 SQL·분석 기여가 확보되면 데이터문제해결도 팀 핏과 완주 측면에서 합리적이라는 조건부 판단을 추가.
- [[2026-10-02-Q-hackathon-choice-for-finance-career]] 및 [[index]]를 보완. 공식 근거 링크와 세부 일정 차이를 기록함.
- 재사용 축: 취업/포트폴리오, 데이터 분석, 백엔드/금융 시스템
## [2026-10-02] query follow-up | AI 코딩 전제 반영한 대회 추천 재평가

- 사용자가 Java 구현 경험은 financial-lab에서 쌓고, 대회 구현 코드는 AI로 작성할 계획이라고 명시해 선택 기준을 업데이트.
- 구현 산출물 자체보다 금융 데이터 주제의 적합성, 팀 분석 강점, 본인의 문제정의·결과 해석·검증 기여를 중심으로 재평가. 적합한 금융/사업 데이터 주제와 역할이 있으면 데이터문제해결 부문 우선, 제품 MVP 팀 핏이 더 강하면 고용24를 선택하는 조건부 권고.
- 데이터문제해결 부문 NICE 서류면제 제외, AI 생성 코드의 동작을 설명하고 활용 범위를 투명하게 밝힐 필요를 기록.
- [[2026-10-02-Q-hackathon-choice-for-finance-career]]의 결론과 후속 비교를 수정.
- 재사용 축: 취업/포트폴리오, 프로젝트 증거, 백엔드/금융 시스템
## [2026-10-02] query follow-up | 데이터문제해결 수상 역량·배점 확인

- 데이터 레시피와 문제해결은행 분석도구 활용 부문의 예선 배점, 공통 본선 발표 배점, 생성형 AI 공개 의무를 공개된 상세 모집요강에서 확인.
- 수상 준비 우선순위를 문제 정의 → 데이터 출처/분석 설계 → 정확한 결과 해석·검증 → 실효성 → 의사결정 발표/Q&A로 정리.
- [[2026-10-02-Q-hackathon-choice-for-finance-career]]에 평가표, AI 공개 조건, 사용자 기여 전략을 추가.
- 근거는 공개 세부 모집요강이며, 제출 직전 KDATA 포털 최신 양식과 대조 권고.
- 재사용 축: 취업/포트폴리오, 프로젝트 증거, 데이터 분석

## [2026-10-02] query follow-up | 개척인상 지원동기·윤리 후보·정량 경계 재확인

- 공식 공고의 선발 취지는 우수인재 발굴·시상을 통해 학생 상호간 동기를 높이고 미래 인재 육성에 대한 학내 관심을 제고하는 것임을 확인했다. [[2026-10-02-Q-GNU-award-essay-evidence-map]]의 2번 계획에 반영하되, 사용자의 실제 지원동기는 아직 확인하지 않았다.
- 자기성찰 기록에서 성장·가시적인 사용자 반응·인정 동기를 다시 확인했다. 이전 창업서포터즈 지원서의 `받은 도움을 돌려주기`도 이번 상의 동기와 동일시하지 않고 후보로 남겼다.
- UNLV 지원서 초안은 Threads의 404 GitHub 링크 게시물을 삭제하고 크롤링 과정을 수정했다고 적지만, 정확한 URL·수정 방법·실제 불이익은 미확인이라 7번 윤리 사례로 확정하지 않았다.
- 봉사 기준 계산을 바로잡았다: 35시간 미만은 1점, 정확히 35시간은 4점. 사용자가 보고한 `35시간 이하`만으로 정량점수를 단정할 수 없어 [[2026-10-02-Q-GNU-pioneering-award-competitiveness]]의 현 추정과 상한을 조건부로 정리했다.
- Q6의 영어 LinkedIn 이력서·관심 기업 3곳 발표·실제 질문 3개의 영어 모의면접을 [[2026-10-02-Q-GNU-award-essay-evidence-map]]에 반영했다. 학생의 구체적 준비 공백과 참여 규모·효과는 여전히 확인이 필요하다.
- 문화적 감성은 Buddy의 유학생 적응 지원·약속시간 기대 조율과 FPT 다국적 팀 협업을 주요 근거로 정리했다. TMU 팀은 한국인 구성이므로 직접 교류 장면을 확인하기 전에는 다국적 팀 경험으로 쓰지 않도록 한계를 기록했다.
- `모두의 창업` 심사평의 세 보완점과 후속 자료를 연결했다: CUEE MVP·로드맵(제품계획), 코레일 실증/기업 제휴 및 이커머스 경로(초기 판로 가설), B2B 수수료와 CPS(수익 가설). 실제 판매·계약·고령 사용자 검증은 없으며, 5/27 아이디어톤 수상과 결과 예정 시점 사이의 연대기는 사용자 확인이 남았다.
- 21:06 KST에 GNU 공지를 다시 검색했지만 접수 연장이나 선발 결과 공지는 확인되지 않았다. 제출 여부는 사용자에게 확인되지 않았으며, 지정된 `Desktop\\1.pdf`도 여전히 없고 `0557720161.pdf`는 공고 양식으로 확인된다.
- 제출 증빙 경로를 다시 조사하고 `20-PDF-U300-challenge-award.png`에서 CUEE 5인 팀의 우수상과 2026-08-11 날짜를 시각 확인했다. Buddy·TMU·FPT 수료/활동 문서는 저장돼 있지만, 5/27 GNU 아이디어톤과 6/16 경남권 대상 상장 원본 및 기간 지정 1365/VMS 확인서는 현재 Desktop/Wiki attachment 경로에서 찾지 못해 [[2026-10-02-Q-GNU-award-essay-evidence-map]]에 분리 기록했다.
- GNU 공식 사이트에서 해당 두 수상의 팀명별 결과 공지도 검색했으나 찾지 못했다. 결과 공지가 없다고 단정하지 않고, 개인 제출 증빙 파일이 필요하다고 기록했다.
- 21:13 KST에 GNU 공고를 다시 확인했으며 여전히 9/29 모집 공고만 보이고 연장 또는 결과 공지는 검색되지 않았다. 이는 현재 공개 상태 확인일 뿐, 사용자의 제출 여부를 증명하지 않는다.
- GNU 본 공고 일정 메타데이터는 10월 2일 14:36까지, 첨부 양식과 학과 게시 안내는 18:00까지로 표시되어 있어 접수 마감 시각 표기가 일치하지 않는다. 접수 여부와 학생과의 안내는 사용자 확인 대기 상태다.
- 자기소개서 초안은 작성하지 않았다. 사용자의 제출 상태·모두의 창업 결과 연대기·개척인상 지원동기 확인을 기다린다.
- 재사용 축: 교내 포상 자기소개서, 리더십·공동체 활동, 윤리적 책임

## [2026-10-02] query follow-up | GNU 개척인상 공고 페이지 현재 표시 재확인

- 공식 GNU 공고 페이지를 21:16 KST에 열어 모집 일정이 2026-09-29 14:36~2026-10-02 14:36으로 표시되고, 첨부파일 다운로드 수가 400회임을 확인했다. 이전 사용자 관찰값 6회와 다르지만 어느 쪽도 지원자 수를 나타내지는 않는다.
- 공고 페이지의 14:36 마감과 첨부 양식·학과 공지의 18:00 마감 표기가 다르며 두 시각 모두 확인 시점에는 경과했다. 제출 상태는 추정하지 않고 사용자에게 확인하도록 소재 지도와 경쟁력 진단에 기록했다.
- 재사용 축: 교내 포상 자기소개서, 지원자 수와 다운로드 수 구분

## [2026-10-02] query follow-up | 경남권 창업동아리 CUEE 대상 1차 출처 보강

- GNU 공식 보도자료(2026-06-01)가 경남권 창업동아리 교육·경진대회 날짜(5/28~29), 참가 규모(24팀·85명), CUEE 대상 수상을 확인하는 것을 찾았다. 앞서 `팀명별 공식 결과 공지를 찾지 못함`이라고 한 기록을 수정했다.
- 보도자료에는 개인별 팀원 명단이나 대상 상금이 없다. Wiki의 6/16 상장 날짜와 5/28~29 대회 시점을 구분하고, 원본 상장 확인 전까지 정량 상금점수는 적용하지 않는다고 `cuee`, 소재 지도, 경쟁력 진단에 반영했다.
- 이 상의 공식 결과는 6/1 보도자료로 확인되므로, 모두의 창업 1차 선정 결과(6월 중순 예정) 이후 성과라고 단정할 수 없다. 정확한 탈락 통보일·심사의견 수령일은 사용자 확인을 요청한다.
- 재사용 축: 교내 포상 자기소개서, 수상 연대기, 팀 성과 증빙

## [2026-10-02] query follow-up | 경남권 대상 상금·지원금 구분 확인

- GNU의 [2026 경남권 대학생 창업동아리 모집 공고](https://map.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&nttSn=6793182)에 첨부된 공식 프로그램 PDF를 내려받아 확인했다. 프로그램은 별도 3단계로 MVP 제작비를 20팀에 팀당 최대 200만원 지원하고, RISE 마일리지는 참여시간을 기준으로 지급한다고 명시한다.
- PDF와 공식 결과 보도자료에서는 CUEE의 대상 수상 상금 액수를 찾지 못했다. MVP 제작비·참여 마일리지는 경진대회 상금과 다른 사업 지원이므로 정량 공모전 점수로 환산하지 않는다. 별도 대상 상금이 지급됐는지는 사용자 보유 상장·지급 증빙으로 확인할 질문으로 남긴다.
- 소재 지도·경쟁력 진단·CUEE 엔티티에 근거 구분을 기록했다.
- 재사용 축: 교내 포상 정량평가, 창업지원금과 상금 구분

## [2026-10-02] query follow-up | 개척인상 공식 취지와 현재 공고 상태 재확인

- GNU 공식 검색에서 제4회 개척인상 연장이나 선발 결과 공지는 찾지 못했고, 9/29 모집 공고가 계속 노출되는 것을 확인했다. 공대·지질학과 등 학교 부서의 동일 공지 재게시에는 10/2 18:00 마감이 표시된다. 본 공고의 포털 일정 14:36과 다른 공식 표기가 있으나 둘 다 현재 시점에는 지났다. 사용자 접수 여부는 추정하지 않는다.
- GNU 지질과학과 공식 재게시의 안내 문구에서 선발 목적이 우수인재 발굴·시상, 학생 상호간 동기부여, 미래 인재 육성에 대한 학내 관심 제고임을 확인했다. [[2026-10-02-Q-GNU-award-essay-evidence-map]]의 Q2 계획에 추가해, 사용자의 진짜 동기를 확인하기 전에는 `타인에게 동기를 주고 싶다`는 이유를 임의로 쓰지 않도록 명시했다.
- 재사용 축: 교내 포상 자기소개서, 공식 지원동기 해석, 접수상태 점검

## [2026-10-02] query follow-up | Q7 제품 피벗 선택과 소재 지도 정정

- 현재 Wiki에서 `CUEE 피벗이 제품 방향인지 수익모델인지 확인`을 계속 미해결로 둔 것을 발견했다. 앞선 사용자 답변은 이미 7번 후보를 `큐의 제품 방향`으로 골랐으므로 이를 반영했다.
- CUEE 엔티티와 자랑스러운 개척인상 소재 지도·경쟁력 진단을 수정해 `배우담`에서 `CUEE`로 바꾼 제품 방향 피벗을 7번의 우선 후보로 정했다. 사용자 보고로 확인된 실패 우려와 기존 작업을 버리는 부담을 기록하고, 실제로 포기한 작업·재사용한 작업·감수한 비용 및 이 선택이 왜 사용자에 대한 책임 판단이었는지는 미확인으로 남겼다. 단순 사업 방향 변경을 윤리행동으로 포장하지 않는다.
- Q2에는 GNU 학과 공지에 적힌 공식 취지(우수인재 발굴·시상, 학생간 동기부여, 미래 인재 육성에 대한 학내 관심)를 연결하되, 사용자의 진짜 동기는 아직 확인 전이라고 명시했다.
- 재사용 축: 개척인상 2·7번 소재 계획, 사용자 확인사항 추적

## [2026-10-02] query follow-up | Desktop 공식 HWP 공고 일정 대조

- Desktop에 `제4회 자랑스러운 개척인상 선발 공고.hwp`가 있음을 확인하고 HWP 미리보기 텍스트를 읽었다. 제목과 내용은 개인 작성본이 아닌 총장 명의 공식 선발 공고다.
- 첨부 공고는 접수 마감을 10/2 18:00, 후보자 심사·최종 발표 기간을 10/6~10/15, 시상식을 10/20 예정으로 명시한다. 여러 학교 부서 재게시도 18:00 마감을 적는다. 포털 상세페이지의 14:36 메타데이터와 차이는 있으나, 사용자의 제출 여부는 알 수 없다.
- 10/2 23:54 KST에는 발표 예정 기간 전이다. 결과 공지가 안 보이는 점으로 제출·선발 상태를 추정하지 않는다. `1.pdf`는 여전히 없고, Desktop의 HWP는 공식 공고문이다.
- 소재 지도와 경쟁력 진단에 공고 종류·시상일정·기한 차이를 구분해 반영했다.
- 재사용 축: GNU 지원서 준비, 공고와 작성본 구분, 접수 상태 검증

## [2026-10-03] query follow-up | Q7 제품 피벗의 공개 개발 근거 대조

- 사용자의 공개 [배우담 개발일지](https://velog.io/@gyutaetae/%EB%B0%B0%EC%9A%B0%EB%8B%B4-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%801) (2026-05-04)를 확인했다. 본문은 개발 전 기획으로 표시되어 있으며, 화면 전환을 어려워할 수 있는 사용자를 위해 실제 앱 위에서 안내하기, 불확실한 버튼은 강조하지 않기, 한 단계 안내 후 멈추기, 민감정보를 로컬에서 처리하기 같은 설계 결정을 담고 있다. 이는 책임 있는 제품 원칙의 근거지만 구현·사용자 효과를 증명하지 않는다.
- 공개 [CUEE GitHub commit history](https://github.com/gyutaetae/cuee/commits/main)를 GitHub API로 확인했다. 현재 저장소는 2026-05-01 설계 문서 및 같은 날 Android 구현 커밋으로 시작한다. 이력은 이전 배우담 학습형 개념의 별도 산출물·폐기 과정을 보여주지 않으며, 별도 로컬·문서 작업이 없었다는 증명도 아니다. 공개 개발일지의 `개발시작 전` 표기와 5/1 저장소 구현 이력 사이 시점을 사용자 확인 전까지 화해시키지 않는다.
- Wiki의 Q7 계획을 사용자가 고른 제품 피벗 중심으로 정리했다. Threads 404 사례는 사용자 요청으로 이전 활동실적 PDF에서 제외됐고 정확한 URL·오류·수정·감수 비용이 검증되지 않아 보조 후보에 둔다.
- 2026-10-03 GNU 공식 공고를 다시 열었을 때 목록에는 기존 공고만 보였고, 접수 일정은 메타데이터상 10/2 14:36 종료, 첨부 공고·학과 재게시상 18:00 종료로 서로 다르다. 다운로드 표시는 401회이며 지원자 수는 아니다. 현재 검색에서 연장·결과 공지를 추가 확인하지 못했고 발표 예정 기간은 아직 시작 전이다.
- 재사용 축: 개척인상 Q7, 사용자 중심 설계, 기술·행동 이력 증빙


## [2026-10-03] query follow-up | 개척인상 지원동기 확인 및 초안 전 기획 유지

- 사용자는 개척인상에 지원하려는 실제 이유로 다음 창업·교육 활동을 이어갈 계기를 얻고 싶다고 확인했다. 이를 소재 지도 Q2에 반영하고, 상을 통해 얻고자 하는 계기의 구체적 의미와 공식 선발 취지·실제 활동 근거를 연결하도록 했다.
- 사용자는 내일이라도 제출할 수 있으니 마감은 더 신경 쓰지 말고 준비하라고 했다. 공식 공고 일정은 사실 기록으로 남기되, 마감 확인을 반복하거나 글쓰기 계획을 멈추지 않는다.
- 사용자의 기존 요청대로 초안은 작성하지 않았다. 모두의 창업 탈락·수상 연대기, 배우담→CUEE 피벗에서 실제로 포기·재사용한 일과 윤리적 이유, 취업동아리 활동의 참여 규모·변화에 대한 사용자 답변을 기다린다.
- 재사용 축: 개척인상 Q2·Q7, 창업·교육 동기, 초안 전 소재 기획

## [2026-10-03] ingest | Modoo CUEE 심사의견 및 사용자 응답

- 사용자가 지정한 Desktop 캡처를 `80. References/Attachments/2026-10-03-Modoo-CUEE-review-context.jpeg`에 보존하고, 보이는 심사평을 `10. Raw Sources/15. Clippings/2026-10-03-Modoo-CUEE-review.md`의 `Original Content`에 전사했다. 기존 `2026-09-08-CUEE-modoo-final-review.jpeg`와 동일한 심사평이며 새 캡처는 주변 페이지 맥락을 더 포함한다.
- 사용자는 첫 `모두의 창업` 탈락과 심사의견이 2026년 4월이었다고 확인했다. 심사평의 긍정·보완점을 이미지 원문과 대조했다.
- 사용자가 설명한 대응을 분리해 기록했다: 노인 구독료를 없애 무료 제공, 구매전환률과 시간 단축 자료 확보, 이를 근거로 Korail 같은 기업에 B2B SaaS 제공, CUEE를 통한 구매 성공별 CPS. 이는 사용자 보고상의 사업모델 전환이며 실제 KPI·계약·거래·수익 증거는 없다.
- 공식 공고 자료의 6월 중순 1차 선정 안내와 사용자의 4월 탈락 기억은 같은 심사 단계인지 불분명해 `cuee`에 경고를 남기고 `disputed: true`로 표시했다. 정확한 단계, 변경 모델의 반영 시점 및 후속 수상과의 인과는 미해결이다.
- `cuee`, `김규태 Leadership and Teaching Evidence`, 개척인상 소재 지도 및 `index.md`를 갱신했다. Raw Sources 수를 56으로 동기화했다.
- 재활용 축: 제품/창업, 에세이, 프로젝트 판단·증거

## [2026-10-03] query follow-up | 4월 탈락 이후 제출물 반영 순서 확인

- 사용자는 4월 결과가 공식 탈락 결과였으며, 노인 무료 제공·전환율/시간 절감 자료 확보·B2B SaaS/CPS 선택이 이후 5/27 아이디어톤과 5월 말 경남권 대회 제출물에 담겼다고 추가 확인했다.
- 이 순서를 반영해 `cuee`, 개척인상 Q1 소재 지도, 원문 클리핑의 사용자 보고를 확인했다. 수상은 이후 발생했지만 해당 사업모델 선택이 수상의 원인이었다고 적지 않았다.
- 중기부가 공지한 전국 모두의 창업 모집 일정(5/15 마감, 6월 중순 5천 명 발표 계획)과 4월 공식 탈락 시점이 같은 평가 단계인지 아직 불명확하다. `modoo.or.kr`의 GNU 최종 심사인지, 전국 사업과 별도인 교내/사전 단계인지 정확한 공고·선발명을 확인해야 연대기를 확정할 수 있다.
- 재활용 축: 개척인상 Q1, CUEE 사업모델 의사결정, 공식 결과 연대기

## [2026-10-03] query follow-up | 개척인상 정량 증빙 파일 재확인

- Desktop 및 Wiki의 `70. Outputs`·`80. References/Attachments`에서 상장, 아이디어톤, 경남권, 봉사/1365/VMS, 활동확인 관련 이름을 대상으로 검색했다. U300+ 우수상 상장 이미지와 Buddy·TMU·FPT 증명은 찾았으며, 상금 액수는 U300+ 상장에 없다.
- GNU 아이디어톤 최우수상 원본, 경남권 대상 원본/상금 액수, 2024-03 이후 기간 지정 포털 봉사 증빙은 검색 결과에서 추가로 찾지 못했다. 파일명이 일반적인 경우까지 배제하지 않도록 확인 범위를 기록했다.
- 이 범위와 한계를 개척인상 소재 지도의 증빙 현황에 반영했다.
- 재활용 축: 개척인상 정량점수, 수상·봉사 증빙 패킷

## [2026-10-03] query follow-up | 4월 모두의 창업 신속 심사 일정 확인

- 중기부의 [2026-04-16 통합 모집 수정공고](https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1067363&cbIdx=310)를 확인했다. 신청 수요가 높은 멘토기관에 신속 심사를 도입했고, 4/23 24시까지 접수한 신청의 결과를 4월 말 안내할 계획이었다. 신속 심사 미선정 아이디어도 접수 마감 뒤 정규 심사에 포함된다고 명시했다.
- 따라서 사용자의 4월 공식 비선정은 전국 프로젝트의 신속 심사 결과일 수 있다. 실제 신청 트랙, 기관, 통지 문구는 아직 확인되지 않아 가능성으로 기록했다. 5/15 모집 마감·6월 중순 전체 선발 발표 계획과 날짜만으로 모순이라고 단정하던 설명을 교정했다.
- `cuee`, CUEE 심사평 원문 클리핑, 개척인상 소재 지도와 경쟁력 진단을 갱신했다. 배우담→CUEE 제품 방향 결정(지원 준비 중)과 4월 심사평 이후 무료 제공·B2B/CPS 수익모델 결정을 분리했다.
- 재활용 축: 개척인상 1·7번, 모두의 창업 신청·심사 연대기, CUEE 피벗 기록

## [2026-10-03] query follow-up | 모두의 창업 비선정 단계 사용자 정정

- 사용자는 4월 Modoo 비선정이 신속 심사가 아니라 `정규·최종 비선정`이었다고 명확히 답했다. 이 답변을 사용자 회고로 기록하고 앞선 신속 심사 가능성 중심 설명을 고쳤다.
- 제공된 화면에는 심사의견만 있으며 실제 결과 통지 문구·날짜는 없다. 전국 정규 선발 예정 시점은 6월 중순이어서 4월 회고와 공식 일정의 차이는 남긴다. 지원서 1번은 심사 단계·정확한 날짜를 쓰지 않고, 비선정 뒤 피드백을 반영한 행동으로 구성한다.
- `cuee`, 심사평 원문 클리핑, 개척인상 소재 지도·경쟁력 진단, 리더십 문서 두 곳을 갱신했다. 7번의 실제 포기한 작업·설득 근거·본인이 감수한 부담은 사용자에게 추가 질문했다.
- 재활용 축: 개척인상 1·7번, 모두의 창업 심사 연대기

## [2026-10-03] output | 자랑스러운 개척인상 1~7번 자기소개서 초안

- 사용자가 확정한 7개 소재 배치를 바탕으로 `70. Outputs/2026-10-03-GNU-Proud-Pioneer-Award-Draft.md`에 첫 문안을 작성했다. 공고 HWP의 실제 1~7번 문항 문구와 전체 5쪽 이내 안내를 대조했다.
- 2·3번에는 수상 후 복지관에 처음 연락해 CUEE 고령자 사용성 검증을 제안한다는 계획을 넣었다. 7번에는 Threads 404 링크를 직접 확인해 글을 내리고 링크 확인 에이전트 워크플로를 개선한 행동을 넣되, 조회수 손실·수정 로그·검증 성능은 주장하지 않았다.
- 사용자는 현재 로컬 브랜치의 모든 변경사항을 GitHub에 푸시하도록 명시적으로 요청했다.
- 재활용 축: 교내 포상 지원서, CUEE 사용자 검증 계획, 윤리 행동 사례


## [2026-10-05] ingest | 금융권 백엔드 취업 준비 영상 7편과 사용자 목적

- Desktop markdown 7개를 Raw Sources/14. Transcripts에 원문 그대로 보존했다. Desktop 파일은 유지한다. 영상 원본·게시일·자막 정확성은 별도 검증하지 않았다.
- 사용자 대화를 Raw Sources/15. Clippings에 보존하고 collectionPurpose에 2027년 8월 졸업 후 금융권 백엔드 취업/인턴 목표, 이상적인 포트폴리오 역설계, 기여 중심 지원동기를 기록했다.
- 새 Wiki 5개: [[금융권 백엔드 목표 포트폴리오를 역설계하는 법]], [[채용공고와 기여 증거를 연결하는 지원동기]], [[개발자 이력서 첫 페이지와 대표 증거]], [[포트폴리오 주제는 기술 문제와 도메인 가치를 함께 보여준다]], [[AI 시대 주니어의 문제 진단과 좋은 코드 판단 기준]]. 새 페이지는 explored: false, verificationStatus: unverified 및 Bias Check를 포함한다.
- 기존 Wiki 5개(Portfolio MOC, 금융 취업 로드맵, Career Narrative, AI 학습 전략, AI 개발자 포지셔닝), Core Context와 index를 갱신했다. 구현 상태와 프로젝트 일일 로그는 추가하지 않았다.
- 기술 난도와 사용자·도메인 가치의 관점을 함께 기록했다. 한 회사의 채용 사례를 금융권 전체 기준으로 일반화하지 않으며, 100% 성공 전략의 미검증 한계와 발표자의 경험 부재를 명시했다.
- Standalone Mode이므로 mainVaultRelated/mainVaultCmds는 비워뒀다. 재활용 축: 취업/포트폴리오, 프로젝트 증거, 백엔드/금융 시스템.
- 보존 점검: 제공 파일 7개의 Original Content를 바이트 단위로 대조해 일치함을 확인했다. 새 Wiki의 index 등재 및 폴더별 통계도 일치한다. 새 페이지·추가 연결의 대상이 존재하며, index의 기존 Karpathy 별칭 링크는 기존 항목이다. 현재 환경에는 qmd 실행 파일이 없어 재색인은 수행하지 못했다.


## [2026-10-05] ingest | 자기 신뢰 독서 관심과 Python 코딩테스트 교차 학습

- 목적을 확인한 책 추천·학습 영상 2개와 사용자 답변 1개를 Raw Sources에 보존했다. Desktop 원본은 유지한다. 한기용 영상은 기존 원문과 동일(마지막 개행 제외)하므로 중복 생성하지 않았고 시행착오 줄이기 목적을 재확인했다.
- 사용자 관심은 첫 책 《자기 신뢰》이며 완독·구매로 기록하지 않았다. 학습 목적은 Java·Spring과 Python 코딩테스트에서 문제 유형을 섞어 전략 선택과 재풀이 능력을 높이는 것이다.
- 새 가이드: [[김규태 Python 코딩테스트 교차 학습 가이드]], [[인출 간격 교차 자기설명을 학습에 적용하는 법]], [[자기 신뢰 독서 관심과 판단 기록]]. 기존 Wiki 7개, Core Context, index/log를 연결했다. 영상의 인용 논문·책 원문은 미검증이며 연구 수치를 코딩테스트 성과로 일반화하지 않았다.
- 카톡·소설 영상은 수집 목적 답변을 기다린다. 전체 인제스트를 마친 뒤 qmd 재색인할 예정이며 Windows qmd.exe 및 3개 collection 설정을 확인했다.


## [2026-10-05] ingest | 카톡 대화 조언과 소설 독서 관점

- 사용자 “네맞아요” 답변으로 관심 있는 사람과의 대화·관계 판단, 소설을 통한 사람·감정 이해 목적을 확인했다. 두 원문을 보존하고 [[관계 대화 조언을 상호성과 명시적 의사로 점검하기]], [[소설 읽기는 인물의 선택과 감정을 따라가는 경험이다]]를 만들었다.
- Relationship Values, 독서 개념, Self Knowledge MOC와 index/log를 갱신했다. 카톡 영상의 상업적 맥락·성별 일반화·마음 추정 및 소설 영상의 장르 우월 수사와 책 해석의 미검증 한계를 남겼다. 원문 전략을 사용자 행동·신념으로 승격하지 않았다.
- 이번 요청의 자료 5개는 신규 4개 인제스트와 한기용 기존 자료 재사용으로 처리했다. 전체 qmd 갱신과 임베딩을 이어서 수행한다.
- 보존·연결 점검: 새 영상 4개의 Original Content는 Desktop 원본과 바이트 단위로 일치한다. 새 Wiki 링크 대상과 index 등재, 폴더별 통계가 일치한다.

## [2026-10-05] reindex | Windows qmd 3개 컬렉션 갱신 완료

- WSL PATH에는 qmd가 없었지만 `C:\Users\kym70\.bun\bin\qmd.exe`의 기존 설치와 로컬 설정을 찾았다. 앞선 설치 부재 설명을 정정한다.
- `qmd update`로 wiki 90개, raw_sources 69개, queries 73개를 등록했다. 총 232개 문서, 최종 2,027개 벡터이며 임베딩 대기 항목은 없다. 이번 세션의 취업 자료와 독서·학습·관계 자료 모두 반영했다.
- GPU 자동 선택과 CPU 실행의 처리 지연을 확인한 뒤, 이번 실행에서 `QMD_LLAMA_GPU=vulkan`, `QMD_EMBED_PARALLELISM=1`을 사용했다. GTX 1050 Ti에서 남은 29개 문서의 176개 청크를 4분 9초에 처리했다. 영구 설정은 변경하지 않았다.
- 키워드 `교차` 검색 및 자연어 `파이썬 알고리즘 문제 유형을 섞어 풀고 며칠 뒤 다시 풀기`의 벡터 검색을 확인했다. 새 Python 교차 학습 가이드가 벡터 검색 첫 결과다. 벡터 확인은 `query "vec: ..." --no-rerank`로 수행했고, 기본 vsearch가 요청한 추가 생성 모델 다운로드는 중단했다.
- 검색 DB와 모델은 이 컴퓨터의 로컬 캐시에 있으며 Git에 넣지 않는다. 다른 컴퓨터에서는 pull 뒤 해당 컴퓨터의 qmd 검색 색인을 갱신한다.

## [2026-09-18] query | 금융사 개발자 근무조건·성장성·입사난이도 심층 비교

- Query saved: [[2026-09-18-Q-korea-financial-developer-employer-deep-comparison]]
- Scope: 9개 은행·인터넷은행과 8개 증권사의 개발 근무지, 직군, 2025 공시 평균급여, 복지, 성장성, 입사난이도 비교
- Compensation boundary: 회사 전체 직원 평균급여를 신입·개발자 연봉과 분리하고, 미공개 오퍼 금액은 임의 추정하지 않음
- Preference boundary: 동일 표본의 개발자 선호도 자료가 없어 제품 소유권·기술 이동성·금융 도메인·보상·신입 성장경로를 종합한 `개발 커리어 매력` 분석으로 대체
- Recruitment update: 삼성증권 2026 하반기 3급 신입 IT서비스 기획/운영과 미래에셋증권 Tech 채용연계형 인턴 통로를 새로 확인해 신입 지원 우선순위를 상향
- Competition boundary: IBK 전체 공채 약 110:1 외에는 회사별 IT 경쟁률이 공개되지 않아 모집 희소성·전형·직무 요구 수준으로 난이도를 판단
- Reuse axis: 취업/포트폴리오, 백엔드/성능/금융 시스템, 독서/책/학습

## [2026-09-18] query update | 금융사 신입 초봉·난이도·채용구조·포트폴리오 보강

- Query updated: [[2026-09-18-Q-korea-financial-developer-employer-deep-comparison]]
- Compensation: 은행권 6,000만~7,000만 원 업권 보도와 회사별 비공식 추정치를 분리하고, 증권사 초봉 자료 충돌을 명시
- Difficulty: 높음·매우 높음·최상을 지원자 준비 수준과 신입 공고 존재 여부로 번역
- Hiring mix: KB·IBK 전체 신입/경력 숫자와 IBK IT·디지털 30/175를 확인하되 개발직군 비율로 확대하지 않음
- Portfolio: 은행·금융 IT·인터넷은행·증권·SRE별 선호 증거와 직접 구현·정량 검증 중심의 신입 생존 전략 추가
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능/금융 시스템

## [2026-09-22] ingest | Gemini 제조 DB 성능 최적화 에이전트 대화

- Raw Source saved: [[2026-09-22-Gemini-Manufacturing-Database-Performance-Agent-Conversation]]
- Compiled: [[제조 DB 성능 최적화 에이전트 프로젝트 검증 가이드]]
- Connected: [[MOC-Portfolio]], [[index]]
- Purpose: 제조 경진대회 아이디어를 DB 실행계획·인덱스·락·파티셔닝을 직접 측정하는 취업/포트폴리오 프로젝트 후보로 발전
- Evidence boundary: Gemini의 기술 추천과 예시 성능 수치는 미검증이며, 현재는 아이디어·실험 설계이지 구현·성능 개선 증거가 아님
- Verification plan: 합성 제조 데이터, 고정 부하, `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)`, 규칙 기반 비교군, p50/p95/p99·throughput·쓰기 비용·락 대기 측정
- Source cleanup: 원문을 `Clippings/`에서 Raw Sources로 이동하고 `## Original Content` 아래에 보존
- Reuse axis: 취업/포트폴리오, 프로젝트 증거, 백엔드/성능, Codex 개발 워크플로

## [2026-09-24] update | Rotor Engineering Knowledge Agent 제안서 통합

- 팀원 제안의 과거 로터 해석·시험 검색 및 재사용과 프로펠러 소음·추력 후보 검토를 하나의 E2E 업무 흐름으로 통합했다.
- 문제를 작업장 시험 소음이 아닌 eVTOL 운항 소음 설계 검증과 해석·시험 근거의 재사용 문제로 정리하고, 현장 반복 업무는 인터뷰 전 가설로 표시했다.
- 관계형 DB·Python·문서 검색의 MVP 역할과 GraphRAG의 후속 검토 범위를 구분했다.
- CFD는 기존 결과 재사용 검토를 MVP 중심으로 두고, CLI/API 기반 단일 benchmark 실행은 환경과 검증 기준을 확보했을 때만 추가하도록 정리했다.
- H200 접근 미확인, 공개 데이터의 실험실 한계, 서로 다른 RPM의 소음 결과, 새 형상 외삽 예측 위험과 사용자 검증 과제를 명시했다.
- Updated: `Propeller Evidence Agent 1.md`, `index.md`

## [2026-09-24] query | 로터 엔지니어링 에이전트 최신 기술과 KICK 후보 조사

- Query saved: [[2026-09-24-Q-emerging-technologies-for-rotor-engineering-agent]]
- 조사: CadQuery/OCCT 형상 인식, BoTorch 다목적 Bayesian optimization, Foam-Agent MCP 기반 OpenFOAM 자동화, NVIDIA PhysicsNeMo/PhysicsNeMo-CFD
- 추천: evidence reuse와 uncertainty-aware 다음 시험 설계를 human-approved workflow로 연결; 데이터가 적은 현재는 예측 대신 coverage gap/비교 보류를 우선
- 한계: 공개 시험 자료는 제조 데이터가 아니며, 서로 다른 조건의 희소 데이터로 소음 예측·최적화를 주장할 수 없음; H200 접근 미확인
- Reuse axis: 프로젝트 증거, 취업/포트폴리오, 학부연구생/학술, 강의/수업/교육

## [2026-09-24] query update | CFD agent 저장소 인기도와 프로젝트 적합성 재비교

- Foam-Agent, ChatCFD, FoamGPT, AutoFOAM, myOpenFoamAgent 및 woog97/cfd-agent의 공개 기능·별 수·제약을 비교했다.
- GitHub stars를 조회 시점의 인기도 신호로만 기록하고 품질의 대리 지표로 사용하지 않았다.
- 판단 수정: Foam-Agent는 MCP composability와 MIT license 때문에 구조 참고에 가장 적합; ChatCFD는 실행 성공과 물리적 타당성을 분리 평가하는 quality gate 참고에 가장 적합.
- 로터 유사 도메인 참고: myOpenFoamAgent는 MRF propeller reference validation을 다루지만 인기도가 매우 낮아 검증 사례/진단 아이디어 참고로 한정.
- 제품 채택: 전체 CFD agent를 MVP에 포함하지 않고, 검증된 단일 reference case 실행만 선택적 stretch로 유지.
- Updated: [[2026-09-24-Q-emerging-technologies-for-rotor-engineering-agent]]

## [2026-09-24] query update | OpenFOAM 공식 CLI·확장·MCP와 프로펠러 계산 기능 확인

- 공식 OpenFOAM CLI를 통한 setup/run/post-process/batch automation과 functionObject/library 확장 경로를 확인했다.
- 공식 API에서 `propellerInfo`의 Kt/10*Kq/J/etaO/wake 출력과 Curle functionObject의 acoustic-pressure output을 확인했다.
- OpenFOAM 본체가 공식 MCP를 제공한다는 문서는 찾지 못했고, Foam-Agent MCP는 별도 제3자 구현으로 구분했다.
- Revised boundary: CLI로 고정 reference case 및 검증된 parameter sweep은 가능하지만, CAD-to-mesh 및 검증된 소음 최적화는 자동으로 성립하지 않음.
- Updated: [[2026-09-24-Q-emerging-technologies-for-rotor-engineering-agent]]

## [2026-09-24] query update | Ansys Fluent 공식 MCP 지원 및 CFD 선택 재평가

- Ansys 공식 PyFluent Python API 및 Ansys 조직의 PyFluent-MCP를 확인했다. MCP는 Fluent tool bridge이며 agent reasoning/orchestration은 별도 구성이다.
- `ansys-fluent-mcp` 0.4.0이 Alpha이며 Python 3.12+, PyFluent, licensed Fluent가 live solver access에 필요함을 기록했다.
- Fluent FW-H의 transient workflow와 steady single moving-reference-frame 한계를 확인하고 프로펠러 소음 비교 조건을 명시했다.
- 팀이 이미 Fluent를 사용한다는 현재 맥락에 따라 종전 OpenFOAM 우선 잠정 권고를 수정: Fluent를 1순위로 유지하고, 라이선스/환경 문제가 있을 때 OpenFOAM을 대안으로 둔다.
- Updated: [[2026-09-24-Q-emerging-technologies-for-rotor-engineering-agent]]

## [2026-09-25] update | 프로펠러 에이전트 2주 데모 실행 항목 구체화

- Windows Pro PC를 통합 실행 환경으로 사용한다는 팀 결정을 반영했다.
- 연구실/팀원 자료에서 시연용 propeller CAD, mesh, Fluent case 확보와 출처·사용 허가·조건 기록을 우선 과제로 추가했다.
- 전문가 점검 순서 인터뷰와 입력·판정 근거·실패 조치·승인 단계 기록을 할 일로 추가했다.
- SQLite는 메타데이터 검색·이력 저장, Python은 TXT/HDF5 데이터 계산, LLM은 규칙 기반 판정의 설명을 맡도록 책임을 분리했다.
- H200은 4일 뒤 접속 안내를 받은 다음 평가하는 선택 항목으로 두고 핵심 데모에서 분리했다.
- Updated: `Propeller Evidence Agent 1.md`, `index.md`

## [2026-09-25] create | Propeller Evidence Agent MVP PRD

- 결과만 제시하는 자동화 대신 자연어 요청 → 실제 절차 점검 → 사람 승인 → Fluent 진행 시각화 → 근거 보고서의 하이브리드 데모 흐름을 제품 킥으로 확정했다.
- 결정론적 사유 코드와 실제 관측값·기준·출처를 연결해 보류 설명을 구현하는 방법, 통과/보류 테스트 기준을 명시했다.
- 실제 케이스 취득, Fluent/PyFluent/MCP/이벤트 조기 기술검증, 실무자 인터뷰, 2주 일정, 차별성·효용·위험·범위를 PRD로 정리했다.
- H200, GraphRAG, 자동 최적화와 검증되지 않은 소음 예측은 MVP에서 제외했다.
- Updated: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent PRD.md`, `index.md`

## [2026-09-26] update | 사람의 가설을 검토하는 프로펠러 에이전트 흐름 확정

- 사람이 가설·비교 목적·시험 조건·평가 지표를 제공하고, 에이전트가 기존 사례와 필요한 해석으로 검토한 뒤 사람이 최종 판단하도록 PRD와 제안서를 맞췄다.
- 사례 재사용을 직접 재사용, 참고 사례로 재사용, 재사용 불가·새 증거 필요의 세 단계로 정의하고 화면·보고서에 사유와 출처를 표시하도록 했다.
- 팀이 소음 사례를 확보할 때까지 소음 우열은 확정하지 않으며, 가설에 필요한 지표를 생성할 수 있는 CFD만 승인 후 실행하도록 범위를 명시했다.
- eVTOLUTION 데이터 링크를 v2로 갱신하고 수치 재계산 필요성을 표시했다.
- Updated: `Propeller Evidence Agent 1.md`, `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent PRD.md`, `index.md`

## [2026-09-26] create | Propeller Evidence Agent 팀 공유용 PRD

- 상세 PRD의 1~3장 핵심 정의와 기능을 유지하고, 나머지 내용을 시연 장면·성공 조건·남은 과제로 압축한 팀 공유용 파일을 만들었다.
- 상세 PRD는 그대로 두고 `index.md`에 공유본 링크를 추가했다.
- Created: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent 팀 공유용 PRD.md`

## [2026-09-26] update | 프로펠러 시제품 검증의 제조 접점과 공개 근거 보강

- 상세 PRD의 중심을 시제품 시험·재시험 판단으로 좁히고, 1차 사용자·결정 시점·Fluent 설치 확인 범위를 구분했다.
- NASA 제품 검증 지침과 X-57 후속 시험 사례, ENODISE·ENOLA 공개 데이터 후보 및 비교 가능성의 미검증 상태를 기록했다.
- 세 가지 재사용 경로와 사람 승인·실제 도구 실행을 발표용 Mermaid 도식으로 정리하고, 수동 대비 사람 개입 시간 측정 기준을 추가했다.
- Updated: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent PRD.md`, `index.md`, `log.md`

## [2026-09-27] update | 공개 프로펠러 실험 비교 후보와 데모 근거 구체화

- ENOLA 재료별 공통 RPM 하중 CSV, 음향 파일 목록·일부 헤더와 ENODISE 2cm/4cm 공통 RPM 소음 시험 목록·추력·README를 읽었다. 전체 음향 비교 및 불확실성은 아직 미검증이다.
- PRD에 A/B 재시험 대표 질문, 실측/CFD 비교의 구분, 데이터별 데모·한계·대체 자료와 핵심 링크 활용표를 추가했다.
- 원본 전체 ZIP 다운로드는 시간 초과; 필요한 소형 항목을 HTTP Range로 별도 확인했다. 원본은 수정하지 않았으며 Git pull/commit/push는 수행하지 않았다.
- Updated: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/Propeller Evidence Agent PRD.md`, `index.md`, `log.md`

## [2026-09-27] update | ENOLA 제작 재료·공법 변경 데모 채택 및 음향 계산 검증

- 사용자 합의로 ENOLA ABS/PA12·7350RPM 비교를 기본 시나리오로 확정하고 Resin을 참고 후보로 두었다.
- 완전 추출한 Mic1 음향 세 파일의 CRC32·시간축·유한값과 탐색 음압 계산을 확인했다. 재현 스크립트는 정현파 및 Parseval 검증을 통과했다.
- ICAS 2024 관련 논문의 제작법·측정 프로토콜을 읽고, 재료 단독 인과효과가 아닌 제작 방식 비교라는 점과 강체 CFD의 범위 한계를 기록했다.
- Excel 메타데이터 런타임 미연결 및 2025 확장 논문 접근 제한으로 미확인된 파일 매핑·교정·반복 조건은 남겨두었다.
- Added: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/ENOLA 음향 검토와 확정 데모 조건.md`, `70. Outputs/2026-09-23-Propeller-Evidence-Agent/scripts/analyze_enola_acoustics.py`
- Updated: 상세 PRD, `index.md`, `log.md`

## [2026-09-27] update | 품질 검토 타깃 확정과 개발계획서 사전 질문 준비

- 품질 엔지니어, 성능·소음 개선 목적의 제작 방식 변경, 제작·시험 후 다음 검토 단계 진행 판단을 PRD의 중심으로 반영했다.
- 절대 요구사항 충족과 기존품 대비 개선을 분리하고, 결정·미결 사항·증거 상태·재개 순서를 기록했다. 팀 공유본에 최신 기준 문서 안내를 추가했다.
- 사용자 제공 개발계획서 양식 항목을 기록했다. 요청에 따라 초안은 작성하지 않고 일정·역할·스택·판정 기준·목표를 질문한다.
- Updated: 상세 PRD, 팀 공유본, `index.md`, `log.md`

## [2026-09-27] create | 개발계획서 초안과 제출 일정 반영

- 사용자 답변에 따라 계획서 9/27·결과물 10/6·발표 10/12, 설치만 완료한 구현 상태, 모델 지원 미정·팀 예산 약 3만원을 반영했다.
- 김규태 연결/DB, 백창민 비교/데이터, 김석준 자문/수동 CFD 중심 역할과 최소 웹 UI를 제안으로 구분했다.
- 과제소개·기술 스택·개발방법·역할·일정·검증 목표를 제출 양식 순서로 작성했다. HWP 실제 페이지 검증과 제출은 수행하지 않았다.
- Added: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/개발계획서 초안.md`; Updated: PRD, `index.md`, `log.md`

## [2026-09-27] update | 로컬 웹 화면 결정 확정

- 사용자가 CLI 중심이 아닌 처음부터 웹 화면을 쓰기로 결정했다. Streamlit 최소 화면을 Windows 로컬에서 구동하고 브라우저로 접속하는 구조로 PRD/개발계획서에 반영했다.
- 클라우드 호스팅은 필요하지 않으며, LLM API를 쓰면 모델 지원 안내 후 원격 API 호출이 발생할 수 있음을 명시했다.
- Updated: PRD, 개발계획서 초안, `log.md`

## [2026-09-27] update | Fluent 케이스 검증 완료 상태 반영 및 모호성 점검

- 사용자가 시연용 Fluent 케이스 실행과 출력 지표 검증을 완료했다고 알려와 설치만 완료된 것으로 남은 문장을 정정했다.
- 독립 케이스 검증과 제품 내 승인형 Streamlit→PyFluent/MCP→SQLite 전체 연결은 구분했다. 재현용 케이스명·출력 지표·로그 기록 필요를 계획서에 표시했다.
- 남은 현장 정의(다음 검토 게이트, 요구사항 증거 기준)와 ENOLA 측정 매핑은 전문가 자문 항목으로 유지한다.
- Updated: PRD, 개발계획서 초안, `log.md`

## [2026-09-27] create | 개발계획서 HWP 붙여넣기용 Markdown

- 표 없이 양식 순서로 정리한 Markdown 본문을 만들고, 기존 TXT 초안은 대체했다.
- Fluent 검증 완료 보고와 제품 내 승인형 도구 호출 통합 미완료를 구분하고, 9/27 제출·10/6 결과물·10/12 발표 일정을 반영했다.
- Updated: `index.md`; Added: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/개발계획서 HWP 붙여넣기용.md`

## [2026-09-28] create | 금융 프로젝트 트랜잭션·동시성·아키텍처 학습 경로

- 현재 financial-lab 메모리 저장 단계와 다음 MySQL/JPA 단계를 바탕으로 원자성, rollback, concurrency control을 구분하고 검증 순서를 정리했다.
- DB 기초·트랜잭션에는 《데이터베이스 개론(4판)》, 소프트웨어 구조에는 《소프트웨어 아키텍처 The Basics(2판)》, 데이터 시스템 심화에는 DDIA 2판을 추천했다.
- Query saved: [[2026-09-28-Q-financial-ledger-transactions-and-architecture-learning]]
- Updated: `index.md`

## [2026-09-28] create | 금융권 백엔드 포트폴리오 레퍼런스 분석

- 사용자 목표를 여의도 금융권 백엔드 전반으로 설정하고, 합격자 자기 회고·증권사 전형 후기·공식 공고와 공고 미러·회사 기술 블로그·공개 저장소 32개를 근거 수준별로 분류했다.
- 합격 원인을 단정하지 않고, 프로젝트 역할 설명·금융 관심·이력서와 면접의 일관성·재현 가능한 기술 증거를 적용 원칙으로 정리했다.
- 2026-09-28 financial-lab 저장소를 읽기 전용으로 확인해 현재 구현을 메모리 기반 계좌 API로 한정했다. Wiki의 9/26 기록과 현재 테스트 파일 사이에 서비스 실패 테스트 범위 차이가 있음을 기록했다. 테스트 실행은 하지 않았다.
- 주 30시간을 반영한 금융 거래 정합성 중심 포트폴리오 V0.1, 현재 사용 가능한 이력서 문장, 검증 후 사용할 문장 틀을 작성했다.
- Query saved: [[2026-09-28-Q-financial-backend-portfolio-reference-analysis]]
- Updated: `index.md`, [[financial-lab]]

## [2026-09-28] create | 금융권 백엔드 이상형 포트폴리오 설계

- 사용자의 수정에 맞춰 current-state-first 접근을 바로잡고, 현재 프로젝트·시간을 설계 조건에서 제외한 이상형을 먼저 작성했다.
- 은행·결제·금융 백엔드 합격 회고, 공개 포트폴리오 walkthrough/PDF, 회사 기술 글, 이력서 리뷰 글을 실제 파일·자기회고·품질 기준으로 구분했다.
- 대표 프로젝트, 재현 가능한 기술 근거, 계층형 포트폴리오, 토스·카카오 수준을 목표로 하는 앵커 기술 글, 세 개 이력서 클리핑의 적용 규칙을 정리했다.
- 실제 지원자 포트폴리오 원본이 비공개이거나 이미지 내용이 열리지 않는 자료가 있어 표본과 인과관계의 한계를 Bias Check에 기록했다.
- Query saved: [[2026-09-28-Q-ideal-financial-backend-portfolio]]
- Updated: `index.md`, [[MOC-Portfolio]]

## [2026-09-28] create | 영상 기준 금융 포트폴리오 사례 비교

- 사용자가 지정한 영상 transcript를 읽고 포트폴리오를 제목·그림·문제·해결·결과의 반복 문제 해결 블록으로 재해석했다.
- 이체/원장, 결제/환불, 정산/대사를 같은 서술 틀로 비교하고, 선택을 강요하지 않고 검토할 수 있는 이체 중심 가설과 대안을 정리했다.
- Query saved: [[2026-09-28-Q-video-based-financial-portfolio-case-choice]]
- Updated: `index.md`, [[MOC-Portfolio]]

## [2026-09-28] review | 생각등대·코딩웨일 기준 이상형 포트폴리오 점검

- 사용자가 이체·원장을 중심에 두고 정산/대사를 문제 해결 사례로 연결하기로 결정했다.
- 생각등대의 제목·그림·문제·해결·결과 블록과 코딩웨일의 시장 정의·레퍼런스·이상형·현실 조정·현업 피드백 순서를 기준으로 현 설계의 적합성과 미완료 증거를 나눠 점검했다.
- 네 개 블록을 동시성, 부분 실패 rollback, 중복 재시도, SQL 정산 대사로 구분하고, 실제 도식·재현·측정과 공개 포트폴리오 원본 부족을 미완료 항목으로 기록했다.
- Query saved: [[2026-09-28-Q-ideal-portfolio-fit-audit]]
- Updated: `index.md`, [[MOC-Portfolio]], [[2026-09-28-Q-ideal-financial-backend-portfolio]], [[2026-09-28-Q-video-based-financial-portfolio-case-choice]]

## [2026-09-28] query | 국내 개발·AI 공모전 포트폴리오 적합도 비교

- 기존 9월 18일 기회 지도와 현재 사용자의 두 명 팀·개발 결과물 선호를 연결하고, 제시한 8개 대회의 산출물·접수 일정·포트폴리오 적합도를 비교했다.
- 경남 AI·SW와 고용24·사회문제 해결 챌린지는 실제 에이전트·서비스 구현, 빅콘테스트와 KISTI는 데이터·모델 분석, 핀테크는 아이디어·발표 중심으로 구분했다.
- 빅콘테스트는 참가 경험은 가능하지만 수상은 데이터 분석·문제 해석 경쟁이라 쉽다고 단정하지 않았고, 수상과 구현 프로젝트를 이력서에서 분리하도록 기록했다.
- Query saved: [[2026-09-28-Q-domestic-developer-competition-portfolio-fit]]
- Updated: `index.md`

## [2026-09-28] update | 금융 workload·TPS·인프라 한 줄 가정 추가

- 이력서 팁 클리핑의 지침에 맞춰 이체 중심 프로젝트에 예상 DAU, 이체량, 조회/이체 비율, 피크 API TPS, API·MySQL 초기 사양을 한 줄로 추가했다.
- 한국은행 2024 국내 지급결제동향의 일평균 입금이체 집계를 크기 비교에만 활용하고, DAU·피크 계수·노드 사양은 프로젝트 가정으로 구분했다.
- 가정 산식과 k6 측정 후 갱신 조건을 적고, 금융 데이터 정확성은 별도 통합·동시성 검증이 필요하다고 명시했다.
- 실제 파일명이 없는 클리핑 위키링크의 `1` 접미사를 정리했다.
- Updated: `index.md`, [[MOC-Portfolio]], [[2026-09-28-Q-ideal-financial-backend-portfolio]], [[2026-09-28-Q-ideal-portfolio-fit-audit]], [[2026-09-28-Q-financial-backend-portfolio-reference-analysis]]

## [2026-09-30] query | 금융 포트폴리오 진행과 이상형 보강

- 사용자가 기존 규모 가정의 수용과 Mac 저장소가 최신 작업본임을 확인했다. 읽기 전용 코드 확인에서 메모리 기반 계좌·이체와 정상 테스트 코드가 있으며 테스트 실행은 하지 않았다.
- 코딩웨일의 이상형 기획과 생각등대의 네 문제 해결 블록을 기준으로 진행 현황, 금융 업무 규칙, 실패 재현·대안 비교·복구·측정 증거와 제출 형태 초안을 보강했다.
- 영상 원문 기준과 금융 프로젝트에 적용한 추가 제안을 구분했다. 외부 정산 명세의 합성 모델은 아직 사용자와 정할 항목으로 유지한다.
- Query saved: [[2026-09-30-Q-portfolio-progress-and-ideal-quality-upgrade]]
- Updated: `index.md`, [[MOC-Portfolio]], [[2026-09-28-Q-ideal-financial-backend-portfolio]]

## [2026-09-30] query | AI·데이터 대회 추가 비교와 포트폴리오 적합도

- 새로 받은 KISTI·Croche·데이터안심구역·AI 활용 아이디어 공모전을 공식 공고 기준으로 정리하고, 앞서 비교한 후보와 접수 중인 고용24·스페이스 해커톤을 함께 비교했다.
- AI 활용 아이디어 공모전의 최우수상은 제보된 150만 원이 아니라 공식 PDF에 적힌 각 100만 원으로 정정했다. 수상과 채용 특전의 범위를 구분하고 승률을 추정하지 않았다.
- Query saved: [[2026-09-30-Q-ai-data-competition-expanded-comparison]]
- Updated: index.md

## [2026-09-30] query | 금융 프로젝트 최종 산출물·대표 글·협업 이상형

- 토스 정산 글과 카카오페이 성능 글, 공개 이력서 PDF·우리은행/KIDB 회고·리뷰 글을 다시 읽고 장점과 현재 초안의 실행 증거 공백을 비교했다.
- 한 개인 이체·원장 프로젝트 안의 네 사례와 별도 협업 프로젝트를 한 포트폴리오에 담는 구성을 제안하고, 실행·테스트·SQL·측정·복구·시연·대표 글의 완료 조건을 작성했다.
- 사용자는 협업 후보 선택 전에 이상형을 먼저 보기로 했으며, 마지막 페이지를 설명한 영상 출처는 나중에 제공하기로 했다. 현재 영상에 없는 지침을 작성자의 주장으로 귀속하지 않았다.
- Query saved: [[2026-09-30-Q-financial-portfolio-deliverables-and-reference-review]]
- Updated: index.md, [[MOC-Portfolio]], [[2026-09-28-Q-ideal-financial-backend-portfolio]]
## [2026-09-30] create | 현상분석3 ‘다음은?’ 작성 워크시트

- `7주 - 현상분석3 - 기술트렌드와 창업 - 2026.2학기.pdf`의 여섯 사례를 읽고, 기술·아이템 변화와 사용자 변화를 직접 분석할 빈칸을 만들었다.
- 정답이나 개인 의견은 대신 쓰지 않고, 근거·출처와 내 사례를 적을 칸을 추가했다.
- Saved: [[2026-09-30-Q-현상분석3-다음은-작성워크시트]]
- Updated: `index.md`

## [2026-09-30] update | 현상분석3 워크시트를 사용자 분석 틀에 맞춤

- 워크시트 항목을 `현상 → 개념 → 기술의 변화 → 누가? → 왜? → 다음은?`으로 재구성했다.
- 사용자가 작성한 게임 트렌드 초안을 해당 틀로 정리하고, 비교 게임 이름·근거·확인할 가설은 직접 채우도록 남겼다.
- PDF의 여섯 사례에도 같은 빈칸 항목을 적용했다.
- Updated: `index.md`, [[2026-09-30-Q-현상분석3-다음은-작성워크시트]]

## [2026-09-30] query | 중간발표 Muse 근거와 다음 단계

- 중간발표 PDF 2~3페이지를 확인하고, 사용자가 실제 과업 수행형 AI를 원한다는 주장을 Gartner의 3,566명 고객 조사로 보강했다.
- Sensor Tower의 다운로드 추정치와 미국 App Store 1위 시점을 분리했다. 약 73만 다운로드는 출시 초기 약 5일, 1위는 출시 10일 뒤로 정리했다.
- Meta의 Muse 기능·모델·데이터센터·글래스 계획과 OpenAI Dots 경쟁 사례를 연결해 ‘상시 접근 가능한 개인 에이전트’라는 다음 단계 가설 및 토론 질문을 작성했다.
- Saved: [[2026-09-30-Q-Muse-에이전트-근거와-다음-단계]]
- Updated: `index.md`

## [2026-10-01] build | CFD 자동화 공개 예제 확보 및 정적 검사

- 공식 Ansys 축류팬 케이스·메시, APC 형상/계산 성능 자료, OpenFOAM 프로펠러 예제, NASA X-57 GLB/VSP 모델을 실제 다운로드했다.
- 공식 케이스에서 버전 26.1과 셀 56,963개를 확인했다. 항공 프로펠러 케이스가 아니라 기술 연결 시험용 팬으로 분리했다.
- OpenFOAM 완성 메시 부재·STL watertight=false 및 HPC 예제의 실제 FFF.cas.h5 부재를 확인했다.
- Windows PyFluent 연결/RPM 재조회/짧은 계산 프로브를 준비했다. 이 Mac에서 Fluent 계산·수렴·물리적 타당성은 검증하지 못했다.
- Added: `70. Outputs/2026-09-23-Propeller-Evidence-Agent/cfd-demo-kit/README.md`, 다운로드·검사 스크립트, manifest/inspection, Windows 프로브.
- 기존 PRD와 사용자 변경은 보존했다. 원본 바이너리·계산 출력은 키트의 Git 추적 제외 규칙을 추가했다.

## [2026-10-01] query | 금융 백엔드 이상형 포트폴리오 제작본

- 코딩웨일의 이상형 선설계와 생각등대의 반복 사례 형식을 원문과 대조했다.
- 소개·개인 개요·동시성/원자성/멱등성/대사·협업 개요와 사례 후보를 작성했다. 구현 성과와 수치는 목표·빈칸으로 유지했다.
- 개인 업무 경계·합성 명세 독립성·협업 팀/사용자·실측·마지막 페이지를 미정 사항으로 기록했다. 내부 이체와 합성 명세 대사 범위를 사용자에게 확인 요청했다.
- Saved: [[2026-10-01-Q-ideal-portfolio-submission-draft]]
- Updated: [[MOC-Portfolio]], `index.md` (실제 Query 파일 84개 반영). 기존 작업은 보존했다.

## [2026-10-01] query | 연동·대사·팀장 역할·검증 구체화

- 금융결제원 개발자 테스트 안내와 실제 이용 신청/계약 절차를 확인했다. 특정 개인의 API 권한이나 기관 협력은 확약하지 않았다.
- 내부 원장 + 별도 모의 기관 연동·대사를 이상형 추천안으로 작성했다. 명세 계약·마감·미결·수정 버전 예시는 프로젝트 제안이다.
- 팀장 희망을 반영해 팀장 + 핵심 백엔드 모듈 책임을 추천하고, 실측·기여 근거를 정리했다.
- Saved: [[2026-10-01-Q-financial-portfolio-integration-reconciliation-and-review]]
- Updated: [[2026-10-01-Q-ideal-portfolio-submission-draft]], [[MOC-Portfolio]], `index.md`.

## [2026-10-01] update | TOEIC Speaking IH 목표와 단기 준비 기준

- 금융 시스템 개발자 취업 로드맵의 어학 목표를 TOEIC Speaking IH 140점 이상으로 확정했다.
- 첫 시험 전 10~14일, 하루 90~120분 집중 훈련과 IM3 취득 시 한 차례 단기 재응시 기준을 추가했다.
- IH 취득 즉시 어학 집중을 종료하고 Java·Spring·SQL·코딩테스트로 시간을 돌리도록 명시했다.
- Updated: [[김규태 금융 시스템 개발자 취업 로드맵]], `index.md`

## [2026-10-06] sync | Git pull 및 qmd 재색인

- `cmds-llm-wiki/main`의 커밋 2개를 fast-forward로 반영했다. HEAD: `69626d9`.
- 기존 로컬 작업은 stash로 백업하고 복원했다. 로드맵·MOC·index·log 충돌은 양쪽 기록을 보존해 해결했으며 백업 stash는 유지했다.
- `index.md`의 문서 수를 실제 파일 수로 갱신하고 qmd의 wiki·raw_sources·queries 텍스트 색인을 갱신했다: 총 249개 문서.
- `qmd embed` 완료: 83개 문서에서 571개 청크 임베딩 생성, 오류 없이 종료.

## [2026-10-06] create | FastReqs 프로젝트 기준 문서 및 WBS 검토본

- 제안서·강의 자료와 사용자 대화를 바탕으로 최신 범위·실행 조건·승인·문서·시연 기준·미결 기술 항목을 프로젝트 기준 MD에 정리했다.
- 연구실 PC의 상시 봇과 사용자 CLI 실행 중에만 가능한 로컬 문서 수정, 종료 중 대화 보관·재연결 조건을 반영했다. 별도 백그라운드 연결 프로그램은 제외한다.
- 완료된 제안서 1개와 신규 작업 30개의 레벨 0/1/2 트리·표형 WBS를 작성했다. 신규 노력 90시간·임시 담당·API 30,000원은 검증 전 계획이며 개발 완료를 뜻하지 않는다.
- 7페이지 PDF의 모든 페이지를 렌더링하여 확인했다. XLSX는 필수 제작 런타임 로더가 없어 생성하지 못했으며 편집용 WBS Markdown을 제공했다.
- Added: `70. Outputs/2026-10-06-FastReqs/FastReqs 프로젝트 기준 문서.md`, `FastReqs WBS 계획과 진척.md`, `FastReqs WBS 검토본.pdf`.
- Updated: `index.md`. 과목 작업 노트·Raw Sources·기존 로컬 작업은 수정하지 않았다.

## [2026-10-06] edit | FastReqs WBS 트리·표 형식 수정

- 사용자 강의 예시처럼 전체 목표 아래 단계들을 배치하고, 각 단계 아래에 동급 작업들을 가로로 펼치는 수직 계층 트리로 수정했다.
- 표를 ID·선행 작업 ID·작업 완료도·작업 이름·기간·시작 날짜·완료 날짜 순서의 7개 열로 변경했다. 담당·API 예산·노력·별도 상태·완료 기준 열은 제거했다.
- 제안서 100%, 나머지 0%로 표시하고 기간은 시작·완료일을 포함한 달력 일수로 계산했다. 계획 일정과 기존 작업 이름은 유지했다.
- WBS Markdown과 PDF를 갱신하고 변경 페이지를 렌더링하여 확인했다.

## [2026-10-06] edit | FastReqs 작업별 기간 차등화

- 신규 작업의 달력 기간을 성격에 따라 1~6일로 차등화하고 시작·완료 날짜를 함께 조정했다. 기존 주별 배정·최종 마감은 유지했다.
- 선행 작업 완료 다음 날 이후 시작하는 관계와 담당자별 주간 가용량을 확인했다. 기간은 검증 전 일정 추정이며 노력 시간과 구분한다.
- 수직 계층 트리의 폭을 줄이는 배치 대안을 사용자에게 설명했다. 이번 수정은 일정표에 적용했다.

## [2026-10-06] edit | FastReqs 전체 개요와 단계별 상세 트리 분리

- 전체 목표와 다섯 단계만 담은 개요 1장, 각 단계 작업을 담은 상세 트리 5장으로 분리했다.
- 넓었던 트리 페이지를 가로 A3로 통일했다. 기존 진척 설명과 작업표를 포함한 PDF는 총 12페이지다.
- WBS Markdown에 새 페이지 구성을 기록했다. 작업 ID·기간·날짜·완료도는 유지했다.

## [2026-10-06] edit | FastReqs 작업 우선순위 추가

- 작업 완료도 뒤에 우선순위 열을 추가했다. 착수 선행 결정·마감·핵심 동작·승인 안전성을 높음, 보완·검사·운영을 보통, 완료 제안서·보고 정리를 낮음으로 차등 적용했다.
- 분류는 팀 검토용 제안이며 낮은 우선순위도 필수 범위임을 표시했다. 기존 선행 관계·기간·날짜·완료도는 유지했다.
- PDF와 편집용 Markdown을 함께 갱신했다.

## [2026-10-06] edit | FastReqs 제출용 Markdown 정리 및 HTML 생성

- 계획과 진척 MD에서 설명문·메타데이터·자원·비용·진척 해설을 제거하고 텍스트 트리·Mermaid 트리·작업표만 남겼다. 텍스트 트리는 사용자 추가 지시에 따라 보존했다.
- 외부 라이브러리 없이 열 수 있는 HTML을 생성했다. 전체 목표 아래 다섯 단계, 각 단계 아래 동급 작업을 세로로 배치해 화면 폭을 줄였다.
- 작업표의 ID·선행 작업 ID·완료도·우선순위·작업 이름·기간·날짜를 유지했다. 프로젝트 기준 MD와 기존 PDF는 수정하지 않았다.
- Added: `70. Outputs/2026-10-06-FastReqs/FastReqs 작업분할도.html`. Updated: 계획과 진척 MD, `index.md`.

## [2026-10-06] edit | HTML에 텍스트형 작업분할도 추가

- 사용자 요청에 따라 HTML에 기존 텍스트 트리를 별도 섹션으로 추가했다.
- 텍스트 트리·한눈에 보는 시각 트리·표형 작업분할도가 HTML에 모두 표시된다.

## [2026-10-06] edit | WBS 목표 제목 및 개발 단계 재구성

- 전체 목표를 `요구사항 관리 Slack 봇 개발`로 바꾸고 레벨 1을 요구분석·설계·코딩·테스트 네 단계로 재구성했다.
- 기존 31개 작업을 성격에 맞게 재배치·표현 수정하고 작업 ID와 모든 선행 작업 참조를 함께 갱신했다. 날짜·기간·우선순위·완료도는 유지했다.
- 계획과 진척 MD의 텍스트 트리·Mermaid·표, HTML의 텍스트 트리·시각 트리·표를 같은 구조로 반영했다. 코딩 작업은 화면에서 두 열로 배치했다.
- 프로젝트 기준 문서의 WBS 규칙과 index 링크 설명을 최신 구성으로 갱신했다.

## [2026-10-06] edit | 코딩 작업 압축 및 설계 작업 보강

- 코딩 17개를 기능별 핵심 작업 7개로 묶었다. 요구사항 질문·최초 문서 생성·승인 보호·회의 처리·충돌 해결·비용 처리는 해당 묶음에 포함했다.
- 설계에 대화·승인 흐름 설계와 AI 분석·회의·충돌 검사 설계를 추가했다. 전체 작업은 요구분석 6개·설계 4개·코딩 7개·테스트 6개로 총 23개다.
- 텍스트 트리·Mermaid·HTML 트리·표를 함께 갱신하고 병합 작업의 기간·날짜와 테스트 선행 ID를 재정리했다.
- HTML의 코딩 두 열 배치를 제거해 네 단계가 동일한 열 너비로 보이게 했다. 프로젝트 기준 문서에 병합 범위와 재추정 필요 사항을 기록했다.

## [2026-10-06] query | 금융 포트폴리오 2쪽·k6·거래 대사 기준

- 사용자 정정에 따라 연구실 요청 자료·문안·관련 안내를 제거했다. 삭제 범위는 해당 포트폴리오 문서이며 별도의 실제 연구 활동 기록은 대상이 아니다.
- 생각등대 보유 영상 원문에서 약 네 문제 해결 블록을 확인했다. 프로젝트 2~3개·전체 2쪽 발언의 직접 출처는 확보하지 못했다.
- 개인·협업 2개 프로젝트의 2쪽 편집 원고를 작성했다. 기존 긴 원고는 상세 기록으로 표시했다. PDF 렌더링·실제 페이지 검증은 수행하지 않았다.
- TinyFish로 Grafana k6와 한국은행·금융결제원 자료를 확인하고 부하 생성·모의 기관·SQL 검증 및 고객 거래/기관 간 결제/명세 마감의 차이를 정리했다.
- Saved: [[2026-10-06-Q-two-page-financial-portfolio-k6-and-domain-rules]]
- Added: `70. Outputs/2026-10-06-Financial-Portfolio/금융 백엔드 포트폴리오 2쪽 원고.md`
- Updated: 기존 포트폴리오 Query 2개, [[MOC-Portfolio]], `index.md` (실제 Query 파일 90개).

## [2026-10-06] query | 아키텍처·대표 기술 글·금융권 지원 목표 보강

- 세 상자 요약을 API·DB·영속 작업·독립 모의 기관·명세·대사·복구가 보이는 구조로 교체하고 상세 설계 문서를 추가했다. 모두 구현 전 목표이며 외부 HTTP와 DB의 원자성을 혼동하지 않도록 구분했다.
- 토스·카카오뱅크 공식 기술 글을 확인해 응답 유실 거래의 확인·복구를 대표 글의 중심 질문으로 정하고 3~4주 실험·집필 계획을 작성했다.
- 우리은행·신한은행 신입 및 하나은행 인턴 합격 회고를 비교했다. 자기 보고·직무·고용 형태·표본 한계를 표시하고 증권사 백엔드 합격선으로 환산하지 않았다.
- 공식 신한투자증권 공고의 ICT 우대 자격과 기존 어학 결정을 함께 고려해 정보처리기사·SQLD·Speaking IH를 목표로 표시했다. 협업은 금융 여부보다 직접 구현·리뷰·통합·실사용 증거를 우선한다.
- Saved: [[2026-10-06-Q-portfolio-architecture-technical-article-and-target-profile]]
- Updated: 금융 백엔드 포트폴리오 2쪽 편집 원고, [[MOC-Portfolio]], `index.md` (재집계한 실제 Query 파일 90개; 직전 기록의 개수는 당시 오집계). PDF 렌더링·실제 페이지 수 검증은 수행하지 않았다.

## [2026-10-07] query | 대표 글 일곱 절과 주제 선택 근거 구체화

- 동시성·응답 유실 복구·대사 SQL·전체 구축기 후보를 비교하고 개인 이체 원장과 협업 데이터 서비스 후보의 선택 이유를 정리했다. 협업 주제는 미정으로 유지했다.
- 일곱 절마다 독자 질문·실패 재현·요청 키/DB 경계·대안·반례·비교 조건·복구/한계와 첨부 증거를 작성했다. 실제 장애와 실험용 비교 구현을 구분했다.
- 개선 전후에는 동일한 기관 키/조회 계약을 유지하고 HTTP 성공과 실제 거래 효과를 구분하도록 명시했다. 구현·측정 수치와 실제 사용 명령은 미완료로 유지했다.
- TinyFish로 신한투자증권 공식 공고의 ICT 관련 자격 우대를 다시 확인했다. 정보처리기사·SQLD는 실제 취득 시 마지막 보조 정보에 표기하도록 반영했다.
- Saved: [[거래 원장 실험과 대표 기술 글 계획]]
- Updated: 대표 글 개요 Query, 금융 포트폴리오 편집 원고, [[금융권 백엔드 목표 포트폴리오를 역설계하는 법]], [[MOC-Portfolio]], `index.md`. 실제 Query 파일 91개. 프로젝트 구현·실험 실행은 수행하지 않았다.

## [2026-10-10] update | financial-lab 개발·학습 길잡이 목적 확정

- 대표 글 상세 계획을 개발·공부 중 반복 참조하는 길잡이로 명시하고 제출본·실제 기술 글과 구분했다. 제출본에는 대표 글 직접 링크로 연결한다.
- 개인의 규칙·실패 재현·탐지·복구·종료 검증·재발 대응 범위를 모의 기관 사례로 설명했다.
- 내부 이체→중복 요청→기관 계약·미확정→대사·복구→측정·집필 순서와 다음 논의 질문을 추가했다. 협업 미정·비교용 구현 표시·동일 기관 계약·자격 한 줄 표기는 유지했다.
- Updated: [[거래 원장 실험과 대표 기술 글 계획]], 금융 포트폴리오 편집 원고, [[MOC-Portfolio]], `index.md`. 구현·실험은 실행하지 않았다.
 
## [2026-10-11] ingest | ideal 이력서와 포트폴리오 구성 참고

- Source: https://www.youtube.com/shorts/j8Ex1YPd1QY — 제목 확인, 전체 영상 자막 미확보. 사용자 메모와 첨부 화면을 Clippings 원문으로 보존했다.
- Purpose: 현재 ideal 포트폴리오와 기존 포트폴리오 기반 이력서 제작의 분량·가독성·구성 참고. 사용자가 이미 명시한 목적을 기록했다.
- Created: [[2026-10-11-YouTube-Resume-Portfolio-Difference-Reference]], [[이력서는 프로젝트 포트폴리오는 문제 해결로 구성한다]]. 이미지 원본은 `80. References/Attachments/2026-10-11-Resume-Project-Reference.png`에 복사했다.
- Updated: [[MOC-Portfolio]], [[금융권 백엔드 목표 포트폴리오를 역설계하는 법]], 기존 금융 포트폴리오 2쪽 원고, `index.md`.
- 현재 기준: 이력서 2장·프로젝트 나열·항목 1~2줄·프로젝트 약 7줄, 포트폴리오 5장·대표 문제 해결 경험 나열. 이전 포트폴리오 2쪽 결정은 과거 기준으로 표시했다.
- Mothership: standalone로 미적용. 실제 이력서·5장 포트폴리오 제작 및 PDF 렌더링은 이번 인제스트 범위에 포함하지 않았다.

## [2026-10-11] ingest | 취업·이력서·포트폴리오 Clippings 전체 선별

- Purpose: 사용자 선택 “현재 ideal 이력서·포트폴리오를 다듬는 참고 기준으로 활용”. 목적 질문을 먼저 받고 답변 후 인제스트했다.
- Scope: Clippings 36개 중 관련 23개 파일, 같은 원문의 중복 2쌍을 합쳐 영상 21개. 신규 Raw Source 19개·기존 원문 2개 재사용. 넥슨은 기존 URL 기록에 전체 로컬 자막과 추가 메모를 보완했다. 다른 분야 13개는 이번 범위에서 제외했다.
- Raw originals: 신규 19개 모두 `## Original Content` 본문이 업로드한 원문과 일치함을 확인했다. Clippings 36개 원본과 Inbox는 그대로 유지했다. 교수버튜버 자료의 기존 본문 재사용 시 frontmatter는 기존 수집 메타데이터를 유지했다.
- Created Wiki (6): [[ideal 이력서와 포트폴리오 참고 영상 활용 지도]], [[이력서 문장은 문제 해결 결과 도메인으로 압축한다]], [[포트폴리오 문제 해결 블록과 그림을 편집하는 법]], [[포트폴리오 트래픽 가정과 측정 결과를 구분하는 법]], [[취업 스펙은 공고와 프로젝트 증거에 맞춰 배치한다]], [[대표 프로젝트 설명과 피드백으로 지원 문서를 개선한다]].
- Updated Wiki (7): 이력서/포트폴리오 구성 기준, 첫 페이지·대표 증거, 지원동기, AI 주니어 판단, AI-Augmented 포지셔닝, 금융 목표 역설계, MOC-Portfolio. 기존 2쪽 편집 원고에 활용 지도 링크를 추가했다.
- Evidence boundary: 영상 재생·게시일·자막 정확성·채용 효과는 미검증이다. 영어·오탈자·상충 조언은 보존하고, 넥슨 자막 뒤의 개인 메모와 프롬프트는 영상 발언과 분리했다. 6~8줄·약 4블록·측정 조건을 참고하며 사용자 결정 2장 이력서/5장 포트폴리오를 유지했다.
- Validation: YAML 파싱과 연결 링크, 원문 일치 검증 통과. 4개 짧은 완전한 자막은 기존 훅의 20개 비어 있지 않은 줄 조건에 걸렸으나 업로드 원문 전체의 일치 검증으로 누락 없음을 확인했다. 원문에 내용을 덧붙이거나 검증 훅을 변경하지 않았다.
- Index: Raw Sources 90, Wiki 98 (Concepts 46 / Entities 15 / Guides 31 / MOCs 6), Queries 91. Mothership 없음(standalone). 실제 이력서·5장 제출본 제작과 프로젝트 구현·측정은 수행하지 않았다.
- Search: `qmd update` 완료 (Wiki 6 new / 7 updated, Raw Sources 19 new). 활용 지도 검색 확인. `qmd embed` 실행 후 모델 초기화 단계에서 아직 진행 중인 상태를 확인했다.

## [2026-10-11] query | 5장 복원 검토와 거래 확정 기준

이력서/포트폴리오 정합성 검토: 개인 대표 사례→3~4장, 기본기→1~2장, 협업→5장 연결을 명시했다. 동시성과 원자성 중복·부하 지표 누락·내부/외부 응답 유실 경계를 정리하고 동일 실험/조건/수치 사용을 명시했다. 새 GitHub 프로필 링크를 반영했다. 실제 성과·PDF 검증은 수행하지 않았다.

추가 검토: 장애 복구 설계와 실험 계획을 개인 네 사례에 맞춰 압축했다. 이전 2쪽 참조·자격/협업 후보/주제 배경·반복 그림을 제거하고 설계는 경계/상태/계약, 실험은 실패 행렬/독립 검증/측정/증거로 구분했다. 내부 멱등성과 외부 기관 확장은 구분 유지했다. 코드 실행은 하지 않았다.

사용자 후속 요청으로 별도 에이전트 개발 길잡이 파일을 삭제하고 현재 링크를 제거했다. 5장 포트폴리오를 목표 맥락으로 제공하고 실제 코드·설정·테스트로 현재 상태를 확인하는 방식을 채택했다. GitHub 저장소 생성은 gh 인증이 HTTP 401로 실패하여 수행하지 못했다. 토큰 내용은 출력하지 않았다.

추가 확정: 개인4장/협업1장으로 변경하고 원자성 블록에 실패 위치·예외 전파·rollback 조건·별도 DB 연결 재조회를 추가했다. 에이전트 개발 길잡이를 작성했다. financial-lab의 AccountService/AccountTest/build.gradle을 읽었으며 테스트는 실행하지 않았다. 현재 원격은 gyutaetae/financial-lab이며 사용자 요청 gyugyutae와 달라 대상 URL을 질문했다. 푸시는 아직 수행하지 않았다.

후속 포맷 확정: 영상 fu9ZN8-xdnk의 보존된 로컬 자막을 확인하고 5장 원고를 추가했다. 개인 3블록·협업 1블록에 제목→그림→문제 원인(약 3줄)→해결 과정(약 3~4줄)→결과를 반복한다. 결과에 환경·서버·요청·기간·반복·정확성·변화·한계를 포함한다. 협업 주제·성과 수치는 미확정이며 실제 페이지 배치는 하지 않았다. Updated: 편집 Wiki, 검토 Query, `index.md`.

후속 사용자 확정: 이력서는 첫 번째 문제 해결형으로 개인/팀 각각 대표 사례를 선택한다. 포트폴리오 표지·보조 정보 제외, 노션 A3·크기83 설정을 채택한다. 이력서 2장 목표 원고를 추가하고 5장 구성은 개인 3장·협업 2장으로 수정했다. 신입 기본기와 본인 구현·검증의 증거를 사례 안에 포함한다. 실제 PDF·프로젝트 결과는 미검증이다.

- 새 인제스트 활용 지도·사례 편집·이력서 문장·스펙·트래픽·피드백 Wiki를 읽고 이전 긴 원고와 압축 원고를 비교했다.
- 이력서 2장·포트폴리오 5장 배치안과 경합 비교·rollback·요청 키·대사 SQL·협업 기여의 복원 항목을 저장했다. 새 제출 PDF를 제작한 것은 아니다.
- 모의 기관의 최종 결과·조회·명세 계약을 근거로 확정/예약 해제를 판단하는 안을 작성했다. 타임아웃·부재·시간 경과는 확정 거절과 구분한다.
- Saved: [[2026-10-11-Q-five-page-portfolio-review-and-confirmation-rules]]. Updated: 개발·학습 길잡이, [[MOC-Portfolio]], `index.md`. Query 92개. A3·83 설정과 5장 포함 범위는 사용자 답변 대기 중이다.

## [2026-10-11] lint | Clippings와 루트 정리 가능 여부 점검

- 요청 범위: 삭제 가능 여부 점검. 실제 삭제·이동·Obsidian 설정 변경은 수행하지 않았다.
- Clippings 37개 중 원문 보존 완료 26개, 미보존 11개. 완료 26개 중 기존 Query의 직접 링크가 있는 4개는 Raw Source로 링크 전환 후 정리해야 한다. 나머지 22개는 본문 보존과 직접 링크 점검상 정리 후보다.
- 루트 이미지 16개(9.43 MiB)는 모두 문서 참조가 있으며 볼트 내 동일 해시의 별도 이미지 사본이 없다. 삭제 대신 첨부 폴더로 이동하며 링크 점검을 권한다. 수업 작업본은 스냅샷 이후 변경되어 유지한다.
- 빈 Markdown 3개·빈 Canvas 1개·macOS 캐시는 정리 후보. 교수버튜버·러팅 원문은 Raw Source 본문과 같으며 작업본으로 쓰지 않는다면 중복 정리 후보다. 내용이 있는 다른 계획·학습 문서는 유지한다.
- 이전 인제스트 오류 보완: 제목 선별에서 누락된 자기소개 영상 [[2026-10-11-YouTube-자기소개 5분만에 써드립니다. 그냥 가져가세요.]]의 원문을 동일한 사용자 목적에 따라 보존했다. 지원동기 문서의 잘못된 출처 표기를 고치고 활용 지도·MOC·통계를 정정했다. 취업 묶음 최종 24개 파일/22개 영상, 신규20개/기존2개다.
- 점검 상세는 임시 산출물 `/tmp/cmds-llm-wiki-cleanup-audit-2026-10-11.md`에 기록했다. Raw Sources 91, Wiki 98, Queries 92. 볼트 전체 lint가 아니라 삭제 판단에 필요한 루트·클리핑 원문과 링크를 점검했다.


## [2026-10-11] ingest | 원문 보존 후 클리핑과 루트 정리

- 사용자 진행 요청에 따라 기존 보존 26개를 재검사하고 미보존 11개를 Raw Source로 추가했다. 신규 11개는 원래 YAML을 포함한 파일 전체를 Original Content에 보존했다. 설명만 있는 2개는 description-only로 표시했으며 영상 전체 자막을 수집한 것으로 간주하지 않는다.
- 기존 Query 8개에서 Clipping 링크를 대응 Raw Source로 변경했다. 기존 4개 직접 참조 자료는 이미 보존되어 있어 중복 인제스트하지 않았다.
- Clippings 37개는 원문 확인 후 .trash/2026-10-11-cleanup/Clippings로 옮긴다. 원래 파일의 메타데이터와 바이트도 복구할 수 있다. 빈 노트·빈 Canvas·DS_Store도 같은 정리 보관함으로 옮긴다.
- 루트 이미지 16개의 원본 바이트를 첨부 폴더에 보존하고 [[2026-10-11-Root-Note-Image-Archive]]에 임베드했다. 12개는 이동, 상대경로 참조 4개는 루트에도 유지하여 작업 노트를 바꾸지 않는다. 향후 기본 첨부 경로도 첨부 폴더로 지정했다.
- 새 [[클리핑 원문 보존과 재사용 지도]]와 index를 갱신했다. standalone이므로 모선 검색 없음. 작업 노트 변경 없이 원문·이미지 해시와 링크를 확인한다. 검색 색인 결과는 후속 검증에 기록한다.
- 검증 완료: 신규 YAML·연결 링크·원문 일치·이미지 해시·작업 노트 무변경 확인. 빈 Markdown 3개, 빈 Canvas 1개, DS_Store 5개 정리. qmd update 완료: Wiki 1개 신규, Raw Source 12개 신규, Query 8개 갱신. 벡터 임베딩은 이번 작업에서 갱신하지 않았다. 최종 Raw Sources 103 / Wiki 99 / Queries 92.

## [2026-10-11] cleanup | 루트 중복 노트 제거

- 루트 21개 일반 파일과 숨김 설정 2개를 확인했다. 교수버튜버 진로 노트와 러팅 노트는 Raw Source Original Content와 본문이 일치하고 직접 wikilink가 없음을 확인한 후 .trash/2026-10-11-cleanup/root-duplicates로 옮겼다.
- 나머지 운영 문서·작업 노트·상대경로 이미지 3개는 유지했다. log 외 나머지 루트 파일의 해시 무변경을 확인했다. Raw Source·Wiki 수에 변화가 없으므로 index 통계는 유지한다.

## [2026-10-12] query | UNLV 연수 다섯 목표와 네트워킹·AI 평가 기술

- 사용자 요청에 따라 [[2026-10-12-UNLV-연수에서-얻어올-다섯가지]]를 70. Outputs에 별도 저장했다. 다섯 목표에 체크리스트·완료 기준·현지 기록 양식을 붙였으며 아직 완료 실적이 아닌 실행 계획으로 표시했다.
- [[2026-10-12-Q-unlv-networking-evidence-wiki-and-ai-tools]]에 실력과 네트워킹의 역할, 2022년 LinkedIn 실험의 적용 한계, Evidence Wiki 평가 루프와 공식 문서 기반 기술 후보를 저장했다.
- [[LLM Wiki Pattern]]에 기록과 실행 평가의 구분을 추가하고 [[MOC-LLM Wiki Guide]]·index를 연결했다. 기존 partial 검증 상태와 explored: false를 유지한다.
- Raw Source 원문·기존 사용자 작업은 수정하지 않았다. Raw Sources 103 / Wiki 99 / Queries 93. 평가 도구 설치·실험·실측 결과 생성은 수행하지 않았다.
- 검증: 변경 문서 YAML 파싱, 신규 문서 wikilink 대상, 다섯 목표 개수, 신규 문서 공백 검사 통과. 검색 인덱스·벡터 임베딩 갱신은 이번 작업 범위에 포함하지 않았다.

## [2026-10-12] ingest | 금융 Java 포트폴리오 3·4단계 성장 목적

- 사용자 제공 목적을 그대로 사용: 현재 2단계 정도라는 자기평가에서 해결 방식의 차이와 환경·제약·선택·트레이드오프 설명으로 성장한다. 추가 목적 질문 없이 이미 주어진 답을 collectionPurpose에 기록했다.
- [[2026-10-12-YouTube-개발자 이력서 4단계와 금융 Java 성장 목적]]에 Clippings/(5) YouTube.md 전체와 사용자 목적을 분리 보존했다. 원본 파일은 유지했다. 외부 영상 제목·발표자·자막은 재검증하지 않았다.
- [[금융 Java 포트폴리오에서 해결 차이와 트레이드오프를 증명하는 법]] 생성, MOC-Portfolio·index 연결. 기존 네 금융 사례에 반례·대안·선택 비용·증거 기준을 연결했다. 원자성 한 사례를 첫 실행 후보로 두되 최신 코드 확인을 선행한다. 신규 구현·실험 성과나 현재 단계 인증은 아니다.
- standalone 모드로 모선 연결 없음. Raw Sources 104 / Wiki 100 / Guides 33 / Queries 93.
- 검증: Original Content와 원본 전체 내용 일치(말미 개행 제외), 신규 YAML·wikilink·실제 파일 수 확인. raw-source hook은 20줄 하한에 걸려 실패했다(원문 16개 비어 있지 않은 줄). 전문 일치를 별도 확인했으며 하한 통과를 위해 원문을 늘리거나 변경하지 않았다.
- qmd update 완료. 벡터 임베딩 갱신은 수행하지 않았다. 기존 로컬 변경은 보존했다.

## [2026-10-12] ingest | 예상 금융 서비스·부하에서 예방과 비용을 설명하기

- 사용자 제공 다섯 목적을 [[2026-10-12-YouTube-이력서에 문제 해결을 쓸 수가 없어요-예상 환경과 예방]]에 원문으로 보존하고 collectionPurpose에 기록했다. Clippings 원본은 유지했다. 제공된 영어 자막 전체를 Original Content로 보존하며 영상 재생/번역 대조는 하지 않았다.
- [[포트폴리오 트래픽 가정과 측정 결과를 구분하는 법]]을 보강: 서비스 후보·회원/DAU/행동량·피크 산식·예방 실험·단일 인스턴스/다중 인스턴스 용량·노드 기반 비용·이력서 표현을 연결했다. MOC-Portfolio·index·5장 목표 원고에도 목적을 연결했다.
- 313 API RPS/52 이체 TPS의 기준 계산은 확인했으나 수요 근거나 성능을 검증한 것은 아니다. 회원 수·활성 비율·SLO·클라우드 상품/리전은 미확정으로 유지했다. 선형 배수·효율·여유율 예시는 추정이고 완료 성과가 아니다.
- TinyFish로 Kubernetes 자원 관리와 Grafana k6 부하 모델 공식 문서를 확인해 가이드에 출처를 연결했다. 이번 작업은 부하 테스트·코드 변경·클라우드 구매/배포·가격 견적 실행이 아니다.
- standalone 모드로 모선 연결 없음. Raw Sources 105 / Wiki 100 / Queries 93. 원문 일치·YAML·연결·통계와 검색 색인 상태는 후속 검증에 기록한다.

## [2026-10-14] sync | 금융 원고 동기화와 피크 근거·검증 점검

- 사용자 요청으로 ideal-portfolio의 이력서·5장 포트폴리오·실험 계획을 Obsidian의 대응 Output 2개·Query 1개와 동일하게 반영한다. 개인 간 송금 서비스 방향은 사용자 결정이며, 해결 차이·제약/대안·선택 비용·정확성/지연/자원을 연결한다.
- 금융권 전국 통계와 카카오페이 온라인 결제·성능 테스트 공식 사례를 실험 계획에 링크했다. 전국 일평균과 결제 이벤트 사례를 개인 간 송금의 관측 피크로 승격하지 않는다.
- 기존 104.2 RPS 목표 대비 100 RPS 검증의 부족을 명시했다. 집중 비율/시간에 따른 100/200 RPS, SLO·자원·지속/급증/회복은 논의 중인 검토안이다. 실제 최대 피크 예측·실험 통과 성과가 아니다.
- 코드의 메모리 기반 초기 상태는 2026-10-14 읽기 전용 점검을 따르며 코드 변경·부하 실행·클라우드 구매/배포는 하지 않았다. 기존 Raw Source·가이드의 로컬 변경은 보존한다.
- index의 이전 개인 3블록 표기를 4블록으로 바로잡고 원고/실험 링크 설명을 갱신했다. 파일 수 변화 없음. 동기화·링크·형식·검색 색인 결과는 검증 후 기록한다.
- 검증 완료: 원고 3쌍의 SHA256 동일, YAML·wikilink·코드 블록·100/200 RPS 산식·양쪽 변경 파일 공백 검사 통과. qmd update 완료; 벡터 임베딩은 미갱신이며 Outputs는 기본 검색 컬렉션 밖이다.

## [2026-10-14] query | 금융 원고 최종 점검과 생각등대 조언 대조

- [[2026-10-14-Q-financial-portfolio-final-review-and-video-alignment]]에 이력서·포트폴리오·아키텍처·실험 계획과 현재 초기 코드의 차이, 제출 전 빈틈, 영상 조언 반영 상태를 저장했다. 금융권 공통 채점표·합격 판정이 아니라 로컬 자료 기반 리뷰다.
- 핵심 영상의 문제 해결 구조·3/4단계·가정에 따른 예방·대표 글/압축·신입 기본기 조언을 가이드와 원문 구간으로 대조했다. 전체 영상 재생·자막 원어 검증·실험 실행·PDF 제작은 하지 않았다.
- 기존 가이드의 개인 3장/협업 2장과 이력서 프로젝트 나열 표기를 현재 개인 4장/협업 1장·대표 문제 해결형으로 정정하고 최근 두 소스/최종 점검을 연결했다. index·MOC도 연결했다.
- 제출 전 실제 결과·본인 선택/기여·정상 피크 모델·협업 사례·직접 링크·PDF 가독성이 남는다. 원고 3쌍의 동일성을 확인했으며 이번 리뷰에서 원고나 financial-lab 코드는 변경하지 않았다.
- Queries 94, 나머지 수량 변화 없음. YAML·wikilink·공백·검색 색인은 후속 검증한다.
- 검증 완료: 신규 점검 문서 YAML·wikilink·Query 수량, 변경 파일 공백 검사 통과. qmd update 완료, 벡터 임베딩 미갱신.

## [2026-10-14] rename | 실험·대표 글 계획 한국어 이름과 문서 역할 점검

- 사용자 요청으로 바탕화면 ideal-portfolio와 Obsidian Query의 영문 파일명을 거래 원장 실험과 대표 기술 글 계획.md로 변경했다. 본문 제목·README 링크·Wiki/Output/Query/index/log 참조를 갱신했다. 기존 영문 이름은 alias로 남겨 외부/과거 wikilink를 보존한다. Raw Sources와 보관함 원문은 수정하지 않았다.
- 두 보조 문서의 본문·목차를 비교했다. 설계는 상태/계약/경계/복구 규칙, 실험은 실패 주입/측정/부하/비용/대표 글을 맡는다. 같은 사례를 언급하지만 동일한 긴 문장 반복은 없고 주요 역할이 달라 분리 유지를 권한다. README에 수정 책임과 설계→검증→설계 갱신 흐름을 기록했다.
- 이 작업은 로컬 파일 이름/참조 변경이며 GitHub push는 수행하지 않았다. 문서 수와 기존 개발 목표·실험 내용은 유지한다. 대응 파일 일치·링크·공백·검색 색인은 후속 검증한다.
- 검증 완료: 대응 문서 4쌍의 바이트 일치, 이전 파일 제거/새 이름 존재, YAML·wikilink·Query 수량·공백 검사 통과. qmd update 완료, 벡터 임베딩 미갱신.
