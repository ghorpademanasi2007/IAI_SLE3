from collections import deque
import time

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}


def bfs_search(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    expanded = 0

    while queue:
        node, path = queue.popleft()
        expanded += 1

        if node == target:
            return path, expanded

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, expanded


def measure_bfs(target, runs=5000):
    bfs_search(GRAPH, "A", target)
    times = []
    path = None
    expanded = 0

    for _ in range(runs):
        start_time = time.perf_counter()
        path, expanded = bfs_search(GRAPH, "A", target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    return path, expanded, sum(times) / len(times), min(times), max(times)


def print_result(case_name, target):
    path, expanded, average, best, worst = measure_bfs(target)
    path_text = " -> ".join(path) if path else "Not found"
    print(f"{case_name:<10} {target:<8} {average:<15.6f} {best:<15.6f} {worst:<15.6f} {expanded:<8}")
    print(f"Path: {path_text}")


if __name__ == "__main__":
    print("=" * 82)
    print("                 BFS GRAPH SEARCH SYSTEM")
    print("=" * 82)
    print("Graph: A -> {B,C}, B -> {D,E}, C -> F, D/E/F -> G")
    print("Timing runs per case: 5000\n")
    print(f"{'Case':<10} {'Target':<8} {'Average(ms)':<15} {'Best(ms)':<15} {'Worst(ms)':<15} {'Nodes':<8}")
    print("-" * 82)

    print_result("Best", "A")
    print_result("Average", "E")
    print_result("Worst", "Z")

    print("-" * 82)
    print("Time complexity: O(V + E)")
    print("Space complexity: O(V)")
