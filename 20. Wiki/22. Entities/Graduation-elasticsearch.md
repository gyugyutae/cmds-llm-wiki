---
type: wiki-page
aliases:
  - Graduation Elasticsearch
description: JavaParser-based source-test traceability analysis repository for Elasticsearch Java Client sources.
author:
  - Codex
date created: 2026-07-10
date modified: 2026-08-16
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
confidence: high
layer: entities
explored: true
claimType: project-evidence
evidenceScope: github-readme
verificationStatus: partial
status: active
---

# Graduation-elasticsearch

## Overview

`Graduation-elasticsearch`는 JavaParser 기반 source-test traceability 분석을 위한 연구/학습 저장소다. Elasticsearch Java Client source tree를 대상으로 test Java file에서 source Java file로 이어지는 strict `TEST FILE -> SOURCE FILE` link set을 추출한다.

김규태는 선배가 남긴 연구를 이어 2026년 5월부터 참여하고 있다. JavaParser와 AST의 기능과 개념은 설명할 수 있지만 관련 코드는 AI가 작성했으며, 현재 JavaParser를 사용해 직접 구현하거나 분석한 경험은 없다. 현재 확인된 본인의 연구 산출물은 논문 정리다.

---

## Research And Backend Signal

- JavaParser AST 분석, `MethodCallExpr` 추출, Symbol Solver resolution을 사용한다.
- parser는 Java로 구현되어 있으며, PowerShell runner가 JavaParser jar를 내려받고 `javac`로 컴파일해 실행한다.
- output은 `source_list_generated.csv`, `test_list_generated.csv`, `source_test_generated.csv`, `method_call_edges.csv`, `unresolved_calls.csv`, `parser_summary.json` 등으로 나뉜다.
- README 기준 verified summary는 source files `3460`, test files `114`, method calls `5486`, resolved calls `3479`, final test-source links `694`다.

---

## Portfolio Use

현재는 대규모 Java 코드베이스를 직접 분석·구현한 개발 경험으로 포지셔닝하지 않는다. 선배 연구를 이어 JavaParser·AST 개념을 학습하고 AI 생성 분석 결과를 검토하는 학부연구 참여 경험으로만 사용한다. 직접 작성한 JavaParser 분석과 검증 산출물이 생기면 다시 평가한다.

면접 핵심 문장:

> 선배가 남긴 source-test traceability 연구를 이어 JavaParser와 AST 개념을 학습하고 있습니다. 현재 분석 코드는 AI가 작성했기 때문에 구현 경험으로 과장하지 않고, 직접 작성·설명 가능한 분석을 만드는 것이 다음 과제입니다.

---

## Evidence Gaps

- 연구실에서 이 프로젝트가 맡은 역할
- 논문/졸업 연구와의 연결
- 직접 작성한 parser 코드는 현재 없음
- AI 생성 결과를 어떤 기준으로 검토했는지
- 매주 수행하는 연구 업무와 실제 제출 산출물
- 정리한 논문의 수·주제·형식과 교수·선배 피드백
- unresolved call 처리 기준
- 결과를 어떤 분석 또는 논문 방향으로 사용할지

---

## Sources

- https://github.com/gyutaetae/Graduation-elasticsearch
- https://raw.githubusercontent.com/gyutaetae/Graduation-elasticsearch/master/README.md
