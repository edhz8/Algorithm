package algorithm.d0224;

import java.io.*;
import java.util.*;

public class jungol_1681 {
	static int N,ans = Integer.MAX_VALUE;
	static boolean[] visited;
	static int[][] cost;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;  
        N = Int(br.readLine());
        visited = new boolean[N];
        cost = new int[N][N];
        for(int i=0;i<N;i++) {
        	st = new StringTokenizer(br.readLine());
        	for(int j=0;j<N;j++) cost[i][j] = Int(st.nextToken());
        }
        dfs(0,0,0);
        System.out.print(ans);
	}
	static int Int(String s) {return Integer.parseInt(s);}
	static void dfs(int x,int sum,int depth) {
		if(sum>ans) return;
		if(depth==N-1) {
			if(cost[x][0] !=0) ans = Math.min(ans, sum+cost[x][0]);
			return;
		}
		for(int i=1;i<N;i++) {
			int w = cost[x][i];
			if(visited[i] || w==0) continue;
			visited[i] = true;
			dfs(i,sum+w,depth+1);
			visited[i] = false;
		}
	}
}
