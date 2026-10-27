---
type: Method
title: "Low-dissipation low-dispersion schemes with shock sensor"
description: "The LD2 scheme pairs an energy-preserving central flux and gradient-extrapolated face values with much-reduced matrix dissipation; LD2C adds a Ducros-weighted shock sensor for compressible hybrid RANS/LES; an optimized sixth-order upwind reconstruction is compared with a second-order energy-preserving central scheme for turbulent kinetic energy budgets."
status: established
aliases: [LD2, LD2C, LD2-Compressible, low-dissipation low-dispersion scheme, Kok flux with JST dissipation, OPT6, optimized upwind scheme, approximate dispersion relation]
tags: [numerical-dissipation, hybrid-rans-les, des, compressible, kinetic-energy-preserving]
timestamp: 2026-10-26T20:48:00Z
---

# Low-dissipation low-dispersion schemes with shock sensor

A **low-dissipation low-dispersion (LD2) scheme** is a second-order
convective discretization for unstructured finite-volume codes, designed for
scale-resolving simulation, in which (i) a central, skew-symmetric
energy-preserving face flux is evaluated with face values extrapolated from
the nodes with a weighted gradient term, which lowers the dispersion error,
and (ii) the artificial (Jameson–Schmidt–Turkel, JST) matrix dissipation that
the central flux needs for stability is reduced far below its RANS level.
The scheme is due to Löwe et al. (2016), as recalled by
[Carlsson et al. (2023)](/sources/carlsson-2023.md), who implement it in the
node-based unstructured solver M-Edge and extend it to compressible flow with
shocks as **LD2C** (LD2-Compressible). The page records their formulation,
the parameter study behind it and its effect in
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

Notation (page-local): $q_i$ the conservative variables at node $i$,
$\boldsymbol d_{ij}$ the node-to-node vector, $c$ the speed of sound,
$\mathcal D_{ij}$ the artificial dissipation flux (the registry's $D_{ij}$ is
the differentiation matrix), $\kappa^{(2)}$ and $\kappa^{(4)}$ the global
second- and fourth-difference coefficients (no relation to the von Kármán
constant, which this page does not use), $d^{(2)}_{ij}$ and $d^{(4)}$ the
local coefficients (Carlsson et al. write $\varepsilon^{(2)}_{ij}$,
$\varepsilon^{(4)}$, renamed here because $\varepsilon$ is the dissipation
rate), and $a$ the extrapolation parameter (Carlsson et al.'s $\alpha$,
renamed because the registry's $\alpha$ is the DG/FV blending factor).

## Formulation

**Semi-discrete form.** On the dual control volume $\Delta V_i$ of node $i$
with $nb_i$ neighbours and face areas $S_{ij}$ (page-local),
$$\Delta V_i\frac{\mathrm dq_i}{\mathrm dt}+\sum_{j=1}^{nb_i}F_{ij}S_{ij}+\sum_{j=1}^{nb_i}G_{ij}S_{ij}=0,\qquad F_{ij}=F^{\mathrm K}_{ij}(q_L,q_R)-\mathcal D_{ij}(q),$$
with $G_{ij}$ the viscous flux and $F^{\mathrm K}_{ij}$ the skew-symmetric
energy-preserving central flux of Kok (Carlsson et al. 2023, §2, Eqs. 1–3).
Time integration is BDF2 with dual time stepping, inner iterations by
low-storage Runge–Kutta with FAS multigrid. The authors state that the Kok
flux "provides no numerical dissipation", which is why the matrix dissipation
is needed on hybrid grids (§2; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

**Face extrapolation (dispersion control).** In LD2 the left and right face
values of velocity and pressure are extrapolated from the nodes with
Green–Gauss gradients (Eq. 4):
$$u_L=u_i+a\,\nabla u_i\cdot\boldsymbol d_{ij},\qquad u_R=u_j-a\,\nabla u_j\cdot\boldsymbol d_{ij},$$
and likewise for $p$. LD2C extrapolates density and speed of sound in the
same way (Eq. 5), which Löwe et al. had omitted, judging the effect small and
testing only subsonic flows (§2.1). The value $a=1/3$ gives a fourth-order
approximation of the derivative, "the theoretically highest order for any"
$a$, on structured meshes; $a=0$ is the plain second-order central scheme
(§2.3; the Taylor expansion is not printed, and no order is claimed on
unstructured meshes). Löwe et al. recommended $a=0.36$; Carlsson et al. use
$1/3$, because their semi-discrete analysis (Fig. 1b) shows small
differences between the two and their earlier LES found little practical
difference among positive values (§2.3).

**Matrix dissipation (dissipation control).** The JST matrix dissipation is
(Eqs. 6–8)
$$\mathcal D_{ij}=\Big|\frac{\partial F}{\partial q}\Big|_{ij}\Big[d^{(2)}_{ij}(q_i-q_j)+d^{(4)}_iL(q_i)-d^{(4)}_jL(q_j)\Big],\qquad d^{(4)}=\max\big[0,\ \kappa^{(4)}-d^{(2)}_{ij}\big],$$
with $L$ the undivided Laplacian, the flux-Jacobian magnitude diagonalized
with a Harten entropy fix that keeps every eigenvalue above 30% of the
spectral radius, and $d^{(4)}_i=d^{(4)}(\lambda_i/2\lambda_{0ij})^{0.3}$ an
eigenvalue scaling (close to Martinelli's) that adds dissipation in the
stretching direction of highly stretched cells (page-local local and face
spectral radii $\lambda_i$, $\lambda_{0ij}$). Typical RANS values
$\kappa^{(4)}\in[1/128,1/64]$ "will severely dissipate resolved
turbulence"; earlier LES of decaying grid turbulence and channel flow placed
the scale-resolving range at $1/512$ to $1/1024$ (§2.2.1). For low Mach
numbers the dissipation is preconditioned (Turkel): $c$ is replaced by
$\tilde c=\tfrac c2\sqrt{(1+\beta_{\mathrm{pc}})^2M^2+4\beta_{\mathrm{pc}}(1-M^2)}$
with $\beta_{\mathrm{pc}}=\min[\max(M^2,K_{\mathrm{pc}}M_\infty^2),1]$,
$K_{\mathrm{pc}}$ typically 1–4 in RANS (Eqs. 9–11; page-local symbols); it
is used in their $M_b=0.15$ channel cases, not at $M_b=1.5$.

**Shock sensors.** The second-difference coefficient is switched by the
Jameson pressure sensor (Eqs. 12–13)
$$d^{(2)}_{ij}=\min\big[\kappa^{(2)}\max(\Psi_i,\Psi_j),\,0.5\big],\qquad \Psi_i=\frac{\big|\sum_{k}(p_i-p_k)\big|}{\sum_k(p_i+p_k)},$$
the cap 0.5 making the scheme first-order upwind at shocks. Because the
Ducros factor
$$\Phi_i=\frac{(\nabla\cdot\boldsymbol u)^2}{(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2+10^{-30}}$$
alone cannot separate shocks from small dilatations and activates wherever
vorticity is negligible, LD2C multiplies the two,
$d^{(2)}_{ij}=\min[\kappa^{(2)}\max(\Psi_i\Phi_i,\Psi_j\Phi_j),0.5]$, which
the authors state distinguishes shocks from compressible turbulence
(Eqs. 14–15; page-local $\Psi_i$, $\Phi_i$).

**Parameter sets** (Carlsson et al. 2023, Table 1):

| Scheme | $\kappa^{(2)}$ | sensor | $\kappa^{(4)}$ | $a$ on $u,p$ | $a$ on $\rho,c$ |
|---|---|---|---|---|---|
| Reference (RANS practice) | 5 | $\Psi_i$ | 1/128 | 0 | 0 |
| LD2 (Probst et al., incompressible) | 0 | none | 1/1024 | 1/3 | 0 |
| LD2C | 5 | $\Psi_i\Phi_i$ | 1/512 | 1/3 | 1/3 |

## Calibration and tests

- **Sod shock tube** (200 points, $\Delta x=0.005$ m, $\tilde t=0.2$;
  $\kappa^{(2)}\in\{0.5,1,2.5,5\}$; §4.1, Fig. 2). Extrapolating $p$ and $u$
  only (LD2) lowers the peak oscillation at the shock but not at the contact
  discontinuity; adding $\rho$ and $c$ (LD2C) with $\kappa^{(2)}=5$ removes
  the oscillations upstream of the shock and "significantly" mitigates the
  contact peak, so $\kappa^{(2)}=5$ is adopted. With the Ducros-weighted
  sensor the results are similar (not shown). For this test only the sensor
  is the maximum of the pressure and density forms (Eq. 22).
- **Decaying isotropic turbulence** (Comte-Bellot–Corrsin experiment,
  $2\pi$ box, $32^3$, $64^3$, $128^3$, $M_t=0.1$, SA- and SST-based LES;
  §4.2, Fig. 3; see [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).
  The reference scheme gives too steep a spectral decay at high wavenumbers on
  all three grids; LD2 with $\kappa^{(4)}=1/512$ or $1/1024$ matches the
  experimental spectra, $1/512$ being slightly more dissipative. With LD2 the
  [DES](/methods/detached-eddy-simulation.md) constants work without
  recalibration ($C_{DES}=0.65$ for SA, $0.61$ for the SST $k$-$\varepsilon$
  branch; $0.78$ for the $k$-$\omega$ branch gives nearly identical results,
  not shown). The authors conclude that the convective numerical dissipation
  dominates the decay of turbulent kinetic energy, controlled by the
  preconditioning and by $\kappa^{(4)}$ "in the range of 1/512 or smaller" (§5).
- **Channel flow, SST-IDDES** ($2\pi\delta\times2\delta\times\pi\delta$,
  $64\times(75$–$132)\times64$ nodes, first node $y^+\approx0.5$; $M_b=0.15$ at
  $Re_\tau=395$, 2400, 18 000 and $M_b=1.5$ at $Re_\tau=500$, 1015, 5000;
  §4.3, Table 2, Figs. 4–6; see [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).
  LD2 and LD2C agree "excellently" with DNS for the mean velocity and the
  total (modelled plus resolved) stresses at $Re_\tau=395$; at $Re_\tau=2400$
  and 18 000 only a small [log-layer mismatch](/definitions/log-layer-mismatch.md)
  appears at the RANS–LES interface ($y^+\approx200$ and $\approx2000$),
  whereas the reference scheme shows a significant mismatch at every Reynolds
  number, correct in the RANS region and failing "as soon as the model
  switches to LES due to adding to[o] much numerical dissipation". Switching
  on $\kappa^{(2)}=5$ in the low-speed channel verifies that the shock term
  turns itself off. In the supersonic channel (isothermal walls,
  Trettel–Larsson transformation; see
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md))
  LD2/LD2C profiles agree with the DNS of Modesti & Pirozzoli at
  $Re_\tau=500$ and 1015 and follow Reichardt's law; the Reynolds stresses are
  captured less well than at $M_b=0.15$ and the streamwise peak is
  under-predicted, improved by doubling $n_x$ and $n_z$.
- **Supersonic axisymmetric base flow** (Herrin–Dutton, $M_\infty=2.46$,
  $Re_R=1.632\times10^6$ on the base radius $R$; SA-DDES with the
  shear-layer-adapted length scale; grids of 1.82, 2.06 and 8.51 million
  cells; §4.4, Figs. 7–10). With that length scale the onset of resolved
  turbulence in the initial shear layer is governed mainly by numerical
  dissipation and grid resolution: the reference scheme delays it and shows
  azimuthally coherent Kelvin–Helmholtz structures, while LD2C unlocks the
  instability, and LD2C on the coarsest grid shows a small-scale content
  comparable to the reference scheme on the finest. Reattachment moves from
  $x/R\approx4.0$ (reference, coarse grid) and $\approx3.0$ (finer grids) to
  $\approx2.7$ with LD2C, against 2.67 measured, and the turbulent shear stress
  at $x/R=1.57$ improves; but the base pressure becomes wavy and
  under-predicted (experiment flat near $C_p=-0.102$), as in earlier ZDES and
  SA-DDES studies, so "improved numerics in the initial shear layer does not
  produce a better prediction of the base pressure profile".

## Position on dissipation

Carlsson et al. (2023, §2.3) argue that the dissipation added to a
scale-resolving simulation should ideally be only that of the subgrid model,
which is the opposite premise of [implicit LES](/definitions/implicit-les.md);
the page on [numerical dissipation](/properties/numerical-dissipation.md)
collects both positions. Their channel results tie the log-layer mismatch of
IDDES at the [hybrid RANS/LES](/definitions/hybrid-rans-les.md) interface to
the numerical dissipation of the convective scheme (§4.3). The shear-layer-adapted
length scale used in the base flow is described on
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

## Related low-dissipation strategies

The LD2/LD2C design (a non-dissipative central flux plus a sensor-switched,
much-reduced artificial dissipation) is one answer to the stabilization of
central schemes; [Bernades et al. (2023)](/sources/bernades-2023.md) compare
others for real-gas (transcritical) flow, on second-order centred
differences (§3.2, Table 2; §4):

- **Implicit compact filtering** of the divergence form, the fourth-order
  filter of Lele and of Visbal & Gaitonde with $\alpha_{\mathrm{cf}}=0.495$
  (page-local filter parameter, not the modal-filter strength $\alpha_f$ of
  registry §11) applied to every conservative variable at every
  Runge–Kutta stage (Eq. 29): it "does not suppress" the spurious pressure
  oscillations at a real-gas density interface (§4.1.2), and filtering is
  cited as able to amplify them through thermodynamic non-linearities (§1);
- a **Ducros-sensor hybrid** of a kinetic-energy-preserving split form and
  an HLLC upwind flux, whose sensor is "mostly activated by the
  oscillations" in an ideal-gas density wave (§4.1.1);
- a non-dissipative scheme that removes the cause instead, by
  [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md),
  which keeps the runs stable with no artificial dissipation (§4.2).

**Optimized high-order upwind reconstruction.**
[Wang et al. (2024)](/sources/wang-2024.md) take the opposite route to LD2:
instead of a central flux with minimal added dissipation, a
dispersion-optimized upwind reconstruction whose dissipation is kept. Their
OPT6 is the linear part of the OMP6 scheme of Li et al. (as recalled), a
cell-centred eight-point reconstruction of the left interface state with
two free parameters, $a_{\mathrm o}$ and $b_{\mathrm o}$ (page-local), set
to 0 and 0.001 as Li et al. recommend, the two interface states combined by
a Roe flux (§2.4, Eqs. 12–13). With $a_{\mathrm o}=b_{\mathrm o}=0$ the
stencil reduces to the symmetric sixth-order interpolation
$\tfrac1{60}(1,-8,37,37,-8,1)$ and $b_{\mathrm o}$ adds the upwind
dissipation *(compiler check, not in the sources)*. Its comparison scheme,
KGP2, is the second-order kinetic-energy-preserving split form (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

Wang et al. characterize both by Pirozzoli's approximate dispersion
relation, the modified wavenumber whose real part measures dispersion and
imaginary part dissipation, reporting the largest accurately resolved
wavenumber and the points per wavelength it implies (§2.5, Fig. 1,
Table 1; the tolerance is not stated):

| Scheme | dispersion: $k_{\max}\Delta x$, points per wavelength | dissipation: $k_{\max}\Delta x$, points per wavelength |
|---|---|---|
| KGP2 (central, second order) | 0.48, 14 ("poor") | $\pi$, 2 ("perfect") |
| OPT6 (upwind, sixth order) | 1.65, 4 ("good") | 1.15, 6 ("good") |

($k_{\max}$ the largest resolved wavenumber, page-local.) In WALE LES of
[channel flow](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=180$,
$M_b=0.2$ ($128\times66\times128$ cells, $\Delta x^+\approx9$,
$\Delta z^+\approx4.5$) both give the same mean velocity, while OPT6 is
closer to DNS at the Reynolds-shear-stress peak and in the budget of the
turbulent kinetic energy, "especially for the dissipation term" (§3.2,
Figs. 3–4). On the [periodic hill](/benchmarks/periodic-hill.md) at
$Re_b=10\,595$, $M=0.2$, first-order statistics are grid-insensitive and
second-order ones and budget terms are not; OPT6 agrees with the reference
even on $48^3$, whereas KGP2 shows a grid-convergence trend (separation at
$x/H=0.26$, 0.24, 0.20, 0.20 on $48^3$ to $196\times128\times186$, against
0.20 in the DNS of Krank et al.) (§3.3, Table 2, Figs. 5–6). The authors
recommend high-order upwind schemes for budget analysis and use OPT6 for an
SA-based [DDES](/methods/detached-eddy-simulation.md) of the 30P30N
three-element airfoil ($M_\infty=0.17$, $Re=1.7\times10^6$, about 27 million
cells), in agreement with measured pressure distributions and slat-cove
spectra (§4–5). They use a nonzero sum of the budget terms as an indicator
of insufficient resolution (§3.3, §4). The central scheme compared is
second order and the upwind one sixth order, and no high-order central
scheme is tested (§2.3–2.4).

**A nonlinear route instead of optimized linear coefficients.**
[Luo & Wu (2021)](/sources/luo-2021-b.md), §6, contrast one route to
high resolution, optimizing the coefficients of a linear scheme (Tam & Webb's
dispersion-relation-preserving schemes, optimized WENO of Wang & Chen, as
recalled), with designing the nonlinear weights of a WENO scheme so that the
least smooth substencil is weighted above its ideal value, which offsets
part of the dissipation of the underlying linear scheme. They assess it with
the same approximate dispersion relation of Pirozzoli, computed numerically
for the nonlinear scheme, whose imaginary part turns positive (negative
dissipation) for an over-strong weighting (§3.1, Fig. 1). Their fifth-order
WENO-Z+M is reported better than the linear fifth-order upwind scheme over
"a much broader wavenumber range" (§4, Fig. 4); its formulation and the
shock tests, none of them turbulent, are on
[WENO and hybrid schemes](/methods/weno-scheme.md).

Bernades et al. distinguish *numerical* dissipation (an undesired property
of the method) from *artificial* dissipation (deliberately added) (§1,
footnote 1); in these terms the JST matrix dissipation of LD2 and LD2C is
artificial dissipation *(compiler check, not in the sources)*.

## Qualifications

- The conclusion (§5) credits the Ducros-weighted sensor with better resolved
  shear stress and grey-area mitigation "compared to a standard scheme using
  the sensor formulation by Jameson"; in the base flow, however, the
  reference scheme and LD2C also differ in $\kappa^{(4)}$ and in $a$, so the
  paper does not isolate the sensor's share *(compiler check, not in the
  sources)*.
- "Excellent" resolved stresses are claimed in §5 for $Re_\tau=395$, 2400 and
  18 000, but stresses are plotted only for $Re_\tau=395$.
- The recommended range is printed as "1/512 to 1/1024" (§2.2.1) and "1/512
  or smaller" (§5).
- **Two answers to one problem.** Carlsson et al. (2023) reduce the
  artificial dissipation added to an energy-preserving central flux so that
  only the subgrid model dissipates; Wang et al. (2024) keep the
  dissipation of a dispersion-optimized upwind scheme and find it better
  than a non-dissipative second-order central scheme for turbulent kinetic
  energy budgets. Carlsson et al. vary the added dissipation of one
  central scheme, against the RANS-level coefficient $1/128$ of their
  solver; Wang et al. vary order and dissipation together (second-order
  central against sixth-order upwind). Neither runs the other's
  comparison, so the entry is recorded as a qualification.
- Wang et al. (2024, §2.3) state that the KGP form follows from the
  general combination of five convective forms with "$\xi=1/2$,
  $\alpha=\beta=\delta=1/4$, and $\varepsilon=0$"; $\xi$ is not defined and
  the weight of the $C^u$ form is not given. In the one-parameter family
  recalled by Bernades et al. (2023) the KGP form is the parameter value
  $\tfrac12$ and carries weight $\tfrac14$ on that form too
  *(compiler check, not in the sources)*; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).
- Printed slips: §5 attributes LD2 to "Löwe et al. [28]", while ref. [28] is
  Probst et al. and LD2 is Löwe et al. [10] elsewhere; §4.3 cites Fig. 4(b) for
  both $Re_\tau=2400$ and 18 000 (the latter is Fig. 4(c)); the text refers to
  the Ducros sensor as Eq. (14) in §4.4 and as Eq. (15) in §4.1 (Eq. 14 is the
  factor, Eq. 15 the sensor used).

# Citations

- [Bernades et al. (2023)](/sources/bernades-2023.md) — §1, footnote 1 (numerical against artificial dissipation; filtering); §3.2, Eq. (29), Table 2 (compact filter, hybrid); §4.1–4.2.
- [Wang et al. (2024)](/sources/wang-2024.md) — §2.3–2.5, Eqs. (5)–(13), Fig. 1, Table 1 (split forms, OPT6, Roe flux, approximate dispersion relation); §3.2, Figs. 3–4 (channel); §3.3, Table 2, Figs. 5–6 (periodic hill); §4–5 (30P30N DDES, recommendation).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §3.1, Fig. 1; §4, Fig. 4 (approximate dispersion relation of WENO-Z+ and WENO-Z+M against UD5); §6 (nonlinear weighting against optimized linear coefficients).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2, Eqs. (1)–(8) (M-Edge discretization, Kok flux, extrapolation, JST dissipation); §2.2.2, Eqs. (9)–(11) (preconditioning); §2.2.3, Eqs. (12)–(15) (Jameson and Ducros sensors); §2.3, Fig. 1 (dispersion/dissipation analysis, choice of $a$); Table 1; §4.1, Eq. (22), Fig. 2 (Sod); §4.2, Fig. 3 (decaying isotropic turbulence); §4.3, Table 2, Figs. 4–6 (channel); §4.4, Figs. 7–10 (base flow); §5.
