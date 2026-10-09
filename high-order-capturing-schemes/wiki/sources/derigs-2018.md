---
type: Source
title: "Derigs et al. (2018) — Ideal GLM-MHD: about the entropy consistent nine-wave magnetic field divergence diminishing ideal MHD equations"
description: "Derives the Godunov–Powell non-conservative terms as physics, adds the cleaning field through a Galilean-invariant ansatz with its energy in the total energy, proves the resulting nine-wave system entropy-consistent while earlier GLM variants are not, and builds entropy-conservative and entropy-stable fluxes, tested in FLASH against staggered CT."
resource: "doi:10.1016/j.jcp.2018.03.002"
source_kind: paper
authors: [Derigs D., Winters A.R., Gassner G.J., Walch S., Bohm M.]
year: 2018
venue: "J. Comput. Phys. 364:420-467"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2018-JCP-Derigs-101016jjcp201803002.pdf"
tags: [mhd, divergence-free, glm, entropy-stable]
timestamp: 2026-10-09T00:00:00Z
---

# Summary

Rederives ideal MHD from the Euler equations plus Maxwell's equations
with monopoles allowed, so the terms proportional to $\nabla\cdot\mathbf B$
appear as physics, not as a fix. A Lagrangian ansatz then adds the
cleaning field, with its energy $\tfrac12\hat\psi_{\mathrm{GLM}}^2$ in the
total energy. The result, "ideal GLM-MHD", is Galilean invariant and
consistent with the entropy law. Merged into the
[GLM](/methods/hyperbolic-divergence-cleaning.md),
[CT](/methods/constrained-transport.md),
[Riemann-solver](/methods/approximate-riemann-solvers.md) and
[positivity](/properties/positivity-preserving.md) pages and the MHD
benchmarks.

# Key claims

1. **Non-conservative terms are physics** (§2, eqs. 2.16, 2.21). Without
   them the Lorentz force has a component $-(\nabla\cdot\mathbf B)|\mathbf B|$
   along $\mathbf B$. They are needed for Galilean invariance and
   symmetrizability. Dropping the energy term books magnetic-energy errors
   as internal-energy loss, so "the pressure could easily become
   negative" (p. 6, an argument with no test).
2. **The eight-wave system only advects divergence** (eq. 2.22), so it
   accumulates at stagnation points.
3. **Ideal GLM-MHD** (§3.4, eqs. 3.16–3.18): induction flux gains
   $c_h\hat\psi_{\mathrm{GLM}}\mathbf I$; $\partial_t\hat\psi_{\mathrm{GLM}} + c_h\nabla\cdot\mathbf B + \mathbf v\cdot\nabla\hat\psi_{\mathrm{GLM}} = 0$;
   energy includes $\tfrac12\hat\psi_{\mathrm{GLM}}^2$. The field is a factor
   $c_h$ smaller than Dedner's, $\psi_{\mathrm{GLM}} = c_h\hat\psi_{\mathrm{GLM}}$
   (compiler's reading of eqs. 3.2 and 4.13).
4. **Waves** (eq. 3.28): $v_x \pm c_f$, $v_x \pm c_s$, $v_x \pm c_A$, $v_x$,
   $v_x \pm c_h$. **Cleaning speed** (eq. 3.30): $c_h = \lambda_{\max} - \max|v|$,
   global, so the time step is unaffected.
5. **Entropy** (§4, eqs. 4.3, 4.12): the system satisfies an entropy
   conservation law. Dedner's GLM, EGLM, its Galilean-invariant form,
   Mackey–Lim and Tricco–Price cannot yield EC or ES schemes (§4.1).
6. **Fluxes** (§§4.2–4.6): an entropy-conservative, kinetic-energy-preserving
   flux $\hat f^{\mathrm{EC}}$ from arithmetic and logarithmic means;
   entropy-stable $\hat f^{\mathrm{ES}}$ with LF, LLF or matrix dissipation
   built on a discrete entropy Jacobian; high-order EC fluxes from
   LeFloch–Mercier–Rohde combinations (Table 1). How to discretize the
   non-conservative terms provably to high order is "unknown" (p. 28).
7. **Damping** (§4.5): the source $\alpha\psi$ keeps the scheme entropy-stable;
   the damped energy goes to the thermal pressure.
8. **Against CT** (§§3.3, 5.3): whether provably ES schemes exist on
   staggered meshes is not known. GLM needs "appreciably less memory"
   than FLASH's staggered USM solver.

**Tests** (§5, FLASH 4.5, fourth-order EC and third-order ES fluxes,
SSP-RK3, CFL 0.8).
* 1D artificial divergence: periodic hyperbolic-only cleaning stalls at
  $10^{-1}$–$10^0$; mixed cleaning reaches about $10^{-14}$.
* 2D divergence advection (Tricco–Price peak): mixed < hyperbolic < none.
* Rotor and Orszag–Tang on AMR: close to USM CT; without cleaning, OT's
  integrated divergence grows to about 1.07 by $t = 0.5$, with cleaning
  it stays at 0.17–0.19. The USM face divergence is at machine precision,
  but its cell-centred central divergence is comparable to GLM's.
* Rotated Ryu–Jones–Frank shock tube: cleaning cuts the parallel-field
  error "significantly"; the full and Janhunen terms are
  indistinguishable.
* Entropy: $\Delta S \propto \Delta t^3$ with EC fluxes on a rotated Brio–Wu
  problem; Roe shows entropy glitches on Toro's modified Sod and on a new
  modified Brio–Wu ($u_L = 1.75$), the ES flux does not.

# Notation map

| Derigs et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol q$ | $u$ | |
| $\boldsymbol u = (u, v, w)$ | $\mathbf v$ | the paper's bold $\boldsymbol v$ is the entropy-variable vector |
| $\varrho$ | $\rho$ | |
| $\psi$ | $\hat\psi_{\mathrm{GLM}}$ | $\psi_{\mathrm{GLM}} = c_h\hat\psi_{\mathrm{GLM}}$ |
| $c_r = c_p^2/c_h$ | (words) | dimensional, 0.18 |
| $\alpha$ (damping rate) | $c_h^2/c_p^2$ | registry $\alpha$ is the LF speed |
| $c_a$ | $c_A$ | |
| $f^{\mathrm{KEPEC}}$, $f^{\mathrm{KEPES}}$ | $\hat f^{\mathrm{EC}}$, $\hat f^{\mathrm{ES}}$ | |
| $\beta = \varrho/(2p)$, $S$, $\boldsymbol v$, $\mathsf H$, $\boldsymbol\Upsilon$ | (words) | collide with $\beta_k$, $S_k$, $\mathbf v$, $\mathcal H$ |
| $\Delta x$ | $h$ | |

# Pages created or updated

* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md): ideal GLM-MHD and its cleaning speed.
* Updated [Constrained transport](/methods/constrained-transport.md): the face vs cell-centred divergence of a staggered run.
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md): EC and ES fluxes, entropy glitches.
* Updated [Positivity preservation](/properties/positivity-preserving.md): the non-conservative energy term.
* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [MHD rotor](/benchmarks/mhd-rotor.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md), [Sod shock tube](/benchmarks/sod-shock-tube.md).
* Updated [Notation registry](/notation.md): $\hat\psi_{\mathrm{GLM}}$, $\hat f^{\mathrm{EC}}$, $\hat f^{\mathrm{ES}}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2018-JCP-Derigs-101016jjcp201803002.pdf` (arXiv:1711.06269v3, 19 Apr 2018, most likely the accepted text; doi:10.1016/j.jcp.2018.03.002 checked on Crossref: J. Comput. Phys. 364:420–467, July 2018): text extraction, all sections; eqs. 3.15–3.17, 3.31–3.33, 4.43–4.45, 4.75–4.78 and 4.79–4.96 with Table 1 read from the page images. Large matrices (eqs. 3.23–3.27, 4.54–4.70, Apps. A–D) summarized, not reproduced. Printed sign slips in eqs. 3.14–3.15 and 4.77, and $\tfrac1{60}$ for $\tfrac1{30}$ in eqs. 4.94–4.95, taken as typos. Reference list: 63 entries.
