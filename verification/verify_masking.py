#!/usr/bin/env python3
"""Reproducible finite algebra and circuit checks for Quantum-Noise-Masking.

Only NumPy and the Python standard library are required. Validated with
NumPy 2.3.5. Run:

    python verify_masking.py
    python verify_masking.py --output verification_report.json

These checks do not numerically certify diamond norms, distance from every
Schur channel, a universal classification, or the topological homotopy theorem.
Those are analytical results. No SDP or gate-synthesis compiler is used.

Qubit q has weight 2**q (little-endian bits). Gate lists are chronological;
applying a list to an identity matrix constructs its unitary by left
multiplication. All calculations use float64/complex128.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import platform
from typing import Iterable

import numpy as np


EPS = float(np.finfo(np.float64).eps)
WEYL_DIMENSIONS = (3, 4, 9, 16, 25, 64)
CIRCUIT_M_VALUES = (1, 2, 3)


def numerical_tolerance(dimension: int, operation_scale: int) -> float:
    """Conservative checking tolerance, not an interval-arithmetic certificate.

For the unitary blocks, ordinary dense product error scales with machine
epsilon times matrix dimension, and repeated products/sums add an operation-
count factor. The Schur example has only five normalized feature rows. The
factor 128 allows ample room for that bounded Gram construction, complex
arithmetic, trigonometric evaluation, and SVD/eigensolver roundoff. Actual
residuals are reported so the tolerance cannot conceal their size.
"""
    return 128.0 * EPS * max(1, dimension) * max(1, operation_scale)


def require(condition: bool, message: str) -> None:
    """Keep assertions active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def require_small(name: str, residual: float, tolerance: float) -> float:
    residual = float(residual)
    require(
        math.isfinite(residual) and residual <= tolerance,
        f"{name}: residual {residual:.6e} exceeds tolerance {tolerance:.6e}",
    )
    return residual


def operator_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def stacked_norm_from_gram(gram: np.ndarray) -> float:
    """Norm of vertically stacked blocks from the sum of block-adjoint blocks."""
    hermitian = (gram + gram.conj().T) / 2.0
    largest = float(np.linalg.eigvalsh(hermitian)[-1])
    return math.sqrt(max(0.0, largest))


def weyl_operators(d: int) -> tuple[np.ndarray, np.ndarray]:
    identity = np.eye(d, dtype=np.complex128)
    x = np.roll(identity, 1, axis=0)
    z = np.diag(np.exp(1j * math.tau * np.arange(d) / d))
    return x, z


def check_weyl_case(d: int) -> dict:
    """Check V through its d-by-d blocks, never a giant Kronecker matrix."""
    length = math.isqrt(d)
    x, z = weyl_operators(d)
    identity = np.eye(d, dtype=np.complex128)
    omega = np.exp(1j * math.tau / d)
    scale = d + length * length + 4 * length + 8
    tolerance = numerical_tolerance(d, scale)
    residuals: dict[str, float] = {}

    def record(name: str, value: float) -> None:
        residuals[name] = require_small(f"d={d}: {name}", value, tolerance)

    record("X_unitarity", operator_norm(x.conj().T @ x - identity))
    record("Z_unitarity", operator_norm(z.conj().T @ z - identity))
    record("ZX_equals_omega_XZ", operator_norm(z @ x - omega * (x @ z)))
    record("X_period_d", operator_norm(np.linalg.matrix_power(x, d) - identity))
    record("Z_period_d", operator_norm(np.linalg.matrix_power(z, d) - identity))

    x_powers = [np.linalg.matrix_power(x, a) for a in range(length)]
    z_powers = [np.linalg.matrix_power(z, b) for b in range(length)]
    isometry_gram = np.zeros((d, d), dtype=np.complex128)
    intertwining_x_gram = np.zeros_like(isometry_gram)
    intertwining_z_gram = np.zeros_like(isometry_gram)

    for a in range(length):
        for b in range(length):
            block = (x_powers[a] @ z_powers[b]) / length
            isometry_gram += block.conj().T @ block
            # VX = (D_b tensor X)V, with D_b|a,b> = omega**b |a,b>.
            error_x = block @ x - (omega**b) * (x @ block)
            # VZ = (D_{-a} tensor Z)V.
            error_z = block @ z - (omega ** (-a)) * (z @ block)
            intertwining_x_gram += error_x.conj().T @ error_x
            intertwining_z_gram += error_z.conj().T @ error_z

    record("V_adjoint_V_equals_identity", operator_norm(isometry_gram - identity))
    record("VX_label_intertwining", stacked_norm_from_gram(intertwining_x_gram))
    record("VZ_label_intertwining", stacked_norm_from_gram(intertwining_z_gram))

    group_commutator = z @ x @ z.conj().T @ x.conj().T
    record(
        "group_commutator_equals_omega_identity",
        operator_norm(group_commutator - omega * identity),
    )
    commutator_norm = operator_norm(x @ z - z @ x)
    expected_commutator_norm = 2.0 * math.sin(math.pi / d)
    record(
        "commutator_norm_formula",
        abs(commutator_norm - expected_commutator_norm),
    )
    require(commutator_norm < 2.0, f"d={d}: principal-log winding undefined")

    eigenvalues = np.linalg.eigvals(group_commutator)
    principal_angles = np.angle(eigenvalues)
    winding = float(np.sum(principal_angles) / math.tau)
    branch_cut_gap = math.pi - float(np.max(np.abs(principal_angles)))
    record("winding_index_equals_one", abs(winding - 1.0))
    require(branch_cut_gap > tolerance, f"d={d}: eigenvalue near log branch cut")

    operators = (identity, x, z)
    hs_gram = np.asarray(
        [[np.vdot(left, right) / d for right in operators] for left in operators],
        dtype=np.complex128,
    )
    record(
        "normalized_Hilbert_Schmidt_Gram_equals_identity",
        operator_norm(hs_gram - np.eye(3, dtype=np.complex128)),
    )

    return {
        "d": d,
        "L": length,
        "share_A_dimension": length * length,
        "share_B_dimension": d,
        "encoder_blocks_checked": length * length,
        "operation_scale_for_tolerance": scale,
        "tolerance": tolerance,
        "residual_norm": "operator norm, except explicitly scalar residuals",
        "residuals": residuals,
        "largest_residual": max(residuals.values()),
        "commutator_norm": commutator_norm,
        "winding": {
            "convention": "sum principal eigenphases of Z X Z* X* divided by 2*pi",
            "value": winding,
            "nearest_integer": int(round(winding)),
            "branch_cut_gap_radians": branch_cut_gap,
        },
        "method": (
            "V*V and both full intertwining norms use d-by-d block Gram sums; "
            "neither V nor label-tensor-data operators are materialized."
        ),
    }


def partial_traces(matrix: np.ndarray, d: int) -> tuple[np.ndarray, np.ndarray]:
    tensor = matrix.reshape(d, d, d, d)
    return (
        np.trace(tensor, axis1=1, axis2=3),
        np.trace(tensor, axis1=0, axis2=2),
    )


def check_schur_masking() -> dict:
    """A deterministic rank-three Gram channel; check every matrix unit."""
    features = np.asarray(
        [
            [1, 2 + 1j, -1 + 2j],
            [2 - 1j, -1, 1 + 1j],
            [1j, 1 - 2j, 2],
            [3 - 1j, 2j, -1 + 3j],
            [1 - 3j, -2 + 1j, 2 + 2j],
        ],
        dtype=np.complex128,
    )
    features /= np.linalg.norm(features, axis=1, keepdims=True)
    d, rank = features.shape
    correlation = features @ features.conj().T
    kraus = [np.diag(features[:, k]) for k in range(rank)]
    identity = np.eye(d, dtype=np.complex128)
    tolerance = numerical_tolerance(d, 4 * rank + 6)
    residuals: dict[str, float] = {}

    copy_isometry = np.zeros((d * d, d), dtype=np.complex128)
    for i in range(d):
        copy_isometry[i * d + i, i] = 1.0

    def record(name: str, value: float) -> None:
        residuals[name] = require_small(f"Schur d={d}: {name}", value, tolerance)

    record("correlation_Hermitian", operator_norm(correlation - correlation.conj().T))
    record("correlation_diagonal_one", float(np.max(np.abs(np.diag(correlation) - 1))))
    smallest_eigenvalue = float(np.linalg.eigvalsh(correlation)[0])
    record("correlation_PSD_violation", max(0.0, -smallest_eigenvalue))
    kraus_normalization = sum((k.conj().T @ k for k in kraus), np.zeros_like(identity))
    record("Kraus_trace_preservation", operator_norm(kraus_normalization - identity))
    record(
        "copy_isometry_normalization",
        operator_norm(copy_isometry.conj().T @ copy_isometry - identity),
    )

    maxima = {
        "Kraus_equals_Schur_on_matrix_units": 0.0,
        "copy_marginal_A_equals_dephasing": 0.0,
        "copy_marginal_B_equals_dephasing": 0.0,
        "masking_A_on_all_matrix_units": 0.0,
        "masking_B_on_all_matrix_units": 0.0,
    }
    for i in range(d):
        for j in range(d):
            unit = np.zeros((d, d), dtype=np.complex128)
            unit[i, j] = 1.0
            noisy = sum((k @ unit @ k.conj().T for k in kraus), np.zeros_like(unit))
            expected_noisy = correlation[i, j] * unit
            maxima["Kraus_equals_Schur_on_matrix_units"] = max(
                maxima["Kraus_equals_Schur_on_matrix_units"],
                operator_norm(noisy - expected_noisy),
            )
            clean_encoded = copy_isometry @ unit @ copy_isometry.conj().T
            noisy_encoded = copy_isometry @ noisy @ copy_isometry.conj().T
            clean_a, clean_b = partial_traces(clean_encoded, d)
            noisy_a, noisy_b = partial_traces(noisy_encoded, d)
            expected_marginal = unit if i == j else np.zeros_like(unit)
            for side, clean, noisy_marginal in (
                ("A", clean_a, noisy_a), ("B", clean_b, noisy_b)
            ):
                key_dephasing = f"copy_marginal_{side}_equals_dephasing"
                key_masking = f"masking_{side}_on_all_matrix_units"
                maxima[key_dephasing] = max(
                    maxima[key_dephasing], operator_norm(clean - expected_marginal)
                )
                maxima[key_masking] = max(
                    maxima[key_masking], operator_norm(noisy_marginal - clean)
                )
    for name, value in maxima.items():
        record(name, value)

    numerical_rank = int(np.linalg.matrix_rank(correlation, tol=tolerance))
    require(numerical_rank == rank, "The deterministic Schur example lost its intended rank")
    require(
        operator_norm(correlation - np.eye(d)) > 0.1
        and operator_norm(correlation - np.ones((d, d))) > 0.1,
        "The Schur example should be neither complete dephasing nor identity",
    )
    return {
        "d": d,
        "Gram_feature_dimension": rank,
        "correlation_numerical_rank": numerical_rank,
        "correlation_smallest_eigenvalue": smallest_eigenvalue,
        "matrix_units_checked": d * d,
        "tolerance": tolerance,
        "residual_norm": "operator norm, except diagonal/PSD scalar residuals",
        "residuals": residuals,
        "largest_residual": max(residuals.values()),
        "generation": (
            "Fixed complex integer feature rows, normalized separately; "
            "C=features @ features.conj().T and K_l=diag(features[:,l])."
        ),
        "interpretation": (
            "Finite numerical check of basis-copy masking for this nontrivial "
            "Gram-generated Schur channel, on a complete matrix-unit basis."
        ),
    }


@dataclass(frozen=True)
class Gate:
    kind: str
    qubits: tuple[int, ...]
    angle: float = 0.0


def inverse_gates(gates: Iterable[Gate]) -> list[Gate]:
    result = []
    for gate in reversed(list(gates)):
        angle = -gate.angle if gate.kind in ("CP", "PHASE") else gate.angle
        result.append(Gate(gate.kind, gate.qubits, angle))
    return result


def qft_gates(n: int, offset: int = 0) -> list[Gate]:
    """Positive-sign QFT, including explicit final bit-reversal swaps."""
    gates = []
    for target in range(n - 1, -1, -1):
        gates.append(Gate("H", (offset + target,)))
        for control in range(target - 1, -1, -1):
            angle = math.pi / (1 << (target - control))
            gates.append(Gate("CP", (offset + control, offset + target), angle))
    for low in range(n // 2):
        gates.append(Gate("SWAP", (offset + low, offset + n - 1 - low)))
    return gates


def phase_block_gates(label_bits: int, data_bits: int, label_offset: int) -> list[Gate]:
    """Data occupy qubits 0,...,data_bits-1; the label is retained."""
    gates = []
    for r in range(label_bits):
        for s in range(data_bits):
            if r + s < data_bits:
                angle = math.tau / (1 << (data_bits - r - s))
                gates.append(Gate("CP", (label_offset + r, s), angle))
    return gates


def matrix_from_gates(n: int, gates: Iterable[Gate]) -> np.ndarray:
    """Apply H, CP, SWAP, PHASE, and CX to matrix rows; no Kronecker products."""
    dimension = 1 << n
    rows = np.arange(dimension, dtype=np.int64)
    matrix = np.eye(dimension, dtype=np.complex128)
    for gate in gates:
        require(all(0 <= q < n for q in gate.qubits), f"Invalid wires: {gate}")
        require(len(set(gate.qubits)) == len(gate.qubits), f"Repeated wire: {gate}")
        if gate.kind == "H":
            (q,) = gate.qubits
            low = rows[(rows & (1 << q)) == 0]
            high = low | (1 << q)
            old_low, old_high = matrix[low].copy(), matrix[high].copy()
            matrix[low] = (old_low + old_high) / math.sqrt(2.0)
            matrix[high] = (old_low - old_high) / math.sqrt(2.0)
        elif gate.kind == "CP":
            p, q = gate.qubits
            selected = ((rows >> p) & 1) & ((rows >> q) & 1)
            matrix[selected.astype(bool)] *= np.exp(1j * gate.angle)
        elif gate.kind == "PHASE":
            (q,) = gate.qubits
            matrix[((rows >> q) & 1).astype(bool)] *= np.exp(1j * gate.angle)
        elif gate.kind == "SWAP":
            p, q = gate.qubits
            different = ((rows >> p) ^ (rows >> q)) & 1
            permutation = rows ^ (different << p) ^ (different << q)
            matrix = matrix[permutation].copy()
        elif gate.kind == "CX":
            control, target = gate.qubits
            permutation = rows ^ (((rows >> control) & 1) << target)
            matrix = matrix[permutation].copy()
        else:
            raise ValueError(f"Unsupported gate kind: {gate.kind}")
    return matrix


def dense_fourier(d: int) -> np.ndarray:
    labels = np.arange(d, dtype=np.int64)
    powers = (labels[:, None] * labels[None, :]) % d
    return np.exp(1j * math.tau * powers / d) / math.sqrt(d)


def restricted_phase_diagonal(
    gates: Iterable[Gate], label: int, label_offset: int, data_bits: int
) -> np.ndarray:
    """Restrict enumerated controlled phases to a fixed computational label."""
    basis = np.arange(1 << data_bits, dtype=np.int64)
    diagonal = np.ones(1 << data_bits, dtype=np.complex128)
    for gate in gates:
        require(gate.kind == "CP", "Phase block contains a non-phase gate")
        control, target = gate.qubits
        require(control >= label_offset and 0 <= target < data_bits, "Bad phase-block wires")
        if (label >> (control - label_offset)) & 1:
            diagonal[((basis >> target) & 1).astype(bool)] *= np.exp(1j * gate.angle)
    return diagonal


def expand_phase_and_swap_gates(gates: Iterable[Gate]) -> list[Gate]:
    """A chronological, ancilla-free expansion into H, PHASE, and CX."""
    expanded = []
    for gate in gates:
        if gate.kind == "CP":
            control, target = gate.qubits
            expanded.extend(
                [
                    Gate("PHASE", (control,), gate.angle / 2),
                    Gate("PHASE", (target,), gate.angle / 2),
                    Gate("CX", (control, target)),
                    Gate("PHASE", (target,), -gate.angle / 2),
                    Gate("CX", (control, target)),
                ]
            )
        elif gate.kind == "SWAP":
            p, q = gate.qubits
            expanded.extend(
                [Gate("CX", (p, q)), Gate("CX", (q, p)), Gate("CX", (p, q))]
            )
        elif gate.kind == "H":
            expanded.append(gate)
        else:
            raise ValueError(f"Unexpected encoder gate: {gate.kind}")
    return expanded


def gate_counts(gates: Iterable[Gate]) -> dict[str, int]:
    return dict(sorted(Counter(gate.kind for gate in gates).items()))


def check_circuit_case(m: int) -> dict:
    n, length, d = 2 * m, 1 << m, 1 << (2 * m)
    a_offset, b_offset = n, n + m
    forward_gates = qft_gates(n)
    backward_gates = inverse_gates(forward_gates)
    phase_a_gates = phase_block_gates(m, n, a_offset)
    phase_b_gates = phase_block_gates(m, n, b_offset)
    encoder_gates = (
        [Gate("H", (q,)) for q in range(n, n + 2 * m)]
        + phase_b_gates
        + forward_gates
        + phase_a_gates
        + backward_gates
    )
    tolerance = numerical_tolerance(d, len(encoder_gates))
    residuals: dict[str, float] = {}

    def record(name: str, value: float) -> None:
        residuals[name] = require_small(f"m={m}: {name}", value, tolerance)

    fourier = dense_fourier(d)
    forward = matrix_from_gates(n, forward_gates)
    backward = matrix_from_gates(n, backward_gates)
    record("gate_QFT_equals_positive_dense_Fourier", operator_norm(forward - fourier))
    record("gate_inverse_QFT_equals_dense_adjoint", operator_norm(backward - fourier.conj().T))
    record("inverse_QFT_times_QFT", operator_norm(backward @ forward - np.eye(d)))

    basis = np.arange(d, dtype=np.int64)
    a_diagonals, b_diagonals = [], []
    max_phase_a, max_phase_b = 0.0, 0.0
    for label in range(length):
        expected = np.exp(1j * math.tau * ((label * basis) % d) / d)
        a_diag = restricted_phase_diagonal(phase_a_gates, label, a_offset, n)
        b_diag = restricted_phase_diagonal(phase_b_gates, label, b_offset, n)
        a_diagonals.append(a_diag)
        b_diagonals.append(b_diag)
        max_phase_a = max(max_phase_a, float(np.max(np.abs(a_diag - expected))))
        max_phase_b = max(max_phase_b, float(np.max(np.abs(b_diag - expected))))
    record("binary_phase_A_block", max_phase_a)
    record("binary_phase_B_block", max_phase_b)

    branch_maximum = 0.0
    worst_branch = [0, 0]
    for a in range(length):
        # The gate-by-gate QFT matrices and enumerated phase gates are used here.
        addition = backward @ (a_diagonals[a][:, None] * forward)
        for b in range(length):
            actual = addition * b_diagonals[b][None, :]
            # Independent direct basis action: |j> -> omega**(b*j)|j+a>.
            expected = np.zeros((d, d), dtype=np.complex128)
            expected[(basis + a) % d, basis] = np.exp(
                1j * math.tau * ((b * basis) % d) / d
            )
            residual = operator_norm(actual - expected)
            require_small(f"m={m}, branch a={a}, b={b}", residual, tolerance)
            if residual > branch_maximum:
                branch_maximum, worst_branch = residual, [a, b]
    record("all_Xa_Zb_branches", branch_maximum)

    # Count actual instructions, then compare with independently stated formulas.
    counted = gate_counts(encoder_gates)
    expected_counts = {"H": 6 * m, "CP": 7 * m * m - m, "SWAP": 2 * m}
    require(counted == expected_counts, f"m={m}: encoder gate count mismatch")
    expected_one_phase_block = (3 * m * m + m) // 2
    require(len(phase_a_gates) == expected_one_phase_block, "Phase A block count mismatch")
    require(len(phase_b_gates) == expected_one_phase_block, "Phase B block count mismatch")
    require(
        gate_counts(forward_gates) == {"H": n, "CP": n * (n - 1) // 2, "SWAP": n // 2},
        "QFT gate count mismatch",
    )
    touched_qubits = {q for gate in encoder_gates for q in gate.qubits}
    require(touched_qubits == set(range(4 * m)), "Unexpected encoder register footprint")

    expanded = expand_phase_and_swap_gates(encoder_gates)
    expanded_counts = gate_counts(expanded)
    expected_expanded_counts = {
        "H": 6 * m,
        "CX": 14 * m * m + 4 * m,
        "PHASE": 3 * (7 * m * m - m),
    }
    require(expanded_counts == expected_expanded_counts, "Primitive gate count mismatch")
    require(
        {q for gate in expanded for q in gate.qubits} == touched_qubits,
        "Primitive expansion introduced an extra work qubit",
    )

    # Independently check the two-qubit decompositions used for these counts.
    distinct_angles = sorted({g.angle for g in encoder_gates if g.kind == "CP"})
    decomposition_residual = 0.0
    for angle in distinct_angles:
        target = np.diag([1.0, 1.0, 1.0, np.exp(1j * angle)])
        compiled = matrix_from_gates(
            2, expand_phase_and_swap_gates([Gate("CP", (0, 1), angle)])
        )
        decomposition_residual = max(decomposition_residual, operator_norm(compiled - target))
    swap_target = np.asarray(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
        dtype=np.complex128,
    )
    swap_compiled = matrix_from_gates(
        2, expand_phase_and_swap_gates([Gate("SWAP", (0, 1))])
    )
    decomposition_residual = max(
        decomposition_residual, operator_norm(swap_compiled - swap_target)
    )
    decomposition_tolerance = numerical_tolerance(4, 5)
    require_small("two-qubit decompositions", decomposition_residual, decomposition_tolerance)
    residuals["CP_and_SWAP_primitive_decompositions"] = decomposition_residual

    return {
        "m": m,
        "input_qubits": n,
        "d": d,
        "L": length,
        "total_encoder_qubits": 4 * m,
        "additional_work_qubits": 0,
        "bit_order": "qubit q has binary weight 2**q",
        "registers": {
            "B": list(range(n)),
            "a": list(range(a_offset, a_offset + m)),
            "b": list(range(b_offset, b_offset + m)),
        },
        "phase_labels_checked_per_block": length,
        "Weyl_branches_checked": length * length,
        "worst_branch_a_b": worst_branch,
        "operation_scale_for_tolerance": len(encoder_gates),
        "tolerance": tolerance,
        "decomposition_tolerance": decomposition_tolerance,
        "residual_norm": "operator norm; diagonal phase residuals use max absolute entry",
        "residuals": residuals,
        "largest_residual": max(residuals.values()),
        "enumerated_gate_counts": counted,
        "formula_gate_counts": expected_counts,
        "enumerated_one_phase_block_count": len(phase_a_gates),
        "enumerated_QFT_counts": gate_counts(forward_gates),
        "enumerated_primitive_counts": expanded_counts,
        "formula_primitive_counts": expected_expanded_counts,
        "primitive_expansion_angles_checked": len(distinct_angles),
        "method": (
            "QFT and inverse are constructed gate by gate on B. Full encoder "
            "instructions are enumerated, while each fixed-label branch is "
            "evaluated on B; no 2**(4m)-dimensional encoder matrix is built."
        ),
    }


def build_report() -> dict:
    weyl_cases = [check_weyl_case(d) for d in WEYL_DIMENSIONS]
    schur_case = check_schur_masking()
    circuit_cases = [check_circuit_case(m) for m in CIRCUIT_M_VALUES]
    all_sections = weyl_cases + [schur_case] + circuit_cases
    return {
        "format_version": 1,
        "status": "pass",
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "real_dtype": "float64",
            "complex_dtype": "complex128",
            "machine_epsilon": EPS,
        },
        "deterministic_inputs": True,
        "random_sampling_used": False,
        "largest_dense_matrix_dimension": max(WEYL_DIMENSIONS),
        "tolerance_policy": {
            "formula": "128 * eps_float64 * matrix_dimension * operation_scale",
            "purpose": (
                "Conservative double-precision verification threshold for "
                "unit-norm products, sums, and stable dense linear algebra; "
                "not a certified interval roundoff bound."
            ),
            "per_case_tolerances_and_residuals_reported": True,
        },
        "largest_reported_residual": max(s["largest_residual"] for s in all_sections),
        "weyl_cases": weyl_cases,
        "schur_basis_copy_case": schur_case,
        "circuit_cases": circuit_cases,
        "not_numerically_certified": [
            "Analytical diamond-norm leakage and perturbation bounds",
            "Distance from every Schur channel, including the 1/48 bound",
            "Universal exact masking classification",
            "Homotopy invariance underlying the winding/Bott obstruction",
            "Optimality of leakage exponents or resource counts",
            "A Solovay-Kitaev compiler or a hardware implementation",
        ],
        "solver_use": "No SDP, optimization solver, SciPy, or new dependency",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()
    report = build_report()
    serialized = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is None:
        print(serialized, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
        print(
            f"PASS: {len(WEYL_DIMENSIONS)} Weyl cases, "
            f"{report['schur_basis_copy_case']['matrix_units_checked']} Schur matrix units, "
            f"{len(CIRCUIT_M_VALUES)} circuit cases; "
            f"largest residual {report['largest_reported_residual']:.3e}. "
            f"Report: {args.output}"
        )


if __name__ == "__main__":
    main()
