---
type: query-result
aliases:
  - UNLV 연수 네트워킹과 Evidence Wiki 기술 후보
description: "Evidence-bounded advice on US developer networking, an evaluation loop for the Evidence Wiki, and complementary AI engineering tools."
author:
  - Codex
date created: 2026-10-12
date modified: 2026-10-12
tags:
  - career
  - llm-wiki
  - ai-evaluation
source:
  - "[[Core Context]]"
  - "[[LLM Wiki Pattern]]"
  - "[[RAG vs Compiled Wiki]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[3-Layer Architecture]]"
reusableFor:
  - 개발자 취업
  - 연수 준비
  - AI 출력 검증
  - 프로젝트 증거
confidence: medium
claimType: mixed
evidenceScope: local-vault-and-current-primary-documentation
verificationStatus: partial
explored: false
mainVaultRelated: []
---

# UNLV 연수 네트워킹과 Evidence Wiki 기술 후보

사용자 요청: 얻어올 다섯 가지를 별도 기록하고 실력 대비 네트워킹의 중요성, Evidence Wiki의 역할과 기술 후보를 설명한다.

사용자 견해: 실력과 역량이 우선이라고 생각한다. 아래 우선순위·수량은 Codex의 제안이며 사용자의 확정된 의견이나 완료 실적이 아니다.

실행 메모: [[2026-10-12-UNLV-연수에서-얻어올-다섯가지]].

## 네트워킹과 실력

실력은 업무 수행과 기술면접의 기반이다. 네트워킹은 새로운 채용 정보·직무 맥락·피드백·소개를 얻는 경로다. 소개받은 뒤 역량을 평가받는 과정과 소개받을 기회를 만드는 과정은 구분해야 한다. 회사마다 리퍼럴 처리와 선발 절차는 다르며 리퍼럴이 서류 통과·면접·합격을 보장한다고 주장하지 않는다.

2022년 Science에 발표된 LinkedIn 실험은 약 2천만 명을 대상으로 연결 추천을 달리했을 때 비교적 약한 관계가 일자리 이동에 도움을 준다는 결과를 보고했다. 디지털 산업에서 효과가 더 두드러졌으며 가장 약한 관계가 항상 최고라는 선형 관계는 아니다. 이는 2015~2019년 LinkedIn 실험이고 현재 미국 신입 개발자의 합격률·비자 조건·역량 대비 중요도 비율을 제공하는 연구가 아니다.

- [연구 논문](https://www.science.org/doi/10.1126/science.abl4476)
- [MIT 연구 소개](https://news.mit.edu/2022/weak-ties-linkedin-employment-0915)
- [Amazon SDE 평가 안내](https://amazon.jobs/content/en/how-we-hire/university/sde-oa): 코딩·기술적 문제 해결 평가를 명시한다. 모든 회사의 전형을 대표하지 않는다.

권장 행동: 코드·시연·질문을 가지고 면담 → 구체적 의견 기록 → 수정 결과 공유. 연락처 수보다 내 작업을 실제로 아는 관계를 만든다. 네트워킹만으로 미국 취업의 별도 채용·취업자격 요건이 해결된다고 기대하지 않는다.

## Evidence Wiki의 역할

이 저장소에서 Evidence Wiki는 원본 근거·주장·본인 역할·검증 상태를 연결하는 운영 방식이다. 새 모델을 학습시키거나 파일을 저장하는 것만으로 AI를 자동 검증하는 기술은 아니다.

- `10. Raw Sources`: 공고·논문·원문·실험 로그 등 근거. explicit ingest/source-update에서 Original Content 보존.
- `20. Wiki`: 근거에서 정리한 개념과 판단. partial/unverified를 확정 사실로 승격하지 않는다.
- `30. Queries`: 질문에 대한 재사용 가능한 합성 답변.
- Schema: AGENTS·skills·commands가 편집과 검증 절차를 정한다.
- 실행용 평가 데이터·스크립트는 프로젝트 저장소에 두고 Wiki에서 커밋·실행 결과로 연결한다.

`explored`는 사용자 탐색 확인, `verificationStatus`는 주장과 근거의 검증 상태다. Wiki 작성·에이전트 점검만으로 사용자가 이해했거나 실험이 통과했다고 판단하지 않는다. 일반 대화는 별도 저장 없이 자동으로 Wiki에 들어가지 않는다. 이번 실행 메모는 70. Outputs, 합성 답변은 30. Queries에 명시적으로 저장했다.

## AI 출력 검증 기준과 실패 사례

UNLV 공고 질의를 예로 한 소규모 평가 제안이다. 아직 평가 도구를 설치하거나 실험을 실행하지 않았다.

| 입력 | 기대 기준 | 실패 분류 |
|---|---|---|
| 학교 지원금은 얼마인가? | 요약표의 약 883만원을 출처와 함께 제시 | 자비 594만원과 뒤바꿈 |
| 기업 인턴십이 포함되는가? | 공고에서 확인되지 않는다고 답함 | 존재하지 않는 인턴십 확약 |
| 개인부담액 원화와 달러가 다르다 | 불일치와 확인 필요를 표시 | 숫자를 임의 수정하거나 충돌 숨김 |
| 원문에 없는 수업 내용 질문 | 확인 불가와 확인 경로 제시 | 세부 커리큘럼 날조 |
| 출처가 주장을 뒷받침하는가? | 접근 여부와 내용 타당성을 별도 검사 | HTTP 200만으로 내용 정확성 판정 |

금액 근거: [공고 PDF](https://www.gnu.ac.kr/common/nttFileDownload.do?fileKey=1f635390816034855e19db199b315e99). 이 표는 기대 기준이지 실행 결과가 아니다.

운영 순서:

1. 사람이 원문을 대조해 입력·정답 사실·허용 답변·금지 주장을 만든다.
2. 정상·충돌·근거 부족·오래된 정보 등 20개 사례를 만든다. 20개는 시작용 제안이다.
3. 숫자·필수 필드·출처 ID 존재·JSON 스키마는 코드로 검사한다. 문장 의미와 인용의 타당성은 사람 또는 보조 LLM 평가를 쓴다.
4. 원문 snapshot/hash·데이터셋 버전·프롬프트·모델 ID와 설정·코드 커밋·검색 설정과 결과·원본 출력·채점 결과를 저장한다.
5. 같은 사례를 변경 전후 각각 3회 실행하는 소규모 비교를 제안한다. 반복 수는 예산과 변동성에 따라 조정한다.
6. 사실·인용·보류·파싱·API 오류와 비용·지연을 분리해 보고한다. 실행 실패를 분모에서 숨기지 않는다.
7. 수정에 사용하지 않은 별도 사례로 확인하고 실패 사례를 회귀 평가에 편입한다.

원격 모델은 같은 설정으로도 출력이 달라질 수 있다. 재현 가능성은 실험 조건과 판정 절차를 다시 실행할 수 있다는 뜻이며 문장이 매번 같다는 보장이 아니다. LLM 채점은 사람 검토로 보정하며 최종 진실 판정기로 삼지 않는다.

## 기술 후보와 선택 기준

2026-10-12 공식 문서를 확인했다. 모두 이번에 처음 등장한 신기술이라는 뜻은 아니다. 기능은 공식 설명이고 이 프로젝트에서의 유용성·학습 순서는 제안이다.

| 후보 | 역할 | 작은 실험 | 경계 |
|---|---|---|---|
| Promptfoo | 테스트 사례로 프롬프트·모델 출력 비교 | 공고 20문항 평가 | 도구가 정답을 자동 확정하지 않음 |
| Ragas | 검색 문맥과 답변의 일치 등 RAG 평가 | 주장별 근거 충실도 확인 | 문맥이 틀리면 충실해도 사실은 틀릴 수 있음 |
| Langfuse | 호출·검색·도구 trace와 평가 연결 | 오류의 검색·생성 단계 구분 | 관측만으로 품질이 개선되지는 않음 |
| Spring AI + Structured Output | Java 앱에서 모델 출력의 타입·스키마 처리 | answer, sourceIds, status를 반환하는 API | 형식 검증과 사실·업무 규칙 검증은 별개 |
| MCP | AI와 데이터·도구의 표준 인터페이스 | 읽기 전용 근거 검색 도구 | 연결·응답이 판단의 정당성을 보장하지 않음 |
| LangGraph | 상태·체크포인트·분기·사람 입력 관리 | 검색→검증→보류/재검색→검토 | 중복 실행·외부 효과는 별도 설계·시험 |

- [Promptfoo assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/)
- [Ragas faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)
- [Langfuse evaluation](https://langfuse.com/docs/evaluation/overview)
- [Spring AI structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html)
- [MCP introduction](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)
- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

권장 시작: 기존 Wiki + 작은 평가 데이터셋 + Promptfoo 하나. Java API가 준비되면 Spring AI로 연결하고 추적할 호출이 늘면 Langfuse를 검토한다. 외부 도구 또는 복잡한 상태 전이가 필요해진 뒤 MCP·LangGraph를 추가한다.

프로젝트 후보:

1. **UNLV 공고 근거 답변 평가**: 숫자·충돌·보류를 확인하기 쉬운 첫 실험.
2. **Java 원장 프로젝트 장애 설명 보조**: 로그·테스트를 인용해 설명. 거래 판단·수정 실행은 기존 코드와 사람이 담당.
3. **CUEE 사용성 피드백 정리 보조**: 익명화한 의견에서 가설·관찰·해석을 분리. 요약 누락·왜곡을 평가하며 실제 고령자 검증을 대체하지 않음.

> [!note] Bias Check
> 네트워킹 연구는 현재 미국 개발자 취업의 정확한 효과 크기를 제공하지 않는다. 공식 문서는 기능 설명이며 사용자 프로젝트의 개선 효과는 아직 측정하지 않았다. 기존 Wiki의 partial 상태와 사용자 이해 경계를 유지한다. 이 답변은 실행 계획이며 설치·평가 완료 보고가 아니다.

## Wiki 피드백과 품질 공백

- [[LLM Wiki Pattern]]에 증거 기록과 실행 평가의 연결을 추가한다.
- 읽은 관련 개념 페이지는 explored: false와 Bias Check를 갖고 있다. 사용자 이해를 대신 확정하지 않는다.
- standalone이므로 mainVaultRelated는 비워 둔다. 연결 누락으로 처리하지 않는다.
- 실행 평가 데이터셋과 실제 결과는 아직 없다. 본 문서로 그 공백이 해소됐다고 주장하지 않는다.

이 답변은 취업/포트폴리오·프로젝트 증거·AI 활용 검증에 활용 가능합니다 — 연수 목표를 결과물로 바꾸고 AI 출력의 개선을 같은 조건으로 비교하는 기준을 제공합니다.
