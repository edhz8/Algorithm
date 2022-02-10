package algorithm.d0210;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2563 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] white = new int[101][101];
		int N = Integer.parseInt(br.readLine()) , sum = 0;
		while(N --> 0) {
			st = new StringTokenizer(br.readLine());
			int I = Integer.parseInt(st.nextToken()) , J= Integer.parseInt(st.nextToken());
			for(int i=I;i<I+10;i++) for(int j=J;j<J+10;j++) white[i][j] = 1;
		}
		for(int i=0;i<101;i++) for(int j=0;j<101;j++) sum+=white[i][j];
		System.out.print(sum);
	}
}
