def loopCheck(n1, n2):
    if n1 == n2:
        return False
    # sum is odd (odd and even num)
    if (n1 + n2) % 2 == 1:
        return True
    # nums will end up even, so if goal is odd, impossible.
    if ((n1 + n2) // 2) % 2 == 1:
        return True

    while n1 != n2:
        if n1 < n2:
            n1, n2 = n2, n1
            
        # If after dividing by gcd is odd, then its an infinite loop.
        if (n1 + n2) % 2 == 1:
            return True
            
        # Find the GCD for efficiency
        g1, g2 = n1, n2
        while g2:
            g1, g2 = g2, g1 % g2
        
        # Divide them by gcd.
        n1, n2 = n1 // g1, n2 // g1
        n1 -= n2
        n2 *= 2
        
    return False

def best_match(index, pairs, matched, visited):
    for i in range(1, len(pairs[index])):
        pair = pairs[index][i]
        if pair in visited:
            continue
        visited.add(pair)
        if pair not in matched or best_match(matched[pair], pairs, matched, visited):
            matched[pair] = index
            return True
    return False
    
def solution(banana_list):
    pairs = [[i] for i in range(len(banana_list))]
    for i in range(len(banana_list)):
        for j in range(i + 1, len(banana_list)):
            if loopCheck(banana_list[i], banana_list[j]):
                pairs[i].append(j)
                pairs[j].append(i)
        
    matched = {}
    res = 0
    for i in range(len(pairs)):
        visited = set()
        if best_match(i, pairs, matched, visited):
            res += 1
    
    if res % 2 == 1:
        res -= 1
    return len(banana_list) - res

print(solution([1073741823,1073741823,1073741823,1073741823,1232134,1073741823,23534, 1073741823]))
        
    
    