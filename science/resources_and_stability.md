# Finite implementation and perturbation stability of Weyl noise masking

This account concerns the supported bipartite isometric masking construction for the channel

```math
\mathcal N_d=\frac13\bigl(\mathrm{id}+\operatorname{Ad}_{X_d}
+\operatorname{Ad}_{Z_d}\bigr).
```

It supplies an explicit circuit, charges its registers and gate precision, and proves stability under channel and encoder errors. It does not assert an optimal leakage exponent, minimal share dimension, or a particular hardware implementation. The mathematical masking encoder remains a coherent isometry with a pure ancillary input and two retained shares.

## 1. Conventions and the finite statement

For linear maps, $`\|\cdot\|_\diamond`$ denotes the unhalved completely bounded trace norm. For two channels define

```math
D_\diamond(\Phi,\Psi):=\frac12\|\Phi-\Psi\|_\diamond.
```

Thus $`D_\diamond`$ ranges from zero to one. All channel errors below use this half-diamond convention. Operator norms are denoted $`\|\cdot\|_\infty`$ and are never halved.

For an encoder channel $`\mathcal E:S\to AB`$, define its leakage about the presence of $`\mathcal N`$, with identity as the fixed baseline, by

```math
\varepsilon_{\mathcal E}(\mathcal N)
=\max_{J=A,B}D_\diamond
\left(\operatorname{Tr}_{J^c}\mathcal E\mathcal N,
\operatorname{Tr}_{J^c}\mathcal E\right).
\tag{1}
```

The same encoder is used under both hypotheses. The diamond norm allows an arbitrary reference correlated with the input; a reference of dimension $`d=\dim S`$ suffices. This condition hides the action of the specified channel relative to identity. It does not require the shares to hide the input state itself.

Use the convenient family

```math
m\ge1,\qquad L=2^m,\qquad d=L^2=2^{2m}.
\tag{2}
```

The input has $`2m`$ qubits. The encoder adds $`2m`$ clean qubits, and its two output shares each have $`2m`$ qubits. An explicit ideal circuit has the following counts in a model with arbitrary pairwise two-qubit controlled-phase gates:

| Resource | Count |
|---|---:|
| Unknown input qubits | $`2m`$ |
| Clean ancillary qubits, retained in share A | $`2m`$ |
| Total encoder qubits | $`4m`$ |
| Additional work qubits | $`0`$ |
| Hadamard gates | $`6m`$ |
| Two-qubit controlled-phase gates | $`7m^2-m`$ |
| SWAP gates | $`2m`$ |

Write $`\varepsilon_m=\varepsilon_V(\mathcal N_d)`$ for the ideal leakage. It satisfies

```math
\varepsilon_m\le
\frac23\max\left\{2^{-m},
\sin\left[\frac{\pi(2^m-1)}{2^{2m}}\right]\right\}
\le\frac{2\pi}{3}\,2^{-m}.
\tag{3}
```

The input noise remains a constant distance from the exactly maskable class:

```math
\inf_{\mathcal S\in\mathfrak M_d}
D_\diamond(\mathcal N_d,\mathcal S)\ge\frac1{48}.
\tag{4}
```

Here $`\mathfrak M_d`$ includes Schur channels in every orthonormal basis. The project's exact classification identifies this set with channels exactly maskable against identity by a bipartite isometry. The baseline, input dimension, and two-share isometric model are part of that identification.

If an actual channel and a common actual encoder satisfy

```math
\eta=D_\diamond(\widetilde{\mathcal N},\mathcal N_d),
\qquad
\kappa=D_\diamond(\widetilde{\mathcal E},\operatorname{Ad}_V),
\tag{5}
```

then

```math
\boxed{
\varepsilon_{\widetilde{\mathcal E}}(\widetilde{\mathcal N})
\le\varepsilon_m+\eta+\frac43\kappa,
\qquad
\inf_{\mathcal S\in\mathfrak M_d}
D_\diamond(\widetilde{\mathcal N},\mathcal S)
\ge\left(\frac1{48}-\eta\right)_+.
}
\tag{6}
```

For a coherent implemented isometry $`W`$, the encoder error obeys

```math
\kappa\le
\tau:=\inf_{\theta\in\mathbb R}
\|W-e^{i\theta}V\|_\infty.
\tag{7}
```

The global-phase minimization is explicit because that phase has no channel meaning. Bounds stated instead with $`\|W-V\|_\infty`$ are valid without this minimization and can only be weaker.

## 2. Encoder convention and the leakage input

The [Weyl construction](weyl_separation.md) fixes $`ZX=\omega XZ`$ with $`\omega=e^{2\pi i/d}`$ and proves the exact finite leakage bound used in (3). Its encoder is

```math
V|\psi\rangle=\frac1L\sum_{a,b=0}^{L-1}|a,b\rangle_A\otimes X^aZ^b|\psi\rangle_B.
\tag{8}
```

The labels remain coherent. Orthogonality of their basis states gives $`V^\dagger V=I`$. The phase-arc estimate in the Weyl proof requires $`L-1\le d/2`$, which holds throughout the sequence (2). The proof also supplies the global distance in (17) and the all-Schur separation in (4). This page develops their implementation and perturbation consequences.

## 3. Explicit circuit on qubits

### 3.1 Registers and operator ordering

Use two m-qubit label registers, denoted a and b, and a $`2m`$-qubit input register B. Set $`A=ab`$. Both labels start in $`|0\rangle^{\otimes m}`$. Apply a Hadamard to every label qubit, giving

```math
\frac1L\sum_{a,b=0}^{L-1}|a,b\rangle.
```

Next apply the controlled operation $`Z^b`$ to B, followed by the controlled operation $`X^a`$. This order is important: the branch operator in (8) is $`X^aZ^b`$.

The resulting isometry is (8) for every input, including an input entangled with a reference. All label qubits remain in output share A. There are no carry qubits, discarded encoder records, postselected outcomes, or measurements.

### 3.2 Controlled phase from binary digits

Let $`n=2m`$, and write

```math
b=\sum_{r=0}^{m-1}2^r b_r,\qquad
j=\sum_{s=0}^{n-1}2^s j_s.
```

The operation $`Z^b`$ multiplies $`|b\rangle|j\rangle`$ by

```math
\omega^{bj}
=\prod_{\substack{0\le r\lt m,\ 0\le s\lt n\\r+s\lt n}}
\exp\left(\frac{2\pi i\,2^{r+s}}{2^n}b_rj_s\right).
\tag{12}
```

Terms with $`r+s\ge n`$ are integer multiples of $`2\pi`$ and can be omitted. Thus the controlled phase is exactly the product of two-qubit gates

```math
\mathrm{CP}(\theta_{rs})
=\operatorname{diag}(1,1,1,e^{i\theta_{rs}}),
\qquad
\theta_{rs}=\frac{2\pi}{2^{n-r-s}},
\tag{13}
```

between label qubit $`b_r`$ and data qubit $`B_s`$. Its gate count is

```math
G_m=\sum_{r=0}^{m-1}(2m-r)=\frac{3m^2+m}{2}.
\tag{14}
```

This factorization is diagonal and exact; the gates can be applied in any order within this phase block.

### 3.3 Controlled addition through the Fourier transform

Define the Fourier transform with the positive-sign convention

```math
F_d|j\rangle=\frac1{\sqrt d}\sum_{k=0}^{d-1}\omega^{jk}|k\rangle.
```

Then

```math
F_dX=ZF_d,\qquad X^a=F_d^\dagger Z^aF_d.
\tag{15}
```

Consequently the controlled $`X^a`$ operation is implemented by applying $`F_d`$ to B, applying the phase block (12) with label a, and applying $`F_d^\dagger`$ to B. This is the established Fourier-adder method [R1], specialized here to an m-bit addend and a $`2m`$-bit target modulo $`2^{2m}`$. The modulus is important: no overflow output or carry register is required.

In chronological order the complete encoder is:

1. Prepare uniform coherent a and b labels with $`2m`$ Hadamards.
2. Apply the b-controlled phase block.
3. Apply $`F_d`$ to B.
4. Apply the a-controlled phase block.
5. Apply $`F_d^\dagger`$ to B.

In a conventional exact n-qubit QFT circuit, each transform uses n Hadamards, $`n(n-1)/2`$ controlled phases, and $`\lfloor n/2\rfloor`$ swaps for bit reversal. Keeping those swaps explicitly and taking $`n=2m`$, the complete encoder uses

```math
2m+2(2m)=6m
```

Hadamards,

```math
2G_m+2\frac{(2m)(2m-1)}2=7m^2-m
\tag{16}
```

controlled phases, and $`2m`$ swaps. These are sufficient counts for the displayed circuit, not optimality statements. Bit reversal can instead be tracked by wire conventions, but that optimization is unnecessary.

The gate count assumes direct gates between the selected pairs of qubits. It is an abstract logical-circuit count; routing, physical gate durations, and fault-tolerant overhead require an architecture-specific account. The circuit is generated from binary arithmetic and known angles, without loading a $`d\times d`$ matrix or using a data-access oracle.

### 3.4 Decoder and reference-assisted global test

Let U denote the complete unitary circuit, including the label Hadamards. Then

```math
V|\psi\rangle=U(|0\rangle_A\otimes|\psi\rangle_B).
```

A joint receiver applies $`U^\dagger`$, recovering the input to the encoder in B and returning A to its initial pure state. When noise was applied before the encoder, this recovers $`\mathcal N_d(\rho)`$; it does not undo the noise itself.

The global distinction has an efficient witness. Introduce a $`2m`$-qubit reference R and prepare $`|\Phi_d\rangle=d^{-1/2}\sum_j|j\rangle_R|j\rangle_B`$, using $`2m`$ Bell pairs. The three vectors $`(I\otimes I)|\Phi_d\rangle`$, $`(I\otimes X)|\Phi_d\rangle`$ and $`(I\otimes Z)|\Phi_d\rangle`$ are orthogonal, so

```math
D_\diamond(\mathcal N_d,\mathrm{id})=\frac23.
\tag{17}
```

Isometric encoding preserves this distance. After joint decoding, subtract R from B modulo d and apply $`F_d^\dagger`$ to R. Indeed,

```math
\frac1{\sqrt d}\sum_j\omega^{bj}|j\rangle_R|j+a\rangle_B
\longmapsto |b\rangle_R|a\rangle_B.
```

Thus the three Weyl branches can be read out in a generalized Bell basis using another Fourier-adder circuit. A test of identity versus the mixture succeeds with probability $`5/6`$ under equal priors. Perfect discrimination applies to the three separate unitary channels, not to identity versus their mixture.

The encoder by itself has $`4m`$ qubits. This optional reference-assisted global test has $`6m`$ qubits while the encoded state is retained, counting R explicitly. The reference is not an encoder ancilla and does not help either marginal evade its diamond-norm leakage bound.

## 4. Finite gate sets and the precision budget

The exact gate count above uses dyadic controlled phases as available gates. Those gates have finite mathematical descriptions, but most are not exactly realizable by a fixed Clifford+T alphabet. The finite-alphabet implementation therefore uses approximation with a declared error budget.

For $`P(\varphi)=\operatorname{diag}(1,e^{i\varphi})`$,

```math
\mathrm{CP}(\theta)
=\bigl(P(\theta/2)\otimes P(\theta/2)\bigr)
\mathrm{CNOT}\bigl(I\otimes P(-\theta/2)\bigr)\mathrm{CNOT}.
\tag{18}
```

This identity follows on a basis state with bits c,t from
$`(c+t-(c\mathbin{\oplus}t))\theta/2=ct\theta`$.
Each controlled phase therefore costs two CNOTs and three single-qubit phase rotations. Replacing every swap by three CNOTs gives sufficient counts of

```math
14m^2+4m\quad\text{CNOTs},\qquad
3(7m^2-m)\quad\text{single-qubit phase rotations},
\tag{19}
```

in addition to the $`6m`$ Hadamards. No extra qubits are introduced.

Let $`C_m=7m^2-m`$. If the rotations in (18) are each approximated, up to an overall single-qubit phase, within operator norm $`\zeta`$, the complete unitary circuit is within $`3C_m\zeta`$ of U up to one overall circuit phase. This is the telescoping product inequality for unitary matrices. Restricting the ancillary input to $`|0\rangle_A`$ gives

```math
\inf_\theta\|W-e^{i\theta}V\|_\infty\le3C_m\zeta.
\tag{20}
```

Consequently, choosing $`\zeta=\tau/(3C_m)`$ ensures encoder half-diamond error at most $`\tau`$. Global phases used to compare single-qubit matrices combine into a single irrelevant circuit phase; no conditional relative phase is discarded.

The Solovay–Kitaev construction supplies an ancilla-free compilation of each single-qubit rotation into a fixed finite inverse-closed universal gate alphabet with length
$`O(\log^c(1/\zeta))`$ for a universal constant c; the standard Dawson–Nielsen account gives an exponent about 3.97 [R2]. Thus a sufficient total length is

```math
O\!\left(m^2\log^c\frac{m^2}{\tau}\right),
\tag{21}
```

with the same $`4m`$ qubits. This is deliberately a conservative compilation bound. It is not an optimal T-count claim.

Taking $`\tau=2^{-m}`$ keeps the compiled encoder size polynomial in m while retaining leakage $`O(2^{-m})`$. The target absolute precision per phase rotation is then $`O(2^{-m}/m^2)`$, requiring $`O(m+\log m)`$ fractional bits to specify to that accuracy. No claim of a fixed nonzero physical gate-error floor being sufficient is made.

In a model of imperfect gate channels, a separate telescoping inequality gives

```math
D_\diamond(\widetilde U_g\cdots\widetilde U_1,
U_g\cdots U_1)
\le\sum_{\ell=1}^g D_\diamond(\widetilde U_\ell,U_\ell).
\tag{22}
```

This is an error budget, not a hardware noise threshold. A desired total encoder error $`\kappa`$ must be met by the synthesized or fault-tolerant logical gates, including state preparation if it is imperfect.

## 5. Perturbation theorem and proof

### 5.1 Converting an isometry error into a channel error

For two isometries V,W and any trace-class operator Q, including a reference,

```math
WQW^\dagger-VQV^\dagger
=(W-V)QW^\dagger+VQ(W^\dagger-V^\dagger).
```

The trace norm is bounded by $`2\|W-V\|_\infty\|Q\|_1`$. Taking the stabilized norm and dividing by two proves (7), also after optimizing the global phase. The same argument applies to full implementing unitaries and then to their restriction to the fixed ancillary input.

### 5.2 Leakage under a common encoder error and channel error

Put $`\mathcal E=\operatorname{Ad}_V`$ and let $`\mathcal T_J=\operatorname{Tr}_{J^c}`$. The following exact decomposition is useful:

```math
\begin{aligned}
\mathcal T_J\widetilde{\mathcal E}
(\widetilde{\mathcal N}-\mathrm{id})
={}&\mathcal T_J\mathcal E(\mathcal N_d-\mathrm{id})\\
&+\mathcal T_J(\widetilde{\mathcal E}-\mathcal E)
(\mathcal N_d-\mathrm{id})\\
&+\mathcal T_J\widetilde{\mathcal E}
(\widetilde{\mathcal N}-\mathcal N_d).
\end{aligned}
\tag{23}
```

Channels have diamond norm one, and the diamond norm is submultiplicative. Equation (17) gives
$`\|\mathcal N_d-\mathrm{id}\|_\diamond=4/3`$. The half-diamond norm of the second term is therefore at most
$`(1/2)(2\kappa)(4/3)=4\kappa/3`$, and that of the third term is at most $`\eta`$. Taking the maximum over J proves the leakage bound in (6).

The simpler bound $`\varepsilon_m+\eta+2\kappa`$ is also valid. The $`4/3`$ coefficient uses this particular channel's distance from identity. The improved coefficient assumes the same actual encoder under both hypotheses; it does not describe two unrelated implementations chosen according to the hidden hypothesis.

The proof permits any CPTP $`\widetilde{\mathcal E}`$ and is consequently useful for assessing implementation noise. For the mathematical statement within the pure-ancilla masking model, take $`\widetilde{\mathcal E}=\operatorname{Ad}_W`$ with W an isometry. General CPTP encoder imperfections may introduce an uncontrolled environment; they are covered as errors, not redefined as admissible exact maskers.

### 5.3 Distance from the Schur class

For every Schur channel $`\mathcal S`$, the triangle inequality gives

```math
D_\diamond(\widetilde{\mathcal N},\mathcal S)
\ge D_\diamond(\mathcal N_d,\mathcal S)-\eta.
```

Taking the infimum and using (4) proves the second assertion in (6). Encoder error does not enter this bound: it concerns the underlying d-to-d noise channel, while Schur form is a property of that channel. If one instead asks about a noisy composite encoder with a different output dimension, the Schur-distance statement must not be transferred without redefining the comparison class.

The full proof of the $`1/48`$ input, including arbitrary Schur Kraus rank and common-environment alignment, is in [Weyl separation](weyl_separation.md#5-distance-from-every-exactly-maskable-channel).

### 5.4 Global distinguishability and decoding under errors

Applying the reverse triangle inequality to (23) without a partial trace proves

```math
D_\diamond(\widetilde{\mathcal E}\widetilde{\mathcal N},
\widetilde{\mathcal E})
\ge\left(\frac23-\eta-\frac43\kappa\right)_+.
\tag{24}
```

If the actual encoder is an isometry W, post-encoding preserves diamond distance exactly, so the stronger bound is

```math
D_\diamond(\operatorname{Ad}_W\widetilde{\mathcal N},
\operatorname{Ad}_W)
=D_\diamond(\widetilde{\mathcal N},\mathrm{id})
\ge\left(\frac23-\eta\right)_+.
\tag{25}
```

An ideal decoder for V also has a useful error guarantee. Complete $`V^\dagger(\cdot)V`$ to a CPTP left inverse $`\mathcal D_V`$ by assigning a fixed state to the orthogonal complement of the code space. Contractivity gives

```math
D_\diamond(\mathcal D_V\widetilde{\mathcal E},\mathrm{id})\le\kappa,
\qquad
D_\diamond(\mathcal D_V\widetilde{\mathcal E}
\widetilde{\mathcal N},\mathcal N_d)\le\kappa+\eta.
\tag{26}
```

These decoder bounds do not assume knowledge of the actual coherent error. If W is implemented by a known ideal finite-gate circuit, reversing that actual circuit instead decodes W exactly in the circuit model.

### 5.5 Optional error in the nominal identity experiment

If a laboratory baseline $`\widetilde{\mathcal I}`$ obeys
$`D_\diamond(\widetilde{\mathcal I},\mathrm{id})\le\eta_0`$, the same proof gives

```math
\max_J D_\diamond(\mathcal T_J\widetilde{\mathcal E}
\widetilde{\mathcal N},
\mathcal T_J\widetilde{\mathcal E}\widetilde{\mathcal I})
\le\varepsilon_m+\eta+\eta_0+\frac43\kappa.
\tag{27}
```

This is a calibration-error bound for the experiment. It does not replace the identity baseline in the exact classification or assert a new classification of arbitrary channel pairs.

## 6. A fully finite family and what robustness means

Choose $`\tau_m,\eta_m=O(2^{-m})`$ and compile a unitary encoder W with (20). Then

```math
\varepsilon_{\operatorname{Ad}_W}(\widetilde{\mathcal N})
=O(2^{-m}),\qquad
\operatorname{dist}_\diamond
(\widetilde{\mathcal N},\mathfrak M_d)
\ge\frac1{48}-O(2^{-m}).
\tag{28}
```

The encoder uses $`4m`$ qubits and a polynomial number of fixed-alphabet gates. Thus the instability survives finite circuit synthesis; an exact native gate of exponentially small angle is not required.

If one also wants to generate the noise channel through finite controls, suppose

```math
\widetilde{\mathcal N}=\sum_{j=0}^2 p_j
\operatorname{Ad}_{\widetilde U_j},
\qquad (U_0,U_1,U_2)=(I,X,Z).
```

Let $r_j=D_\diamond(\operatorname{Ad}_{\widetilde U_j},
\operatorname{Ad}_{U_j})$. Then

```math
\eta\le \frac12\sum_{j=0}^2|p_j-1/3|
+\sum_{j=0}^2p_jr_j.
\tag{29}
```

This follows by adding and subtracting $`\sum_jp_j\operatorname{Ad}_{U_j}`$. Each $`r_j`$ is at most the phase-optimized operator error in $`\widetilde U_j`$. Z is a product of known single-qubit phases, and $`X=F_d^\dagger ZF_d`$ gives a finite polynomial-size route to approximate X with the same synthesis method. This is separate from the masker's ancilla budget: the channel's random selector is part of the supplied noise mechanism, not a secret encoder key.

Uniform three-way randomness can also be approximated with a fixed number r of unbiased classical bits. Map the uniformly sampled integer in $`\{0,\ldots,2^r-1\}`$ to its residue modulo three. The resulting three probabilities have total-variation distance exactly $`2/(3\,2^r)`$ from uniform. Hence $`r=O(\log(1/\eta_m))=O(m)`$ classical random bits suffice for that part of (29), without rejection or postselection.

A fixed nonzero $`\eta`$ or $`\kappa`$ gives the finite leakage floor displayed in (6). Vanishing leakage requires those implementation errors to vanish; retaining the specific $`2^{-m}`$ rate requires errors of that order. At any fixed accuracy, however, separation from the Schur class remains positive whenever $`\eta\lt 1/48`$. There is no claim of a hardware fault-tolerance threshold, optimal precision cost, or noise-independent implementation accuracy.

The Weyl operators are known operations on a growing logical Hilbert space. Their polynomial circuit descriptions do not turn this example into an independent local-qubit-noise model. The proved payoff is reference-stable local invisibility with a jointly retained signal and constant separation from exact bipartite maskability.

## 7. Verification and finite examples

The [reproducible verifier](../verification/README.md) checks Weyl identities in six dimensions, all 25 matrix units of a nontrivial Schur example, and the qubit circuits at $`m=1,2,3`$. It builds the QFT gate by gate and compares every label branch with its direct permutation-and-phase action. The committed run has largest overall residual $`4.27\times10^{-14}`$ and largest circuit-branch residual below $`1.93\times10^{-15}`$. These are finite floating-point checks; the general identities and bounds are established above.

| m | Input qubits | Encoder qubits | Controlled-phase gates | Ideal leakage upper bound in (3) |
|---:|---:|---:|---:|---:|
| 4 | 8 | 16 | 108 | 0.122027 |
| 8 | 16 | 32 | 440 | 0.00814907 |
| 12 | 24 | 48 | 996 | 0.000511202 |

These are logical-circuit counts and analytical upper bounds, not measured device performance. No optimality claim relies on these small numerical checks.

## References and inherited ingredients

- **[R1]** Thomas G. Draper, *Addition on a Quantum Computer*, arXiv:quant-ph/0008033 (2000). [Primary PDF](https://arxiv.org/pdf/quant-ph/0008033). Sections 3 and 5 give the Fourier-transform and phase-addition construction. The no-carry adder is inherited; the register assignment and counts here are for the particular masking encoder.
- **[R2]** Christopher M. Dawson and Michael A. Nielsen, *The Solovay–Kitaev algorithm*, Quantum Information and Computation **6**, 81–95 (2006), arXiv:quant-ph/0505030v2. [Primary PDF](https://arxiv.org/pdf/quant-ph/0505030). Supplies fixed-alphabet single-qubit compilation with polylogarithmic dependence on inverse error. The conservative compilation estimate in (21) is sufficient; improved synthesis algorithms are not prerequisites.
- **[R3]** Dennis Kretschmann, Dirk Schlingemann and Reinhard F. Werner, *A Continuity Theorem for Stinespring's Dilation*, Journal of Functional Analysis **255**, 1889–1904 (2008), arXiv:0710.2495. [Primary PDF](https://arxiv.org/pdf/0710.2495). Theorem 1, Eqs. (6)–(7), supplies the common-representation bound $`\inf\|V_1-V_2\|_\infty\le\sqrt{\|\Phi_1-\Phi_2\|_\diamond}`$ in finite-dimensional Schrödinger-picture notation. The following paragraph explicitly permits the direct sum of minimal representations.
- **[R4]** Terry A. Loring, *Quantitative K-Theory Related to Spin Chern Numbers*, SIGMA **10**, 077 (2014). [Primary PDF](https://sigma-journal.com/2014/077/sigma14-077.pdf). Section 2 and Theorem 2.3 supply the nonzero-winding obstruction and the total operator-distance bound greater than $`\sqrt2`$. The topology and constant are inherited inputs, not new claims of this implementation account.
