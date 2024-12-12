from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_edge(self, city1, city2, cost=1):
        if city1 not in self.adjacency_list:
            self.adjacency_list[city1] = []
        if city2 not in self.adjacency_list:
            self.adjacency_list[city2] = []
        self.adjacency_list[city1].append((city2, cost))
        self.adjacency_list[city2].append((city1, cost))

    def bfs(self, start, goal):
        queue = deque([(start, [start], 0)])
        visited = set()
        steps = 0
        
        while queue:
            steps += 1
            current_city, path, cost = queue.popleft()
            
            if current_city == goal:
                return path, cost, steps
            
            visited.add(current_city)
            
            for neighbor, edge_cost in self.adjacency_list.get(current_city, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + edge_cost))
        
        return None, float('inf'), steps

    def dfs(self, start, goal):
        stack = [(start, [start], 0)]
        visited = set()
        steps = 0
        
        while stack:
            steps += 1
            current_city, path, cost = stack.pop()
            
            if current_city == goal:
                return path, cost, steps
            
            if current_city not in visited:
                visited.add(current_city)
                
                for neighbor, edge_cost in reversed(self.adjacency_list.get(current_city, [])):
                    stack.append((neighbor, path + [neighbor], cost + edge_cost))
        
        return None, float('inf'), steps

    def ucs(self, start, goal):
        priority_queue = [(0, start, [start])]
        visited = set()
        steps = 0
        
        while priority_queue:
            steps += 1
            cost, current_city, path = heapq.heappop(priority_queue)
            
            if current_city == goal:
                return path, cost, steps
            
            if current_city not in visited:
                visited.add(current_city)
                
                for neighbor, edge_cost in self.adjacency_list.get(current_city, []):
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))
        
        return None, float('inf'), steps
