
from collections import deque
from typing import Optional

MAZE_GRID = [
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

START = (0, 0)
END   = (6, 6)

ROWS = len(MAZE_GRID)
COLS = len(MAZE_GRID[0])

class MazeGraph:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.adj: dict[tuple, list[tuple]] = {}
        self._build()

    def _build(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 0:
                    vertex = (r, c)
                    self.adj[vertex] = []
                    for dr, dc in self.DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < self.rows and
                                0 <= nc < self.cols and
                                self.grid[nr][nc] == 0):
                            self.adj[vertex].append((nr, nc))

    def vertices(self) -> list[tuple]:
        return list(self.adj.keys())

    def neighbors(self, v: tuple) -> list[tuple]:
        return self.adj.get(v, [])

    def print_maze(self, path: Optional[list[tuple]] = None) -> None:
        path_set = set(path) if path else set()
        print()
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                cell = (r, c)
                if cell == START:
                    row_str += " S"
                elif cell == END:
                    row_str += " E"
                elif cell in path_set:
                    row_str += " ."
                elif self.grid[r][c] == 1:
                    row_str += " #"
                else:
                    row_str += "  "
            print(row_str)
        print()

def reconstruct_path(came_from: dict, start: tuple,
                     end: tuple) -> list[tuple]:
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    if path[0] == start:
        return path
    return []

def dfs(graph: MazeGraph, start: tuple, end: tuple
        ) -> tuple[list[tuple], int]:
    stack: list[tuple] = [start]
    came_from: dict[tuple, Optional[tuple]] = {start: None}
    visited_count = 0

    while stack:
        current = stack.pop()
        visited_count += 1

        if current == end:
            return reconstruct_path(came_from, start, end), visited_count

        for neighbor in graph.neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                stack.append(neighbor)

    return [], visited_count

def bfs(graph: MazeGraph, start: tuple, end: tuple
        ) -> tuple[list[tuple], int]:
    queue: deque = deque([start])
    came_from: dict[tuple, Optional[tuple]] = {start: None}
    visited_count = 0

    while queue:
        current = queue.popleft()
        visited_count += 1

        if current == end:
            return reconstruct_path(came_from, start, end), visited_count

        for neighbor in graph.neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    return [], visited_count

def main():
    print("\n" + "="*60)
    print("  QUESTÃO 3 - LABIRINTO: DFS vs BFS")
    print("="*60)

    graph = MazeGraph(MAZE_GRID)

    print(f"\nVértices no grafo: {len(graph.vertices())}")
    print(f"Entrada: {START}  |  Saída: {END}")

    print("\n-- Labirinto original ----------------------------")
    graph.print_maze()

    print("-- DFS (Busca em Profundidade) -------------------")
    dfs_path, dfs_visited = dfs(graph, START, END)

    if dfs_path:
        print(f"Caminho encontrado ({len(dfs_path)} passos): {dfs_path}")
        print(f"Nós visitados: {dfs_visited}")
        graph.print_maze(dfs_path)
    else:
        print("Sem caminho encontrado (DFS)")

    print("-- BFS (Busca em Largura) ------------------------")
    bfs_path, bfs_visited = bfs(graph, START, END)

    if bfs_path:
        print(f"Caminho encontrado ({len(bfs_path)} passos): {bfs_path}")
        print(f"Nós visitados: {bfs_visited}")
        graph.print_maze(bfs_path)
    else:
        print("Sem caminho encontrado (BFS)")

    print("\n-- Comparação DFS x BFS --------------------------")
    print(f"{'Métrica':<30} {'DFS':>8} {'BFS':>8}")
    print("-"*48)
    print(f"{'Comprimento do caminho':<30} {len(dfs_path):>8} {len(bfs_path):>8}")
    print(f"{'Nós visitados':<30} {dfs_visited:>8} {bfs_visited:>8}")
    print(f"{'Caminho ótimo (mínimo)?':<30} {'?':>8} {'Sim':>8}")

if __name__ == "__main__":
    main()
