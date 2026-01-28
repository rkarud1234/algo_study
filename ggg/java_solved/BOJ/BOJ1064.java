package java_solved.BOJ;

import java.io.*;
import java.util.*;
public class BOJ1064 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        //  xA yA xB yB xC yC
        Point[] points = new Point[3];
        for (int i = 0; i < 3; i++) {
            points[i] = new Point(parse(st.nextToken()), parse(st.nextToken()));
        }

        // 1. 세 점이 삼각형이 될 수 있는지 확인하기
        if (getSlope(points[0], points[1]) == getSlope(points[1], points[2])) {
            System.out.println("-1.0");
            return;
        }

        // 2. 각 변의 길이 계산하기
        double AB = getDistance(points[0], points[1]);
        double BC = getDistance(points[1], points[2]);
        double CA = getDistance(points[2], points[0]);
        double max = Math.max(Math.max(AB, BC), CA);
        double min = Math.min(Math.min(AB, BC), CA);

        // 3. 만들 수 있는 평행사변형 둘레 -> 두 변의 길이의 합 * 2
        double ans = (AB + BC + CA - min) * 2 - (AB + BC + CA - max) * 2;
        System.out.println(ans);

    }

    static double getSlope(Point p1, Point p2) {
        if (p2.x == p1.x)
            return 0;
        return (double) (p2.y - p1.y) / (p2.x - p1.x);
    }

    static double getDistance(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }

    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static int parse(String s) {
        return Integer.parseInt(s);
    }
}
