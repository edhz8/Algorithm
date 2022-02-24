package algorithm.d0224;

import java.io.*;
import java.util.*;

public class boj_1753 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int V = Int(st.nextToken()), E = Int(st.nextToken()), K = Int(br.readLine());
        ArrayList<ArrayList<Node>> g = new ArrayList<>(V+1);
        for(int i=0;i<V+1;i++) g.add(new ArrayList<>());
        int[] dp = new int[V+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for(int i=0;i<E;i++) {
        	st = new StringTokenizer(br.readLine());
        	g.get(Int(st.nextToken())).add(new Node(Int(st.nextToken()),Int(st.nextToken())));
        }   
        dp[K] = 0;
        pq.offer(new Node(K,0));
        while(!pq.isEmpty()) {
        	Node poll = pq.poll();
        	int to = poll.to, w = poll.w;
        	for(Node cnode: g.get(to)) {
        		int cto = cnode.to, cw = cnode.w;
        		int nw = w+cw;
        		if(nw<dp[cto]) {
        			dp[cto] = nw;
            		pq.offer(new Node(cto,nw));
        		}
        	}
        }
        for(int i=1;i<V+1;i++) sb.append(dp[i]== Integer.MAX_VALUE ? "INF" : dp[i]).append('\n');
        System.out.print(sb.toString());
	}
	static int Int(String s) {return Integer.parseInt(s);}
	
	static class Node implements Comparable<Node>{
		int to,w;
		public Node(int to, int w) {
			this.to = to;
			this.w = w;
		}
		public int compareTo(Node o) {
			return this.w-o.w;
		}
	}
}
