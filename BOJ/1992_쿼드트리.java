package algorithm.d0216;

import java.io.*;

public class Main {
	static int N;
	static char[][] graph;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		graph = new char[N][];
		for(int i=0;i<N;i++) graph[i] = br.readLine().toCharArray();
		rec(0,0,N);
		System.out.print(sb.toString());
	}
	public static void rec(int x,int y,int n) {
		char cur = graph[x][y];
		for(int i=x;i<x+n;i++) {
			for(int j=y;j<y+n;j++) {
				if(cur != graph[i][j]) {
					cur='N';
					break;
				}
			}
		}
		if (cur == 'N') {
			sb.append('(');
			n/=2;
			rec(x,y,n);
			rec(x,y+n,n);
			rec(x+n,y,n);
			rec(x+n,y+n,n);
			sb.append(')');
		}
		else sb.append(cur);	
	}
}
