---
type: Source
title: "Siegel et al. (2018) — Recovery schemes for primitive variables in general-relativistic magnetohydrodynamics"
description: "Stand-alone comparison of five conservative-to-primitive recovery schemes for ideal GRMHD with ideal-gas, Helmholtz and LS220 equations of state, showing that Newton–Raphson schemes with temperature as unknown need 1–2 orders of magnitude fewer EOS calls on tabulated EOSs, that the bracketed one-dimensional schemes are more robust, and recommending a 3D Newton–Raphson first pass with a one-dimensional fallback."
resource: "doi:10.3847/1538-4357/aabcc5"
source_kind: paper
authors: [Siegel D.M., Mösta P., Desai D., Wu S.]
year: 2018
venue: "Astrophys. J. 859:71"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2018-ApJ-Siegel-1038471538-4357aabcc5.pdf"
tags: [mhd, relativity, primitive-recovery, equation-of-state, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper is a systematic, application-independent comparison of
conservative-to-primitive ("recovery") schemes for ideal general-relativistic
MHD with a composition-dependent, finite-temperature EOS in
$(\rho, T, Y_e)$, $Y_e$ the electron fraction. Five schemes are compared: the
2D Noble et al. (2006) scheme extended to tabulated EOSs ("2D NR Noble"), a 2D
Newton–Raphson (NR) scheme in $(W, T)$, a 3D NR scheme in $(W, z, T)$ after
Cerdá-Durán et al. (2008), the bracketed one-dimensional Brent scheme of
Neilsen et al. (2014) and Palenzuela et al. (2015) ("1D Brent"), and the
one-dimensional pressure iteration of Newman & Hamlin (2014) ("1D Newman").
Each scheme is run on synthetic primitive sets (primitives to conserved, then
inverted) for an ideal gas, the partially tabulated Helmholtz EOS and the fully
tabulated LS220 EOS, and scored by iterations, EOS calls, accuracy and fraction
recovered. The schemes that take $T$ as an unknown need 1–2 orders of magnitude
fewer EOS calls on tabulated EOSs, because the others invert the EOS for $T$ at
every iteration; the one-dimensional schemes are more robust but costlier. The
open-source testbed "GRMHD con2prim" is released on Zenodo (§5). Merged into
[primitive-variable recovery](/methods/primitive-variable-recovery.md).

# Key claims

1. **Problem** (§2, eqs. 8–21). Valencia-type 3+1 conservation form with
   conserved vector $(D, S_i, \tau, \mathbf B, DY_e)$ and primitives
   $(\rho, \mathbf v, e, \mathbf B, Y_e)$; $D = \rho W$ (eq. 10); $\tau$
   excludes $D$ (eq. 13). An evolution equation for $Y_e$ (eq. 4) is added.
   Recovery runs at every evaluation of the fluxes and sources (§1–2); it
   changes no conserved variable, and it imposes no time-step constraint.
   Atmosphere and floor treatment, and the reset of conserved variables after
   a failure, are not discussed.
2. **Dimensionality** (§3). Recovery is in principle five-dimensional
   ($\rho$, $\mathbf v$, $e$; $\mathbf B$ and $Y_e$ are trivial). 5D schemes
   (HARM) were "later shown to be slow and inaccurate"; 1D and 2D reductions
   are more efficient and 2D schemes "less pathological" — asserted from the
   literature (Noble et al. 2006).
3. **2D NR Noble** (§3.1, eqs. 22–25). Unknowns $z \equiv \rho h_{\mathrm{rel}}W^2$
   and $\vert\mathbf v\vert^2$, with $h_{\mathrm{rel}} = 1 + e + p/\rho$ the
   relativistic specific enthalpy. For a three-parameter EOS each iteration
   inverts $h_{\mathrm{rel}} = z/(\rho W^2)$ for $T$ by a 1D NR with bisection
   fallback.
4. **2D NR** (§3.2, eqs. 26–28). Unknowns $(W, T)$, using
   $B^iS_i = \rho h_{\mathrm{rel}}W\alpha_{\mathrm L}b^0$ (eq. 26); no EOS
   inversion, because $T$ is an unknown.
5. **3D NR** (§3.3, eqs. 29–32). Unknowns $(W, z, T)$: eqs. 27–28 plus the
   constraint $e - e(\rho, T, Y_e) = 0$ (eq. 31), with $e(W, z, T)$ from eq. 32;
   no EOS inversion. The constraint idea is credited to Cerdá-Durán et al.
   (2008).
6. **1D Brent** (§3.4.1, eqs. 33–44). Brent's method on the master function
   $f(x) = x - \hat h_{\mathrm{rel}}\hat W$ in $x \equiv h_{\mathrm{rel}}W$
   (eqs. 33–34), bracketed by $1 + q - s < x < 2 + 2q - s$ (eq. 35) with
   $q = \tau/D$, $s = B^2/D$ (eqs. 36–39). Each iteration inverts $\hat e$ for
   $T$. The bracket "guarantees the existence of a root and convergence"
   (§4.2) — asserted from the bracket property, not proved here.
7. **1D Newman** (§3.4.2, eqs. 45–60). Iteration on $p$, initial guess $p = 0$
   (or the pressure at the table's minimum temperature); a cubic in
   $B^2 + z$ solved in closed trigonometric form (eqs. 49–56); then
   $\vert\mathbf v\vert^2$ (eq. 57), $\rho = D/W$, and an inversion of the
   enthalpy density for $T$. Aitken acceleration once three successive
   pressures exist.
8. **Cost mechanism** (§4.2, §5). 1D Brent, 2D NR Noble and 1D Newman each need
   one EOS inversion per iteration, "roughly 10–100 EOS calls by itself" (§5).
   Measured: LS220 EOS calls 836 / 758 / 331 against 13.0 / 11.3 for 2D / 3D NR
   (Table 1).
9. **Speed-up** (§5). 3D NR "can yield a speed-up by a factor of at least a few
   to 10, potentially up to a factor of 100" — inferred from EOS-call counts;
   no wall-clock timing is reported anywhere. "Up to ∼40% of the total
   simulation cost" for recovery in an evolution code is asserted without
   source or measurement.
10. **Accuracy** (§4.2, Fig. 2, Tables 1–2). NR schemes reach higher accuracy
    because "one or two additional iterations of the solver improve the
    accuracy by orders of magnitude"; 3D NR is the most accurate in Test A
    ($1.3\times10^{-13}$ LS220, $1.7\times10^{-14}$ Helmholtz). Measured.
11. **Robustness** (§4.2, §5). NR schemes need good initial guesses (the
    previous time step) and thermodynamic derivatives, which for tables are
    numerical and "may be thermodynamically inconsistent (i.e., the Maxwell
    relations may not be satisfied to machine precision)". The inner EOS
    inversion of the 1D schemes reintroduces both implicitly. Only 1D Newman is
    "entirely independent of the previous time step". Enthalpy inversions
    (1D Newman, 2D NR Noble) are less robust than $e$ inversions (1D Brent).
12. **Recommendation** (abstract, §5). Analytic EOS: 1D Brent or 1D Newman,
    Newman preferred for accuracy. Three-parameter EOS: 3D NR first, falling
    back to 1D Brent or 1D Newman for failed points. Asserted; the combined
    strategy is not tested.
13. **Order** (§1). With a finite-volume code the recovery methods "are
    second-order accurate; additional complexity would arise for higher-order
    finite-volume schemes" — asserted, no argument given.

**Tests** (§4; stand-alone forward–inverse tests, no evolution, no wall-clock
timing, no convergence-order test). Common set-up (§4.1): ideal gas with
$\gamma = 4/3$, Helmholtz EOS with the Siegel & Metzger (2017) modifications,
LS220; $W$ varied with random velocity direction and $\mathbf B$ parallel to
$\mathbf v$; initial guesses perturbed by 5% ("essentially unchanged" with 10%,
not shown); failed 2D/3D NR retried from the Cerdá-Durán et al. (2008) safe
guess; convergence tolerance $5\times10^{-9}$; success if the mean relative
deviation (eq. 61) is below $5\times10^{-8}$; iteration cap not stated.
*Test A*, density–temperature plane ($W = 2$, magnetic-to-gas pressure ratio
$10^{-3}$, $Y_e = 0.1$; Figs. 1–2, Table 1): all schemes recover the
ideal-gas plane in about 5 iterations; with LS220, 2D NR Noble and 1D Newman
fail at very high density and low temperature ("less than 1.5% of the total
points") because the first step drives the enthalpy off the table. Mean
iterations (2D NR / 3D NR / 1D Brent / 2D NR Noble / Newman): ideal gas
5.5 / 5.4 / 4.8 / 4.5 / 4.9; LS220 11.5 / 9.1 / 6.9 / 6.1 / 6.1; Helmholtz
25.0 / 16.2 / 5.7 / 6.3 / 5.9. EOS calls: ideal gas 6.5 / 7.4 / 6.8 / 6.5 / 5.9;
LS220 13.0 / 11.3 / 836 / 758 / 331; Helmholtz 28.2 / 18.2 / 111 / 83.4 / 57.0.
*Test B*, Lorentz factor–magnetization plane ($\rho = 10^{11}$ g cm$^{-3}$,
$T = 5$ MeV, $Y_e = 0.1$; Fig. 3, Table 2): all schemes fail at very strong
magnetization or high $W$; 2D and 3D NR fail beyond $W \approx 10$ for the
ideal gas, 3D NR reaches $W \simeq 100$ (LS220) and $10^2$–$10^3$
(Helmholtz). Percent recovered (same order): ideal gas
56.0 / 58.7 / 74.9 / 75.7 / 79.1; LS220 52.6 / 69.1 / 68.0 / 60.0 / 77.1;
Helmholtz 56.9 / 77.3 / 75.6 / 65.0 / 77.4 — 1D Newman highest for every EOS.
The plane deliberately extends to unphysical magnetizations, so these are not
production failure rates.

# Notation map

| Siegel et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf q = [D, S_i, \tau, B^i, DY_e]$ | $u$ | conserved state; $D$, $S_i$, $\tau$ as in the registry ($\tau$ excludes $D$) |
| $\mathbf p = [\rho, v^i, \epsilon, B^i, Y_e]$ | none (words) | primitive vector; **collision:** bold $\mathbf p$ against pressure $p$ |
| $\mathbf f^{(i)}$, $\mathbf s$ | $\mathbf f$, $s(u)$ | |
| $\alpha$, $\beta^i$, $\gamma_{ij}$ | $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | |
| $\gamma$ (determinant of $\gamma_{ij}$) | none (words) | **collision** with the adiabatic index $\gamma$ |
| $\Gamma$ | $\gamma$ | ideal-gas index of the tests ($4/3$) |
| $\epsilon$ | $e$ | specific internal energy |
| $e \equiv \tau + D$ (Newman scheme) | none (words) | **collision** with registry $e$ |
| $h = 1 + \epsilon + p/\rho$ | none; written $h_{\mathrm{rel}}$ on this page | relativistic specific enthalpy; **collision** with cell size $h$ |
| $w = \rho h$ | none (words) | enthalpy density |
| $W$, $v^i$ | $W$, $\mathbf v$ | |
| $B^i$ | $\mathbf B$ | Eulerian field with $(4\pi)^{-1/2}$ absorbed (Heaviside–Lorentz-like) |
| $b^\mu$, $b^0$, $b^2$ | none (words) | comoving field four-vector |
| $p_{\mathrm{mag}} = b^2/2$ | none (words) | magnetic pressure |
| $P$ (eq. 51) | $p$ | |
| $Y_e$ | none (words) | electron fraction |
| $z \equiv \rho hW^2$; $x = hW$, $q$, $r$, $s$, $t$ | local | scheme-local; $s$, $t$ collide with $s(u)$ and time |
| $\varepsilon$, $a$, $d$, $\phi$, $\mathcal M^2$, $\mathcal T$ | local | Newman cubic; $a$ collides with the scale factor, $d$ with the dimension count |
| $\mathrm{tol}_{\mathrm{conv}}$, $\mathrm{tol}_{\mathrm{recov}}$ | none (words) | |

# Pages created or updated

* Created [Primitive-variable recovery](/methods/primitive-variable-recovery.md).
* Also cited on [Athena++ (block-based AMR framework for astrophysical MHD)](/software/athena-plus-plus.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2018-ApJ-Siegel-1038471538-4357aabcc5.pdf`.
   * **Version.** arXiv:1712.07538v2 [astro-ph.HE], 24 Jun 2018 ("Draft
     version June 26, 2018", AASTeX61, 13 pages): the author preprint, not the
     typeset ApJ article; page numbers are preprint pages. Code: "GRMHD
     con2prim", doi:10.5281/zenodo.1213306, development version at
     bitbucket.org/dsiegel/grmhd_con2prim (§5); a stand-alone testbed, not
     tied to a host evolution code.
   * **Identity.** doi:10.3847/1538-4357/aabcc5, checked on Crossref: "Recovery
     Schemes for Primitive Variables in General-relativistic
     Magnetohydrodynamics", Astrophys. J. 859(1):71, published 2018-05-20;
     four authors as on page 1.
   * **How it was read.** Text extraction, all sections; pp. 3–6 and 10
     checked on rendered pages (eqs. 2–60, Table 1, the §4.2 robustness text).
     Parameter-plane ranges were read from figure axes; grid resolution of the
     planes, the iteration cap and the inner-inversion tolerances are not
     stated.
   * **Recorded as printed.** Eq. 53 reads $d \le \frac{4}{27}4a^3$ where
     eq. 54 implies $d \le \frac{4}{27}a^3$; eq. 56's first term lacks the
     factor $a$; eq. 58 reads $W^2 = 1/\sqrt{1-v^2}$, against eq. 16; eq. 48
     divides $(B^iv_i)^2$ and $B^iS_i$ by $\sqrt\gamma$ (dimensionally odd); eq.
     61 has no absolute values. None verified against Newman & Hamlin (2014).
     §4.2 reads "definite failure for the 2D NR scheme above Lorentz factors of
     $W \lesssim 10$" (direction ambiguous). §4.2 says 2D and 3D NR recover most
     of the Helmholtz plane in "less than 10 iterations", while Table 1 gives
     means 25.0 and 16.2.
   * **Reference list:** 28 entries. The source owns the key `siegel-2018`;
     Siegel & Metzger (2018, ApJ 858:52) is keyed `siegel-2018-b` and the
     Zenodo code release (Siegel & Mösta 2018, the only printed DOI)
     `siegel-2018-c`. `newman-2014` is printed without a first page ("SIAM J.
     Sci. Comput., 36"). Duez et al. (2005) carries its printed arXiv
     identifier astro-ph/0503420 as a note.
