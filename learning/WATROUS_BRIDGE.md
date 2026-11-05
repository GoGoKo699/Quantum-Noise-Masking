# Watrous bridge: from channel language to hidden noise

**Educational anchor:** John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018). The [author's official book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides chapter manuscripts and errata. This bridge uses section numbers and titles, because pagination differs between layouts. It links to the source without reproducing or distributing the book.

Imagine preparing a quantum system, allowing a known noise process to act, and then reversibly distributing the output into two shares. An observer receives one share. Can that observer tell whether the noise occurred? What changes if the observer also holds a reference previously entangled with the input? What can two observers learn by combining their records or their systems?

The project studies this experiment against an identity, or idle, baseline. The important distinction is between **information about the input** and **information about the noise acting on it**. A share can retain the first while revealing none of the second. The example below makes that distinction concrete before connecting it to the exact classification and its failure of uniform stability.

The [30-milestone map](MILESTONES.md) organizes the full scientific story. This page supplies a route from the anchor into that story; the authoritative statements and proofs remain in [science](../science/model.md).

## 1. The targeted route through the anchor

Use these sections when their associated project question arises. Reading the entire book is unnecessary for beginning the example.

| Project question | Verified Watrous location | Project destination |
|---|---|---|
| What does one observer retain? | [§2.1.3, reductions and purifications](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | [Marginal channels and reference](../science/model.md#reference-sensitive-local-leakage) |
| How is a noisy process represented? | [§§2.2.1–2.2.2, channels and their representations](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | [Exact masking](../science/exact_masking.md) |
| How well can two channels be distinguished? | [§§3.3.1–3.3.3, channel discrimination and distance](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | [Leakage definition](../science/model.md#reference-sensitive-local-leakage) |
| What are the noise families used here? | [§§4.1.2–4.1.3, Weyl and Schur channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | [Weyl example](../science/weyl_separation.md) |
| How can fixed observables constrain noise? | [§4.2.2, fixed points of unital channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | [Fixed-observable lemma](../science/exact_masking.md#lemma-2-the-faithful-fixed-observable-algebra) |

### Notation that changes between source and project

| Anchor convention | Repository convention |
|---|---|
| Operator or map adjoint, $`T^*`$ | $`T^\dagger`$ |
| Completely bounded trace norm | Diamond norm, $`\lVert\Phi\rVert_\diamond`$; distance includes an additional factor of one half |
| Choi operator $`J(\Phi)`$, §2.2.2 | The normalized Choi state is $`J(\Phi)/d`$, where $`d`$ is the input dimension |
| Weyl dimension $`n`$, shift $`U`$, clock $`V`$, phase $`\zeta`$ | $`d,X_d,Z_d,\omega`$; the repository's $`V`$ instead denotes an encoder |
| Schur multiplier matrix $`A`$, §4.1.3 | Correlation matrix $`C`$; output share $`A`$ is a different object |

In particular, the book's Weyl convention gives $`W_{a,b}=U^aV^b`$ and $`VU=\zeta UV`$. It agrees with the project after the stated renaming; reversing the order would change phase formulas.

## 2. The experiment added to the channel formalism

Let $`H`$ denote the input space and let $`\mathcal N`$ be its noise channel. An isometry $`V:H\to A\otimes B`$ preserves inner products and maps the noisy output into two retained shares. Write

```math
\mathcal V(\rho)=V\rho V^\dagger,
\qquad
M_A=\operatorname{Tr}_B\circ\mathcal V,
\qquad
M_B=\operatorname{Tr}_A\circ\mathcal V.
```

The partial trace describes the information available to an observer who holds only one share. It does not mean that the other share is physically destroyed. The two channels $`M_A`$ and $`M_B`$ are complementary outputs of the same pure encoder.

The quantity of interest is

```math
\varepsilon_V(\mathcal N)
=\max_{S\in\{A,B\}}
\frac12\lVert M_S\circ\mathcal N-M_S\rVert_\diamond.
```

Here the first experiment applies noise before encoding; the second encodes the unchanged input. The diamond norm allows every input state and an untouched reference held by the observer. With equal prior probabilities, that observer's optimal success probability is at most $`(1+\varepsilon_V(\mathcal N))/2`$. Zero leakage means that the two local experiments are identical, including their correlations with the reference.

The encoder may use a counted pure ancilla, but it retains exactly two outputs and discards no secret key. The observer does not receive the noise environment or its kick record. The task is also different from error correction: reversing the encoder recovers $`\mathcal N(\rho)`$, not automatically the original $`\rho`$. These restrictions and the identity baseline are part of the [model](../science/model.md).

## 3. A complete example: phase noise hidden by one controlled operation

This example uses one input qubit, one clean ancillary qubit, and a controlled-NOT. It illustrates exact masking. It does not establish the later counterexample about approximate masking.

### 3.1 Specify the state and noise

In the basis $`\lvert0\rangle,\lvert1\rangle`$, write an arbitrary input state as

```math
\rho=
\begin{pmatrix}
a&c\\
\overline c&1-a
\end{pmatrix},
\qquad
0\le a\le1,
\qquad
\lvert c\rvert^2\le a(1-a).
```

The diagonal numbers are the probabilities of the two basis outcomes. The off-diagonal number $`c`$ records coherence between those alternatives. The last condition ensures that the matrix is a physical state.

Let a phase flip occur with known probability $`p`$:

```math
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\mathcal N_p(\rho)=(1-p)\rho+pZ\rho Z,
\qquad 0\le p\le1.
```

The Kraus operators $`\sqrt{1-p}\,I`$ and $`\sqrt p\,Z`$ describe this channel. Direct multiplication gives

```math
\mathcal N_p(\rho)=
\begin{pmatrix}
a&(1-2p)c\\
(1-2p)\overline c&1-a
\end{pmatrix}.
```

The noise preserves both populations and changes the coherence. At $`p=1/2`$ it removes the coherence completely; at $`p=1`$ it reverses its sign.

### 3.2 Encode coherently

Prepare the ancilla in $`\lvert0\rangle`$ and apply a controlled-NOT from the input to the ancilla. Call the original qubit $`A`$ and the ancilla $`B`$. The resulting isometry is

```math
V\lvert0\rangle=\lvert00\rangle,
\qquad
V\lvert1\rangle=\lvert11\rangle.
```

This copies basis labels, not arbitrary quantum states. For instance, it maps $`\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$ to an entangled state rather than to two copies of $`\lvert+\rangle`$. The basis-copy isometry is itself standard; Watrous already uses it in §4.1.3, Eq. (4.117). The calculation here identifies what it hides in this experiment.

Set $`\lambda=1-2p`$. The two-share output is

```math
\begin{aligned}
\sigma_p=V\mathcal N_p(\rho)V^\dagger
={}&a\lvert00\rangle\langle00\rvert
+(1-a)\lvert11\rangle\langle11\rvert\\
&+\lambda c\lvert00\rangle\langle11\rvert
+\lambda\overline c\lvert11\rangle\langle00\rvert.
\end{aligned}
```

No measurement has selected a basis label, and both qubits are retained.

### 3.3 Inspect either share, including a reference

Tracing out either qubit removes the cross terms because the two basis vectors of the discarded qubit are orthogonal. Thus

```math
\operatorname{Tr}_B\sigma_p
=\operatorname{Tr}_A\sigma_p
=a\lvert0\rangle\langle0\rvert
+(1-a)\lvert1\rangle\langle1\rvert.
```

The answer is independent of $`p`$. It still depends on $`a`$: input $`\lvert0\rangle`$ and input $`\lvert1\rangle`$ are perfectly distinguishable from either share. The input has therefore not been universally hidden.

To check the stronger reference-sensitive statement, write an arbitrary input-reference state in operator blocks,

```math
\rho_{HR}=\sum_{i,j=0}^1
\lvert i\rangle\langle j\rvert\otimes R_{ij}.
```

The blocks $`R_{ij}`$ are operators on the reference; they need not individually be states. The same calculation gives, for either share $`S`$,

```math
[(M_S\circ\mathcal N_p)\otimes\mathrm{id}_R](\rho_{HR})
=\sum_{i=0}^1\lvert i\rangle\langle i\rvert_S\otimes R_{ii}
=(M_S\otimes\mathrm{id}_R)(\rho_{HR}).
```

This is an identity for every input-reference state, so $`\varepsilon_V(\mathcal N_p)=0`$. Checking only the two reduced states for input $`\lvert+\rangle`$ would not have established that universal channel statement.

### 3.4 Detect the change through correlations

Now choose input $`\lvert+\rangle`$ and define the two orthogonal Bell states

```math
\lvert\Phi_\pm\rangle
=\frac{\lvert00\rangle\pm\lvert11\rangle}{\sqrt2}.
```

The baseline output is $`\lvert\Phi_+\rangle\langle\Phi_+\rvert`$, while the noisy output is

```math
\sigma_p=(1-p)\lvert\Phi_+\rangle\langle\Phi_+\rvert
+p\lvert\Phi_-\rangle\langle\Phi_-\rvert.
```

Either qubit by itself is maximally mixed under both hypotheses. But the observable $`X\otimes X`$, where $`X\lvert0\rangle=\lvert1\rangle`$ and $`X\lvert1\rangle=\lvert0\rangle`$, has expectation

```math
\operatorname{Tr}[(X\otimes X)\sigma_p]=1-2p.
```

One can measure $`X`$ on each qubit and multiply the two outcomes. The product is negative with probability $`p`$ after noise and never negative in the baseline experiment. Combining those measurement records accesses a correlation and is outside the one-share guarantee.

The half-trace distance of the two joint states is $`p`$, giving optimal equal-prior success probability $`(1+p)/2`$. This input attains the channel distance $`D_\diamond(\mathcal N_p,\mathrm{id})=p`$: the reverse bound follows from $`\mathcal N_p-\mathrm{id}=p(\operatorname{Ad}_Z-\mathrm{id})`$ and the fact that two channels have half-diamond distance at most one.

Finally, applying the controlled-NOT again returns $`\mathcal N_p(\rho)\otimes\lvert0\rangle\langle0\rvert`$. The encoder was reversible, but this reversal alone does not undo the noise. The example exhibits complete local invisibility of a change that remains visible in two-share correlations.

## 4. The missing steps from the example to the project

### From one exact mechanism to the whole exact class

The example's multiplier matrix is

```math
C_p=\begin{pmatrix}1&1-2p\\1-2p&1\end{pmatrix}.
```

It has unit diagonal and nonnegative eigenvalues $`2p`$ and $`2(1-p)`$. Thus it is a Schur channel of the kind introduced by the anchor. Basis copying masks any Schur channel in its defining basis, because both marginal outputs depend only on the unchanged diagonal. In higher dimensions, Schur channels need not be mixtures of diagonal unitary gates; the classification includes those channels too.

The difficult direction is the converse: why must every exactly maskable CPTP map have such a basis? The [exact-classification proof](../science/exact_masking.md) excludes transient stationary support and nontrivial noisy tensor factors, then obtains a complete pure fixed basis. The unital fixed-point result in Watrous §4.2.2 is helpful background, but the channel under investigation is not assumed unital. That assumption must not be inserted at the start of the project proof. These steps connect the example to [M14–M16](MILESTONES.md#m14--why-a-transient-sector-cannot-survive-exact-masking).

### From exact invariance to small marginal changes

For a finite gate family, [coherent averaging](../science/approximate_gates.md) retains a label register while averaging controlled products of known gates. On the system share, translating a finite averaging window changes only its boundary. On the label share, nearly commuting gates make the corresponding change small.

The converse follows a different route. Stinespring continuity turns approximate invariance of a marginal into an approximate representative of a gate on the opposite share. Representatives on separate shares commute. Comparing them with the original gates bounds the original commutators. The project uses contractions obtained from a sufficiently enlarged common environment; it does not assume the sharp bound for a unitary acting on every prescribed small environment.

Together these arguments give dimension-independent implications between small leakage and small operator commutators for fixed family size. Their error exponents are not matched. The detailed constants and hypotheses belong to the [quantitative theorem](../science/approximate_gates.md#theorem-2-quantitative-equivalence), corresponding to [M17–M19](MILESTONES.md#m17--local-invariance-forces-almost-commuting-gates).

### Why approximate hiding need not resemble exact hiding

The clock and shift have $`Z_dX_d=\omega X_dZ_d`$. Their matrix commutator becomes small as $`d`$ grows, although they have a nonzero winding index. Their conjugation channels commute exactly; this does not remove the obstruction for the implementing matrices.

The project uses these gates in one noise channel,

```math
\mathcal N_d=
\frac{\mathrm{id}+\operatorname{Ad}_{X_d}+\operatorname{Ad}_{Z_d}}3.
```

An explicit pure encoder achieves vanishing marginal leakage using two shares of dimension at most $`d`$. Yet, for every $`d\ge3`$,

```math
D_\diamond(\mathcal N_d,\mathrm{id})=\frac23,
\qquad
\inf_{\mathcal S\in\mathfrak M_d}
D_\diamond(\mathcal N_d,\mathcal S)\ge\frac1{48},
```

where $`\mathfrak M_d`$ is the entire exact masking class. The noise remains strong globally and separated from every channel with a perfect masking mechanism. Small local signatures therefore do not justify a nearby exact Schur description uniformly in dimension.

The [single-channel proof](../science/weyl_separation.md) explains the critical extra step: a hypothetical nearby Schur channel would, through Stinespring continuity, produce two common diagonal approximants to the Weyl gates. Polar normalization would produce nearby commuting unitaries, contradicting the inherited winding obstruction. This is the route through [M20–M26](MILESTONES.md#m20--a-concrete-family-of-noisy-weyl-channels), not a consequence of a textbook definition alone.

### What the implementation account adds

For $`d=2^{2m}`$, the [resource account](../science/resources_and_stability.md) gives an encoder with $`4m`$ qubits in total, including the $`2m`$ input qubits. It specifies the Fourier-addition circuit, precision budget, and perturbation estimates. Decreasing implementation-error budgets gives a sufficient guarantee that the advertised leakage bound vanishes. Fixed error budgets can leave nonvanishing terms in that upper bound; this does not prove that every fixed error causes actual leakage. These resource and stability questions are [M27–M28](MILESTONES.md#m27--a-circuit-with-all-registers-charged).

## 5. Where each level of the explanation comes from

**Book foundations.** Watrous supplies the channel representations, marginal-state language, operational norm, and Weyl/Schur examples used to formulate the problem. The worked calculation above is supplied here using those standard objects.

**Project derivations.** The repository supplies the arbitrary-dimensional exact classification, coherent finite averaging, the quantitative gate criterion, the extraction from an arbitrary Schur comparator, and the combination into a failure of uniform stability. Follow the [scientific reading route](../science/model.md#reading-route) for their proofs rather than treating the bridge as a replacement.

**Primary research ingredients.** These are proof dependencies and attribution sources, not additional educational anchors:

- [Honeycutt–Murray–Chitambar](https://arxiv.org/html/2510.09456v2) establishes the channel-masking model, the exact unitary-family criterion, and the noisy-qubit predecessor.
- [Kretschmann–Schlingemann–Werner, Theorem 1 and Lemma 5](https://arxiv.org/abs/0710.2495) supplies common-representation Stinespring continuity used in both quantitative converses.
- [Loring, Theorem 2.3](https://sigma-journal.com/2014/077/sigma14-077.pdf) supplies the quantitative obstruction to commuting approximants. The winding index and Weyl obstruction are established mathematics.
- Fixed-space structure and the circuit/synthesis ingredients have their sources identified in [exact masking](../science/exact_masking.md#references) and [resources](../science/resources_and_stability.md#references-and-inherited-ingredients).

The [related-work account](../references/RELATED_WORK.md) distinguishes approximate state masking, approximate commuting-algebra results, and earlier topology in masking from the precise contribution here. [M29–M30](MILESTONES.md#m29--attribution-evidence-and-remaining-quantitative-limits) put those boundaries together with the complete scientific statement.

## 6. Continue through the understanding map

The worked example supports [M02–M07](MILESTONES.md#m02--reduced-states-correlations-and-references), the operational synthesis [M12](MILESTONES.md#m12--the-complete-operational-question), the exact mechanism [M13](MILESTONES.md#m13--the-basis-copying-mechanism), and global discrimination [M25](MILESTONES.md#m25--the-noise-remains-visible-globally). The later sections connect that mechanism to the project's harder converse and stability questions. Use [MILESTONES.md](MILESTONES.md) for their dependency order and source pointers.

The endpoint is a precise distinction: **exact local invisibility forces a basis-preserving noise structure, while increasingly accurate local invisibility need not approach that structure as dimension grows.** The statement concerns a fixed finite family, a one-use experiment, a pure two-share encoder, and reference-sensitive local tests. It does not claim universal input-state masking, optimal resource costs, or privacy after arbitrary subsequent communication and computation.
