package java_solved.BOJ;

import java.io.*;
import java.util.*;

public class BOJ1030 {

    private static int[][] grid;
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int s = Integer.parseInt(st.nextToken()); // 시간 0~10
        N = Integer.parseInt(st.nextToken()); // 나누어질 전체 크기 3~8
        int k = Integer.parseInt(st.nextToken()); // 채워질 크기 1~N-2
        int r1 = Integer.parseInt(st.nextToken()); // 출력 시작행
        int r2 = Integer.parseInt(st.nextToken()); // 출력 끝행
        int c1 = Integer.parseInt(st.nextToken()); // 출력 시작열
        int c2 = Integer.parseInt(st.nextToken()); // 출력 끝열

//        [i / N + i % N][j / N + i % N]의 값은 i ~ i+N까지의 값을 결정한다
        // i,j의 값은 그 지점을 역으로 검사하면 알 수 있다.
        grid = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if ((N - k) / 2 <= i && (N - k) / 2 <= j && i < (N + k) / 2 && j < (N + k) / 2)
                    grid[i][j] = 1;
            }
        } // N*N은 미리 초기화해둔다.

        if (s == 0) {
            System.out.println("0");
        } else {
            for (int i = r1; i <= r2; i++) {
                for (int j = c1; j <= c2; j++) {
                    System.out.print(go(i, j));
                }
                System.out.println();
            }
        }
    }

    private static int go(int i, int j) {
        if (i < N && j < N)
            return grid[i][j];

        int before = go(i / N, j / N);
        if (before == 0) {
            return go(i % N, j % N);
        } else {
            return 1;
        }
    }
}
