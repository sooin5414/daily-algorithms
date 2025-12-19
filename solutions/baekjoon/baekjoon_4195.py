""" 친구 네트워크(Union Find)

- 친구 관계(간선)가 하나씩 추가될 때마다 그 두사람이 속한 연결 컴포넌트(친구 네트워크)의 크기를 즉시 출력하는 문제
- 그래프에서 연결된 컴포넌트(한 사람에서 친구 관계만 타고 가서 도달할수 있는 모든 사람 집합)
- DSU(Disjoint Set Union) 자료구조 """

"""1단계: 집합(Set) 개념
집합 A = {1, 2, 3}
집합 B = {4, 5}
원소들의 모음
각 원소는 어떤 집합에 속해있음

2단계: 서로소 집합 (Disjoint Set)
집합 A = {1, 2, 3}
집합 B = {4, 5}
집합 C = {6, 7}
서로 겹치지 않는 집합들
한 원소는 정확히 하나의 집합에만 속함
Union-Find는 이런 집합들을 관리하는 자료구조!

Find (찾기)
"이 원소는 어느 집합에 속해있어?"
Find(2) → 집합 A
Find(5) → 집합 B

Union (합치기)
"두 집합을 하나로 합쳐!"
Union(A, B) → 집합 AB = {1, 2, 3, 4, 5}"""

parent = {}
size = {}

def find(x):
    if x not in parent:
        parent[x] = x
        size[x] = 1
    
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return size[root_x]
    
    parent[root_y] = root_x
    size[root_x] += size[root_y]

    return size[root_x]