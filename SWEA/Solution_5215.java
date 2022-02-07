import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Solution_5215 {

	public static void main(String[] args) throws Exception{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t=1;t<=T;t++) {
        	StringTokenizer NL = new StringTokenizer(br.readLine()," ");
        	int N = Integer.parseInt(NL.nextToken()) , L = Integer.parseInt(NL.nextToken());
        	int[] W = new int[N+1];
        	int[] V = new int[N+1];
        	int[][] dp = new int[N+1][L+1];
        	for(int i=1;i<=N;i++) {
        		StringTokenizer VW = new StringTokenizer(br.readLine()," ");
        		V[i] = Integer.parseInt(VW.nextToken());
        		W[i] = Integer.parseInt(VW.nextToken());
        	}
        	for(int i=1;i<=N;i++) {
        		for(int j=1;j<=L;j++) {
        			dp[i][j] = W[i] > j ? dp[i-1][j] : Math.max(dp[i-1][j], dp[i-1][j-W[i]] + V[i]);
        		}
        	}
        	bw.append(String.format("#%d %d%n", t,dp[N][L]));
        }
        bw.flush();
        br.close();
        bw.close();
	}
}
