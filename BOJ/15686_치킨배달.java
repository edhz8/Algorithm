package algorithm.d0223;

import java.awt.Point;
import java.io.*;
import java.util.*;

public class boj_15686 {
	static int N,M,ans,HS,CS;
	static int[][] dist;
	static int[] nums;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Int(st.nextToken()); M = Int(st.nextToken());ans=Integer.MAX_VALUE;
		nums = new int[M];
		LinkedList<Point> home = new LinkedList<>(),chi = new LinkedList<>();
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<N;j++) {
				int num = Int(st.nextToken());
				if(num == 1) home.add(new Point(i,j));
				else if(num == 2) chi.add(new Point(i,j));
			}
		}
		HS = home.size();CS = chi.size();
		dist = new int[HS][CS];
		for(int i=0;i<HS;i++) for(int j=0;j<CS;j++) dist[i][j] = Math.abs(home.get(i).x - chi.get(j).x)+Math.abs(home.get(i).y - chi.get(j).y);
		rec(0,0);
		System.out.print(ans);
	}
	static int Int(String s) {return Integer.parseInt(s);}
	static void rec(int start,int cnt) {
		if(cnt == M) {
			int ct = 0;
			for(int i=0;i<HS;i++) {
				int ch = Integer.MAX_VALUE;
				for(int j:nums) ch = Math.min(ch,dist[i][j]);
				ct += ch;
			}
			ans = Math.min(ans, ct);
			return;
		}
		for(int i=start;i<CS;i++) {
			nums[cnt] = i;
			rec(i+1,cnt+1);
		}
	}
}
