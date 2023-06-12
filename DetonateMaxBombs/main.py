class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        graph = {}
        n, max_bombs = len(bombs), 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i] += [j]

        def dfs(self, i, visited):
            for parent in graph[i]:
                for child in parent:
                    pass

        for i in range(n):
            visited = [i]
            dfs(i, visited)


def main():
    bombs = [[2,1,3],[6,1,4]]
    sol = Solution()
    sol.maximumDetonation(bombs)

if __name__ == "__main__":
    main()