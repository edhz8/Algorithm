import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution_1208 {

	public static void main(String[] args) throws Exception{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int t=1;t<=10;t++) {
			int dump = Integer.parseInt(br.readLine());
			int[] cnt = new int[101];	
			//cnt배열은 높이별로 몇개가 있는지를 나타냅니다. ex) cnt[80]이 2라면 높이가 80인 기둥이 2개라는 뜻입니다.
			StringTokenizer st = new StringTokenizer(br.readLine());
			while(st.hasMoreTokens()) {
				cnt[Integer.parseInt(st.nextToken())]++;
			}
			while(dump --> 0) {
				int start=1,end=100;
				while(true) {
					if(cnt[end]>0) {
						cnt[end]--;
						cnt[end-1]++;
						break;
					}
					end--;
				}
				while(true) {
					if(cnt[start]>0) {
						cnt[start]--;
						cnt[start+1]++;
						break;
					}
					start++;
				}
			}
			int min=0,max=0;
			for(int i=1;i<101;i++) {
				if(cnt[i]>0) {
					min = i;
					break;
				}
			}
			for(int i=100;i>0;i--) {
				if(cnt[i]>0) {
					max = i;
					break;
				}
			}
			bw.append(String.format("#%d %d%n",t,max-min));
		}
		bw.flush();
		br.close();
		bw.close();
	}
}