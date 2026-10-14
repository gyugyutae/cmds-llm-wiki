---
type: query-result
aliases:
  - 금융 계좌이체 프로젝트 트랜잭션·아키텍처 학습 경로
description: "A staged reading and experiment plan for learning transactions, concurrency, and backend architecture through the financial ledger project."
author:
  - Codex
date created: 2026-09-28
date modified: 2026-09-28
tags:
  - query-result
  - financial-backend
  - database
  - transactions
  - software-architecture
source:
  - "[[financial-lab]]"
  - "[[2026-09-13-Q-java-bank-transfer-ledger-portfolio-design]]"
  - https://www.hanbit.co.kr/books/B6873873587?code=B6873873587
  - https://www.hanbit.co.kr/books/B7449193745?code=B7449193745
  - https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/
  - https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-model.html
  - https://dev.mysql.com/doc/refman/8.0/en/innodb-locks-set.html
  - https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html
reusableFor:
  - 프로젝트 증거
  - 백엔드/성능/금융 시스템
  - 독서/책/학습
confidence: medium
verificationStatus: partial
evidenceScope: project-wiki-and-official-publisher-and-framework-documentation
---

# 금융 계좌이체 프로젝트 트랜잭션·아키텍처 학습 경로

## 결론

SQL 문법 연습, DB 트랜잭션 이론, 소프트웨어 아키텍처는 서로 연결되지만 같은 공부는 아니다. 지금 프로젝트에는 책 완독보다 DB 저장을 붙인 뒤 실패와 동시 요청을 직접 재현하는 학습이 우선이다.

현재 `financial-lab`은 `ConcurrentHashMap` 기반 메모리 저장소 단계다. DB commit/rollback이나 실제 이체 원자성은 아직 구현되지 않았다. 다음 단계에서 JPA와 MySQL을 붙이고 트랜잭션과 원장을 구현하도록 설계되어 있다.

## 개념 구분

- **원자성 / rollback**: 한 이체의 출금, 입금, `Transfer`, 차변·대변 원장 항목이 한 DB 트랜잭션에서 전부 commit되거나 전부 취소된다.
- **동시성 제어**: 겹쳐 실행된 요청들이 같은 잔액을 읽고 둘 다 성공 처리하는 경쟁 조건을 막는다. `@Transactional`만으로 업무 규칙의 경쟁 조건이 자동으로 해결되지는 않는다.
- **일관성**: 잔액은 음수가 되지 않고, 성공 이체의 차변·대변 합계는 0이라는 업무 불변조건이 유지된다.

Spring `@Transactional`은 보통 AOP proxy와 transaction manager를 통해 메서드 경계에 트랜잭션을 적용한다. Spring 기본 rollback 규칙은 unchecked exception과 `Error`에 rollback을 적용하고, checked exception은 기본적으로 자동 rollback하지 않으므로 프로젝트 예외 계층과 규칙을 확인해야 한다. MySQL 문서는 commit/rollback 및 locking read 동작을 구현 시점에 확인한다.

## 프로젝트에서 확인할 실험 순서

1. DB 저장 happy path를 연결하고, 이체 Service 한 경계 안에서 양쪽 계좌와 transfer/ledger 기록을 변경한다.
2. 출금 이후 예외를 주입한다. 독립된 조회로 양쪽 잔액과 거래/원장 행이 전부 원래 상태인지 확인한다.
3. 잔액 100,000원 계좌에서 80,000원 이체 두 건을 동시에 실행한다. 한 건만 성공하고 잔액이 음수가 되지 않는지 확인한다.
4. 실패를 먼저 재현한 뒤 조건부 UPDATE, optimistic locking (`@Version`), pessimistic locking (`SELECT ... FOR UPDATE`)을 비교하고 선택 이유를 설명한다.
5. 이체 Service transaction boundary, repository, DB가 맡는 책임과 대안을 짧은 architecture decision record로 남긴다.

## 책과 학습 단계

### 지금: DB 원리와 프로젝트 실험

**김연희, 《IT CookBook, 데이터베이스 개론(4판)》**을 transaction·recovery·concurrency의 기초 책으로 추천한다. 2026년 출간된 초급서이며 SQL, 데이터 모델링, 설계에 이어 11장에서 트랜잭션, 장애와 회복, 병행 제어를 다룬다. 이 책으로 ACID와 동시성 현상을 이해하고, 코드는 Spring과 MySQL 문서 및 프로젝트 테스트에서 확인한다.

### 코드 구조를 보는 아키텍처

**마크 리처즈·닐 포드, 《소프트웨어 아키텍처 The Basics(2판)》**을 다음 아키텍처 책으로 추천한다. 한국어판은 2025년 출간됐다. 계층형 아키텍처와 모듈형 모놀리스, 컴포넌트 경계, 트레이드오프, architecture decision record, 다이어그램을 다룬다. 프로젝트의 Controller-Service-Repository와 transfer transaction boundary를 왜 그 위치에 두는지 설명하는 데 적용한다.

### 데이터 시스템 아키텍처 심화

**Martin Kleppmann·Chris Riccomini, *Designing Data-Intensive Applications*, 2nd Edition**은 consistency, reliability, scalability, transaction isolation과 distributed systems를 더 넓게 공부하고 싶을 때 읽을 심화서다. O'Reilly는 2026년 2월 출간, intermediate-to-advanced, 영어판으로 안내한다. 한국어판으로 확인되는 《데이터 중심 애플리케이션 설계》는 2018년판이다. 지금 프로젝트의 첫 트랜잭션 실험을 끝낸 뒤 읽는 편이 맥락을 잡기 쉽다.

## 학습 우선순위

SQL 입문서는 SELECT/JOIN 등을 쓰는 연습에 사용하고, 금융 정합성은 별도의 DB 개념 학습과 실패 테스트로 확인한다. 당장 읽을 책은 데이터베이스 개론 4판, 아키텍처 책은 계층형·모듈형 모놀리스 중심으로 이어서 읽는다. 프로젝트의 현재 범위에서는 계좌이체 한 건의 요청에서 DB까지의 흐름과 트랜잭션 경계를 먼저 명확히 만든다.

> [!note] Bias Check
> 책 설명과 판본은 출판사/저자 자료로 확인했지만, 어떤 책이 가장 잘 맞는지는 사용자 수준과 프로젝트 목표를 바탕으로 한 추천 판단이다. 트랜잭션 성공은 어노테이션 존재만으로 주장하지 않고, DB 상태를 관찰하는 rollback 및 동시성 테스트로 검증한다.

이 답변은 백엔드/금융 시스템과 프로젝트 증거에 활용 가능합니다 — 책의 개념을 계좌이체 실패·동시 요청 테스트 및 설명 가능한 아키텍처 결정으로 바꾸는 경로를 제시한다.
