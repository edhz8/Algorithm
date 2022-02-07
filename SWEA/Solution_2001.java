import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution_2001 {

	public static void main(String[] args) throws Exception{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t=1;t<=T;t++) {
        	String[] nm = br.readLine().split(" ");
        	int N = Integer.parseInt(nm[0]), M = Integer.parseInt(nm[1]);
        	int[][] map = new int[N][N];
        	int max = -1;
        	for(int i=0;i<N;i++) {
        		StringTokenizer st = new StringTokenizer(br.readLine());
        		for(int j=0;j<N;j++) {
        			map[i][j] = Integer.parseInt(st.nextToken());
        			if(i>0) map[i][j] += map[i-1][j];
        			if(j>0) map[i][j] += map[i][j-1];
        			if(i>0 && j>0) map[i][j] -= map[i-1][j-1];
        			if(i>=M-1 && j>=M-1) {
        				int current = map[i][j];
        				if(i-M >= 0) current -= map[i-M][j];
        				if(j-M >= 0) current -= map[i][j-M];
        				if(i-M >= 0 && j-M >= 0) current += map[i-M][j-M];
        				max = max > current ? max : current;
        			}
        		}
        	}
        	bw.write(String.format("#%d %d%n", t,max));
        }
        bw.flush();
		br.close();
		bw.close();

	}

}