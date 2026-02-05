package java_solved.BOJ;

import java.io.*;
import java.util.*;

public class BOJ1080 {
    private static int[][] xor;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] A = new int[N][M];
        int[][] B = new int[N][M];
        xor = new int[N][M];
        for (int i = 0; i < N; i++)
            A[i] = br.readLine().chars().map(c -> c - '0').toArray();
        for (int i = 0; i < N; i++)
            B[i] = br.readLine().chars().map(c -> c - '0').toArray();

        // 1. 두 행렬에 XOR 연산을 수행한다. -> N*M, 최대 크기 = 50*50 = 2500
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                xor[i][j] = A[i][j] ^ B[i][j];
            }
        }


        // 2. (1)의 결과 행렬을 탐색하면서 1을 발견하면 3*3 칸의 뒤집기를 수행한다. -> N*M = 2500
        int ans = 0;
        outer:
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (xor[i][j] == 1) {
                    if (i + 2 >= N || j + 2 >= M) {
                        ans = -1;
                        break outer;
                    }
                    flip(i, j);
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }

    private static void flip(int si, int sj) {
        for (int i = si; i < si + 3; i++) {
            for (int j = sj; j < sj + 3; j++) {
                xor[i][j] ^= 1;
            }
        }
    }
}
