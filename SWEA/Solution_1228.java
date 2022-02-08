package algorithm.d0208;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution_1228 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for(int t=1;t<=10;t++) {
			int N = Integer.parseInt(br.readLine());
			LinkedList<String> nums = new LinkedList<>();
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<N;i++) nums.add(st.nextToken());
			int M = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			while(M --> 0) {
				st.nextToken();
				int x = Integer.parseInt(st.nextToken()) , y = Integer.parseInt(st.nextToken());
				if(x>10) {
					while(y --> 0) st.nextToken();
					continue;
				}
				LinkedList<String> inputs = new LinkedList<>();
				while(y --> 0) inputs.add(st.nextToken());
				nums.addAll(x, inputs);
			}
			sb.append("#").append(t);
			for(int i=0;i<10;i++) sb.append(" ").append(nums.get(i));
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}