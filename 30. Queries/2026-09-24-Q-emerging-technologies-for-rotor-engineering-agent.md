---
type: query-result
aliases:
  - 로터 엔지니어링 에이전트 최신 기술 조사
  - 프로펠러 에이전트 KICK 기술 후보
description: "A feasibility-ranked review of current open-source technologies for differentiating a rotor engineering evidence agent, with explicit data and validation gates."
author:
  - Codex
date created: 2026-09-24
date modified: 2026-09-24
tags:
  - query
  - aerospace
  - agentic-ai
  - rotor
  - cfd
  - bayesian-optimization
source:
  - "[[Propeller Evidence Agent 1]]"
  - "[[2026-09-01-Q-emerging-traceability-technology-selection]]"
  - https://github.com/CadQuery/cadquery
  - https://github.com/meta-pytorch/botorch
  - https://github.com/csml-rpi/Foam-Agent
  - https://github.com/tianhanz/ChatCFD
  - https://github.com/jwjoo00/myOpenFoamAgent
  - https://github.com/csml-rpi/FoamGPT
  - https://github.com/AGN000/AutoFOAM
  - https://github.com/woog97/cfd-agent
  - https://github.com/NVIDIA/physicsnemo
  - https://github.com/NVIDIA/physicsnemo-cfd
  - https://github.com/ansys/pyfluent-mcp
  - https://fluent-mcp.docs.pyansys.com/
  - https://pypi.org/project/ansys-fluent-mcp/
  - https://fluent.docs.pyansys.com/version/stable/user_guide/session/launching_ansys_fluent.html
  - https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/flu_ug/flu_ug_sec_use_aeronoise_use.html
  - https://zenodo.org/records/17941588
  - https://arxiv.org/abs/2509.18178
reusableFor:
  - 프로젝트 증거
  - 취업/포트폴리오
  - 학부연구생/학술
  - 강의/수업/교육
confidence: medium
status: active
---

# 로터 엔지니어링 에이전트의 KICK이 될 최신 기술 후보

## 결론

프로젝트의 차별화 후보로 **형상·조건을 함께 이해하는 과거 사례 검색 + 다음 시험의 정보가치를 설명하는 Human-in-the-loop test-planning agent**를 추천한다. 단순 LLM 문서 검색이나 여러 에이전트 이름을 붙이는 것보다, 형상/조건이 달라 비교할 수 없는 경우를 잡고 다음에 무엇을 측정해야 불확실성이 줄어드는지 제안하는 흐름이 항공우주 제조·시험 업무에 더 직접 연결된다.

다만 현재 데이터가 매우 제한적이므로 첫 버전에서 “AI가 최적 프로펠러를 예측한다”거나 “소음을 낮춘다”고 주장하면 안 된다. 공개 eVTOLUTION 데이터는 실험 근거의 파서·비교 게이트를 검증하는 자료로 쓰고, 다음 시험 추천은 **coverage gap 또는 제한된 후보 중 정보가치 기준의 실험 설계 데모**로 분리한다. 실측 자료가 충분해진 뒤에만 BoTorch 기반 불확실성 모델/다목적 최적화를 제품 기능으로 승격한다.

## 기술 후보와 적합성

| 우선순위 | 기술 / 저장소 | 프로젝트에 쓰는 역할 | 적합성 및 주의점 |
|---|---|---|---|
| 1 | CAD-aware retrieval: [CadQuery](https://github.com/CadQuery/cadquery) / OCCT | 매개변수 CAD, STEP 기반 후보 형상 생성·기술 피처 계산·설계 버전 연결 | 로터 형상 검색을 파일명/설명 검색에서 형상 파라미터 기반 검색으로 발전시킬 기반. 하지만 CadQuery는 CAD 라이브러리이지 자동 프로펠러 이해/성능 예측 모델은 아니다. 실제 STEP 파일이나 공개 형상 파라미터가 없다면 즉시 구현 범위를 작게 둔다. |
| 2 | Active learning / multi-objective Bayesian optimization: [BoTorch](https://github.com/meta-pytorch/botorch) | 추력·소음 등 상충 목표에서 Pareto trade-off를 찾고, 다음에 시험할 후보/조건을 고름 | “최고 후보를 예측”보다 “현재 불확실성을 가장 줄일 다음 시험”을 추천하는 연구 방향. 다만 학습 가능한 충분한 비교 가능한 측정값이 필수다. 현재의 4엽/5엽 서로 다른 RPM 데이터로 실제 최적화나 실험 추천을 주장할 수 없다. |
| 3 | Agentic CFD + MCP: [Foam-Agent](https://github.com/csml-rpi/Foam-Agent) | CFD 워크플로를 강한 타입의 도구로 분해해 기존 LangGraph 오케스트레이터에서 선택적으로 호출 | 최신 논문/공개 구현을 참고할 만한 직접 유사 사례. 논문은 110개 OpenFOAM 과제에서 자체 성공률을 보고하지만, 그 수치는 해당 벤치마크·모델 구성에 한정되고 프로펠러 음향 정확도를 뜻하지 않는다. rotor acoustics 검증 없이 전체 CFD 자동실행을 MVP 핵심으로 삼지 않는다. |
| 4 | Physics-ML / surrogate / active-learning infrastructure: [NVIDIA PhysicsNeMo](https://github.com/NVIDIA/physicsnemo), [PhysicsNeMo-CFD](https://github.com/NVIDIA/physicsnemo-cfd) | 충분한 시뮬레이션 데이터가 쌓인 뒤 CFD 결과 surrogate를 학습·평가하거나 시뮬레이션 데이터 생성 루프 구성 | H200을 쓸 수 있는 연구 확장축. PhysicsNeMo는 현재 모델/레시피/active-learning 기능을 제공하지만, CFD 패키지는 README가 experimental v0이며 production 안정 API가 아니라고 밝힌다. 학습 데이터·검증용 held-out 케이스 없이 GPU만으로 믿을 만한 예측이 생기지는 않는다. |
| 5 | Retrieval-augmented CFD tool agent: [Foam-Agent MCP docs/repo](https://github.com/csml-rpi/Foam-Agent) | CFD 설정·실행·오류/후처리를 MCP 도구로 노출하고 상위 agent가 정책·승인 제어 | 컴퓨터 화면을 클릭하는 agent보다 API/명령행 도구가 재현성과 감사에 유리하다. 프로젝트는 Foam-Agent를 그대로 가져오기보다 tool schema, validation, reviewer loop 구조를 참조한다. |

## 추천 아키텍처: Evidence-to-Test Loop

```text
사용자 목표/제약
  → geometry + operating-condition 검색
  → 관계형 DB의 실험/해석 evidence 조회
  → Python 비교 가능성·단위·품질 게이트
  → (자료 부족) 순위 보류 + missing evidence 설명
  → (자료가 있는 제한 영역) 다음 시험 후보 / 정보가치 산정
  → 사람 승인
  → 새 결과 등록 후 evidence loop 갱신
```

- 관계형 DB는 수치, 형상 revision, 시험조건, 출처 관계의 기준 저장소로 둔다.
- 문서·벡터검색은 보고서의 설명과 페이지 근거 검색에 쓴다. GraphRAG를 핵심 KICK으로 추가하지 않는다.
- CadQuery/OCCT는 CAD 파일에서 형상 지표를 만들 수 있는지 확인하는 탐색 과제다. 당장 CAD 파일이 없다면 블레이드 수, 직경, 피치, chord/twist 등 확인된 명시 파라미터만 구조화한다.
- LLM agent는 요청 구조화, 알맞은 검색·분석 도구 선택, 누락값 질의, 근거 설명, 검토 요청을 맡는다. 수치비교·단위환산·적격성 판정·최적화는 deterministic Python/검증된 BO tool이 담당한다.
- MCP는 도구 연결 표준으로만 사용하고, 여러 agent를 늘리는 것이 핵심 혁신이라는 식으로 말하지 않는다.

## 대회용 단계 제안

### 지금 시연 가능한 “KICK”

1. 데이터셋 파일과 실험 조건을 정규 스키마로 적재하고, 출처·페이지·파일 해시를 보존한다.
2. 조건/형상 비교가능성 게이트를 만든다. 서로 다른 RPM·마이크 설정·형상 버전은 조용함 순위에 섞지 않는다.
3. 일반 키워드 검색과 구조화 검색을 비교하고, “잘못 매칭한 유사 케이스”와 “맞게 보류한 비교 불가 케이스”를 평가한다.
4. 다음 측정 추천은 AI가 빈 데이터에서 수치를 예측하는 기능이 아니라, 아직 없는 조건 축/범위를 찾아 사람에게 승인 후보를 제시하는 coverage gap demo로 구현한다.
5. 시스템이 비교를 거부하는 실패 사례까지 시연한다. 항공우주에서 이 정직한 abstention과 provenance가 단순 생성형 답변보다 설득력 있는 차별점이다.

### Stretch / 연구 확장

- 팀이 H200 접근, 시간, 저장공간, 설치 권한을 확인한 뒤 한 개의 공개·재현 가능한 OpenFOAM benchmark를 MCP 또는 CLI로 실행한다.
- 첫 단계는 CFD 입력 생성 전체 자동화가 아니라, 고정된 검증 case 실행 → 수렴/잔차 검사 → 파일·설정·로그 보존 → 사람 승인으로 제한한다.
- PhysicsNeMo surrogate는 여러 parametric simulation 결과와 독립 검증 세트를 확보한 뒤 검토한다.
- BoTorch multi-objective Bayesian optimization은 동일 조건 또는 모델링 가능한 시험 설계에서 충분한 샘플과 불확실성 평가가 가능한 단계의 후속 목표다.

## 심사에서의 주장과 증거

추천 스토리:

> “우리는 LLM이 프로펠러 소음을 상상해서 예측하게 하지 않습니다. 설계 형상과 시험 조건을 먼저 맞춰 과거 근거를 재사용하고, 근거가 모자라면 비교를 보류하며, 다음에 어떤 시험을 해야 판단이 나아지는지 제안하는 항공우주 시험 의사결정 에이전트를 만듭니다.”

증명할 지표 후보:

- 질문에서 유사 실험 근거 찾는 시간: 키워드/수동 baseline 대비
- 필수 비교조건 충돌 감지 precision/recall
- 근거 페이지/원본 파일 연결 비율
- 비교 불가 사례에서 잘못된 순위를 내지 않은 비율
- 사람이 승인/수정한 다음 시험 제안의 비율 및 추천 이유의 추적 가능성
- CFD stretch에서는 단순 “실행 성공”이 아니라 고정 reference case 기준 결과 편차·수렴·반복 재현성

## 핵심 한계

- 공개 데이터는 학술 풍동/실험 자료이고 제조사의 제품·공정·품질 데이터가 아니다.
- 데이터가 희소하고 시험조건이 다르면 유사도 검색, AI 예측, Bayesian optimization 모두 쉽게 과신될 수 있다.
- CAD geometry similarity는 aerodynamic/acoustic equivalence를 자동으로 증명하지 않는다.
- CFD 유동 해석이 돌아가는 것과 로터의 검증된 소음 예측은 서로 다른 주장이다.
- H200 지원은 실제 endpoint, 접근 권한, 사용량, 컨테이너 제약이 확인되기 전까지 계획 가정이다.
- MCP로 임의 CFD 실행을 열어두면 비용, 파일/명령 주입, 자원 고갈 위험이 있으므로 허용된 템플릿, sandbox, resource budget, approval gate를 적용해야 한다.

## CFD agent 저장소 비교 업데이트 (2026-09-24)

GitHub stars는 이 날짜에 확인한 대략적인 인기도 스냅샷이다. 도메인이 좁아 널리 쓰이는 범용 프레임워크 수준의 star 수와 비교할 수 없고, 품질·정확도·유지보수 보증으로 해석하지 않는다.

| 저장소 | 대략 stars | 확인된 범위 | 프로젝트 관점 |
|---|---:|---|---|
| [Foam-Agent](https://github.com/csml-rpi/Foam-Agent) | 326 | OpenFOAM 작업을 multi-agent workflow와 MCP 서비스로 분해; 논문 저자 측 110-case benchmark 보고; MIT license | 공개 채택과 tool-composability 기준 참고 1순위. 우리 LangGraph의 하위 CFD tool adapter 참고에 적합. |
| [ChatCFD](https://github.com/tianhanz/ChatCFD) | 66 | 구조화 지식 DB, 오류 위치 추적, reflection, paper/PDF+mesh 입력; 논문에서 315 cases, execution success와 physical fidelity 각각 보고 | **새로 추가할 핵심 비교군.** 물리 조건 검증과 생성된 입력 검토 설계 참고에 좋음. OpenFOAM 2406/Python 의존성이 고정적이며 우리 로터/음향 데이터에 검증된 모델은 아니다. |
| [FoamGPT](https://github.com/csml-rpi/FoamGPT) | 17 | OpenFOAM tutorial 기반 데이터 처리·LLM fine-tuning recipe 공개 | H200으로 CFD 전용 LLM 학습을 고민할 때 참고는 가능하나, 현 데이터량/기간에 재현·튜닝·평가를 수행하기엔 우선순위 낮음. |
| [woog97/cfd-agent](https://github.com/woog97/cfd-agent) | 12 | ChatCFD를 설명하는 README와 OpenFOAM v2406 지식베이스 기반 workflow를 가진 별도 공개 저장소 | `ConMoo/ChatCFD` 링크는 `tianhanz/ChatCFD`로 redirect된다. 둘의 코드/데이터 관계는 확인하지 못했으므로 별도 프로젝트로 취급하고 본격 채택 전 재현성 확인 필요. |
| [AutoFOAM](https://github.com/AGN000/AutoFOAM) | 6 | 로컬 14B 모델, tutorial RAG, 재시도·active-learning 기반 self-evolution을 표방; OF 2412와 모델 접근 필요 | 현재 star와 배포 제약을 고려하면 참고 탐색용. self-modifying agent는 보안·검증·데모 범위에서 제외한다. README상 모델 weight 접근 요청이 필요하다. |
| [myOpenFoamAgent](https://github.com/jwjoo00/myOpenFoamAgent) | 1 | MRF 회전기계·파라미터 프로펠러 geometry·실험/benchmark 결과 확인, typed tools와 사람 승인 주장; GPL-3.0 | **로터 도메인 유사성은 매우 높아 코드보다 검증 시나리오/진단 체크리스트 참고 가치가 큼.** star/사용자 기반은 작고, README가 개인 프로젝트라 독립 재현·코드 품질 확인 전 통합하지 않는다. GPL 의무 검토 필요. |

ChatCFD 논문은 자체 실험에서 315개 케이스 기준 실행 성공률과 물리적 타당성을 분리해 보고했고, 성공적으로 실행되는 설정도 물리 조건에 어긋날 수 있음을 강조한다. Foam-Agent 논문의 기존 수치(110개 케이스)와는 벤치마크, 모델 버전, 실행 조건이 다르므로 성공률 숫자를 그대로 서열 비교하지 않는다.

### 현재 프로젝트에 가장 적합한 채택 판단

1. **직접 채택할 CFD agent 제품은 없음.** 우리 MVP는 CFD 수행 자동화가 아니라 유사 해석·시험 evidence 재사용과 조건 비교성 판정이 중심이다. 전체 CFD agent를 붙이면 검증해야 할 입력·격자·solver·수렴·음향모델이 늘어 스코프가 새어 나간다.
2. **아키텍처 참고는 Foam-Agent 우선.** 상대적으로 가장 높은 GitHub 별 수, MIT, MCP로 기존 LangGraph workflow에 개별 기능을 연결하는 구조가 우리와 가장 잘 맞는다.
3. **품질 게이트 설계는 ChatCFD 우선 참고.** 실행 성공과 물리적 타당성을 별도 평가하는 방식, 오류 탐지·reflection·구조화 지식베이스가 우리 비교 보류/검토 논리와 유사하다.
4. **도메인 데모 영감은 myOpenFoamAgent를 검토.** 소형 회전익/프로펠러 케이스와 reference validation을 다룬다는 점은 직접적이다. 단, 인기/재현성이 확보된 솔루션이라 말하거나 코드에 의존하지 말고, DTMB 4119/Wageningen 등 검증 사례와 실패 판정 흐름만 참고한다.
5. CFD 시연을 넣는다면 1개의 고정 reference case를 사람이 승인한 뒤 실행하고, 설정·수렴·force/thrust·결과 파일과 reference 편차를 보이는 데 그친다. 소음 최적화, 새 형상 신뢰 예측, 자유형 자연어를 통한 안전한 전자동 CFD는 주장하지 않는다.

## Sources and existing Wiki context

- Current team scope: [[Propeller Evidence Agent 1]]
- Prior traceability-tech evaluation: [[2026-09-01-Q-emerging-traceability-technology-selection]]
- NVIDIA PhysicsNeMo: https://github.com/NVIDIA/physicsnemo
- NVIDIA PhysicsNeMo-CFD and its experimental-v0 warning: https://github.com/NVIDIA/physicsnemo-cfd
- BoTorch multi-objective Bayesian optimization: https://github.com/meta-pytorch/botorch/blob/main/docs/multi_objective.md
- Foam-Agent source repository: https://github.com/csml-rpi/Foam-Agent
- Foam-Agent 2025 paper: https://arxiv.org/abs/2509.18178
- CadQuery / OCCT: https://github.com/CadQuery/cadquery
- eVTOLUTION public experimental record: https://zenodo.org/records/17941588
- ChatCFD 2026 paper (execution success + physical fidelity): https://doi.org/10.1002/aidi.202500174
- OpenFOAM agent repository comparison: https://github.com/tianhanz/ChatCFD, https://github.com/woog97/cfd-agent, https://github.com/jwjoo00/myOpenFoamAgent, https://github.com/csml-rpi/FoamGPT, https://github.com/AGN000/AutoFOAM

## 공식 CFD 인터페이스와 OpenFOAM CLI 가능성 확인 (2026-09-24)

### MCP / 플러그인 구분

- CFD는 소프트웨어 하나가 아니라 해석 방법의 이름이다. 아래는 팀 후보인 OpenFOAM을 기준으로 확인했다.
- 확인한 공식 OpenFOAM 문서는 OpenFOAM applications와 utilities를 CLI에서 실행해 case setup, execution, evaluation, batch processing을 제어하는 방식을 공식 사용 경로로 설명한다. `blockMesh -help`, case 인자, background run, 병렬 실행, `postProcess` 등이 문서화돼 있다.
- 공식 문서에서 OpenFOAM 자체가 MCP 서버를 공식 포함/지원한다는 안내는 확인하지 못했다. 이는 공식 문서에서 확인되지 않았다는 뜻이지, 서드파티 MCP가 없다는 뜻은 아니다.
- OpenFOAM에는 플러그인형 확장에 가까운 `functionObjects`, 사용자 library, solver, boundary condition 등 확장점이 있다. 특히 `functionObject`는 controlDict 설정과 필요 라이브러리를 통해 실행/후처리 기능을 추가한다. GUI 확장 marketplace식 plugin과 같지는 않다.
- Foam-Agent는 OpenFOAM 본체의 기능이 아니라 외부 LangGraph/MCP agent implementation이다. 현재 README 기준 default는 Foundation OpenFOAM v10, ESI/OpenCFD v2006 선택 target이며, 최신 OpenCFD v2606 API와 버전 호환을 전제하면 안 된다.

### 사용 목표를 실현할 수 있는 공식 OpenFOAM 기능

- OpenCFD API v2606에는 `propellerInfo` function object가 문서화되어 있다. 회전 모드를 지정하거나 MRF zone과 연결해 추력 계수 `Kt`, 토크 계수 `10*Kq`, advance ratio `J`, open-water efficiency `etaO`와 wake 결과를 기록한다.
- OpenFOAM v2312 문서에는 `Curle` function object가 있다. Curle analogy로 acoustic pressure를 계산하고 observer 위치로 출력할 수 있다. 다만 문서상 정상 압력(normal-pressure) force만 포함하며 postProcess utility로 실행할 수 없고 simulation 중에 계산한다.
- 따라서 이미 만들어 둔 로터 CFD case를 OpenFOAM CLI로 반복 실행하고, 성능 계수 및 제한된 음향 pressure 지표를 파일로 남겨 우리 Python/DB evidence pipeline에 연결하는 것은 기술적으로 가능하다.
- 단, 이 기능이 임의 CAD에서 mesh/경계조건/회전 모델/수렴 기준을 자동으로 맞춰주지는 않는다. 소음 출력도 곧바로 공인 dBA·운항 소음 예측 정확도를 의미하지 않는다. 형상, RPM, 추력/전진비, 관측 위치, 격자/시간 단계와 해석 모델이 통제되고 실험 reference로 검증돼야 후보 간 비교를 주장할 수 있다.

### 권장 통합 경로

1. 우선 사람이 검증한 단일 propeller tutorial/reference case를 하나 고정하고 OpenFOAM 버전을 확정한다.
2. 에이전트가 자유로운 shell command를 생성하지 않도록, 입력 parameter schema와 허용 명령 목록을 둔다. 예: case copy → 필요한 dictionary 값 검증 → `checkMesh` → solver run → output parser.
3. `propellerInfo`의 성능 산출물을 수집한다. Curle는 해당 solver/유동 조건과 버전에서 function object 설정·실행을 검증한 뒤에만 음향 데이터로 쓴다.
4. run ID, geometry hash, case/config hash, OpenFOAM 버전, mesh/solver 설정, 수렴 상태, 출력 파일, 사람 승인 결과를 DB에 저장한다.
5. agent는 기존 결과 검색, 파라미터 변경 제안, 실행 전 검증 체크리스트 작성, 실행 상태 설명을 하고 실행/수정/제출 전에는 승인 gate를 둔다.

상용 Ansys Fluent가 이미 대회 환경에 제공된다면 공식 PyFluent API와 meshing/solver workflows가 있으므로 MCP 없이 Python에서 제어 가능하다. 라이선스·버전·환경을 확보해야 한다. 팀이 현재 선택한 OpenFOAM을 전제로 하면 별도 MCP 구현은 필수 기능이 아니다.

### Revised verdict

**CLI로 하고자 하는 실험의 일부는 실현 가능하다.** 명시된 회전 속도와 고정 geometry/case에서 solver를 반복 실행하고 propeller 성능 coefficient, wake, Curle acoustic pressure output을 모으는 benchmark는 가능성이 있다. 반면 “자연어만으로 새 프로펠러 형상을 설계→mesh→CFD→실제 저소음 조합 판정”은 격자/물리조건 검토와 acoustic validation까지 들어가므로 현 MVP의 안전한 주장 범위를 벗어난다.

권장 선택은 **MVP에서 OpenFOAM 공식 CLI + 고정 reference case + Python parser를 먼저 검증하고, 외부 Foam-Agent MCP는 필요 시 참고**하는 것이다. 이는 공식 backend와 third-party agent protocol을 분리하고, 버전 호환/보안/재현성을 우리 팀이 통제하기 쉽다.

Official references:

- OpenFOAM CLI and batch processing: https://doc.openfoam.com/2606/fundamentals/command-line/
- OpenFOAM case/application workflow: https://www.openfoam.com/documentation/user-guide/3-running-applications
- Official functionObjects and dynamic library pattern: https://api.openfoam.com/2506/namespaceFoam_1_1functionObjects.html
- Official propellerInfo API: https://api.openfoam.com/2606/classFoam_1_1functionObjects_1_1propellerInfo.html
- Official Curle function object: https://doc.openfoam.com/2312/tools/post-processing/function-objects/field/Curle/
- Official Ansys PyFluent APIs: https://fluent.docs.pyansys.com/version/stable/api/api_contents.html
- Third-party Foam-Agent MCP implementation and supported OpenFOAM targets: https://github.com/csml-rpi/Foam-Agent

> [!note] Bias Check
> “최신” 또는 “AI Agent”라는 이름만으로 기술적 적합성이 입증되지는 않는다. 저장소의 기능은 현재 공개 README/문서에서 확인했지만, 프로젝트의 실제 성능·설치 호환성·H200 접근은 별도 검증이 필요하다. 이 추천의 novelty는 새로운 foundation model이 아니라 geometry-aware evidence reuse와 uncertainty-aware test planning을 하나의 human-approved workflow로 묶는 데 있다.

이 답변은 프로젝트 증거와 학부연구생/학술에 활용 가능합니다 — 도메인 맞춤 retrieval, 보류 정책, 다음 시험 설계를 측정 가능한 구현·평가 축으로 구체화하기 때문입니다.

## Ansys Fluent 공식 MCP 지원 및 CFD 선택 재평가 (2026-09-24)

### 먼저 결론

팀이 이미 쓰는 CFD가 Ansys Fluent라면 **Fluent를 유지하는 것이 현재 프로젝트에 가장 잘 맞는다.** 기존 작업환경을 버리지 않아도 되는 데다, Ansys의 PyFluent Python API와 Ansys 조직의 공식 PyFluent-MCP가 확인됐다. 앞 절의 OpenFOAM 우선 권고는 팀의 현재 solver를 알기 전, OpenFOAM 중심으로만 비교한 잠정안이므로 여기서 갱신한다.

### 공식 지원 범위와 주의점

- Ansys 공식 PyFluent는 Python에서 Fluent를 실행하거나 이미 실행 중인 Fluent에 연결하고, mesh workflow·solver 설정·계산·결과 추출을 자동화할 수 있다.
- Ansys 소유 `ansys/pyfluent-mcp` 저장소와 공식 PyAnsys 문서가 `ansys-fluent-mcp` MCP 서버를 제공한다. 이 서버는 Fluent/PyFluent 기능을 MCP 도구로 노출하며 세션 연결, 설정/API 탐색, 검증된 Python 실행 경로, mesh 품질 검사, 결과/파일 비교, 보고서 등의 도구를 제공한다. 즉 **Fluent 연동 자체와 MCP 도구 브리지는 공식**이다.
- 단, PyFluent-MCP는 에이전트 두뇌나 LangGraph 대체품이 아니다. 공식 설명대로 결정론적 도구 레이어이고, 계획·모델 라우팅·workflow reasoning은 우리 LangGraph가 맡는 구조다.
- 최신 확인 release는 PyPI `0.4.0`(2026-08-14)이며 패키지 분류가 `Alpha`다. 대회용 프로토타입에서 시험해볼 수 있지만, 성숙한 상용 운영 솔루션이라고 포장하면 안 된다. MCP 실 solver 동작에는 Python 3.12+와 PyFluent, 라이선스가 있는 Fluent 설치가 필요하다. 팀의 실제 Fluent release/PyFluent 호환성과 사용 가능한 라이선스 seat는 별도로 smoke test 해야 한다.

### 프로펠러 소음 문제와 CFD별 적합성

| 후보 | 우리에게 유리한 점 | 중요한 제약 | 판정 |
|---|---|---|---|
| Ansys Fluent + PyFluent-MCP | 이미 팀이 사용 중. 공식 Python API + 공식 MCP tool bridge. 공식 FW-H aeroacoustics가 source surface와 observer에서 pressure signal을 계산하고 FFT/SPL 분석을 지원 | MCP는 Alpha. FW-H는 transient time-accurate 유동/충분한 수렴·시간 해상도·source/receiver 설정이 필요하고 비용이 클 수 있음. steady 단일 moving-reference-frame 근사는 표면 압력 시간미분 항을 0으로 둠 | **1순위 유지** |
| OpenFOAM | 오픈소스, 공식 CLI로 case 실행·평가·batch automation. 공식 도구에 프로펠러 성능 지표와 Curle acoustic-pressure 처리 경로가 있음 | Fluent case·mesh·모델·스크립트를 옮기고 다시 검증해야 함. Curle 기능은 제한된 acoustic approximation이며 postProcess 단독 실행 불가. 공식 OpenFOAM MCP는 확인하지 못했고 Foam-Agent는 별도 제3자 구현 | 라이선스 문제 또는 공개 재현성 요구가 크면 대안 |
| SU2 등 다른 solver | 오픈소스/연구 solver 선택지 | 현재 팀의 Fluent 환경에 비해 전환·검증 비용이 생기고, 이번 조사 범위에서 우리 프로펠러 FW-H와 agent 연결의 이득을 확인하지 못함 | 지금은 전환 근거 부족 |

Fluent의 FW-H는 기본적으로 시간에 따라 변하는 유동장 표면 데이터를 받아 지정한 수음점(receiver)의 음압 신호를 계산하는 절차다. transient 소음 비교는 통계적으로 안정된 유동까지 먼저 계산하고, source data를 적절한 간격/기간으로 모아야 한다. steady 단일 moving reference frame도 지원되지만 time derivative of surface pressure 항을 0으로 두므로, 이 설정의 수치를 실제 운항 소음 또는 transient 예측과 동등하게 해석하면 안 된다.

### 우리 시스템에 넣을 모양

```text
LangGraph Evidence Agent
  ├─ 기존 문서/CFD run 검색 + 조건 비교성 판정
  ├─ 입력 누락·단위·RPM/추력/수음점 검증 및 실행 승인
  └─ 허용된 Fluent 도구 호출
       ↓ MCP
Ansys PyFluent-MCP → PyFluent → licensed Fluent
       ↓
고정된 reference case 결과 → Python 후처리/DB → 근거 포함 분석 보고서
```

1. 엔지니어가 한 개의 기존 propeller Fluent case를 기준 사례로 고르고, 형상/mesh/회전 모델/경계조건/수렴 기준과 solver release를 확인한다. GUI에서 사람이 만든 실행 절차를 PyFluent script/journal로 재현 가능하게 만든다.
2. 먼저 MCP가 연결되는지, case를 읽는지, mesh-quality와 setup report가 나오는지, 안전한 고정 파라미터 변경 1개가 반영되는지 작은 smoke test만 한다. 시작부터 CAD 자동 mesh나 free-form natural-language-to-CFD를 약속하지 않는다.
3. LangGraph는 누락 조건을 질문하고, 조건이 맞지 않거나 증거가 약하면 실행/순위화를 보류한다. 실행 가능한 parameter 범위와 tool 목록을 제한하고, solver 실행·저장 전에 사람 승인을 둔다.
4. 후보 비교 조건을 고정한다: 가능한 경우 동일 RPM·유입/전진비·환경·receiver 위치에서 추력/토크와 pressure signal을 같이 기록한다. 소음 단독 최소 대신 필요한 추력/성능 조건을 만족하는 후보 중 비교하도록 한다.
5. DB에는 geometry/case/config hash, Fluent/PyFluent 버전, mesh 품질, solver 모델/시간단계, 수렴 상태, source/receiver 위치, 결과 파일과 SPL/FFT 계산 정의, 승인자를 함께 저장한다. 보고서에는 simulated result와 실제 시험 데이터를 분리 표시한다.

### 대회에서의 강조점과 검증 게이트

차별점은 “LLM이 CFD를 알아서 돌린다”가 아니라 **공식 solver tool을 제한된 계약으로 호출하고, 공학적 비교 가능성·수렴·근거를 통과하지 못하면 결론을 보류하는 evidence-gated agent**다. Ansys의 공식 MCP는 이 설계의 믿을 만한 tool bridge를 제공하지만, agent 판단의 타당성까지 인증해주지는 않는다.

다음 구현 전 팀이 확인할 네 가지는 (1) Fluent 정확한 release, (2) MCP 서버를 띄울 수 있는 Python 3.12+ 환경, (3) 그 환경에서 쓸 수 있는 Fluent 라이선스와 계산 자원, (4) 재사용 가능한 propeller case 및 예상 출력이다. 이 중 case와 라이선스가 확보되지 않으면 CFD 자동실행은 stretch로 낮추고, 기존 결과 파일 검색·조건 판정·보고서 생성을 MVP로 유지하는 게 안전하다.

Official references:

- Ansys PyFluent-MCP repository/tool scope/prerequisites: https://github.com/ansys/pyfluent-mcp
- PyFluent-MCP official documentation: https://fluent-mcp.docs.pyansys.com/
- PyFluent launch/connect from Python: https://fluent.docs.pyansys.com/version/stable/user_guide/session/launching_ansys_fluent.html
- Package release and Alpha classifier: https://pypi.org/project/ansys-fluent-mcp/
- Fluent FW-H aeroacoustics workflow and caveats: https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/flu_ug/flu_ug_sec_use_aeronoise_use.html
- OpenFOAM CLI: https://doc.openfoam.com/2606/fundamentals/command-line/
- OpenFOAM Curle limitation: https://doc.openfoam.com/2312/tools/post-processing/function-objects/field/Curle/
- OpenFOAM noise postprocessing: https://doc.openfoam.com/2312/tools/post-processing/utilities/noise/

> [!note] Bias Check
> 현재 선택은 이미 팀이 Fluent를 사용한다는 새 사실을 반영한 실용적 추천이다. 공식 MCP 존재는 연동 경로의 증거지 예측 정확도, agent 자율성 안전, 결과의 실험실/실기체 타당성 증거가 아니다. package가 Alpha인 점, Fluent 버전/licensing, 회전익 acoustic case의 mesh·시간 해상도와 실측 검증 가능성을 실제 실행 전에 확인한다.

이 답변은 프로젝트 증거와 학부연구생/학술에 활용 가능합니다 — 공식 Fluent 자동화 경로의 범위와 한계를 확인해 대회 MVP의 통합·검증 계획을 현실화하기 때문입니다.
