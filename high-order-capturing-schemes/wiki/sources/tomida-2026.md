---
type: Source
title: "Tomida et al. (2026) — Systematic comparison between constrained transport and mixed divergence cleaning methods for astrophysical MHD simulations"
description: "Same-code (Athena++) comparison of Stone–Gardiner CT and Dedner mixed GLM cleaning: the cleaning is derived under constant, uniform parameters, a time-step-tied cleaning speed makes spurious divergent fields when the step drops, localized fields leak at any resolution, AMR breaks the assumptions, and EGLM's energy term matters at low β; CT is judged more robust."
resource: "doi:10.3847/1538-4365/ae8785"
source_kind: paper
authors: [Tomida K., Sadanari K.E., Takasao S., Iwasaki K.]
year: 2026
venue: "Astrophys. J. Suppl. 285:64"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2026-ApJS-Tomida-1038471538-4365ae8785.pdf"
tags: [mhd, divergence-free, glm, constrained-transport, amr]
timestamp: 2026-10-09T00:00:00Z
---

# Summary

The authors add mixed GLM cleaning to Athena++, next to its CT solver,
and compare the two with everything else equal (second-order van Leer
integrator, piecewise-linear primitives, HLLD). They show that the
cleaning is derived under two assumptions, smooth fields and an operator
that commutes with $\partial_t$ and $\nabla$, and that common practice
breaks the second. Merged into the [GLM](/methods/hyperbolic-divergence-cleaning.md)
page (consistency conditions, AMR, and an open `## Contradictions` entry
on the cleaning speed), the [CT](/methods/constrained-transport.md),
[high-order AMR](/methods/high-order-amr.md),
[positivity](/properties/positivity-preserving.md) and
[PLUTO](/software/pluto.md) pages, and the Alfvén-wave benchmark.

# Key claims

1. **Derivation and assumptions** (§2.3.1, eqs. 8–12). $\psi_{\mathrm{GLM}}$
   and $\nabla\cdot\mathbf B$ obey the same telegraph equation only if the
   fields are smooth and the cleaning operator commutes with time and space
   derivatives.
2. **Time-step-tied $c_h$** (§2.3.3, eq. 19): $c_h = \nu h_{\min}/\Delta t^n$,
   "the largest possible $c_h$ which does not introduce any additional
   timestep constraint", violates assumption (ii).
3. **Damping length** (eq. 20): Dedner's $c_r = 0.18$ is dimensional;
   $C_r = c_p^2/(c_h L_{\mathrm{GLM}})$ with a free length. PLUTO uses
   $L_{\mathrm{GLM}} = h_{\min}$, which changes under AMR.
4. **Leakage** (§3.2): a localized field leaks into weakly magnetized gas,
   up to $|\mathbf B| \sim 10^{-4}$ ($L_{\mathrm{GLM}} = 1$) or $10^{-2}$
   ($L_{\mathrm{GLM}} = h$), at any resolution and with constant $c_h$.
5. **Time-step drop** (§3.3): $\Delta t$ divided by 40 for 100 steps raises
   $\max\psi_{\mathrm{GLM}}$ about 40-fold; the excess becomes spurious
   non-solenoidal ripples. Constant $c_h$ and CT are unaffected.
6. **Stability** (§§3.1.2, 4.1.2): with constant $c_h$ the KHI run needs
   $c_h$ above the maximum flow speed ($c_h \lesssim 1.0$ is unstable).
7. **Collapse on AMR** (§3.4, Fig. 9): peak field $7.1\times10^{-4}$ G
   (time-step-tied $c_h$, $L_{\mathrm{GLM}} = 1$) against $6.8\times10^{-9}$ G
   (CT) and $4.2\times10^{-9}$ G (constant $c_h$).
8. **Refresh** (§4.1.2): project and reset $\psi_{\mathrm{GLM}} = 0$ before any
   change of $c_h$.
9. **EGLM energy term** (App. B): without it the thermal-energy error on a
   CPAW at plasma beta $1.98\times10^{-4}$ reaches about 30%, as for CT,
   whose cell-centred field is a linear average of face fields.
10. **Conclusion** (§5): CT "is less arbitrary, more robust and less prone
    to spurious behaviors"; the conventional variable-speed implementation
    is "strongly discouraged".

**Tests**: magnetized KHI with uniform and localized fields and with an
imposed time-step drop; primordial and present-day cloud collapse on AMR;
a stratified convective dynamo (third order, RK3 and PPM); the
circularly polarized Alfvén wave (GLM vs EGLM vs CT); Powell's
eight-wave scheme on the localized-field KHI. None of the bundle's
field-loop, blast, Orszag–Tang or rotor benchmarks is run.

# Notation map

| Tomida et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ | $\psi_{\mathrm{GLM}}$ | |
| $c_h$, $c_p$ | $c_h$, $c_p$ | |
| $C_r$, $L$ | $C_r$, $L_{\mathrm{GLM}}$ | registry $L$ is the left-eigenvector matrix |
| $\tau_d$, $t_{\mathrm{adv}}$ | (words) | registry $\tau$ is the WENO-Z indicator |
| $\eta_{\mathrm{CFL}}$ | $\nu$ | |
| $h$, $h_{\min}$ | $h$, $\min_d h_d$ | |
| $c_s$, $v_a$ | $c$, $c_A$ | registry $c_s$ is the slow speed |
| $\beta$ | (words: plasma beta) | |

# Pages created or updated

* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md): consistency conditions, AMR, EGLM energy, `## Contradictions`.
* Updated [Constrained transport](/methods/constrained-transport.md), [High-order AMR](/methods/high-order-amr.md), [Positivity preservation](/properties/positivity-preserving.md), [PLUTO](/software/pluto.md), [Circularly polarized Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Notation registry](/notation.md): $L_{\mathrm{GLM}}$, $C_r$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2026-ApJS-Tomida-1038471538-4365ae8785.pdf` (arXiv:2605.07928v2, 11 Jul 2026, post-review manuscript; doi:10.3847/1538-4365/ae8785 checked on Crossref: Astrophys. J. Suppl. 285(2):64, August 2026): text extraction, all sections; Fig. 9 values read from the page image, other figures from captions. Reference list: 63 entries in AAS style, which prints no article titles.
