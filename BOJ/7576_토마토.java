package algorithm.d0225;

import java.awt.Point;
import java.io.*;
import java.util.*;

public class boj_7576 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int[] dx = {-1,0,1,0}, dy = {0,1,0,-1};
        st = new StringTokenizer(br.readLine());
        int C = Int(st.nextToken()), R = Int(st.nextToken()),green=0,max = Integer.MIN_VALUE;
        int[][] graph = new int[R][C], date = new int[R][C];
        Deque<Point> q = new ArrayDeque<>();
        for(int i=0;i<R;i++) {
        	st = new StringTokenizer(br.readLine());
        	for(int j=0;j<C;j++) {
        		int input = Int(st.nextToken());
        		if(input == 0) green++;
        		else if(input == 1) q.add(new Point(i,j));
        		graph[i][j] = input;
        	}
        }
        if(!q.isEmpty() && green==0) {
        	System.out.print(0);
        	return;
        }
        while(!q.isEmpty()) {
        	Point p = q.pop();
        	int x = p.x, y = p.y;
        	for(int d=0;d<4;d++) {
        		int nx = x+dx[d], ny = y+dy[d];
        		if(nx<0 || nx>=R || ny<0 || ny>=C || graph[nx][ny]!=0) continue;
        		graph[nx][ny] = 1;
        		date[nx][ny] = date[x][y] + 1;
        		green--;
        		max = date[nx][ny];
        		if(green==0) {
        			System.out.print(max);
        			return;
        		}
        		q.add(new Point(nx,ny));
        	}
        }
        System.out.print(-1);
	}
	static int Int(String s) { return Integer.parseInt(s);}
}
