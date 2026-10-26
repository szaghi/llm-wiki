---
type: Source
title: "Cheylan et al. (2023) — Analysis of the immersed boundary method for turbulent fluid-structure interaction with Lattice Boltzmann method"
description: "Studies the Lagrangian weight of direct-forcing immersed boundaries coupled to the lattice Boltzmann solver ProLB, proposes an explicit weight that needs no linear solve, gives guidelines on grid, time step, kernel and marker spacing, and applies the coupling to fluid–structure cases up to a shear-improved Smagorinsky LES at Re = 10 000."
resource: "doi:10.1016/j.jcp.2023.112418"
source_kind: paper
authors: [Cheylan I., Fringand T., Jacob J., Favier J.]
year: 2023
venue: "J. Comput. Phys. 492:112418"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Cheylan_Analysis_of_the_immersed_boundary_method_for_turbulent_fluid.pdf"
tags: [immersed-boundary, lattice-boltzmann, fluid-structure-interaction, les]
timestamp: 2026-10-26T07:42:00Z
---

# Summary

Cheylan et al. (2023) couple the lattice Boltzmann solver
[ProLB](/software/prolb.md) (D3Q19 lattice, hybrid recursive regularized
collision, Guo forcing; see [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md))
with the finite-element structural solver Calculix through a direct-forcing
[immersed boundary method](/methods/immersed-boundary-method.md) and an
explicit sequential staggered coupling. The paper is about fluid–structure
interaction and immersed-boundary numerics; turbulence enters only in its
last case.

The subject is the Lagrangian weight $W_k$, the missing volume element of
each marker in the spreading of the boundary force to the Eulerian nodes;
its value decides whether interpolation and spreading are reciprocal, and
hence the boundary slip error. Three computations are compared: the linear
system $AW=1$ (direct inversion or BiCGSTAB, after Pinelli et al. 2010 and
Favier et al. 2014), the analytical correction of Gsell et al. (2019), and
a new explicit expression from a Taylor expansion of the reciprocity
condition that sums over neighbouring markers and needs no linear solve.
A parametric study on the laminar cylinder at $Re=100$ gives guidelines
(fine grid and small time step, the slip error scaling with the Courant
number; a narrow kernel; marker spacing $0.8<\Delta s/\Delta x<1.2$; a
crash below $\Delta s/\Delta x=0.785$ with the weight applied). In a
Poiseuille channel the weight cuts the mass-flow error by about three; in
a three-dimensional flapping flag the force histories agree better with the
literature with the weight than without.

The last case is the turbulent benchmark of Breuer et al.: an elastic beam
behind a fixed cylinder at $Re=10\,000$ and solid-to-fluid density ratio 1,
computed as [large-eddy simulation](/definitions/large-eddy-simulation.md)
with the shear-improved variant (Lévêque et al. 2007) of the
[Smagorinsky model](/methods/smagorinsky-model.md), whose eddy viscosity
enters the lattice Boltzmann relaxation time. The Strouhal numbers 0.185
and 0.101 compare with 0.175 and 0.103 of Breuer et al. (2012).

# Version read

Version of record (Elsevier; received 9 September 2022, revised 3 June
2023, accepted 5 August 2023, online 11 August 2023), 25 pages numbered
1–25 without the article-number running header, all read, pp. 1 and 3–22
also visually. Page-1 title, authors and order match the metadata above;
no identity issue. Section, equation, table and figure numbers on this
page are those of this version.

# Key claims

Page-local symbols: $X_k$ Lagrangian marker $k$, $\boldsymbol x_j$ Eulerian
node $j$, $\delta_h$ the regularized discrete delta kernel (the source's
$\delta$), $W_k$ the non-dimensional Lagrangian weight (divided by $\Delta x^3$),
$A_{kl}=\sum_j\delta_h(\boldsymbol x_j-X_k)\delta_h(\boldsymbol x_j-X_l)$ the
kernel-overlap matrix, $\Delta x$ the Eulerian spacing, $\Delta s$ the
marker spacing, $C_{\mathrm{CFL}}=U_0\Delta t/\Delta x$ the Courant number,
$\tau_{\mathrm{LB}}$ the lattice Boltzmann relaxation time, $\overline{C_d}$ the mean
drag coefficient.

1. The boundary slip error of immersed boundaries arises when interpolation and spreading are not reciprocal; a notorious consequence is the over-prediction of aerodynamic forces, although global mass and momentum are conserved (§1). **Stated**
2. $W_k$ is the volume of influence of each marker and cannot be computed directly because a dimension is missing in the surface space; setting $W_k=\Delta x^3$ has no justification (§2.4, Eqs. 16–17). **Stated**
3. Requiring that spreading then interpolating a constant Lagrangian function returns it gives $AW=1$ (a vector of ones) (§2.4.1, Eqs. 18–21; after [10,11]). **Derived** (background)
4. The new expression $W_l=1/\sum_k\sum_j\delta_h(\boldsymbol x_j-X_k)\delta_h(\boldsymbol x_j-X_l)$ follows from Taylor-expanding the transported quantity and $W$ about neighbouring markers and neglecting first-order terms, assuming a fine boundary discretization and a smooth quantity at the wall (§2.4.2, Eqs. 24–28). **Derived** (contribution)
5. It assumes neither a constant normal distance between markers and Eulerian points nor negligible curvature, so its assumptions are "less restrictive than in [38]"; it is claimed usable for any mesh-size ratio and kernel at negligible cost (§2.4.2). **Stated**
6. On the cylinder at $Re=100$ the three weight computations give velocity profiles within 1%; slip errors $10^{-4}$ (explicit weight), $5\times10^{-5}$ (BiCGSTAB), $10^{-5}$ (inverse matrix); relative CPU time 1, 1.6, 2.25 (Table 2, Fig. 5). **Shown**
7. Grid convergence on the cylinder: drag error from 0.52 ($\Delta x=0.08$) to 0.035 ($\Delta x=0.005$), $\overline{C_d}=1.408$ against the reference 1.36 (Table 3). **Shown**
8. A smaller time step reduces the drag error (0.12 to 0.06 at $\Delta x=0.02$); the slip error scales with $C_{\mathrm{CFL}}$, as in [38] (§3.1.1, Table 4). **Shown**
9. Of three kernels the four-point one (Eq. 14) gives the largest error (drag error 0.32 against 0.23); "a flatter function gives a bigger error", a narrow support a sharper boundary (§3.1.2, Table 5). **Shown**
10. The predictive step (fluid advanced without the solid first) gives a more regular intermediate velocity and reduces grid locking, so kernels need not be chosen to suppress it (§2.3, §3.1.2). **Stated**
11. More markers improve accuracy, but with the weight applied the computation crashes when $\Delta s/\Delta x<0.785$ (Table 8), attributed to two markers with near-identical kernels making two rows of the linear system identical (§3.1.3–3.1.4). **Shown**
12. Applying $W_k=2.35$ reduces the drag error from 0.066 to 0.037 at $\Delta x=0.01$ and from 0.066 to 0.044 at $\Delta x=0.02$, against the conclusion of Zhou & Balachandar [19] that the weight has little effect on the Eulerian force (§3.1.4–3.1.5, Table 7). **Shown**
13. Recommended marker spacing $0.8<\Delta s/\Delta x<1.2$: too many markers bring instability, too few fluid leakage (§3.1.5). **Shown**/**Stated**
14. Poiseuille channel at $Re=100$: a local or a mean weight changes the flow-rate error by 0.04% (Table 10), so a constant weight is used; the weight lowers the mass-flow error by about three (0.042 with $W=1$, 0.014 with $W=2$ at $\Delta x=0.0025$; 0.0083 at $\Delta x=0.00125$) (§3.2, Table 11). **Shown**
15. The weight corrects the slip error but not the wall velocity gradient, which the regularized kernels diffuse (as Peng et al. [37]); the near-wall solution is first order in the grid size while the far field is insensitive (as [19]) (§3.2). **Shown**/**Stated**
16. Three-dimensional flapping flag ($Re=200$, mass ratio 1): lift and drag histories agree better with the literature with the analytical weight than without; drag slightly overestimated; trailing-edge displacement agrees "excellently" in frequency and amplitude (§3.3, Figs. 12–14). **Shown** (figures only)
17. The weight's benefit in fluid–structure interaction is quantified as "reduce the error by 20%" (Abstract) and "20%-30%" (§4); no number in §3.3 supports it. **Stated**
18. Lower high-frequency noise in the flag forces than in earlier studies [55,53] is attributed to the collision model, the weighted immersed-boundary formulation and the structural integrator (§3.3). **Stated**
19. A weak explicit coupling suffices for robust and accurate results in the flag and in a high-added-mass case (density ratio 1) (§2.6, §3.3, §3.4). **Shown**
20. Beam behind a cylinder at $Re=10\,000$: the second-order predictor–corrector for the structural velocity gives a less noisy lift spectrum than the first-order prediction $v_n=(d_{n+1}-d_n)/\Delta t$ (§3.4, Fig. 19). **Shown** (qualitative)
21. Strouhal numbers: primary 0.185 against 0.175 (Breuer et al. 2012, fixed case), secondary 0.101 against 0.103 (oscillating case); the primary is linked to vortex shedding, the secondary to the beam oscillation (Table 13, §3.4). **Shown**
22. LES is "not well established in the FSI context"; immersed boundaries avoid the mesh-motion equation of the ALE approach of Breuer et al. [25] (§1). **Stated**

Shear-improved Smagorinsky coupling (§2.7, Eqs. 37–38): the eddy viscosity is the Smagorinsky one with the strain-rate magnitude replaced by $|\bar S|-\mathcal S_{\mathrm{lp}}$, $\mathcal S_{\mathrm{lp}}$ the magnitude of the low-pass time-filtered strain rate, filter width the local $\Delta x$, and $\tau_{\mathrm{LB}}=(\nu+\nu_t)/c_s^2+\Delta t/2$. The source prints $\nu_t=(C_S^2\Delta x)^2(|S|-\mathcal S)$ (see Printed slips); the value of $C_S$ and the normalization of $|S|$ (with or without the factor two) are not printed.

# Printed slips

- **Eq. (12):** "$\int_\Omega(x-x_0)^k\delta(x-x_0)^k\,dx=0$" raises the kernel to the power $k$, while the text speaks of moments of order $k$.
- **Eqs. (14), (15):** the opening parentheses of each branch are never closed.
- **Eq. (37):** "$\nu_t=(C_S^2\Delta x)^2(|S|-\mathcal S)$" squares $C_S$ inside the square, while $C_S$ is called "the Smagorinsky constant".
- **Eq. (40):** "$V(r)=V_{max}(1-\frac{r}{R})$" is linear in $r$, while §3.2 calls the target profile parabolic.
- **Eqs. (25)–(26):** the remainder is written $o(|X_k-X_l|^2)$ after a first-order term.
- **Table 12:** solid density "$10^4$ kg/m³" with fluid density $10^3$ kg/m³, while the table and text give a density ratio of 1; time step "$1.15\times10^4$ s".
- **Instability threshold:** the text says the computation crashes for "$\Delta s/\Delta x<0.785$", while Table 8 lists a crash at $\Delta s/\Delta x=0.785$ itself.
- **Recommended spacing against the best cases** *(compiler check, not in the source)*: the best cylinder cases (Table 9) have $\Delta s/\Delta x=0.00628/0.005=0.01256/0.01=1.256$, outside the recommended $0.8<\Delta s/\Delta x<1.2$.
- **Table entries:** case 4 has $\Delta s=0.01245$ in Table 6 and $0.01256$ in Tables 3 and 7; case 5 drag error 0.24 (Tables 4, 6) and 0.23 (Table 5) for the same $\overline{C_d}=1.68$; case 14 drag error 0.06 (Table 4) and 0.066 (Table 7) for the same $\overline{C_d}=1.45$; Table 8 prints $\Delta s/\Delta x=0.62$ for case 19 ($0.02512/0.04=0.628$, *compiler check, not in the source*). Case 20 prints $St=0.165$ with error 0.055, while $|0.165-0.162|/0.162\approx0.019$ *(compiler check, not in the source)* and Table 6 assigns 0.018 to $St=0.165$ in cases 6 and 12.
- **§3.4:** "fluid-to-density ratio of 1".
- **Citations in the text:** "Qiuxiang et al. [20]" (a given name); "Silva et al. [50]" for a reference whose first author is Lima; "Peng and Luo [5]" and "Luo et al. [5]"; "in 2009, Wu and Shu [9]" against the 2010 reference; "in 2022, Wang et al [24]" against the 2023 reference; Piperno and Farhat [41,42] said to treat aeroacoustics, while the titles concern aeroelasticity and [41] is by Farhat & Lesoinne; "Piperno and Farhat [57,41]" where [57] is Piperno alone. Ref. [42] prints "aroelastic".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f_i$, $f_i^{eq}$, $f_i^{neq}$ | $f_q$, $f^{\mathrm{eq}}_q$, (non-equilibrium part) (page-local, as on [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)) | **collision:** not the body force $f_i$ |
| $c_i$, $\omega_i$, $c_s$ | $\boldsymbol c_q$, $w_q$, $c_s$ (lattice velocities, weights, sound speed; page-local) | **collision:** $\omega_i$ is not the vorticity |
| $\tau$ | $\tau_{\mathrm{LB}}$ (page-local relaxation time, as on the lattice Boltzmann page) | **collision:** not the subgrid stress |
| $\Pi_{\alpha\beta}$ | (second moment of $f_i$) | **collision:** not the SGS energy flux |
| $h_i$, $g$ | (lattice forcing term), (immersed-boundary force density) | |
| $\delta$ | $\delta_h$ (page-local kernel) | **collision:** not the boundary-layer thickness |
| $d$ | (cosine-kernel radius, 1.5) | **collision:** not the wall distance |
| $\kappa=\int\delta(r)^2dr$ | (page-local) | **collision:** not the von Kármán constant |
| $C=U_0\Delta t/\Delta x$; $M$, $C$, $K$ | $C_{\mathrm{CFL}}$; (mass, damping, stiffness matrices) | the source uses $C$ for both |
| $\alpha$, $\beta$, $\gamma$ | (Hilber–Hughes–Taylor parameters) | **collision:** not the DG/FV blending factor, the field-inversion field, the ratio of specific heats |
| $d_n$, $v_n$, $a_n$, $u_n$ | (structural displacement, velocity, acceleration; displacement in Fig. 2) | |
| $\nu_t$, $C_S$, $\lvert S\rvert$, $\mathcal S$ | $\nu_t$, $C_s$, $\lvert\bar S\rvert$, $\mathcal S_{\mathrm{lp}}$ (page-local) | normalization of $\lvert S\rvert$ not printed |
| $\Delta x$ | $\Delta$ (filter width = local spacing) | |
| $h$ (flag thickness) | (page-local) | **collision:** not the element size |
| $E$, $E_s$ | (Young's modulus) | **collision:** not the total energy |
| $\overline{C_d}$, $C_l^{max}$, $St$ | $C_D$ (mean), $C_L$ (peak), $St$ | **collision:** the overbar is a time average |
| $Re$ | $Re_D$ (cylinders), $Re$ on flag length | |
| $Q$ | (flow rate) | |

# Reference list

61 printed references, numbered style ([1]–[61]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Three cited works collide by key with different works of this
archive and take suffixed keys (`huang-2022-b`, `li-2022-f`, `wang-2023-d`): ref. [20] (Q. Huang et al., Phys.
Fluids 2022) is not the Source [huang-2022](/sources/huang-2022.md); ref.
[55] (Li, Oger & Le Touzé, J. Comput. Phys. 449:110786) is not the Source
[li-2022](/sources/li-2022.md); ref. [24] (Wang, Liu & Rajamuni, Proc.
IMechE C 237) is not the archive paper keyed `wang-2023`. Same-author
same-year works are keyed in printed order (Piperno 1997, Jacob 2018, Feng
2019). [18] prints no page or article number, [20] no volume or page, [60]
no book title; [50] is keyed by its printed first author (`lima-2003`). No
item is unparseable.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunk 5. This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [ProLB](/software/prolb.md)
