package algorithm.d0221;

import java.io.*;
import java.util.*;

public class boj_1759 {
	static int L,C;
	static int[] nums;
	static char[] chars;
	static StringBuilder sb = new StringBuilder();
	static int Int(String s) { return Integer.parseInt(s);}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        L = Int(st.nextToken()); C= Int(st.nextToken());
        nums = new int[L];
        chars = new char[C];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<C;i++) chars[i] = st.nextToken().charAt(0);
        Arrays.sort(chars);
        rec(0,0);
        System.out.print(sb.toString());
	}
	static void rec(int start,int cur) {
		if(cur==L) {
			StringBuilder stb = new StringBuilder();
			int ja=0,mo=0;
			for(int n:nums) {
				char c = chars[n];
				stb.append(c);
	        	if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u') ja++;
	        	else mo++;
			}
			if(ja>0 && mo>1) sb.append(stb).append('\n');
			return;
		}
		for(int i=start;i<C;i++) {
			nums[cur] = i;
			rec(i+1,cur+1);
		}
	}
}
