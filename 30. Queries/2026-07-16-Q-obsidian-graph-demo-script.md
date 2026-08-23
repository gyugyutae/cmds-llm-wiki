--
type: query-result
aliases:
  - Obsidian Graph Demo Script
  - LLM Wiki Demo Scenario
description: Demo script for showing an Obsidian LLM Wiki workflow: clipping an article, ingesting it into Raw Sources and Wiki, querying it, reviewing explored status, and explaining portfolio value.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - query
  - demo
  - obsidian
  - llm-wiki
  - portfolio
source:
  - "[[Core Context]]"
  - "[[MOC-Portfolio]]"
  - "[[2026-07-16-Q-llm-wiki-sharing-demo-strategy]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "Obsidian pricing official page"
  - "ScreenToGif GitHub"
  - "OBS Studio official page"
reusableFor:
  - 취업/포트폴리오
  - 프로젝트 증거
  - Codex 개발 워크플로
  - 에세이/블로그
confidence: medium
---

# Obsidian Graph Demo Script

## Query

Obsidian Publish는 비용이 드는지, 비용이 든다면 그래프를 GIF/영상으로 어떻게 보여줄지, 그리고 Web Clipper -> Raw Source -> ingest -> Wiki -> Query -> explored까지 보여주는 데모 시나리오는 어떻게 구성하면 좋은가?

## Recommendation

Obsidian Publish는 비용이 드므로, 지금은 **무료 대안으로 Obsidian graph 화면 녹화 + GitHub README 제출**이 현실적이다. 공개 URL이 꼭 필요하면 README에 GIF/영상과 핵심 스크린샷을 넣고, 나중에 시간이 있으면 Quartz/GitHub Pages로 public subset만 배포한다.

## Demo Thesis

데모의 메시지는 이 한 문장으로 잡는다.

> 자료를 단순히 저장하는 것이 아니라, Raw Source를 보존하고 LLM이 Wiki와 Query 결과로 컴파일하게 해서 취업 포트폴리오와 학습 자산으로 재사용하는 시스템입니다.

## Recommended Demo Asset

### 제출용

- `README.md`: 시스템 설명, 구조도, 데모 GIF, 주요 링크
- `demo-llm-wiki-workflow.gif`: 45-60초 핵심 흐름
- 필요하면 `demo-full.mp4`: 3-5분 전체 시연

### GIF 제작

Windows 기준으로 가장 쉬운 방법은 ScreenToGif다.

1. Obsidian 창을 데모용 vault에 맞춰 정리한다.
2. ScreenToGif에서 `Recorder`를 선택한다.
3. Obsidian graph와 note area가 보이는 영역만 캡처한다.
4. 45-60초만 녹화한다.
5. 불필요한 앞뒤 프레임을 잘라낸다.
6. 10-15fps, 폭 1200px 이하로 export한다.
7. README에는 GIF를 바로 넣고, 긴 설명은 아래에 적는다.

긴 발표 영상은 OBS Studio로 MP4 녹화하고, README에는 GIF만 넣는 구성이 좋다.

## 3-Minute Live Demo Scenario

### 0:00-0:20 Opening

화면: README 또는 Obsidian `index.md`

말하기:

> 이 시스템은 제가 읽은 자료를 그냥 저장하지 않고, Raw Source, Wiki, Query 결과로 나누어 취업 포트폴리오와 학습 자료로 재사용하기 위한 LLM Wiki입니다.

보여줄 것:

- `10. Raw Sources`
- `20. Wiki`
- `30. Queries`
- `index.md`

### 0:20-0:50 Graph Overview

화면: Obsidian Graph View

필터:

```text
path:"20. Wiki" OR path:"30. Queries"
```

또는 중심 노드:

- `MOC-Portfolio`
- `김규태`
- `financial-order-latency-lab`
- `harness`
- `LLM Wiki Pattern`

말하기:

> 그래프는 단순 장식이 아니라, 프로젝트, 학습, Query 결과가 어떻게 연결되는지 보여주는 지도입니다. 예를 들어 포트폴리오 MOC에서 제 대표 프로젝트와 evidence gap으로 바로 이동할 수 있습니다.

### 0:50-1:30 Web Clipper -> Inbox -> Raw Source

화면: 브라우저 + Obsidian Inbox

사용할 글:

- 너무 길지 않은 공개 기술 글
- 내 관심 축과 연결되는 글
- 예: AI agent workflow, LLM Wiki, 개발자 생산성, 백엔드 성능, Obsidian/PKM 관련 글

말하기:

> 새 글을 발견하면 바로 Wiki에 넣지 않고, 먼저 Inbox에 저장합니다. 그리고 왜 수집했는지 목적을 정합니다. 이 목적이 나중에 Query routing과 포트폴리오 재사용성을 결정합니다.

데모 입력 예시:

```text
collectionPurpose: Codex 개발 워크플로 - AI agent workflow를 내 개발 harness와 포트폴리오 설명에 재사용하기 위해 수집
```

보여줄 것:

- `00. Inbox/...`
- `/ingest` 요청
- Raw Source가 `10. Raw Sources/...`로 이동
- 원문은 `## Original Content` 아래 보존

### 1:30-2:10 Raw Source -> Wiki Update

화면: 관련 Wiki page

보여줄 페이지 후보:

- `harness`
- `AI-Augmented Developer Positioning`
- `LLM Wiki Pattern`
- `MOC-Portfolio`

말하기:

> Ingest가 끝나면 원문은 Raw Source에 남고, 반복해서 쓸 개념은 Wiki page에 반영됩니다. 즉 원본과 해석을 분리합니다.

보여줄 것:

- `source:` frontmatter
- `related:`
- `confidence`
- 새로 추가된 문단

### 2:10-2:45 Query -> Reusable Output

화면: Query 명령과 결과 페이지

데모 Query:

```text
/query 방금 ingest한 글을 내 harness 프로젝트와 연결해서, 개발자 포트폴리오에서 "AI를 도구로 활용한 개발 workflow"로 설명할 수 있게 3문장으로 정리해줘. 내가 판단한 부분과 AI가 도운 부분을 분리해줘.
```

말하기:

> Query는 단순 질의응답이 아니라, 면접 답변, README 문장, 블로그 초안처럼 재사용 가능한 산출물을 만드는 단계입니다. 좋은 Query 결과는 `30. Queries`에 저장됩니다.

보여줄 것:

- `30. Queries/YYYY-MM-DD-Q-...`
- `reusableFor`
- `source`
- 산출 문장

### 2:45-3:20 Explored / Verification Boundary

화면: Wiki page frontmatter

말하기:

> 중요한 점은 LLM이 정리했다고 해서 제가 안다고 주장하지 않는다는 것입니다. `explored`, `verificationStatus`, `confidence`로 AI가 정리한 지식과 제가 직접 검토한 지식을 구분합니다.

보여줄 상태:

```yaml
explored: false
verificationStatus: unverified
confidence: medium
```

그 다음 직접 읽고 설명 가능한 페이지라면:

```yaml
explored: true
exploredBy: 김규태
exploredDate: 2026-07-16
verificationStatus: partial
```

주의:

실제로 읽지 않은 페이지를 데모용으로 `explored: true`로 바꾸면 안 된다. 데모에서는 "검토 전 상태"와 "검토 후 승격 기준"을 보여주는 것이 더 신뢰를 준다.

### 3:20-3:50 Why This Matters

말하기:

> 이걸 쓰는 이유는 자료를 많이 모으기 위해서가 아닙니다. 프로젝트 증거, 학습 내용, Codex와의 개발 판단을 나중에 이력서, 면접 답변, README, 블로그 글로 재사용하기 위해서입니다. 특히 AI가 도운 부분과 제가 직접 판단하고 검증한 부분을 분리해서 기록하기 때문에, AI 의존이 아니라 AI를 개발 역량의 증폭기로 활용했다는 점을 설명할 수 있습니다.

## 60-Second GIF Cut

GIF는 전체 과정을 다 담지 말고, 시각적으로 강한 장면만 담는다.

1. Graph View에서 `MOC-Portfolio` 중심 연결 보여주기
2. `Raw Sources -> Wiki -> Queries` 폴더 구조 보여주기
3. Query result 페이지 열기
4. `explored`, `verificationStatus`, `confidence` 확대
5. 마지막에 README 한 문장 보여주기

자막 문장:

```text
Raw source -> Compiled wiki -> Reusable portfolio answer
```

## Demo Checklist

- 민감한 개인 정보가 보이는 노트는 닫는다.
- 투자 금액, 자기소개서 초안, 팀원 개인정보는 숨긴다.
- Obsidian left sidebar는 필요한 폴더만 펼친다.
- Graph node가 너무 많으면 `20. Wiki`와 `30. Queries`만 필터링한다.
- 데모용 글은 짧고 공개 가능한 글을 고른다.
- `explored: true`는 실제로 검토한 페이지에만 쓴다.

## Reuse Axis

이 답변은 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 에세이/블로그에 활용 가능합니다 — LLM Wiki를 외부 평가자에게 보여주는 실제 데모 흐름과 녹화 전략을 정리했기 때문입니다.
