package java_solved;

import java.io.*;
import java.util.*;

public class BOJ16929 {
    private static int n, m;
    private static char[][] map;
    private static boolean[][] visit;
    private static boolean finished;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[n][m];
        visit = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            map[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visit[i][j])
                    continue;

                go(new Point(-1, -1), new Point(i, j));
            }
        }

        System.out.println(finished ? "Yes" : "No");
    }

    private static final int[][] move = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    private static void go(Point prev, Point now) {
        if (finished) {
            return;
        }

        visit[now.i][now.j] = true;

        for (int d = 0; d < 4; d++) {
            int ni = now.i + move[d][0];
            int nj = now.j + move[d][1];

            Point next = new Point(ni, nj);
            if (!isValid(next) || map[now.i][now.j] != map[ni][nj] || (ni == prev.i && nj == prev.j)) // 유효하지 않은 인덱스이거나, 문자가 다르거나, 직전의 점인 경우 Pass
                continue;

            if (visit[ni][nj]) {
                // 이미 방문한 점을 또 만났다 -> 사이클
                finished = true;
                return;
            } else {
                // 아닌 경우엔 dfs 진행
                go(now, next);
            }

        }
    }

    private static boolean isValid(Point p) {
        return p.i >= 0 && p.j >= 0 && p.i < n && p.j < m;
    }

    private static class Point {
        int i, j;

        Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
