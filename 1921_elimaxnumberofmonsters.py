class Solution(object):
    def eliminateMaximum(self, dist, speed):
        n = len(dist)
        arrival_times = [float('inf')] * n

        for i in range(n):
            arrival_times[i] = (dist[i] + speed[i] - 1) // speed[i]  # Calculate arrival time for each monster

        arrival_times.sort()  # Sort monsters by arrival time
        eliminated = 0

        for i in range(n):
            if i >= arrival_times[i]:  # If a monster arrives at or after the time the weapon charges, you lose
                return eliminated
            eliminated += 1

        return eliminated
