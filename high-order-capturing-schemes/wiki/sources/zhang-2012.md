---
type: Source
title: "Zhang & Shu (2012) — Positivity-preserving high order finite difference WENO schemes for compressible Euler equations"
description: "Extends the Zhang–Shu positivity limiter to finite-difference WENO: with a global Lax–Friedrichs splitting the FD scheme is two FV WENO schemes for the split fluxes, whose reconstructed values are limited; includes local splitting, source terms, general equations of state and multi-D."
resource: "doi:10.1016/j.jcp.2011.11.020"
source_kind: paper
authors: [Zhang X., Shu C.-W.]
year: 2012
venue: "J. Comput. Phys. 231:2245-2258"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2012-JCP-Zhang-101016jjcp201111020.pdf"
tags: [positivity, limiter, finite-difference, weno, euler]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

FD WENO is preferred over DG and FV WENO for multi-D cost, but the
positivity framework of 2010 is not directly applicable to it. This
paper bridges the gap through the reconstruction-pair view of FD
schemes. Merged into the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md),
[positivity preservation](/properties/positivity-preserving.md),
[conservative finite difference](/methods/conservative-finite-difference.md)
and benchmark pages.

# Key claims

1. **Reconstruction pair** (§2.2): an FD WENO scheme for $u$ is an FV
   WENO scheme for $\mathcal{H}$. A maximum principle cannot be enforced
   this way without losing accuracy, because $\mathcal{H}$ overshoots
   $u$; positivity of solutions bounded away from zero can.
2. **Theorem 3.1**: with the global LF splitting into the states
   $\frac12(u \pm f/\alpha)$, the update is a sum of two FV schemes. It is
   positivity-preserving under $\alpha\Delta t/h \le \hat w_1$ if the
   limited reconstructed split values are admissible; eqs. (3.7)–(3.11)
   checked on the page image.
3. **CFL** (Remark 3.3): $\hat w_1 = 1/12$ (fifth order) and $1/20$
   (seventh order), much smaller than usual but only sufficient; enforced
   only when a trial step fails.
4. **Generalizations** (§4): local LF halves the CFL bound; geometric,
   gravity, reaction and radiative-cooling sources; general equations of
   state through concavity of $\rho e$; multi-D by direction splitting
   of the update.
5. **Tests** (§5, WENO5 + RK3): near-vacuum vortex at fifth order;
   double rarefaction; 1D and 2D Sedov; shock diffraction; Mach 2000
   jet; detonation diffraction; a three-species reacting flow, which
   needs the WENO $\varepsilon$ lowered from $10^{-6}$ to $10^{-20}$ for
   densities near $10^{-10}$.

# Notation map

| Zhang & Shu (2012) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf w$ | $u$ | |
| $\mathbf f^\pm(\mathbf w) = \frac12(\mathbf w \pm \mathbf f/\alpha)$ | $\pm f^\pm/\alpha$ | registry $f^\pm = \frac12(f \pm \alpha u)$ |
| $\mathbf h^\pm = R_{\Delta x}(\mathbf f^\pm)$ | $\mathcal{H}$ of the split fluxes | reconstruction pair |
| $a$ (max $\vert u\vert + c$) | $\alpha$ | |
| $A_{i+1/2}$, $L$, $R$ | Roe matrix, $\ell^{(p)}$, $r^{(p)}$ | |
| $\hat w_1$, $\hat w_N$ | $\hat w_1$, $\hat w_{N_{\mathrm{GL}}}$ | |
| $\theta_1$, $\theta_2$ | $\theta_\rho$, $\theta_p$ | |
| $\varepsilon$ | $\epsilon_{\mathcal{G}}$ | |

# Pages created or updated

* Updated [Double-rarefaction (near-vacuum) Riemann problems](/benchmarks/double-rarefaction.md).
* Updated [High-Mach-number astrophysical jet (Mach 80 and Mach 2000)](/benchmarks/high-mach-astrophysical-jet.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Sedov point-blast wave (low-density positivity test)](/benchmarks/sedov-blast-wave.md).
* Updated [Shock diffraction at a backward-facing corner](/benchmarks/shock-diffraction.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [Zhang–Shu positivity-preserving scaling limiter](/methods/positivity-preserving-scaling-limiter.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2012-JCP-Zhang-101016jjcp201111020.pdf` (doi:10.1016/j.jcp.2011.11.020; typeset article): text extraction, all sections; §§3.2–4.1 (eqs. 3.4–4.3, Remark 3.3) read from the page images (pp. 2249–2250). The time-step choice in the accuracy test is illegible in the text layer and not reproduced. Reference list: 23 entries.
