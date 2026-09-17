---
type: wiki-page
aliases:
  - Graduation Elasticsearch
description: JavaParser-based source-test traceability analysis repository for Elasticsearch Java Client sources.
author:
  - Codex
date created: 2026-07-10
date modified: 2026-09-09
tags:
  - project
  - research
  - java
  - elasticsearch
source:
  - https://github.com/gyutaetae/Graduation-elasticsearch
  - https://raw.githubusercontent.com/gyutaetae/Graduation-elasticsearch/master/README.md
related:
  - "[[김규태]]"
  - "[[MOC-Portfolio]]"
confidence: medium
layer: entities
explored: true
claimType: mixed
evidenceScope: github-readme
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: Codex
disputed: false
status: active
---

# Graduation-elasticsearch

## Overview

`Graduation-elasticsearch`는 JavaParser 기반 source-test traceability 분석을 위한 연구/학습 저장소다. Elasticsearch Java Client source tree를 대상으로 test Java file에서 source Java file로 이어지는 strict `TEST FILE -> SOURCE FILE` link set을 추출한다.

김규태는 선배가 남긴 연구를 이어 2026년 5월부터 참여하고 있다. JavaParser와 AST의 기능과 개념은 설명할 수 있지만 관련 분석 코드는 직접 작성하지 않았다. 사용자는 AI 보고에서 실제 `src/test/java` 파일 수보다 `test` 포함 경로 수가 더 큰 이상을 발견해 분류 기준 재검토를 요청했다. 반면 `unresolved_calls.csv` 원본 행은 아직 직접 검토하지 않았으므로, 외부 dependency 등 unresolved 원인 분석을 본인 수행으로 표현하지 않는다.

2026-08-31 확인한 사용자 연구 노트에는 `A GraphDatabase–Based Approach to Measuring Traceability Coverage in Open-Source Software`의 CoDoc·Neo4j·trace link 구조와 JavaParser/Symbol Solver 알고리즘이 정리돼 있다. `알고리즘 2 자바파서 내파트`라는 자기 기록과 Elasticsearch Java의 source/test CSV, cosine similarity, LLM yes/no, revision history·code clone 검증 흐름이 포함돼 있다. 이는 연구 주제와 데이터 구조를 학습한 증거지만 직접 구현 또는 논문 작성 증거는 아니다.

---

## Research And Backend Signal

- JavaParser AST 분석, `MethodCallExpr` 추출, Symbol Solver resolution을 사용한다.
- parser는 Java로 구현되어 있으며, PowerShell runner가 JavaParser jar를 내려받고 `javac`로 컴파일해 실행한다.
- output은 `source_list_generated.csv`, `test_list_generated.csv`, `source_test_generated.csv`, `method_call_edges.csv`, `unresolved_calls.csv`, `parser_summary.json` 등으로 나뉜다.
- 2026-08-29 공개 README 기준 repository-reported summary는 source files `3460`, test files `114`, method calls `5486`, resolved calls `3479`, unresolved calls `2007`, parse failure `1`, final test-source links `694`다. 이번 Wiki 검증에서는 parser를 재실행하지 않았다.
- 전체 Java files는 `3574`, unresolved 비율은 `36.58%`다.
- 외부 dependency classpath 누락과 실제 Java가 아닌 입력 파일이라는 unresolved 원인 후보는 AI가 생성한 보고서·README의 분석이며 사용자가 원본 행으로 직접 검증하지 않았다.
- `src/test/java` 중심 분류, dependency classpath 추가, 깨진 입력 정리는 구현 완료가 아니라 도출한 개선 방향이다.
- 사용자는 1차 결과를 교수에게 공유했고 `unresolved 비율이 너무 높다`는 피드백을 받았다. 이후 AI에 원인 후보·개선 방향과 비율 원형 그래프가 포함된 README 작성을 요청했다. 교수 피드백은 사용자 자기보고이며 별도 회의록·메일 증빙은 아직 확인하지 않았다.

## 2026-09-09 Test Classification Audit

현재 로컬 프로젝트 트리에서 직접 계수한 결과는 다음과 같다. 이는 2026-06-30에 생성된 `parser_summary.json`의 3,574개 Java 파일·114개 test file보다 뒤의 프로젝트 상태이므로 두 스냅샷을 섞지 않는다.

- 현재 전체 Java 파일: `4,215개`
- 실제 `src/test` 경로 Java 파일: `153개`
- 경로 전체에 대소문자 구분 없이 `test`가 포함된 Java 파일: `171개`
- `src/main`에 있지만 기존 규칙이 test로 분류한 소스 파일: `18개`
- 사용자는 AI 보고에서 `153`과 `171`의 불일치를 발견하고 분류 기준 재검토를 요청했다.
- JavaParser 코드, 재계수 스크립트, README와 원형 그래프 작성은 AI가 담당했다.
- 사용자가 직접 확인한 판단은 `path contains test`가 실제 test source set의 기준이 될 수 없으며 `src/test/java` 중심 규칙이 필요하다는 점이다.

기존 `unresolved_calls.csv`에는 2,008개 진단 행이 있고 열은 `test_path`, `method_call`, `line`, `column`, `error_type`, `error_message`다. 현재 로컬 집계상 error type은 `UnsolvedSymbolException 1,997`, `UnsupportedOperationException 8`, `MethodAmbiguityException 2`, `ParseProblemException 1`이다. 사용자는 아직 이 원본을 직접 열어 표본 검토하지 않았다.

## Neo4j Local Graph Verification

2026-09-08에 로컬 Docker Neo4j 5 환경을 실행하고 JavaParser의 `source_test_generated.csv`를 `TEST_FILE -[:TESTS]-> SOURCE_FILE` 관계로 적재했다. Neo4j Browser에서 전체 그래프, `RequestTest.java` 연결, 라벨별 개수, 전체 관계 샘플을 직접 확인했다.

- 노드: `CODE 4,215`, `ISSUE 547`, `API_DOCUMENT 97`
- 추가 라벨: `TEST_FILE 92`, `SOURCE_FILE 245`
- 관계: `MODIFIES 52`, `EXPLAINS 34`, `TESTS 693`
- JavaParser 후보 694개 중 693개 적재, `MultisearchBody.java` 1개는 대응 `CODE` 경로 부재로 스킵
- 실행 기록과 스크린샷: [[EvolvingTraceDB Neo4j 구축 및 검증 가이드]]

---

## Portfolio Use

현재는 대규모 Java 코드베이스를 직접 구현한 개발 경험으로 포지셔닝하지 않는다. 선배 연구를 이어 JavaParser·AST 개념을 학습하고 AI 생성 보고의 파일 수 불일치를 발견해 분류 기준을 재검토하게 한 학부연구 참여 경험으로 사용한다. unresolved 원인 분석은 원본 표본을 직접 검토한 뒤에만 본인 분석으로 확장한다.

면접 핵심 문장:

> 선배가 남긴 source-test traceability 연구에서 AI가 만든 JavaParser 보고를 검토하다 실제 `src/test` 파일 153개보다 `test` 포함 경로가 171개로 집계된 이상을 발견했습니다. 재검토 결과 소스 파일 18개가 잘못 포함된 것을 확인해 `src/test/java` 중심 분류가 필요하다고 판단했습니다. 코드는 직접 작성하지 않았으며 다음 과제는 unresolved 원본 표본과 개선 후 결과를 직접 검증하는 것입니다.

---

## Evidence Gaps

- 연구실에서 이 프로젝트가 맡은 역할
- 논문/졸업 연구와의 연결
- 직접 작성한 parser 코드는 현재 없음
- AI 생성 결과를 어떤 기준으로 검토했는지
- 교수 피드백을 받은 시점·형식과 공유 자료
- 매주 수행하는 연구 업무와 실제 제출 산출물
- 정리한 논문의 수·주제·형식과 교수·선배 피드백
- unresolved call 처리 기준
- `unresolved_calls.csv`의 직접 표본 검토와 수동 분류표
- 결과를 어떤 분석 또는 논문 방향으로 사용할지

---

## Sources

- https://github.com/gyutaetae/Graduation-elasticsearch
- https://raw.githubusercontent.com/gyutaetae/Graduation-elasticsearch/master/README.md
