package java_solved.BOJ;

import java.io.*;
import java.util.*;

public class BOJ25330 {

    private static int N, ans;
    private static int[][] village;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // 마을 수
        int K = Integer.parseInt(st.nextToken()); // 시루의 초기 체력

        int[] cost = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] reward = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        village = new int[N][2];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            village[i][0] = cost[i];    // 몬스터 체력
            village[i][1] = reward[i];  // 보상
        }

        // 조합을 순회하면서 모든 경우의 수를 체크한다.
        // 중간에 시루의 체력으로 무찌를 수 없는 몬스터만 남게되면 순회를 종료해야하기 때문에 재귀를 이용해 풀이한다. -> 이 경우를 위해서 사전에 몬스터 배열을 정렬한다.
        Arrays.sort(village, Comparator.comparingInt(o -> o[0]));

        go(K, 0, 0);
        System.out.println(ans);
    }

    private static void go(int health, int saved, int damage) {
        ans = Math.max(ans, saved);

        int remain = 0;
        for (int i = 0; i < N; i++) {
            if (!visited[i] && damage + village[i][0] <= health) {
                remain += village[i][1];
            }
        }
        if (saved + remain <= ans)
            return;

        // 전수조사
        for (int i = 0; i < N; i++) {
            if (visited[i]) continue;
            if (health - village[i][0] - damage < 0)
                return;
            visited[i] = true;
            go(health - village[i][0] - damage, saved + village[i][1], damage + village[i][0]);
            visited[i] = false;
        }
    }
}
