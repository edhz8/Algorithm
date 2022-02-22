package algorithm.d0222;

import java.io.*;
import java.util.*;

public class Solution_7465 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;	
		int T = Int(br.readLine());
		for(int t=1;t<=T;t++) {
			st = new StringTokenizer(br.readLine());
			int N = Int(st.nextToken()), M = Int(st.nextToken()), ans=0;
			boolean[][] map = new boolean[N+1][N+1];
			boolean[] v = new boolean[N+1];
			while(M-->0) {
				st = new StringTokenizer(br.readLine());
				int a = Int(st.nextToken()), b = Int(st.nextToken());
				map[a][b] = map[b][a] = true;
			}
			for(int i=1;i<N+1;i++) {
				if(v[i]) continue;
				ans++;
				v[i] = true;
				Deque<Integer> q = new ArrayDeque<>();
				q.add(i);
				while(!q.isEmpty()) {
					int cur = q.poll();
					for(int j=1;j<N+1;j++) {
						if(map[cur][j] && !v[j]) {
							v[j] = true;
							q.add(j);
						}
					}
				}
			}
			sb.append('#').append(t).append(' ').append(ans).append('\n');
		}
		System.out.println(sb.toString());
	}
	static int Int(String s) { return Integer.parseInt(s);}
}
