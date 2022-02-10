package algorithm.d0209;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class boj_2605 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		LinkedList<Integer> l = new LinkedList<>();
		for(int i=1;st.hasMoreTokens();i++) l.add(Integer.parseInt(st.nextToken()),i);
		while(!l.isEmpty()) sb.append(l.pollLast()).append(' ');
		System.out.println(sb.toString());
	}
}
