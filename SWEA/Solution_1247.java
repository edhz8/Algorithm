package algorithm.d0217;

import java.io.*;
import java.util.*;

public class Solution_1247{
	static int N,MIN;
	static int[][] xy,len;
	static boolean[] TF;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Int(br.readLine());
		for(int t=1;t<=T;t++) {
			N = Int(br.readLine());
			st = new StringTokenizer(br.readLine());
			xy = new int[N+2][];
			xy[N] = new int[] {Int(st.nextToken()),Int(st.nextToken())};
			xy[N+1] = new int[] {Int(st.nextToken()),Int(st.nextToken())};
			for(int i=0;i<N;i++) xy[i] = new int[] {Int(st.nextToken()),Int(st.nextToken())};
			len = new int[N+2][N+2];
			for(int i=0;i<N+2;i++) for(int j=0;j<N+2;j++) len[i][j] = Math.abs(xy[i][0] - xy[j][0]) + Math.abs(xy[i][1] - xy[j][1]);
			MIN = Integer.MAX_VALUE;
			TF = new boolean[N];
			rec(0,N,0);
			sb.append('#').append(t).append(' ').append(MIN).append('\n');
		}
		System.out.print(sb.toString());
	}
	static void rec(int cnt,int li,int sum) {
		if(cnt==N) {
			MIN = Math.min(MIN, sum+len[N+1][li]);
			return;
		}
		for(int i=0;i<N;i++) {
			int nc = sum + len[i][li];
			if(TF[i] || MIN<nc) continue;
			TF[i] = true;
			rec(cnt+1,i,nc);
			TF[i] = false;
		}
	}
	static int Int(String s) {return Integer.parseInt(s);}
}
