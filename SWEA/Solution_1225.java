package algorithm.d0208;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution_1225 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for(int t=1;t<=10;t++) {
			br.readLine();
			LinkedList<Integer> Q = new LinkedList<>();
			StringTokenizer nums = new StringTokenizer(br.readLine());
			while(nums.hasMoreTokens()) Q.offer(Integer.parseInt(nums.nextToken()));
			int min = Collections.min(Q)/15;
			for(int i=0;i<8;i++) Q.offer(Q.poll()-15*(min)+15);
			for(int i=0;;i++) {
				int num = Q.poll()-(i%5+1);
				if(num>0) Q.offer(num);
				else {
					Q.add(0);
					break;
				}
			}
			sb.append("#").append(t);
			for(int q : Q) sb.append(" ").append(q);
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}
