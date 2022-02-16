package algorithm.d0216;

import java.io.*;
import java.util.*;

public class Solution_5644 {
	static int[] dx = {-1,0,1,0}, dy= {0,1,0,-1};
	static int[][] map;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			st = new StringTokenizer(br.readLine());
			int ans=0,M=Integer.parseInt(st.nextToken()),A=Integer.parseInt(st.nextToken());
			int [] AM = new int[M],BM = new int[M],ps = new int[A];
			map = new int[10][10];
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<M;i++) AM[i] = Integer.parseInt(st.nextToken())-1;
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<M;i++) BM[i] = Integer.parseInt(st.nextToken())-1;
			for(int i=0;i<A;i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken()),y= Integer.parseInt(st.nextToken()),c= Integer.parseInt(st.nextToken()),p= Integer.parseInt(st.nextToken());
				maskBC(y-1,x-1,i,0,c);
				ps[i] = p;
			}
			int ax=0,ay=0,bx=9,by=9;
			for(int sec=0;sec<=M;sec++) {
				if(sec!=0) {
					int ad, bd;
					if((ad = AM[sec-1]) != -1) {						
						ax += dx[ad];
						ay += dy[ad];
					}
					if((bd = BM[sec-1]) != -1) {						
						bx += dx[bd];
						by += dy[bd];
					}
				}
				LinkedList<int[]> as = new LinkedList<>(),bs = new LinkedList<>();
				as.add(new int[] {-1,0});
				bs.add(new int[] {-2,0});
				for(int i=0;i<A;i++) {
					if(isOne(map[ax][ay],i)) as.add(new int[] {i,ps[i]});
					if(isOne(map[bx][by],i)) bs.add(new int[] {i,ps[i]});
				}
				as.sort((int[] a, int[] b) -> b[1]-a[1]);
				bs.sort((int[] a, int[] b) -> b[1]-a[1]);
				if(as.get(0)[0] == bs.get(0)[0]) ans += (as.get(1)[1] >= bs.get(1)[1]) ? as.get(1)[1] + bs.get(0)[1] : as.get(0)[1] + bs.get(1)[1];
				else ans += (as.get(0)[1] + bs.get(0)[1]);
			}
			sb.append('#').append(t).append(' ').append(ans).append('\n');
		}
		System.out.println(sb.toString());
	}
	
	public static void maskBC(int x,int y,int num,int cur,int end) {
		if(cur > end) return;
		map[x][y] |= (1<<num);
		for(int i=0;i<4;i++) {
			int nx = x+dx[i],ny = y+dy[i];
			if(nx<0 || nx>=10 || ny<0 || ny>=10) continue;
			maskBC(nx,ny,num,cur+1,end);
		}
	}
	public static boolean isOne(int target,int num) {
		return ((target & (1<<num)) != 0); //1이면 true 0이면 false
	}
}