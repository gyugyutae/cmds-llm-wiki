---
type: wiki-page
aliases:
  - EvolvingTraceDB Neo4j Setup Guide
description: "Reproducible setup, loading, and verification guide for the EvolvingTraceDB Neo4j graph."
author:
  - Codex
date created: 2026-09-08
date modified: 2026-09-08
tags:
  - llm-wiki
  - neo4j
  - javaparser
  - traceability
source:
  - "[[2026-09-08-EvolvingTraceDB-Neo4j-local-build-record]]"
related:
  - "[[Graduation-elasticsearch]]"
  - "[[MOC-Portfolio]]"
explored: false
claimType: mixed
evidenceScope: user-original
verificationStatus: partial
---

# EvolvingTraceDB Neo4j 구축 및 검증 가이드

## 그래프 스키마

```text
(ISSUE)-[:MODIFIES]->(CODE)
(API_DOCUMENT)-[:EXPLAINS]->(CODE)
(TEST_FILE:CODE)-[:TESTS]->(SOURCE_FILE:CODE)
```

`TEST_FILE`과 `SOURCE_FILE`은 기존 `CODE` 노드에 추가로 붙은 라벨이다.

## 1. Python 환경 구축

WSL/Linux:

```bash
cd /mnt/c/Users/user/Desktop/EvolvingTraceDB
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install neo4j python-dotenv requests
```

Windows PowerShell:

```powershell
cd C:\Users\user\Desktop\EvolvingTraceDB
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install neo4j python-dotenv requests
```

## 2. Neo4j Docker 실행

Docker Desktop을 켠 뒤 실행한다.

```bash
docker run --name evolving-neo4j \
  -p 7474:7474 \
  -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/evolving123 \
  -d neo4j:5
```

```text
Neo4j Browser: http://localhost:7474
Connection URL: localhost:7687
User: neo4j
Password: evolving123
```

`.env`:

```dotenv
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=evolving123
```

## 3. JavaParser 빌드 및 실행

Maven 없이 PowerShell runner를 사용하는 방법:

```powershell
cd parser
powershell -ExecutionPolicy Bypass -File .\run_parser.ps1
cd ..
```

Maven을 사용하는 방법:

```bash
cd parser
mvn clean package
java -jar target/trace-link-extractor-0.1.0.jar \
  --project-root ../14.elasticsearch-java_result/project \
  --output-dir ../14.elasticsearch-java_result/parser_output
cd ..
```

핵심 결과는 `source_test_generated.csv`이고, 각 링크의 메서드 호출 근거는 `method_call_edges.csv`에 남는다.

## 4. Neo4j 노드와 관계 적재

```bash
python scripts/init_neo4j/create_nodes.py --proj-id 14 --proj-name elasticsearch-java
python scripts/init_neo4j/link_issue_code.py --proj-id 14 --proj-name elasticsearch-java
python scripts/init_neo4j/link_api_code.py --proj-id 14 --proj-name elasticsearch-java
python scripts/init_neo4j/link_test_source.py --proj-id 14 --proj-name elasticsearch-java
```

스크립트는 `MERGE`를 사용하므로 재실행해도 중복 관계가 만들어지지 않는다.

## 5. Neo4j Browser 검증

### 테스트-소스 관계

```cypher
MATCH p=(t:TEST_FILE)-[:TESTS]->(s:SOURCE_FILE)
RETURN p
LIMIT 100;
```

![[2026-09-08-EvolvingTraceDB-TESTS-overview.jpeg]]

### RequestTest.java 연결

```cypher
MATCH p=(t:TEST_FILE)-[:TESTS]->(s:SOURCE_FILE)
WHERE t.file_name = 'RequestTest.java'
RETURN p;
```

![[2026-09-08-EvolvingTraceDB-RequestTest-links.jpeg]]

### 노드 개수

```cypher
MATCH (n)
UNWIND labels(n) AS label
RETURN label, count(*) AS count
ORDER BY count DESC;
```

![[2026-09-08-EvolvingTraceDB-node-counts.jpeg]]

### 모든 관계 유형

```cypher
MATCH p=(a)-[r]->(b)
RETURN p
LIMIT 100;
```

![[2026-09-08-EvolvingTraceDB-Neo4j-relationship-visualization.png]]

## 6. 검증 결과

| 항목 | 개수 |
|---|---:|
| `CODE` | 4,215 |
| `ISSUE` | 547 |
| `API_DOCUMENT` | 97 |
| `TEST_FILE` | 92 |
| `SOURCE_FILE` | 245 |
| `MODIFIES` | 52 |
| `EXPLAINS` | 34 |
| `TESTS` | 693 |

## 7. 재실행

```bash
docker start evolving-neo4j
docker stop evolving-neo4j
docker logs evolving-neo4j
```

> [!warning] 현재 데이터 한계
> JavaParser 파서의 현재 분류 규칙은 경로에 `test`가 포함되는지 확인한다. 따라서 `src/main/java`의 `TestPopulation.java`, `TTestAggregate.java` 등이 테스트로 오분류될 수 있다. 현재 693개 `TESTS` 관계는 MVP 파이프라인 검증 결과로 해석한다.

> [!note] Bias Check
> Counter-argument: 시각적으로 관계가 생성됐다는 사실은 추적 링크의 정확도를 보장하지 않는다.
> Data gap: 링크 표본의 수동 검증, precision/recall 측정, 분류 규칙 개선 후 재실행이 필요하다.

## Related

- [[Graduation-elasticsearch]]
- [[2026-09-08-EvolvingTraceDB-Neo4j-local-build-record]]
- [[MOC-Portfolio]]
