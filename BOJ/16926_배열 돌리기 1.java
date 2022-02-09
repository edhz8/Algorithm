package algorithm.d0209;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main_16926 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st  = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(st.nextToken()), M=Integer.parseInt(st.nextToken()) , R=Integer.parseInt(st.nextToken());
		String[][] map = new String[N][];
		for(int i=0;i<N;i++) map[i] = br.readLine().split(" ");
		for(int i=0;i<Math.min(N, M)/2;i++) {
			LinkedList<String> l = new LinkedList<>();
			int a,b,c,d;
			for(a=i;a<N-i;a++) l.offer(map[a][i]);a--;
			for(b=i+1;b<M-i;b++) l.offer(map[a][b]);b--;
			for(c=a-1;c>i-1;c--) l.offer(map[c][b]);c++;
			for(d=b-1;d>i;d--) l.offer(map[c][d]);d++;
			Collections.rotate(l,R%l.size());
			for(a=i;a<N-i;a++) map[a][i] = l.poll();a--;
			for(b=i+1;b<M-i;b++) map[a][b] = l.poll();b--;
			for(c=a-1;c>i-1;c--) map[c][b] = l.poll();c++;
			for(d=b-1;d>i;d--) map[c][d] = l.poll();d++;
		}
		for(int i=0;i<N;i++) for(int j=0;j<M;j++) sb.append(map[i][j]).append(j==M-1 ? '\n' : ' ');
		System.out.println(sb.toString());
	}
}
