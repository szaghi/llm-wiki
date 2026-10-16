---
type: Source
title: "Panici, Conlin, Dudt, Unalmis & Kolemen (2023) — The DESC stellarator code suite. Part 1. Quick and accurate equilibria computations"
description: "Verification paper comparing a Fourier–Zernike pseudospectral equilibrium code (DESC) with a Fourier/radial-finite-difference code (VMEC), read here for its Zernike basis on the unit disc (radial polynomials, regularity at the origin, indexing schemes), its Fourier–Zernike product basis and its measured exponential versus first-order radial convergence."
resource: "doi:10.1017/S0022377823000272"
source_kind: paper
authors: [Panici D., Conlin R., Dudt D.W., Unalmis K., Kolemen E.]
year: 2023
venue: "J. Plasma Phys. 89:955890303"
local_file: "/home/stefano/papers/mosaic/orthogonal-polynomials-and-quadrature/2023_Crossref_Journal_of_Plasma_Physics_Panici_The_DESC_stellarator_code_suite_Part_1_Quick_and_accurate_eq.pdf"
tags: [paper, zernike, spectral-basis, axis-regularity, spectral-convergence]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper compares two codes that compute three-dimensional ideal-MHD
equilibria of stellarators. VMEC represents the solution by Fourier series in
the two angles on discrete radial surfaces, with first-order finite
differences in radius. DESC represents it in a global Fourier–Zernike basis
(Zernike functions on the poloidal cross-section, a Fourier series in the
toroidal angle) and solves the force-balance residual at collocation nodes.
On a common normalized force-error metric, DESC converges exponentially in
its radial resolution where VMEC converges at first order, keeps the
regularity of the solution at the magnetic axis (the centre of the disc)
where VMEC's Fourier coefficients violate it, and reaches about one order of
magnitude lower error at equal run time on a W7-X case.

**Read for this bundle's subject.** The whole paper was read (32 pages,
§§1–6 and Apps. A–C, plus the reference list). This bundle takes from it only
the basis and convergence material: the Zernike radial polynomials and real
Zernike functions (§3.2, eqs. 3.18–3.19), the regularity condition at the
origin of the disc (eq. 3.21, §5.1 and Fig. 4), the Fourier–Zernike product
expansion and its truncation and indexing (eqs. 3.17, 3.20, Table 2,
App. C), the collocation use (§3.2, §5.3.2) and the expected and measured
convergence (§5.2, Table 1, Figs. 7–8, App. C). The equilibrium physics
(flux coordinates, force decomposition, the energy-descent scheme, Mercier
stability, the VMEC derivation of App. A, run-time comparisons) is outside
this bundle's scope and is not extracted.

**Grids and quadrature are not described.** The paper says only that the
residuals are evaluated "on a collocation grid" (p. 8) and that the error
has minima on the collocation surfaces (p. 15, p. 30). It names no node set
(no Gauss–Jacobi or concentric grid) and no quadrature rule; its volume and
surface averages (eqs. 4.1–4.3) are written as integrals without saying how
they are evaluated. No quadrature page of this bundle cites it.

# Key claims

1. **Zernike basis** (§3.2, eqs. 3.18–3.19, p. 7): definition of the radial
   polynomials, called "the shifted Jacobi polynomial", and of the real
   Zernike functions with $\cos$ for $m\ge0$ and $\sin$ for $m<0$. The
   printed eq. 3.19 has a sign slip (see Citations).
2. **Regularity at the origin** (eq. 3.21, p. 7, after Lewis & Bellan 1990):
   the $m$-th Fourier coefficient of an analytic function on the disc is
   $r^{\lvert m\rvert}$ times an even power series; a Zernike expansion
   satisfies it by construction. The paper says this makes the basis
   automatically satisfy "the necessary constraints at the axis for analytic
   functions" (§2, p. 3).
3. **Regularity diagnostic** (§5.1, Fig. 4, pp. 11–12): Fourier coefficients
   divided by $r^{\lvert m\rvert}$ stay flat for the Fourier–Zernike solution
   and diverge toward $r=0$ for the finite-difference solution, "evidence of
   possibly unphysical modes".
4. **Fourier–Zernike expansion** (eqs. 3.17, 3.20, pp. 6–7) with
   resolutions $L$, $M$ and a toroidal resolution, and two Zernike indexing
   schemes, ANSI and Fringe, which set the radial resolution for given $L$
   and $M$ (Table 2, p. 17); radial and poloidal modes are coupled, so
   raising $M$ raises the radial resolution (App. C, p. 30).
5. **Expected convergence** (§5.2, p. 12; Table 1, p. 14): exponential in the
   angular resolution for both representations, "assuming a smooth solution"
   and citing Boyd (2001); radially exponential for the Fourier–Zernike basis,
   algebraic $O(N_\text{radial}^{-1})$ for first-order finite differences.
6. **Measured convergence** (Figs. 7–8, p. 14), axisymmetric D-shaped case,
   $M=16$: Fourier–Zernike error fit $\exp(-0.61L-0.01)$ for
   $L=16,\dots,24$; finite-difference error fit
   $\log(\text{error})=-1.02\log(N)+3.27$ in the number $N$ of radial grid
   points.
7. **Saturation** (App. C, p. 30, Fig. 22): on the W7-X case the
   Fourier–Zernike error stops decreasing uniformly around $L=M=N=16$ (the
   paper's $N$ is the toroidal resolution here).

# Notation map

| Panici et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$ (radial label, $\sqrt{\psi/\psi_a}$) | $r$ | radial coordinate of the unit disc |
| $\theta$ (poloidal angle) | $\phi$ | azimuthal angle of the disc; registry $\theta$ is the polar angle on the sphere |
| $\zeta$, with $N_{FP}\zeta$ in $\mathcal F^n$ | $\zeta$ | the field-period factor is stated in words |
| $l$ (radial degree) | $n$ | **collision:** registry $\ell$ is a spherical-harmonic degree |
| $m$ (poloidal index, signed) | $m$ | same |
| $n$ (toroidal index, signed) | $k$ | **collision:** registry $n$ is a polynomial degree |
| $L$, $M$, $N$ (resolutions) | $L$, $M$, $K$ | **collision:** registry $N$ counts strips of an equally spaced rule; in Figs. 7–8 the paper's $N$ is the number of radial grid points, written in words |
| $\mathcal Z_l^m$ (eq. 3.17), printed $\mathcal Z_m^l$ in eq. 3.18 | $Z_n^m$ | index placement differs between the two equations |
| $\mathcal R_l^{\lvert m\rvert}$ | $R_n^{\lvert m\rvert}$ | |
| $s$ (summation index of eq. 3.19) | $j$ | the paper's $s$ is also the VMEC radial label |
| $\mathcal F^n(\zeta)$ | $\mathcal F_k(\zeta)$ | |
| $R_{lmn}$, $Z_{lmn}$, $\lambda_{lmn}$ | $c_{nmk}$ | one coefficient set per expanded function |
| $a_m(\rho)$, $a_{m,i}$ | $f_m(r)$, $b_{m,i}$ | |
| $R$, $Z$ (cylindrical coordinates of the surfaces) | words | **collision** with $R_n^m$, $Z_n^m$ |

# Pages created or updated

* Created [Zernike polynomials and the Fourier–Zernike basis](/definitions/zernike-polynomials.md).
* Updated [Orthogonal polynomials with respect to a weight function](/definitions/orthogonal-polynomials.md): pointer to the Zernike polynomials, and the first stated convergence rate of an orthogonal expansion.
* Updated [Notation registry](/notation.md): section 8 (functions on the unit disc and Fourier–Zernike bases); the note on $P_n^{(\alpha,\beta)}$.

# Citations

1. `~/papers/mosaic/orthogonal-polynomials-and-quadrature/2023_Crossref_Journal_of_Plasma_Physics_Panici_The_DESC_stellarator_code_suite_Part_1_Quick_and_accurate_eq.pdf`.
   * **Identity.** Page 1: D. Panici, R. Conlin, D.W. Dudt, K. Unalmis and
     E. Kolemen (Princeton University), *J. Plasma Phys.* (2023), vol. 89,
     955890303, doi:10.1017/S0022377823000272, Open Access CC-BY 4.0;
     received 31 October 2022, revised 16 March 2023, accepted 17 March
     2023. Crossref agrees: title, five authors in this order, vol. 89,
     issue 3, article 955890303, 53 references.
   * **How it was read.** Text layer extracted in full. Pages 7 (eqs.
     3.18–3.19), 12 (Fig. 4) and 14 (Table 1, Figs. 7–8) were also read
     visually to check the formulae and the figure values.
   * **Recorded as printed.**
     * Eq. 3.19, p. 7: the last denominator factorial is printed
       $\big[(l-\lvert m\rvert)/2+s\big]!$. The standard radial Zernike
       polynomial has $-s$; with $+s$ the sum gives $2\rho^2-\tfrac12$
       for $l=2$, $m=0$ instead of $2\rho^2-1$ (compiler check).
     * Eq. 3.17 writes $\mathcal Z_l^m$, eq. 3.18 writes $\mathcal Z_m^l$.
     * Eqs. 3.17 sum $l=0,\dots,L$ for every $m$, although $\mathcal R_l^{\lvert m\rvert}$
       is defined only for $l\ge\lvert m\rvert$, $l-\lvert m\rvert$ even.
     * Figs. 7–8 use $N$ for the radial resolution, which elsewhere is the
       toroidal resolution.
     * The quasi-helical case is described with three different resolution
       sets (text p. 18 and Fig. 15: $M=12$, $N=10$; Fig. 13: $L=M=12$,
       $N=12$; Fig. 14: DESC $L=M=12$, $N=10$).
   * **Reference list.** 53 entries, merged complete into the
     [bibliography](/bibliography.md). DOIs: those printed (Dudt et al.
     2023, Panici 2022) and four verified on Crossref (Genberg et al. 2002,
     Lewis & Bellan 1990, Sakai & Redekopp 2009, Zernike & Stratton 1934).
     Printed anomalies kept as notes: "Conlin, W." for R. Conlin in Dudt et
     al. 2022; Conlin et al. 2023 as "Submitted"; "72505" for Glasser 2016;
     "John, H.S." for H. St. John in Lao et al. 1985; the truncated author
     list of Virtanen et al. 2020; JAX "version 0.3.13" dated 2018.
