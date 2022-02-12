package algorithm.d0211;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class boj_16935 {
	static String[][] map;
	static int N,M,R;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		map = new String[N][M];
		for(int i=0;i<N;i++) {			
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<M;j++) map[i][j] = st.nextToken();
		}
		st = new StringTokenizer(br.readLine());
		while(st.hasMoreTokens()) {
			switch(Integer.parseInt(st.nextToken())) {
			case 1 : one();break;
			case 2 : two();break;
			case 3 : three();break;
			case 4 : four();break;
			case 5 : five();break;
			case 6 : six();break;
			default : break;
			}
		}
		for(int i=0;i<N;i++) for(int j=0;j<M;j++) sb.append(map[i][j]).append(j==M-1 ? '\n':' ');
		System.out.print(sb.toString());
	}
	public static void one() {
		for(int i=0;i<M;i++) {
			LinkedList<String> tmp = new LinkedList<>();
			for(int j=0;j<N;j++) tmp.add(map[j][i]);
			for(int j=0;j<N;j++) map[j][i] = tmp.pollLast();			
		}
	}
	public static void two() {
		for(int i=0;i<N;i++) {
			LinkedList<String> tmp = new LinkedList<>();
			for(int j=0;j<M;j++) tmp.add(map[i][j]);
			for(int j=0;j<M;j++) map[i][j] = tmp.pollLast();			
		}
	}
	public static void three() {
		String[][] nmap = new String[M][N];
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				nmap[j][N-1-i] = map[i][j];
			}
		}
		map=nmap;
		int temp = M;
		M = N;
		N = temp;
	}
	public static void four() {
		String[][] nmap = new String[M][N];
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				nmap[M-1-j][i] = map[i][j];
			}
		}
		map=nmap;
		int temp = M;
		M = N;
		N = temp;
	}
	public static void five() {
		int n = N/2,m=M/2;
		String[][] nmap = new String[N][M];
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				if(i<n && j<m) nmap[i][j+m] = map[i][j];
				else if(i<n && j>=m) nmap[i+n][j] = map[i][j];
				else if(i>=n && j>=m) nmap[i][j-m] = map[i][j];
				else if(i>=n && j<m) nmap[i-n][j] = map[i][j];
			}
		}
		map=nmap;
	}
	public static void six() {
		int n = N/2,m=M/2;
		String[][] nmap = new String[N][M];
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				if(i<n && j<m) nmap[i+n][j] = map[i][j];
				else if(i<n && j>=m) nmap[i][j-m] = map[i][j];
				else if(i>=n && j>=m) nmap[i-n][j] = map[i][j];
				else if(i>=n && j<m) nmap[i][j+m] = map[i][j];
			}
		}
		map=nmap;
	}
}
