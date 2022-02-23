package algorithm.d0223;

import java.io.*;

public class boj_10026 {
	static int N;
	static boolean[][] v1,v2;
	static char[][] map1,map2;
	static int[] dx = {-1,0,1,0}, dy= {0,1,0,-1};
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		v1 = new boolean[N][N];v2 = new boolean[N][N];
		map1 = new char[N][N];map2 = new char[N][N];
		int a1=0,a2=0;
		for(int i=0;i<N;i++) {
			char[] line = br.readLine().toCharArray();
			for(int j=0;j<N;j++) {
				map1[i][j] = line[j];
				map2[i][j] = line[j] == 'R' ? 'G':line[j];
			}
		}
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				if(!v1[i][j]) {
					dfs1(i,j);
					a1++;
				}
				if(!v2[i][j]) {
					dfs2(i,j);
					a2++;
				}
			}
		}
		System.out.printf("%d %d",a1,a2);
	}
	static void dfs1(int x,int y){
		v1[x][y] = true;
		for(int i=0;i<4;i++) {
			int nx = x+dx[i], ny = y+dy[i];
			if(nx>=0 && nx<N && ny>=0 && ny<N && map1[nx][ny]==map1[x][y] && !v1[nx][ny]) dfs1(nx,ny);
		}
	}
	static void dfs2(int x,int y){
		v2[x][y] = true;
		for(int i=0;i<4;i++) {
			int nx = x+dx[i], ny = y+dy[i];
			if(nx>=0 && nx<N && ny>=0 && ny<N && map2[nx][ny]==map2[x][y] && !v2[nx][ny]) dfs2(nx,ny);
		}
	}
}
