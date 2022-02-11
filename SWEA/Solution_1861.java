package algorithm.d0211;

import java.io.*;
import java.util.StringTokenizer;

public class Solution_1861 {
	static int[] dx = {-1,0,1,0} , dy = {0,1,0,-1};
	static int N,max,mi;
	static int[][] map;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int TC = Integer.parseInt(br.readLine());
		for(int t=1;t<=TC;t++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			max = Integer.MIN_VALUE;
			mi = Integer.MAX_VALUE;
			for(int i=0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0;j<N;j++) map[i][j] = Integer.parseInt(st.nextToken());
			}
			for(int i=0;i<N;i++) for(int j=0;j<N;j++) dfs(i,j,1,map[i][j]);
			sb.append('#').append(t).append(' ').append(mi).append(' ').append(max).append('\n');
		}
		System.out.print(sb.toString());
	}
	
	public static void dfs(int x,int y,int cnt,int first) {
		boolean LAST = true;
		for(int d=0;d<dx.length;d++) {
			int nx = x+dx[d] , ny = y+dy[d];
			if(nx<0 || nx>=N || ny<0 || ny>=N || map[x][y]+1 != map[nx][ny]) continue;
			LAST = false;
			dfs(nx,ny,cnt+1,first);
		}
		if(LAST && max<=cnt) {
			mi = max<cnt ? first : Math.min(mi, first);
			max = cnt;
		}
	}
}
