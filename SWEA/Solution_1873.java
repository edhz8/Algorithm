import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution_1873 {

	public static void main(String[] args) throws Exception{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int[] dx = {-1,0,1,0};
        int[] dy = {0,1,0,-1};
        ArrayList<Character> me = new ArrayList<>(Arrays.asList('^','>','v','<'));
        ArrayList<Character> cmd = new ArrayList<>(Arrays.asList('U','R','D','L'));
        int direction = 0;
        int cx=0,cy=0;
        for(int t=1;t<=T;t++) {
        	String[] length = br.readLine().split(" ");
        	int H = Integer.parseInt(length[0]);
        	int W = Integer.parseInt(length[1]);
        	char[][] map = new char[H][];
        	for(int i=0;i<H;i++) {
        		map[i] = br.readLine().toCharArray();
        		for(int j=0;j<W;j++) {
        			if(me.indexOf(map[i][j]) != -1) {
        				direction = me.indexOf(map[i][j]);
        				cx = i;
        				cy = j;
        			}
        		}
        		
        	}
        	br.readLine();
        	char[] commands = br.readLine().toCharArray();
        	for(char command : commands) {
        		if(command == 'S') {
        			int nx = cx;
        			int ny = cy;
        			while(true) {
        				nx += dx[direction];
        				ny += dy[direction];
        				if(nx<0 || nx>=H || ny<0 || ny>=W || map[nx][ny]=='#') break;
        				if(map[nx][ny] == '*') {
        					map[nx][ny] = '.';
        					break;
        				}        				
        			}
        		} else {
        			direction = cmd.indexOf(command);
        			int nx = cx + dx[direction];
    				int ny = cy + dy[direction];
    				if(nx<0 || nx>=H || ny<0 || ny>=W || map[nx][ny] != '.') {
    					map[cx][cy] = me.get(direction);
    					continue;
    				}
    				map[cx][cy] = '.';
    				map[nx][ny] = me.get(direction);
        			cx = nx;
        			cy = ny;
        		}
        		
        	}
        	bw.append(String.format("#%d ", t));
        	for(int i=0;i<H;i++) {
        		for(int j=0;j<W;j++) {
        			bw.append(map[i][j]);
        		}
        		bw.append('\n');
        	}
        }
        bw.flush();
		br.close();
		bw.close();
	}

}