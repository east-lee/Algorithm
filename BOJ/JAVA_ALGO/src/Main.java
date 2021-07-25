import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int [] bead;
	static int totalCnt = 0;
	static int result = 0;
	

	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken());
		bead = new int [N];
		
		for (int i = 0 ; i < N ; i++) {
			st = new StringTokenizer(bf.readLine());
			int inputCnt = Integer.parseInt(st.nextToken());
			
			bead[i] = inputCnt;
			totalCnt += inputCnt;
		}
		
		DFS(0, -1, -1);
		
		System.out.println(result);

	}
	
	public static void DFS(int k, int before, int before_before) {
		if (k == totalCnt) {
			result ++;
		} else {
			for (int i = 0; i<N; i++) {
				if (bead[i] == 0 || before == i || before_before == i) continue;
				
				bead[i] -= 1;
				DFS(k+1,i,before);
				bead[i] += 1;
						
				
				
			}
		}
	}

}
