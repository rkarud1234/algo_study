package java_solved;

import java.io.*;
import java.util.*;

public class BOJ2146 {
    private static int[][] map;
    private static int groupNo = 2, N, ans = 1000;
    private static Queue<Point> lands = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            map[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1) {
                    setGroup(new Point(i, j, groupNo));
                }
            }
        } // 대륙별로 다른 숫자로 그룹화하는 과정

        bfs();

        System.out.println(ans == 1000 ? 0 : ans);
    }

    private static final int[][] move = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    private static void setGroup(Point start) {
        Queue<Point> q = new LinkedList<>();
        q.offer(start);
        lands.offer(start);
        map[start.i][start.j] = groupNo;

        while (!q.isEmpty()) {
            Point now = q.poll();
            for (int d = 0; d < 4; d++) {
                int ni = now.i + move[d][0];
                int nj = now.j + move[d][1];

                Point next = new Point(ni, nj, groupNo);
                if (!isValid(ni, nj) || map[ni][nj] != 1)
                    continue;

                map[next.i][next.j] = groupNo;
                q.offer(next);
                lands.offer(next);
            }
        }
        groupNo++;
    }

    private static void bfs() {
        int[][] dist = new int[N][N];

        while (!lands.isEmpty()) {
            int size = lands.size();
            for (int s = 0; s < size; s++) {
                Point now = lands.poll();
                for (int d = 0; d < 4; d++) {
                    int ni = now.i + move[d][0];
                    int nj = now.j + move[d][1];

                    if (!isValid(ni, nj))
                        continue;

                    Point next = new Point(ni, nj, now.groupNo);
                    if (now.groupNo == map[ni][nj])
                        continue;

                    if (map[ni][nj] == 0) {
                        // 바다면 그대로 진행
                        lands.offer(next);
                        dist[ni][nj] = dist[now.i][now.j] + 1;
                        map[ni][nj] = now.groupNo;
                    } else {
                        // 그룹이 다른 땅을 만났다
                        ans = Math.min(ans, dist[now.i][now.j] + dist[ni][nj]);
                    }
                }
            }
        }
    }

    private static boolean isValid(int i, int j) {
        return i >= 0 && j >= 0 && i < N && j < N;
    }

    private static class Point {
        int i, j, groupNo;

        Point(int i, int j, int groupNo) {
            this.i = i;
            this.j = j;
            this.groupNo = groupNo;
        }
    }
}
