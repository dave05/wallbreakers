class Solution:
    def distributeCandies(self, candies):
        candies_types=set(candies)
        return min(len(candies_types),len(candies)//2)

        """
        :type candies: List[int]
        :rtype: int
        """

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            candies = stringToIntegerList(line);

            ret = Solution().distributeCandies(candies)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
