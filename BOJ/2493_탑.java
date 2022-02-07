package algorithm.d0207;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_2493 {

	public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<int[]> s = new Stack<>();
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
		for(int i=1;i<=N;i++) {
        	int cur = Integer.parseInt(st.nextToken());
        	while(!s.isEmpty()) {
        		int[] peek = s.peek();
        		if(peek[1]<cur) {
        			s.pop();
        			continue;
        		}
        		sb.append(peek[0]);
    			sb.append(' ');
    			break;
        	}
        	if(s.isEmpty()) sb.append("0 ");
        	s.push(new int[] {i,cur});
        }
		System.out.print(sb.toString());
		br.close();
	}
}
