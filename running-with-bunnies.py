from itertools import permutations
def solution(times, times_limit):
    rowLen = len(times)
    # Function to traverse routes
    def traverse(bunnies):
        # Add the start and the end
        route = [0]
        route.extend(bunnies)
        route.append(-1)
        
        time = 0
        for i in range(1, len(route)):
            x, y = route[i-1], route[i]
            time += times[x][y]
        if time <= times_limit:
            bunnies.sort()
            return [bun - 1 for bun in bunnies]
            
    # floyd-warshal
    for k in range(rowLen):
        for i in range(rowLen):
            for j in range(rowLen):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]
                    
    # If there's a negative cycle, one main diagonal will be negative
    for i in range(rowLen):
        if times[i][i] < 0:
            return [j for j in range(rowLen - 1)]
            
                    
    # Try every permutation, greedy.
    perms = []
    for i in range(rowLen - 2, 0, -1):
        for buns in permutations(range(1, rowLen - 1), i):
            res = traverse(list(buns))
            if res:
                return res
    
        
        
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))