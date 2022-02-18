package algorithm.d0218;

import java.io.*;
import java.util.*;

public class Solution_3234 {
	static int N,ans;
	static int[] weight,nums;
	static boolean[] TF;
	static int Int(String s) {return Integer.parseInt(s);}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Int(br.readLine());
		for(int t=1;t<=T;t++) {
			N = Int(br.readLine());ans = 0;
			weight = new int[N];nums = new int[N];
			TF = new boolean[N];
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<N;i++) weight[i] = Int(st.nextToken());
			rec(0);
			sb.append('#').append(t).append(' ').append(ans).append('\n');
		}
		System.out.print(sb.toString());
	}
	static void rec(int cur) {
		if(cur == N) {
			dfs(0,0);
			return;
		}

		for(int i=0;i<N;i++) {
			if(TF[i]) continue;
			nums[cur] = weight[i];
			TF[i] = true;
			rec(cur+1);
			TF[i] = false;
		}
	}
	static void dfs(int cur,int w) {
		if(cur == N) {
			ans ++;
			return;
		}
		dfs(cur+1,w+nums[cur]);
		if(w-nums[cur]>=0) dfs(cur+1,w-nums[cur]);
	}
}
