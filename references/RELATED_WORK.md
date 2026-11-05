# Related work and contribution boundaries

## Operational question

Let $`\mathcal N`$ be a channel on a finite-dimensional input space $`H`$. A deterministic pure encoder is an isometry $`V:H\to A\otimes B`$, with complementary marginal channels

```math
\alpha=\operatorname{Tr}_B\circ\operatorname{Ad}_V,
\qquad
\beta=\operatorname{Tr}_A\circ\operatorname{Ad}_V.
```

We quantify how well either share can detect whether the prescribed channel acted before encoding by

```math
\varepsilon_V(\mathcal N)=\max\left\{
\tfrac12\|\alpha\mathcal N-\alpha\|_\diamond,
\tfrac12\|\beta\mathcal N-\beta\|_\diamond
\right\}.
```

The diamond norm allows the observer to hold an arbitrary reference entangled with the input. The encoder has no discarded key, mixed private randomness, or third share. It preserves the channel output globally, but need not remove the noise. Its marginals may retain information about the input state: the information being hidden is the change produced by a specified channel.

The central question is whether small local detectability forces the noise to be close to a channel that is exactly invisible under some pure bipartite encoder. The answer developed here is negative uniformly in dimension, even when both output shares have dimension no greater than the input dimension.

## Statements developed here

| Statement | Precise content | Established ingredients used |
|---|---|---|
| Exact noisy-channel classification | A finite-dimensional CPTP map is exactly maskable against the identity iff it is a Schur multiplier in some orthonormal basis. A finite family containing the identity is simultaneously maskable iff its members are Schur in a common basis. | Channel fixed-space structure; the impossibility of universal pure bipartite state masking; the operational model of channel masking. |
| Quantitative gate criterion | For a fixed finite family containing the identity, vanishing optimal marginal diamond leakage is equivalent, with dimension-independent moduli, to vanishing operator-norm commutators of the implementing unitaries. | Stinespring continuity; elementary coherent averaging and commutator estimates. |
| Single-noise separation | A three-branch Weyl noise channel has leakage tending to zero under an explicit pure encoder, remains a fixed distance from the identity, and stays a fixed diamond distance from every exactly maskable CPTP channel. | The exact classification, Stinespring continuity, and the established winding obstruction for almost commuting unitaries. |

For $`\delta=\max_{i,j}\|[U_i,U_j]\|`$, $`k\geq2`$ gates besides the identity, and optimal leakage $`\varepsilon_*`$, the quantitative statement is

```math
\frac{\delta^2}{32}\leq\varepsilon_*
\leq\inf_{L\in\mathbb N,\ L\ge1}\left\{\frac1L+(k-1)(L-1)\delta\right\}.
```

The upper bound is at most $`2\sqrt{(k-1)\delta}`$ when $`0\lt (k-1)\delta\lt 1`$, and uses a flag share of dimension $`L^k`$. These exponents are not matched. The statement concerns the commutators of the implementing unitaries, not commutators of their conjugation superoperators.

## Closest comparisons

### Exact channel masking

Honeycutt, Murray, and Chitambar [1] introduce the same pure-isometry channel-masking task. Their Theorem 1 characterizes exactly maskable unitary families through commutation of relative gates. With the identity included, this is pairwise commutation of the gates themselves. Their Theorem 3 characterizes a noisy qubit channel maskable against the identity by unitality and a pure fixed point; the paper also treats convex combinations and local orthogonality conditions.

The present exact classification extends the noisy-channel part to arbitrary finite dimension. That extension is a supporting result. The main additional content is quantitative approximate masking and its failure to imply proximity to any exactly maskable noisy channel. Neither the operational definition nor the exact unitary criterion is a contribution of this work.

### Approximate state masking

The universal pure-state no-masking theorem [2] concerns an encoder whose two marginal states reveal no information about an arbitrary input state. Li and Modi [3] consider probabilistic and approximate versions. In particular, their Definition 3 and Theorem 3 impose closeness of marginal outputs as the input state ranges over the entire input space, and derive dimension-dependent limitations.

Li, Shu, and Zhu [4] analyze random isometries and average or worst-case variation of marginal states. Their Theorem 1 excludes good universal approximate state masking by random bipartite subspaces in their setting; they also establish multipartite positive results. Section V.2 explicitly connects their analysis to approximate quantum error correction using reference-sensitive quantities, including a completely bounded purified distance. The distinction from the present problem is therefore not merely the availability of a reference. Their masking criterion suppresses input-state variation; ours asks whether specified transformations leave both marginal channels nearly invariant. Substantial input information can remain locally accessible in our construction, consistently with these state-masking limitations.

### Quantitative commuting-algebra results

Xu, Renou, and Klep [5] obtain approximate Schur lemmas and quantitative Tsirelson results for observable/algebra models. Their Lemma 2.1 uses clock and shift generators to control distance to scalar operators. Lemma 2.4 and Theorem 2.5 approximate one algebra by operators in another algebra's commutant, with bounds depending on dimension and polynomial representations of algebra generators. Their application compares approximately commuting and tensor-product correlation models.

These are related operator-approximation techniques, but do not give a pure encoding that makes both complementary channels invariant under a specified gate family. The present finite-gate criterion has moduli independent of input dimension for fixed family size, and the noisy-channel separation compares against the entire exact masking class. The general connection between approximate commutation and quantum subsystem structure is established background.

### Topology and masking

The obstruction to approximating certain almost commuting unitary pairs by commuting pairs is established mathematics. Loring [6, Theorem 2.3] supplies the quantitative bound used here. The clock/shift example, its nonzero winding index, and the operator-norm separation are inherited.

Topology also already appears in quantum masking: Zhu [7] characterizes masking of real quantum states using Hurwitz–Radon/Clifford structures, and Bott periodicity enters the available representation dimensions. That result concerns exact real-state masking and representation-size restrictions. Here a winding index of almost commuting complex unitary matrices obstructs approximation by exactly maskable noise. The contribution is this specific operational separation, not a first connection between topology and masking.

### Continuity and fixed-space structure

Kretschmann, Schlingemann, and Werner [8, Theorem 1 and Lemma 5] provide the common-representation Stinespring continuity theorem. We use its square-root estimate and project common-environment representatives either onto the original environment or onto canonical Kraus flags. These steps produce contractions or common diagonal approximants; they do not require a unitary alignment in an arbitrarily preassigned small environment.

The exact classification uses standard channel fixed-space structure [9,10]. Its [proof](../science/exact_masking.md) includes the needed finite-dimensional facts directly: the faithful fixed-observable commutant, annihilation of stationary-support coherences by the Cesàro projection, and the resulting algebra decomposition. These facts agree with Albert’s Propositions 1 and 3 and Eq. (22). Combining them with pure bipartite no-masking removes transient sectors and nontrivial noisy factors; the remaining pure fixed basis forces diagonal Kraus operators. The structural channel machinery is inherited.

## Why the noisy-channel comparison is unrestricted

The [separation proof](../science/weyl_separation.md#5-distance-from-every-exactly-maskable-channel) compares the Weyl mixture with every channel admitting exact pure bipartite masking. The exact classification permits a Schur dilation in an arbitrary basis; common-environment continuity preserves that diagonal structure. Projecting onto the canonical Weyl flags yields simultaneous diagonal approximants and then commuting unitary approximants, which the winding obstruction excludes. This covers arbitrary Schur Kraus rank and does not assume a random-unitary comparator. The enlarged environment is a proof representation, not an extra physical share.

## Physical interpretation and scope

Exact local invisibility forces noise to preserve a complete orthogonal basis and to act as a Schur multiplier in that basis. Vanishing local signatures do not force proximity to that structural class uniformly in dimension. The discrepancy can persist for a single noise channel of fixed global distinguishability, even when local signatures are tested with an arbitrary reference and both shares are only as large as the original system.

The result separates two statements that exact theory might otherwise conflate: a channel can become increasingly difficult to detect locally while remaining intrinsically separated from every channel admitting perfect local invisibility. The mechanism is almost commutation without a nearby commuting realization. No new topological invariant or continuity theorem is needed.

The dimension grows as leakage decreases, and the task concerns a fixed finite family and one use. It does not establish universal state masking, optimal error exponents, privacy for arbitrary circuits, indefinite reuse, or a practical cryptographic protocol. The environment of the noise channel and its classical kick record are inaccessible to the observers, as in the ordinary channel model. The pure bipartite restriction is essential: adding private randomness or another share changes the masking problem.

## Bibliography

The educational anchor is John Watrous, *The Theory of Quantum Information* (2018), available through the [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/). It supplies the channel, norm, Weyl and Schur foundations used in the [learning bridge](../learning/WATROUS_BRIDGE.md). In particular, the basis-copy isometry is a standard ingredient appearing in §4.1.3, Proposition 4.17; the bridge explains its channel-masking use. The research comparisons below and the cited continuity and topological results remain separate from that educational role.

1. Anna Honeycutt, Hailey Murray, and Eric Chitambar, “Quantum channel masking,” *Physical Review A* **113**, 042457 (2026). [Published article](https://doi.org/10.1103/5r9z-k5qn); [arXiv:2510.09456v2](https://arxiv.org/html/2510.09456v2).
2. Kavan Modi, Arun K. Pati, Aditi Sen(De), and Ujjwal Sen, “Masking Quantum Information is Impossible,” *Physical Review Letters* **120**, 230501 (2018). [DOI](https://doi.org/10.1103/PhysRevLett.120.230501).
3. Mao-Sheng Li and Kavan Modi, “Probabilistic and approximate masking of quantum information,” *Physical Review A* **102**, 022418 (2020). [Published article](https://doi.org/10.1103/PhysRevA.102.022418); [arXiv:1912.02419](https://arxiv.org/abs/1912.02419).
4. Xiaodi Li, Xinyang Shu, and Huangjun Zhu, “Random approximate quantum information masking,” arXiv:2507.19454v1 (2025). [Primary text](https://arxiv.org/html/2507.19454v1).
5. Xiangling Xu, Marc-Olivier Renou, and Igor Klep, “Quantitative Tsirelson's Theorems via Approximate Schur's Lemma and Probabilistic Stampfli's Theorems,” arXiv:2505.22309v2 (2025). [Primary text](https://arxiv.org/html/2505.22309v2).
6. Terry A. Loring, “Quantitative K-Theory Related to Spin Chern Numbers,” *SIGMA* **10**, 077 (2014). [DOI](https://doi.org/10.3842/SIGMA.2014.077); [primary PDF](https://sigma-journal.com/2014/077/sigma14-077.pdf).
7. Huangjun Zhu, “Hiding and masking quantum information in complex and real quantum mechanics,” *Physical Review Research* **3**, 033176 (2021). [DOI](https://doi.org/10.1103/PhysRevResearch.3.033176); [primary PDF](https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.3.033176).
8. Dennis Kretschmann, Dirk Schlingemann, and Reinhard F. Werner, “A continuity theorem for Stinespring's dilation,” *Journal of Functional Analysis* **255**(8), 1889–1904 (2008). [DOI](https://doi.org/10.1016/j.jfa.2008.07.023); [arXiv:0710.2495](https://arxiv.org/abs/0710.2495).
9. Robin Blume-Kohout, Hui Khoon Ng, David Poulin, and Lorenza Viola, “Information-preserving structures: A general framework for quantum zero-error information,” *Physical Review A* **82**, 062306 (2010). [DOI](https://doi.org/10.1103/PhysRevA.82.062306).
10. Victor V. Albert, “Asymptotics of quantum channels: conserved quantities, an adiabatic limit, and matrix product states,” *Quantum* **3**, 151 (2019). [DOI](https://doi.org/10.22331/q-2019-06-06-151); [primary PDF](https://quantum-journal.org/papers/q-2019-06-06-151/pdf/).
