---
type: query-result
aliases:
  - 2026-08-29 Vault Audit
description: "Read-only whole-vault audit of Wiki eligibility, MOC consistency, and claim confirmability, with a prioritized verify queue."
author:
  - Codex
date created: 2026-08-29
date modified: 2026-08-29
tags:
  - query
  - audit
  - verification
  - wiki-health
source:
  - "[[Core Context]]"
  - "[[index]]"
  - "[[MOC-Knowledge Management]]"
  - "[[MOC-LLM Wiki Guide]]"
  - "[[MOC-Portfolio]]"
  - "[[MOC-김규태 Self Knowledge]]"
  - "[[경제적 자유는 나의 북극성이다]]"
reusableFor:
  - LLM Wiki 운영
  - 취업/포트폴리오
confidence: medium
---

# 2026-08-29 LLM Wiki 전체 감사

## Scope

- 범위: `20. Wiki/` 전체 70개 페이지
- 구조: Concepts 40, Entities 10, Guides 15, MOCs 5
- 근거 풀: Raw Sources 40개, Queries 15개
- 방식: 전 페이지 `$verify` 후 YAML/v5 schema/H1/source/Related/wikilink/MOC 직접 포함을 재검사하고, high-confidence·프로젝트·개인·금융 문서를 근거와 대조
- standalone 경계: `mainVaultRelated`는 [[Core Context]]의 Mode A 정책에 따라 필수 결함으로 채점하지 않음

## Vault Health

| Gate | Score | Basis |
|---|---:|---|
| Eligibility | 100/100 | 70/70이 v5 필드, H1, non-empty source, Related surface를 갖고 YAML/claimType 검사를 통과 |
| Consistency | 98/100 | broken wikilink 0, direct MOC orphan 0, 확인된 material conflict 0; 전체 문장쌍 의미 비교는 비결정적 영역으로 남김 |
| Confirmability | 94/100 | `verified` 10, `partial` 60, `unverified` 0; high 10/10에 Bias Check와 1차·운영 근거가 있음 |
| **Composite Vault Health** | **97/100** | 세 점수의 단순 평균, 반올림 |

점수는 운영 상태를 비교하기 위한 지표다. `partial` 페이지의 개별 주장이나 사용자의 실제 역량이 97% 확실하다는 뜻이 아니다.

## Phase A — Eligibility

- YAML parse error: 0
- duplicate top-level key: 0
- invalid `claimType`: 0
- v5 metadata 완비: 70/70
- `verificationStatus`: `verified` 10, `partial` 60, `unverified` 0, `disputed` 0
- `confidence`: `high` 10, `medium` 54, `low` 6
- `explored`: `true` 3, `false` 67; 검증 작업은 이 값을 임의로 바꾸지 않음
- frontmatter source: 70/70
- frontmatter Related: 70/70
- H1: 70/70
- broken wikilink: 0
- MOC direct orphan: 0

본문 `## Sources`는 28개, `## Related`는 64개다. 나머지도 frontmatter에 source/related가 있으므로 이번 schema에서는 결함으로 채점하지 않았다.

## Phase B — Consistency

### Resolved material conflicts

- [[MOC-Portfolio]]와 [[김규태]]를 최신 [[Core Context]] 및 project entity에 맞춰 동기화했다. 공개 repository artifact, AI 작업, 사용자 판단, 직접 구현, 재실행 여부를 분리했다.
- [[MOC-LLM Wiki Guide]]와 architecture pages를 Codex-first `AGENTS.md → .agents/skills → .codex/commands` 순서로 통일했다. Claude files는 legacy mirror로만 남겼다.
- [[MOC-Knowledge Management]]의 존재하지 않는 직접 링크는 broken link가 아닌 `Unmaterialized Candidates` prose로 전환했다.
- 금융 cluster는 beta neutrality, delta neutrality, leverage, liquidity, option PnL을 구분했고 [[시장중립은 무위험이 아니다]]와 [[변동성 트레이딩과 델타 헤징]]을 공식 자료로 보강했다.
- 모든 Wiki page가 5개 MOC 중 하나에 직접 포함되도록 정리했다.

현재 deterministic check에서 material conflict는 0개다. 이는 70개 모든 문장의 의미적 모순이 수학적으로 부재함을 보장하지 않는다.

## Phase C — Confirmability

### Verified 10

- Repo operation/design: [[3-Layer Architecture]], [[Schema Engineering for LLM Wiki]], [[MOC-LLM Wiki Guide]], [[Web Clipper to Inbox Workflow]]
- Primary history/entity: [[Andrej Karpathy]], [[Vannevar Bush]], [[Memex]]
- Finance theory/risk: [[시장중립은 무위험이 아니다]], [[변동성 트레이딩과 델타 헤징]]
- Attributed infrastructure frame: [[AI 팩토리와 토큰 생산 인프라]]

### Partial 60

`partial`은 실패가 아니라 확인 범위를 명시한 결과다. 주요 이유는 다음과 같다.

- user-original 선호·목표·자기보고를 외부 관찰 성향이나 현재값으로 확대하지 않음
- repository/fixture/README 존재를 사용자 직접 구현·live service·재현 성공으로 확대하지 않음
- 로컬 운영 제안, 학습 전략, 아이디어 workflow를 구현 완료나 성과 측정으로 확대하지 않음
- Gemini/YouTube 출발점을 1차 자료로 보강했더라도 전체 synthesis를 보편 규칙으로 확정하지 않음
- qmd, citation manager, `$idea`, `$track`처럼 현재 미설치·미구현인 부분을 설계 상태로 유지

`high` 10개 모두 Bias Check를 갖는다. 전체 70개 중 Bias Check가 있는 페이지는 65개다.

## Conditional Re-verify Queue

다음 항목은 지금 다시 `$verify`를 반복하기보다 새 증거가 생길 때 재검증한다.

1. [[harness]] — 접근 가능한 현재 checkout/README와 원본 대비 변경점 확보
2. [[financial-order-latency-lab]] — 사용자가 직접 재구현·재실행한 Java/Linux 측정
3. [[cuee]] — 실제 사용자 테스트, live Korail 경계, Play 심사와 사용자 직접 구현 범위
4. [[Graduation-elasticsearch]] — 직접 작성·실행한 parser와 연구실 역할/피드백
5. [[자본 레버리지는 자유의 핵심 엔진이다]] — 최신 자산 snapshot, 현금흐름, 경로 의존 백테스트
6. [[qmd]] — 이 Mac에 설치하고 실제 indexing/search를 성공시킨 로그
7. [[Citation Manager Integration for LLM Wiki]] — citation schema와 round-trip prototype
8. [[Idea Generation Pipeline]] / [[Track Classification and Research Gap Detection]] — 실제 skill 구현, 정확도·신규성·수집 편향 평가
9. [[Personal Context Layer for LLM Wiki]] / [[메타인지 학습 루프]] — 비교 가능한 답변 품질·학습 유지율 기록
10. [[김규태 금융 시스템 개발자 취업 로드맵]] — 실제 지원 직전 최신 공고·학적·언어·프로젝트 상태 갱신

## Bias Check

> [!note] Bias Check
> 이번 감사 전 `$verify`에서 모든 페이지를 읽고 중요한 외부 주장을 1차·공식 자료로 보강했지만, `partial` 60개의 데이터 공백을 새 증거로 채운 것은 아니다. 특히 사용자 자기보고, AI가 작성한 프로젝트, fixture demo, 미구현 proposal은 정직하게 제한된 상태로 남겼다. `97/100`은 schema·연결·경계 관리 상태가 좋아졌다는 뜻이며 실서비스 검증률이나 개인 역량 점수가 아니다.
