import math

s = 45 # 10**10
r1 = int((s/2)**0.5)
r2 = int(s**0.5)
ans = 0
sol = set()

def _sign(x):
    return 1 if x == 0 else 2

def sign(x, y, z):
    return _sign(x) * _sign(y) * _sign(z)

def perm(x, y, z):
    n = len(set([x, y, z]))
    return 6 // math.factorial(4-n)

def dup(x, y, z):
    return sign(x, y, z) * perm(x, y, z)

# u<=v<, w is independent
for u in range(r2+1):
    for v in range(u, r2+1):
        wq = s - u**2 - v**2
        if wq >= 0:
            w_ = wq**0.5
            w = int(w_)
            if w == w_:
                x = abs(w**2 - u**2 -v**2)
                y = 2 * u * w
                z = 2 * v * w
                tpl = tuple(sorted([x, y, z]))
                if tpl not in sol:
                    ans += dup(*tpl) * (x + y + z)
                    sol.add(tpl)

print(ans, len(sol))
for i in sorted(sol):
    print(*i)

# 0 0 45
# 0 27 36
# 5 20 40
# 13 16 40
# 16 20 37
