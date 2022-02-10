package algorithm.d0210;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj_2309 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] nums = new int[9];
		int sum = 0;
		for(int i=0;i<9;i++) {
			int num = Integer.parseInt(br.readLine());
			nums[i] = num;
			sum += num;
		}
		Arrays.sort(nums);
		for(int i=0;i<8;i++) {
			for(int j=i+1;j<9;j++) {
				if(nums[i]+nums[j] == sum-100) {
					for(int k=0;k<9;k++) if(k!=i && k!=j)System.out.println(nums[k]);
					return;
				}
			}
		}
	}
}