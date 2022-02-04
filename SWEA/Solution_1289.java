public class Solution_1289 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		for(int t=0;t<testCase;t++) {
			int ret = 0;
			char cur = '0';
			char[] chars = sc.next().toCharArray();
			for(char c : chars) {
				if(c != cur) {
					cur = c;
					ret++;
				}
			}
			System.out.printf("#%d %d%n",t+1,ret);
		}
	}

}