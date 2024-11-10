package Intervals;
import java.util.Arrays;

public class removeOverlapIntervals {
    public static void main(String[] args) {
        int[][] intervals = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
        System.out.println(eraseOverlapIntervals(intervals));
    }

    // doesn't pass all test cases
    public static int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }

        // Sort intervals by end time
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        int count = 0;
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                count++;
            } else {
                end = intervals[i][1];
            }
        }

        return count;
    }

    public static int eraseOverlapIntervals2(int[][] intervals) {
        if (intervals.length == 0) return 0;

        Arrays.sort(intervals, (a, b) -> a[1] == b[1] ? b[0] - a[0] : a[1] - b[1]);

        int minErase = 0;
        int prevEnd = Integer.MIN_VALUE;

        for (int[] interval : intervals) {
            if (interval[0] < prevEnd) {
                minErase++;
            } else {
                prevEnd = interval[1];
            }
        }

        return minErase;
    }
}


