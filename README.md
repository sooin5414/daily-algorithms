# Algorithm Solutions

## Baekjoon 4195 - 친구 네트워크

Union-Find(Disjoint Set Union) 자료구조를 활용한 문제

### 문제 설명
- 친구 관계가 하나씩 추가될 때마다 두 사람이 속한 친구 네트워크의 크기를 즉시 출력
- 연결된 컴포넌트(한 사람에서 친구 관계만 타고 가서 도달할 수 있는 모든 사람 집합) 관리

### 핵심 개념
- **서로소 집합(Disjoint Set)**: 서로 겹치지 않는 집합들을 관리
- **Find 연산**: 특정 원소가 어느 집합에 속해있는지 찾기
- **Union 연산**: 두 집합을 하나로 합치기
- **경로 압축(Path Compression)**: Find 연산 최적화

### 구현
- DSU(Disjoint Set Union) 자료구조 사용
- 각 집합의 크기를 추적하여 네트워크 크기 출력
