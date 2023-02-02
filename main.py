def geron(s):
    a, b, c = s[0], s[1], s[2]
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
n = len(sides)
max_sides = 0, 0, 0
max_s = 0

for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != k and j != k:
                    ch_sides = list(sorted([sides[i], sides[j], sides[k]]))
                    if ch_sides[0] + ch_sides[1] > ch_sides[2]:
                        r = geron(ch_sides)
                        if max_s < r:
                            max_s = r
                            max_sides = ch_sides
print(max_sides, max_s)
