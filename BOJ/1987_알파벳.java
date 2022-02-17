package algorithm.d0217;

import java.io.*;
import java.util.*;

public class boj_1987 {
	static int r,c,res = Integer.MIN_VALUE;
	static int[] dx = {-1,0,1,0},dy= {0,1,0,-1};
	static char[][] graph;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c= Integer.parseInt(st.nextToken());
		graph = new char[r][c];
		for(int i=0;i<r;i++) graph[i] = br.readLine().toCharArray();
		dfs(writeBit(0,graph[0][0]),0,0,1);
		System.out.print(res);
	}
	static void dfs(int bit,int x,int y,int cnt) {
		for(int d=0;d<4;d++) {
			int nx = x+dx[d], ny = y+dy[d];
			if(nx<0 || nx>=r || ny<0 || ny>=c || cantGo(bit,graph[nx][ny])) {
				res = Math.max(res, cnt);
				continue;
			}
			dfs(writeBit(bit,graph[nx][ny]),nx,ny,cnt+1);
		}
	}
	static boolean cantGo(int bit,char c) {
		return (bit&(1<<(c-'A'))) != 0;
	}
	static int writeBit(int bit,char c) {
		return bit|(1<<(c-'A'));
	}
}
