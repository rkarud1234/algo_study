package java_solved.BOJ;

import java.io.*;
import java.util.*;

public class BOJ1024 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        for (int i = L; i <= 100; i++) {
            int q = N / i; // 몫
            int r = N % i; // 나머지

            if (i % 2 == 1 && r == 0) {
                // 나누었을 때 나머지가 0인 경우 -> i가 짝수면 안됨. 홀수면 됨
                print(q - (i / 2), q + (i / 2));
                return;
            } else if (i % 2 == 0 && r != 0 && N % (2 * q + 1) == 0) {
                // 나누었을 때 나머지가 있는 경우 -> i가 홀수면 안됨. 짝수면 됨
                // 짝수면서 몫 +1 했을 떄의 값으로 나누어떨어져야 함
                print(q - (i / 2) + 1, q + (i / 2));
                return;
            }
        }
        System.out.println("-1");
    }

    private static void print(int start, int end) {
        if (start < 0 || end - start + 1 > 100) {
            System.out.println("-1");
            return;
        }

        for (int i = start; i <= end; i++) {
            System.out.print(i + " ");
        }
    }
}
