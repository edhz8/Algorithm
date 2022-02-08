package algorithm.d0208;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_9229 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int TC = Integer.parseInt(br.readLine());
		for(int t=1;t<=TC;t++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			int[] nums = new int[N];
			int ans = -1;
			for(int i=0;i<N;i++) nums[i] = Integer.parseInt(st.nextToken());
			for(int i=0;i<N;i++) {
				for(int j=i+1;j<N;j++) {
					if(j>=N) continue;
					int sum = nums[i] + nums[j];
					if(sum>M) continue;
					ans = Math.max(ans, sum);
				}
			}
			sb.append("#").append(t).append(" ").append(ans).append("\n");
		}
		System.out.print(sb.toString());
	}
}
