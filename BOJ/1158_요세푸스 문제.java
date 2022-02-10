package algorithm.d0210;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class boj_1158 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st  = new StringTokenizer(br.readLine());		
		int N=Integer.parseInt(st.nextToken()),K=Integer.parseInt(st.nextToken());
		LinkedList<Integer> nums = new LinkedList<>();
		for(int i=1;i<=N;i++) nums.offer(i);
		sb.append('<');
		while(N --> 0) {
			Collections.rotate(nums, -K+1);
			sb.append(nums.poll()).append(nums.isEmpty() ? ">" : ", ");
		}
		System.out.println(sb.toString());
	}
}
