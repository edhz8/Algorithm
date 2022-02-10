package algorithm.d0209;

import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Solution_1210 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for(int t=1;t<=10;t++) {
			br.readLine();
			String[][] map = new String[100][];
			for(int i=0;i<100;i++) map[i] = br.readLine().split(" ");
			int y=0;
			for(int j=0;j<100;j++) {
				if(map[99][j].charAt(0) == '2') {
					y=j;
					break;
				}
			}
			for(int x=98;x>=0;x--) {
				boolean GO = true;
				while(y-1>=0 && map[x][y-1].charAt(0) == '1') {
					GO = false;
					y--;
				}
				while(GO && y+1<100 && map[x][y+1].charAt(0) == '1') y++;
			}
			sb.append('#').append(t).append(' ').append(y).append('\n');
		}
		System.out.println(sb.toString());
	}
}
