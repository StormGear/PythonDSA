package Graphs;

public class BellmanFord {

    // A directed edge
    public static class Edge {
        double cost;
        int from, to;
        public Edge(int from, int to, double cost) {
            this.to = to;
            this.from = from;
            this.cost = cost;
        }
    }

     public static void main(String[] args) {
        // Example graph represented as an edge list
        // int[][] graph = {
        //     {0, 1, -1},
        //     {0, 2, 4},
        //     {1, 2, 3},
        //     {1, 3, 2},
        //     {1, 4, 2},
        //     {3, 2, 5},
        //     {3, 1, 1},
        //     {4, 3, -3}
        // };
        Edge[] graph = {
            new Edge(0, 1, -1),
            new Edge(0,2,4),
            new Edge(1,2,3),
            new Edge(1,3,2),
            new Edge(1,4,2),
            new Edge(3,2,5),
            new Edge(3,1,1),
            new Edge(4,3,-3),

        };
        int V = 5; // Number of vertices
        int E = graph.length; // Number of edges
        int src = 0; // Starting vertex

        bellmanFord(graph, V, E, src);
    }

   public static void bellmanFord(Edge[] graph, int V, int E, int src) {
       double[] dist = new double[V];

       // Step 1: Initialize distances from src to all other vertices as infinite
       for (int i = 0; i < V; i++) {
           dist[i] = Double.POSITIVE_INFINITY;
       }
       dist[src] = 0;

       // Step 2: Relax all edges |V| - 1 times
       for (int i = 1; i < V; i++) {
           for (int j = 0; j < E; j++) {
               int u = graph[j].from;
               int v = graph[j].to;
               double weight = graph[j].cost;
               if (dist[u] != Double.POSITIVE_INFINITY && dist[u] + weight < dist[v]) {
                   dist[v] = dist[u] + weight;
               }
           }
       }

       // Step 3: Check for negative-weight cycles
       for (int j = 0; j < E; j++) {
           int u = graph[j].from;
            int v = graph[j].to;
            double weight = graph[j].cost;;
           if (dist[u] != Double.POSITIVE_INFINITY && dist[u] + weight < dist[v]) {
               System.out.println("Graph contains negative weight cycle");
               return;
           }
       }

       // Print the distance array
       System.out.println("Vertex Distance from Source");
       for (int i = 0; i < V; i++) {
           System.out.println(i + "\t\t" + dist[i]);
       }
   }

}
