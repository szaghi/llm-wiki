---
type: Source
title: "Brio & Wu (1988) — An upwind differencing scheme for the equations of ideal magnetohydrodynamics"
description: "Roe-type upwind scheme for the 1D ideal-MHD system with constant normal field: an exact Roe matrix for gamma = 2 only, a renormalized right-eigenvector set claimed well defined everywhere (eq. 46 fixes the factors at the triple umbilic by assignment), the coplanar shock tube with a slow compound wave, and a proof that the MHD system is nonconvex."
resource: "doi:10.1016/0021-9991(88)90120-9"
source_kind: paper
authors: [Brio M., Wu C.C.]
year: 1988
venue: "J. Comput. Phys. 75:400-422"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1988-JCP-Brio-1010160021-99918890120-9.pdf"
tags: [mhd, shock-capturing, riemann-solver, eigenvectors, benchmark]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds a Roe-type (linearized Riemann solver) upwind scheme for
1D ideal MHD: the seven-equation system that remains when the normal field
is held constant (§IV, eqs. 16–23).
* For $\gamma = 2$ it finds an exact Roe matrix in mean-value-Jacobian form
  (eqs. 26–30). For general $\gamma$ it finds none and uses the Jacobian at
  an arithmetic average state, which loses the exact flux-difference
  property (§IV.1).
* Its lasting contribution is a **renormalized complete set of right
  eigenvectors** (eqs. 39–46), claimed well defined everywhere, including
  zero normal field and zero transverse field; eq. 46 fixes the factors at
  the triple umbilic by assignment.
* The coplanar Riemann problem of §V, the "Brio–Wu shock tube", has a
  solution containing a **slow compound wave**.
* With the complete eigenvector set, §VI shows that the MHD system is
  **nonconvex**, which explains the compound wave.

The paper says nothing about discrete divergence control. In 1D the
constraint reduces to a constant normal field, a parameter of the scheme.
It is ingested as the origin of the shock tube that the
[rotated shock tube](/benchmarks/rotated-shock-tube.md) rotates and of the
eigenvector normalization used by [Jiang & Wu (1999)](/sources/jiang-1999.md).

# Key claims

1. **Divergence constraint** (§II after eq. 4; §IV after eq. 22). The 3D
   system holds "with the additional requirement that $\nabla\cdot B = 0$,
   which is satisfied in the initial value problem if it is satisfied
   initially." In 1D the normal-field equation drops out and the normal
   field is constant, so the system has seven equations and the Jacobian
   (eq. 23) is $7\times7$ with the normal field as a parameter. No reason
   beyond this is given; multi-dimensional extension is mentioned only as
   possible "with or without dimensional splitting" (§III).
2. **Non-strict hyperbolicity** (§§I, II, IV.2). The eigenvalues (eq. 31)
   are the flow speed and the flow speed $\pm$ the fast, Alfvén and slow
   speeds (eqs. 32–33); up to five of the seven may coincide.
   * Zero normal field: slow and Alfvén speeds vanish, and the flow speed
     has multiplicity 5.
   * Zero transverse field: fast and slow speeds become the larger and
     smaller of the sound and normal Alfvén speeds; multiplicity 2, or 3 when
     those two speeds are equal (§IV.2).
3. **Roe matrix for $\gamma = 2$** (§IV.1, eqs. 24–30). A Roe matrix of
   mean-value form exists, with $\sqrt\rho$-weighted velocities and
   enthalpy, the geometric-mean density, and $\sqrt\rho$-weighted
   transverse fields. Applied to the Euler equations, the procedure
   reproduces Roe's average uniquely.
4. **General $\gamma$: no Roe matrix found** (§IV.1, p. 407). The nonlinear
   system "does not decouple ... we are not able to solve it analytically.
   Neither do we succeed in finding an appropriate parameterization as
   suggested by Roe." The authors evaluate the Jacobian at a simple average,
   which satisfies hyperbolicity and consistency but not the exact
   flux-difference property, so "stationary discontinuities are no longer
   steady solutions", though "they still can be resolved with few grid
   points". The recommended average is the arithmetic mean of density,
   velocity, magnetic field and **total pressure**; averaging the energy
   instead "may lead to a negative averaged pressure which is not allowed".
5. **Eigenvector renormalization** (§IV.3, eqs. 34–46). The Jeffrey–Taniuti
   right eigenvectors become ill defined (0/0 or $\infty$) near zero normal
   or zero transverse field; the eigenvector matrix is singular there, its
   determinant proportional to the square of the difference of the squared
   fast and slow speeds. Fast and slow eigenvectors are rescaled by factors
   built from the fast, slow, sound and normal Alfvén speeds (eqs. 39–40),
   transverse directions by the unit transverse-field components (eqs.
   41–42), Alfvén eigenvectors by the inverse transverse Alfvén speed, with
   explicit limits at the degeneracies (eqs. 45–46). Eq. 46 sets both the
   fast and the slow factor to 1 where the transverse field vanishes and
   the sound speed equals the normal Alfvén speed (the triple umbilic): a
   definition by assignment, not a limit. Result: "a set of right
   eigenvectors which is well defined everywhere." With this normalization
   some entries "are not continuous" as both transverse components
   approach zero (p. 410). Continuity as the
   transverse field passes through zero also needs a sign factor on the
   slow or fast eigenvectors; this is irrelevant for the Roe scheme but
   "crucial" for §VI (p. 410).
6. **Scheme** (§III, eqs. 6–15; §V). First-order Roe flux: the central
   average minus half the sum over waves of $|\lambda_k|$ times wave
   strength times eigenvector (eq. 15). Second order "by Harten's approach",
   with artificial compression on the linearly degenerate field; no limiter
   or entropy fix is given for MHD.
7. **Nonconvexity** (§VI, eqs. 54–55, Figs. 8–10). In the coplanar case, the
   directional derivative of the fast (if the sound speed is below the
   normal Alfvén speed) or slow (otherwise) eigenvalue along its eigenvector
   is proportional to the transverse field near zero: zero at one point,
   nonzero elsewhere. These fields are neither genuinely nonlinear nor
   linearly degenerate; "the MHD system is nonconvex". Jeffrey and
   Taniuti's genuinely-nonlinear conclusion is "not correct, since the set
   (34) is not complete." Compound waves (a shock with an attached
   rarefaction of the same family) follow.
8. **Intermediate shock** (§VI, p. 420). The transverse field changes sign
   across the slow shock in the compound wave, so it is an intermediate
   shock. If such shocks are inadmissible, "all numerical schemes tested in
   Section 5 admit nonphysical shocks"; the authors cite resistive-MHD
   evidence that some intermediate shocks, "including the one here", can
   exist.
9. **Cost** (§VII). About 10 times the flops per point per step of
   Lax–Wendroff; upwind at 200 points (4 times fewer steps) beats
   Lax–Wendroff at 800.

# Tests

* **Coplanar shock tube** (§V, pp. 411–414, Figs. 2–6, 9). Left: density 1,
  velocity 0, pressure 1, transverse field 1. Right: density 0.125,
  velocity 0, pressure 0.1, transverse field $-1$. Normal field $0.75$,
  $\gamma = 2$ (Sod's hydrodynamic data). 800 points, $\Delta x = 1$,
  $\Delta t = 0.2$ ("CFL ≈ 0.8"), shown after 400 steps.
  * Waves: left-moving fast rarefaction and **slow compound wave**;
    right-moving contact, slow shock and fast rarefaction; checked against
    Riemann invariants and Rankine–Hugoniot conditions (pp. 412–413).
  * Exact Roe ($\gamma = 2$) and arithmetic-average variants agree to 4
    significant digits in constant states and 2 in transitions (p. 413).
  * Lax–Wendroff with Lapidus viscosity oscillates between the waves;
    Lax–Friedrichs smears the slow shock over about 20 points and, at 20 000
    points, matches the second-order upwind result except for the contact;
    FCT shows undershoots and oscillations, much worse at CFL 0.8.
  * Variant with right transverse field $-0.4$: upwind and Lax–Friedrichs
    give an almost stationary slow intermediate shock; Lax–Wendroff could
    not be stabilized "with any value of artificial viscosity" (p. 414).
  * Compound-wave check (§VI, Figs. 8–9): the analytic rarefaction-tail state
    (density 0.6965, velocity 0.5987, transverse velocity $-1.583$,
    transverse field $-0.5341$, pressure 0.5157) against the numerical one
    (0.6963, 0.5997, $-1.578$, $-0.5341$, 0.5133): "The agreement is
    excellent."
* **High-Mach Riemann problem** (§V, p. 416, Fig. 7). As above with zero
  normal field and left pressure 1000 (hydrodynamics with total pressure);
  right-moving shock of Mach 15.5, compared with the exact solution.

No divergence measure is reported; the problems are 1D.

# Notation map

| Brio & Wu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_x$ (normal field) | words: normal field | constant parameter in 1D; the rotated-shock-tube page writes $B_n$ |
| $B_y, B_z$ | words: transverse field | |
| $\nabla\cdot B = 0$ | $\nabla\cdot\mathbf B = 0$ | no discrete form in the paper |
| $\lambda_k$ | $\lambda_k$ | eigenvalues; no registry conflict |
| $f_{i+1/2}$ | words: base-scheme numerical flux of the full system | $f^{x,*}$ is registered for field components only |
| $A$, $A_{i+1/2}$ (Roe matrix) | words | **collision:** $A_h$ is the vector potential |
| $R_k$ (eigenvectors) | words | **collision:** $R$ is restriction |
| $C_k$ (wave strengths) | words | **collision:** $C_h$ is the discrete curl |
| $c_f, c_a, c_s$, $a$ | words | no registry symbols; $c_h$, $c_p$ are GLM quantities |
| $\alpha_f, \alpha_s$ | words | collide with $\alpha^{\mathrm{LF}}$, $\mathcal E^{\alpha}$ |
| $H$ (enthalpy), $h$ | words | **collision:** grid spacings |
| $E$ (total energy) | words | **collision:** $E_h$ is the EMF |
| $P^*$, $\rho^*$ | words | **collision:** star marks base-scheme provisional values |

# Pages created or updated

* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): the unrotated problem's data, origin and wave structure.
* Updated [Eight-wave formulation](/methods/eight-wave.md): the seven-wave system and its eigenvector degeneracies.

# Citations

1. `~/papers/mosaic/div-free-amr/1988-JCP-Brio-1010160021-99918890120-9.pdf`.
   * **Version read.** The published journal version (Academic Press scan,
     23 PDF pages; PDF page $n$ is printed page $399+n$). Received
     21 June 1985, revised 15 May 1987.
   * **Identity.** doi:10.1016/0021-9991(88)90120-9, checked on Crossref:
     title and authors match; vol. 75, issue 2, pp. 400–422, issued April
     1988; reference count 20.
   * **How it was read.** The text layer is OCR and garbles most equations;
     every equation used here was read from rendered pages (PDF pp. 4–12,
     19, 22–23). Not reproduced: the last row of the Jacobian (eq. 23),
     eq. 27, the $3\times3$ systems (eqs. 51–52) and the Jeffrey–Taniuti
     eigenvectors (eq. 34). Figures are used through captions and text.
   * **Recorded as printed.** §IV.3 cites Jeffrey & Taniuti as "[3]"
     (it is [6]); §VI says the eigenvectors were "constructed in Section 3"
     (they are in §IV.3).
   * **Reference list.** 20 entries, all merged; Crossref's reference count
     agrees. Three Harten 1983 entries were resolved by venue: SIAM Rev.
     25:35 is `harten-lax-1983`, J. Comput. Phys. 49:357 is `harten-1983`,
     Harten & Hyman (J. Comput. Phys. 50:235) is the new `harten-1983-c`.
     Osher & Chakravarthy (J. Comput. Phys. 50:447) is `osher-1983-b`,
     distinct from `osher-1983` (Osher & Sanders, Math. Comp. 41:321;
     Crossref). The key `brio-1988` was renamed `brio-wu-1988` to match
     this page. The bibliography holds 3639 entries after this batch.
