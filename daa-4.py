import heapq 
import streamlit as st
  
def dijkstra(graph, source): 
    """ 
    Dijkstra's Algorithm using Min-Heap 
    Time: O((V + E) log V), Space: O(V) 
    graph: dict {u: [(v, weight), ...]}, 0-indexed 
    """ 
    n = len(graph) 
    dist = [float('inf')] * n 
    prev = [None] * n 
    dist[source] = 0 
    pq = [(0, source)]  # (distance, vertex) 
    visited = set() 
  
    while pq: 
        d, u = heapq.heappop(pq) 
        if u in visited: 
            continue 
        visited.add(u) 
        for v, w in graph[u]: 
            if dist[u] + w < dist[v]: 
                dist[v] = dist[u] + w 
                prev[v] = u 
                heapq.heappush(pq, (dist[v], v)) 
  
    return dist, prev 
  
def reconstruct_path(prev, source, target): 
    path = [] 
    node = target 
    while node is not None: 
        path.append(node) 
        node = prev[node] 
    path.reverse() 
    if path[0] == source: 
        return path 
    return [] 
  
# -------------------- Streamlit UI --------------------

st.title("Dijkstra's Shortest Path Algorithm")

st.write("Click the button below to find the shortest paths from the source vertex.")

if st.button("Run Dijkstra Algorithm"):

    # --- Graph Definition (Adjacency List) ---
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }

    source = 0

    dist, prev = dijkstra(graph, source)

    st.subheader(f"Shortest Paths from Vertex {source}")

    result = []

    for v in range(len(graph)):
        path = reconstruct_path(prev, source, v)
        path_str = " → ".join(map(str, path)) if path else "No Path"
        d = dist[v] if dist[v] != float('inf') else "INF"

        result.append({
            "Vertex": v,
            "Distance": d,
            "Path": path_str
        })

    st.table(result)