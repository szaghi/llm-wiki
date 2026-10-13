---
type: Source
title: "van Leer & Nomura (2005) — Discontinuous Galerkin for diffusion"
description: "Proposes the recovery principle for DG diffusion: at each interface, recover the smooth polynomial on the two adjacent cells with the same Legendre moments as the discrete solution and use it in the twice-integrated weak form; Fourier analysis gives fourth order for K = 1 and an eighth-order good eigenvalue for K = 2 (unconfirmed), recovery lies outside the (σ, μ) interior-penalty family, and one steady 1D test confirms order 4 against order 2 for the Symmetric and Baumann schemes."
resource: "doi:10.2514/6.2005-5108"
source_kind: paper
authors: [van Leer B., Nomura S.]
year: 2005
venue: "AIAA Paper 2005-5108 (17th AIAA CFD Conference)"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2005-AIAA-VanLeer-10251462005-5108.pdf"
tags: [dg, accuracy, legendre-basis, stability]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A conference paper arguing that DG for diffusion has lacked a guiding
principle. The classic interface terms (Arnold's interior penalty, the
Symmetric and Baumann bilinear terms, unified by van Raalte as a
$(\sigma, \mu)$ family) are read as *ad hoc* Lagrange-multiplier terms.
The **recovery principle** replaces them: at each interface, recover a
smooth polynomial on the union of the two adjacent cells that has the
same moments as the discrete solution against all $K+1$ Legendre test
functions in both cells, and use its value and derivative in a weak form
integrated by parts twice. The paper also argues that advection
(upwind, data "as is") and diffusion (unbiased, smooth recovery) need
different interpretations of the same data. Orders come from Fourier
eigenvalue and eigenvector analysis, not proofs. Merged into
[recovery DG for diffusion](/methods/recovery-dg-diffusion.md).

# Key claims

1. **Advection side** (§2). Finite-difference schemes from $p$-th-order
   interpolation correspond to finite-volume schemes with subcell
   polynomials of order $p-1$; directionally unbiased interpolation gives
   an upwind-biased advection operator (§2.2). DG keeps a fixed stencil
   as the order grows and superconverges (§2.3). Van Leer's 1977 Schemes
   III and VI are DG with exact-shift time stepping; Scheme III advects
   one eigenfunction at third order. Its extension to nonlinear systems
   failed because the exact shift no longer applies (§2.3).
2. **The weak form alone fails at $K = 0$** (§2.4, eqs. 12–15; §3.4,
   eqs. 33–35). For advection it gives a zero right-hand side, so upwind
   values must be borrowed from finite volume; for diffusion it does not
   fix the penalty, which consistency sets to exactly 1.
3. **FTCS diffusion** is stable for diffusion number at most $\tfrac12$;
   Richardson's leap-frog and a one-sided version are unconditionally
   unstable (§3.1, eqs. 16–19). The standard FV face gradient
   differentiates a continuous piecewise-linear interpolant that does not
   conserve cell averages; a short-time exact diffusion solution at each
   jump is inconsistent (§3.2, eqs. 20–25).
4. **$(\sigma, \mu)$ family, $K = 1$** (§3.5, eqs. 36–58). Baumann's
   scheme has a second-order good eigenvalue that vanishes at the $2h$
   mode (odd–even decoupling); the stabilized Symmetric scheme is second
   order; consistency of the slope update requires $\sigma + \mu = \tfrac52$
   (eq. 57, "omitting details"), and the member $\mu = \tfrac94$,
   $\sigma = \tfrac14$ is fourth order (eq. 58; Appendix A3, no proof).
5. **Recovery** (§4, eqs. 59–85). $K = 0$ reproduces the three-point
   scheme without a parameter; $K = 1$ is stable with good eigenvalue
   $-\xi^2 + O(\xi^6)$ and bad-eigenfunction weight $O(\xi^6)$, "truly
   fourth-order accurate"; $K = 2$ has good eigenvalue
   $-\xi^2 + O(\xi^{10})$, possibly eighth order, unconfirmed. "A general
   proof remains to be found" (p. 16).
6. **Recovery is not in the family** (§5.1); a suboptimal (smoothed)
   recovery is second order (§5.2); a new $[v_x][u_x]$ bilinear term with
   coefficient $\omega$ extends the family to contain both recovery
   schemes for $K = 1$ (§5.3).
7. **Order needs both** the best eigenvalue (operator error) and the
   bad-eigenfunction weight in the projected data (starting error)
   (Appendix A1).

**Test** (§6, eqs. 102–106; $K = 1$ only): steady 1D diffusion with a
source, Dirichlet and Neumann ends, error in cell averages. $L_2$ slopes
(Fig. 5): Recovery 3.967, $(\sigma, \mu) = (\tfrac14, \tfrac94)$ 3.497,
suboptimal recovery and stabilized Symmetric 2.002, Baumann 2.078.
Baumann with two Dirichlet ends shows odd–even decoupling (Fig. 6). The
boundary recovery degree controls the observed order: 2.882 (quadratic)
against 3.922 (quartic) in $L_\infty$ (Fig. 7). $K = 2$ errors are at
round-off on a 4-cell grid. The diffusion coefficient, the time
integrator and the grid sizes are not printed.

# Notation map

| van Leer & Nomura (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$, $x_{j\pm\frac12}$, $I_j$ | $i$, $x_{i\pm1/2}$, $I_i$ | the paper's $I_j$ is open |
| $\Delta x$ | $h$ | |
| $D$ | $\mu$ | diffusion coefficient, as in the ILW convection–diffusion problem |
| $\mu$ (penalty) | $\mu_{\mathrm{IP}}$ (registered, batch 11) | collides with the diffusion coefficient $\mu$ |
| $\sigma$ | $\sigma_{\mathrm{DG}}$ (registered, batch 11) | collides with the Hu–Adams–Shu $\sigma$ |
| $\omega$ | $\omega_{\mathrm{DG}}$ (registered, batch 11) | collides with the weights $\omega_k$ |
| $r = D\Delta t/(\Delta x)^2$ | words ("diffusion number") | $r$ is the stencil count |
| $p$ (polynomial degree) | $K$ | $p$ is the pressure |
| $v_m$ (unnormalized Legendre functions) | $P_l(\zeta)$ | eq. 81 prints $v_1$ for the quadratic, a misprint for $v_2$ |
| $\overline{\Delta u}_j$, $\overline{\Delta^2 u}_j$ | $\hat u^{(1)}_i$, $2\hat u^{(2)}_i$ | $\Delta u_i$ is the PPM jump |
| $[q]$, $\langle q\rangle$ | $[\![q]\!]$, $\{\!\{q\}\!\}$ (registered, batch 11) | $\langle w\rangle_{i+1/2}$ is the face average |
| $f(\xi)$, $f_0$, $f'_0$, … | $u^{\mathrm{rec}}_{i+1/2}$ and its face values (registered, batch 11) | $f$ is the flux; the paper's $\xi$ is $x - x_{j+\frac12}$ |
| $\mathcal U(x, t^n)$ | words | $\mathcal U$ is the primitive |
| $\beta$ | $\xi$ | Fourier angle per cell; $\beta_k$ is the smoothness indicator |
| $\lambda_{1,2,3}$, $T$, $M$, $\hat M$ | words | eigenvalues, shift, scheme matrices; collide with $\lambda^{(p)}$, $\mathcal T$, $M$ |

# Pages created or updated

* Created [Recovery discontinuous Galerkin for diffusion](/methods/recovery-dg-diffusion.md).
* Proposed for the [notation registry](/notation.md): $\mu_{\mathrm{IP}}$, $\sigma_{\mathrm{DG}}$, $\omega_{\mathrm{DG}}$, $[\![\cdot]\!]$, $\{\!\{\cdot\}\!\}$, $u^{\mathrm{rec}}_{i+1/2}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2005-AIAA-VanLeer-10251462005-5108.pdf`.
   * **Version.** The published AIAA conference paper (download banner
     dated April 22, 2016), 30 pages. Not a preprint.
   * **Identity.** doi:10.2514/6.2005-5108, printed in the download banner
     and checked on Crossref: proceedings article, "Discontinuous Galerkin
     for Diffusion", van Leer B. and Nomura S., 17th AIAA Computational
     Fluid Dynamics Conference (Toronto, 6–9 June 2005), no page range.
   * **How it was read.** The text layer is garbled (Type 3 fonts), so all
     30 pages were read from page images; Fig. 5 was re-rendered at higher
     resolution to attribute the slope labels. Figure values (e.g. the
     scaled eigenvalue errors in Figs. 2 and 4) are read off the plots.
   * **Recorded as printed.** Eq. 4 has the wrong sign for $a > 0$ (eqs. 7
     and 11 are consistent with a minus); eq. 33 prints "$2\bar uj$"; eq. 81
     labels the quadratic $v_1$; eq. 82 has a stray comma; eq. 83 has
     $\int v_1^2\,dx$ where eq. 84 needs $v_2^2$; the text dates Fromm 1967,
     reference [12] 1968; eq. 92 is an empty numbered line. Not given: the
     consistency proof of eq. 57, the $K = 2$ scheme matrix, and the
     $K = 2$ eigenvector analysis (deferred).
   * **Reference list:** 18 entries. `cockburn-1999`, `reed-1973`,
     `vanleer-1977` and `vanleer-1979` were already in the bibliography
     (Reed & Hill is printed "Los Alamos National Laboratory", the entry
     has "Scientific"; same report LA-UR-73-479). Woodward's UCRL-90009
     report `woodward-1983` shares its title with the book chapter
     `woodward-1986` and is kept as a distinct work. `suzuki-2005` is a
     submitted extended abstract.
