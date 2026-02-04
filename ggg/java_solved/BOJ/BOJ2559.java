package java_solved.BOJ;

import java.io.*;
import java.util.*;

public class BOJ2559 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = parse(st.nextToken());
        int K = parse(st.nextToken());
        int[] arr = new int[N];

        int sum = 0;
        int ans = -10000000;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = parse(st.nextToken());
            if (i < K) {
                sum += arr[i];
            } else {
                ans = Math.max(ans, sum);
                sum = sum - arr[i - K] + arr[i];
            }
        }
        System.out.println(Math.max(ans, sum));
    }

    private static int parse(String s) {
        return Integer.parseInt(s);
    }

}
