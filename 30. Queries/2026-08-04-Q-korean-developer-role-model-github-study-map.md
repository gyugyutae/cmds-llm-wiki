---
type: query-result
aliases:
  - Korean Developer Role Model GitHub Study Map
description: Evidence-based comparison and study plan for learning open-source maintenance, agent workflows, commits, collaboration, and documentation from selected Korean developers.
author:
  - Codex
date created: 2026-08-04
date modified: 2026-08-04
tags:
  - query
  - developer-growth
  - github
  - open-source
  - ai-agents
  - documentation
source:
  - "[[Core Context]]"
  - "[[MOC-Portfolio]]"
  - "[[AI-Augmented Developer Positioning]]"
  - "[[AI 자동화는 개인 생산성 레버리지다]]"
  - "[[harness]]"
  - https://github.com/Yeachan-Heo
  - https://github.com/code-yeongyu
  - https://github.com/junegunn
  - https://github.com/yunjey
  - https://github.com/devxoul
  - https://github.com/velopert
  - https://github.com/milooy
  - https://github.com/jojoldu
  - https://www.ycombinator.com/companies/fountain
reusableFor:
  - Codex 개발 워크플로
  - 취업/포트폴리오
  - 독서/책/학습
  - 에세이/블로그
confidence: medium
claimType: synthesis
evidenceScope: public-github-snapshot-and-wiki
verificationStatus: partial
---

# 한국 개발자 롤모델 GitHub 학습 지도

## Query

허예찬, 류기백, 김연규, 최준건, 최윤제, 전수열, 박상권, 김민준, 진유림, 이동욱을 롤모델로 어떻게 공부할 것인가? 개발 의도, 코드 구조, AI/agent 활용, commit, issue/PR, README·문서화, 유지보수에서 각자에게 배울 점은 무엇인가?

## Scope And Metric Note

이 분석은 2026-08-04 공개 GitHub/YC 스냅샷을 기준으로 한다. `owned stars`는 GitHub가 제공하는 공식 프로필 지표가 아니라, 개인 계정이 소유한 공개 non-fork 저장소의 현재 star를 합산한 재현 가능한 수치다. 조직 저장소, 이전된 저장소, 공동 메인테이너십은 빠질 수 있다.

`Builders Only`의 허예찬 `190k+`, 김연규 `42k+`같은 표기와 아래 수치가 다른 것은 집계 범위와 시점이 다르기 때문으로 보인다. 따라서 서로 다른 홍보 지표를 직접 비교하지 않는다.

## Core Conclusion

한 사람을 통째로 복제하는 것보다 역할별 롤모델 포트폴리오가 적합하다.

- **AI agent 운영**: 허예찬 + 김연규
- **미니멀 오픈소스 설계와 장기 유지보수**: 최준건 + 전수열
- **연구 코드의 재현성과 교육적 구조**: 최윤제
- **백엔드 운영·테스트·글쓰기**: 이동욱
- **쉽게 가르치는 README와 제품화**: 김민준
- **협업 문화·Git/GitHub 교육·사람 성장**: 진유림
- **글로벌 사용자 문제와 사업 확장**: 류기백

김규태의 현재 과제에는 `허예찬/김연규의 agent gate + 최준건의 scope 절제 + 이동욱의 운영 증거 + 진유림의 협업 설명`이 가장 잘 맞는 조합이다.

## Current Public Snapshot

| Person | Confirmed public identity | Followers | Owned stars | Representative public evidence |
|---|---|---:|---:|---|
| 허예찬 | [Yeachan-Heo](https://github.com/Yeachan-Heo) | 4,694 | 74,594 | [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) 38,306, [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) 32,407 |
| 김연규 | [code-yeongyu](https://github.com/code-yeongyu) | 3,660 | 71,813 | [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) 67,164 |
| 최준건 | [junegunn](https://github.com/junegunn) | 8,650 | 151,240 | [fzf](https://github.com/junegunn/fzf) 82,233, [vim-plug](https://github.com/junegunn/vim-plug) 35,734 |
| 최윤제 | [yunjey](https://github.com/yunjey) | 3,519 | 40,238 | [pytorch-tutorial](https://github.com/yunjey/pytorch-tutorial) 32,446, [StarGAN](https://github.com/yunjey/stargan) 5,294 |
| 전수열 | [devxoul](https://github.com/devxoul) | 4,029 | 20,111 | [Then](https://github.com/devxoul/Then) 4,392, [URLNavigator](https://github.com/devxoul/URLNavigator) 3,346 |
| 김민준 | [velopert](https://github.com/velopert) | 3,771 | 5,156 | velog 제품군, React 교육 저장소 |
| 진유림 | [milooy](https://github.com/milooy) | 2,384 | 4,366 | [remote-or-flexible-work-company-in-korea](https://github.com/milooy/remote-or-flexible-work-company-in-korea) 3,293, Git/GitHub 교육 |
| 이동욱 | [jojoldu](https://github.com/jojoldu) | 6,726 | 16,818 | [junior-recruit-scheduler](https://github.com/jojoldu/junior-recruit-scheduler) 11,291, [blog-code](https://github.com/jojoldu/blog-code) |
| 류기백 | [kibaekr](https://github.com/kibaekr) / Keith Ryu | 31 | public repo 0 | [YC Fountain](https://www.ycombinator.com/companies/fountain) founder/operator evidence |
| 박상권 | 미확정 | - | - | 동명인을 분리할 GitHub/블로그 URL 필요 |

star는 인지도와 분포를 보여 주지만 코드 품질, 기여자 경험, 재현성, 지속 가능성을 보장하지 않는다. 따라서 아래의 공개 행동과 함께 봐야 한다.

## What To Learn From Each Person

### 허예찬 — agent 대량 실행을 증거 gate로 통제하기

- 최근 `oh-my-claudecode` 100 commit 중 79개가 conventional prefix를 사용했다. feature/fix/test/ci/release lane이 보이도록 분리한다.
- 저장소에 `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, 다국어 README, `docs/`, 여러 CI workflow가 함께 있다.
- [issue #3627](https://github.com/Yeachan-Heo/oh-my-claudecode/issues/3627)의 maintainer comment는 재현 행렬 감사 -> 루트 원인 -> fix PR -> 정확한 head/merge SHA -> CI 통과를 완료 증거로 남긴다. 댓글에 소유자의 `clawdbot`이라고 명시해 agent 작업 경계도 드러낸다.
- 5,954개 blob 중 test 패턴 파일이 약 2,898개인 거대한 test-heavy 구조다. 이는 배울 가치가 있지만 초보 프로젝트에 전체 복제할 모델은 아니다.
- 배울 핵심: `issue -> 조사 -> 작은 PR -> test/CI -> SHA와 관찰 결과로 완료 선언`.

### 김연규 — agent-native 저장소를 사람과 글로벌 기여자가 함께 다루게 하기

- `oh-my-openagent` README는 Jobdori라는 AI assistant가 feature, fix, issue triage를 유지보수한다고 공개한다. `AGENTS.md`는 Sisyphus agent의 issue/PR 처리 workflow도 명시한다.
- 최근 100 commit 중 67개가 conventional prefix, 32개가 merge commit이었다. 빠른 feature branch 통합 흐름이 직접 보인다.
- `CONTRIBUTING.md`는 English-first 이유, Bun-only setup, dev branch, local harness QA, PR checklist를 설명한다. `AGENTS.md`는 dev PR의 merge commit 정책과 실제 harness 구동 증거를 강제한다.
- [issue #6584](https://github.com/code-yeongyu/oh-my-openagent/issues/6584)에서는 보고자의 코드 경로가 맞는지 먼저 확인하고, failure chain을 순서대로 재구성한다.
- 배울 핵심: agent 수를 늘리기 전에 언어, branch, test, merge, release 규약을 저장소에 코드화하기.

### 류기백 — 코드가 아니라 문제·시장·운영 레버리지 공부

- 공개 GitHub에는 분석할 저장소가 없다. commit/PR/README 롤모델로 단정하면 안 된다.
- YC의 Fountain 프로필은 78개국에서 연 120만 명 이상을 채용하는 high-volume hiring 플랫폼으로 소개한다.
- 배울 핵심: 사람이 기존 채용 프로세스에서 어디서 이탈하는지, mobile-first automation이 어떤 운영 비용을 줄이는지, 한 국가의 해결책을 글로벌 제품으로 표준화하는 방법.
- `cuee`의 제품·사용자 검증에 이 관점을 적용하되, AI/agent 사용법은 현재 근거가 없으므로 따라 쓰지 않는다.

### 최준건 — 더 많이 넣기보다 기능 경계를 지키기

- `fzf`는 개인 소유 repo star 82,233, 전체 owned stars 151,240으로 이 목록에서 가장 큰 장기 글로벌 영향력을 보인다.
- 최근 100 commit은 conventional prefix 6개, merge commit 0개다. `Fix ...`, `Separate ...`, `Wrap ...`처럼 변경 효과를 직접 적는 imperative subject가 많다.
- [issue #4878](https://github.com/junegunn/fzf/issues/4878)에서 feature request를 거절하며 fzf를 all-in-one tool이 아니라 응용이 감싸 쓸 수 있는 기초 building block으로 남겨야 한다는 경계를 설명한다.
- [issue #4870](https://github.com/junegunn/fzf/issues/4870)에서는 환경 변수, popup 여부, preview option, terminal emulator를 하나씩 제거하며 재현 범위를 줄인다.
- README는 설치 -> shell/Vim 통합 -> 검색 문법 -> 예제 -> 성능 -> 고급 확장 순으로 사용자 성숙도를 따라간다.
- 배울 핵심: 코드 깔끔함을 줄 수로 보지 말고, non-goal을 지키는 제품 판단으로 보기.

### 최윤제 — 논문을 다른 사람이 실행할 수 있는 코드로 바꾸기

- `pytorch-tutorial`은 45개 blob의 작은 교육 저장소이며 README는 basics -> intermediate -> advanced -> utilities의 학습 사다리와 실행법·의존성을 즉시 보여 준다.
- `StarGAN`과 `StarGAN v2`는 논문, 결과 이미지, pretrained model, 실행 방법을 연결하는 연구 재현성 모델이다.
- 대표 tutorial의 최근 commit은 2020년이고 pushed timestamp는 2023년이다. 현재 AI agent 운영 또는 최근 PR 문화의 근거로 쓰면 안 된다.
- 배울 핵심: `Graduation-elasticsearch`의 README를 연구 질문 -> 데이터 -> 방법 -> 재현 명령 -> 결과 -> 한계 순으로 만들기.

### 전수열 — 작은 API와 완성도 높은 library stewardship

- `Then`은 11개 blob, `Sources`, `Tests`, 하나의 CI workflow로 구성된 작은 Swift library다.
- README는 `At a Glance -> Tips and Tricks -> Real World Example -> Installation -> License`로 짧고 사용 중심적이다.
- [issue #82](https://github.com/devxoul/Then/issues/82)에서 유지보수 속도가 느린 점을 솔직히 인정하면서도, 작고 완성된 library를 계속 단순하게 유지하겠다는 의도를 설명한다.
- [issue #106](https://github.com/devxoul/Then/issues/106)에서 Swift language mode와 actor isolation의 루트 원인을 짚고 API 변경 없이 해결하는 최소 수정을 PR로 연결한다.
- 배울 핵심: 적은 코드로 표현력 높은 API를 만들고, 플랫폼 변화 때만 정확히 보수하기.

### 김민준 — 독자의 출발점을 선언하는 교육·제품 문서

- `react-tutorial` README는 강의 출처, JavaScript 기초를 알고 있어야 한다는 전제, 강의 대상을 먼저 선언한다.
- velog 제품군과 React 교육 저장소는 `사용자가 어디서 막히는가`를 코드와 글 모두로 푸는 모델이다.
- 선택한 tutorial repo는 7 commit의 완결형 자료에 가깝다. 현재 오픈소스 유지보수 습관의 대표 표본으로 보지 않는다.
- 배울 핵심: README 첫 10줄에 `누구를 위한 것인지`, `무엇을 알아야 하는지`, `무엇을 만들게 되는지`를 쓰기.

### 진유림 — Git/GitHub을 사람 사이의 협업 언어로 설명하기

- `remote-or-flexible-work-company-in-korea`는 기여 규칙에 맞춰 회사 정보를 PR로 축적한 커뮤니티 아카이브다. 최근 100 commit 중 61개가 merge commit으로 외부 기여 통합 비중이 크다.
- 충돌이 난 PR에 `conflict 해결 부탁드립니다 ㅎㅎ`처럼 짧고 친근하게 다음 행동을 요청한 흔적이 있다.
- Git/GitHub 강의·저서와 공개 resume에서는 코칭, 1:1, 기술 토론, 코드 스멜 Wiki 등 개인 코딩을 넘어 팀의 성장 시스템을 다룬다.
- 배울 핵심: PR comment를 평가문이 아니라 상대가 바로 수정할 수 있는 다음 행동으로 쓰기.

### 이동욱 — 회사와 팀에 필요한 문제를 검증 가능한 글과 코드로 남기기

- 공개 resume는 대규모 traffic, 정산, test 2,500개, query 성능 5초 -> 1.2초처럼 문제·역할·수치를 연결한다.
- `blog-code` 최근 100 commit은 64개의 서로 다른 날짜에 걸쳐 있고 merge/conventional prefix가 없다. `작성중`, `피드백 반영`, `본문 도식 추가`처럼 글과 예제를 짧게 반복 개선한다.
- repo `AGENTS.md`는 한국어 commit 메시지, conventional prefix 미사용, 한국어 주석·문서, 용어 검증을 명시한다.
- 배울 핵심: 기술을 공부한 글이 아니라 실제 운영 문제, 재현 코드, test, before/after 수치가 있는 글을 쓰기.

### 박상권 — 식별 보류

이름만으로는 사용자가 뜻한 개발자와 GitHub 계정을 확정할 수 없었다. 헤이딜러 관련 박상권 프로필 등 동명인은 보이지만, 코드·star·maintainership을 같은 사람에게 귀속할 증거가 부족하다. URL을 받은 후 다시 분석한다.

## Commit Pattern Comparison

아래는 대표 repo 기본 branch의 최근 최대 100 commit 표본이다. 프로젝트 전체 이력이 아니며 관찰 창에 따라 달라진다.

| Repo | Sample | Conventional | Merge | Observation |
|---|---:|---:|---:|---|
| Yeachan-Heo/oh-my-claudecode | 100 | 79 | 2 | release/fix/test/ci lane을 prefix로 분리 |
| code-yeongyu/oh-my-openagent | 100 | 67 | 32 | feature branch를 자주 merge하는 고속 통합 |
| junegunn/fzf | 100 | 6 | 0 | 행동과 효과를 직접 쓰는 간결한 subject |
| yunjey/pytorch-tutorial | 100 | 0 | 27 | 2017-2020 교육 repo의 외부 패치 통합 기록 |
| devxoul/Then | 100 | 1 | 18 | 필요할 때 작은 library를 현대화 |
| velopert/react-tutorial | 7 | 0 | 0 | 강의 자료 단위의 완결형 commit |
| milooy/remote-or-flexible-work-company-in-korea | 100 | 7 | 61 | 커뮤니티 PR merge가 핵심 |
| jojoldu/blog-code | 100 | 0 | 0 | 글·예제를 여러 날에 걸쳐 작게 개선 |

결론은 conventional commit이 항상 우수하다는 것이 아니다. 에이전트가 많은 고속 repo에서는 machine-readable prefix가 유용하고, 최준건처럼 scope가 명확한 repo에서는 간결한 일반 문장도 충분하다. 핵심은 협업자가 diff를 읽기 전에 변경의 의도와 범위를 알 수 있는가이다.

## README And Documentation Patterns

| Pattern | Best model in this set | Application |
|---|---|---|
| 30초 안에 가치·설치·예제 보여 주기 | 최준건, 전수열 | 첫 화면에 실행 GIF/명령/결과 |
| 독자의 전제와 순서 선언 | 김민준, 최윤제 | prerequisite + basic/intermediate/advanced |
| 운영 규칙을 repo에 코드화 | 허예찬, 김연규 | AGENTS + CONTRIBUTING + CI + release policy |
| 문제·수치·재현 코드 연결 | 이동욱 | before/after + test + failure note |
| 외부 기여자가 바로 수정할 수 있는 규칙 | 진유림 | contribution schema + concrete review comment |

## A README Shape For 김규태

```markdown
# Project name — 한 문장 가치

## Problem
누가 어떤 상황에서 무엇으로 인해 실패하는가?

## Result In 30 Seconds
실행 명령, 화면/GIF, 핵심 수치.

## My Judgment
비교한 대안, 선택, non-goal.

## Architecture
데이터/요청 흐름과 핵심 모듈 역할.

## Agent Boundary
내가 판단한 것 / AI에게 맡긴 것 / 내가 검증한 것.

## Reproduce And Verify
설치, test, benchmark, 환경, 예상 결과.

## Failures And Trade-offs
실패한 시도, 알려진 한계, 다음 실험.

## Contributing And Maintenance
issue/PR 형식, branch, CI, release 정책.
```

## Recommended Additional Role Models

| Person | Why add them | What to study first |
|---|---|---|
| [Simon Willison](https://github.com/simonw) | AI 실험을 코드·데모·release note·blog로 투명하게 남김 | LLM 신기능을 작은 tool로 검증하고 변경 이력을 설명하는 법 |
| [Sindre Sorhus](https://github.com/sindresorhus) | 작은 패키지, 일관된 README, 명확한 contribution 경계의 대표적 메인테이너 | 하나의 문제만 푸는 module과 거절 규칙 |
| [Anthony Fu](https://github.com/antfu) | 현대 TypeScript/Vue 생태계의 다수 repo를 일관된 개발자 경험으로 운영 | monorepo, docs, playground, config 기본값 |
| [Mitchell Hashimoto](https://github.com/mitchellh) | 개발자 도구를 제품 품질로 끌어올리는 설계·성능·크로스플랫폼 사고 | Ghostty 같은 프로젝트의 설계 문서와 scope 관리 |
| [박재성](https://github.com/javajigi) | 한국 Java 커뮤니티의 TDD, refactoring, peer learning 문화 | 자동차 경주·보드게임 미션의 작은 단계와 피드백 구조 |
| [이종립](https://github.com/johngrib) | 개발자 wiki와 학습 기록을 오랫동안 링크된 지식으로 축적 | TIL을 정의·예제·출처·관련 노트로 편집하는 법 |
| [[Andrej Karpathy]] | AI를 first principles 코드와 교육자원으로 설명 | micrograd/nanoGPT의 최소 구현과 학습 순서 |

## Eight-Week Practice Plan

| Week | Model | Output In 김규태's Repo |
|---|---|---|
| 1 | 최준건 | 각 대표 프로젝의 non-goal 3개와 제거할 기능 1개 |
| 2 | 이동욱 | `financial-order-latency-lab`에 문제·재현·p99 before/after 증거 추가 |
| 3 | 최윤제 | `Graduation-elasticsearch`에 연구 질문·데이터·방법·한계 추가 |
| 4 | 허예찬 | `harness`에 issue -> PR -> test -> completion evidence 흐름 1개 적용 |
| 5 | 김연규 | `harness`의 AGENTS, branch, test, merge 규칙을 1page로 축소·명확화 |
| 6 | 전수열 + 김민준 | 대표 프로젝 README 첫 30초 경험과 작은 API/모듈 하나 개선 |
| 7 | 진유림 | 다른 사람이 실제로 바로 쓸 수 있는 issue template + PR template 작성 |
| 8 | 류기백 | `cuee`의 사용자 funnel, 이탈 지점, 운영 자동화, 실제 지불/사용 증거 설계 |

각 주의 완료 조건은 글을 읽은 것이 아니라 `commit 1개 + PR 설명 1개 + 검증 결과 1개`다.

## Quality Gaps

- 박상권은 공개 URL 없이 식별할 수 없다.
- 류기백의 코딩, AI/agent, commit/PR 습관은 공개 근거가 부족하다.
- 김민준·진유림·최윤제의 대표 repo 중 여러 개는 최근 유지보수 표본이 아니다. 지속적 교육/커뮤니티 공헌과 현재 repo 활동을 분리해야 한다.
- 공개 GitHub만으로 회사 내부 코드 품질, 사전 기획, 실패, AI 사용량을 확인할 수 없다.
- 저장소 star와 follower는 2026-08-04 스냅샷이며 계속 변한다.

> [!note] Bias Check
> star가 큰 개발자만 보면 developer tool·English-speaking open source·공개 활동에 유리한 사람이 과대 대표된다. 회사 내부에서 훌륭한 운영 코드와 협업 문화를 만든 개발자는 GitHub star가 적을 수 있다. 따라서 인지도가 아니라 김규태의 현재 약점을 보완하는 공개 행동을 선택한다.

## Reuse Axis

이 답변은 Codex 개발 워크플로, 취업/포트폴리오, 독서/책/학습, 에세이/블로그에 활용 가능합니다 — 롤모델의 명성을 소비하는 데서 그치지 않고, 공개된 개발 판단을 자신의 프로젝트 증거로 바꾸는 반복 학습 계획으로 전환하기 때문입니다.
