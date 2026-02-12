package java_solved.BOJ;

import java.util.*;

public class BOJ9527 {
    private static long[] sum;

    public static void main(String[] args) {
        long[] dp = new long[60]; // 2^(i-1) ~ 2^i 까지의 1의개수의 함
        sum = new long[60]; // 0~2^i - 1 까지의 1의개수의 합 (누적합)
        dp[1] = 1;
        sum[1] = 1;

        for (int i = 2; i < dp.length; i++) {
            dp[i] = sum[i - 1] + (long) Math.pow(2, i - 1);
            sum[i] = sum[i - 1] + dp[i];
        }

        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong() - 1;
        long B = sc.nextLong();
        System.out.println(recur(B, getExp(B)) - recur(A, getExp(A)));
    }

    private static int getExp(long num) {
        return 64 - Long.numberOfLeadingZeros(num);
    }

    private static long recur(long num, int exp) {
        if (num == 0) return 0;
        if (num == 1) return 1;
        long next = num - (1L << (exp - 1));
        if (next == 0)
            return sum[exp - 1] + 1;
        else
            return sum[exp - 1] + recur(next, getExp(next)) + next + 1;
    }
}
