---
type: Source
title: "Coleman (2020) — An extension of the Athena++ framework for general equations of state"
description: "Extends non-relativistic Athena++ (M)HD to any equation of state supplying pressure, internal energy and sound speed, adds a log-space bilinear tabular-EOS utility and a PVRS wave-speed estimate for HLLC, and publishes a verification suite with exact solutions for an ionizing-hydrogen and a Helmholtz EOS, on which HLLE fails to converge for asymmetric double shocks."
resource: "doi:10.3847/1538-4365/ab82ff"
source_kind: paper
authors: [Coleman M.S.B.]
year: 2020
venue: "Astrophys. J. Suppl. 248:7"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2020-ApJS-Coleman-1038471538-4365ab82ff.pdf"
tags: [software, hydro, mhd, equation-of-state, riemann-solver, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper makes non-relativistic (M)HD in
[Athena++](/software/athena-plus-plus.md) work with an arbitrary equation of
state. The EOS must satisfy $(\partial p/\partial\rho)_e > 0$ and
$(\partial p/\partial e)_\rho > 0$ and supply three functions: pressure from
density and internal energy density, internal energy density from density and
pressure, and $c_s^2$ from density and pressure. Every occurrence of $\gamma$
in the code was replaced by one of them. A tabular-EOS utility interpolates
log-space tables bilinearly; with an ideal gas a 2×2 table reproduces the ideal
EOS to machine precision. For HLLC the Roe-average wave-speed estimate, which
needs a fourth EOS function, is replaced by a generalized PVRS estimate (Toro
1999); HLLD keeps the Miyoshi & Kusano (2005) estimate. The paper contributes a
verification suite with exact solutions: six hydrodynamic Riemann problems and
one all-discontinuity MHD Riemann problem with a Saha-ionization hydrogen EOS,
HD and MHD linear waves, and two Riemann problems with the Helmholtz EOS.
Riemann tests converge near first order and linear waves near second order,
except the asymmetric double-shock tests, where convergence stalls; HLLE fails
to converge there with every wave-speed estimator tried. Merged into
[general equations of state](/methods/general-equation-of-state.md),
[Athena++](/software/athena-plus-plus.md) and
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Key claims

1. **Admissibility** (§2, eqs. 4–5). $(\partial p/\partial\rho)_e > 0$ and
   $(\partial p/\partial e)_\rho > 0$ in the fluid rest frame, "sufficient, but
   not necessary" for a unique Riemann solution, citing Chen et al. (2019);
   asserted, not proved here. Sound speed $c_s^2 \equiv (\partial p/\partial\rho)_s$
   (eq. 8).
2. **Three-function interface** (§3.1, eqs. 13–15). $p(\rho, \rho e)$,
   $\rho e(\rho, p)$ and $c_s^2(\rho, p)$, with
   $E = \rho e + \tfrac12\rho\vert\mathbf v\vert^2 + \tfrac12 B^2$. Athena++ evolves
   $E$ and keeps the thermal $p$ as primitive, so the internal energy is
   obtained by subtracting the kinetic and magnetic parts before calling the
   pressure function; $c_s^2$ feeds the CFL condition and the Riemann solvers.
   "Any EOS which is able to provide these functions and obey Eqns. 4 and 5 can
   work in this framework, even a piecewise EOS."
3. **Recipe** (§3.1, eqs. 16–18). $p = (\gamma-1)\rho e$, $\rho e = p/(\gamma-1)$
   and $c_s^2 = \gamma p/\rho$ map to the three general functions; that this
   preserves all characteristic speeds is deferred to Chen et al. (2019),
   App. B. "With one caveat (see Appendix A)" — the Roe-average estimate —
   "we found all instances of $\gamma$ and replaced them". Characteristic
   reconstruction does not support a general EOS (footnote 3); every run uses
   PLM on primitives with VL2.
4. **Tabular EOS** (§3.2, eqs. 19–28). Tables of $\log(p/\rho e)$,
   $\log(\rho e/p)$ and $\log\Gamma_1$, with $\Gamma_1 \equiv (\partial\ln p/\partial\ln\rho)_s = \rho c_s^2/p$
   (eq. 22), on a grid regular in $\log\rho$ and in the logarithm of the
   energy or pressure times $\rho^{\eta}$ ($\eta$ a user constant). Bilinear
   interpolation "guarantees the preservation of monotonicity"; off-table
   requests are extrapolated linearly, with the advice to build large tables
   and set floors. For an ideal gas the three quantities are constants, so a
   table with at least 2×2 points reproduces the ideal EOS "exactly (to
   machine precision)" — stated as verified, no data shown.
5. **Analytic EOSs through a temperature root-find** (§4 fn. 6, §4.4 fn. 8).
   Hydrogen EOS: every call root-finds $T$ by Brent–Dekker to "one part in
   $10^{12}$", preferred to a table so that table resolution does not
   contaminate convergence. Helmholtz EOS: the author's own implementation in
   $(\rho, T)$ after Timmes & Swesty (2000), $T$ by bisection, secant and
   Newton–Raphson seeded with the last temperature.
6. **HLLC wave speeds** (§3.3, App. A). The previous Roe-average estimate
   needs a fourth EOS function, $c_s^2$ of the Roe-averaged density and
   enthalpy (eqs. A1–A7); the Hu et al. (2009) variant also needs four and
   gave worse errors than PVRS on tests 3 and 4. The generalized PVRS estimate
   (eqs. A8–A17), now the HLLC default, needs only the three functions: a
   star-state pressure and velocity from arithmetic means, star densities, a
   star-state $\Gamma_1$, and a shock factor that multiplies $c_s$ on each side
   when the star pressure exceeds that side's pressure. Measured, not proved:
   "significant reduction of errors and improved convergence in tests 3 and 4
   … without negatively affecting the accuracy of solutions using an ideal gas
   EOS".
7. **HLLD** (§3.3, §5.2). Keeps the Miyoshi & Kusano (2005, eq. 12) estimate;
   PVRS "is not readily extendable to MHD".
8. **HLLE** (§5.1.4, §6). No estimator changed tests 1, 2, 5, 6, where HLLE
   errors were "a few tens of per cent worse than HLLC". On tests 3 and 4 HLLE
   "did not converge to the correct solution for any of the wavespeed
   estimators we tried"; with the Roe estimator it does converge on the
   ideal-gas analogues (fn. 10). "We were unable to find a modification to
   HLLE that enabled it to properly converge to the solutions of tests 3 and
   4" (§6). The abstract and §6 name only HLLC and HLLD as extended.
9. **Scope** (§1, §4.4). Non-relativistic only; EOS functions take no passive
   scalars; Helmholtz tests kept where the sound speed is non-relativistic and
   degeneracy pressure does not dominate.
10. **Priority** (§1, asserted). Athena++ is "the first publicly-available
    open-source MHD code whose general EOS capabilities have been explicitly
    verified with a suite of (M)HD tests utilizing a non-trivial EOS"; FLASH
    has published no such test; Castro ran similar tests (Zingale & Katz 2015)
    but is hydro-only.
11. **Finite-volume limitation** (§5.1.2, §6). In tests 3 and 4, cells
    straddling the shocks pass a cell-averaged $(\rho, p)$ to the EOS, giving a
    $\Gamma_1$ below its value on either side because $\Gamma_1$ is
    non-monotonic there; the under-prediction is "roughly the same for N = 64
    and N = 2048". Offered as the likely cause of the stalled convergence —
    an interpretation, not demonstrated.
12. **Coupling.** The EOS is not a split module: it is called in every
    conserved–primitive conversion and every Riemann solve; the time step is
    the usual CFL condition with the general $c_s$. Conservation is not
    discussed explicitly.

**Tests** (§4–5; PLM on primitives, VL2, $\nu = 0.4$, $N = 64$ to 2048 cells;
per-cell $L_1$ and $L_2$ errors against exact solutions, eqs. 29–31; the paper
states orders only as "close to linear" or "near quadratic"). Hydrogen EOS
(version 19.0 of Athena++): a sound wave returns to its position after one
crossing (§4.1, qualitative); tests 1–2, Sod-like Riemann problems (Tables 2,
5–7, Figs. 2–3), $L_1(\rho)$ from 1.16821e-09 to 5.48822e-11 (test 1), with a
velocity overshoot at the rarefaction tail persisting at $N = 2048$; tests 3–4,
asymmetric shock–shock (Figs. 4–5, Tables 8–9), errors "nearly constant for
$512\le N\le2048$" ($L_1(\rho)$ 3.64848e-08 at 512, 3.0004e-08 at 2048 for test
3), ringing at the shocks; tests 5–6, rarefaction–rarefaction (Figs. 6–7),
near linear, with the usual central density spike; test 7, MHD Riemann problem
with the Ryu & Jones (1995) 2a states and the hydrogen EOS, exact solution from
49 jump conditions (eqs. 32–38), near linear with HLLD (Tables 12–13,
Figs. 8–9); tests 1–6 rerun as MHD with $\mathbf B = 0$ and HLLD match HLLC
except on tests 3–4 (errors up to 3× larger, reproduced by HLLC with the HLLD
estimator). Tests 8–9, HD sound and MHD fast linear waves (Tables 14–15,
Fig. 10): near quadratic, $L_1(\rho)$ from 6.36583e-16 to 5.30243e-19 (test 8).
Helmholtz EOS, tests 10–11 (Table 4, Figs. 11–12, Tables 16–18): Sod-like
converges well ($L_1(\rho)$ 0.00842 to 0.000282591); asymmetric shock–shock
better than hydrogen tests 3–4. Serna & Marquina (2014) van der Waals tests:
"comparable results" by visual comparison. The notes' own slope fit of
$L_1(\rho)$ from 64 to 2048 cells (not printed in the paper) gives 0.41 and
0.27 for tests 3 and 4, about 0.8–0.95 for the other Riemann tests, and about
2.0 for the linear waves.

# Notation map

| Coleman (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $p$, $E$, $\mathbf B$ | $\rho$, $\mathbf v$, $p$, $E$, $\mathbf B$ | $E = e + \rho v^2/2 + B^2/2$: Heaviside–Lorentz-like field units |
| $e$ (main text) | $\rho e$ | **collision:** the paper's $e$ is internal energy density |
| $\epsilon$ (App. B) | $e$ | specific internal energy |
| $a$, $a^2$ | $c_s$, $c_s^2$ | **collision** with the scale factor $a$ |
| $\Gamma_1 = (\partial\ln p/\partial\ln\rho)_s$ | none; written $\Gamma_1$ on this page | generalized adiabatic index; equals $\gamma$ for an ideal gas |
| $\gamma$ | $\gamma$ | ideal gas only |
| $\lambda_{\min}$, $\lambda_{\max}$ | none (words) | HLL-type signal-speed bounds |
| $p_*$, $v_{x*}$, $\rho_{*K}$, $\Gamma_{*K}$ | none (words) | star-region states |
| $\mathbf U$ | $u$ | |
| $\tilde\rho$, $\tilde h$, $\tilde a$ | none (words) | Roe averages; in App. B the tilde means dimensionless |
| $\eta$ | none (words) | tabulation exponent; distinct from $\eta_1$, $\eta_2$ |
| $x$ | none (words) | ionization fraction; **collision** with position |
| $N$ | number of cells | not $N_{\mathrm b}$ |
| $\Delta x$, $\Delta t$ | none (words) | **collision:** domain length and total run time, not $h$ and the time step |
| CFL number | $\nu$ | 0.4 throughout |

# Pages created or updated

* Created [General equations of state in Godunov codes](/methods/general-equation-of-state.md).
* Updated [Athena++](/software/athena-plus-plus.md) (HLLE's general-EOS
  failure on double shocks recorded as a qualification of
  [Stone et al. (2020)](/sources/stone-2020.md), not a contradiction) and
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* Also cited on [CASTRO (compressible astrophysics code on BoxLib AMR)](/software/castro.md).
* Also cited on (batch 4) [Density and pressure floors](/methods/numerical-floors.md), [FLASH](/software/flash.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2020-ApJS-Coleman-1038471538-4365ab82ff.pdf`.
   * **Version.** arXiv:1909.05274v3 [astro-ph.IM], 8 Apr 2020 ("Draft
     version April 10, 2020", AASTeX61, 32 pages): the accepted-manuscript
     preprint, not the typeset article. Code: Athena++ public version,
     https://github.com/PrincetonUniversity/athena-public-version
     (footnote 1); hydrogen tests 1–7 use version 19.0 (§4.1); the version for
     the linear-wave and Helmholtz tests is not given.
   * **Identity.** doi:10.3847/1538-4365/ab82ff, checked on Crossref: title and
     single author match; Astrophys. J. Suppl. 248(1):7, online 2020-04-27,
     print 2020-05-01.
   * **How it was read.** Text extraction, all sections; eqs. B31–B38 checked
     on rendered pages (eq. B36, the closed-form $\Gamma_1$ of the hydrogen
     EOS, read visually on p. 24 and not reproduced). The observed orders
     quoted under Tests were fitted by the reader from the error tables. The machine-readable rarefaction profiles of App. C were not
     available in the PDF.
   * **Recorded as printed.** Eq. 3 prints the energy flux without the factor
     $v_x$. Eq. A11 prints $p_{x,R}$, $p_{x,L}$ where $p_R$, $p_L$ are meant.
     §3.1 says the pressure and internal-energy functions convert "primitives
     to conservatives and the inverse, respectively", the order swapped. §4.4
     and §5.4 call the Helmholtz tests "tests 8 and 9", while Table 4,
     Figs. 11–12 and Tables 16–18 number them 10 and 11 (the tables are taken
     as authoritative). Table 15 is captioned "HD Linear Wave" for the MHD
     test. §4.3 has an empty citation ("see e.g. Appendix B of )").
   * **Reference list:** 35 entries, titles only for Toro (1999); printed DOIs
     for Serna & Marquina (2014) and Masci et al. (2018). "Stone, Tomida, White
     & Felker 2019, submitted" is merged with
     [stone-2020](/sources/stone-2020.md); the undated "in prep." self-citation
     is `coleman-2020-b` (citing-year rule); Stone & Norman (1992a, b) map to
     `stone-1992-c` and `stone-1992-d`. The Miyoshi & Kusano (2005) venue,
     J. Comput. Phys. 208:315, is taken from this list. Banks et al. (2008)
     prints pages "69857002", recorded as 227:6985; Masci et al. is printed
     2018 with volume 131; neither verified.
