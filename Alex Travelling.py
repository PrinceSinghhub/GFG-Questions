'''
//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

// Position this line where user code will be pasted.

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();

            int tmp = sc.nextInt();
            int[][] flights = new int[tmp][3];
            for (int i = 0; i < tmp; i++) {

                int u1 = sc.nextInt();
                int v1 = sc.nextInt();
                int w1 = sc.nextInt();
                flights[i][0] = u1;
                flights[i][1] = v1;
                flights[i][2] = w1;
            }

            Solution ob = new Solution();
            int ans = ob.minimumCost(flights, n, k);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {

    class Graph {
		private class Node {
			int vertex;
			int weight;

			public Node(int vertex, int weight) {
				this.vertex = vertex;
				this.weight = weight;
			}
		}

		private class QueueNode {
			private int vertex;
			private int key;

			public QueueNode(int vertex, int key) {
				super();
				this.vertex = vertex;
				this.key = key;
			}
		}

		private int v;
		private ArrayList<ArrayList<Node>> adj;

		public Graph(int v) {
			this.v = v;
			this.adj = new ArrayList<ArrayList<Node>>(this.v);
			for (int u = 0; u < this.v; u++) {
				this.adj.add(new ArrayList<Node>());
			}
		}

		public void addEdge(int u, int v, int weight) {
			adj.get(u).add(new Node(v, weight));
		}

		public int minimumCost(int k) {
			int[]visited = new int[this.v];
			Arrays.fill(visited, -1);
			Queue<QueueNode> queue = new LinkedList<QueueNode>();
			visited[k] = 0;
			queue.add(new QueueNode(k, visited[k]));
			while (!queue.isEmpty()) {
				QueueNode current = queue.poll();
				int u = current.vertex;
				for (Node adjacent : adj.get(u)) {
					int v = adjacent.vertex;
					int weight = adjacent.weight;
					if (visited[v] == -1 || visited[v] > visited[u] + weight) {
						visited[v] = visited[u] + weight;
						queue.add(new QueueNode(v, visited[v]));
					}
				}
			}
			int minimumCost = 0;
			for (int i = 1; i < visited.length; i++) {
				if(visited[i] != -1) {
                    minimumCost = Math.max(minimumCost, visited[i]);
                }else if(visited[i] == -1){
                    return -1;
                }
			}
			return minimumCost;
		}

	}
    int minimumCost(int[][] flights, int n, int k) {
        // Your code here
        Graph graph = new Graph(n + 1);
        for(int[] edge : flights){
            graph.addEdge(edge[0], edge[1], edge[2]);
        }
        return graph.minimumCost(k);
    }
}


'''