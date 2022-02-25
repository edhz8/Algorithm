package algorithm.d0225;

import java.io.*;
import java.util.*;

public class boj_1244 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
		StringTokenizer st;
        int N = Int(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] S = new int[N+1];
        for(int i=1;i<=N;i++) S[i] = Int(st.nextToken());
        int stu = Int(br.readLine());
        for(int t=0;t<stu;t++) {
        	st = new StringTokenizer(br.readLine());
        	boolean man = Int(st.nextToken()) ==  1;
        	int num = Int(st.nextToken());
        	if(man) {
        		for(int i=num;i<=N;i+=num) S[i] ^= 1;
        	} else {
        		int from = num, to = num;
        		while(from>0 && to<=N && S[from]==S[to]) {
        			S[from]^=1;
        			if(from != to) S[to] ^= 1;
        			from--;
        			to++;
        		}
        	}
        }
        for(int i=1;i<N+1;i++) sb.append(S[i]).append(i%20==0 ? '\n' : ' ');
        System.out.print(sb.toString());
	}
	static int Int(String s) {return Integer.parseInt(s);}
}
