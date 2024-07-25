
class Solution:

    def findMinDiff(self, A, N, M):
        if M > N:
            return -1

        A.sort()
        min_diff = A[M - 1] - A[0]
        j = M - 1
        for i in range(1, N - M + 1):
            while A[i + M - 1] - A[i] < A[j] - A[j - M]:
                j = i
            min_diff = min(min_diff, A[i + M - 1] - A[i])

        return min_diff
