package algorithm.d0209;

import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Solution_3499 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			int N = Integer.parseInt(br.readLine());
			String[] deck = br.readLine().split(" ");
			int half = (deck.length+1)/2;
			sb.append('#').append(t);
			for(int i=0;i<N;i++) sb.append(' ').append(deck[i/2 + (i%2==0 ? 0 : half)]);
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}
}
