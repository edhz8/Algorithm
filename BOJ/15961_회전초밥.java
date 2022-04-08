package algorithm.d0405;

import java.io.*;
import java.util.*;

public class jungol_2577 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N=Int(st.nextToken()),d=Int(st.nextToken()),k=Int(st.nextToken()),c=Int(st.nextToken()),sushi[]=new int[N],visit[]=new int[d + 1],total=0,max=0;
		for (int i = 0; i < N; i++) sushi[i] = Int(br.readLine());
		for (int i = 0; i < k; i++) {
			if (visit[sushi[i]] == 0) total++;
			visit[sushi[i]]++;
		}
		max = total;
		for (int i = 1; i < N; i++) {
			if (max <= total) max = visit[c] == 0 ? total + 1 : total;
			visit[sushi[i-1]]--;
			if (visit[sushi[i-1]] == 0) total--;
			if (visit[sushi[(i+k-1)%N]] == 0) total++;
			visit[sushi[(i + k - 1) % N]]++;
		}
		System.out.print(max);
	}
	static int Int(String s) {return Integer.parseInt(s);}
}