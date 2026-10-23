---
type: Source
title: "Paula et al. (2023) — A robust high-resolution discrete-equations method for compressible multi-phase flow with accurate interface capturing"
description: "Shows that the high-order discrete-equations method for the Baer–Nunziato model imposes a CFL condition on an arbitrarily small effective cell size, and proposes RDEMIC, an N-phase DEM with cell-average flow channels and pseudo-Riemann fluxes, combined with a multi-dimensional THINC reconstruction time-averaged consistently with SSP-RK3."
resource: "doi:10.1016/j.jcp.2023.112371"
source_kind: paper
authors: [Paula T., Adami S., Adams N.A.]
year: 2023
venue: "J. Comput. Phys. 491:112371"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Paula_A_robust_high-resolution_discrete-equations_method_for_compr.pdf"
tags: [multiphase, interface-capturing, thinc, riemann-solver, finite-volume]
timestamp: 2026-10-23T23:00:00Z
---

# Summary

The paper deals with the
[discrete equations method (DEM)](/methods/discrete-equations-method.md) of
Abgrall and Saurel for the non-equilibrium Baer–Nunziato (seven-equation)
multi-phase model. DEM builds a multi-phase Godunov scheme from single-phase
and two-phase Riemann problems, one per "flow channel" between the phase
sub-volumes of neighbouring cells. The non-conservative interface terms
$p_{\mathrm I}\nabla\phi_k$ and $p_{\mathrm I}v_{\mathrm I}\cdot\nabla\phi_k$
come from the Lagrangian flux across the contact wave, so they need no
closure. With piecewise-constant volume fractions DEM is robust but smears
interfaces strongly. The original high-order extension adds an in-cell
two-phase Riemann problem at the jump of a nonlinear reconstruction. A
wave-path argument shows that the CFL condition must then hold for an
effective cell size that can be arbitrarily small.

The contribution is RDEMIC (robust DEM for interface capturing). The flow
channels are defined from the cell averages of the volume fractions. The
sub-volumes between cell average and reconstructed face value are handled
inside the two-phase channel by a pseudo-Riemann flux and matching exchange
terms. Their Lagrangian parts cancel, so the upwind excess volume is merely
transferred and triggers no wave in a sub-cell volume. The time-step limit
of the piecewise-constant scheme is thus kept. Reverse fluxes handle
non-monotone reconstructions, and the method extends to $N_\phi$
phases (page-local $N_\phi$).

The volume fraction is reconstructed by a genuinely multi-dimensional
[THINC](/methods/thinc-reconstruction.md) function, time-averaged over its
translation by the interface velocity consistently with each stage of
[SSP-RK3](/methods/ssp-runge-kutta.md); the paper calls this
positivity-preserving, without proof. The other variables use
characteristic-wise third-order [WENO-JS](/methods/weno-js-reconstruction.md)
on primitive variables and HLLC with Davis speeds
([HLL solvers](/methods/hll-riemann-solvers.md)) in the code ALPACA. The
tests are [material-interface advection](/benchmarks/material-interface-advection.md)
with 2 and 5 materials, where pressure and velocity are kept to round-off
([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md));
a five-material vortex deformation; smooth-profile convergence;
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md) up
to a 1 TPa water–air shock tube; a spherical
[underwater explosion](/benchmarks/underwater-explosion.md); the
three-material [triple-point problem](/benchmarks/triple-point-problem.md);
and Haas–Sturtevant [shock–bubble interactions](/benchmarks/shock-bubble-interaction.md)
in 2D and 3D, together with an air bubble collapsing in water.

# Version read

The version of record (Elsevier typeset; received 16 Dec 2022, accepted 10
Jul 2023, online 17 Jul 2023), 32 pages: main text pp. 1–26, Appendices A–D
pp. 27–30, references pp. 30–32. Page 1 prints the DOI and matches the
Crossref card. No identity problem.

# Key claims

Notation of the Notation map: phases $k$, $l$, $m$; $\phi_k$ the volume
fraction, $\phi^-_{l,i+1/2}$ and $\phi^+_{l,i+1/2}$ the
left- and right-biased face values (the source's $(\alpha_l)^L_{i+1/2}$, $(\alpha_l)^R_{i+1/2}$), $\bar\phi_{l,i}$ the cell value;
$\delta^C_{lm}$, $\delta^L_{lm}$, $\delta^R_{lm}$
the channel areas and in-cell sub-volumes; $v^*_{lm}$ and $p^*_{lm}$ the
contact velocity and pressure of the $l$–$m$ Riemann problem; $b_{lm}$ the
Lagrangian exchange term and $g$ the unscaled channel fluxes.

1. In the original DEM with a nonlinear volume-fraction reconstruction, the in-cell Riemann problem at $\tilde x_i$ (Eq. (21)) launches waves that reach a cell face or the in-cell contact after only part of $\Delta x$. The CFL condition must hold for the effective cell size $\Delta\tilde x_i=\min(\tilde x_i-x_{i-1/2},\,x_{i+1/2}-\tilde x_i)$ (Eq. (22)) (§3.2, Fig. 3b). **Derived**
2. Piecewise-constant DEM has the CFL condition of single-phase flow, because every wave runs within its phase sub-volume over the full $\Delta x$ (§3.2, Fig. 3a). **Derived**
3. RDEMIC supports a high-order volume-fraction reconstruction without time-step restrictions beyond those of piecewise-constant DEM. The channels come from the cell averages (Eqs. (23)–(24)). In the two-phase channel the pseudo-Riemann flux $g^K_{lm,n}=v^*_{lm}V^K_n+b_{lm}$ and the exchange term combine to $(d_{lm})^L-(f_{lm,m})=-\delta^L_{lm}v^*_{lm}V^L_m$ (Eq. (50)), a uniform transfer that triggers no wave in the upwind sub-volume (§4.3, Fig. 8). **Derived**
4. The net exchange term of the downwind cell does not depend on the downwind contact area: $(d_{lm})^R=(\delta^C_{lm}-\delta^L_{lm}-\delta^R_{lm})b^+_{lm}+\delta^R_{lm}b^+_{lm}=(\delta^C_{lm}-\delta^L_{lm})b^+_{lm}$ (Eq. (31)). **Derived**
5. No extra in-cell Riemann problem is solved, unlike the original high-order DEM: the whole two-phase channel evolves by the single cell-face two-phase Riemann solution (§4.1 item 2; conclusions). **Stated**
6. Item 2 of §4.1 "is the most essential part of our method and is sufficient for most of the occurring interface configurations". The reverse fluxes of item 3 handle non-monotone reconstructions, "especially in multi-dimensional or multi-phase settings", and leave the compression and positivity properties of the reconstruction untouched (end of §4.1). **Stated**
7. RDEMIC holds for any number of phases, with the pairwise contact areas $\delta^K_{lm}=\delta^K_{l\bullet}\delta^K_{\bullet m}/\Delta^K_{\mathrm{tot}}$ (Eq. (43)). This general construction differs from the physics-based prioritization of Chinnayya et al. (§4.2). **Derived**
8. The scaling factors $s_{lm,l}=\delta^C_{lm}/\delta^C_{l\bullet}$ and $s_{lm,m}=\delta^C_{lm}/\delta^C_{\bullet m}$ (Eq. (44)) cannot divide by zero: they are evaluated only when $\delta^C_{lm}>0$, which implies $\delta^C_{l\bullet}>0$ and $\delta^C_{\bullet m}>0$ (§4.2). **Stated**
9. RDEMIC itself does not prevent a loss of positivity when the volume taken from the upwind cell exceeds its content; the classical CFL condition (9) does not handle this. The remedy is the time-averaged THINC reconstruction (end of §4.3, §5.2). **Stated**
10. Time-averaging the THINC function over its translation by $v_{\mathrm I}$ during the step (Eq. (56)) anticipates the interface motion and prevents over-estimated fluxes. For SSP-RK3 the averaging windows are $[0,\Delta t]$, $[-\Delta t,0]$ and $[-\tfrac12\Delta t,\tfrac12\Delta t]$ for the three stages (Eq. (58)). This follows from rewriting stage 2 as $\bar u^{(2)}=\bar u^n+\tfrac14\Delta t\mathcal L(\bar u^n)+\tfrac14\Delta t\mathcal L(\bar u^{(1)})$ (Eq. (57)), a prediction at $t^{n+1/2}$. **Derived**
11. For RK3, positivity is mainly violated in the first stage; the time-averaged volume fractions are used in all three stages for consistency (§5.2). **Stated**
12. To the authors' knowledge, time averaging of the THINC function had not been proposed for multi-stage time integration or applied to compressible flow; earlier works treat incompressible flow with single-step integration and average the upwind volume flux directly (§5.2). **Stated**
13. The THINC function is symmetric only for two phases, so the reconstructed face values are normalized at every face to $\sum_l\phi_l=1$ (§6). This normalization can defeat the positivity-preserving time integration: for the triple-point problem the CFL number had to be lowered to 0.15 (§7.5). **Stated** / **Shown**
14. Characteristic decomposition of the primitive variables reduces spurious oscillations significantly. Since the fluxes are not integrated over the cell faces, the spatial convergence is limited to second order in the lateral direction (§6). **Stated**
15. Removing phases with $\phi_l<10^{-9}$ and rescaling the rest by $(1-\phi_l)^{-1}$ keeps the diffuse interface within about eight cells (for $\beta_{\mathrm T}=3$) and prevents round-off from spreading. The conservation error this introduces is called negligible: it partly cancels on both sides of the interface, and the cutoff is small (§6). **Stated**
16. Interface advection with uniform $p$ and $v$: the maximum relative velocity and pressure errors are $9.4\times10^{-15}$ and $4.7\times10^{-15}$ (1D), $1.1\times10^{-14}$ and $2.3\times10^{-15}$ (2D, 2 materials), $1.2\times10^{-14}$ and $8.4\times10^{-15}$ (2D, 5 materials). The volume errors are $5.4\times10^{-15}$, $1.1\times10^{-8}$ and $3.3\times10^{-9}$ (Table 1, §7.1). **Shown**
17. In the five-phase advection, triple points with an initial angle ratio 2:1:1 are distorted (the angles equilibrate and kink the surrounding phase), while the quadruple point with equal angles is not (§7.1.2, Fig. 10c). **Shown**
18. Smooth advection: the first-order scheme converges at first order, and the "nominally third-order WENO3" only at second order, which "is well-known". The density errors with and without an interface are about the same (§7.3, Fig. 12). **Shown**
19. Weak shock through a water–air interface: the computed interface position matches the theoretical one for every $\beta_{\mathrm T}\in\{0.325,1,3\}$. "In contrast to [64]", the shock front is reproduced without oscillations whatever the interface diffusion. No thermodynamic relaxation is needed, because the two-phase Riemann problem enforces mechanical equilibrium. Only $\beta_{\mathrm T}=0.325$ shows small deviations of the air pressure and velocity on the liquid side (§7.4.1, Figs. 13–14). **Shown**
20. Extreme water–air shock tube (1 TPa): with density ratio 100 the results agree "perfectly" with the reference and the exact solution, and the run also succeeds at density ratio 1000, with CFL 0.4 (§7.4.2, Fig. 15). **Shown**
21. Spherical underwater explosion: the bubble reaches its minimum radius $\approx0.422$ m at $t\approx0.196$ s, in "very good agreement" with a sharp-interface reference at similar resolution; another diffuse-interface reference needs a much higher resolution. The solution converges from above, like the sharp-interface one; the other converges from below (§7.4.3, Fig. 16). **Shown**
22. Triple-point problem with three ideal gases: the wave system and the interface deformation agree "very well" with the high-resolution results of Pan et al. (§7.5, Fig. 18). **Shown**
23. Haas–Sturtevant shock–bubble interaction (Mach 1.22, helium and R22, $8192\times1024$ cells, about 1150 cells per diameter): good agreement with the experiment and numerical references. For R22 the feature trajectories agree excellently, except the late downstream jet position, which exceeds the experiment because the simulation has no viscous dissipation (§7.6, Fig. 22). **Shown**
24. Three-phase helium-core/R22-shell bubble: the global shape agrees with Pelanti & Shyue but shows much finer structure, and differs notably from Billaud Friess & Kokh, as Pelanti & Shyue also noted. In 3D the R22 jet is faster and longer, and the upstream wall moves more slowly than in 2D (§7.6.3–7.6.4, Figs. 23–25). **Shown**
25. HLLC develops shock instabilities in the gas above Mach 2 inside the shocked air bubble in water. HLLC-LM, applied only to the air–air single-phase Riemann problems, removes them, which shows that DEM can combine different Riemann solvers (§7.7, Fig. 26). **Shown**
26. Air bubble in water: the water jet hits the downstream bubble wall about 2.83 μs after impact (3.69 μs absolute), "which agrees perfectly" with the reference (§7.7). **Shown**
27. Default parameters: THINC $\beta_{\mathrm T}=3$, CFL 0.5, WENO3, HLLC with Davis speeds, SSP-RK3, volume-fraction cutoff $10^{-9}$, Newton tolerance $10^{-6}$ for THINC (§6, §7, Appendix B). **Stated**
28. The approximate signed distance $d_i\approx\frac1{2\beta_{\mathrm T}}\log\frac{\bar\phi_i}{1-\bar\phi_i}+d_{\mathrm{corr}}(2\bar\phi_i-1)$, with $d_{\mathrm{corr}}=\frac1{2\beta_{\mathrm T}}\log\frac{\sinh\beta_{\mathrm T}}{\beta_{\mathrm T}}$, has maximum error below $10^{-2}$ for $\beta_{\mathrm T}=3$ (Appendix D, Eqs. (D.2)–(D.3), Fig. D.29). **Shown** ($d_{\mathrm{corr}}=0.20096$ for $\beta_{\mathrm T}=3$ *(compiler check, not in the sources)*.)

# Printed slips

- Eq. (66) writes the interface position as $\sum_i(\bar\alpha_1\bar\alpha_2)_i(x_i-d_i\Delta x)/\sum_i(\bar\alpha_1\bar\alpha_2)_i$, without the normal sign $n_i$ of Eq. (51). From Eq. (51) the interface ($\Phi=\tfrac12$) lies at $x=x_i-d_i\Delta x/n_i$, so Eq. (66) holds as printed only where $n_i=+1$ *(compiler check, not in the sources)*.
- §7.1.2 says the 2D pressure and velocity errors are "on the order of $1\times10^{-14}$", while Table 1 gives pressure errors of $2.3\times10^{-15}$ and $8.4\times10^{-15}$.
- The 2D volume errors of Table 1 ($1.1\times10^{-8}$, $3.3\times10^{-9}$) are about $10^6$ times the 1D one and are not discussed in the text.
- §4.3 ends "We address this problem in the next chapter", meaning §5.
- References: [37], [64] and [77] print no volume, [40] prints "J. Comput. Phys. (2007) 34" with no volume, [63] prints neither volume nor pages, and [51], [70], [71] give only start pages.

# Notation map

| Paula et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $l$, $m$, $n$ | $l$, $m$, $n$ (phase indices) | $n$ is a passive phase; repeated indices do not sum; the [DEM page](/methods/discrete-equations-method.md) writes $k$, $l$ for the pair $l$, $m$ |
| $\alpha_l$, $\bar\alpha_l$ | $\phi_l$, $\bar\phi_l$ | volume fraction; **collision** with the WENO weights $\alpha_k$ |
| $(\alpha_l)^L_{i+1/2}$, $(\alpha_l)^R_{i+1/2}$, $(\alpha_l)^C_i$ | $\phi^-_{l,i+1/2}$, $\phi^+_{l,i+1/2}$, $\bar\phi_{l,i}$ | left- and right-biased face values (registry $u^\mp$), cell value; the source's $(\alpha_l)^R_{i-1/2}$ of §3.1.2 is $\phi^+_{l,i-1/2}$ |
| $\rho_l$, $u_l$, $p_l$, $e_l$, $E_l$ | $\rho_l$, $v_l$, $p_l$, $e_l$, $E_l$ | phasic states; **the source's $u$ is the velocity** |
| $p_{int}$, $u_{int}$ | $p_{\mathrm I}$, $v_{\mathrm I}$ (local) | interface pressure and velocity |
| $\gamma_l$, $p_{\infty,l}$ | $\gamma_l$, $p_{\infty,l}$ | stiffened-gas parameters; agree |
| $U_l$, $F_l$, $B$ | $u_l$, $f_l$, $B_{\mathrm{nc}}$ (local) | phase state, flux, interaction tensor; **collision**: registry $B$ is the SBP boundary matrix |
| $V_l$, $G_l$ | $V_l$, $G_l$ (local) | volume-fraction-specific state and flux; **collision** with the control volumes $V$ and the admissible set $G$ |
| $\hat F$, $\hat D$ | $\hat f$, $\hat D$ | total face flux, total exchange term |
| $g$, $b$; $f=\delta g$, $d=\delta b$ | kept | unscaled channel flux and Lagrangian exchange term; area-scaled versions |
| $u^*_{lm}$, $p^*_{lm}$ | $v^*_{lm}$, $p^*_{lm}$ | contact velocity and pressure, phase $l$ on the left |
| $\delta_{lm}$, $\delta^C_{lm}$, $\delta^L_{lm}$, $\delta^R_{lm}$, $\delta^\square_{lm}$ | kept | contact areas and sub-volumes; **not the TENO flag $\delta_k$** |
| $\Delta^K_l$, $\Delta^K_{total}$, $s_{lm,l}$, $\sigma^\pm_{lm}$ | $\Delta^K_l$, $\Delta^K_{\mathrm{tot}}$, $s_{lm,l}$, $\sigma^\pm_{lm}$ (local) | $N$-phase jumps, scaling factors, direction indicators; **$\sigma$ is the affine scaling in §10** |
| $\Phi$, $\tilde\Phi$ | $u^{\mathrm T}$, $\tilde u^{\mathrm T}$ | THINC profile and its time average |
| $\beta$ | $\beta_{\mathrm T}$ | THINC steepness; never $\beta_k$ |
| $d_i$, $n$, $P(x)$ | kept | normalized interface distance, interface normal, linear surface function |
| $A_g$, $T$, $R$, $s$ | kept | Newton variables of the THINC inversion; **$R$ is the eigenvector matrix in the registry** |
| $L(\bar U)$ | $\mathcal L(\bar u)$ | semi-discrete operator; **collision** with the left-eigenvector matrix $L$ |
| $C_{CFL}$ | $\nu$ | CFL number, with the multi-D form of Eq. (9) |
| $\tilde x_i$, $\Delta\tilde x_i$ | kept | in-cell contact position, effective cell size |

# Reference list

The paper prints 81 references, numbered [1]–[81]. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` including
`paula-2023`. Hoppe et al. 2022 [44] and [61] take suffixes in printed
order. [37], [40], [64] and [77] lack a volume and [63] a volume and pages;
they are recorded as printed. [39] is a conference paper, [42] the ALPACA
software record (DOI 10.14459/2022MP1647482, printed), [46] and [56] books,
[48] and [81] technical reports, [78] a book chapter. Only the paper's own
DOI and that of [42] are printed. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23). This source is cited on:

* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Discrete equations method (DEM)](/methods/discrete-equations-method.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Triple-point problem](/benchmarks/triple-point-problem.md)
* [Underwater explosion](/benchmarks/underwater-explosion.md)
