from collections import defaultdict


def max_points_in_line(points: list):
    max_n = 1
    for i in range(len(points)):
        slopes = defaultdict(int)
        for j in range(i + 1, len(points)):
            slope = float("inf")
            if points[i][0] != points[j][0]:
                slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
            slopes[slope] += 1
            max_n = max(max_n, slopes[slope] + 1)
    return max_n


def main():
    points = [[1, 1], [2, 2], [3, 3], [4, 5], [2, 3], [2, 5], [2, 6]]
    result = max_points_in_line(points)
    print(result)


if __name__ == "__main__":
    main()
