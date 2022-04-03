package algorithm.d0330;

import java.io.*;
import java.util.*;

public class Solution_3124 {
	static class Edge implements Comparable<Edge>{
		int v, w;
		Edge(int e, int v) {
			this.v = e;
			this.w = v;
		}
		@Override
		public int compareTo(Edge o) { return this.w - o.w; }
	}
	static int Int(String s) {return Integer.parseInt(s);}
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;		
		int T=Int(br.readLine());		
		for(int t=1;t<=T;t++) {
			st=new StringTokenizer(br.readLine()," ");
			int V=Integer.parseInt(st.nextToken()), E=Integer.parseInt(st.nextToken());
			boolean[] visited= new boolean[V];			
			List<Edge>[] edgeList = new ArrayList[V];			
			for(int i=0;i<V;i++) edgeList[i] = new ArrayList<Edge>();			
			for(int i=0; i<E; i++) {
				st = new StringTokenizer(br.readLine());
				int from = Int(st.nextToken())-1 , to = Int(st.nextToken())-1 , weight=Int(st.nextToken());
				edgeList[from].add(new Edge(to,weight));
				edgeList[to].add(new Edge(from,weight));
			}			
			PriorityQueue<Edge> pq=new PriorityQueue<Edge>();
			for(Edge e : edgeList[0]) pq.add(e);			
			long result=0;
			int cnt=0;
			visited[0]=true;
			while(!pq.isEmpty()){
				Edge cur=pq.poll();
				if(visited[cur.v]) continue;
				result+=cur.w;  
				visited[cur.v]=true;
				if(cnt++ == V-1) break; 
				for(Edge e:edgeList[cur.v]) if(!visited[e.v]) pq.add(e);
			}
			sb.append("#").append(t).append(" ").append(result).append("\n");
		}
        System.out.print(sb);
    }
}