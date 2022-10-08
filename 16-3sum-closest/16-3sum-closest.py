class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
          if i > 0 and num[i] == num[i-1]:
            continue
          l, r = i + 1, len(num) - 1
          while l < r:
            s = num[i] + num[l] + num[r]
            if abs(s - target) < abs(result - target):
              result = s
            if s < target:
              l += 1
            elif s > target:
              r -= 1
            else:
                return result
        return result