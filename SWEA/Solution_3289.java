package algorithm.d0222;

import java.io.*;
import java.util.*;

public class Solution_3289 {
	static int[] arr;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Int(br.readLine());
		for(int t=1;t<=T;t++) {
			sb.append('#').append(t).append(' ');
			st = new StringTokenizer(br.readLine());
			int n = Int(st.nextToken()), m = Int(st.nextToken());
			arr = new int[n+1];
			for(int i=1;i<n+1;i++) arr[i] = i;
			while(m-->0) {
				st = new StringTokenizer(br.readLine());
				int c = Int(st.nextToken()), ap = find(Int(st.nextToken())), bp = find(Int(st.nextToken()));
				if(c==0) arr[Math.min(ap, bp)] = Math.max(ap, bp);
				else sb.append(ap==bp ? 1 : 0);
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}
	static int Int(String s) { return Integer.parseInt(s);}
	static int find(int a) {return a==arr[a] ? a : find(arr[a]);}
}