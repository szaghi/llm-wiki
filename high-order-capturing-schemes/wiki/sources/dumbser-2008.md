---
type: Source
title: "Dumbser et al. (2008) — A unified framework for the construction of one-step finite volume and discontinuous Galerkin schemes on unstructured meshes"
description: "Defines the PNPM family — data of degree N, a constrained least-squares reconstruction of degree M ≥ N, finite volume for N = 0 and DG for N = M — with a nodal, continuous-in-time local space–time Galerkin predictor solved by Picard iteration and a quadrature-free one-step update; the 1D linear CFL limit depends on N only (Table 1), the intermediate schemes are the most efficient on smooth Euler, and orders up to six are shown on triangles and tetrahedra, with WENO shock tests for MHD, RMHD and elasticity."
resource: "doi:10.1016/j.jcp.2008.05.025"
source_kind: paper
authors: [Dumbser M., Balsara D.S., Toro E.F., Munz C.-D.]
year: 2008
venue: "J. Comput. Phys. 227:8209–8253"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2008-JCP-Dumbser-101016jjcp200805025.pdf"
tags: [ader, single-step, dg, finite-volume, unstructured, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper defines the **PNPM family** of one-step schemes. The data are
stored and tested with polynomials of degree $N$ per element; before
each step a linear, constrained least-squares reconstruction raises them
to degree $M \ge N$, and that polynomial drives the time evolution and
the fluxes. $N = 0$ is classical high-order finite volume, $N = M$ is
DG, and $0 < N < M$ is a new intermediate ("Hermite FV" or
"reconstructed DG") class from third order up (§1, Fig. 1, §2). The time
discretization is a new **local continuous space–time Galerkin
predictor**: nodal, with the initial condition imposed strongly at
$t^n$, solved by a Picard-type fixed-point iteration (§3). It supplies
space–time polynomials of the state, fluxes and sources to a
quadrature-free one-step update with one Riemann problem per face,
independent of the order (§4). A 1D von Neumann analysis shows that the
CFL limit depends on $N$ only, not on $M$ (Table 1). Convergence to
sixth order is shown on 2D Euler (triangles) and 3D GLM-MHD
(tetrahedra), where the intermediate schemes are the most efficient for
the hydrodynamic variables (§5). With $N = 0$ and nonlinear WENO the
scheme runs shock problems for ideal MHD, relativistic MHD and nonlinear
elasticity (§6). In this bundle the predictor is merged into
[ADER](/methods/ader.md).

# Key claims

The registry degree $K$ of the evolved polynomial $\mathcal P_i$ is the
paper's reconstruction degree $M$; the data degree $N$ has no registry
symbol and is named in words.

1. **The PNPM framework** (§§1–2, Fig. 1, eqs. 2–7). Data of degree $N$
   and reconstruction of degree $M \ge N$ in hierarchical orthogonal bases
   that share their first modes. $N = 0$ is FV, $N = M$ is DG (the
   reconstruction is the identity), and $N \ne 0$, $M > N$ is new "from
   third-order of accuracy upwards" (§1; p. 8210 misprints the condition,
   see Citations). Nonlinear HWENO $P_1P_2$ and $P_1P_3$ on structured
   meshes are credited to Balsara et al. (2007) (§1;
   [Hermite WENO](/methods/hermite-weno.md)).
2. **"M-exact" reconstruction** (§2, eqs. 9–13). An $L^2$ projection on
   every stencil element, in reference coordinates, which for
   straight-edged simplices "avoids ill-conditioned reconstruction
   matrices" (p. 8213). The minimum stencil is the ratio of the numbers of
   modes of degree $M$ and $N$, "very compact for $N > 0$" (p. 8214); in
   practice twice that in 2D and three times (at least 12) in 3D. The
   overdetermined system is solved once, in preprocessing, by constrained
   least squares under **generalized conservation**: the first modes of
   the reconstruction equal the data. It generalizes Barth–Frederickson
   k-exact reconstruction. The reconstruction is linear; nonlinear PNPM is
   future work (§§1, 7).
3. **Local continuous space–time Galerkin predictor** (§3.2,
   eqs. 14–25). The PDE on the space–time reference element is tested
   with space–time nodal basis functions; state, fluxes and sources are
   expanded in the same basis, the flux degrees of freedom being *nodal*
   evaluations of the physical flux at the state nodes (eq. 22). The
   nodes at $t^n$ are known from the reconstruction; only the later nodes
   are iterated (eqs. 23–25, eq. 25 read from the page image). There is no
   integration by parts in time and the initial condition is imposed
   strongly. Contrast (§3.1, p. 8216): the local space–time *DG*
   predictor of Dumbser, Enaux & Toro (2008) imposes it weakly and has more
   degrees of freedom; only the non-stiff case is treated here.
4. **Convergence of the iteration** (§3.2, p. 8218, eq. 26). By symbolic
   algebra, the iteration matrices of the flux terms, and every linear
   combination of them, have only zero eigenvalues "for any order of
   accuracy up to six and for any number of space dimensions up to
   three"; the general case is conjectured. The eigenvalues of the source
   matrix have modulus below one. For linear PDEs the iteration is then a
   contraction, convergent "at least under a suitable CFL stability
   condition"; for linear homogeneous scalar equations it converges "for
   any initial guess vector after at most $M$ iterations". It is "a
   discrete analogue of the Picard iteration for ODEs".
5. **Iteration count in practice** (§3.2, p. 8218; §5.2.1, p. 8223). The
   initial guess is the stationary solution. "Also for nonlinear systems
   only at most $M$ or $M+1$ iterations were needed to reach convergence
   to a precision of $10^{-9}$", consistent with the continuous-Picard
   estimate that the error is $O(\Delta t^{M+1})$ after $M$ iterations.
   The convergence runs iterate to a tolerance of $10^{-9}$ on the
   Euclidean norm of the update, not to a fixed count. At second order
   ($M = 1$) the predictor is "fully explicit" and needs no iteration; in
   the second-order FV case it "automatically reduces to the MUSCL
   scheme" ([MUSCL](/methods/muscl.md)).
6. **Minimal nodal space–time basis** (§3.3, eqs. 27–31). Its size is
   that of the full space–time polynomial space of degree $M$; nodes are
   equispaced on simplex layers at times $t^n + l\Delta t/M$,
   $0 \le l < M$, plus one node at the spatial barycentre at $t^{n+1}$.
7. **Quadrature-free one-step update** (§4, eqs. 32–38). The DG weak form
   over the space–time element is tested with the degree-$N$ functions,
   with the predictor in the flux and source terms. The numerical flux has
   a leading two-point part at the face's space–time barycentre and a
   corrector linear in the four arguments (two states, two fluxes), so it
   integrates analytically through precomputed matrices; both parts are
   Rusanov, with signal speeds "computed using the states at the element
   face space–time barycenter and then … frozen" (p. 8220), credited to
   Dumbser, Käser, Titarev & Toro (2007). Four steps: reconstruction,
   local evolution, Riemann problem, update (p. 8221).
8. **Linear stability depends on $N$ only** (§5.1, eqs. 39–40, Table 1).
   1D von Neumann on linear advection: largest stable $\nu$ is 1.00 for
   $N = 0$ and every $M$; 0.33 for $N = 1$, $M = 1$ and 0.32 for
   $N = 1$, $M = 2, 3, 4$; 0.17 for $N = 2$; 0.10 for $N = 3$; 0.069 for
   $N = 4$. "It is the polynomial degree $N$ of the data representation
   that governs the stability … and not the polynomial degree $M$", so
   $0 < N < M$ runs larger steps than DG of the same order. The analysis
   is 1D, up to fifth order; **no multi-D rule is derived**. The 2D and 3D
   runs use $\nu = 0.7/(2N+1)$, or $0.5/(2N+1)$ at fifth and sixth order
   (p. 8223).
9. **Efficiency** (§5.2.1, Tables 2–3). On smooth 2D Euler, "high order
   finite volume schemes seem to be less accurate than the mixed $P_NP_M$
   schemes and the pure DG schemes of the same accuracy on the same mesh";
   PNPM with $N < M$, $N$ close to $M$, is as accurate as DG. An error of
   about $3\times10^{-5}$ costs about 900 s with $P_4P_4$, 450 s with
   $P_3P_4$ and 300 s with $P_2P_4$ (all on $32^2$), and about 2800 s with
   $P_0P_4$ on $128^2$. Per element update at sixth order: 140 µs
   ($P_0P_5$) to 210 µs ($P_5P_5$) (Table 3).
10. **MHD needs cleaning for formal order** (§5.2.2, pp. 8227–8228). "We
    did not obtain the correct convergence rates without the use of the
    divergence cleaning approach … high order schemes alone are not able to
    resolve the problem of the divergence-free condition". For the field
    components pure DG is the most efficient; for $\rho$, $\mathbf v$, $p$
    the intermediate schemes are
    ([hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
11. **Generality of the predictor** (§6.2, p. 8233). In relativistic MHD
    the primitive variables have no closed form in the conserved ones, so
    a Cauchy–Kowalewski procedure "becomes impossible for orders greater
    than two"; the predictor needs only pointwise flux and source
    evaluations. The authors claim the first high-order WENO FV RMHD
    computations on unstructured triangles (p. 8240).
12. **Against TVD Runge–Kutta** (§7): no extra MPI communication within a
    step; no accuracy barrier in time; no stored stages; one numerical flux
    per face and no spatial Gaussian quadrature.
13. **History of the high-order Riemann problem** (§3.1). Kolgan (1972):
    reconstruction without time evolution, second order in space, first in
    time, linearly unstable. Ben-Artzi & Falcovitz's GRP: a time series at
    the interface. MUSCL–Hancock: Cauchy–Kowalewski evolution, then a
    classical Riemann problem; Harten et al.'s ENO extends that line to
    arbitrary order; ADER returns to the GRP line. Castro & Toro: "for
    linear hyperbolic systems, all approaches coincide".

# Tests

| § | Test | Set-up | Findings |
|---|---|---|---|
| 5.1 | 1D linear advection, von Neumann | periodic, one Fourier mode, up to fifth order | Table 1 (claim 8) |
| 5.2.1 | 2D [isentropic vortex](/benchmarks/isentropic-vortex.md) | $[0,10]^2$ periodic, strength 5, $\gamma = 1.4$, $t = 10$; irregular triangles, $N_G$ = 24/16 … 128/64 (FV/others; 128/48 at sixth order); $\nu = 0.7/(2N+1)$ ($0.5/(2N+1)$ at fifth and sixth); Picard tolerance $10^{-9}$ | Table 2: $L^2(\rho)$ design order for all PNPM, O2–O6; e.g. O6 finest rates $P_0P_5$ 6.2, $P_1P_5$ 6.9, $P_2P_5$ 4.9 (5.9 one step before), $P_3P_5$ 5.9, $P_4P_5$ 5.8, $P_5P_5$ 5.8. Table 3: CPU times |
| 5.2.2 | 3D ideal MHD vortex (Balsara), rotated 45° about $y$ | $[-5,5]^3$ periodic, GLM $c_h = 3$, $t = 10$; tetrahedra $N_G$ = 10–40, 64 CPUs | Tables 4–5: orders reached O2–O6; $P_3P_4$ on $40^3$ (434,327 tetrahedra) reaches about $10^{-5}$ with $8.69\times10^6$ DOF per variable; needs GLM (claim 10). Table 6: CPU times |
| 6.1.1 | 3D MHD shock tubes: Lax with $\mathbf B = 0$, [Brio–Wu](/benchmarks/brio-wu-shock-tube.md), [Ryu–Jones](/benchmarks/ryu-jones-shock-tubes.md) | 186,145 tetrahedra, $h = 1/400$, $[-0.5,0.5]\times[-0.01,0.01]^2$; $P_0P_2$ characteristic WENO; $c_h$ = 0, 2, 2 | "excellent agreement" with 1D references (Fig. 8); the Brio–Wu reference is a 1D second-order TVD run on 20,000 cells |
| 6.1.2 | [MHD rotor](/benchmarks/mhd-rotor.md) | circle $r = 1/2$, 106,842 triangles, $c_h = 2$, $\gamma = 1.4$, $t = 0.25$ (745 steps); $P_0P_2$ componentwise WENO | agrees with Balsara–Spicer; no spurious oscillations in density or magnetic pressure "thanks to the divergence cleaning"; 76 min on one core |
| 6.1.3 | [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) | $[0,2\pi]^2$, Jiang–Wu data with $\mathbf B$ scaled by $\sqrt{4\pi}$ (eq. 53), $\gamma = 5/3$, 89,832 triangles, $c_h = 2$, $t = 5$ (1533 steps); $P_0P_2$ componentwise WENO | pressure at $t$ = 0.5, 2, 3, 5 agrees with Jiang–Wu fifth-order FD WENO on $192^2$ (Fig. 11) |
| 6.2.1 | RMHD 1D shock tubes 1–5 (Balsara) | 400 cells (800 for case 3), $\nu = 0.8$ (0.1 for case 4); $P_0P_2$ characteristic WENO; exact solution of Giacomazzo–Rezzolla | very good agreement; a compound wave in case 1, as in Balsara's TVD runs, absent from the exact solution; largest oscillations in $\rho$ for case 2; wall heating in case 4 |
| 6.2.2 | RMHD case 5 on a 2D mesh | $[0,1]\times[0,0.05]$, 17,628 triangles | cut at $y = 0.025$ matches the 1D reference (Fig. 19) |
| 6.2.3 | RMHD large-amplitude Alfvén wave (Del Zanna et al.) | $[0,1]\times[0,0.4]$ periodic, adiabatic index 4/3, $t = 2.618033988$; $\nu = 0.5/(2N+1)$ | Table 9 ($B_z$): finest rates $P_0P_2$ 3.0, $P_1P_2$ 3.2, $P_2P_3$ 3.9, $P_3P_5$ 6.1; $P_3P_5$ at $N_G = 4$ gives $3.58\times10^{-5}$ in 47.8 s, $P_0P_2$ at $N_G = 128$ gives $3.44\times10^{-5}$ in 16,597.6 s |
| 6.2.4 | RMHD rotors (Del Zanna et al.) | circle $R = 0.5$, 121,196 triangles, rotor speeds 0.8 and 0.995, $c_h = 1$; $P_0P_2$ characteristic WENO | Alfvén waves and shear roll-up as in the reference; negative pressures handled by reducing the order "locally to one" |
| 6.3 | Nonlinear elasticity (Godunov–Romenski; Titarev et al.): 3- and 5-wave shock tubes, a rotor | copper equation of state; 4420 triangles, $t = 0.06$; rotor on 121,196 triangles; $P_0P_2$ componentwise WENO | very good agreement with Titarev's reference, "only few oscillations" |

# Notation map

| Dumbser et al. (2008) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_p$ (component $p$) | $u$ | the index $p$ collides with pressure and the family index $(p)$ |
| $f_p, g_p, h_p$; $\vec F_p$ | $\mathbf f(u)$ | |
| $S_p$ | $\mathbf s(u)$ | |
| $N$ (data degree) | words ("data degree") | not in the registry |
| $M$ (reconstruction and predictor degree) | $K$ | **collision**: $M$ is the TVB constant; PNPM kept as a proper name |
| $\Phi_l$, $\Psi_l$ | words (bases of degree $N$ and $M$) | **collision**: $\Phi$ is the projection potential |
| $\hat u^{(m)}_{pl}$ | $\hat u^{(l)}_i$ | modal coefficients |
| $w_p$ | $\mathcal P_i$ | reconstructed polynomial |
| $\mathcal U_p(\vec\xi,\tau)$ | $u^{\mathrm p}_i$ | the predictor |
| $\theta_k$ (space–time nodal basis) | words | **collision**: limiter $\theta$ |
| $\hat{\mathcal U}_{lp}$, $\hat{\mathcal F}_{lp}$ | words (nodal space–time degrees of freedom) | the registry $\hat u^{(t)}$, $\hat f^{(x)}$ are modal |
| $\tau = (t - t^n)/\Delta t$ | words | **collision**: WENO-Z $\tau$ |
| $\vec\xi = (\xi, \eta, \zeta)$ | words (reference coordinates) | **collisions**: $\xi$, $\eta$, $\zeta$ |
| $K^\tau$, $K^\xi$, $M$ (matrices) | words | $K$ is a degree, $M$ the TVB constant |
| $T^{(m)}$ | $\mathcal T$ (triangles), words (tetrahedra) | |
| CFL | $\nu$ | |
| $c_h$, $\Psi$ (GLM) | $c_h$, $\psi_{\mathrm{GLM}}$ | |
| $\gamma$ (Lorentz factor, §6.2), $\Gamma$ (adiabatic index, §6.2) | words; $\gamma$ | **collision** in §6.2 only: the roles are swapped |
| $\epsilon$, $\kappa$, $\mu$, $q$ (vortex parameters) | words | **collisions** with $\kappa$, $\mu$, $q$ |
| $\lambda_1$, $r$, $\varepsilon$ (WENO parameters) | $d_{\mathrm c}$, $q$, $\varepsilon$ | **collision**: the paper's $r$ is the weight power |

# Pages created or updated

* Updated [ADER one-step schemes](/methods/ader.md) (batch-18 block: PNPM,
  the continuous nodal predictor and its convergence argument, Table 1 and
  the attribution of "divided by the dimension", frozen Rusanov speeds,
  efficiency; a bullet added to the Open Picard-count entry, which stays
  Open).
* Updated [Balsara (2017)](/sources/balsara-2017-d.md) (key claim 1)
  and [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)
  (claim 10).
* Cited on [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md) (batch-18 block).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2008-JCP-Dumbser-101016jjcp200805025.pdf`.
   * **Version read.** The publisher's typeset PDF (Elsevier), 45 pages.
     Received 12 December 2007; revised 9 May 2008; accepted 13 May 2008;
     online 10 June 2008.
   * **Identity.** doi:10.1016/j.jcp.2008.05.025, printed on page 1 and
     checked on Crossref: title as on page 1, authors Dumbser, Balsara,
     Toro, Munz, J. Comput. Phys. 227(18):8209–8253, September 2008,
     reference count 83. The bibliography entry once carried a different
     title ("… quadrature-free one-step finite-volume …"); it now has the
     page-1 title.
   * **How it was read.** Text extraction of all sections; eq. 25 and
     Table 9 read from page images (pp. 8217–8218, 8242). Not reproduced:
     Appendix A (the explicit $M = 3$ 1D basis and matrices, text layer
     garbled), eq. 48 (GLM-MHD flux), eqs. 51–52 and 54–62 (vortex
     perturbations, RMHD conversion). Figures read through captions and
     text.
   * **Recorded as printed.**
     - p. 8210, §1: "For $N \ne 0$; $N > M$ we obtain a new class" is a
       misprint for $M > N$ (abstract, Fig. 1 caption and §7 say $M > N$).
     - Ref. [43] prints Gottlieb & Shu, Math. Comp. 67, with year 1988;
       ref. [79] van Leer, SIAM J. Sci. Stat. Comput. 5, with 1985; ref. [1]
       Abgrall with J. Comput. Phys. volume 144; ref. [7] "Spicerm";
       ref. [36] Ann. IHP volume 3 for 1991 (unverified); ref. [33] has
       garbled, duplicated author names.
   * **Reference list:** 83 entries, all merged (83 keys, matching
     Crossref's count). Gottlieb & Shu printed 1988 lands on
     `gottlieb-1998` ("printed with year 1988 by dumbser-2008"); van Leer
     printed 1985 on `vanleer-1984-c`; Abgrall printed 144:45 on
     `abgrall-1994` ("printed as J. Comput. Phys. 144:45 by
     dumbser-2008"); "Loercher" on `lorcher-2007` ("first author printed
     'Loercher' by dumbser-2008"); Hirsch is `hirsch-1988` ("printed as
     Vol. I: Fundamentals of Numerical Discretisation by dumbser-2008").
     Printed-order suffixes were mapped to the bundle's keys by vol:page:
     Dumbser, Enaux & Toro (2008) is `dumbser-2008-b`; the Cockburn & Shu
     1989 pair (`cockburn-1989` Math. Comp. 52:411, `cockburn-1989-b`
     J. Comput. Phys. 84:90), the Cockburn 1998 pair (`cockburn-1998`
     J. Comput. Phys. 141:199, `cockburn-1998-c` SIAM J. Numer. Anal.) and
     the Balsara & Spicer 1999 pair were swapped against printed order;
     the Dumbser 2007 papers land on `dumbser-2007`, `-2007-b`, `-2007-c`,
     and Geophys. J. Int. 171:665 is the new `dumbser-2007-e`; Qiu's papers
     on `qiu-2004`, `qiu-2005-b`, `qiu-2005-c`. Bibliography: 3380 entries.
