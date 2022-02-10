package algorithm.d0209;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class boj_3040 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] nums = new int[9];
		int sum = 0;
		for(int i=0;i<9;i++) {
			int num = Integer.parseInt(br.readLine());
			nums[i] = num;
			sum += num;
		}
		sum-=100;
		for(int i=0;i<9;i++) {
			for(int j=i+1;j<9;j++) {
				if(j==9) break;
				if(nums[i]+nums[j] == sum) {
					for(int k=0;k<9;k++) if(k!=i && k!=j)System.out.println(nums[k]);
				}
			}
		}
	}
}
