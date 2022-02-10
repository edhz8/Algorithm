package algorithm.d0210;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2116 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int cnt = Integer.parseInt(br.readLine()),max=Integer.MIN_VALUE;
		int[][] cubes = new int[cnt][6];
		for(int i=0;i<cnt;i++) {
			st  = new StringTokenizer(br.readLine());
			for(int j=0;j<6;j++) cubes[i][j] = Integer.parseInt(st.nextToken());
			int temp = cubes[i][3];
			cubes[i][3] = cubes[i][4];
			cubes[i][4] = temp;
		}
		for(int i=0;i<6;i++) {
			int top = cubes[0][i], ti = i;
			int cur = 0;
			for(int j=0;j<cnt;j++) {
				for(int k=0;k<6;k++) {
					if(cubes[j][k] == top) {
						top = cubes[j][5-k];
						ti = 5-k;
						break;
					}
				}
				int cmax = Integer.MIN_VALUE;
				for(int k=0;k<6;k++) {
					if(k==ti || k==5-ti) continue;
					cmax = Math.max(cmax, cubes[j][k]);
				}
				cur += cmax;
			}
			max = Math.max(max, cur);
		}
		System.out.print(max);
	}
}
