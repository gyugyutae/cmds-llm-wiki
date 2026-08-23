---
type: query-result
aliases:
  - LLM Wiki Sharing Demo Strategy
  - LLM Wiki URL 공유 전략
description: Strategy for sharing Kim Gyutae's LLM Wiki and Obsidian knowledge graph as portfolio URLs, comparing GitHub README, deployed static sites, Obsidian Publish, Quartz, and live demo flow.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - query
  - llm-wiki
  - portfolio
  - demo
  - deployment
source:
  - "[[Core Context]]"
  - "[[MOC-Portfolio]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
  - "GitHub Pages official docs"
  - "Obsidian Publish official page"
  - "Quartz official docs"
reusableFor:
  - 취업/포트폴리오
  - 프로젝트 증거
  - Codex 개발 워크플로
  - 에세이/블로그
confidence: medium
---
# LLM Wiki URL 공유와 데모 전략

## Query

이 LLM Wiki와 만든 것들을 URL 형식으로 공유해야 할 때 GitHub README를 제출할지, 배포해서 보여줄지, Obsidian 지식 그래프를 데모에서 어떻게 보여주는 것이 효과적인가?

## Recommendation

가장 좋은 구성은 **GitHub README + 공개 데모 사이트 + 짧은 그래프 시연 영상/GIF** 조합이다.

| 목적 | 추천 URL | 역할 |
|------|----------|------|
| 심사자가 빠르게 이해 | GitHub README | 문제, 구조, 사용법, 증거, 한계를 설명하는 공식 문서 |
| 실제 결과를 체험 | 배포 사이트 | Wiki/그래프/검색을 클릭해 볼 수 있는 데모 |
| 발표에서 임팩트 | 60-90초 화면 녹화 | Obsidian graph가 실제로 지식 구조를 보여준다는 증거 |

README만 제출하면 안정적이지만, LLM Wiki의 핵심 가치인 연결 구조와 탐색 경험이 약하게 보인다. 반대로 배포 사이트만 주면 "그래서 네가 뭘 만들었나"가 흐려질 수 있다. 따라서 README를 중심 허브로 두고, 그 안에서 데모 사이트와 영상으로 연결하는 방식이 가장 좋다.

## Best Demo Flow

1. README 첫 화면에서 한 문장으로 시작한다.
	- "Raw Sources를 LLM이 Wiki/Queries로 컴파일해 취업 포트폴리오 증거로 재사용하는 개인 지식 시스템입니다."
2. 구조 그림을 보여준다.
	- `10. Raw Sources -> 20. Wiki -> 30. Queries`
3. Obsidian graph를 보여준다.
	- `김규태`, `MOC-Portfolio`, `financial-order-latency-lab`, `harness`, `cuee`, `LLM Wiki Pattern` 중심으로 연결이 보이게 필터링한다.
4. 한 페이지를 클릭한다.
	- 예: `MOC-Portfolio`에서 프로젝트 spine과 evidence gap을 보여준다.
5. Query 결과를 보여준다.
	- 예: `2026-07-16-Q-how-to-use-llm-wiki-well`처럼 질문 결과가 저장되어 재사용 산출물이 되는 흐름을 보여준다.
6. 마지막에 "AI가 만든 것과 내가 검증한 것의 경계"를 말한다.
	- `explored`, `verificationStatus`, `confidence` 필드를 보여주면 과장 없이 진지한 시스템으로 보인다.

## Tool Choice

### Fastest: GitHub README only

장점:
- 제출이 가장 쉽고 안정적이다.
- GitHub commit, markdown, repo 구조 자체가 개발자 포트폴리오 증거가 된다.
- 민감한 노트를 공개하지 않고 선별된 설명만 보여줄 수 있다.

단점:
- 지식 그래프의 시각적 임팩트가 약하다.
- "사용 가능한 시스템"보다 "문서"처럼 보일 수 있다.

사용 시점:
- 제출 마감이 가깝거나, 공개 가능한 노트를 아직 선별하지 못했을 때.

### Balanced: GitHub README + screen recording

장점:
- 민감한 vault를 공개하지 않아도 Obsidian graph를 보여줄 수 있다.
- 데모에서 가장 안정적이다.
- 60-90초 GIF/영상 하나면 심사자가 바로 이해한다.

단점:
- 직접 클릭 가능한 웹 데모는 아니다.

사용 시점:
- 지금 가장 현실적인 1차 제출 방식.

### Best public demo: Quartz + GitHub Pages

장점:
- 공개용 markdown subset을 사이트로 배포할 수 있다.
- Obsidian-style wikilinks, backlinks, graph view, full-text search 같은 digital garden 기능을 보여주기 좋다.
- GitHub Pages로 URL 공유가 가능하다.

주의:
- 전체 vault를 그대로 공개하지 말고 `public/` 또는 `docs/`용 subset을 만들어야 한다.
- 개인 자산, 투자, 미검증 주장, private context는 제외해야 한다.

사용 시점:
- 며칠 정도 정리할 시간이 있고, "실제 클릭 가능한 지식 그래프"를 보여주고 싶을 때.

### Most Obsidian-native: Obsidian Publish

장점:
- Obsidian 공식 publish 방식이며 graph view, backlinks, hover previews 같은 Obsidian다운 탐색 경험을 제공한다.
- 설정이 상대적으로 간단하다.

주의:
- 유료 서비스 성격이 있으므로 비용을 감안해야 한다.
- 공개할 노트 선별이 중요하다.

사용 시점:
- 비용보다 빠른 공개와 Obsidian-native 경험이 더 중요할 때.

## What To Publish

공개용 subset만 만든다.

추천 공개 페이지:
- `README.md`
- `MOC-Portfolio`
- `LLM Wiki Pattern`
- `3-Layer Architecture`
- `Ingest-Query-Lint Cycle`
- `MOC-LLM Wiki Guide`
- `MOC-Knowledge Management`
- `2026-07-16-Q-how-to-use-llm-wiki-well`
- 프로젝트별 public-safe summary page:
	- `financial-order-latency-lab`
	- `Graduation-elasticsearch`
	- `cuee`
	- `harness`

비공개 또는 주의:
- 개인 자산/투자 세부 금액
- 민감한 자기소개서 초안
- 검증되지 않은 강한 주장
- 타인 개인정보, 팀원 이름, 회의록 원문
- `explored: false`인데 확정적으로 보이는 페이지

## README Shape

README는 아래 순서가 좋다.

1. 한 줄 요약
2. 데모 링크
3. 60초 시연 GIF
4. 문제 정의
5. 시스템 구조
6. 핵심 기능
7. 대표 Query 예시
8. 포트폴리오 활용 예시
9. 기술 스택
10. 한계와 다음 개선

## Demo Message

발표에서 이렇게 말하면 좋다.

> 저는 자료를 단순히 저장하는 게 아니라, Raw Source를 보존하고 LLM이 Wiki와 Query 결과로 컴파일하게 해서 취업 포트폴리오 증거로 재사용하는 시스템을 만들었습니다. Obsidian graph는 제가 어떤 프로젝트, 학습, 회고를 연결해서 관리하는지 보여주고, `verificationStatus`와 `explored` 필드는 AI가 정리한 내용과 제가 직접 검증한 내용을 구분하기 위한 장치입니다.

## Reuse Axis

이 답변은 취업/포트폴리오, 프로젝트 증거, Codex 개발 워크플로, 에세이/블로그에 활용 가능합니다 — LLM Wiki를 외부 심사자에게 URL과 데모로 보여주는 제출 전략을 정리했기 때문입니다.
