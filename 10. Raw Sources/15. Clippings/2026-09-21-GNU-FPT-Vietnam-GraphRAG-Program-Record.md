---
type: raw-source
aliases:
  - 2025 베트남 FPT GraphRAG 프로그램 기록
  - GNU FPT Vietnam AI Program Record
description: "Official program facts, certificate evidence, repository observations, and Kim Gyutae's self-report about leading an international financial GraphRAG project at FPT University in Da Nang."
author:
  - "[[김규태]]"
  - 경상국립대학교 빅데이터 혁신융합대학 사업단
  - FPT University
date created: 2026-09-21
date modified: 2026-09-21
date ingested: 2026-09-21
tags:
  - raw-source
  - vietnam
  - fpt
  - graphrag
  - generative-ai
  - financial-analysis
  - international-collaboration
source:
  - "http://smartbigdata.gnu.ac.kr/열린마당/공지사항/?pg=4&no=242"
  - "https://github.com/VIK-GraphRAG/Finance_GraphRAG"
  - "[[2025-FPT-Vietnam-BigData-AI-Program-Plan.hwp]]"
  - "[[2026-01-24-FPT-Vietnam-AI-Completion-Certificate.jpeg]]"
sourceDocument: "2025 글로벌 빅데이터·AI 교육 및 실무 체험 프로그램(베트남 FPT) 계획(안)"
sourceFormat: "HWP, JPEG, GitHub repository, user statement"
conversionTool: "olefile/zlib HWP record extraction, visual certificate review, GitHub history and README inspection"
conversionDate: 2026-09-21
conversionFidelity: "High for extracted program text and certificate transcription; individual role and collaboration details remain user-reported."
category: Clippings
status: ingested
collectionPurpose: "취업/포트폴리오·자기소개서·AI 프로젝트 증거·해외 협업 — 베트남 FPT에서의 다국적 GraphRAG 프로젝트를 향후 지원서와 면접에서 검증 가능한 실행·리더십 사례로 재사용하기 위해 수집."
mainVaultRelated: []
mainVaultCmds: ""
---

# GNU FPT Vietnam Financial GraphRAG Program Record

## Source Notes

- 공식 계획서는 경상국립대학교 주관 교육 일정을 `2025-12-29~2026-01-23` 4주로 명시한다.
- FPT 수료증은 체류·프로그램 범위를 `2025-12-28~2026-01-24` 다낭으로 적고 있다. 어느 날짜를 쓰는지에 따라 교육 일정과 전체 체류 일정을 구분한다.
- 공식 계획서의 Project 2는 Python·LLM·Graph science·Streamlit 기반 GraphRAG 과제였다.
- 공개 저장소는 Neo4j 지식 그래프, PDF·CSV·JSON 통합, 2~3 hop 추론, 반도체 공급망 위험 예시와 56개 commit을 확인할 수 있다.
- 팀 구성, 팀장·개발 리드 역할, 일일 스크럼 운영과 반도체 시장 타깃 제안은 사용자 자기보고다.
- 영어 최종 발표는 팀 단위로 진행됐으나 김규태가 직접 발표하지는 않았다.
- 2026-09-21 사용자 확인에 따라 `gyugyu <zn7034@gnu.ac.kr>` 55개와 `kim gyutae` 1개 commit identity는 모두 김규태다.
- 김규태는 문제 정의, 시스템 설계, 프롬프트, 생성형 AI를 활용한 코드 생성과 실행을 담당했고, 인도인 팀원은 UI를 담당했다고 확인했다.
- Windows와 macOS를 함께 쓰는 팀의 환경 차이를 줄이기 위해 김규태가 Docker 환경을 구성해 공통 개발 환경으로 사용했다고 확인했다.

## Official Program Extract

### 사업 목적

> 베트남 FPT 대학교에서 제공하는 글로벌 교육 및 실무 체험 프로그램에 참여하여, 베트남 대표 SW 기업인 FPT IS 재직자 멘토링을 통해 빅데이터·인공지능 최신 기술을 습득하고 실무 적용 경험을 확보.

### 공식 일정

> FPT University, FPT IS / 베트남 다낭 / 2025. 12. 29. ~ 2026. 1. 23., 4주 / 경상국립대학교 주관.

### Project 2: GraphRAG LLM

> The app can interact with relationships in the dataset to answer or debate with the end-user. The core technology of the app is LLM.

> Develop a fast GraphRAG that can operate in a real system; use Python, open frameworks, and open LLM APIs; improve graph extraction accuracy and inference speed; create a simple chat app using Streamlit.

> Week 1: Research applications and the current state of GraphRAG. Week 2: Collect a dataset, install an open framework, and test the LLM. Week 3: Improve GraphRAG accuracy. Week 4: Build a Streamlit app and test the full system.

## Certificate Transcription

> KIM GYUTAE of GyeongSang National University has successfully completed Experiential Project-Based Learning Program for International Students. From December 28, 2025 to January 24, 2026 in Da Nang city, Viet Nam. A program authorized by FPT Education Global, FPT University.

## Repository Observation

- Repository: https://github.com/VIK-GraphRAG/Finance_GraphRAG
- Name: `VIK AI - Privacy-First Financial GraphRAG`
- Main verified features: Neo4j knowledge graph, PDF/CSV/JSON integration, 2~3 hop reasoning, Streamlit interface, risk-path visualization.
- Verified example: `Taiwan Strait Tension → Taiwan → TSMC → Nvidia` supply-chain risk path.
- Verified files include `seed_semiconductor_ontology.py`, `seed_financial_data.py`, `src/`, `evaluator/`, Docker and multiple system test scripts.

## Original Content

### User Statement, 2026-09-21

> 베트남 다낭 fpt 에서했고 인도인 한명 베트남 한명 한국인 세명에서했고 파이썬으로 했고 금융분석하는 graphrag으로 반도체시장에서 잠재적인 위협을 매크로와 마이크로 거시적 기업적관점에서 분석했음 내가맡은역할은 팀장이고 개발을 리드했음 직접제안한것은 전체시장으로 하지말고 위험성이 크고 변동성이 크고 사이클을 자주타는 반도체시장을 타깃하고 반도체시장의 특성을 보고 위험성을 사전에 분석할수있게하였다. 위험성으로 한 이유는 반도체는 다른 섹터보다 더욱 이런 위험성에 취약하기때문이다.

> 인도친구와 영어로 소통해서 내가하고싶은말을 제대로 전달하지못하였다. 나는 프로젝트를 2주안에 빠르게 끝내고 남은기간을 더욱 완벽하게 만들고싶었는데 인도인 팀원은 여유롭게 한달안에만 만들면된다고 해서 힘들었음. 그래서 서로 각자 매일 업무를하기전 스크럼시간을 가지고 오늘 각자맡은바를 내가 부여하고 서로 얼마나 진행되었는지를 공유하고 서로 소통하는시간을 가졌다.

> 최종결과물은 깃헙을 보고 발표도 했고 영어로했음. 발표는 내가 안함. 수료는했음. 성적은없었고 그냥 정량적인 평가는없고 수료했다로 끝임.

## Evidence Boundary

> [!note] Bias Check
> Counter-argument: 수료증은 4주 PBL 수료를, 공개 저장소는 결과물의 존재를 보여주지만 개인의 독립 코드 기여율·영어 발표력·GraphRAG 추론 정확도를 증명하지는 않는다.
> Data gap: 프롬프트별 생성 코드와 본인 수정 내역, 팀원별 산출물, 최종 발표자·멘토 평가, GraphRAG 정확도·인용 검증 자료가 추가로 필요하다.
