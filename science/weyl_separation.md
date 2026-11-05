# A single noisy channel far from every exactly maskable channel

This page combines an explicit two-share encoder with a quantitative obstruction to approximating almost-commuting matrices by commuting ones. Definitions and the identity baseline are fixed in the [model](model.md).

## 1. Clock, shift and noise

For $`d\ge3`$, set $`\omega=e^{2\pi i/d}`$ and
```math
X|j\rangle=|j+1\bmod d\rangle,\qquad
Z|j\rangle=\omega^j|j\rangle.
```
Then
```math
ZX=\omega XZ,\qquad
\|XZ-ZX\|_{\mathrm{op}}=2\sin(\pi/d).
```
The unitary matrices almost commute as $`d`$ grows. Their conjugation channels commute exactly, because the scalar phase disappears under conjugation. The distinction is essential to the [gate criterion](approximate_gates.md).

Consider the one-use noisy channel
```math
\mathcal N_d=\frac13
\left(\mathrm{id}+\operatorname{Ad}_X+\operatorname{Ad}_Z\right).
```

## 2. A pure encoder with two small shares

For a positive integer $`L`$ with $`L-1\le d/2`$, define
```math
V_L|\psi\rangle
=\frac1L\sum_{a,b=0}^{L-1}
|a,b\rangle_A\otimes X^aZ^b|\psi\rangle_B.
```
The orthogonality of the label states gives $`V_L^\dagger V_L=I`$. The dimensions are $`\dim A=L^2`$ and $`\dim B=d`$. There is no measured or discarded label.

Let $`\alpha=\operatorname{Tr}_B\circ\mathcal V_L`$ and $`\beta=\operatorname{Tr}_A\circ\mathcal V_L`$. We bound the effect of $`X`$ and $`Z`$ on both marginals.

### The system share: only the edge of the averaging window changes

The second marginal is
```math
\beta(\rho)=\frac1{L^2}\sum_{a,b=0}^{L-1}
X^aZ^b\rho Z^{-b}X^{-a}.
```
Applying $`X`$ to the input shifts the $`a`$ window by one; its scalar Weyl phases cancel. The terms with $`a=1,\ldots,L-1`$ agree, leaving
```math
\beta\circ\operatorname{Ad}_X-\beta
=\frac1{L^2}\sum_{b=0}^{L-1}
\left(\operatorname{Ad}_{X^LZ^b}-\operatorname{Ad}_{Z^b}\right).
```
Each difference of channels has diamond norm at most two. Therefore
```math
D_\diamond(\beta\circ\operatorname{Ad}_X,\beta)\le\frac1L.
```
The same argument shifts the $`b`$ window for $`Z`$ and gives the identical bound. The argument is in diamond norm and includes every input-reference state.

### The label share: a short spectral arc

Define diagonal label unitaries
```math
D_b|a,b\rangle=\omega^b|a,b\rangle,\qquad
D_{-a}|a,b\rangle=\omega^{-a}|a,b\rangle.
```
The exact intertwining relations are
```math
V_LX=(D_b\otimes X)V_L,\qquad
V_LZ=(D_{-a}\otimes Z)V_L.
```
Tracing out $`B`$ yields
```math
\alpha\circ\operatorname{Ad}_X=\operatorname{Ad}_{D_b}\circ\alpha,
\qquad
\alpha\circ\operatorname{Ad}_Z=\operatorname{Ad}_{D_{-a}}\circ\alpha.
```

Both diagonal unitaries have eigenvalues in an arc of angular width
$`\theta=2\pi(L-1)/d\le\pi`$. For any density operator $`\sigma`$, the convex hull of that arc obeys
$`|\operatorname{Tr}(\sigma D)|\ge\cos(\theta/2)`$ after centering its phase. For a purified input, the overlap of the two possible pure outputs is this trace. Their trace distance is consequently at most $`\sin(\theta/2)`$. Convexity extends the bound to mixed inputs, and an arbitrary reference is already included by the purification. Hence
```math
D_\diamond(\operatorname{Ad}_{D},\mathrm{id})
\le\sin(\theta/2).
```
Precomposition by $`\alpha`$ does not increase diamond distance, so
```math
D_\diamond(\alpha\circ\operatorname{Ad}_X,\alpha),
\ D_\diamond(\alpha\circ\operatorname{Ad}_Z,\alpha)
\le\sin\frac{\pi(L-1)}d.
```

### Leakage of the mixture

Convexity, with the identity term contributing zero, gives
```math
\boxed{\;
\varepsilon_{V_L}(\mathcal N_d)
\le\frac23\max\left\{\frac1L,\sin\frac{\pi(L-1)}d\right\}.
\;}
```
Choose $`L=\lfloor\sqrt d\rfloor`$. The spectral-arc condition holds and $`L^2\le d`$, so the label share can be padded to dimension $`d`$. Since $`L\ge\sqrt d/2`$ and $`\sin x\le x`$,
```math
\varepsilon_{V_L}(\mathcal N_d)\le\frac{2\pi}{3\sqrt d}.
```
The exact finite expression is more informative at small $`d`$. Neither this exponent nor the share dimensions are asserted to be optimal.

## 3. The noise remains globally visible

Let $`|\Omega\rangle=d^{-1/2}\sum_j|j,j\rangle`$. The three vectors
```math
|\Omega\rangle,\quad
(X\otimes I)|\Omega\rangle,\quad
(Z\otimes I)|\Omega\rangle
```
are orthonormal: $`I,X,Z`$ are mutually orthogonal in the Hilbert–Schmidt inner product. The normalized Choi state of $`\mathcal N_d`$ is the equally weighted mixture of their projectors. Its half-trace distance from the identity-channel Choi state is $`2/3`$.

This gives the lower bound $`D_\diamond(\mathcal N_d,\mathrm{id})\ge2/3`$. The reverse inequality follows by writing the difference as one third of each of two channel differences, whose half-diamond distances are at most one. Thus
```math
D_\diamond(\mathcal N_d,\mathrm{id})=\frac23.
```
The three separate unitary alternatives are perfectly distinguishable with this probe. Their mixture versus the identity has distance $`2/3`$, not one.

## 4. Imported matrix obstruction

For a unitary pair with $`\|UV-VU\|_{\mathrm{op}}\lt2`$, a winding/Bott index can be defined through the principal logarithm of the multiplicative commutator. Up to the order convention,
```math
\operatorname{Bott}(U,V)
=\frac1{2\pi i}\operatorname{Tr}\log(VUV^\dagger U^\dagger).
```
The value is an integer: the commutator has determinant one and its spectrum avoids the logarithm's branch cut. The clock/shift pair has index one in this convention, while a commuting pair has index zero.

We use the following consequence of [Loring, Theorem 2.3](https://sigma-journal.com/2014/077/sigma14-077.pdf): if a unitary pair has nonzero index and commutator norm below two, then every commuting unitary pair $`U_0,V_0`$ satisfies
```math
\|U-U_0\|_{\mathrm{op}}+\|V-V_0\|_{\mathrm{op}}\gt \sqrt2.
```
Loring proves a stronger commutator-dependent estimate. The conservative form above is sufficient here. The clock/shift obstruction and its topological invariant are established matrix theory; the masking consequence is derived next.

## 5. Distance from every exactly maskable channel

**Theorem.** For all $`d\ge3`$,
```math
\inf_{\mathcal S\in\mathfrak M_d}
D_\diamond(\mathcal N_d,\mathcal S)\ge\frac1{48}.
```

**Proof.** By the [exact classification](exact_masking.md), an arbitrary $`\mathcal S\in\mathfrak M_d`$ is Schur in some orthonormal basis, which may depend on $`\mathcal S`$. Put $`\eta=D_\diamond(\mathcal N_d,\mathcal S)`$.

A canonical Stinespring isometry for $`\mathcal N_d`$ is
```math
W_N=\frac1{\sqrt3}\left(
I\otimes|0\rangle+X\otimes|1\rangle+Z\otimes|2\rangle\right).
```
A Schur channel admits a dilation
```math
W_S=\sum_i |i\rangle\langle i|\otimes|e_i\rangle
```
in its Schur basis, with unit vectors $`e_i`$. The vectors need not be orthogonal, and no random-unitary representation is assumed.

The [continuity theorem for Stinespring dilations](https://arxiv.org/pdf/0710.2495), Theorem 1, gives isometric embeddings of the two environments into a common, sufficiently large environment such that
```math
\|(I\otimes J_N)W_N-(I\otimes J_S)W_S\|_{\mathrm{op}}
\le\sqrt{2\eta}.
```
The channel-to-operator bound uses full diamond distance under the square root; the factor two comes from the definition of $`\eta`$. A larger common environment is allowed for this proof comparison, without adding a physical output to the masker.

The three vectors $`f_j=J_N|j\rangle`$ are orthonormal. Projecting the common dilations onto $`f_1`$ and $`f_2`$, then multiplying by $`\sqrt3`$, gives operators $`D_X,D_Z`$ diagonal in the same Schur basis and
```math
\|X-D_X\|_{\mathrm{op}},
\ \|Z-D_Z\|_{\mathrm{op}}
\le\sqrt{6\eta}.
```
Environment changes preserve diagonal form, so this step covers arbitrary Schur Kraus representations.

If $`\eta\ge1/6`$, the claimed lower bound is immediate. Otherwise put $`e=\sqrt{6\eta}\lt1`$. For any diagonal $`D`$ within $`e`$ of a unitary, its singular values lie in $`[1-e,1+e]`$. Its diagonal polar unitary $`U_D`$ therefore obeys
```math
\|D-U_D\|_{\mathrm{op}}\le e,\qquad
\|U-U_D\|_{\mathrm{op}}\le2e.
```
The polar unitaries associated with $`D_X,D_Z`$ commute, since they are diagonal in one basis. Their total distance from $`X,Z`$ is at most $`4\sqrt{6\eta}`$. The matrix obstruction requires
```math
4\sqrt{6\eta}\gt \sqrt2,
```
and hence $`\eta\gt 1/48`$. Taking the infimum over $`\mathfrak M_d`$ proves the stated non-strict lower bound. $`\square`$

## 6. What fails uniformly with dimension?

Suppose a function $`f(t)\to0`$ as $`t\to0`$ bounded the distance of every channel to the exact class whenever a pure two-share encoder achieved leakage at most $`t`$, independently of input dimension. The constructed family would imply
```math
\frac1{48}\le f\!\left(\varepsilon_{V_L}(\mathcal N_d)\right)\longrightarrow0,
```
a contradiction.

This is a failure of a uniform structural inference. Each fixed $`d`$ remains finite, the encoder is explicit, both output dimensions are at most $`d`$, and the noise is one fixed three-term mixture for that dimension. The encoder uses no discarded random key or private randomness. Its output shares are at most the input dimension, and the leakage bound uses the full reference-sensitive norm.
