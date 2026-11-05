# Reproduce the finite checks

The verifier checks explicit matrix and circuit identities supporting the written proofs. It uses Python 3.11 or later, NumPy 2.3.5, and the standard library. The separate [hosted-mathematics check](hosted/README.md) compares formulas displayed by GitHub with their pinned source and supplies screenshots for visual inspection.

From the repository root:

    python3 -m pip install -r verification/requirements.txt
    python3 verification/verify_masking.py

The second command prints a JSON report and exits with status zero when every check passes. To save a local report with a short terminal summary:

    python3 verification/verify_masking.py --output verification/local-report.json

The committed [reference report](expected/verification_report.json) was generated with Python 3.12.14 and NumPy 2.3.5. It records the verifier's SHA-256, runtime versions, all residuals, per-case tolerances, and instruction counts. Floating-point residuals may vary slightly across numerical libraries; the verifier tests the stated tolerances rather than requiring identical output bytes.

## What is checked

| Check family | Cases | Assertions |
|---|---|---|
| Weyl encoder | d = 3, 4, 9, 16, 25, 64 | Unitarity, periods, Weyl phase relation, isometry normalization, both complete label-intertwining identities, commutator norm, winding value and orthogonality of the three channel branches |
| Exact Schur masker | A deterministic rank-three Gram channel in dimension 5; all 25 matrix units | Complete positivity through a Gram/Kraus construction, trace preservation, basis-copy dephasing and both marginal invariance equalities |
| Qubit implementation | m = 1, 2, 3; every one of the 84 label branches | Positive-sign QFT and inverse built gate by gate, binary phase blocks, the required shift-after-phase ordering, and comparison with direct modular permutation/phase matrices |
| Gate accounting | The same three circuits | Counts enumerated from chronological instructions, controlled-phase/CNOT expansion, swap expansion and unchanged qubit footprint |

The matrix-unit check tests the full linear-map identities for the selected Schur example, not a sample of input states. The circuit comparison constructs the Fourier circuit independently of the direct dense Fourier formula. Every branch is compared with its direct action on the computational basis.

The isometry and intertwining checks use sums of small block Gram matrices. The largest dense matrix is 64 by 64; the program does not allocate the full label–data operator.

## Expected numerical result

The committed run passes all checks. Its largest reported residual is approximately 4.27e-14, from clock periodicity. The largest circuit-branch residual is below 1.93e-15.

| m | Hadamards | Controlled phases | SWAPs | Expanded CNOTs | Expanded single-qubit phases |
|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 2 | 18 | 18 |
| 2 | 12 | 26 | 4 | 64 | 78 |
| 3 | 18 | 60 | 6 | 138 | 180 |

Per-case tolerances scale as 128 times float64 machine epsilon times the matrix dimension and an explicit operation-count scale. The report gives the actual residuals alongside those thresholds. These are conservative floating-point checks, not interval-arithmetic certificates.

## Relation to the proofs

- [Exact classification](../science/exact_masking.md) proves necessity in every finite dimension. The Schur example checks its constructive sufficiency on one nontrivial channel.
- [Approximate gates](../science/approximate_gates.md) proves the diamond-norm bounds through isometries, averaging and Stinespring continuity.
- [Weyl separation](../science/weyl_separation.md) proves the local leakage bound, global distance and separation from every exactly maskable channel.
- [Resources and stability](../science/resources_and_stability.md) proves the general gate-count formulas and perturbation estimates.

No numerical optimization of a diamond norm or of distance to the Schur class is performed. The universal classification, the 1/48 lower bound, topological homotopy invariance and asymptotic conclusions rely on the analytical arguments and cited theorems. The verifier also does not implement a Solovay–Kitaev compiler or assess physical hardware.
