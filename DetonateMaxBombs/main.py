class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        bombsRange = range(len(bombs))
        maxBombs = 0

        
        for firstBombIdx in bombsRange:
            stack = []
            x1, y1, r1 = bombs[firstBombIdx]

            for secondBombIdx in bombsRange:
                if firstBombIdx == secondBombIdx:
                    continue

                x2, y2, r2 = bombs[secondBombIdx]
                dist = self.distBetween(x1, y2, x2, y2)
                within = dist <= r1

                if within:
                    stack.append(secondBombIdx)

    def distBetween(self, x1, y1, x2, y2):
        den = (x2 - x1)
        if den == 0:
            return 0
        return abs((y2 - y1)/den)
    
def main():
    bombs = [[2,1,3],[6,1,4]]
    sol = Solution()
    sol.maximumDetonation(bombs)

if __name__ == "__main__":
    main()