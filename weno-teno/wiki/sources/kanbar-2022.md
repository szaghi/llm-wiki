---
type: Source
title: "Kanbar et al. (2022) — Well-Balanced Central Scheme for the System of MHD Equations with Gravitational Source Term"
description: "Second-order Riemann-solver-free unstaggered central scheme for 2D ideal MHD with gravity: it evolves the deviation from a known steady state for exact well-balancing and applies Touma's unstaggered constrained transport to keep a centred discrete divergence of B at round-off, tested on stratified atmospheres."
resource: "doi:10.4208/cicp.oa-2022-0067"
source_kind: paper
authors: [Kanbar F., Touma R., Klingenberg C.]
year: 2022
venue: "Commun. Comput. Phys. 32:878-898"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Communications_in_Computational_Physics_Kanbar_Well-Balanced_Central_Scheme_for_the_System_of_MHD_Equations.pdf"
tags: [mhd, well-balanced, central-scheme, finite-volume, tvd]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper builds a second-order finite-volume
[unstaggered central scheme](/methods/unstaggered-central-scheme.md) for the 2D ideal MHD
equations with a gravitational source $S=(0,0,-\rho g,0,-\rho v_2g,0,0,0)$. It combines three
known ingredients. (i) The Jiang–Levy–Lin–Osher–Tadmor / Touma unstaggered scheme: a
piecewise-linear solution with MC slopes limited in the
[TVD](/definitions/total-variation-diminishing.md) sense, projected onto implicit
ghost staggered (dual) cells, evolved there by a Nessyahu–Tadmor predictor–corrector, and
projected back. No Riemann problem is solved. (ii) A subtraction
form of [well-balancing](/properties/well-balancing.md): with a known stationary solution
$u_{\mathrm e}$, the scheme evolves the deviation $\delta u=u-u_{\mathrm e}$ through
$\partial_t\delta u+\partial_x[f(\delta u+u_{\mathrm e})-f(u_{\mathrm e})]+\partial_y[g(\delta u+u_{\mathrm e})-g(u_{\mathrm e})]=S(\delta u)$,
which uses that $S$ is linear in $u$. (iii) Touma's constrained transport for unstaggered
schemes, which keeps a centred discrete divergence of the
[magnetic field](/properties/divergence-free-magnetic-field.md) at zero.

Short arguments show that $\delta u^n=0$ is preserved through predictor, corrector and back
projection, and that the corrected field keeps the centred divergence zero. The tests use CFL
0.485 and MC parameter 1.5: the Brio–Wu tube in 2D, an MHD
[four-state Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) (divergence
about $10^{-14}$ with constrained transport, $O(1)$ without), a stationary MHD vortex, and
hydrodynamic and MHD waves in gravitationally stratified atmospheres from Fuchs et al.
Agreement with the literature is judged visually. No error norms or convergence orders are
printed, so second order is not verified numerically. The scheme is well balanced only for the
supplied $u_{\mathrm e}$. The printed vortex data are not an MHD equilibrium (see Printed slips),
which this test cannot detect, because the scheme keeps $u_{\mathrm e}$ by construction.

# Version read

arXiv 2202.08584v1 [math.AP], 17 Feb 2022, dated "February 18, 2022" on page 1 and labelled
"A PREPRINT": an author preprint, not the CiCP version of record. It has 14 pages; the
published article has 21 (878–898), so text, tests and slips may differ. Title and authors
match page 1 and Crossref. The PDF's embedded subject and keywords are template leftovers.
Equation, section and figure numbers are those of the preprint.

# Key claims

Local symbols (see the Notation map): $u_{\mathrm e}$ the reference steady state, $\delta u=u-u_{\mathrm e}$,
$\theta_{\mathrm{MC}}$ the MC limiter parameter, $\Omega=-v_1B_2+v_2B_1$.

1. The scheme is a second-order finite-volume unstaggered central scheme that evolves the solution on a single grid and avoids Riemann solvers at cell interfaces through ghost staggered cells (Abstract, §1, §3). **Stated** (second order is not checked numerically)
2. Writing $u=\delta u+u_{\mathrm e}$ and subtracting the steady balance $f(u_{\mathrm e})_x+g(u_{\mathrm e})_y=S(u_{\mathrm e})$ gives the deviation law (6), which reduces to (7) with source $S(\delta u)$ because $S$ is linear in $u$ (§3, Eqs. 4–7). **Derived**
3. The scheme evolves (7) instead of (1) and recovers $u=\delta u+u_{\mathrm e}$; knowing $u_{\mathrm e}$ analytically or numerically is "a key ingredient" (§1, §3). **Stated**
4. Well-balanced property: if $\delta u^n_{i,j}=0$, then $\delta u^{n+1/2}_{i,j}=0$, $\delta u^{n+1}_{i+1/2,j+1/2}=0$ and $\delta u^{n+1}_{i,j}=0$; the solution "remains stationary up to machine precision" (§3, Eq. 17). **Proved** (first item; the other two are called "straight forward")
5. The source integral over the space–time dual box is approximated by the midpoint rule, as the average of $S$ at the four primary nodes at $t^{n+1/2}$ (§3, Eq. 12). **Stated** (design choice)
6. Constrained transport for unstaggered schemes [19]: if the centred divergence $\frac{(B_1)_{i+1,j}-(B_1)_{i-1,j}}{2\Delta x}+\frac{(B_2)_{i,j+1}-(B_2)_{i,j-1}}{2\Delta y}$ is zero at $t^n$, correcting $B$ on the dual cells by Eq. (18) and averaging back to the nodes gives a zero centred divergence on the dual grid (Eq. 20) and on the primary grid (Eq. 21) (§4). **Derived** (the substitution is sketched)
7. $\Omega^{n+1/2}$ at the dual nodes is the average of $\Omega^{n+1}$ and a four-node average of $\Omega^n$, "in order to obtain second order of accuracy in time" (§4). **Stated**
8. All tests use CFL number 0.485 and the MC limiter with $\theta_{\mathrm{MC}}=1.5$ (§5). **Stated**
9. Brio–Wu tube on $[-1,1]^2$, $t=0.25$: cross sections agree "very good" with the literature; constrained transport has "a small smearing out effect", shown on 200, 400 and 800 points with it and on one grid without it (§5.1, Fig. 3). **Shown** (visual; the "convergence study" is a grid overlay)
10. Four-state MHD Riemann problem, $400\times400$, $t=0.8$: with constrained transport the divergence is of order $10^{-14}$, without it $O(1)$ (about $\pm1.5$); the densities look alike (§5.2, Figs. 4–5). **Shown**
11. "Even without treatment we are able to show numerical simulation while other schemes simply blow up without special treatment of the magnetic field" (§5.2). **Stated** (no other scheme is run or cited for this test)
12. MHD vortex: the steady state "gets preserved exactly as the background solution $\tilde U$ is the vortex itself"; pressure profiles on $32^2$, $64^2$, $128^2$ (§5.3, Fig. 6). **Shown** (no error norms)
13. Hydrostatic atmosphere $\rho=\rho_0e^{-y/H}$, $p=p_0e^{-y/H}$, $v=0$, $B=0$, with $H=0.158$, $p_0=1.13$, $g=2.74$: preserved "exactly" with $u_{\mathrm e}$ equal to it; density and energy at $t=0$ and $t=1.8$ coincide (§5.4, Eq. 23, Fig. 7). **Shown** (no error magnitude printed)
14. Perturbed atmosphere (bottom piston, Eq. 24), $800\times200$, $t=1.8$, amplitudes 0.003 and 0.3: results "in a very good agreement" with [7], matching "the most accurate (third order) of the three schemes compared in [7]" (§5.4, Fig. 8). **Shown** (visual, no overlay)
15. Magnetized atmosphere with $B=(0,\mu_B,0)$, $t=0.54$: for $\mu_B=1$ on $400\times200$ without constrained transport the divergence is clearly nonzero (about $-3$ to $5$); with it, on $1200\times600$, it is zero "up to machine precision", and the diffusion it adds is "resolved by evolving the solution on a finer grid" (§5.5, Figs. 10–11). **Shown**
16. The second-order results of §5.5 "are comparable with the results in [7], obtained with third order schemes" (§5.5). **Shown** (visual)
17. As $\mu_B$ grows the wave profile "gets compressed"; for $\mu_B\approx0$ the wave spreads radially (§5.5, Figs. 9, 12). **Shown**
18. The scheme "is capable of preserving any type of known equilibrium states", by the reformulation around a reference state (§6). **Stated** (holds for the supplied $u_{\mathrm e}$; tested on a hydrostatic and a magnetohydrostatic state and on the vortex)
19. Constrained transport is "applied dynamically whenever needed", and is not applied in tests where the divergence is zero at the final time and no instability occurs (§6). **Stated** (no criterion given)
20. All computations are on 2D Cartesian grids; triangular meshes are future work (§6). **Stated**

# Printed slips

- §2, $\Pi_{ij}=-\frac12B_iB_j$ for $i\ne j$ *(compiler check, not in the sources)*. The ideal-MHD momentum flux ($\mu_0=1$) is $\rho vv^\top+(p+\frac12\lvert B\rvert^2)I-BB^\top$, so the off-diagonal stress is $-B_iB_j$. The printed diagonal $\Pi_{ii}=p+\frac12(B_j^2+B_k^2-B_i^2)=p+\frac12\lvert B\rvert^2-B_i^2$ is correct. With $\Pi_{ij}=-B_iB_j$, the printed energy flux $Ev_1+v_1\Pi_{11}+v_2\Pi_{12}+v_3\Pi_{13}$ is the standard $(E+p+\frac12\lvert B\rvert^2)v_1-B_1(v\cdot B)$.
- Eq. (1), last three entries of $F$ printed as $(0,\Lambda_2,-\Lambda_3)$ with $\Lambda=v\times B$ *(compiler check, not in the sources)*. The $x$-flux of $B_k$ in the induction equation is $v_1B_k-B_1v_k$, which gives $(0,\Lambda_3,-\Lambda_2)$. The printed $G$ entries $(-\Lambda_3,0,\Lambda_1)$ agree with the same derivation, and so does the 2D induction equation of §4 with $\Omega=-\Lambda_3$.
- §5.3, MHD vortex *(compiler check, not in the sources)*. The printed field $B_1=-m_pe^{(1-r^2)/2}y$, $B_2=-m_pe^{(1-r^2)/2}x$ has $\nabla\cdot B=2m_pxye^{(1-r^2)/2}\ne0$. The printed pressure $p=1+\frac{m_p^2}2(1-r^2)-\frac{\kappa_p^2}2$ has no factor $e^{1-r^2}$: with $m_p=\kappa_p=1$ it is $1-r^2/2$, negative for $r>\sqrt2$, that is on most of $[-5,5]^2$. For $\rho=1$, $v=\kappa_pe^{(1-r^2)/2}(-y,x)$ and $B=m_pe^{(1-r^2)/2}(-y,x)$, the steady momentum balance $(v\cdot\nabla)v+\nabla(p+\frac12\lvert B\rvert^2)-(B\cdot\nabla)B=0$ gives $\nabla(p+\frac12\lvert B\rvert^2)=(\kappa_p^2-m_p^2)e^{1-r^2}(x,y)$. Hence $p=1+e^{1-r^2}\big(\frac{m_p^2}2(1-r^2)-\frac{\kappa_p^2}2\big)$, and the state is an equilibrium (with $v\times B=0$, so $B$ is also steady). The printed data are not.
- §5.3: "$t=100\frac{2\pi}{\sqrt e\kappa_p}\approx100\frac{3.14}{\kappa_p}$", but $2\pi/\sqrt e\approx3.81$. The vortex is said to be "advected … with a velocity $(u_0,v_0)$", but $u_0=v_0=0$.
- Eq. (14), second bracket: "$D^y_+F(\Delta U^{n+1/2}_{i+1,j}+\tilde U_{i+1,j})$" should be $D^y_+G$.
- Below Eq. (11): "$R_{xy}=[x_i,x_{i+1}]\times[y_i,y_{i+1}]$" should end in $[y_j,y_{j+1}]$.
- End of §3: the scheme maintains "stationary solutions of the Euler system with gravitational source term"; MHD is meant.
- §2 calls $E$ "the kinetic and internal energy of the fluid", but the formula includes $\frac12\lvert B\rvert^2$. $\gamma$ is never given for any test.
- §5.4, Fig. 7: the horizontal axis is labelled $x\in[0,1]$ for a vertical profile on $[0,4]\times[0,1]$. Eqs. (24) and (26) use ghost-index sets $\{0,-1\}$ and $\{0,1\}$.
- §5.1: "we did a convergence study in figure 3", but Fig. 3 overlays three grids without an error measure.
- Typos: "oroginal", "Taylor expnsions" (p. 6), "refered" (p. 3).
- Reference list: [19] and [20] are the same paper (Touma 2010, Appl. Numer. Math. 60:752–766), and [12] and [13] the same Powell 1994 ICASE report in two forms. [4] and [5] share title and authors (Brackbill & Barnes), [5] as J. Comput. Phys. 35:426–430, 1980, and [4] as J. Comp. Phys. 201:261–285, 2004. [6] (Evans & Hawley) is printed as "Astrophys. J. Lett., 332:659".

# Notation map

| Kanbar et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F(U)$, $G(U)$, $S(U)$ | $u$, $f$, $g$, $S$ | conserved vector, fluxes in $x$ and $y$, source |
| $u=(u_1,u_2,u_3)$; $u_x$, $u_y$ (§4) | $v=(v_1,v_2,v_3)$ | velocity |
| $B=(B_1,B_2,B_3)$; $B_x$, $B_y$ (§4) | $B$ | agree |
| $\rho$, $p$, $E$, $\gamma$ | agree | $E$ includes $\frac12\lvert B\rvert^2$ |
| $\Pi_{ij}$, $\Lambda=u\times B$ | total stress, $v\times B$ | see Printed slips |
| $\phi$, $\phi_y=g$ | gravitational potential, $g$ | gravity along $-y$; $g$ is also the $y$-flux, read by context |
| $a$, $b$, $b_i$, $c_f$, $c_s$ | $c$, Alfvén speed, $B_i/\sqrt\rho$, fast and slow speeds | **collision**: registry $a$ is the maximum wave speed |
| $\tilde U$, $\Delta U=U-\tilde U$ | $u_{\mathrm e}$, $\delta u$ (local) | as on the [well-balancing](/properties/well-balancing.md) and [unstaggered central scheme](/methods/unstaggered-central-scheme.md) pages; $\Delta$ kept for steps, $\tilde u$ for the normalised cell average |
| $J_F$ | $A$ | flux Jacobian |
| $\theta$ | $\theta_{\mathrm{MC}}$ (local) | MC limiter parameter, $1<\theta_{\mathrm{MC}}<2$; it is the $\beta$ of $\mathrm{MC}_\beta$ on the [TVD](/definitions/total-variation-diminishing.md) page, renamed here because $\beta$ is the plasma beta; **collision** with the Zhang–Shu $\theta$ |
| $\overline\rho_{i+1/2,j}$, $[[\rho]]_{i+1/2,j}$ | $\{\!\{\rho\}\!\}$, $[\![\rho]\!]$ | two-point averages and jumps, right minus left; agree |
| $C_{i,j}$, $D_{i+1/2,j+1/2}$ | primary cell $I_{i,j}$, dual cell | finite volume, cell averages at nodes |
| $\Omega=-u_xB_y+u_yB_x$ | $\Omega=-v_1B_2+v_2B_1$ (local) | $z$-component of $-v\times B$, as on the concept pages; **collision** with the domain $\Omega$, read by context |
| $\mu$ | $\mu_B$ (local) | vertical field strength, not a viscosity |
| $\kappa_p$, $m_p$, $u_0$, $v_0$ | vortex amplitudes and advection speed (local) | |
| $H$, $\rho_0$, $p_0$, $c$ | scale height, base density and pressure, piston amplitude | |
| $\beta=2p/B^2$ | plasma beta (local) | **collision** with the smoothness indicators $\beta_k$ |
| CFL | $\nu$ | 2D definition not stated |

# Reference list

The preprint prints 23 references, numbered [1]–[23] and sorted alphabetically by first
author. The list is merged complete into the [bibliography](/bibliography.md), with `citedby`
including `kanbar-2022`. The printed duplicates [12]/[13] (Powell 1994) and [19]/[20] (Touma
2010) are kept as distinct items with a note, and [4]/[5] share title and authors under different
venues. [2] has no volume or pages, [8] prints an uncertain volume and page, and [3] and [16]
print "and et al.". No item is unparseable.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–11 (2026-10-22/24). This source is cited on:

* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Hydrostatic equilibrium tests under gravity](/benchmarks/hydrostatic-equilibrium-tests.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Unstaggered central schemes](/methods/unstaggered-central-scheme.md)
* [Well-balancing](/properties/well-balancing.md)
