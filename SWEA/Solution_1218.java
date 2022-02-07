import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution_1218 {

	public static void main(String[] args) throws Exception{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String brs = "([{<)]}>";
        for(int t=1;t<=10;t++) {
        	br.readLine();
        	int[] cnts = {0,0,0,0};
        	char[] cs = br.readLine().toCharArray();
        	boolean NO = false;
        	for(char c : cs) {
        		int i = brs.indexOf(c);
        		cnts[i%4] += i/4>0 ? -1 : 1;
        		if(cnts[i%4]<0) {
        			NO = true;
        			break;
        		}
        	}
        	for(int i : cnts) {
        		if(i!=0) {
        			NO = true;
        			break;
        		}
        	}
        	bw.write(String.format("#%d %d%n",t,NO ? 0 : 1));
        }
        bw.flush();
        br.close();
        bw.close();
	}
}
