# Thirty milestones for understanding quantum noise masking

This map follows the scientific argument from individual quantum systems to the distinction between exact structure and approximate local evidence. Its thirty understanding targets are defined by the project. The canonical statements and proofs remain in [the model](../science/model.md) and the linked science pages.

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, available through the [official author page][Watrous]. Section numbers below follow the [official contents][Contents] and chapter PDFs. The [Watrous bridge](WATROUS_BRIDGE.md) translates notation and assumptions and supplies a complete qubit example. Primary papers cited in the science pages provide research attribution and imported theorems; they are not additional educational anchors.

## Allocation and scientific route

- **Background/preliminaries: M01–M12, twelve milestones.** Registers, reduced states and channels lead to the operational norm, then to the Schur, stationary-state and Weyl structures needed to formulate the question. M12 integrates these objects into one precise experiment.
- **Narrative/innovation: M13–M30, eighteen milestones.** Four milestones establish the exact class; three connect approximate masking to almost commutation; seven build and interpret the single-channel separation; two account for implementation and perturbations; the last two locate the contribution and synthesize the complete result.

The larger narrative allocation reflects three distinct arguments that must be connected: the structural converse for arbitrary noisy channels, the quantitative gate criterion, and the obstruction to approximating one noisy channel by the whole exact class. The circuit and stability account then makes the growing-dimension example concrete. Each phase progresses from its component mechanisms to a global understanding target.

Each milestone records a central question, an understanding target, earlier dependencies and its story role, a conceptual connection, and source pointers. The phase is given by its enclosing heading. Dependencies identify conceptual prerequisites within this map; they do not replace the explanations in the sources.

## Phase I — Background/preliminaries

### M01 — Registers, states and coherent alternatives

**Central question:** What information does the state of a finite quantum register describe?

**Understanding target:** Distinguish a vector state, a density operator and a statistical mixture, and explain how the dimension counts available orthogonal states. Identify the input register and the two future output registers without interpreting a coherent sum of labels as discarded classical randomness.

**Dependencies and story role:** None. Establishes the individual objects from which the encoding experiment is built.

**Conceptual connection:** The distinction between coherence and mixing will determine whether the encoder has an uncounted random key.

**Source pointers:** Watrous [§§1.1.1–1.1.2][W1] and [§§2.1.1–2.1.2][W2]; [model: what is being hidden?](../science/model.md#what-is-being-hidden).

### M02 — Reduced states, correlations and references

**Central question:** How can two joint states differ while their individual shares look the same?

**Understanding target:** Explain the partial trace and the information retained in correlations. Distinguish an encoded share from an untouched reference initially entangled with the input, and understand why a claim about one share may change when that reference is available.

**Dependencies and story role:** M01. Moves from an individual register to the different observers of a compound system.

**Conceptual connection:** Local indistinguishability and global distinguishability are compatible because they describe different accessible systems.

**Source pointers:** Watrous [§2.1.3][W2]; [model: reference-sensitive local leakage](../science/model.md#reference-sensitive-local-leakage); [qubit bridge](WATROUS_BRIDGE.md).

### M03 — Channels and preserved observations

**Central question:** How is a physical change represented independently of the chosen input state?

**Understanding target:** Explain complete positivity, trace preservation, channel composition and the identity channel. Relate the Schrödinger description of changing states to the adjoint description of changing observables, including what it means for an observable to be fixed.

**Dependencies and story role:** M01–M02. Turns state comparisons into a question about a transformation acting on every input.

**Conceptual connection:** Marginal invariance will become a statement about which input observables survive the noise.

**Source pointers:** Watrous [§1.1.2][W1] and [§§2.2.1–2.2.2][W2]; [model](../science/model.md); [exact masking: Lemma 2](../science/exact_masking.md#lemma-2-the-faithful-fixed-observable-algebra).

### M04 — Pure encoders and two retained outputs

**Central question:** What does the pure bipartite restriction require of the encoder?

**Understanding target:** Interpret $`V:H\to A\otimes B`$ with $`V^\dagger V=I_H`$ as reversible on its image. Obtain the two complementary marginal channels by tracing opposite outputs. Explain why the encoder retains all its outputs and why a discarded third system, a mixed private key or postselection changes the task.

**Dependencies and story role:** M02–M03. Fixes the physical model before introducing approximation.

**Conceptual connection:** Global reversibility permits local hiding through correlations without recovering information already lost to the noise environment.

**Source pointers:** Watrous [§§2.1.3 and 2.2.2][W2]; [model: what is being hidden?](../science/model.md#what-is-being-hidden).

### M05 — One channel, several mathematical representations

**Central question:** What is the same, and what is different, in Kraus, Choi and Stinespring descriptions?

**Understanding target:** Translate between a Kraus sum, a channel's Choi operator and an isometric dilation. Distinguish representation freedom from physical access to an environment or a Kraus label. Recognize that a normalized maximally entangled probe produces the Choi operator divided by the input dimension.

**Dependencies and story role:** M03–M04. Supplies the representation changes needed by both the exact converse and the separation proof.

**Conceptual connection:** A proof must compare channels independently of which Kraus representation happens to be written down.

**Source pointers:** Watrous [§2.2.2][W2]; [model](../science/model.md); [Weyl separation: arbitrary exact comparators](../science/weyl_separation.md#5-distance-from-every-exactly-maskable-channel).

### M06 — Discrimination with an accessible reference

**Central question:** How is the best observable evidence for noise quantified?

**Understanding target:** Connect trace distance with binary state discrimination and the diamond norm with channel discrimination. Keep the project's factor of one half explicit: $`D_\diamond(\mathcal E,\mathcal F)=\tfrac12\lVert\mathcal E-\mathcal F\rVert_\diamond`$. Understand why an arbitrary reference is included and why one of dimension equal to the input suffices.

**Dependencies and story role:** M02–M05. Gives local leakage an operational meaning that survives input entanglement.

**Conceptual connection:** A small error bound limits every allowed local discrimination strategy, rather than only selected probe states.

**Source pointers:** Watrous [§3.1.1 and §§3.3.1–3.3.3][W3]; [model: reference-sensitive local leakage](../science/model.md#reference-sensitive-local-leakage).

### M07 — Populations, coherences and Schur channels

**Central question:** What can a channel change while preserving every population in a chosen basis?

**Understanding target:** Separate diagonal populations from off-diagonal coherences. Explain how a positive semidefinite matrix with unit diagonal specifies a Schur channel and how diagonal Kraus operators express the same structure. Distinguish this class from mixtures of diagonal unitaries in arbitrary dimension.

**Dependencies and story role:** M03 and M05. Identifies the structural class that will appear in the exact theorem.

**Conceptual connection:** Preserving population information can coexist with hiding changes to coherence.

**Source pointers:** Watrous [§§4.1.1 and 4.1.3][W4]; [model: the exact class](../science/model.md#the-exact-class); [qubit bridge](WATROUS_BRIDGE.md).

### M08 — Stationary states and fixed-observable structure

**Central question:** How do stationary states and conserved observables reveal the structure of a channel?

**Understanding target:** Distinguish a fixed state from a fixed observable, faithful support from a transient complement, and raw iteration from a Cesàro average. Understand the role of commutants and invariant algebra blocks. Keep the unital-channel hypotheses of the textbook's fixed-point result separate from the general channel needed here.

**Dependencies and story role:** M03, M05 and M07. Introduces the structural tools needed to prove necessity beyond unital examples.

**Conceptual connection:** A proposed exact masker constrains the channel's stationary structure, including sectors invisible to a faithful-state argument on only part of the input.

**Source pointers:** Watrous [§4.2.2][W4]; [exact masking: Lemmas 2–3](../science/exact_masking.md); [fixed-space attribution](../references/RELATED_WORK.md#continuity-and-fixed-space-structure).

### M09 — From implementation distance to channel distance

**Central question:** When do close isometries or channels permit a controlled comparison of their dilations?

**Understanding target:** Distinguish operator norm from diamond norm and use their different roles in perturbation estimates. Understand the easy direction from close isometries to close channels, and the square-root continuity input that aligns channel dilations in a common enlarged environment. Separate that proof environment from an additional physical output.

**Dependencies and story role:** M04–M06. Connects operational errors with the operator estimates used later.

**Conceptual connection:** Continuity allows local statistical invariance to constrain the way a gate can act on the other share.

**Source pointers:** Watrous [§1.1.3][W1] and [§§3.3.2–3.3.3][W3]; [approximate gates: Lemmas 4–5](../science/approximate_gates.md#3-two-continuity-lemmas-with-the-norm-conventions-fixed), including the cited Kretschmann–Schlingemann–Werner theorem.

### M10 — Clock, shift and two meanings of commutation

**Central question:** How can conjugation channels commute when their implementing unitary matrices do not?

**Understanding target:** Interpret the discrete shift $`X_d`$ and clock $`Z_d`$, their relation $`Z_dX_d=e^{2\pi i/d}X_dZ_d`$, and the associated small operator-norm commutator as dimension grows. Explain why the phase cancels in conjugation and why superoperator commutation is therefore a different condition.

**Dependencies and story role:** M01, M03 and M09. Supplies the concrete operator geometry behind the counterexample.

**Conceptual connection:** The quantitative masking criterion will concern the implementing matrices, even though the physical alternatives are channels.

**Source pointers:** Watrous [§4.1.2][W4]; [Weyl separation: clock, shift and noise](../science/weyl_separation.md#1-clock-shift-and-noise); [approximate gates](../science/approximate_gates.md).

### M11 — Exact classification and uniform stability

**Central question:** What extra claim is made when an exact characterization is extended to small errors?

**Understanding target:** Distinguish existence of an attained exact encoder from an infimum over approximate encoders. Formulate a stability implication whose bound is independent of input dimension, and distinguish it from a statement at one fixed dimension. Identify input dimension, share dimensions and coherent ancillas as separate resources.

**Dependencies and story role:** M04, M06–M10. Moves from individual structures to the quantifiers of the research question.

**Conceptual connection:** An exact algebraic description need not provide a uniform inference from finite experimental error.

**Source pointers:** Watrous [§1.2.1][W1] and [§3.3.3][W3] for limits and channel distance; [model: the exact class](../science/model.md#the-exact-class); [Weyl separation: uniformity question](../science/weyl_separation.md#6-what-fails-uniformly-with-dimension).

### M12 — The complete operational question

**Central question:** What precisely would it mean to hide a known noise channel from either share?

**Understanding target:** Assemble the experiment: noise versus identity on the same finite input, one common pure encoder, either share plus an untouched reference, and an inaccessible noise environment. Interpret

```math
\varepsilon_V(\mathcal N)
=\max_{S\in\{A,B\}}
D_\diamond(M_S\circ\mathcal N,M_S).
```

Explain why the marginals may still reveal input information and why the global channel output remains recoverable from both shares.

**Dependencies and story role:** M01–M11. Synthesizes the background into the model and the exact-versus-approximate question.

**Conceptual connection:** The object being hidden is the effect of a specified transformation, while access to the input's information is governed by a different question.

**Source pointers:** Watrous [§2.2.2][W2] and [§§3.3.1–3.3.3][W3]; [canonical model](../science/model.md); [qubit bridge](WATROUS_BRIDGE.md).

## Phase II — Narrative/innovation

### M13 — The basis-copying mechanism

**Central question:** Why does copying orthogonal basis labels hide every Schur channel in that basis?

**Understanding target:** Explain the isometry $`V\lvert i\rangle=\lvert i\rangle_A\lvert i\rangle_B`$ and calculate why each marginal retains populations while discarding coherence terms. Show that Schur noise leaves both marginals unchanged for every input, including inputs entangled with a reference. Recognize basis copying as an established ingredient.

**Dependencies and story role:** M04, M06–M07 and M12. Starts the narrative with the constructive direction of exact masking.

**Conceptual connection:** Coherence can remain in joint correlations even when its noise-induced change is locally invisible.

**Source pointers:** Watrous [§4.1.3, particularly the isometry in Eq. (4.117)][W4]; [exact masking: Theorem 1 and its proof](../science/exact_masking.md); [qubit bridge](WATROUS_BRIDGE.md).

### M14 — Why a transient sector cannot survive exact masking

**Central question:** Could a channel evade the Schur description by moving states into a smaller stationary support?

**Understanding target:** Follow the Cesàro projection onto fixed states and its annihilation of coherences between stationary support and its complement. Explain how exact invariance of both marginals would make a transient state's marginal both equal to and supported orthogonally to its stationary image, giving a contradiction. Do not assume convergence of the unaveraged channel powers.

**Dependencies and story role:** M02, M08, M12–M13. Removes the obstruction to a faithful stationary-state argument on the whole input.

**Conceptual connection:** Pure bipartite encoding converts loss of support coherences into an incompatibility between the two marginal constraints.

**Source pointers:** Watrous [§§2.1.3 and 2.2.2][W2] for the underlying objects; [exact masking: Lemmas 1–3 and proof of Theorem 1](../science/exact_masking.md), which supplies the general-channel argument.

### M15 — Why a nontrivial noisy factor is impossible

**Central question:** After transient sectors are excluded, what further structure does exact masking forbid?

**Understanding target:** Explain the faithful fixed-observable commutant and its decomposition into algebra blocks and multiplicity factors. Understand why a nontrivial noisy factor, with the other factor fixed, would require universal pure bipartite masking of arbitrary states on that factor. Identify the resulting no-masking contradiction.

**Dependencies and story role:** M02, M07–M08 and M14. Completes the structural necessity argument by removing residual noisy factors.

**Conceptual connection:** A theorem about hiding prescribed channel effects uses universal state no-masking only inside a hypothetical factor of the channel.

**Source pointers:** Watrous [§4.2.2][W4] for the unital fixed-point foundation; [exact masking: Lemma 2 and proof of Theorem 1](../science/exact_masking.md); [no-masking and fixed-space attribution](../references/RELATED_WORK.md).

### M16 — The exact class and a common basis for families

**Central question:** What complete characterization follows, and when can several channels share one masker?

**Understanding target:** Connect exact maskability, a complete orthogonal pure fixed-state basis, diagonal Kraus operators and a Schur correlation matrix. Explain why a positive convex mixture and extremality of pure states force one common basis for a finite simultaneously maskable family against identity. No unitality assumption is imposed on the initial channel.

**Dependencies and story role:** M07 and M13–M15. Integrates the exact proof into a classification usable in the later comparison.

**Conceptual connection:** The single-channel separation must exclude this entire structural class, rather than a chosen basis or a restricted noise model.

**Source pointers:** Watrous [§4.1.3][W4]; [exact masking: Theorem 1 and Corollary 1](../science/exact_masking.md); [exact-channel prior work](../references/RELATED_WORK.md#exact-channel-masking).

### M17 — Local invariance forces almost commuting gates

**Central question:** What does small leakage imply about two logical gates?

**Understanding target:** Use common-environment Stinespring continuity to obtain approximate representatives as contractions on opposite original shares. Explain why those contractions commute and why a four-term estimate gives $`\lVert[U_i,U_j]\rVert_{\mathrm{op}}\le4\sqrt{2\varepsilon}`$. Understand why a unitary alignment on an arbitrarily prescribed small environment is unnecessary.

**Dependencies and story role:** M04, M09–M10, M12 and M16. Begins the approximate theory with a necessary condition valid for every pure encoder.

**Conceptual connection:** Operational invariance of complementary channels constrains the algebra of transformations on the original input.

**Source pointers:** Watrous [§2.2.2][W2] and [§§3.3.2–3.3.3][W3]; [approximate gates: Lemma 5 and lower-bound proof](../science/approximate_gates.md), with the cited KSW continuity input.

### M18 — Coherent averaging over a finite cube

**Central question:** How can almost commuting gates produce a pure encoder that hides their action?

**Understanding target:** Construct an isometry by coherently flagging the ordered products $`U_1^{a_1}\cdots U_k^{a_k}`$ for $`0\le a_j\le L-1`$. Explain normalization, why the label share stays quantum and retained, and why the two share dimensions are $`L^k`$ and $`d`$.

**Dependencies and story role:** M04, M09–M10 and M12. Supplies the constructive counterpart to M17 with all encoding resources visible.

**Conceptual connection:** Finite averaging resembles randomization in one marginal, while a coherent dilation keeps the complete encoding reversible.

**Source pointers:** Watrous [§2.2.2][W2] and [§4.1.1][W4]; [approximate gates: upper-bound construction](../science/approximate_gates.md#proof-of-the-upper-bound).

### M19 — The quantitative finite-gate criterion

**Central question:** How do the two error mechanisms combine into an operational equivalence?

**Understanding target:** Separate the label-share commutation error from the system-share boundary error of the finite averaging window. For $`\delta=\max_{i,j}\lVert[U_i,U_j]\rVert_{\mathrm{op}}`$, understand the bounds

```math
\frac{\delta^2}{32}
\le\varepsilon_*
\le\inf_{L\in\mathbb N,\ L\ge1}
\left[\frac1L+(k-1)(L-1)\delta\right].
```

Explain the fixed-family-size qualification, the optimization giving a square-root upper bound, and the unmatched exponents.

**Dependencies and story role:** M09–M11 and M17–M18. Synthesizes necessity and construction into the general approximate theorem.

**Conceptual connection:** Approximate gate masking is controlled by almost commutation, which still leaves open the separate question of proximity to exactly commuting gates.

**Source pointers:** Watrous [§§3.3.2–3.3.3][W3] for the norm framework; [approximate gates: Theorem 2 and proofs](../science/approximate_gates.md#theorem-2-quantitative-equivalence).

### M20 — A concrete family of noisy Weyl channels

**Central question:** How can the gate mechanism be converted into one specified noisy channel?

**Understanding target:** Interpret, for $`d\ge3`$,

```math
\mathcal N_d=\frac13
\left(\mathrm{id}+\operatorname{Ad}_{X_d}+\operatorname{Ad}_{Z_d}\right),
```

and specialize the coherent construction to labels $`(a,b)`$ and products $`X_d^aZ_d^b`$. Distinguish the channel's inaccessible random kick from the encoder's retained coherent labels.

**Dependencies and story role:** M05, M10, M12 and M18–M19. Starts the explicit single-channel construction.

**Conceptual connection:** Convexity transfers bounds on specified gate alternatives to a physical noise mixture without granting access to its branch label.

**Source pointers:** Watrous [§§4.1.1–4.1.2][W4]; [Weyl separation: Sections 1–2](../science/weyl_separation.md).

### M21 — Why the system share sees only an averaging boundary

**Central question:** What changes in the system marginal when a clock or shift acts on the input?

**Understanding target:** Express the system marginal as a uniform mixture over a finite Weyl box. Understand that translating one coordinate preserves the interior terms and changes only a boundary fraction, yielding half-diamond leakage at most $`1/L`$. Explain why the estimate already includes any untouched reference.

**Dependencies and story role:** M06, M18–M20. Isolates the first of the two local hiding mechanisms.

**Conceptual connection:** A total-variation estimate on averaging weights becomes a channel-discrimination bound through convexity.

**Source pointers:** Watrous [§§1.2.1–1.2.2][W1] and [§3.3.2][W3]; [Weyl separation: system share](../science/weyl_separation.md#the-system-share-only-the-edge-of-the-averaging-window-changes).

### M22 — Why the label share sees only a short spectral arc

**Central question:** Why does retaining coherent labels not reveal the hidden kick?

**Understanding target:** Use the exact covariance identities to move the gate to the traced system share and a diagonal phase operator on the label share. Explain how a spectral arc of width $`2\pi(L-1)/d\le\pi`$ bounds the distinguishability, including a reference, by $`\sin[\pi(L-1)/d]`$.

**Dependencies and story role:** M02, M06, M09–M10 and M20. Establishes the second local guarantee without discarding the encoder's coherence.

**Conceptual connection:** Spectral geometry controls an operational error even when the local state is correlated with another system.

**Source pointers:** Watrous [§§1.1.3 and 1.2.1][W1], [§3.1.1][W3] and [§4.1.2][W4]; [Weyl separation: label share](../science/weyl_separation.md#the-label-share-a-short-spectral-arc).

### M23 — The obstruction to nearby commuting matrices

**Central question:** Why can a very small commutator coexist with a fixed distance from every commuting pair?

**Understanding target:** Understand the winding or Bott index of a unitary commutator, the domain on which it is well defined, and why the Weyl pair has index one while commuting pairs have index zero. Identify Loring's quantitative separation as an imported theorem, rather than a consequence of the elementary commutator estimate.

**Dependencies and story role:** M09–M11 and M20. Supplies the obstruction needed to prevent rounding the approximate construction to an exact mechanism.

**Conceptual connection:** A discrete invariant can obstruct a uniform approximation even while a local algebraic defect tends to zero.

**Source pointers:** Watrous [§§1.1.3 and 1.2.1][W1] supplies spectral and continuity foundations; [Weyl separation: imported matrix obstruction](../science/weyl_separation.md#4-imported-matrix-obstruction) gives the needed definition and cites Loring, Theorem 2.3. The topology is supplied there, not attributed to the textbook.

### M24 — From arbitrary Schur channels to commuting approximants

**Central question:** Why does the matrix obstruction exclude every exactly maskable noisy comparator?

**Understanding target:** Start with an arbitrary-basis Schur dilation, align it with the canonical three-flag dilation of $`\mathcal N_d`$ in a common environment, and project onto the Weyl flags. Explain why this produces two diagonal approximants in the same basis, why polar normalization yields commuting unitaries, and how the obstruction gives distance at least $`1/48`$.

**Dependencies and story role:** M05, M09, M16, M20 and M23. Converts the matrix theorem into a separation from the full exact channel class.

**Conceptual connection:** Representation freedom and arbitrary Kraus rank do not evade a comparison that preserves common diagonal structure through dilation continuity.

**Source pointers:** Watrous [§2.2.2][W2] and [§4.1.3][W4]; [Weyl separation: distance proof](../science/weyl_separation.md#5-distance-from-every-exactly-maskable-channel), including its KSW and Loring inputs.

### M25 — The noise remains visible globally

**Central question:** What can an observer holding both shares detect that either share alone cannot?

**Understanding target:** Use a maximally entangled probe and the orthogonal Choi vectors of $`I,X_d,Z_d`$ to obtain $`D_\diamond(\mathcal N_d,\mathrm{id})=2/3`$. Distinguish perfect discrimination of the three pure unitary branches from the mixture-versus-identity success probability $`5/6`$. Explain why reversing the encoder recovers the noisy output, not the state before noise.

**Dependencies and story role:** M02, M04–M06 and M20–M22. Connects local hiding to an explicit surviving joint signal.

**Conceptual connection:** The separation concerns where evidence can be found, while isometric encoding preserves the evidence available globally.

**Source pointers:** Watrous [§2.2.2][W2] and [§§3.1.1 and 3.3.1][W3]; [Weyl separation: global visibility](../science/weyl_separation.md#3-the-noise-remains-globally-visible); [joint decoder and test](../science/resources_and_stability.md#34-decoder-and-reference-assisted-global-test).

### M26 — The single-channel theorem and failure of a uniform modulus

**Central question:** What follows when local hiding, global visibility and the exact-class separation are combined?

**Understanding target:** Choose $`L=\lfloor\sqrt d\rfloor`$ and connect the three conclusions: local leakage is $`O(d^{-1/2})`$, global distance from identity is $`2/3`$, and distance from every exactly maskable channel is at least $`1/48`$. Explain why both shares have dimension at most $`d`$ and why no dimension-independent function tending to zero can turn this leakage into proximity to the exact class.

**Dependencies and story role:** M11, M16 and M20–M25. Integrates the counterexample and its quantifiers.

**Conceptual connection:** Approximate local evidence does not inherit the structural rigidity of the exact theorem uniformly with growing dimension.

**Source pointers:** Watrous [§3.3.3][W3] for channel distance; [Weyl separation: Sections 2–6](../science/weyl_separation.md); [interpretation](../science/interpretation.md).

### M27 — A circuit with all registers charged

**Central question:** What finite quantum circuit implements the encoder, and what resources does it require?

**Understanding target:** On $`d=2^{2m}`$ and $`L=2^m`$, identify the $`2m`$ input qubits and $`2m`$ clean label qubits, with $`2m`$ qubits in each final share. Explain the controlled phase and Fourier-addition construction, its $`6m`$ Hadamards, $`7m^2-m`$ controlled phases and $`2m`$ SWAPs, and the absence of an extra work register. Keep a discrimination reference separate from the encoder budget.

**Dependencies and story role:** M04, M10, M18, M25–M26. Converts the dimensional construction into an explicit logical circuit.

**Conceptual connection:** A coherent mathematical flag is a retained physical register whose preparation, gates and size must all be counted.

**Source pointers:** Watrous [§§2.1.1 and 2.2.2][W2] for registers and isometries; [resources: Sections 2–3](../science/resources_and_stability.md), including attribution of the Fourier adder. These counts assume the stated pairwise logical gates, without architecture-specific routing or fault tolerance.

### M28 — Finite precision and perturbation guarantees

**Central question:** Which conclusions survive finite gate synthesis and a perturbed noise channel?

**Understanding target:** Distinguish channel error $`\eta`$ from a common encoder error $`\kappa`$ and interpret the sufficient upper bound $`\varepsilon_m+\eta+4\kappa/3`$ together with separation at least $`\max\{0,1/48-\eta\}`$. Explain why vanishing budgets suffice for vanishing guaranteed leakage and budgets of order $`2^{-m}`$ retain that sufficient rate under polynomial-size compilation. Fixed budgets leave nonvanishing terms in this bound; they do not prove a necessary physical leakage floor.

**Dependencies and story role:** M09, M26–M27. Connects the asymptotic theorem to explicit finite implementation guarantees.

**Conceptual connection:** Stability is a controlled implication from specified errors, not an assertion that every implementation must saturate the bound.

**Source pointers:** Watrous [§§1.1.3 and 1.2.1][W1] and [§3.3.2][W3]; [resources: Sections 4–6](../science/resources_and_stability.md), including the cited finite-alphabet synthesis input.

### M29 — Attribution, evidence and remaining quantitative limits

**Central question:** Which parts are established ingredients, which conclusions are developed here, and what remains unproved?

**Understanding target:** Separate the inherited channel-masking task, exact unitary criterion, no-masking principle, fixed-space theory, Stinespring continuity and matrix obstruction from their use in this project. Distinguish general proofs from finite numerical checks. Identify the unmatched gate exponents and nonoptimal resource bounds without treating their optimization as necessary for the separation.

**Dependencies and story role:** M16, M19 and M23–M28. Places the connected result within its evidence and prior-work boundaries.

**Conceptual connection:** Scientific significance depends on what the combination establishes operationally, not on relabeling established ingredients as new.

**Source pointers:** [Related work and contribution boundaries](../references/RELATED_WORK.md); [verification scope](../verification/README.md); [interpretation: quantitative questions](../science/interpretation.md#quantitative-questions-left-open-by-the-result). Watrous remains the educational foundation; the primary papers in these pages supply attribution and imported theorems.

### M30 — The scientific story as a whole

**Central question:** What can, and cannot, be inferred about noise from its weak local signature?

**Understanding target:** Explain the complete chain: exact pure bipartite masking forces Schur structure; approximate finite-gate masking corresponds quantitatively to almost commutation; Weyl topology prevents a nearby exact noise mechanism; coherent encoding hides one specified channel locally while preserving a joint signal. State the reference-sensitive, single-use, known-channel and growing-dimension assumptions, the charged implementation resources, and why universal state hiding, arbitrary circuit privacy and indefinite reuse are outside the result.

**Dependencies and story role:** M12, M16, M19 and M26–M29. Synthesizes the narrative from its local mechanisms into the global operational conclusion.

**Conceptual connection:** A rigid exact classification and a controlled approximation theorem can coexist with a failure of dimension-independent structural inference.

**Source pointers:** [Model and result statements](../science/model.md); [interpretation and scope](../science/interpretation.md); [resources and stability](../science/resources_and_stability.md); [Watrous bridge](WATROUS_BRIDGE.md).

[Watrous]: https://cs.uwaterloo.ca/~watrous/TQI/
[Contents]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf
[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W4]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf
