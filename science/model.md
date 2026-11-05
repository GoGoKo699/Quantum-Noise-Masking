# Model, operational question and results

## What is being hidden?

A channel changes an input quantum state before a reversible encoder distributes the output into two shares. The question is whether either share, viewed by itself, reveals that the channel acted.

The local outputs may retain information about the input. For example, copying the labels of an orthonormal basis into two shares preserves their populations locally while hiding changes confined to coherences. This is channel masking against a specified baseline, not universal masking of arbitrary input states.

All Hilbert spaces are finite dimensional. The input space is $`H=\mathbb C^d`$, the noise is a known completely positive trace-preserving map $`\mathcal N:\mathcal L(H)\to\mathcal L(H)`$, and the baseline is the identity channel on the same space. A deterministic pure encoder is an isometry
```math
V:H\longrightarrow A\otimes B,\qquad V^\dagger V=I_H.
```
Write $`\mathcal V(\rho)=V\rho V^\dagger`$ and
```math
M_A=\operatorname{Tr}_B\circ\mathcal V,\qquad
M_B=\operatorname{Tr}_A\circ\mathcal V.
```

Both outputs are retained. A pure ancillary register is allowed and counted. There is no discarded third output, mixed private randomness, secret key or postselection. The encoder may depend on the known channel or gate family.

## Reference-sensitive local leakage

For channels with the same domain and codomain, use the half-diamond distance
```math
D_\diamond(\mathcal E,\mathcal F)
=\frac12\|\mathcal E-\mathcal F\|_\diamond.
```
Define
```math
\varepsilon_V(\mathcal N)
=\max_{S\in\{A,B\}}D_\diamond(M_S\circ\mathcal N,M_S).
```

The observer holds one retained share and an arbitrary untouched reference system; the noise environment and any record of its random kick are inaccessible. The diamond norm includes that reference. Equivalently, for every input-reference state $`\rho_{HR}`$ and either share $`S`$,
```math
\frac12\left\|
[(M_S\circ\mathcal N-M_S)\otimes\mathrm{id}_R](\rho_{HR})
\right\|_1
\le\varepsilon_V(\mathcal N).
```
A reference of dimension $`d`$ suffices for channel discrimination. With equal prior probabilities for noise versus identity, the optimal success probability using that share and the reference is at most $`(1+\varepsilon_V(\mathcal N))/2`$.

An observer holding both shares has a different experiment. Isometric encoding preserves the global channel distance:
```math
D_\diamond(\mathcal V\circ\mathcal N,\mathcal V)
=D_\diamond(\mathcal N,\mathrm{id}).
```
The local guarantee therefore does not protect against holders communicating their quantum systems or accessing both shares jointly. It also does not assert privacy through arbitrary later gate sequences.

## The exact class

Let $`\mathfrak M_d`$ denote the channels for which some finite-dimensional pure bipartite encoder attains $`\varepsilon_V(\mathcal N)=0`$. This is an existence definition, not an identification of a zero infimum with an attained exact masker.

The [exact classification](exact_masking.md) gives
```math
\mathcal N\in\mathfrak M_d
\quad\Longleftrightarrow\quad
\mathcal N(|i\rangle\langle j|)
=C_{ij}|i\rangle\langle j|
```
in some orthonormal basis, where $`C\succeq0`$ and $`C_{ii}=1`$.

These are Schur channels in an arbitrary basis. Equivalent descriptions are a complete orthonormal basis of pure fixed states, preservation of all basis populations, and Kraus operators diagonal in one common basis. The copying isometry $`V|i\rangle=|i\rangle_A|i\rangle_B`$ is an exact encoder. Higher-dimensional Schur channels need not be mixtures of diagonal unitaries, so the exact class is broader than classical random phase noise.

## Approximate gate masking

For a fixed family of unitaries $`U_1,\ldots,U_k`$ and the identity baseline, let
```math
\delta=\max_{i,j}\|U_iU_j-U_jU_i\|_{\mathrm{op}},\qquad
\varepsilon_*=\inf_V\max_j\varepsilon_V(\operatorname{Ad}_{U_j}),
```
where $`\operatorname{Ad}_{U}(\rho)=U\rho U^\dagger`$. The [quantitative gate theorem](approximate_gates.md) proves
```math
\frac{\delta^2}{32}\le\varepsilon_*
\le
\inf_{L\in\mathbb N,\ L\ge1}
\left[\frac1L+(k-1)(L-1)\delta\right].
```

The upper construction uses a coherent register of dimension $`L^k`$ and a second share of dimension $`d`$. For fixed $`k`$, vanishing commutators and vanishing local gate leakage imply one another with bounds independent of $`d`$. The exponents are not matched. The commutators here are those of the implementing unitary matrices, not those of their conjugation superoperators.

## Single-channel separation

The [Weyl construction and separation](weyl_separation.md) gives, for every $`d\ge3`$,
```math
\mathcal N_d=\frac13
\left(\mathrm{id}+\operatorname{Ad}_{X_d}+\operatorname{Ad}_{Z_d}\right).
```
With $`L=\lfloor\sqrt d\rfloor`$, a pure encoder into shares of dimensions $`L^2`$ and $`d`$ satisfies
```math
\varepsilon_V(\mathcal N_d)
\le\frac23
\max\left\{\frac1L,\,
\sin\frac{\pi(L-1)}d\right\}
=O(d^{-1/2}),
```
but
```math
\inf_{\mathcal S\in\mathfrak M_d}
D_\diamond(\mathcal N_d,\mathcal S)\ge\frac1{48},
\qquad
D_\diamond(\mathcal N_d,\mathrm{id})=\frac23.
```

Thus there is no dimension-independent function tending to zero that converts small local leakage into distance to the exact class. The comparison permits every Schur channel in every basis, including channels with arbitrary Kraus representations.

The [implementation and stability account](resources_and_stability.md) supplies a finite qubit circuit for a convenient dimension sequence and separates channel error from encoder error. The [interpretation](interpretation.md) explains what this instability does and does not establish.

## Reading route

1. [Exact masking](exact_masking.md): why population-preserving noise is the whole exact class.
2. [Approximate gates](approximate_gates.md): coherent finite averaging and the converse through complementary channels.
3. [Weyl separation](weyl_separation.md): explicit local hiding, persistent global noise and distance from all exact mechanisms.
4. [Resources and stability](resources_and_stability.md): registers, gates, precision and perturbations.
5. [Interpretation](interpretation.md): the operational consequence and the remaining quantitative limits.

The [related-work account](../references/RELATED_WORK.md) credits the exact masking results, channel-continuity machinery and matrix obstruction on which the arguments build. [Finite verification](../verification/README.md) checks specified algebra and circuits; it does not replace the proofs.
