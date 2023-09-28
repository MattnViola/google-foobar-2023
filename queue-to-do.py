def solution(start, length):
    
    # Xor sums have a pattern of 4
    def xorRange(left, right):
        if left != 0:
            left = xorRange(0, left - 1)

        mod = right % 4
        if mod == 1:
            right = 1
        elif mod == 2:
            right += 1
        elif mod == 3:
            right = 0
        
        return left ^ right
        
    num = start
    k = length
    checksum = 0
    while length > 0:
        right = num + length - 1
        if right > 2000000000:
            return checksum ^ xorRange(num, 2000000000)
        checksum ^= xorRange(num, right) 
        num += k
        length -= 1

    return checksum

print(solution(17, 4))