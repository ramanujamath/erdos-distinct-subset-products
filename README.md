# Third-order bounds for Erdős's distinct subset products problem

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24505892.svg)](https://doi.org/10.5281/zenodo.24505892)

This repository holds the manuscript and verification scripts for

> Ramanuja, *Third-order bounds for Erdős's distinct subset products problem.*

Let f(N) be the largest size of a subset of {1, …, N} with distinct subset products, and h(N) the same maximum for squarefree integers. With X = N^{1/3}, the paper proves

```
f(N) − π(N) − π(√N)     = Θ(π(X)),
h(N) − π(N) − ½·π(√N)   = Θ(π(X)).
```

## The constants

Normalized by π(N^{1/3}):

| | unrestricted | squarefree |
|---|---|---|
| Lower bound, Raghavan (2025) | 1/3 ≈ 0.3333 | — |
| Lower bound, this paper (Thm 1.3) | 1/2 = 0.5000 | (64/2583)^{1/3} ≈ 0.2915 |
| Ceiling of the construction used | 1/2 (Remark 6.3) | ≈ 0.3616 (Prop. 6.8) |
| Upper bound, this paper (Prop. 4.2) | ≤ 160.49 | ≤ 160.99 |

## Contents

| Path | Purpose |
|---|---|
| `verification/check_claims.py` | Exact check of Lemmas 6.2 and 6.7, Tables 2–3, M = 20664, and the identity in Prop. 6.8. |
| `verification/explicit_constants.py` | Numerical values of c₂, q\*, τ\*, y\* and C₀ in Prop. 4.2. |
| `verification/*_output.txt` | Recorded output of both scripts. |
| `manuscript/` | LaTeX source and PDF. |

## Running

```bash
python3 verification/check_claims.py         # exact arithmetic; exits 1 on any failure
python3 verification/explicit_constants.py
```

Both scripts use only the Python standard library (Python ≥ 3.8) and run in about a second.

## What is checked

- **Lemma 6.2:** the block {p³, q³, r, r², pr², qr², pq} is dissociated (all 128 subset sums are distinct).
- **Lemma 6.7:** the thirteen monomials on eight primes are dissociated (all 8192 subset sums are distinct).
- **Table 2:** the affine allocation uses each unit interval of [0, 64] exactly once.
- **Table 3:** for each row, the program recomputes the largest Bernstein coefficient over the ten cubic monomials exactly (rational arithmetic). This gives M = 20664 = 41·12·42, hence the coefficient 8/M^{1/3} = (64/2583)^{1/3}.
- **Proposition 6.8:** the product identity b₃²b₅²b₆b₇b₈²b₁₂b₁₃ = p₃² ∏_{i≠3} pᵢ⁴.
- **Proposition 4.2:** C₀ = 20q\* + 2τ\* + y\* − 2 = 160.489…

## Citation

Please cite the paper above. To cite the software:

> Ramanuja, *Verification scripts for third-order bounds in Erdős's distinct subset products problem*, v1.0, Zenodo, 2026. doi:[10.5281/zenodo.24505892](https://doi.org/10.5281/zenodo.24505892)
