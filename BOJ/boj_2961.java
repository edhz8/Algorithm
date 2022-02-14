package algorithm.d0214;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2961 {
	static int min;
	static int N;
	static int[] sour,bitter;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		min = Integer.MAX_VALUE;
		sour = new int[N];
		bitter = new int[N];
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			sour[i] = Integer.parseInt(st.nextToken());
			bitter[i] = Integer.parseInt(st.nextToken());
		}
		
		rec(0,0);
		System.out.println(min);

	}
	public static void rec(int flag,int cnt) {
		if(cnt == N) {
			if(flag==0) return;
			int s=1,b=0;
			for(int i=0;i<N;i++) {
				if((flag & 1<<i) != 0) {
					s*=sour[i];
					b+=bitter[i];
				}
			}
			min = Math.min(min, Math.abs(s-b));
			return;
		}
		rec(flag|1<<cnt,cnt+1);
		rec(flag,cnt+1);
	}
}
