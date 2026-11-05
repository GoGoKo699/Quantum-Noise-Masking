# Quantum Noise Masking

**Can noise become almost invisible in each of two shares without being close to noise that can be hidden exactly?** Yes. A pure reversible encoder can make a globally strong channel arbitrarily difficult to detect locally, while the channel remains a fixed distance from the entire exact masking class.

The baseline is the identity channel. Each local observer may hold one share and an arbitrary untouched reference, while the noise environment is inaccessible. The encoder retains exactly two outputs and uses a pure ancillary register.

## Principal results

**Exact structure.** A finite-dimensional channel is exactly maskable against identity by a pure bipartite isometry if and only if it is a Schur channel in some orthonormal basis: it preserves every population in that basis and acts entrywise on coherences. A finite family has a common exact masker precisely when its channels share such a basis.

**Approximate structure can be different.** Let $`X_d,Z_d`$ be the cyclic shift and phase clock and define
```math
\mathcal N_d=\frac13
\left(\mathrm{id}+\operatorname{Ad}_{X_d}+\operatorname{Ad}_{Z_d}\right),
\qquad d\ge3.
```
With $`L=\lfloor\sqrt d\rfloor`$, the explicit encoder
```math
V|\psi\rangle=\frac1L
\sum_{a,b=0}^{L-1}|a,b\rangle_A\otimes X_d^aZ_d^b|\psi\rangle_B
```
has shares of dimensions $`L^2\le d`$ and $`d`$. Its local half-diamond leakage satisfies
```math
\varepsilon_V(\mathcal N_d)
\le\frac23\max\left\{\frac1L,\sin\frac{\pi(L-1)}d\right\}
=O(d^{-1/2}),
```
yet
```math
\inf_{\mathcal S\in\mathfrak M_d}
D_\diamond(\mathcal N_d,\mathcal S)\ge\frac1{48},
\qquad
D_\diamond(\mathcal N_d,\mathrm{id})=\frac23.
```
Here $`\mathfrak M_d`$ is the entire class of exactly maskable channels, in every basis, and $`D_\diamond`$ is half the diamond norm. The local guarantee includes reference-entangled inputs. The separation rules out a dimension-independent inference from small local leakage to a nearby exact masking mechanism.

**A quantitative gate criterion.** For a fixed family of $`k\ge2`$ unitaries and the identity baseline, let $`\delta`$ be the largest operator norm of their pairwise commutators. The optimal local leakage obeys
```math
\frac{\delta^2}{32}
\le\varepsilon_*
\le\inf_{L\in\mathbb N,\ L\ge1}
\left[\frac1L+(k-1)(L-1)\delta\right].
```
Thus almost commutation and approximate gate masking imply one another with dimension-independent bounds for fixed $`k`$. This does not require a nearby commuting gate family.

## Read the science

| Question | Authoritative account |
|---|---|
| What is observed, and what does the norm guarantee? | [Model and exact statements](science/model.md) |
| Why are Schur channels the entire exact class? | [Exact classification and finite families](science/exact_masking.md) |
| How does almost commutation control leakage? | [Coherent averaging and the quantitative converse](science/approximate_gates.md) |
| How can one noisy channel stay far from every exact mechanism? | [Weyl construction and separation proof](science/weyl_separation.md) |
| Which registers, gates and precision does the encoder need? | [Finite implementation and stability](science/resources_and_stability.md) |
| What does the separation mean physically? | [Interpretation and scope](science/interpretation.md) |
| Which results and techniques are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

Start with the model, then follow the exact classification, approximate gate criterion and single-channel separation. The [LLM reading guide](llms.txt) maps questions to these same authoritative files.

## Implementation and errors

For $`d=2^{2m}`$ and $`L=2^m`$, the encoder uses $`4m`$ qubits total, including $`2m`$ clean label qubits retained as one share. A sufficient exact circuit uses $`6m`$ Hadamards, $`7m^2-m`$ controlled phases and $`2m`$ swaps, with no additional work qubits. Finite-alphabet synthesis remains polynomial in $`m`$ at the precision needed for leakage of order $`2^{-m}`$.

If the channel has half-diamond error $`\eta`$ and one common encoder has half-diamond error $`\kappa`$, the local leakage increases by at most $`\eta+4\kappa/3`$, while distance from the exact class decreases by at most $`\eta`$. These are logical-circuit and error-budget statements; they do not assume a hardware noise floor can stay fixed as the target leakage vanishes.

## Reproduce the finite checks

Install the pinned numerical dependency and run the documented verifier:
```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_masking.py
```

The [verification guide](verification/README.md) covers the Weyl relations, isometry and intertwining identities, exact Schur masking, and gate-by-gate Fourier implementation. Finite numerical checks support those tested identities. The all-dimensional classification, diamond-norm guarantees and distance lower bound are established by proofs.

## Scope and attribution

The dimension grows as leakage decreases. Both holders jointly can recover the noisy output, and the encoder need not hide the original input state. No optimal leakage exponent, minimal register size, arbitrary-circuit privacy or practical cryptographic protocol is claimed.

The pure channel-masking model and exact unitary criterion are due to [Honeycutt, Murray and Chitambar](https://arxiv.org/html/2510.09456v2). Channel continuity, fixed-space structure, the clock/shift obstruction and Fourier addition are established ingredients. The related-work account separates those foundations from the noisy classification, quantitative criterion and single-channel operational separation developed here.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
