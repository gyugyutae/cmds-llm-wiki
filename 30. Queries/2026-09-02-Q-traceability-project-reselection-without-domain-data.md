---
type: query-result
aliases:
  - 도메인 데이터 없는 추적성 프로젝트 재선정
  - AI 코드 변경 추적성 프로젝트
description: "A reassessment of semester traceability projects that require no external domain dataset, recommending AI-assisted software change provenance with OpenTelemetry GenAI and signed build attestations."
author:
  - Codex
date created: 2026-09-02
date modified: 2026-09-02
tags:
  - query
  - traceability
  - ai-coding
  - software-provenance
  - opentelemetry
  - slsa
source:
  - "[[2026-09-02-Q-semester-project-concrete-team-brief]]"
  - "[[Graduation-elasticsearch]]"
  - https://github.com/open-telemetry/semantic-conventions-genai
  - https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md
  - https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations
  - https://slsa.dev/spec/v1.2/build-track-basics
  - https://spec.c2pa.org/specifications/specifications/2.3/index.html
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 프로젝트 증거
  - Codex 개발 워크플로
confidence: high
status: active
---

# 도메인 데이터 없는 추적성 프로젝트 재선정

## 재판단

무인기 데이터가 없고 Upbit 문제에 팀이 확신하지 못한다면 두 후보를 보류하는 것이 맞다. 외부 데이터 없이 한 학기 동안 가장 자연스럽게 만들 수 있는 새 1순위는 다음과 같다.

> **TraceForge — 요구사항부터 AI 작업, 코드 변경, 테스트, 빌드 산출물까지 연결하는 AI 코드 변경 추적성 플랫폼**

팀의 GitHub 저장소와 개발 과정 자체가 데이터가 된다. 따라서 가짜 산업 데이터를 만드는 대신, 팀이 실제 개발하면서 발생시키는 issue, prompt metadata, tool call, commit, pull request, test, build를 수집하고 연결한다.

## 문제

AI 코딩 도구를 사용하면 코드는 빨리 바뀌지만 리뷰어는 다음을 확인하기 어렵다.

- 이 변경은 어떤 요구사항 때문에 생겼는가?
- AI가 어떤 파일과 도구를 사용했는가?
- 사람이 실제로 무엇을 검토하고 승인했는가?
- 각 acceptance criterion을 검증하는 테스트는 무엇인가?
- 최종 실행 파일은 승인된 commit과 CI에서 만들어졌는가?

GitHub에는 issue, PR, commit, test result가 각각 존재하지만 AI 실행 과정과 요구사항 검증 근거까지 하나의 흐름으로 보여주지는 않는다.

## 사용자와 가치

- 1차 사용자: AI 코딩 도구를 쓰는 3~5명 학생 개발팀
- 2차 사용자: 팀 프로젝트를 평가하는 교수·조교, 코드 리뷰어
- 가치: “AI로 만들었다”가 아니라 **어떤 요구사항을 어떤 변경과 테스트로 충족했고 사람이 무엇을 검증했는지** 증명한다.

## 한 건의 실제 흐름

```text
Issue #12: 로그인 5회 실패 시 10분 잠금
→ acceptance criteria 3개 등록
→ AI 작업 실행: model/version, tool call, 수정 파일 metadata 기록
→ PR #18: AuthService.java, LoginTest.java 변경
→ 테스트 7개 실행, criterion별 test 연결
→ 사람 리뷰: 보안 파일 변경 승인
→ GitHub Actions build
→ commit SHA와 build provenance가 연결된 Evidence Packet 생성
```

리뷰 화면은 `요구사항 → AI run → 파일 diff → 테스트 → 사람 승인 → 빌드` 그래프로 보여준다. `잠금 해제 테스트가 없음` 또는 `민감 파일을 AI가 수정했지만 사람이 승인하지 않음` 같은 끊어진 연결을 경고한다.

## 최신 기술을 맛보는 지점

### Headline — OpenTelemetry GenAI agent observability

OpenTelemetry의 GenAI semantic conventions는 agent 호출, model operation, tool execution, retrieval 등을 공통 span과 attribute로 표현하는 작업을 진행 중이다. TraceForge는 이 규약을 참고해 AI run을 vendor-specific 대화 로그가 아니라 구조화된 trace로 수집한다.

중요한 경계:

- 현재 GenAI conventions는 development 상태인 부분이 있으므로 고정 버전을 명시한다.
- prompt 원문과 source code를 무조건 저장하지 않고 hash, model, operation, file path, 승인 상태 중심으로 수집한다.
- 상용 Codex나 Copilot 내부를 해킹하지 않는다. 팀이 제어하는 간단한 AI coding runner 또는 trace JSON importer를 만든다.

### Stretch — SLSA/GitHub Artifact Attestation

GitHub Actions는 binary나 container image에 build provenance attestation을 생성하고 검증할 수 있다. SLSA Build L1은 provenance 존재, L2는 hosted build platform에서 생성된 signed provenance를 요구한다. TraceForge는 최종 build가 어떤 repository, workflow, commit에서 만들어졌는지를 evidence graph 끝에 연결한다.

서명 기능은 직접 암호 알고리즘을 만드는 것이 아니라 GitHub Artifact Attestation 또는 Sigstore를 사용한다.

## MVP 화면

1. `Project Map`: issue, PR, commit, test, build의 전체 추적 그래프
2. `Change Evidence`: 한 요구사항에 대한 AI run, 변경 파일, test, review 상세
3. `Gap Detector`: test 없음, 승인 없음, 연결되지 않은 commit 등 경고
4. `Evidence Packet`: 교수·리뷰어에게 제출할 JSON/PDF 요약과 검증 결과

## 필수 구현과 제외 범위

필수:

- GitHub repository 한 개의 issue, PR, commit, changed files, check result 수집
- 팀이 제어하는 AI run trace 수집기 또는 JSON importer
- requirement/criterion/AI run/file/commit/test/review/build 데이터 모델
- 수동 link 생성·수정과 자동 link 후보 생성
- trace graph와 누락 link 경고
- 사람 승인 기록
- 일반 GitHub PR 화면과 Evidence Packet의 비교 실험

8주차 이후 선택:

- OpenTelemetry GenAI exporter
- GitHub build artifact attestation 검증
- LLM 기반 criterion-test 후보 추천

제외:

- 모든 IDE/Copilot/Codex 자동 연동
- AI가 작성한 코드 비율 판별
- 완전 자동 코드 품질 판정
- blockchain
- 대규모 오픈소스 전체 분석
- 모델 학습

## 연구 질문과 baseline

- RQ1. TraceForge가 일반 GitHub issue/PR 화면보다 변경 근거를 찾는 시간과 정답률을 개선하는가?
- RQ2. 규칙 기반 gap detector가 의도적으로 만든 미연결 test·미승인 변경을 얼마나 탐지하는가?
- RQ3. 구조화된 AI trace가 자유형 AI 대화 로그보다 실행 경로 재구성에 유용한가?

Baseline:

- GitHub issue + PR + Actions 화면만 제공
- AI 작업은 자유형 텍스트 로그로만 제공

Proposed:

- 연결된 trace graph + Evidence Packet + gap warning
- 구조화된 OpenTelemetry-style AI run

평가:

- 미연결 항목 탐지 precision/recall
- 특정 변경의 요구사항과 검증 test를 찾는 시간
- 사용자 답변 정확도
- GitHub event 반영 지연 p95
- trace 수집으로 증가한 실행시간과 저장량
- Evidence Packet의 commit/build attestation 검증 성공률

20~30개 issue와 의도적으로 만든 30~50개 정상·누락 link면 학기 내 수업용 실험이 가능하다. 산업 일반화는 주장하지 않는다.

## 협업 구조

4명 기준:

- GitHub/AI trace 수집: webhook, API, OpenTelemetry-style event
- 백엔드/도메인: graph model, link rule, gap detector
- 프론트엔드: graph, evidence detail, reviewer approval UX
- 품질/DevOps: test mapping, GitHub Actions, attestation, baseline 사용자 실험

각 구성원이 자기 기능의 요구사항, 코드, 테스트, Evidence Packet을 남기게 하면 프로젝트 자체가 프로젝트를 검증하는 dogfooding 구조가 된다.

## 12주 계획

| 주차 | 완료 기준 |
|---|---|
| 1~2주 | 학생 개발자 3~5명 인터뷰, trace schema, 데모 issue 확정 |
| 3~4주 | GitHub issue/PR/commit/check 수집과 DB 저장 |
| 5~6주 | 수동 link, 상세 화면, 기본 trace graph |
| 7~8주 | AI trace importer, gap detector, 사람 승인까지 중간 데모 |
| 9~10주 | OTel exporter 또는 artifact attestation 중 하나 추가, Evidence Packet |
| 11주 | gold link와 baseline 사용자 실험, 성능·오류 주입 테스트 |
| 12주 | 분석 보고서, 최종 데모, 포트폴리오 README |

## 다른 후보 비교

| 후보 | 최신 기술 | 데이터 확보 | 협업성 | 12주 위험 | 판단 |
|---|---|---:|---:|---:|---|
| TraceForge | OTel GenAI + SLSA attestation | 5 | 5 | 중간 | **1순위** |
| OriginLens | C2PA Content Credentials | 5 | 4 | 중간 | 2순위 |
| BuildProof | SBOM + SLSA/Sigstore | 5 | 4 | 낮음 | 안전하지만 AI 인상 약함 |
| DataLine | OpenLineage 기반 ETL lineage | 4 | 4 | 중간 | 데이터 엔지니어링 관심 시 적합 |

### 2순위 OriginLens

이미지에 생성·편집 이력과 서명을 담은 C2PA Content Credential을 읽고 검증해 사람이 이해할 수 있는 타임라인으로 보여주는 서비스다. 원본 이미지 → AI 편집 → 자르기 → 게시 이력을 표시하고 픽셀을 변조하면 검증 실패를 보여준다. 공식 C2PA 사양은 콘텐츠의 출처와 변경 이력을 위한 공개 표준이고 Node/Rust/Android SDK도 존재한다.

시각적 데모는 가장 좋지만, C2PA는 이미지가 진실인지 또는 AI 생성물인지 자동 판별하지 않는다. 첨부된 provenance가 변조되지 않았는지를 검증한다. 이 경계를 팀이 이해하지 못하면 “딥페이크 탐지기”로 잘못 설명할 위험이 있다.

## 최종 추천

현재는 TraceForge를 팀 회의의 1안으로 가져가는 것이 좋다. 기존 source-test traceability 연구와 연결되면서도 선배 코드를 반복하지 않고, 최신 AI agent observability와 software supply-chain provenance를 직접 구현·검증할 수 있다. 무엇보다 별도 산업 데이터가 없어도 팀의 개발 활동으로 12주 내내 실제 데이터를 축적한다.

팀이 개발자 도구보다 일반 사용자에게 보이는 시각적 제품을 선호하면 OriginLens를 2안으로 가져간다.

> [!note] Bias Check
> OpenTelemetry GenAI conventions의 일부는 아직 development 상태이고, GitHub artifact attestation과 C2PA는 이미 존재하는 표준이다. 독창성은 표준 자체를 만들었다는 데 있지 않다. TraceForge는 요구사항·AI run·사람 승인·test·signed build를 학생 팀의 리뷰 Evidence Packet으로 연결하고 효과를 baseline과 비교하는 응용에서 차별성을 검증해야 한다.

## Sources

- OpenTelemetry GenAI conventions: https://github.com/open-telemetry/semantic-conventions-genai
- OpenTelemetry GenAI agent spans: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md
- GitHub Artifact Attestations: https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations
- SLSA Build Track 1.2: https://slsa.dev/spec/v1.2/build-track-basics
- Sigstore in-toto attestations: https://docs.sigstore.dev/cosign/verifying/attestation/
- C2PA specification 2.3: https://spec.c2pa.org/specifications/specifications/2.3/index.html
- C2PA Node SDK: https://github.com/contentauth/c2pa-js/tree/main/packages/c2pa-node

이 답변은 강의/수업/교육, 취업/포트폴리오, Codex 개발 워크플로에 활용 가능합니다 — 외부 도메인 데이터 없이 팀의 실제 AI 개발 과정을 추적성 데이터와 검증 실험으로 전환합니다.
