class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(growTime)
        indices = sorted(range(n), key=lambda x: -growTime[x])
        plant_sum = mx = 0
        for i in indices:
            time = plant_sum + plantTime[i] + growTime[i]
            mx = max(mx, time)
            plant_sum += plantTime[i]
        return mx