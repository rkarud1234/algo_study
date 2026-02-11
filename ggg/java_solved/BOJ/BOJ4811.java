package java_solved.BOJ;

import java.io.*;

public class BOJ4811 {
    private static long[][] pills;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        pills = new long[31][31];
        go(30, 0);

        int N;
        while ((N = parse(br.readLine())) != 0) {
            System.out.println(pills[N][0]);
        }

    }

    private static long go(int W, int H) {
        if (H < 0 || W < 0) return 0;
        if (W == 0) return 1;

        if (pills[W][H] == 0)
            pills[W][H] = go(W, H - 1) + go(W - 1, H + 1);

        return pills[W][H];
    }

    private static int parse(String s) {
        return Integer.parseInt(s);
    }
}
