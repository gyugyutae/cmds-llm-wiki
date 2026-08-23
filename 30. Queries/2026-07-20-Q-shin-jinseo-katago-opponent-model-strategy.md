---
type: query-result
aliases:
  - 신진서 카타고 상대 모델 전략
  - Shin Jinseo KataGo Opponent Modeling Strategy
description: "Assesses whether KataGo likely knew it faced Shin Jinseo and whether deliberately inviting human mistakes would have improved its win probability in the July 2026 handicap match."
author:
  - Codex
date created: 2026-07-20
date modified: 2026-07-20
tags:
  - query-result
  - go
  - katago
  - ai-strategy
  - opponent-modeling
  - decision-theory
source:
  - "https://www.hankyung.com/article/2026071710097"
  - "https://www.hankyung.com/article/202607171174i"
  - "https://news.ikbc.co.kr/article/view/kbc202607190030"
  - "https://github.com/lightvector/KataGo"
  - "https://github.com/lightvector/KataGo/blob/master/docs/Analysis_Engine.md"
reusableFor:
  - 독서/책/학습
  - 에세이/블로그
  - AI 전략
confidence: medium
status: active
verificationStatus: partial
claimType: interpretive
evidenceScope: public-reporting-and-official-documentation
---

# 신진서 vs KataGo: 상대 인식과 인간 오류 유도 전략

## 결론

공개된 자료만으로는 이 대국의 KataGo가 **신진서라는 개인을 인식하도록 설정됐는지** 확인할 수 없다. 다만 기본 KataGo/GTP 구조와 공식 문서를 보면, 별도 설정이 없는 한 엔진은 기보의 현재 판·착수 순서·규칙·덤 정보로 다음 수를 계산할 뿐, 상대의 이름이나 심리 상태를 입력받지 않는다. 따라서 `신진서라서 실수를 유도하는 수를 두었다`고 단정할 근거는 없다.

질문의 핵심 직감은 맞다. 상대의 실수 확률을 신뢰성 있게 예측할 수 있다면, 즉시 약간 손해를 보더라도 복잡한 교전을 만들어 기대승률을 높이는 전략은 가능하다. 그러나 그것은 `블루스팟보다 나쁜 수`를 고르는 문제가 아니라, **상대 모델을 포함한 다른 목적함수에서 더 좋은 수**를 고르는 문제다. 그 상대 모델과 목적함수가 실제 대국에서 켜졌는지는 공개되지 않았다.

## 확인된 사실

- 1국은 신진서가 두 점 접바둑의 큰 우세로 출발했지만 KataGo가 복잡한 전투에서 격차를 줄였고, 이후 신진서의 강한 공격이 성공하지 않으면서 KataGo가 이겼다고 보도됐다. 해설은 KataGo가 한 번의 큰 승부수가 아니라, 손해가 가장 적은 수를 누적해 격차를 지웠다고 평가했다.
- 2국에서는 신진서가 290수 끝에 4집 반 승리해 최종 1승 1패가 됐다. 즉 같은 두 점 접바둑 조건에서도 인간이 이길 여지는 실제로 있었다.
- KataGo는 GUI가 아닌 GTP 엔진이며, 모델과 설정 파일을 지정해 동작한다. 표준 GTP의 `genmove` 요청은 둘 색을 알려 주는 방식이지, 상대 선수의 이름을 전달하는 방식이 아니다.
- KataGo 공식 문서에는 `human SL model`과 `humanSLProfile`이 있다. 이는 특정 급수대 인간이 둘 법한 수를 예측하는 **선택적·일반적 인간 모델**이며, 공식 예시는 5급 같은 실력 프로필이다. 신진서 개인을 식별하거나 그 사람의 습관을 학습하는 기능이라는 설명은 없다.

## 무엇을 뜻하는가

### 1. 카타고는 상대가 인간인 것을 알았나?

세 층을 나누어 봐야 한다.

| 층 | 의미 | 이번 대국에서 확인된가 |
|---|---|---|
| 판 인식 | 두 점 접바둑의 돌 배치, 덤, 현재 국면을 안다 | 예. 판 자체에 들어 있다 |
| 일반 인간 모델 | 특정 실력대 인간의 다음 수 분포를 활용한다 | 기능은 존재하나 사용 여부 미공개 |
| 신진서 개인 모델 | 이름·기보·습관을 바탕으로 신진서의 실수를 겨냥한다 | 공개 근거 없음 |

그래서 가장 안전한 답은 **두 점 접바둑이라는 비대칭 국면은 보았지만, 신진서라는 개인을 알고 심리전을 했다고 볼 근거는 없다**이다. 대국 설정 파일, 사용 모델, human 모델 유무, 목표 함수가 공개돼야 더 강하게 말할 수 있다.

### 2. 블루스팟만 둔 것이 인간 상대 전략과 모순되나?

꼭 그렇지는 않다. 화면의 블루스팟은 대개 해당 분석 엔진의 방문 수·목적함수·설정 아래에서 좋은 후보라는 뜻이다. 이것은 보통의 의미에서 `절대적이고 유일한 최선수`라는 뜻은 아니다. 승률, 집 차이, 덤, 핸디캡, 시간, 상대 실력 모델을 다르게 두면 후보 순서도 바뀔 수 있다.

또한 "복잡하게 만들어 상대 실수를 기다리기"가 실제로 유리하려면 아래가 성립해야 한다.

```text
유도전의 기대가치
= 즉시 감수한 손해
+ (상대가 유도된 실수를 할 확률 × 회수 가능한 이득)
- (내 전술 리스크 × 내 손해)
```

이 값이 안전한 블루스팟의 기대가치보다 커야 한다. 신진서처럼 최상위 인간을 상대로는 실수 확률을 과대평가하면 오히려 불리해질 수 있다. 특히 두 점을 깔고 출발한 KataGo는 열세를 줄일 필요가 있었으므로, 정교한 전투 수가 결과적으로 인간에게 어려운 선택지를 주더라도 그것이 곧 "실수 유도용 희생수"였다고 해석할 수는 없다.

### 3. 실제 1국은 어떻게 읽는 편이 타당한가?

보도에 따르면 신진서는 초반에 실리 위주로 두다가, KataGo가 격차를 줄인 뒤 중앙 백 대마를 공격하는 강한 전투를 선택했다. 이는 "신진서가 처음부터 계속 전투를 피했고 KataGo가 끝까지 블루스팟만 두었다"보다 다음에 가깝다.

> KataGo가 낯선 포석과 정교한 수순으로 국면을 바꾸며 열세를 줄였고, 신진서는 그 변화 속에서 자기 스타일 밖의 전투를 선택했다.

이것은 상대방의 심리를 읽은 함정이라고 증명되지는 않는다. 다만 판 위에서 가장 적은 손해로 버티고 추격하는 수들이 인간에게는 어려운 선택을 계속 만들 수 있다는 사례다.

## 더 정확한 검증에 필요한 것

- 주최 측의 KataGo 버전, 네트워크 파일, GTP 설정 파일
- human SL model / `humanSLProfile` 사용 여부
- 분석 화면의 블루스팟이 어떤 엔진·방문 수·승률 또는 집 차이 기준인지
- 두 대국의 SGF와 수순별 KataGo 평가값

이 정보가 있으면 각 후보수에 대해 `순수 최선수`, `점수 추격수`, `상대 실수 유도 가능성이 있는 수`를 분리해 다시 분석할 수 있다. 현재 공개 자료로는 마지막 항목을 검증할 수 없다.

## Sources

- 한국경제, 1국 보도: https://www.hankyung.com/article/2026071710097
- 한국경제, 1국 해설 칼럼: https://www.hankyung.com/article/202607171174i
- KBC 광주방송, 2국 결과: https://news.ikbc.co.kr/article/view/kbc202607190030
- KataGo 공식 README: https://github.com/lightvector/KataGo
- KataGo 공식 Analysis Engine 문서: https://github.com/lightvector/KataGo/blob/master/docs/Analysis_Engine.md

## Quality Gaps

- 이 질의는 공개 기사와 KataGo 공식 문서를 기반으로 한 해석이다. 실제 대국 운영 설정은 공개 자료에서 확인하지 못했다.
- 대국 SGF와 수순별 분석 로그가 없으므로 특정 수를 "심리전용 희생수"라고 판정할 수 없다.

이 답변은 독서/책/학습, 에세이/블로그, AI 전략에 활용 가능합니다 — AI의 최선수, 상대 모델, 목적함수를 구분해 인간-AI 대국과 의사결정 시스템을 해석하는 틀을 제공하기 때문입니다.
