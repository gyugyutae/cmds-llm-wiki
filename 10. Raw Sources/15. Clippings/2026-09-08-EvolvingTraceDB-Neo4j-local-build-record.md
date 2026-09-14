---
type: raw-source
aliases:
  - EvolvingTraceDB Neo4j local build record
description: "User-verified screenshots and commands from the local EvolvingTraceDB Neo4j graph build."
author:
  - "[[김규태]]"
date created: 2026-09-08
date modified: 2026-09-08
date ingested: 2026-09-08
tags:
  - raw-source
  - neo4j
  - javaparser
  - traceability
source: "User-provided local Neo4j Browser screenshots and terminal execution"
source-attachment:
  - "[[2026-09-08-EvolvingTraceDB-TESTS-overview.jpeg]]"
  - "[[2026-09-08-EvolvingTraceDB-RequestTest-links.jpeg]]"
  - "[[2026-09-08-EvolvingTraceDB-node-counts.jpeg]]"
  - "[[2026-09-08-EvolvingTraceDB-Neo4j-relationship-visualization.png]]"
source-format: image
conversion-tool: Codex visual inspection and user-provided Cypher
conversion-date: 2026-09-08
conversion-fidelity: high
category: Clippings
status: ingested
collectionPurpose: "학부연구생/학술·프로젝트 증거 — EvolvingTraceDB의 JavaParser 테스트-소스 추적 링크를 Neo4j에 적재하고 재현한 과정과 결과를 논문·랩미팅·포트폴리오 증거로 재사용하기 위함."
mainVaultRelated: []
mainVaultCmds: ""
---

# EvolvingTraceDB Neo4j Local Build Record

## Original Content

### TEST FILE → SOURCE FILE 전체 결과

```cypher
MATCH p=(t:TEST_FILE)-[:TESTS]->(s:SOURCE_FILE)
RETURN p
LIMIT 100;
```

![[2026-09-08-EvolvingTraceDB-TESTS-overview.jpeg]]

### RequestTest.java 연결 결과

```cypher
MATCH p=(t:TEST_FILE)-[:TESTS]->(s:SOURCE_FILE)
WHERE t.file_name = 'RequestTest.java'
RETURN p;
```

![[2026-09-08-EvolvingTraceDB-RequestTest-links.jpeg]]

### 라벨별 노드 개수

```cypher
MATCH (n)
UNWIND labels(n) AS label
RETURN label, count(*) AS count
ORDER BY count DESC;
```

![[2026-09-08-EvolvingTraceDB-node-counts.jpeg]]

### 모든 관계 유형 시각화

```cypher
MATCH p=(a)-[r]->(b)
RETURN p
LIMIT 100;
```

![[2026-09-08-EvolvingTraceDB-Neo4j-relationship-visualization.png]]

### 적재 결과

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

JavaParser 결과 694개 중 693개가 Neo4j에 연결됐다. `MultisearchBody.java` 1개는 `CODE` 목록에 대응하는 경로가 없어 스킵됐다.
