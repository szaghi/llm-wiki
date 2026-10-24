---
type: Source
title: "Bhoriya et al. (2023) — High-order finite-difference entropy stable schemes for two-fluid relativistic plasma flow equations"
description: "Semi-discrete entropy-stable finite-difference schemes of orders two to four for the two-fluid relativistic plasma equations: closed-form entropy-conservative fluxes for 3D-velocity relativistic hydrodynamics, TeCNO dissipation on ENO-reconstructed scaled entropy variables, entropy-neutral Lorentz sources, and ARK-IMEX stepping for the stiff sources."
resource: "doi:10.1016/j.jcp.2023.112207"
source_kind: paper
authors: [Bhoriya D., Kumar H., Chandrashekar P.]
year: 2023
venue: "J. Comput. Phys. 488:112207"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Bhoriya_High-order_finite-difference_entropy_stable_schemes_for_two-.pdf"
tags: [entropy-stable, relativistic, finite-difference, imex, stiff-source, mhd]
timestamp: 2026-10-23T15:19:00Z
---

# Summary

The paper builds semi-discrete [entropy-stable](/properties/entropy-stability.md)
finite-difference schemes of arbitrary order for the two-fluid relativistic
plasma equations. Ions and electrons each obey the equations of
[special relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
with a 3D velocity, and they are coupled to Maxwell's equations in the
divergence-cleaning ("perfectly hyperbolic") form of Munz et al. The
18-component flux splits into three independent blocks (ions, electrons,
Maxwell), which interact only through the Lorentz-force sources. The paper
proves that smooth solutions transport each species' specific entropy, and that
the sources are entropy-neutral: their product with the entropy variables
vanishes. Entropy stability therefore reduces to the two fluid blocks.

For each fluid block the authors give a closed-form two-point
[entropy-conservative flux](/methods/entropy-conservative-flux.md) for 3D
velocities. It is derived by jump matching with
[logarithmic means](/operators/logarithmic-mean.md) and raised to fourth order
by the LeFloch–Mercier–Rohde combination. The entropy-stable flux adds a
Rusanov-type dissipation $\tilde R\Lambda\tilde R^\top$ with Barth-scaled
eigenvectors, which acts on jumps of ENO-reconstructed scaled entropy variables
([TeCNO](/methods/tecno-scheme.md)). The Maxwell block uses a Rusanov flux with
minmod or [WENO](/methods/weno-js-reconstruction.md) reconstruction. Time
stepping is explicit [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) of orders
2–4, or [ARK-IMEX](/methods/imex-runge-kutta.md) with implicit sources (Pareschi–Russo
second order, Kennedy–Carpenter third and fourth order). The implicit step is a
local $18\times18$ Newton solve per point.

Tests: a forced smooth solution (orders about 2, 3 and 4); a relativistic
two-fluid [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) with finite
skin depth, where IMEX is up to about 34 times faster than explicit stepping in
the stiffest case; a resistive self-similar current sheet; and in 2D the
relativistic [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), a
two-fluid [blast wave](/benchmarks/mhd-blast-wave.md) and GEM reconnection. The
[magnetic-field divergence](/properties/divergence-free-magnetic-field.md) is
cleaned hyperbolically and monitored, not controlled further.

# Version read

arXiv preprint arXiv:2210.08568v2 [math.NA], 10 May 2023 (stamp on page 1), in
the authors' LaTeX layout, not the JCP version of record; 44 pages, all read by
text extraction, pp. 8, 9, 15, 16, 30 and 43 also visually. Title and authors
match Crossref; the file prints no DOI. Equation, table and page numbers cited
here are those of the arXiv v2, which can differ from the published article.

# Key claims

Registry notation (see the notation map): species $\mathrm s\in\{\mathrm i,\mathrm e\}$,
Lorentz factor $W_{\mathrm s}$, velocity $v_{\mathrm s}$, entropy
$\eta_{\mathrm s}=-\rho_{\mathrm s}W_{\mathrm s}s_{\mathrm s}/(\gamma_{\mathrm s}-1)$
with $s_{\mathrm s}=\ln(p_{\mathrm s}\rho_{\mathrm s}^{-\gamma_{\mathrm s}})$,
entropy variables $w_{\mathrm s}$, entropy potential $\psi_{\mathrm s}$,
entropy-conservative flux $f^{\mathrm{ec}}$; the Maxwell cleaning potentials are
$\phi_{\mathrm E}$ and $\psi_{\mathrm{GLM}}$.

1. The two-fluid system is hyperbolic on $\{\rho_{\mathrm s}>0,\ p_{\mathrm s}>0,\ \lvert v_{\mathrm s}\rvert<1\}$, with real eigenvalues and a complete set of eigenvectors; for $\gamma_{\mathrm s}\in(1,2]$ the sound speed is below 1 (§3, Lemma 3.1, App. B.1). **Derived** (eigenstructure given explicitly; no separate proof of the lemma)
2. Smooth solutions satisfy $\partial_ts_{\mathrm s}+v_{1,\mathrm s}\partial_xs_{\mathrm s}=0$, hence $\partial_t(\rho_{\mathrm s}W_{\mathrm s}H(s_{\mathrm s}))+\partial_x(\rho_{\mathrm s}W_{\mathrm s}v_{1,\mathrm s}H(s_{\mathrm s}))=0$ for every smooth $H$, and in particular $\partial_t\eta_{\mathrm s}+\partial_xF_{\eta,\mathrm s}=0$, with the Lorentz sources present (Prop. 3.1, Eqs. 5–6; proof App. A, Lemmas A.1–A.2). **Proved**
3. The Lorentz sources do not enter the entropy balance: $w_{\mathrm s}^\top S_{\mathrm s}=0$, because the energy source equals $v_{\mathrm s}$ times the momentum source (proof of Thm 4.2, App. A). **Proved**
4. The flux splits into three independent blocks coupled only by sources, so entropy stability reduces to entropy stability of each fluid block and holds for any discretization of the Maxwell block (§3, Remark 4.3). **Stated** (follows from claims 2–3)
5. Closed-form two-point fluxes $f^{\mathrm{ec}}$ in $x$ and $y$ (Eqs. 18–19), written with arithmetic and logarithmic means of $\rho_{\mathrm s}$, $\rho_{\mathrm s}/p_{\mathrm s}$ and $W_{\mathrm s}v_{\mathrm s}$, satisfy Tadmor's condition $[\![w_{\mathrm s}]\!]\cdot f^{\mathrm{ec}}=[\![\psi_{\mathrm s}]\!]$; they extend the authors' 1D construction (Bhoriya & Kumar 2020) to 3D velocities (§4.1.1). **Derived**
6. The scheme with these fluxes is second-order accurate and entropy conservative (Thm 4.2). **Proved** (via Tadmor's theorem and claim 3)
7. A fourth-order entropy-conservative flux is $\tfrac43f^{\mathrm{ec}}(u_i,u_{i+1})-\tfrac16\big[f^{\mathrm{ec}}(u_{i-1},u_{i+1})+f^{\mathrm{ec}}(u_i,u_{i+2})\big]$ (LeFloch–Mercier–Rohde); only even orders exist, so an odd target order uses the next even one (§4.1.1, Remarks 4.1–4.2). **Stated** (cited)
8. The entropy-stable flux (Eq. 22) uses the dissipation matrix $\mathcal D=\tilde R\Lambda\tilde R^\top$ with $\Lambda=\max_l\lvert\lambda_l\rvert\,I$ (Rusanov type) and entropy-scaled eigenvectors with $\partial u/\partial w=\tilde R\tilde R^\top$, and is close to a Roe-type dissipation on $[\![u]\!]$ (§4.1.2, Eq. 21). **Derived**
9. With ENO reconstruction of the scaled entropy variables $\tilde R^\top w$ (sign property), the scheme with flux (22) satisfies the discrete entropy inequality (12); minmod is used at second order, ENO-3 and ENO-4 at third and fourth order (Thm 4.3). **Proved** (by reference to Fjordholm–Mishra–Tadmor plus claim 3)
10. The Barth scaling $T=\sqrt Y$ of the 3D relativistic block is given in closed form; $Y$ is block-diagonal with a coupled $2\times2$ block in the transverse velocities, whose square root is printed (App. B.2). **Derived**
11. The Maxwell block uses a Rusanov flux with speed 1; reconstruction is minmod at second order, and "third and fifth-order WENO reconstructions" give the third- and fourth-order Maxwell solvers (§4.2). **Stated**
12. The ARK-IMEX implicit step is local: one nonlinear system of 18 equations per point, solved by Newton's method with backtracking line search; no global nonlinear solve (§5.2.1, Conclusion). **Stated**
13. Forced smooth solution ($t=2$, $\gamma=5/3$): the explicit schemes reach orders 1.9382, 3.2101 and 3.8104 at 3200 points, with $L^1$ errors of $\rho_{\mathrm i}$ of 2.04466e-05, 5.12307e-09 and 1.77044e-11 (Table 2). **Shown**
14. The IMEX versions reach 1.9387, 3.2099 and 3.9162 at 3200 points (errors 2.02807e-05, 5.14011e-09, 1.63939e-11), comparable with the explicit schemes (Table 3). **Shown**
15. Two-fluid Brio–Wu with $r_{\mathrm i}=-r_{\mathrm e}=10^3/\sqrt{4\pi}$: at 400 points the profile roughly matches relativistic MHD; at 1600 and 6400 points dispersive two-fluid waves appear; the third- and fourth-order schemes capture the dispersive effects already at 400 points, the fourth-order one better (§6.1.2, Fig. 1). **Shown**
16. Explicit and IMEX schemes of the same order give almost the same entropy decay; higher order dissipates less entropy (Fig. 1c–d). **Shown**
17. In the stiff cases $r_{\mathrm i}=10^4/\sqrt{4\pi}$ and $10^5/\sqrt{4\pi}$ at 400 points the solutions are close to relativistic MHD; the small-scale oscillations are not resolved but the solution stays stable "thanks to the built in entropy stability" (Fig. 2). **Shown**
18. Timings of an MPI code on a 10-core CPU (Table 4): for $r=10^5/\sqrt{4\pi}$ at 800 points, second order takes 413.55 s explicit and 12.11 s IMEX, fourth order 374.54 s and 47.00 s; for $r=10^4/\sqrt{4\pi}$ at 800 points IMEX is faster at second order (14.28 s against 17.90 s) and slower at third (22.14 s against 13.04 s) and fourth order (44.90 s against 37.98 s). **Shown**
19. Self-similar current sheet: all IMEX schemes reproduce the resistive relativistic-MHD profile $B_2=B_0\,\mathrm{erf}(x/(2\sqrt{Dt}))$ at $t=9$ on 400 points, with no visible difference between orders (Fig. 3). **Shown**
20. Relativistic Orszag–Tang ($200\times200$): results comparable with Balsara et al. (2016); entropy decays sharply from $t\approx0.4$, when discontinuities form; the divergence error concentrates at discontinuities and has a similar $L^1$ norm for both orders up to $t=2$ (Figs. 4–7). **Shown**
21. Two-fluid blast wave ($200\times200$, $t=4$, $B_0=0.1$ and $1.0$): stable, comparable with Amano (2016) and Balsara et al. (2016); the fourth-order scheme decays less entropy, and for $B_0=1$ has a smaller $L^1$ divergence error (Figs. 8–13). **Shown**
22. Relativistic GEM reconnection ($512\times256$): solutions at $t=40$, 80 agree with Amano (2016), and the reconnected flux matches Amano's data at $N_x=128,256,512$; the schemes differ only after $t=80$, when the flow is turbulent (Figs. 14–19). **Shown**
23. Entropy solutions of multi-D systems can be non-unique (Chiodaroli–De Lellis–Kreml), but entropy stability remains "one of the few nonlinear stability estimates" (§1). **Stated**
24. Earlier two-fluid relativistic schemes are a third-order explicit scheme with divergence cleaning and divergence-free constraint-preserving schemes; this is presented as the first entropy-stable scheme for the model (§1). **Stated**

# Printed slips

- **ARK3 stiff weights (App. C, Table 5).** With the printed $c=(0,\ 1767732205903/2027836641118,\ 3/5,\ 1)$, the printed $b^{[S]}=(2756255671327/12835298489170,\ -10771552573575/22201958757719,\ 9247589265047/10645013368117,\ 2193209047091/5459859503100)$ gives $\sum_lb_l=1$ and $\sum_lb_lc_l=1/2$ but $\sum_lb_lc_l^2=0.345754\ne1/3$, so the printed row is not a third-order weight vector. *(compiler check, not in the sources: exact rational arithmetic on the printed table.)*
- §6.2, 2D time step printed as $\Delta t=\mathrm{CFL}\cdot\min\{\Delta x/\Lambda^x_{\max}+\Delta y/\Lambda^y_{\max}\}$, which exceeds each 1D limit; the index range reads "$1\le y\le N_y$" for $j$.
- §6.1.2: the skin depth is $10^{-3}/\sqrt{\rho_{\mathrm i}}$ and $\Delta x=0.0025$ at 400 points is said to be "slightly larger than the plasma skin depth in the entire domain"; in the right state ($\rho_{\mathrm i}=0.0625$) that formula gives $4\times10^{-3}>\Delta x$. *(compiler check, not in the sources)*
- §6.2.3, GEM initial data: $B_1=B_0\tan(y/d)$ is singular at $y=\pm\pi d/2$ inside the domain, where pressure balance with the $\mathrm{sech}^2$ profiles needs $\tanh$; $p_{\mathrm e}=-p_{\mathrm i}$ is a negative pressure; $\rho_{\mathrm e}=(m_{\mathrm e}/m_p)n$ uses $m_p$ for the defined $m_{\mathrm i}$; the perturbation amplitude $\psi_0$ is never given.
- §2: "Equations (1i) and (1j) are equations for the correction potentials φ and χ"; the potentials are $\phi$ and $\psi$, $\chi$ being a speed.
- $k_\alpha$ is $\gamma_\alpha/(\gamma_\alpha-1)$ in §2 and $\frac1{\gamma-1}\frac1{\beta^{\ln}_\alpha}+1$ in §4.1.1; $\psi$ is both a cleaning potential and the entropy potential; $\Lambda$ is both the eigenvalue matrix and a resistive-term quantity (Eq. 28).
- §5.1: the SSP-RK loop "For m = 1, …, k + 1" leaves $k$ undefined and does not match the stage counts of Table 1.
- Equations (23), (25) and (26) do not exist (numbering jumps 22, 24, 27).
- §6.1.3 uses $r_{\mathrm i}=-r_{\mathrm e}=10^3$ without the $1/\sqrt{4\pi}$ of the other tests.
- "Orzag-Tang" throughout §6.2.1; "ES-O3-IMEX" in the Figs. 6 and 12 captions against "O3-ES-IMEX" in the text; "mess 512 × 256" (Figs. 14–17); "$E_z=-\sin(2\pi(x)$".

# Notation map

| Bhoriya et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha\in\{i,e\}$ | $\mathrm s\in\{\mathrm i,\mathrm e\}$ (page-local) | species; **$\alpha$ is the DG–FV blending coefficient, $i$ a grid index** |
| $\rho_\alpha$, $\mathbf u_\alpha$, $p_\alpha$ | $\rho_{\mathrm s}$, $v_{\mathrm s}$, $p_{\mathrm s}$ | rest-frame density, 3-velocity, pressure |
| $\Gamma_\alpha$ | $W_{\mathrm s}$ | Lorentz factor, $c=1$ |
| $h_\alpha$, $\gamma_\alpha$, $c_\alpha$ | $h_{\mathrm s}$, $\gamma_{\mathrm s}$, $c_{\mathrm s}$ | specific enthalpy (page-local), ratio of specific heats, sound speed |
| $D_\alpha$, $\mathbf M_\alpha$, $\mathcal E_\alpha$ | kept | conserved density, momentum, energy (with rest mass) |
| $\mathbf U$, $\mathbf f^x$, $\mathbf s$ | $u$, $f$, $S(u)$ | 18 components |
| $\mathbf B$, $\mathbf E$ | $B$, $E_{\mathrm{em}}$ (page-local) | **$E$ is the total energy in the registry** |
| $\phi$, $\psi$, $\chi$, $\kappa$ | $\phi_{\mathrm E}$, $\psi_{\mathrm{GLM}}$, kept | cleaning potentials and speeds (set to 1); **$\kappa$ is the kinetic energy in the registry** |
| $r_\alpha=q_\alpha/m_\alpha$ | $r_{\mathrm s}$ | charge-to-mass ratio; **$r$ is the WENO stencil size in the registry** |
| $s_\alpha$ | $s_{\mathrm s}$ | $\ln(p\rho^{-\gamma})$, as in the registry |
| $\mathcal U_\alpha$, $\mathcal F^d_\alpha$ | $\eta_{\mathrm s}$, $F_{\eta,\mathrm s}$ | convex entropy pair, decay $\le0$ |
| $\mathbf V_\alpha$, $\psi^d_\alpha$ | $w_{\mathrm s}$, $\psi_{\mathrm s}$ | entropy variables and potential ($\psi^x=\rho W v_1$) |
| $\beta_\alpha=\rho_\alpha/p_\alpha$ | written out | **$\beta_k$ is a smoothness indicator in the registry** |
| $[\![a]\!]$, $\bar a$, $a^{\ln}$ | $[\![a]\!]$, $\{\!\{a\}\!\}$, $\{\!\{a\}\!\}_{\log}$ | |
| $\tilde{\mathbf F}$, $\tilde{\mathbf F}^{x,2p}$ | $f^{\mathrm{ec}}$ | entropy-conservative flux of order $2p$ |
| $D^d_\alpha$ | $\mathcal D$ (page-local) | **$D$ is the DG differentiation matrix in the registry** |
| $R^d_\alpha$, $\tilde R^d_\alpha=R^d_\alpha T^d_\alpha$, $Y$ | $R$, $\tilde R$, kept | Barth-scaled eigenvectors, as on the TeCNO page |
| $\Lambda^d_{\alpha k}$, $\Lambda^d_\alpha$ | $\lambda_l$, $\Lambda$ | eigenvalues, Rusanov diagonal |
| $k$ (§4.1.2) | kept | ENO polynomial degree / order |
| $F_{NS}$, $F_S$, $a^{[NS]}_{ml}$, $a^{[S]}_{ml}$, $b_l$, $c_l$ | kept | ARK splitting and Butcher coefficients |
| $\eta$ (resistivity) | $\eta_{\mathrm m}$ (page-local) | **$\eta$ is the entropy in the registry** |
| $\omega_p$, $d_p$ | kept | plasma frequency, skin depth |

# Reference list

49 printed references in numbered style ([1]–[49]), all merged complete into
the [bibliography](/bibliography.md) with `citedby` `bhoriya-2023`. Ref. [1]
prints no page or article number; ref. [42] (Barth 1999) prints truncated
editors; ref. [33] prints a DOI with a "/FIGURES/8" suffix (kept as printed);
ref. [36] prints "(September 2021) (2022)" and is dated 2022. Same-author
same-year pairs are suffixed in printed order (Balsara 2016, Zenitani 2009).
No printed duplicates.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–10 (2026-10-23). This source is cited on:

* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [GLM divergence cleaning](/methods/glm-divergence-cleaning.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [Sign-preserving WENO](/methods/sign-preserving-weno.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
* [TeCNO schemes — entropy-stable reconstruction with the sign property](/methods/tecno-scheme.md)
