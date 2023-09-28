def solution(x, y):
    x, y = int(x), int(y)
    if x % 2 == 0 and y % 2 == 0:
        return 'impossible'
    
    count = 0
    while x > 1 or y > 1:
        if x < y:
            count += y // x
            y %= x
        elif y < x:
            count += x // y
            x %= y
        else:
            return 'impossible'
    return str(count - 1)

print(solution('18', '15'))