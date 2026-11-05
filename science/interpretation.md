# Interpretation and scope

## Local evidence does not determine an exact noise mechanism

Exact masking is structurally rigid. If a pure reversible encoder makes both shares invariant under a noise channel, the channel must preserve a complete orthogonal basis and act as a Schur multiplier in that basis. Populations can remain locally visible; the noise acts on coherences that the encoder places in correlations.

Approximate invariance has a different implication. The explicit Weyl family has local leakage tending to zero while staying a constant half-diamond distance from every channel with that exact structure. A small local signature is therefore insufficient evidence for a nearby exactly maskable noise mechanism when the dimension is allowed to grow.

The conclusion concerns a strong operational norm. It survives input entanglement with an arbitrary accessible reference, and the comparison includes every basis and every Schur Kraus rank. The construction uses two shares no larger than the input, with a pure coherent label register. These features make the separation a statement about the masking task itself.

## Why almost commutation is the right intermediate quantity

The [gate theorem](approximate_gates.md) connects local invariance to the commutators of the implementing unitaries. If a gate is almost invisible in one marginal, Stinespring continuity represents its action approximately on the opposite share. Choosing two gates on opposite shares gives commuting contractions. Pulling them back through the encoder bounds the original commutator.

Conversely, coherent averaging over finite powers makes a gate nearly invisible. One marginal sees only a small change at the boundary of the averaging window; in the other, small commutators allow the gate to move through the coherent products.

These arguments relate approximate masking to almost commutation. A separate matrix-approximation question asks whether the gates are close to a commuting family. The clock/shift pair shows that this further inference can fail. The [single-noise separation](weyl_separation.md) converts that established obstruction into distance from the entire exact noisy-channel class.

## What remains available globally

The encoder preserves its input isometrically. In the Weyl example, a joint receiver can reverse the encoder and recover the noisy channel output. The half-diamond distance from the identity remains $`2/3`$ even though either share alone has a small signature.

This is not recovery of the state before the noise. It is preservation of the information that remains in the noisy output. The local and global discrimination experiments have different access to the encoded systems.

An accessible noise environment or a classical record of the chosen kick would add information absent from the stated channel model. The marginal guarantees concern one retained share and an untouched input reference, with that environment inaccessible.

## Registers, gates and accuracy

On the sequence $`d=2^{2m}`$, the encoder takes $`2m`$ input qubits and adds $`2m`$ clean label qubits. It uses $`4m`$ qubits total and no additional work register. A known Fourier-adder construction realizes it with a quadratic number of controlled phases. Finite-alphabet compilation gives a polynomial-size circuit at the precision required for leakage of order $`2^{-m}`$. The complete counts and precision assumptions are in [Resources and stability](resources_and_stability.md).

These are logical circuits with specified pairwise gates. They do not include an architecture-specific routing or fault-tolerance estimate. The underlying noise is a known Weyl mixture on a growing register, rather than independently acting single-qubit noise.

For a perturbed channel at half-diamond distance $`\eta`$ from the target and one common encoder at half-diamond distance $`\kappa`$ from the ideal encoder, the proved local upper bound increases by at most $`\eta+4\kappa/3`$. The distance from the exact class decreases by at most $`\eta`$. Fixed nonzero implementation errors create a finite upper-bound floor; vanishing leakage requires an error budget that also tends to zero.

## Quantitative questions left open by the result

The general gate bounds have different exponents: the converse is quadratic in the commutator, while the averaging construction gives a square-root upper bound. The Weyl leakage exponent and encoder register sizes are sufficient bounds, not optima.

The stated separation needs no resolution of those optimizations. Its conclusion already follows from leakage tending to zero and a uniform positive distance from the exact class. It makes no assertion about universal input-state masking, privacy for all products in a generated group, unlimited circuit reuse, or a deployable cryptographic protocol.

## Position relative to prior work

Exact unitary channel masking, the underlying no-masking principle, stationary channel structure, Stinespring continuity, and the clock/shift obstruction are established ingredients. The [related-work account](../references/RELATED_WORK.md) identifies the theorem-level comparisons, including earlier approximate state masking and earlier uses of topology in masking.

The connected contribution is an all-dimensional noisy classification, a quantitative finite-gate criterion, and a reference-sensitive single-channel counterexample to uniform approximation by the exact class.
