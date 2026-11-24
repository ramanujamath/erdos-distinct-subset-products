#!/usr/bin/env python3
"""
Exact verification of the finite computations in

    Ramanuja, "Third-order bounds for Erdos's distinct subset products problem".

Checks (all in exact integer / rational arithmetic, standard library only):
  * Lemma 6.2   - the block {p^3, q^3, r, r^2, p r^2, q r^2, p q} is dissociated;
  * Lemma 6.7   - the thirteen monomials on eight primes are dissociated;
  * Table 2     - the affine allocation uses each unit interval of [0, 64] once;
  * Table 3     - the largest Bernstein coefficient in each row, hence M = 20664;
  * Thm 1.3(ii) - 8 / 20664^(1/3) = (64/2583)^(1/3);
  * Prop 6.8    - the product identity b3^2 b5^2 b6 b7 b8^2 b12 b13 = p3^2 prod_{i!=3} p_i^4.

Exits with status 1 if any check fails.
"""
from fractions import Fraction as Fr
from math import comb, e
import sys

FAILED = False
def check(cond, msg):
    global FAILED
    print(("  ok    " if cond else "  FAIL  ") + msg)
    FAILED |= not cond

def dissociated(vecs):
    """True if all 2^m subset sums are distinct."""
    seen = set()
    d = len(vecs[0])
    for mask in range(1 << len(vecs)):
        s = tuple(sum(v[i] for k, v in enumerate(vecs) if mask >> k & 1) for i in range(d))
        if s in seen:
            return False
        seen.add(s)
    return True

print("Lemma 6.2")
B = [(3,0,0), (0,3,0), (0,0,1), (0,0,2), (1,0,2), (0,1,2), (1,1,0)]
check(dissociated(B), "B(p,q,r) has distinct subset products")

print("Lemma 6.7")
mons = {1:(2,5,7), 2:(2,6,8), 3:(1,5,6), 4:(1,3), 5:(2,3,8), 6:(5,7,8), 7:(2,4,5),
        8:(4,6,7), 9:(3,), 10:(4,), 11:(4,6,8), 12:(1,2,7), 13:(1,4,8)}
V = [tuple(1 if i in m else 0 for i in range(1, 9)) for m in mons.values()]
check(dissociated(V), "the thirteen monomials have distinct subset products")
E = sorted(tuple(int(c) for c in s) for s in
           ["257","268","156","238","578","245","467","468","127","148"])
check(sorted(m for m in mons.values() if len(m) == 3) == E,
      "E is exactly the set of ten cubic monomials")

print("Table 2 (allocation)")
T = """30+ 22- 46- 29+ 31+ 20- 28+ 20+
35+ 14- 60+ 36+ 39+ 15- 32+ 16-
48- 7- 59+ 8- 8+ 49- 43+ 46+
38- 13- 55+ 18- 19- 27+ 40+ 26+
33+ 16+ 55- 24+ 26- 24- 34+ 23-
41+ 10- 53- 11- 12- 42+ 44+ 38+
53+ 4+ 59- 63- 64- 2+ 58- 3+
50+ 1- 61+ 5+ 2- 56+ 49+ 52-"""
U = [[(int(x[:-1]), 1 if x[-1] == '+' else -1) for x in row.split()] for row in T.splitlines()]
ivals = sorted((a, a + b) if b > 0 else (a - 1, a) for row in U for a, b in row)
check(ivals == [(j, j + 1) for j in range(64)], "each interval [j, j+1], 0 <= j < 64, is used once")

print("Table 3 (Bernstein certificate)")
def polymul(P, Q):
    R = [Fr(0)] * (len(P) + len(Q) - 1)
    for i, a in enumerate(P):
        for j, b in enumerate(Q):
            R[i + j] += a * b
    return R
def bernstein_max(A):
    return max(sum(Fr(comb(j, l), comb(3, l)) * A[l] for l in range(j + 1)) for j in range(4))
claimed = [20240, 20475, 20304, 19926, 20592, 20664, 19530, 17442]
rows = []
for row in U:
    best = Fr(0)
    for m in E:
        P = [Fr(1)]
        for i in m:
            a, b = row[i - 1]
            P = polymul(P, [Fr(a), Fr(b)])
        best = max(best, bernstein_max(P))
    rows.append(best)
check(rows == claimed, f"row maxima {[int(x) for x in rows]}")
M = max(rows)
check(M == 41 * 12 * 42, "M = 20664 = 41*12*42 is attained (row 6, monomial b3, t = 0)")
check(Fr(8**3) / M == Fr(64, 2583), "8 / M^(1/3) = (64/2583)^(1/3)")
print(f"        coefficient (64/2583)^(1/3) = {(64/2583)**(1/3):.6f}")

print("Proposition 6.8")
ex = {3: 2, 5: 2, 6: 1, 7: 1, 8: 2, 12: 1, 13: 1}
tot = [0] * 9
for j, k in ex.items():
    for i in mons[j]:
        tot[i] += k
check(tot[1:] == [4, 4, 2, 4, 4, 4, 4, 4] and sum(ex.values()) == 10,
      "b3^2 b5^2 b6 b7 b8^2 b12 b13 = p3^2 prod_{i!=3} p_i^4 (ten factors)")
print(f"        ceiling e/(7^(7/15) 8^(8/15)) = {e / (7**(7/15) * 8**(8/15)):.6f}")

print("\nALL CHECKS PASSED" if not FAILED else "\nSOME CHECKS FAILED")
sys.exit(1 if FAILED else 0)
