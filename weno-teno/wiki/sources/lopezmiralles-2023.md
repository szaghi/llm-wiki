---
type: Source
title: "López-Miralles et al. (2023) — On the application of Jacobian-free Riemann solvers for relativistic radiation magnetohydrodynamics under M1 closure"
description: "Extends the relativistic MHD code Lóstrego to grey M1 radiation transport with an IMEX Runge–Kutta treatment of the stiff radiation–matter coupling, and introduces a Jacobian-free polynomial-viscosity-matrix Riemann solver (PVM-int-8) with an opacity-scaled viscosity, tested against a radiative HLL solver."
resource: "doi:10.1016/j.cpc.2022.108630"
source_kind: paper
authors: [López-Miralles J., Martí J.M., Perucho M.]
year: 2023
venue: "Comput. Phys. Commun. 284:108630"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computer_Physics_Communications_López-Miralles_On_the_application_of_Jacobian-free_Riemann_solvers_for_rela.pdf"
tags: [riemann-solver, relativistic, mhd, imex, finite-volume, stiff-source]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

The paper extends the three-dimensional special-relativistic MHD finite-volume
code Lóstrego to relativistic radiation MHD. It uses the two-moment grey
formulation, with radiation energy density and flux, closed by the M1 Eddington
tensor. The stiff radiation–matter source terms are integrated with an
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) scheme built on the three-stage
SSP-RK3. Each explicit stage is followed by an implicit update of the radiation
fields only: an iterated linearized $4\times4$ solve that conserves total energy
and momentum.

The main contribution is the explicit flux, a Jacobian-free
[polynomial viscosity matrix (PVM) Riemann solver](/methods/polynomial-viscosity-matrix-solver.md)
of Castro, Gallardo and Marquina (2017), applied "for the first time" to
radiation MHD. The solver approximates $\lvert A\rvert$ by the degree-8 "internal"
polynomial approximation of $\lvert x\rvert$ (PVM-int-8). It evaluates the
viscosity term by Horner's rule, with matrix–vector products replaced by finite
differences of fluxes, so no eigenstructure and no separate wave speeds for the
fluid and radiation blocks are needed. Because the scheme over-diffuses in
optically thick cells, the viscosity term is multiplied by
$\min\{1/\tau_L,1/\tau_R,1\}$, where $\tau$ is the cell optical depth. The
competitor is a radiative [HLL](/methods/hll-riemann-solvers.md) solver with
separate block wave speeds and optical-depth speed limiting.

The code also gains [monotonicity-preserving](/methods/monotonicity-preserving-limiter.md)
MP3 and MP5 reconstruction (Suresh & Huynh) and a five-step fourth-order SSP-RK.
On a [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
the observed orders are 1 (Godunov), 2 (PLM), 3 (MP3+RK3, and MP5+RK3) and 5
(MP5+RK4).

The radiation tests are:

- optically thin radiation Riemann problems;
- the four Farris et al. radiative shock tubes;
- an optically thick diffusing pulse;
- 2D and 3D radiative versions of the [magnetized blast wave](/benchmarks/mhd-blast-wave.md);
- single and double shadows.

PVM-int-8 is sharper than Rad-HLL at radiation contacts in the thin limit and
slightly more accurate in the opaque diffusion limit. Radiative runs use PLM with
the van Leer limiter and RK3. The paper reconstructs with PLM and MP and uses no
WENO or TENO.

# Version read

The file is the arXiv preprint arXiv:2212.00370v1 [astro-ph.HE] of 1 Dec 2022
(footer "Preprint submitted to Computer Physics Communications, December 2,
2022"), not the typeset version of record. It has 21 pages, all read, with
pp. 3–9 and 13–14 also read visually because text extraction drops superscripts
("214 cells" is $2^{14}$). Page 1 matches Crossref (title, three authors, order).
Equation, table and section numbers here are those of the preprint.

# Key claims

The source's relativistic symbols are kept where the registry has none; see the
notation map. $W$ is the Lorentz factor.

1. In Minkowski metric and Cartesian coordinates the Rad-RMHD system is a balance law $\partial_tu+\partial_if^{(i)}(u)=S(u)$ with $u=(D,S^j,\tau_e,B^j,E_r,F_r^j)$. Radiation couples to matter only through the sources $S=(0,G^j,G^0,0,-G^0,-G^j)$ (§2.1, Eqs. 1–3, 10). **Stated** (recalled from Melon Fuksman & Mignone 2019)
2. The M1 closure is $P_r^{ij}=D_r^{ij}E_r$, with $D_r^{ij}=\frac{1-\xi}2\delta^{ij}+\frac{3\xi-1}2n^in^j$ and $\xi=(3+4f^2)/(5+2\sqrt{4-3f^2})$, $f=\lvert F_r\rvert/E_r$. It reduces to the Eddington approximation as $f\to0$ and to free streaming as $f\to1$ (§2.2, Eqs. 15–17). **Stated**
3. The radiation Jacobian depends only on $(E_r,F_r)$, so the Jacobian splits into an RMHD block and a radiation block whose wave speeds can be computed independently. Common speeds cause excessive diffusion (§3.2.1, Eq. 26). **Stated**
4. The radiation-block eigenvalues are given analytically by Eqs. (27–30). They tend to $\cos\theta$ as $f\to1$, and to $\lambda_{r2}\to0$, $\lambda_{r1,r3}\to\mp1/\sqrt3$ as $f\to0$ (§3.2.1). **Stated** (cited). The limits follow from Eqs. (17, 27–30) by substitution. *(compiler check, not in the sources)*
5. In optically thick cells the radiation speeds are limited, $\lambda_{r,L}=\max(\lambda_{r1},-4/(3\tau))$ and $\lambda_{r,R}=\min(\lambda_{r3},4/(3\tau))$, with $\tau=\rho W(\kappa_{\mathrm a}+\sigma_s)\Delta x$ (Eq. 31, after Sądowski et al. 2013). **Stated**
6. The radiative HLLC of Melon Fuksman & Mignone (2019) must revert to HLL when the speeds are limited, so it improves Rad-HLL only in optically thin media. The HLLD solver has not been adapted to radiation (§3.2.1). **Stated**
7. PVM-int-$n$ solvers "guarantee the stability conditions needed to ensure the robustness and convergence" and admit a Jacobian-free formulation that uses only flux evaluations and vector operations (§3.2.2). **Stated** (from Castro et al. 2017)
8. With $p_0=1$ and $p_k=\frac12(2p_{k-1}-p_{k-1}^2+x^2)$, the case $k=3$ gives the degree-8 polynomial $p_3=-\frac1{128}x^8+\frac3{32}x^6-\frac{23}{64}x^4+\frac{31}{32}x^2+\frac{39}{128}$, evaluated by Horner's rule in $x^2$ (Eqs. 34–35). **Stated**. The printed coefficients agree with expanding the recursion. *(compiler check, not in the sources)*
9. The upper bound of the spectrum is taken as $\lambda_{\max}=1$ (the speed of light), "reasonable" for radiation transport (§3.2.2). **Stated**
10. The opacity-scaled flux is $\hat f_{i+1/2}\approx\frac12(f(u^-)+f(u^+))-\frac{\beta_\tau}2\,p_3(A)(u^+-u^-)$, with $\beta_\tau=\min\{1/\tau_L,1/\tau_R,1\}$. It removes the excess diffusion in optically thick media. Suppressing the viscosity outright for $\tau>1$ "yields oscillatory solutions" (§3.2.2, Eqs. 37–38). **Shown** (pulse test) for the scaling; **Stated** for the oscillation remark. The authors call the choice of $\beta_\tau$ "somehow arbitrary" (§5).
11. On the circularly polarized Alfvén wave, the $L_1$ error of $v_3$ (the source's $v_z$) after one period converges at first order with Godunov reconstruction (HLL: 0.915669 at $N=256\to512$) and at second order with PLM (MC/HLL 2.024194, van Leer/HLL 2.093994). MinMod generally gives the largest PLM errors (Tables 1–4, Fig. 1). **Shown**
12. With HLLC the Alfvén-wave results "are the same as those obtained in Martí (2015)". HLLD performs like HLLC on smooth solutions (§4.1.1, Tables 2–3). **Shown**
13. MP3+RK3 gives third order with HLLD (2.998231 at the finest pair) and with PVM-int-8 (2.998835) (Tables 3–4). **Shown**
14. MP5+RK3 is limited to third order by the time integrator (HLLD, 3.005290), with errors almost two orders of magnitude below MP3+RK3 ($4.284\times10^{-9}$ against $3.224\times10^{-7}$ at $N=512$) (Table 3, §5). **Shown**
15. MP5 with the five-step fourth-order SSP-RK reaches fifth order (HLLD, orders 4.827224 to 5.046792; error $9.006\times10^{-12}$ at $N=512$, $\nu=0.3$) (Table 3). **Shown**. The paper does not discuss why a fourth-order integrator does not limit the observed order.
16. The PVM-int-8 Alfvén-wave errors are "very similar to those found with HLLC" (Table 4 against Table 2, Fig. 1). **Shown**
17. On the optically thin radiation Riemann problems ($2^8$ zones, first order), both solvers give three waves. PVM-int-8 is sharper than Rad-HLL at the contact in Test 1 and less so in Test 2, and the difference shrinks with PLM (§4.1.2, Fig. 2). **Shown**
18. On the Farris et al. shock tubes with M1, the results are consistent with the literature. In the highly relativistic shock the front drifts at about $1.6\times10^{-4}$ and the maximum $\tilde F_r^x/\tilde E_r$ is about 0.31. M1 smooths the radiation profile at the shock relative to the Eddington approximation (§4.1.3, Figs. 3–6). **Shown** (no overplotted reference)
19. Optically thick pulse with $\sigma_s=5$, 100 and 1000 per cell: PVM-int-8 with $\beta_\tau$ "improves slightly" on Rad-HLL with speed limiting. First-order reconstruction, PVM-int-8 with $\beta_\tau=1$, or Rad-HLL without limiting give "catastrophic diffusive solutions (specially for $\tau>100$)" (§4.1.4, Fig. 7). **Shown** (the catastrophic runs are described, not plotted)
20. "This is the first time to our knowledge that a Riemann solver improves the accuracy of Rad-HLL in the highly optically thick regime ($\tau\gg1$)" (§5). **Stated** (priority claim resting on Fig. 7)
21. Radiative magnetized blast wave:
    - $\kappa_{\mathrm a}=1$ (optically thin): $W_{\max}\approx1.7$, similar to Melon Fuksman & Mignone, with the radiation staying cylindrically symmetric.
    - $\kappa_{\mathrm a}=1000$: an oblate ring with $W_{\max}\approx2.72$. This case needs Rad-HLL, MinMod and $\nu=0.01$ to avoid unphysical states, so it is not run with the new solver.
    - A 3D spherical version runs on $256^3$.

    (§4.2.1, Figs. 8–10). **Shown**
22. M1 reproduces shadows in 2D and 3D. In the double-shadow case it produces a spurious narrow shadow along the axis, a known M1 artefact (§4.2.2, Figs. 11–13). **Shown**
23. From Castro et al. (2017): PVM-Cheb-12 and DOT-Cheb-12 are slightly less diffusive than PVM-int-8, but PVM-int-8 satisfies the stability condition automatically. PVM-int-8 costs about twice HLL in CPU time, mainly because of repeated primitive recovery (§5). **Stated** (cited)
24. Radiation variables are both primitive and conserved, so the radiation block adds no primitive recoveries to the cost of PVM (§5). **Stated** (no timing given)
25. PVM-int-16 gave results identical to PVM-int-8 at higher cost (§5). **Stated** (not shown)
26. The Jacobian-free PVM solver treats the full system with one algorithm, without block decomposition, improves Rad-HLL in both the thin and the thick limit, and is robust across the 1D–3D tests (§5). **Shown** (by the test suite)

# Printed slips

- §2.1, after Eq. 3: "$h^*=1+\epsilon+\gamma/\rho+\lvert b\rvert^2/\rho$". The term $\gamma/\rho$ mixes the adiabatic exponent with specific energies; by the paper's own $p^*=p+\lvert b\rvert^2/2$ it should be $p/\rho$.
- Eq. (19): $U^*_i=U^n_i-\frac1{\Delta x}(\hat F_{i+1/2}-\hat F_{i-1/2})$ lacks the factor $\Delta t$ of Eqs. (18) and (21).
- §3.2.2, algorithm step 6: the loop "for $l=1,\dots,k$" gives $k+1$ applications of $A^2$ and $k+2$ coefficients. Horner's rule for an even polynomial of degree $2^k$ needs $2^{k-1}$ applications and $2^{k-1}+1$ coefficients. The two agree only for $k=3$ (PVM-int-8); for PVM-int-16 ($k=4$), which the paper says it also ran, the printed loop is short. *(compiler check, not in the sources)*
- Eq. (51): the analytic pulse $E_r=A\exp(-x^2/(4D(t+t_0)))((t+t_0)/t_0)^{-1/4}$ does not satisfy the 1D diffusion equation $\partial_tE_r=D\,\partial_x^2E_r$, which requires the exponent $-1/2$. *(compiler check, not in the sources)*
- §4.1.4: a single $t_0\approx4800$ is given for three cases whose diffusion coefficient $D=1/(3(\kappa_{\mathrm a}+\sigma_s))$ differs by a factor 200.
- §4.1.1: "from N=16 to N=512 zones", while Tables 1–4 start at $N=8$.
- §4.1.3, radiation-pressure-dominated shock: "radiation is transported from the left to the right ($\tilde F_r^x<0$)". A negative flux transports radiation leftwards, as the radiation penetrating "up to $x\sim-12$" confirms.
- Fig. 6 caption names the non-relativistic strong shock (that is Fig. 3, $t=5000$, 800 zones); the text assigns Fig. 6 to the radiation-pressure-dominated shock.
- The five-step fourth-order RK is attributed to "Balsara, 2001" in §1 and late in §5, and to "Balsara, 2017" in §4.1.1 and early in §5.
- §4.2.2, double shadow: $F_r^x=0.93cE_r$, $F_r^y=-0.37cE_r$ gives $\lvert F_r\rvert/(cE_r)=1.0009>1$, marginally beyond the paper's own limit $\lvert F_r\rvert\le E_r$ (Eq. 23). *(compiler check, not in the sources)*
- "Martí (2015)" is ambiguous: the reference list holds two single-author Martí 2015 works (CPC and MNRAS) without suffixes.
- Typography: "Dumber-Osher-Toro (DOT)" for Dumbser; "Runka-Kutta" (Table 1 caption); "authours", "difussive", "Ackowledgements".

# Notation map

| López-Miralles et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $V$ | $u$; primitive vector | cell averages; reconstruction on primitives |
| $F^i$, $\hat F_{i+1/2}$ | $f^{(i)}$, $\hat f_{i+1/2}$ | physical and numerical fluxes |
| $U_L$, $U_R$; $F_L$, $F_R$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$; $f(u^\mp)$ | interface states |
| $S$ (source vector) | $S(u)$ | **$S^j$ is also the momentum density** |
| $v^j$ ($v_x,v_y,v_z$) | $v$, components $v_1,v_2,v_3$ | three-velocity |
| $W$ | $W$ | Lorentz factor; agrees |
| $D$, $\tau_e$, $B^j$ | kept | relativistic density, energy minus rest mass, magnetic field |
| $\epsilon$ | kept locally (specific internal energy) | **also the finite-difference step $10^{-8}$; collides with the WENO $\epsilon$** |
| $E_r$, $F_r^i$, $P_r^{ij}$, $D_r^{ij}$, $\xi$, $f$ | kept | radiation moments and M1 closure; **$E_r$ is not the gas $E$; $f$ is the reduced flux, not a flux; $\xi$ is not the TENO-A $\xi_{\mathrm A}$** |
| $\kappa$, $\sigma_s$ | $\kappa_{\mathrm a}$, $\sigma_s$ | absorption and scattering coefficients; **$\kappa$ is the kinetic energy in the registry** |
| $\tau$ | $\tau$ (cell optical depth), local | **$\tau$ is the WENO-Z global indicator in the registry** |
| $\lambda_L$, $\lambda_R$ | $s^-$, $s^+$ | HLL speed estimates |
| $\lambda_{r1,r2,r3}$, $\zeta$, $\theta$ | kept | radiation eigenvalues, auxiliary function, flux–normal angle; **$\zeta$ and $\theta$ collide with registry symbols** |
| $A_{i+1/2}$, $Q_{i+1/2}$ | $A$ (at $u_m=\frac12(u^-+u^+)$), viscosity matrix | Roe: $Q=\lvert A\rvert$ |
| $p_k(x)$, $\alpha_0,\dots,\alpha_4$ | kept | internal polynomial and Horner coefficients; **$\alpha_l$ collides with $\alpha_k$** |
| $\beta$ (Eq. 38) | $\beta_\tau$ | opacity scaling; **not a smoothness indicator** |
| $L(U)$ | $\mathcal L(u)$ | explicit spatial operator |
| CFL | $\nu$ | 0.3 by default |
| RK3, RK4 | three-stage SSP-RK3; five-step fourth-order SSP-RK | |

# Reference list

There are 91 printed references in alphabetical author–year style. All are
parsed and merged complete into the [bibliography](/bibliography.md) with
`citedby` `lopezmiralles-2023`. Same-author same-year works take the keys of the merged bibliography:
`marti-2015` (Martí & Müller, Living Rev.), `marti-2015-b` (Martí, CPC 191) and
`marti-2015-c` (Martí, MNRAS 452); `takahashi-2013` (Takahashi et al., ApJ 764) and
`takahashi-2013-c` (Takahashi & Ohsuga, ApJ 772), `takahashi-2013-b` being a
different work cited elsewhere. Two arXiv-only items (Audit et al.
2002, Sekora & Stone 2009) are kept in preprint form. Two books print no
publisher. The Takahashi et al. entry spans two pages and is parsed in full. No
printed duplicates were found.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunks 6–8 (2026-10-23). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Monotonicity-preserving (MP) limiter](/methods/monotonicity-preserving-limiter.md)
* [Polynomial viscosity matrix (PVM) Riemann solver](/methods/polynomial-viscosity-matrix-solver.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
