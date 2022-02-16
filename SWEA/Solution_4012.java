package algorithm.d0216;

import java.io.*;
import java.util.StringTokenizer;

public class Solution_4012 {
	static int N,min;
	static boolean[] num;
	static int[][] S;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			N = Integer.parseInt(br.readLine());
			S = new int[N][N];
			min = Integer.MAX_VALUE;
			num = new boolean[N];
			for(int i=0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0;j<N;j++) S[i][j] = Integer.parseInt(st.nextToken());
			}
			rec(0,0);
			sb.append('#').append(t).append(' ').append(min).append('\n');
		}
		System.out.println(sb.toString());
	}
	public static void rec(int start,int cnt) {
		if(cnt==N/2) {
			int s1=0,s2=0;
			for(int i=0;i<N-1;i++) {
				for(int j=i;j<N;j++) {
					if(i==j) continue;
					else if(num[i]&&num[j]) s1 += (S[i][j]+S[j][i]);
					else if(!num[i]&&!num[j]) s2 += (S[i][j]+S[j][i]);
				}
			}
			min = Math.min(min, Math.abs(s1-s2));
			return;
		}
		for(int i=start;i<N;i++) {
			num[i] = true;
			rec(i+1,cnt+1);
			num[i] = false;
		}
	}
}