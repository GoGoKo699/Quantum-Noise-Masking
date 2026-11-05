# Exact masking is equivalent to Schur noise

The [model](model.md) fixes the identity baseline and pure bipartite encoder. Here $`\alpha_V=M_A`$, $`\beta_V=M_B`$, and $`\varepsilon_V`$ is the half-diamond leakage defined there. The operator norm is written $`\|\cdot\|_\infty`$.

## 2. Exact classification

### Theorem 1: classification in arbitrary finite dimension

For a channel $`\mathcal N:\mathcal B(H)\to\mathcal B(H)`$, the following statements are equivalent.

1. There are finite-dimensional spaces $`A,B`$ and an isometry $`V:H\to A\otimes B`$ such that $`\varepsilon_V(\mathcal N)=0`$.
2. There is an orthonormal basis $`\{|i\rangle\}_{i=1}^d`$ such that every $`|i\rangle\langle i|`$ is fixed by $`\mathcal N`$.
3. In one orthonormal basis, every Kraus operator in a Kraus representation of $`\mathcal N`$ is diagonal.
4. In one orthonormal basis, $`\mathcal N`$ is a Schur channel:

```math
\mathcal N(|i\rangle\langle j|)
=C_{ij}|i\rangle\langle j|,
\qquad
C\succeq0,
\qquad
C_{ii}=1.
```

When these conditions hold, the encoder

```math
V|i\rangle=|i\rangle_A\otimes|i\rangle_B
```

works with $`\dim A=\dim B=d`$.

The diagonal-Kraus conclusion is independent of a specially chosen Kraus representation: if a basis of pure states is fixed, **every** Kraus representation has diagonal Kraus operators in that basis.

A Schur channel preserves the full diagonal algebra pointwise, but the theorem does not assume that it is a convex mixture of diagonal unitaries. “Schur channel” is the exact mathematical class used here.

The nontrivial implication is from exact masking to a pure fixed-state basis. The next three lemmas make its treatment of channels without a faithful stationary state explicit. They reproduce the relevant finite-dimensional fixed-point facts with proofs; the general information-preserving structure and asymptotic-channel results are established prior machinery [2,3].

### Lemma 1: orthogonality from a vanishing cross marginal

Let $`u,v\in A\otimes B`$ be nonzero pure vectors. If

```math
\mathrm{Tr}_B|u\rangle\langle v|=0,
```

then the supports of their $`B`$ marginals are orthogonal.

**Proof.** Take Schmidt decompositions

```math
|u\rangle=\sum_r \sqrt{\lambda_r}\,|a_r\rangle|b_r\rangle,
\qquad
|v\rangle=\sum_s \sqrt{\mu_s}\,|c_s\rangle|d_s\rangle,
```

with strictly positive displayed Schmidt coefficients. The cross partial trace is

```math
\sum_{r,s}\sqrt{\lambda_r\mu_s}\,
\langle d_s|b_r\rangle\,|a_r\rangle\langle c_s|.
```

The operators $`|a_r\rangle\langle c_s|`$ are linearly independent: multiply on the left by $`\langle a_r|`$ and on the right by $`|c_s\rangle`$. Its vanishing therefore gives $`\langle d_s|b_r\rangle=0`$ for every $`r,s`$. The two Schmidt supports in $`B`$ are orthogonal. The analogous assertion holds with $`A`$ and $`B`$ exchanged. $`\square`$

### Lemma 2: the faithful fixed-observable algebra

Suppose a channel

```math
\mathcal T(X)=\sum_\mu K_\mu X K_\mu^\dagger
```

has a faithful stationary state $`\sigma\gt 0`$. Then

```math
\mathrm{Fix}(\mathcal T^\dagger)
=\{K_\mu,K_\mu^\dagger:\mu\}',
```

the common commutant of its Kraus operators and their adjoints. In particular this fixed-observable space is a unital finite-dimensional $`C^*`$-algebra.

**Proof.** Let $`F`$ satisfy $`\mathcal T^\dagger(F)=F`$. Since $`\mathcal T^\dagger`$ is unital and completely positive, its Schwarz inequality gives

```math
D=\mathcal T^\dagger(F^\dagger F)-F^\dagger F\succeq0.
```

Stationarity implies

```math
\mathrm{Tr}(\sigma D)
=\mathrm{Tr}[\mathcal T(\sigma)F^\dagger F]
-\mathrm{Tr}(\sigma F^\dagger F)
=0.
```

Faithfulness forces $`D=0`$. Expanding a sum of squares gives

```math
\begin{aligned}
\sum_\mu(FK_\mu-K_\mu F)^\dagger(FK_\mu-K_\mu F)
&=\mathcal T^\dagger(F^\dagger F)
-\mathcal T^\dagger(F^\dagger)F
-F^\dagger\mathcal T^\dagger(F)+F^\dagger F\\
&=0.
\end{aligned}
```

Every summand vanishes, so $`F`$ commutes with each $`K_\mu`$. Apply the same argument to $`F^\dagger`$ to obtain commutation with each $`K_\mu^\dagger`$ as well. Conversely, an operator commuting with all $`K_\mu`$ and $`K_\mu^\dagger`$ is fixed because $`\sum_\mu K_\mu^\dagger K_\mu=I`$. $`\square`$

This is the zero-frequency case of the Kraus-commutation principle in Albert's Proposition 1 [3]. The explicit proof also records where faithfulness is required.

### Lemma 3: the stationary projection kills support–complement coherences

Let $`\mathcal N`$ be any finite-dimensional channel, and define its Cesàro projection

```math
\mathcal P
=\lim_{M\to\infty}\frac1M\sum_{n=0}^{M-1}\mathcal N^n.
```

Let

```math
R=\mathrm{supp}\mathcal P(I_H),
\qquad
T=R^\perp.
```

Then:

- $`\mathcal P`$ is CPTP and idempotent, with range $`\mathrm{Fix}(\mathcal N)`$;
- every output of $`\mathcal P`$ is supported on $`R`$;
- $`\mathcal P`$ annihilates both operator corners $`\mathcal B(T,R)`$ and $`\mathcal B(R,T)`$.

In particular,

```math
\mathcal P(|r\rangle\langle t|)=0
\qquad
(r\in R,\ t\in T).
```

**Proof.** The powers of a channel are uniformly bounded as linear maps. In finite dimension this excludes nontrivial Jordan blocks on the unit circle, so Cesàro averaging converges to the spectral projection at eigenvalue one. Hence

```math
\mathcal P^2=\mathcal P,
\qquad
\mathcal N\mathcal P=\mathcal P\mathcal N=\mathcal P,
```

and $`\mathcal P`$ is CPTP as a limit of CPTP maps.

For a state $`\rho`$, the operator inequality $`0\preceq\rho\preceq I_H`$ implies

```math
0\preceq\mathcal P(\rho)\preceq\mathcal P(I_H).
```

Therefore $`\mathcal P(\rho)`$ is supported on $`R`$. States linearly span the operator space, so the same support assertion holds for all outputs. Moreover,

```math
\sigma_R=\frac{\mathcal P(I_H)}{d}
```

is a stationary state faithful on $`R`$. Every stationary state equals its image under $`\mathcal P`$ and is supported on $`R`$, so $`R`$ is the maximal stationary support.

Choose a Kraus representation of $`\mathcal P`$. Since every Kraus range lies in $`R`$, its operators have the block form

```math
L_\mu=
\begin{pmatrix}
A_\mu&B_\mu\\
0&0
\end{pmatrix}
\quad\text{on }R\oplus T.
```

Indeed, $`\mathcal P(I_H)=\sum_\mu L_\mu L_\mu^\dagger`$ has support $`R`$, so $`L_\mu^\dagger t=0`$ for every $`t\in T`$. Trace preservation gives

```math
\sum_\mu A_\mu^\dagger A_\mu=I_R,
\qquad
\sum_\mu A_\mu^\dagger B_\mu=0,
\qquad
\sum_\mu B_\mu^\dagger B_\mu=I_T.
```

The restriction

```math
\mathcal P_R(Y)=\sum_\mu A_\mu Y A_\mu^\dagger
```

is a CPTP projection on $`\mathcal B(R)`$ and has faithful stationary state $`\sigma_R`$. Put $`\mathcal F_R=\mathrm{Fix}(\mathcal P_R^\dagger)`$. By Lemma 2, every $`F\in\mathcal F_R`$ commutes with every $`A_\mu`$ and $`A_\mu^\dagger`$. Consequently

```math
\mathcal P^\dagger(F\oplus0)
=
\begin{pmatrix}
F&0\\
0&\displaystyle\sum_\mu B_\mu^\dagger F B_\mu
\end{pmatrix}.
```

The upper-right entry, for example, is

```math
\sum_\mu A_\mu^\dagger F B_\mu
=F\sum_\mu A_\mu^\dagger B_\mu=0.
```

For $`Z=|r\rangle\langle t|`$, write $`Y=\mathcal P(Z)`$. It is supported on $`R`$ and satisfies $`\mathcal P_R(Y)=Y`$. For every $`F\in\mathcal F_R`$,

```math
\mathrm{Tr}(F^\dagger Y)
=\mathrm{Tr}\!\left[
\mathcal P^\dagger(F^\dagger\oplus0)Z
\right]=0,
```

because the first factor is block diagonal and $`Z`$ is an off-diagonal corner.

The pairing between the range of a projection and the range of its adjoint is nondegenerate. Explicitly, for arbitrary $`G\in\mathcal B(R)`$,

```math
\mathrm{Tr}(G^\dagger Y)
=\mathrm{Tr}\!\left[
(\mathcal P_R^\dagger G)^\dagger Y
\right]=0,
```

since $`\mathcal P_R^\dagger G\in\mathcal F_R`$. Thus $`Y=0`$. Adjoint preservation gives the assertion for the opposite corner. $`\square`$

The annihilation conclusion agrees with the stationary part of Albert's asymptotic formula, Proposition 3 and Eq. (22) [3]. The proof above uses the Cesàro projection directly; it needs no assumption that powers of $`\mathcal N`$ converge or that peripheral eigenvalues other than one are absent.

### Proof of Theorem 1

Assume exact masking by $`V`$, and abbreviate its marginal channels to $`\alpha,\beta`$. Iterating their invariance and taking Cesàro averages gives

```math
\alpha\circ\mathcal P=\alpha,
\qquad
\beta\circ\mathcal P=\beta.
```

**Step 1: the stationary support is the entire input space.** Suppose $`T\ne\{0\}`$ and choose a unit vector $`t\in T`$. For every $`r\in R`$, Lemma 3 gives

```math
\alpha(|r\rangle\langle t|)
=\alpha\!\left(\mathcal P(|r\rangle\langle t|)\right)=0.
```

Lemma 1 implies that the $`B`$ marginal of $`Vt`$ has support orthogonal to the $`B`$ marginal of $`Vr`$, for every $`r\in R`$. The state $`\mathcal P(|t\rangle\langle t|)`$ is supported on $`R`$, so its spectral decomposition expresses its $`B`$ marginal as a convex combination of such orthogonally supported marginals. Hence

```math
\beta\!\left(\mathcal P(|t\rangle\langle t|)\right)
```

has support orthogonal to $`\beta(|t\rangle\langle t|)`$. Invariance says these two unit-trace positive operators are equal, a contradiction. Therefore $`T=0`$ and $`\mathcal N`$ has a faithful stationary state.

**Step 2: no noisy tensor factor can remain.** Apply Lemma 2 to $`\mathcal N`$. The finite-dimensional decomposition of its fixed-observable algebra has the form

```math
H=\bigoplus_j L_j\otimes M_j,
\qquad
\mathcal F:=\mathrm{Fix}(\mathcal N^\dagger)
=\bigoplus_j\mathcal B(L_j)\otimes I_{M_j}.
```

Every Kraus operator commutes with $`\mathcal F`$, so

```math
K_\mu=\bigoplus_j I_{L_j}\otimes K_{\mu j}.
```

The maps

```math
\mathcal N_j(Y)=\sum_\mu K_{\mu j}Y K_{\mu j}^\dagger
```

are channels on $`M_j`$. Their adjoint fixed spaces are scalar:

```math
\mathrm{Fix}(\mathcal N_j^\dagger)=\mathbb C I_{M_j}.
```

To verify this, if $`\mathcal N_j^\dagger(F)=F`$, then the operator $`I_{L_j}\otimes F`$ in block $`j`$, with zero in all other blocks, is fixed by $`\mathcal N^\dagger`$. Its membership in the displayed algebra forces $`F`$ to be scalar.

The fixed space of a finite-dimensional linear map has the same dimension as that of its adjoint. Each $`\mathcal N_j`$ therefore has a unique stationary state $`\tau_j`$, and its Cesàro projection is

```math
Y\longmapsto\mathrm{Tr}(Y)\tau_j.
```

For a unit vector $`a\in L_j`$ and any unit vector $`b\in M_j`$,

```math
\mathcal P\!\left(
|a\rangle\langle a|\otimes|b\rangle\langle b|
\right)
=|a\rangle\langle a|\otimes\tau_j.
```

Both marginals of $`V(a\otimes b)`$ are consequently independent of $`b`$.

If $`\dim M_j\ge2`$, choose orthogonal $`b_0,b_1\in M_j`$ and put $`u=V(a\otimes b_0)`$, $`v=V(a\otimes b_1)`$. The two $`B`$ marginals are equal. Independence of the $`A`$ marginal for the four superpositions

```math
\frac{b_0+b_1}{\sqrt2},\quad
\frac{b_0-b_1}{\sqrt2},\quad
\frac{b_0+ib_1}{\sqrt2},\quad
\frac{b_0-ib_1}{\sqrt2}
```

forces $`\mathrm{Tr}_B|u\rangle\langle v|=0`$. Lemma 1 then makes the two equal $`B`$ marginals orthogonally supported, which is impossible for unit-trace states. Thus every $`M_j`$ is one-dimensional.

It follows that each $`K_\mu`$ is scalar on each block $`L_j`$. Choose an orthonormal basis within every $`L_j`$. All Kraus operators are diagonal in the resulting complete basis. This proves statement 3 from statement 1.

**Step 3: equivalent diagonal forms and construction.** If

```math
K_\mu=\sum_i c_{\mu i}|i\rangle\langle i|,
```

then

```math
\mathcal N(|i\rangle\langle j|)
=\left(\sum_\mu c_{\mu i}\overline{c_{\mu j}}\right)
|i\rangle\langle j|.
```

The coefficient matrix is positive semidefinite, and trace preservation makes its diagonal equal to one. Hence statement 3 implies statement 4, which immediately implies statement 2.

Conversely, if $`\mathcal N(|i\rangle\langle i|)=|i\rangle\langle i|`$, then in any Kraus representation

```math
|i\rangle\langle i|
=\sum_\mu |K_\mu i\rangle\langle K_\mu i|.
```

Every positive summand must be supported on $`\mathbb C|i\rangle`$. Thus $`K_\mu|i\rangle=c_{\mu i}|i\rangle`$ for all $`\mu,i`$, proving statement 3.

Finally, the copying isometry in the theorem has both marginals equal to complete dephasing in this basis:

```math
\alpha_V(X)=\beta_V(X)
=\sum_i\langle i|X|i\rangle\,|i\rangle\langle i|,
```

after identifying the output bases. A Schur channel leaves this diagonal unchanged, so it is masked exactly. $`\square`$

### Corollary 1: a common basis for finite families

Let $`\mathcal N_0=\mathrm{id},\mathcal N_1,\ldots,\mathcal N_m`$ be channels on the same finite-dimensional space. A single pure bipartite isometry masks the family exactly if and only if all $`\mathcal N_j`$ are Schur channels in one common basis.

**Proof.** Choose strictly positive weights $`p_j`$ with $`\sum_jp_j=1`$ and set

```math
\overline{\mathcal N}=\sum_{j=0}^m p_j\mathcal N_j.
```

An exact common masker also masks $`\overline{\mathcal N}`$. By Theorem 1, it has a complete basis of pure fixed states. For each such projector $`P_i`$,

```math
P_i=\sum_jp_j\mathcal N_j(P_i).
```

The right side is a convex combination of density operators. A pure state is an extreme point, so $`\mathcal N_j(P_i)=P_i`$ for every $`j`$. Theorem 1's pure-state argument makes each channel diagonal-Kraus in this same basis. The copying isometry proves the converse. $`\square`$

The identity reference is an assumption of the corollary. A general family with a different common marginal output is not silently included.

For a family of unitary channels containing identity, the corollary reduces to simultaneous diagonalizability of their unitary representatives, equivalently pairwise commutation. That exact unitary-family characterization is already established in [1]; the all-dimensional noisy-channel classification is the additional exact statement here.

## References

1. **Anna Honeycutt, Hailey Murray, and Eric Chitambar**, “Quantum channel masking,” *Physical Review A* **113**, 042457 (2026). [DOI: 10.1103/5r9z-k5qn](https://doi.org/10.1103/5r9z-k5qn). [arXiv:2510.09456v2](https://arxiv.org/html/2510.09456v2). Relevant material: the isometric channel-masking definition, Theorem 1 for unitary families, and the identity-containing noisy-qubit classification.

2. **Robin Blume-Kohout, Hui Khoon Ng, David Poulin, and Lorenza Viola**, “Information-preserving structures: A general framework for quantum zero-error information,” *Physical Review A* **82**, 062306 (2010). [DOI: 10.1103/PhysRevA.82.062306](https://doi.org/10.1103/PhysRevA.82.062306). [Author-hosted publication record and PDF](https://authors.library.caltech.edu/records/my2y3-p3p03). Relevant material: Theorem 5, on maximal fixed-state support, fixed-observable algebras, and distorted fixed-state algebras.

3. **Victor V. Albert**, “Asymptotics of quantum channels: conserved quantities, an adiabatic limit, and matrix product states,” *Quantum* **3**, 151 (2019). [DOI: 10.22331/q-2019-06-06-151](https://doi.org/10.22331/q-2019-06-06-151). [Open-access PDF](https://quantum-journal.org/papers/q-2019-06-06-151/pdf/). [arXiv:1803.00109](https://arxiv.org/abs/1803.00109). Relevant material: Proposition 1 on faithful Kraus commutation; Proposition 3 and Eq. (22) on asymptotic support corners.

4. **Dennis Kretschmann, Dirk Schlingemann, and Reinhard F. Werner**, “A continuity theorem for Stinespring's dilation,” *Journal of Functional Analysis* **255**, 1889–1904 (2008). [DOI: 10.1016/j.jfa.2008.07.023](https://doi.org/10.1016/j.jfa.2008.07.023). [arXiv:0710.2495](https://arxiv.org/abs/0710.2495). [Primary PDF](https://arxiv.org/pdf/0710.2495). Relevant material: Theorem 1, Eqs. (6)–(7), Lemma 5, and Proposition 6. The common enlarged representation, rather than an arbitrary fixed-size environmental unitary, is the form used here.
