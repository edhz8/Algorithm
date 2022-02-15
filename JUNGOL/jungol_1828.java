package algorithm.d0215;

import java.io.*;
import java.util.*;

public class jungol_1828 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine()), cnt = 1,max;
		int[][] temp = new int [N][2];	
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			temp[i][0] = Integer.parseInt(st.nextToken()); 
			temp[i][1] = Integer.parseInt(st.nextToken()); 
		}
		Arrays.sort(temp, (int[] a, int[] b) -> a[1]-b[1]);		
		max=temp[0][1];
		for(int i=1;i<N;i++) {
			if(max < temp[i][0]) {
				max = temp[i][1];
				cnt++;
			}
		}
		System.out.println(cnt);
	}
}