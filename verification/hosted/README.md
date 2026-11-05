# Verify the hosted mathematics

The scientific verifier checks the algebra and circuits. This separate collector checks the mathematical content displayed by GitHub for an exact public repository commit.

It inventories all tracked Markdown pages, compiles their formulas into reference MathML, and compares that structure with the actual GitHub page at widths of 1440 and 760 pixels. The comparison retains fractions, scripts, operators and meaningful token formatting. Explicit full-text contracts cover the headline equations and a repaired inline expression. The output includes source hashes, captured HTML, screenshots, per-expression comparisons and a report bound to the source revision.

## Run locally

Use Node.js 18 or later, Python 3.10 or later and a Git checkout containing the exact commit. Install the optional browser dependencies outside the scientific checkout:

```bash
npm install --prefix /absolute/temporary/dependencies playwright@1.56.1 mathjax-full@3.2.1
node /absolute/temporary/dependencies/node_modules/playwright/cli.js install chromium
NODE_PATH=/absolute/temporary/dependencies/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root /absolute/scientific-checkout \
  --repository GoGoKo699/Quantum-Noise-Masking \
  --revision FULL_40_CHARACTER_COMMIT \
  --contract verification/hosted/math-contract.json \
  --output /absolute/new-empty-evidence-directory
```

Replace the illustrative paths and revision with actual values. The collector reads Git objects at that revision, not uncommitted working files, and requires a new output directory for each attempt. Network access to the real public GitHub page is necessary. The [repository workflow](../../.github/workflows/hosted-math.yml) runs the same command in an isolated browser job with read-only repository access and no persisted checkout credentials.

## Read the result

A successful automated report establishes that the declared page and expression inventory matched the observed host at both widths. It does not prove the science, certify all browser versions or replace visual inspection of the screenshots. Inspect equations, tables, navigation and substantial explanations, including every repaired or flagged expression. The report preserves failed or blocked observations as failures.

The [main verification guide](../README.md) gives the separate finite scientific checks and their limits.
