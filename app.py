from flask import Flask, request, jsonify
from graph import Graph  # Import the Graph class

app = Flask(__name__)

# Create the graph
graph = Graph()
graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 2)
graph.add_edge("A", "D", 4)
graph.add_edge("D", "C", 1)

@app.route('/run', methods=['GET'])
def run_algorithm():
    algo = request.args.get('algo')
    start = request.args.get('start')
    goal = request.args.get('goal')
    
    if algo == "bfs":
        path, cost, steps = graph.bfs(start, goal)
    elif algo == "dfs":
        path, cost, steps = graph.dfs(start, goal)
    elif algo == "ucs":
        path, cost, steps = graph.ucs(start, goal)
    else:
        return jsonify({"error": "Invalid algorithm selected"}), 400

    return jsonify({"path": path, "cost": cost, "steps": steps})

if __name__ == '__main__':
    app.run(debug=True)
