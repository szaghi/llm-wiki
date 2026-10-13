---
type: Source
title: "Zachary, Malagoli & Colella (1994) — A higher-order Godunov method for multidimensional ideal magnetohydrodynamics"
description: "Strang-split higher-order Godunov MHD scheme on a nonconservative (Brackbill–Barnes) momentum form with an Engquist–Osher-type flux; divergence held only to truncation error, with an optional collocated central-difference projection that made no noticeable difference in its 2D tests."
resource: "doi:10.1137/0915019"
source_kind: paper
authors: [Zachary A.L., Malagoli A., Colella P.]
year: 1994
venue: "SIAM J. Sci. Comput. 15:263-284"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1994-SISC-Zachary-1011370915019.pdf"
tags: [godunov, operator-splitting, nonconservative-momentum, projection, riemann-solver, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper extends the 1D higher-order Godunov MHD scheme of Zachary &
Colella (1992) to 2D and 3D by Strang operator splitting (eq. 6). The MHD
equations are rewritten in a nonconservative form (eq. 1) whose right-hand
side differs from conservation form by terms $\propto \nabla\cdot\mathbf B$.
Each 1D sweep then holds $B_x$ constant, and the residual
$\partial B_x/\partial x$ terms are treated as source terms (§§2.1–2.2).

The predictor traces characteristics in primitive variables with a hybrid
MUSCL/characteristic limiter (eqs. 7–12). The corrector is a generalized
Engquist–Osher flux written as a sum over sonic points (eqs. 24–28), with
three repairs: an Einfeldt-type flux for strong rarefactions (eqs. 29–30),
interpolation in specific volume instead of density, and degeneracy
detection with Rusanov dissipation for transonic degenerate pairs
(eqs. 31–33).

**$\nabla\cdot\mathbf B$ is held only to truncation error.** A collocated
Hodge projection with second-order central gradient and divergence
(eq. 34) is available after each step. The authors report that it made
"no noticeable difference" in their 2D tests (§2.4). Tests: Sod, Brio–Wu,
a strong Brio–Wu variant, Einfeldt's 1-2-0-3 problem, a magnetized blast
and a compressible [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md),
all at CFL 0.8 without artificial viscosity. No divergence value is
reported anywhere.

# Key claims

1. **Nonconservative system** (§2.1, eq. 1, p. 265). The momentum equation
   is printed as
   $$\frac{\partial\rho u_x}{\partial t}+\frac{\partial}{\partial x}\Big(\rho u_x^2+p+\frac{B_{\perp,x}^2}{8\pi}\Big)+\nabla\cdot(\mathbf u_{\perp,x}u_x\rho)-\frac{1}{4\pi}(\mathbf B_{\perp,x}\cdot\nabla)B_x=0$$
   (1b, cyclic forms 1c–1d), with $\mathbf B_{\perp,x_i}=\mathbf B-B_{x_i}\hat{\mathbf e}_i$.
   Induction is **conservative**,
   $\partial_t\mathbf B+\nabla\cdot(\mathbf{uB}-\mathbf{Bu})=0$ (1e).
   "The right-hand side of these equations differs from the conservation
   form of the equations by terms of the form $\nabla\cdot\mathbf B(\ldots)$."
   The stated motive is splitting: to minimize the extent to which discrete
   terms in different sweep directions "would have to sum to zero due to
   the divergence-free constraint", by analogy with advective differencing
   in incompressible flow; the form also "reduces the effect of magnetic
   monopole forces" (citing Brackbill & Barnes).
   *Compiler check (symbolic):* (1b) equals the conservative $x$-momentum
   equation plus $(B_x/4\pi)\,\nabla\cdot\mathbf B$ on the left-hand side,
   the Brackbill–Barnes form. For the energy equation see **Recorded as
   printed**.
2. **1D split system** (§2.1, eqs. 2–4). $\partial B_x/\partial t = 0$
   (2e); transverse induction $\partial_t B_y+\partial_x(u_xB_y-u_yB_x)=0$
   (2f–2g); energy without $B_x^2$ (2h). "We have not completely eliminated
   terms of the form $\partial B_x/\partial x$; they appear in the $B_y$,
   $B_z$, and $\rho E$ evolution equations. However, since
   $\partial B_x/\partial t=0$, we can formally treat them as source
   terms." The nonconservative product uses the face-averaged state (eq. 4).
3. **Strang splitting** (eq. 6):
   $\mathbf U^{n+1}=\mathcal L_x\mathcal L_y\mathcal L_z\mathcal L_z\mathcal L_y\mathcal L_x\mathbf U^n$,
   second order in time if each 1D operator is.
4. **Predictor** (§2.2, eqs. 7–15). Limiter
   $\bar\alpha_k=\min(\gamma|\alpha_k^-|,\gamma|\alpha_k^+|,|\alpha_k^c|,|\alpha_k^m|)\,\mathrm{sign}(\alpha_k^c)$
   if $\alpha_k^-\alpha_k^+>0$, else 0 (eq. 10), with the factor $\gamma = 2$
   for genuinely nonlinear fields and 1 where the structure coefficient
   changes sign (eq. 11). The plain MUSCL gradient gave "moderate amplitude
   (5–10%) fluctuations" that flattening did not cure (p. 267). In
   primitive variables the $\partial B_x/\partial x$ sources reduce to
   $u_y\,\partial_xB_x$ and $u_z\,\partial_xB_x$ in the transverse-field
   equations: "In the W-representation, $\partial B_x/\partial x$ changes
   only the $\mathbf B_\perp$-equations, and not the pressure equation"
   (eq. 15, p. 269).
5. **Engquist–Osher flux** (§2.3.1, eqs. 18–28). Jump expansion at the
   mean state (eq. 18); scalar form $F^{EO}=f(u_L)+\sum_s(-1)^sf(u^s)$ over
   sonic points (eq. 24) and its system form (eqs. 25–27), split into
   subfluxes so that parts can be differenced as divergences and others as
   gradients (eq. 28). Linear wave-speed interpolation replaces the 1992
   cubic Hermite one, which "does not alter any of our results".
6. **Strong rarefactions** (§2.3.2, eqs. 29–30). Detected when the fast
   speed at the mean state is below the jump of the entropy-wave speed; the
   flux becomes the "positively conservative" Einfeldt form with
   $b^+=\max(\lambda_R^+,\lambda_e^+,0)$, $b^-=\min(\lambda_L^-,\lambda_e^-,0)$.
7. **Degeneracies** (§2.3.3, eqs. 31–33). $B_x=0$ gives a five-fold
   coincidence; $\mathbf B_\perp=0$ gives fast–Alfvén, Alfvén–slow or
   triple coincidence. With the 1992 eigenvectors "the degeneracy of the
   eigenvalues does not also imply a deficiency in the eigenvectors. We
   always have a set of complete, linearly independent eigenvectors"
   (p. 273); they are not reprinted.
   [Roe & Balsara (1996)](/sources/roe-balsara-1996.md) fn. 1 (p. 60)
   correct those 1992 eigenvectors (their ref. [3], Zachary & Colella,
   J. Comput. Phys. 99, 1992): the last component of the slow left
   eigenvector "should be $\tau\alpha_s$", and the normalizing factors
   "can be simplified considerably". Detection
   $|\lambda_l^e-\lambda_m^e|\le c\sum_k|\alpha_k(\kappa_{kl}-\kappa_{km})|$,
   $c=0.1$ (eq. 31), plus an empirical test for the Alfvén–slow case
   (eq. 32). Degenerate pairs whose speed changes sign get a Rusanov term
   $-\tfrac12\nu\sum_{k=l,m}\alpha_k\bar{\mathbf R}_k$ (eq. 33).
8. **$\nabla\cdot\mathbf B$** (§2.4, pp. 274–275).
   * The scheme preserves $\nabla\cdot\mathbf B=0$ "only to the truncation
     error of the method. In principle, that truncation error could be
     $O(1)$" at discontinuities.
   * Vector-potential and flux-function formulations are set aside: they
     need "a staggered mesh, and the equations are not in a form suitable
     for characteristic analysis".
   * "We follow the prescription in [4], remove the nonsolenoidal part of
     B, and then apply a Hodge projection to B at the end of each
     timestep": eq. 34 prints $\nabla^2\phi+\nabla\mathbf B=0$, then
     $\mathbf B=\mathbf B-\nabla\phi$ (see **Recorded as printed**). Gradient
     and divergence are "second-order central difference approximations",
     which "leads to nonstandard discretizations of the Laplacian",
     solvable by multigrid.
   * "For the two-dimensional problems presented in this paper, we did not
     find any noticeable difference regardless of whether or not we applied
     a projection."
   * §4: the projection is an option ("we have the option of applying a
     Hodge decomposition"); the nonconservative formulation "appears to
     suppress the occurrence of monopole forces"; $\nabla\cdot\mathbf B=0$
     "applies exactly to the continuum equations, even if it does not apply
     to the discretized version".
9. **Unsplit outlook** (§§1, 4). An unsplit method after Colella is
   announced, expected to "improve the advection of the solenoidal
   magnetic field".
10. **Cost** (§3). 15 µs per cell in 1D, twice that in 2D (about 32,000
    points/s) on a Cray Y-MP; Courant number $\sigma = 0.8$ (eq. 35).

# Tests

All at $\sigma = 0.8$, no artificial viscosity (§3). Gaussian units.

| § / Fig. | Problem | Set-up | Findings |
|---|---|---|---|
| §3.1, Figs. 1–2 | Sod | $\gamma=1.4$; 100 points, 50 steps | Shock in 3 points; contact more diffuse (no contact detection); a small undershoot at the rarefaction base. Compared with PPM with and without contact detection. |
| §3.1, Fig. 3 | Brio–Wu | $\gamma=2$, $B_y = \pm\sqrt{4\pi}$, $B_x=0.75\sqrt{4\pi}$; 800 points, 400 steps | "Excellent agreement"; small perturbation at rarefactions; sharp shocks without post-shock oscillations. |
| §3.1, Fig. 4 | Strong magnetized Sod | $B_x=0$, $P_L=1000$, $\gamma=5/3$; 200 points, 100 steps | Well behaved at $\gamma \ne 2$, "while the Brio and Wu solver could not". |
| §3.1, Fig. 5 | Einfeldt 1-2-0-3 | $\gamma=1.4$, velocities $\mp2$; 100 points, $t=0.1$ | Two strong rarefactions, "not linearizable"; handled by eqs. 29–30. |
| §3.2.1, Figs. 6–8 | Magnetized blast | $r=0.1$, inner/ambient pressure 100/1, $B_{y0}=0, 10, 100$; $120^2$, 48 steps | Spherical at $B_{y0}=0$ ("essentially identical" to PPM); increasingly anisotropic with field; step-like contour irregularities near strong discontinuities. |
| §3.2.2, Fig. 9 | Compressible Orszag–Tang | Periodic, $192^2$; $\mathbf v=-\sin y\,\hat{\mathbf x}+\sin x\,\hat{\mathbf y}$, $\mathbf B=-\sin y\,\hat{\mathbf x}+\sin 2x\,\hat{\mathbf y}$; $M_0=1$, $\beta=10/3$ | Shown after 300 steps, "approximately 2 Alfven transit times"; two sharp shock jumps in a cut; decay "appears to closely match" Dahlburg–Picone. |

No divergence diagnostic in any test, and the paper does not say whether
the 2D figures were run with or without the projection.

# Notation map

| Zachary et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$ (cell-centred) | $B_h$, collocated | Gaussian units |
| $\mathbf u$ | $u_h$ | |
| $\phi$ (eq. 34) | $\phi_h$ | the printed signs are inconsistent (see below) |
| central $\nabla\cdot$, $\nabla$ (eq. 34) | $D_h^{\mathrm c}$, central $G_h$ | "second-order central difference" |
| "nonstandard" Laplacian | $D_h^{\mathrm c} G_h$ | the wide $2\Delta x$ stencil of [projection](/methods/projection-method.md) |
| $\mathcal L_x^{\Delta t}$, $\mathbf L_x^{\Delta t}$ | words: 1D sweep operators | |
| $\mathbf F^{EO}$, $\mathbf F^G$ | words: base-scheme numerical flux of the full system | $f^{x,*}$ is registered for field components only |
| $\mathbf W_L^*$, $\mathbf W_R^*$ | words: Riemann intermediate states | **collision**: not the provisional $B_h^*$ |
| $\gamma$ (limiter factor, eq. 10) | words | **collision** with the adiabatic $\gamma$ in the same paper |
| $c = 0.1$ (eq. 31) | words | letter-only clash with $c_h$, $c_p$ |
| $\alpha_k$, $\bar{\mathbf R}_k$, $\kappa_{lm}$ | words | paper-local; $\mathbf R$ is not restriction |
| $\Delta x$, $\Delta t$, $\sigma$ | $h$, $\Delta t$, words | |

# Pages created or updated

* Created [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): the $192^2$ compressible set-up and the "no noticeable difference" statement.
* Updated [Projection method](/methods/projection-method.md): an optional collocated central projection with eq. 34 as printed, and its reported lack of effect.
* Updated [Eight-wave formulation](/methods/eight-wave.md): a Godunov use of the nonconservative momentum form before Powell, with the split-sweep source terms.
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): unrotated Brio–Wu runs in Gaussian units and the strong variant.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (the scheme placed in the truncation-error class, §2.4).

# Citations

1. `~/papers/mosaic/div-free-amr/1994-SISC-Zachary-1011370915019.pdf`.
   * **Version read.** The publisher's typeset version of record (SIAM, 22
     pages, download watermark of 27 November 2014). Received 22 June
     1992; revised version accepted 24 June 1993.
   * **Identity.** doi:10.1137/0915019, checked on Crossref: title and
     authors match; SIAM J. Sci. Comput. 15(2):263–284, issued March 1994;
     reference count 25.
   * **How it was read.** Text extraction of all pages; pp. 3–16, 19–21
     and the reference page were rendered and read visually. The 1992
     eigenvectors are not in this paper and are not reproduced.
   * **Recorded as printed.**
     * Eq. 34 prints $\nabla^2\phi+\nabla\mathbf B=0$ (dot missing), then
       $\mathbf B=\mathbf B-\nabla\phi$ (pp. 274–275). Taken literally
       this doubles the divergence:
       $\nabla\cdot(\mathbf B-\nabla\phi)=2\nabla\cdot\mathbf B$ (checked by
       the compiler on the page images). One of the two signs must be
       flipped for a projection; the intent is unambiguous.
     * Eq. 1f (energy), reader's reading: with the stated total energy it
       differs from the conservative energy equation by a term that is not
       a $\nabla\cdot\mathbf B$ term, so the claim of $\nabla\cdot\mathbf
       B(\ldots)$ differences is verified for momentum only; the 1D form
       (2h) is consistent, which suggests the energy in (1f) is meant per
       direction. Its first sum prints $\partial/\partial x$ for
       $\partial/\partial x_i$.
     * Eq. 4 prints no operator between the two $\mathbf H$ terms
       (reader's reading).
     * Eq. 35 prints $\Delta t=\sigma\max(\ldots)$ where a CFL step is a
       minimum (reader's reading).
     * Fig. 5: the right-state density prints as "l", read as 1.
   * **Reference list.** 25 entries, all merged; no DOIs printed. Roe is
     printed as J. Comput. Phys. 53 (1981), p. 357. Trangenstein is printed
     "Tragenstein"; the Brackbill–Barnes title prints "∇B" without the dot.
     The bibliography key `zachary-1994` was renamed
     `zachary-malagoli-colella-1994` to match this page. The bibliography
     holds 3711 entries after this batch.
