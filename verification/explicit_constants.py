#!/usr/bin/env python3
"""
Numerical values of the constants in Proposition 4.2 of

    Ramanuja, "Third-order bounds for Erdos's distinct subset products problem".

  c2   : positive root of  w = log2(1 + 5w)
  q*   : sum_{k>=1} 2^{-k} log2(1 + c2 4^k)
  tau* : positive root of  tau = q* + log2(1 + 8 tau)
  y*   : positive root of  y = 2 log2(1 + 5y)
  C0   = 20 q* + 2 tau* + y* - 2       (unrestricted)
  C0 + 1/2                            (squarefree)

Roots are found by bisection to full double precision; the series for q* is
summed until its terms are below 1e-30 (the tail is bounded by the next term
times a geometric factor). Standard library only.
"""
from math import log2

def root(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if f(mid) > 0 else (mid, hi)
    return hi

c2 = root(lambda w: w - log2(1 + 5 * w), 1.0, 50.0)
q = sum(2.0 ** -k * log2(1 + c2 * 4.0 ** k) for k in range(1, 200))
tau = root(lambda t: t - q - log2(1 + 8 * t), 1.0, 500.0)
y = root(lambda v: v - 2 * log2(1 + 5 * v), 1.0, 500.0)
C0 = 20 * q + 2 * tau + y - 2

print(f"c2   = {c2:.6f}")
print(f"q*   = {q:.6f}")
print(f"tau* = {tau:.6f}")
print(f"y*   = {y:.6f}")
print(f"20 q* = {20*q:.4f}, 2 tau* = {2*tau:.4f}, y* = {y:.4f}")
print(f"C0 (unrestricted) = {C0:.4f}")
print(f"C0 + 1/2 (squarefree) = {C0 + 0.5:.4f}")
