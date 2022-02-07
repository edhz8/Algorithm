import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution_2805 {

	public static void main(String[] args) throws Exception {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t=1;t<=T;t++) {
        	int N = Integer.parseInt(br.readLine());
        	int sum = 0;
        	int from = N/2+1 , to = N/2-1;
        	for(int i=0;i<N;i++) {
        		String current = br.readLine();
        		if(i<=N/2) {
        			from --;
        			to ++;
        		} else {
        			from ++;
        			to --;
        		}
        		for(int j=from;j<=to;j++) {
        			sum += (current.charAt(j) - '0');
        		}
        	}
        	bw.append(String.format("#%d %d%n", t,sum));
        }
        bw.flush();
		br.close();
		bw.close();
	}

}