"""
Vertex 정점 - 간선이 존재한다면 '인접정점'
Edge 간선 - 두 정점을 연결하는 선
Degree 차수 - 정점 하나에 연결된 간선의 수

너비우선탐색(BFS)
너비우선 탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후
방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식입니다.
따라서 선입선출 형태의 큐 자료구조를 활용하여 만듭니다.

깊이우선탐색(DFS)
시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해가다가 더 이상 갈 곳이 없게 되면
가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서
다른 방향의 정점으로 탐색을 계속 반복하여
결국 모든 정점을 방문하는 순회 방법입니다.
가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 탐색하므로
후입선출 구조로 구현합니다.
메모리 스택을 활용한 재귀 함수, 혹은 직접 스택에 탐색 내용을 사용합니다.
"""


# 방향 그래프
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def printGraph(graph):
    for src in range(len(graph.adjList)):
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest})', end=' ')
        print()


edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]

n = 6

graph = Graph(edges, n)

printGraph(graph)
