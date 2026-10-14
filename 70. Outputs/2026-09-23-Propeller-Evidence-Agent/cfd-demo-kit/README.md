---
type: project-output
aliases:
  - CFD Automation Demo Kit
description: "Downloaded public CFD assets, static verification evidence, and a Windows Fluent connection probe."
author:
  - Codex
date created: 2026-10-01
date modified: 2026-10-01
tags:
  - cfd
  - project
verificationStatus: partial
---

# CFD 자동화 데모 준비 및 검증

## 확정한 개발 범위

- Windows / Fluent Student 2026 R1, 한 PC에서 실행.
- 전문가 검토 템플릿 하나와 고정 형상·메시. 최초 가변 입력은 RPM 하나.
- 추력·토크 우선. 소음·형상 변경·CAD 자동 메시 생성은 후속 범위.
- LLM은 요구사항 정리, 템플릿 안에서 계획 및 후속 운전조건 제안, 결과 설명.
- Python은 설정 적용, 실제값 재조회, 단위 변환, 비교, 계산, 결과 추출.
- LangGraph는 승인·수정·계산 상태·결과 분기. MCP는 준비한 Python 도구의 호출 연결부.
- 계획 승인 → 설정 적용 → 실제값 검증 → 계산 승인. 설정 변경 시 재검증.

## 실제 확보 결과

다운로드 URL·파일 크기·SHA-256·압축 내 파일 목록은 `manifest.json`에 기록했다. 정적 검사 결과는 `inspection.json`에 있다. 원본 파일은 `assets/`에 그대로 보존했다. 공개 다운로드와 재배포 허용은 다르므로 공개 GitHub에 원본 묶음을 올리기 전 각 출처 이용조건을 확인한다. 이 키트는 원본을 Git 추적에서 제외한다.

| 자료 | 실제 확보·검사 | 사용 결정 |
|---|---|---|
| Ansys 공식 axial_fan.cas.h5 / axial_fan.msh.h5 | HDF5 읽기 성공. 버전 26.1. 셀 56,963개. 회전영역 rotating-fan | 우선 연결·RPM·힘/모멘트 추출 시험용 |
| APC 형상 PE0 전체 자료 | 압축 해제 성공. 10x7E-PERF.PE0 포함 | 항공 프로펠러 형상 근거 및 케이스 제작 대안 |
| APC 성능 PERFILES 자료 | 압축 해제 성공. PER3_10x7E.dat 포함 | 계산 기반 참고자료. 실측값으로 표현하지 않음 |
| skfelix/propeller-OpenFOAM | 원본 저장소 ZIP·STL·해석 설정·튜토리얼 확보 | 메시 생성 작업 필요, 즉시 실행 후보 제외 |
| NASA X-57.glb / X-57.vsp3 | GLB 헤더/크기 정상. VSP XML 파싱 성공, Propeller 항목 7개 | 발표·형상 연구 참고. 최초 계산 입력 제외 |
| rtuhpc/HPC-example-ANSYS | 원본 저장소 확보 | README에 언급된 FFF.cas.h5가 실제 저장소에 없음. 실행 후보 제외 |

**주의: 확보된 Fluent 케이스는 덕트 내부 축류팬이며 항공기 단독 프로펠러가 아니다.** 기술 연결 검증에는 적합하지만 프로펠러 최종 시연이라고 표시하지 않는다. 축방향 힘 역시 실제 항공 프로펠러 추력 검증과 구분한다.

공식 팬 케이스의 정적 확인: 회전축 Y, 원점 (0,0,0), 회전영역 rotating-fan, 회전속도 표현식 rotational_speed 연결. 팬 표면 fan-walls 및 fan-tip-wall 존재. 케이스 내 출구압 표현식은 200 Pa이며, 문서 초기 예시의 0 Pa와 다르다. 기준 조건을 그대로 기록하고 전문가 검토 없이 값을 통일하지 않는다.

OpenFOAM 예제: rhoSimpleFoam, MRF, 회전축 Y, 314.16 rad/s(주석상 3000 RPM). simulationTemplate에 완성 polyMesh가 없다. prop.stl은 43,538 삼각형이며 trimesh 기준 watertight=false. 형상 보수·단위·메시 품질 확인이 필요하다. 이 STL과 APC 형상이 동일하다고 가정하지 않는다.

## 검증의 현재 경계

이 Mac의 PATH에서 Fluent·OpenFOAM 솔버가 발견되지 않았다. Windows PC 접속 정보도 없으므로 실제 계산·Student 라이선스 동작·수렴·추력/토크 정확성은 검증하지 못했다. HDF5 파일을 읽었다는 사실이 Fluent에서 계산된다는 뜻은 아니다.

완료: 실제 다운로드, Git LFS 포인터가 아닌 바이너리 확인, 압축 해제, HDF5 구조/셀 수/버전/영역 확인, STL 검사, GLB/VSP 형식 검사, Windows 프로브 문법·인자 검사.

미완료: Fluent GUI에서 기준 계산, PyFluent 연결·RPM 쓰기/재조회, 힘·모멘트 추출, 수렴 기준 합의, MCP/LangGraph 종단 연결. `windows_fluent_probe.py`는 실행 준비용이며 Fluent에서 검증된 코드라고 주장하지 않는다.

## Windows에서 1~3단계 검증

1. 이 폴더를 Windows의 짧은 경로(예: C:\cfd-demo-kit)로 복사한다.
2. Fluent Student 2026 R1을 3D·배정밀도·CPU 2개로 새 세션에서 시작한다. 기존 작업 세션을 사용하지 않는다.
3. `assets/ansys-axial-fan/axial_fan.cas.h5`를 연다. mesh check와 기준 설정을 확인한다.
4. 사람이 초기화·계산하고 잔차 및 힘/토크 안정성을 확인한다. 시간·반복수·표면·축·결과를 기록한다. 이는 기술 시험용 팬이다.
5. GUI의 File → Applications → Server → Start 또는 TUI의 `server/start-server`로 서버를 시작한다. 생성된 server-info 파일을 로컬에서 사용하고 공유/커밋하지 않는다.
6. Python 가상환경에 `ansys-fluent-core`를 설치하고 설치 버전을 기록한다.

PowerShell 예시:

```powershell
cd C:\cfd-demo-kit
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install ansys-fluent-core
.\.venv\Scripts\python.exe -m pip freeze
.\.venv\Scripts\python.exe windows_fluent_probe.py --server-info C:\cfd-session\server.txt
.\.venv\Scripts\python.exe windows_fluent_probe.py --server-info C:\cfd-session\server.txt --rpm 1500
.\.venv\Scripts\python.exe windows_fluent_probe.py --server-info C:\cfd-session\server.txt --rpm 1500 --run --iterations 20
```

프로브는 매번 기준 케이스를 다시 로드한다. RPM 1500은 연결 시험값이며 전문가가 검증한 운전범위가 아니다. 20회 계산은 API 동작 시험으로, 수렴했다고 판단하지 않는다. 실행 시 하이브리드 초기화로 현재 세션의 해를 초기화한다. 원본 케이스 파일은 덮어쓰지 않고 결과는 `runs/<timestamp>/`에 저장한다.

프로브 결과 확인:

- read_case 및 mesh.check 성공 여부.
- RPM을 rad/s로 변환한 승인값과 Fluent 재조회값 일치.
- 실제 MRF 활성화·Y축 확인.
- 생성된 force/moment 보고 정의와 실제 GUI 표시가 일치하는지 확인.
- 팬 표면 선택(팁 포함), 원점 및 부호를 전문가가 검토.
- GUI에서 같은 정의로 계산한 N·N m 값과 Python 결과가 일치하는지 확인.

프로브 실패 시 `runs/.../probe.json`의 오류로 분류한다. 오류를 LLM이 임의 코드로 우회하지 않는다.

## 분기 규칙의 모호한 부분 해소

| 상태 | 행동 | 추가 정의 |
|---|---|---|
| 발산 | 즉시 중단·해석 검토 | NaN/Inf, Fluent 오류, 모니터 비정상 증가 판단 기준 |
| 미수렴 | 예산 내 추가 반복 또는 해석 검토 | 잔차 + 추력/토크 안정성, 최대 반복수·시간 |
| 지표 누락 | 보고 정의 추가 | 기존 해에서 재추출 가능한 경우 재계산하지 않음 |
| 유효한 계산·미달 | 허용 RPM 범위에서 새 조건 제안 | 추력 하한, 토크 상한, 부호 정의, 허용 RPM |
| 충족 | 사람 최종 검토 | 수치적 유효성 판단을 먼저 통과해야 함 |
| 불가 | 탐색 종료 및 이유 보고 | 승인된 시험 범위/예산 내 미충족이며 전역적 불가능을 뜻하지 않음 |

초기 운전조건 변경은 RPM만. 발산·미수렴 시 자동으로 난류모델/메시/경계조건을 바꾸지 않는다. 전문가 템플릿의 복구 절차와 허용된 반복수·완화계수 변경 범위를 따로 정한다. 반복 재계산에는 횟수·시간 한도를 둔다.

MCP 권장 도구: load_template, apply_rpm, verify_settings, start_run, get_run_status, collect_results. start_run은 job_id를 즉시 반환하고 장시간 계산은 별도 worker에서 진행한다. 중복 호출은 같은 job_id를 조회하고 동일 계산을 다시 시작하지 않는다. LangGraph 재개가 Fluent 프로세스 복원을 보장하지 않으므로 세션/케이스/계획버전/작업상태를 별도 보존한다.

## 사용자에게 요청할 자료

기술 연결 시험용 케이스는 확보했으므로 새 파일을 기다리지 않고 Windows에서 시험할 수 있다. 항공 프로펠러 최종 시연에는 연구실에 다음을 요청한다.

> Fluent Student 2026 R1에서 실제 계산 가능한 단독 공기 프로펠러 정상상태 MRF `.cas.h5`와 가능하면 `.dat.h5`, 기본 RPM·유입조건·회전축·프로펠러 벽면 이름·기준 추력/토크·수렴 기록. Student 셀/노드 제한 이하이며, 재사용/발표 가능한 파일이면 좋겠습니다. CATIA 원본은 필수 아님.

전문가에게 추가로 합의할 것: 허용 RPM 범위, 추력/토크 부호 및 보고 표면, 수렴 판단, 복구 절차, 최대 재시도. 요구값은 케이스 확보 후 가상 데모 요구사항으로 명시하고 정한다.

## 출처

- [Ansys 공식 축류팬 자동화 예제](https://fluent.docs.pyansys.com/version/dev/examples/00-fluent/axial_fan_performance_curve_workflow.html)
- [Ansys 공식 예제 데이터](https://github.com/ansys/example-data/tree/main/pyfluent/axial_fan_performance_curve)
- [APC 제조사 다운로드](https://www.apcprop.com/technical-information/file-downloads/)
- [APC2BEM](https://github.com/jamesjhu/APC2BEM)
- [OpenFOAM 프로펠러 예제](https://github.com/skfelix/propeller-OpenFOAM)
- [NASA X-57 원본 모델](https://github.com/nasa/NASA-3D-Resources/tree/master/3D%20Models/X-57)
- [실제 케이스 부재를 확인한 HPC 예제](https://github.com/rtuhpc/HPC-example-ANSYS)
- [PyFluent 연결 공식 문서](https://fluent.docs.pyansys.com/version/stable/user_guide/session/launching_ansys_fluent.html)
