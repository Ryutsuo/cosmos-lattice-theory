# Cellular Polarity and Cancer: A Lattice Vacuum Framework
# for Membrane Potential as Geometric Attractor

**Author:** David Botargues Martín
**Date:** May 2026
**Contact:** akirashenkai@gmail.com
**Related work:** DOI 10.5281/zenodo.20320293

---

## Abstract

We propose that the healthy/cancerous cell duality is a biological
instantiation of the Lattice Vacuum Theory's fundamental equation
Light + Dark = tanh(r₀/l_P) + (1 - tanh(r₀/l_P)) = 1.

A healthy cell maintains negative membrane potential V_m ≈ -70mV
(cooperative state, tanh → 1). A cancerous cell exhibits depolarized
membrane potential V_m → 0mV (absorptive state, tanh → 0).

We model this as a dynamic system where membrane potential follows
the same geometric attractor as the Lattice resolution r₀(R).
We make one falsifiable prediction: restoring membrane potential
to the healthy attractor state should suppress cancerous behavior,
consistent with existing TTFields therapy results.

---

## 1. The Polarity Framework

### 1.1 Healthy Cell — Cooperative State

```
V_healthy = -70 mV  (resting membrane potential)
State     = tanh(r₀/l_P) → 1  (deep vacuum, cooperative)
Behavior  = regulated division, apoptosis intact
ACGT      = normal expression pattern
```

### 1.2 Cancerous Cell — Absorptive State

```
V_cancer  = -20 to 0 mV  (depolarized)
State     = 1 - tanh(r₀/l_P) → 0  (shallow vacuum, absorptive)
Behavior  = unregulated division, apoptosis suppressed
ACGT      = mutated expression pattern
```

### 1.3 The Conservation Law

```
Healthy + Cancer = tanh(V) + (1 - tanh(V)) = 1

Always. In every cell. At every moment.
```

This means: a cancerous cell contains all the information
needed to reconstruct the healthy state. The information
is not lost — it is transformed. r₀ > 0 always.

---

## 2. Mathematical Model

### 2.1 Membrane Potential as Lattice Analog

We propose the following mapping:

```
r₀(R) / l_P  ↔  |V_m| / V_threshold

where V_threshold = 70 mV (healthy resting potential)
```

The Lattice equation becomes:

```
φ(V_m) = tanh(|V_m| / V_threshold)

φ = 1.0  →  healthy cell  (V_m = -70mV)
φ = 0.5  →  pre-cancerous (V_m = -35mV)
φ → 0    →  cancerous     (V_m → 0mV)
```

### 2.2 Dynamic Equation

The membrane potential evolves as:

```
dV_m/dt = -γ·(V_m - V_attractor) + η(t) + Cell(t)

where:
γ           = restoration rate (healthy cell machinery)
V_attractor = -70mV (healthy attractor)
η(t)        = noise (random mutations)
Cell(t)     = adversarial term (oncogenic signals)
```

This is identical in structure to the Lattice equation:

```
dr₀/dt = -γ·(r₀ - l_P) + perturbations
```

### 2.3 Cancer as Loss of Attractor

Cancer occurs when Cell(t) overwhelms γ:

```
|Cell(t)| >> γ  →  V_m drifts from -70mV toward 0mV
                →  φ(V_m) drifts from 1 toward 0
                →  cell loses cooperative behavior
```

### 2.4 Cure as Attractor Restoration

Restoring the healthy attractor requires:

```
γ_restored > |Cell(t)|

Methods:
1. Increase γ: restore tumor suppressor genes (p53, BRCA)
2. Decrease Cell(t): block oncogenic signals
3. Direct V_m restoration: TTFields therapy (external electric fields)
```

---

## 3. The ACGT Encoding

Every cell state can be encoded as:

```
A = 00  →  adenine  →  energy storage
C = 01  →  cytosine →  structural
G = 10  →  guanine  →  signaling
T = 11  →  thymine  →  regulation
```

Healthy cell: balanced ACGT expression
Cancer cell:  imbalanced — certain codons overexpressed

The transformation healthy → cancer is a specific ACGT
mutation pattern. The inverse transformation cancer → healthy
requires identifying and reversing that pattern.

This is computationally equivalent to finding the inverse
of a hash function — which connects to P vs NP:

```
Verify cancer state:   easy (sequence the genome)
Find cure:             hard (find the inverse transformation)
```

---

## 4. Falsifiable Predictions

**Prediction 1 — Membrane potential threshold:**
Cells with V_m < -50mV should show significantly lower
proliferation rates than cells with V_m > -30mV.
Testable with patch-clamp electrophysiology.

**Prediction 2 — TTFields mechanism:**
TTFields therapy works by forcing V_m oscillation around
the healthy attractor (-70mV), disrupting the cancerous
attractor (0mV).
Prediction: TTFields efficacy correlates with
|V_m_healthy - V_m_cancer| in individual patients.

**Prediction 3 — Information preservation:**
Since r₀ > 0 always, the healthy cell information is
preserved in the cancerous cell's geometry.
Prediction: every cancer cell retains epigenetic markers
of its healthy origin state, recoverable by
methylation reprogramming.

---

## 5. Connection to P vs NP

The cancer problem is a biological instantiation of P vs NP:

```
P side (easy):  verify that a cell is cancerous
                → sequence genome, measure V_m: O(n)

NP side (hard): find the transformation that cures it
                → search space of all possible
                  gene expression states: O(2^n)
```

If the Lattice framework is correct — if every cancer cell
preserves its healthy origin state — then the search space
is not 2^n but 1: the original healthy attractor.

This would mean: cancer is always curable in principle,
because the information to restore the healthy state
is always present. r₀ > 0. Information is never destroyed.

The practical challenge is reading that information
and applying the correct inverse transformation.

---

## 6. Conclusion

We propose that cancer is a geometric phenomenon —
a cell that has lost its attractor state — rather than
purely a genetic phenomenon.

The Lattice Vacuum framework predicts:
1. Membrane potential follows the same attractor dynamics
   as the vacuum resolution r₀(R)
2. The healthy/cancerous duality satisfies
   φ + (1-φ) = 1 always
3. Information is preserved — every cancer cell contains
   its healthy origin state
4. Restoration is theoretically possible for all cancers

These predictions are falsifiable with existing technology.

---

## 5. Oxygen-Membrane Potential Coupling

The oxygen concentration follows the same attractor dynamics:

```
φ_O2(pO2) = tanh(pO2 / pO2_threshold)

where pO2_threshold = 5% O2 (normoxia threshold)

Normoxia (5-7% O2):   φ_O2 = 0.76  →  healthy attractor
Hypoxia  (<1% O2):    φ_O2 → 0     →  cancerous state
Hyperoxia (>20% O2):  φ_O2 → 1     →  oxidative stress
```

The stable attractor is at the transition point — not at
the extremes. Exactly as tanh(1) = 0.7616.

**Three therapies — one mechanism:**

| Therapy | Parameter | Effect on φ |
|---------|-----------|-------------|
| TTFields | V_m | Oscillates toward -70mV |
| Photodynamic | Light energy | Increases φ |
| Hyperbaric O2 | pO2 | Restores φ_O2 toward 0.76 |

All three push the cell toward the same attractor.
This unifies three distinct therapies under one framework.

**Prediction 5:** Combined TTFields + hyperbaric O2 should
show synergistic efficacy, because they restore two
independent parameters (V_m and pO2) toward the same
attractor state simultaneously.

Botargues Martín, D. (2026b). Lattice Vacuum Theory.
DOI: 10.5281/zenodo.20320293

Botargues Martín, D. (2026a). Emergent Protocell-like Structures.
DOI: 10.5281/zenodo.19670389

Kirson et al. (2007). Disruption of cancer cell replication
by alternating electric fields. Cancer Research.

Hanahan & Weinberg (2011). Hallmarks of Cancer. Cell.

---

*"A cancerous cell is not the enemy.
It is a healthy cell that lost its way home.
The information to find the way back is always there.
r₀ > 0. Always."*

— David Botargues Martín, May 2026
