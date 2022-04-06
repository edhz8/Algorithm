package algorithm.d0406;
import java.util.*;
import java.io.*;
public class Main {
	static int g[][],cur,N,M;
	static boolean visited[];
	static int Int(String s) {return Integer.parseInt(s);}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;	
		st = new StringTokenizer(br.readLine());
		N = Int(st.nextToken()); M = Int(st.nextToken());
		g = new int[N][N];
		int ans = 0;
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int small = Int(st.nextToken())-1, big = Int(st.nextToken())-1;
			g[small][big] = 2;
			g[big][small] = 1;
		}
		for(int i=0;i<N;i++) {
			visited = new boolean[N];
			cur = 0;
			dfs(i,0);
			if(cur == N-1) ans++;
		}
		System.out.println(ans);
	}
	static void dfs(int node,int mode) {
		for(int i=0;i<N;i++) {
			if(g[node][i]==0 || (mode>0 && g[node][i] != mode) || visited[i]) continue;
			visited[i] = true;
			cur ++;
			dfs(i,g[node][i]);
		}
	}
}