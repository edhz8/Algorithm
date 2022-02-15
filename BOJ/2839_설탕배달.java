package algorithm.d0215;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class boj_2839 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int min = -1;
		for(int i=N/5;i>=0;i--) {
			if((N-5*i)%3==0) {
				min = i+(N-5*i)/3;
				break;
			}
		}
		System.out.print(min==-1 ? -1 : min);
	}
}
