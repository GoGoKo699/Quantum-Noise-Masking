# Approximate gate masking and almost commutation

Use the [model and norm conventions](model.md), with $`\alpha_V=M_A`$, $`\beta_V=M_B`$ and operator norm $`\|\cdot\|_\infty`$. The identity is included as the reference gate. The exact endpoint is proved in [Exact masking](exact_masking.md).

## 3. Two continuity lemmas with the norm conventions fixed

### Lemma 4: close isometries induce close channels

Let $`W_1,W_2:H\to K\otimes E`$ be isometries and let

```math
\Phi_i(X)=\mathrm{Tr}_E(W_iXW_i^\dagger).
```

Then

```math
\frac12\|\Phi_1-\Phi_2\|_\diamond
\le \|W_1-W_2\|_\infty.
```

**Proof.** Before tracing the environment, write the difference as

```math
(W_1-W_2)XW_1^\dagger
+W_2X(W_1^\dagger-W_2^\dagger).
```

The trace norm of either term, including an arbitrary identity map on a reference, is bounded by $`\|W_1-W_2\|_\infty\|X\|_1`$. Thus the full isometric channels differ by diamond norm at most $`2\|W_1-W_2\|_\infty`$. Postprocessing by the partial trace is diamond-norm contractive. $`\square`$

### Lemma 5: a contraction on the original environment

For the same two isometries, put $`D=\|\Phi_1-\Phi_2\|_\diamond`$. There is a contraction $`C:E\to E`$ such that

```math
\|W_1-(I_K\otimes C)W_2\|_\infty\le\sqrt D.
```

**Proof.** Stinespring continuity in a common enlarged environment gives isometries $`J_1,J_2:E\to F`$ such that

```math
\|(I_K\otimes J_1)W_1
-(I_K\otimes J_2)W_2\|_\infty
\le\sqrt D.
```

This is the channel specialization of the upper bound in KSW, Theorem 1, Eqs. (6)–(7) [4], together with uniqueness of minimal dilations. If the prescribed $`W_i`$ have unused environment dimensions, enlarge $`F`$ further and extend the corresponding embeddings isometrically; this does not change their action on $`W_i`$.

Apply $`I_K\otimes J_1^\dagger`$ to the difference. The operator $`C=J_1^\dagger J_2`$ has norm at most one and gives the claimed inequality. $`\square`$

The proof does **not** assert that $`C`$ can be chosen unitary on an arbitrary prescribed environment of the original size. The use of an enlarged common dilation is deliberate. The contraction acts on the original environment, and no extra physical output share is introduced.

For completeness, KSW's contraction formulation can also be obtained directly from its Lemma 5 and Proposition 6 [4]. Their completely bounded norm for adjoint maps is the diamond norm of the Schrödinger-picture channel difference.

## 4. Quantitative gate-masking theorem

Fix $`k\ge2`$ unitaries $`U_1,\ldots,U_k`$ on $`H`$, together with the identity as reference. Define

```math
\delta
=\max_{i,j}\|U_iU_j-U_jU_i\|_\infty
```

and

```math
\varepsilon_*(U_1,\ldots,U_k)
=\inf_V\max_{1\le j\le k}\varepsilon_V(\mathrm{Ad}_{U_j}),
```

where the infimum is over all finite-dimensional pure bipartite isometries. A global phase on a representative $`U_j`$ changes neither quantity.

### Theorem 2: quantitative equivalence

The following bounds hold:

```math
\boxed{
\frac{\delta^2}{32}
\le
\varepsilon_*(U_1,\ldots,U_k)
\le
\inf_{L\in\mathbb N,\ L\ge1}
\left[
\frac1L+(k-1)(L-1)\delta
\right].
}
```

For $`0\lt (k-1)\delta\lt 1`$, the explicit choice

```math
L=\left\lceil[(k-1)\delta]^{-1/2}\right\rceil
```

gives

```math
\varepsilon_*(U_1,\ldots,U_k)
\le2\sqrt{(k-1)\delta}.
```

The constructive encoder for a chosen $`L`$ has

```math
\dim A=L^k,\qquad \dim B=d.
```

If $`\delta=0`$, a common-eigenbasis encoder masks the family exactly with two $`d`$-dimensional shares. For a single nontrivial gate, exact masking is always possible by its eigenbasis, so the $`k\ge2`$ restriction merely avoids a vacuous commutator parameter.

The implications are dimension independent for fixed $`k`$. Their exponents are not matched, and this theorem does not claim an optimal dependence on $`\delta`$, $`k`$, or ancillary dimension.

### Proof of the upper bound

Let

```math
Q_L=\{0,\ldots,L-1\}^k,
\qquad
W_{\mathbf a}=U_1^{a_1}U_2^{a_2}\cdots U_k^{a_k},
```

and define

```math
V_L|\psi\rangle
=L^{-k/2}
\sum_{\mathbf a\in Q_L}
|\mathbf a\rangle_A\otimes W_{\mathbf a}|\psi\rangle_B.
```

Since the flag vectors are orthonormal and every $`W_{\mathbf a}`$ is unitary,

```math
V_L^\dagger V_L
=L^{-k}\sum_{\mathbf a\in Q_L}W_{\mathbf a}^\dagger W_{\mathbf a}
=I_H.
```

The register $`A`$ remains coherent and is retained as one of the two shares.

**The $`A`$ marginal.** Telescoping powers gives

```math
\|[U_i^{a_i},U_j]\|_\infty
\le a_i\|[U_i,U_j]\|_\infty
\le a_i\delta.
```

Commuting $`U_j`$ through the entire product therefore gives

```math
\|W_{\mathbf a}U_j-U_jW_{\mathbf a}\|_\infty
\le\sum_{i\ne j}a_i\delta
\le r,
\qquad
r=(k-1)(L-1)\delta.
```

Orthogonality of the flags implies

```math
\|V_LU_j-(I_A\otimes U_j)V_L\|_\infty\le r.
```

For example, the square of the norm on any input vector is the average of the squared norms of its flagged differences, each bounded by $`r^2`$. The two isometries induce $`\alpha_{V_L}\circ\mathrm{Ad}_{U_j}`$ and $`\alpha_{V_L}`$ after tracing $`B`$. Lemma 4 gives

```math
\frac12
\|\alpha_{V_L}\circ\mathrm{Ad}_{U_j}-\alpha_{V_L}\|_\diamond
\le r.
```

**The $`B`$ marginal.** It is the random-unitary channel

```math
\beta_{V_L}
=L^{-k}\sum_{\mathbf a\in Q_L}\mathrm{Ad}_{W_{\mathbf a}}.
```

Move an input $`U_j`$ only past the factors to its right. Extending the definition of $`W_{\mathbf a}`$ to nonnegative integer coordinates gives

```math
\|W_{\mathbf a}U_j-W_{\mathbf a+\mathbf e_j}\|_\infty
\le\sum_{i\gt j}a_i\delta
\le r.
```

Lemma 4 and convexity bound the half-diamond distance from
$`\beta_{V_L}\circ\mathrm{Ad}_{U_j}`$ to the translated-box mixture

```math
\widetilde\beta_j
=L^{-k}\sum_{\mathbf a\in Q_L}
\mathrm{Ad}_{W_{\mathbf a+\mathbf e_j}}
```

by $`r`$. The uniform measures on $`Q_L`$ and $`Q_L+\mathbf e_j`$ have total variation distance $`1/L`$: their intersection contains $`(L-1)L^{k-1}`$ of the $`L^k`$ labels. A random-unitary channel difference is bounded in half-diamond norm by the total variation distance of its label distributions, so

```math
\frac12\|\widetilde\beta_j-\beta_{V_L}\|_\diamond\le\frac1L.
```

The triangle inequality proves

```math
\frac12
\|\beta_{V_L}\circ\mathrm{Ad}_{U_j}-\beta_{V_L}\|_\diamond
\le r+\frac1L.
```

This applies to each gate and proves the finite-$`L`$ bound. Put $`t=(k-1)\delta`$. For $`L=\lceil t^{-1/2}\rceil`$, $`1/L\le\sqrt t`$ and $`(L-1)t\lt \sqrt t`$, proving the stated square-root estimate. For all parameters, the choice $`L=1`$ already gives the trivial upper bound one. $`\square`$

### Proof of the lower bound

Suppose an arbitrary encoder $`V`$ has leakage at most $`\varepsilon`$ for every gate. Fix two gates $`U_i,U_j`$ and set

```math
t=\sqrt{2\varepsilon}.
```

The marginal $`\beta_V\circ\mathrm{Ad}_{U_i}`$ has Stinespring isometry $`VU_i`$, with the $`A`$ share as its environment. Lemma 5 and the half-diamond convention produce a contraction $`A_i`$ on $`A`$ satisfying

```math
\|VU_i-(A_i\otimes I_B)V\|_\infty\le t.
```

Similarly, the invariance of $`\alpha_V`$ under $`U_j`$ produces a contraction $`B_j`$ on $`B`$ satisfying

```math
\|VU_j-(I_A\otimes B_j)V\|_\infty\le t.
```

Abbreviate

```math
\widehat A_i=A_i\otimes I_B,\qquad
\widehat B_j=I_A\otimes B_j,
```

and let

```math
E_i=VU_i-\widehat A_iV,\qquad
E_j=VU_j-\widehat B_jV.
```

The two contractions commute because they act on opposite shares. The exact identity

```math
\begin{aligned}
V(U_iU_j-U_jU_i)
&=
E_iU_j+\widehat A_iE_j-E_jU_i-\widehat B_jE_i
\end{aligned}
```

therefore yields

```math
\|[U_i,U_j]\|_\infty
=\|V[U_i,U_j]\|_\infty
\le4t=4\sqrt{2\varepsilon}.
```

Taking the maximum over pairs, squaring, and then taking the infimum over encoders proves

```math
\varepsilon_*\ge\frac{\delta^2}{32}.
```

No attainment of the encoder infimum is assumed. $`\square`$

## 5. Resource and interpretation boundaries

The coherent averaging construction is an explicit pure isometry. One implementation prepares $`k`$ uniform $`L`$-level flag registers and applies the controlled products in the order that realizes $`W_{\mathbf a}`$. The flags contain $`k\log_2 L`$ qubits of Hilbert-space dimension, before integer rounding of physical register widths. The output system $`B`$ retains the input dimension $`d`$.

The theorem charges these registers and does not provide cost-free powers of unknown unitary oracles. If controlled applications of known $`U_j`$ are supplied, each power can be implemented by repeated controlled applications; arbitrary matrix synthesis and gate approximation costs require their own implementation model. The special clock/shift construction can be analyzed separately with its known arithmetic circuits.

The upper bound hides the choice among the identity and the specified finite gates. It does not hide every product in their generated group. High powers can accumulate noncommutation, and a claim of arbitrary-circuit or indefinite-reuse privacy does not follow. The full reference norm is a strong one-use guarantee; ordinary multi-use diamond-error accumulation remains relevant.

Theorem 1 identifies the exact class, while Theorem 2 measures approximate masking in terms of almost commutation. Neither theorem states that almost-commuting unitaries are close to a commuting family. That distinct approximation question is where a topological obstruction can enter the single-noise counterexample.

## References

1. **Anna Honeycutt, Hailey Murray, and Eric Chitambar**, “Quantum channel masking,” *Physical Review A* **113**, 042457 (2026). [DOI: 10.1103/5r9z-k5qn](https://doi.org/10.1103/5r9z-k5qn). [arXiv:2510.09456v2](https://arxiv.org/html/2510.09456v2). Relevant material: the isometric channel-masking definition, Theorem 1 for unitary families, and the identity-containing noisy-qubit classification.

2. **Robin Blume-Kohout, Hui Khoon Ng, David Poulin, and Lorenza Viola**, “Information-preserving structures: A general framework for quantum zero-error information,” *Physical Review A* **82**, 062306 (2010). [DOI: 10.1103/PhysRevA.82.062306](https://doi.org/10.1103/PhysRevA.82.062306). [Author-hosted publication record and PDF](https://authors.library.caltech.edu/records/my2y3-p3p03). Relevant material: Theorem 5, on maximal fixed-state support, fixed-observable algebras, and distorted fixed-state algebras.

3. **Victor V. Albert**, “Asymptotics of quantum channels: conserved quantities, an adiabatic limit, and matrix product states,” *Quantum* **3**, 151 (2019). [DOI: 10.22331/q-2019-06-06-151](https://doi.org/10.22331/q-2019-06-06-151). [Open-access PDF](https://quantum-journal.org/papers/q-2019-06-06-151/pdf/). [arXiv:1803.00109](https://arxiv.org/abs/1803.00109). Relevant material: Proposition 1 on faithful Kraus commutation; Proposition 3 and Eq. (22) on asymptotic support corners.

4. **Dennis Kretschmann, Dirk Schlingemann, and Reinhard F. Werner**, “A continuity theorem for Stinespring's dilation,” *Journal of Functional Analysis* **255**, 1889–1904 (2008). [DOI: 10.1016/j.jfa.2008.07.023](https://doi.org/10.1016/j.jfa.2008.07.023). [arXiv:0710.2495](https://arxiv.org/abs/0710.2495). [Primary PDF](https://arxiv.org/pdf/0710.2495). Relevant material: Theorem 1, Eqs. (6)–(7), Lemma 5, and Proposition 6. The common enlarged representation, rather than an arbitrary fixed-size environmental unitary, is the form used here.
