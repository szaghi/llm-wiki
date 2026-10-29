---
type: Method
title: "Low-dissipation low-dispersion schemes with shock sensor"
description: "The LD2 scheme pairs an energy-preserving central flux with much-reduced matrix dissipation, LD2C adds a Ducros-weighted shock sensor; the page also compares an optimized sixth-order upwind reconstruction with a central scheme for energy budgets, and records stencils, filters and reconstruction weights optimized by spectral objectives."
status: established
aliases: [LD2, LD2C, LD2-Compressible, low-dissipation low-dispersion scheme, Kok flux with JST dissipation, OPT6, optimized upwind scheme, approximate dispersion relation, dispersion-relation-preserving scheme, optimized selective filter, FDo11p, RFo11p]
tags: [numerical-dissipation, hybrid-rans-les, des, compressible, kinetic-energy-preserving]
timestamp: 2026-10-29T05:13:00Z
---

# Low-dissipation low-dispersion schemes with shock sensor

A **low-dissipation low-dispersion (LD2) scheme** is a second-order
convective discretization for unstructured finite-volume codes, designed for
scale-resolving simulation, in which (i) a central, skew-symmetric
energy-preserving face flux is evaluated with face values extrapolated from
the nodes with a weighted gradient term, which lowers the dispersion error,
and (ii) the artificial (Jameson–Schmidt–Turkel, JST) matrix dissipation that
the central flux needs for stability is reduced far below its RANS level.
The scheme is due to Löwe et al. (2016), as cited by
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

**Compact differences with a compact filter in a DNS.** The historical
review of DNS and LES of [Kim & Leonard (2024)](/sources/kim-2024-b.md),
§4.8, records that high-order compact finite-difference schemes (Lele
1992) were developed to minimize numerical dispersion error, for
computational aeroacoustics at NASA Ames. A DNS solver of that family is
the one of [Kang & Lee (2024)](/sources/kang-2024.md), §II.B,
Eqs. (8)–(9), for a Mach 2.9 compression-ramp interaction: the
sixth-order tridiagonal compact first derivative
$\tfrac13\phi'_{i-1}+\phi'_i+\tfrac13\phi'_{i+1}=\tfrac{14}{9}\frac{\phi_{i+1}-\phi_{i-1}}{2h}+\tfrac19\frac{\phi_{i+2}-\phi_{i-2}}{6h}$
on curvilinear grids, with sixth-order one-sided compact closures at the
boundaries, stabilized by an eighth-order tridiagonal compact low-pass
filter of parameter $0.47$ applied to the solution at every final
Runge–Kutta stage (coefficients of Gaitonde & Visbal; a parameter closer
to $0.5$ filters less), lowered to a second-order filter of parameter
$0.49$ at shocks flagged by a Ducros-type sensor, plus a localized
artificial diffusivity (see
[shock sensors](/definitions/shock-sensor.md) and
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).
With the printed filter coefficients the right-hand-side weights sum to
$1+2\times0.47$ and their alternating sum is zero, so the transfer
function is one at zero wavenumber and zero at the grid Nyquist
wavenumber *(compiler check, not in the sources)*.

**Optimized high-order upwind reconstruction.**
[Wang et al. (2024)](/sources/wang-2024.md) take the opposite route to LD2:
instead of a central flux with minimal added dissipation, a
dispersion-optimized upwind reconstruction whose dissipation is kept. Their
OPT6 is the linear part of the OMP6 scheme of Li et al. (as cited there), a
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
$Re_h=10\,595$, $M=0.2$, first-order statistics are grid-insensitive and
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
cited there), with designing the nonlinear weights of a WENO scheme so that the
least smooth substencil is weighted above its ideal value, which offsets
part of the dissipation of the underlying linear scheme. They assess it with
the same approximate dispersion relation of Pirozzoli, computed numerically
for the nonlinear scheme, whose imaginary part turns positive (negative
dissipation) for an over-strong weighting (§3.1, Fig. 1). Their fifth-order
WENO-Z+M is reported better than the linear fifth-order upwind scheme over
"a much broader wavenumber range" (§4, Fig. 4); its formulation and the
shock tests, none of them turbulent, are on
[WENO and hybrid schemes](/methods/weno-scheme.md).

**One parameter between upwind and central.**
[Deng et al. (2022)](/sources/deng-2022.md) make the dissipation of an
upwind-biased finite-volume reconstruction adjustable rather than optimized.
In their $P_nT_m$-BVD-AD schemes, wherever both sides of a face keep the
degree-$n$ polynomial reconstruction, the two face values are replaced by
convex combinations of each other with a parameter $\lambda_{\mathrm{AD}}\in[0.5,1]$
(page-local; §3.2, Eq. 21): $\lambda_{\mathrm{AD}}=1$ is the $(n+1)$-order upwind-biased
scheme, $\lambda_{\mathrm{AD}}=0.5$ makes the two face values equal, so the upwind term of
the Riemann flux vanishes and the scheme becomes the non-dissipative
$(n+2)$-order central interpolation (Remarks 1–2). The new face jump is
$(2\lambda_{\mathrm{AD}}-1)$ times the old one, so $\lambda_{\mathrm{AD}}$ scales the upwind dissipation
term linearly *(compiler check, not in the sources)*. Their approximate
dispersion relation analysis (after Pirozzoli; §4.1, Figs. 1–2) shows that
the ninth-order linear upwind scheme keeps an inherent dissipation despite
its order, that ninth-order mapped WENO (WENO-M) is more dissipative than the
same-order linear scheme at high wavenumbers because the nonlinear
adaptation treats high-wavenumber waves as discontinuities, that the
eighth- and tenth-order $P_6T_3$ and $P_8T_3$ versions at $\lambda_{\mathrm{AD}}=0.5$
retrieve the non-dissipative central schemes (the sixth-order $P_4T_2$
keeps "very small" dissipation at high wavenumbers), and that their
dispersion is almost that of the corresponding central schemes. On sine-wave
advection the three schemes reach $L_1$ orders 5.99, 7.99 and 10.00 at 160
cells, i.e. $n+2$ (Table 1). The authors cite the MDCD schemes (below) as
another way to adjust dissipation without touching optimized dispersion,
and state that $\lambda_{\mathrm{AD}}=0.5$ suits DNS or explicit LES while larger values
supply the dissipation of implicit LES (Remark 2; the $\lambda_{\mathrm{AD}}$ study is on
[implicit LES](/definitions/implicit-les.md), the BVD selection on
[WENO](/methods/weno-scheme.md)).

**Compact nonlinear interpolation for resolution.**
[Ma et al. (2022)](/sources/ma-2022.md) raise the resolution of the weighted
compact nonlinear scheme (WCNS) by replacing its explicit fifth-order
nonlinear interpolation with a seventh-order nonlinear tri-diagonal compact
interpolation on the same five-point stencil (WCNS-T; formulation on
[WENO](/methods/weno-scheme.md)). By Fourier and approximate-dispersion
analysis the resolving ratio (fraction of resolvable wavenumbers) rises from
30.2% to 49.3% (Fourier) and from 28.6% to 39.7% (approximate dispersion
relation), about 1.6 and 1.4 times the resolvable wavenumbers of the
explicit version (§2.3, Table 1, Fig. 1; the error threshold that defines
"resolvable" is not stated); in the shock–entropy-wave interaction
WCNS-T on 200 points matches WCNS-E on 300 (§2.3.1, Fig. 2). They judge
the compact reconstructed WENO (CRWENO) of Ghosh & Baeder good in
dispersion but too dissipative ("the excessive upwind", §1). The scheme
family is on
[weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md).

**Linear weights and a 2% upwind blend on a high-lift airfoil.**
[Wu et al. (2023)](/sources/wu-2023-b.md) measure the effect of
convective-scheme dissipation in hybrid RANS/LES (SATES) of the
[30P30N high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
($Re=1.71\times10^6$, $M=0.17$, angle of attack $5.5^\circ$, 27 million
cells) in the structured finite-difference code PHengLEI. Three Roe-flux
schemes share the solver (§2.2, Eqs. 12–15): a second-order blended
central/upwind interpolation (BCD) of the interface states with upwind
fraction $\sigma_b=0.02$ ($\sigma_b=1$ fully second-order upwind,
$\sigma_b=0$ central), chosen "to reduce the numerical dissipation and
maintain the numerical stability", and the fourth-order
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
with Z-type weights, either with the regularizer set to 100 so that the
weights stay near their linear values (WCNS-L) or to $10^{-6}$ (WCNS-Z).
The lift coefficient against the experimental mean 2.83 is $-11.0\%$
(BCD), $-6.7\%$ (WCNS-Z) and $-0.4\%$ (WCNS-L) (Table 2); the less
dissipative schemes make the slat-cove shear layer go unstable sooner
(§3.3, Fig. 11). The authors attribute the WCNS-Z deficit to the Z-type
weights losing accuracy near high-order critical points and recommend the
linear interpolation for shock-free low-Mach flow (§3.3, §4). Wang et
al. (2024) above run the same airfoil with the sixth-order upwind OPT6 in
SA-based DDES; the two studies use different hybrid models and solvers and
do not test each other's schemes.

**Dispersion against formal order in the first High-Order CFD Workshop.**
In the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) case at
$Re=1600$ of [Wang et al. (2013)](/sources/wang-2013.md), §5.6, NASA Glenn
submitted standard central finite differences of fourth, eighth and twelfth
order and a fourth-order dispersion-relation-preserving (DRP) scheme, a
family that, in the authors' words, attempts "to minimize dispersion errors
instead of directly addressing the formal order of accuracy": the
error of the twelfth-order central scheme is comparable with that of the
formally fourth-order DRP scheme, and that of the standard fourth-order
scheme much higher, which "seems to indicate that the dispersion error
already dominates". None of the finite-difference schemes attains its
projected order for any of the three error measures (Figs. 25–27).

**Bandwidth-optimized WENO for shock trains.**
[Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) apply the
bandwidth-optimized WENO schemes of Martín et al., whose linear weights are
optimized for resolution rather than for maximal order, so that in smooth
regions their dispersion is "comparable" to that of the sixth-order compact
central scheme (§1, §2.2.1): on a symmetric set of four three-point stencils
(six points) the optimized weights are 0.094647545896, 0.428074212384,
0.408289331408 and 0.068988910311, on five four-point stencils (eight
points) 0.040195483373, 0.249380000671, 0.480268625626, 0.200977547673
and 0.029178342658 (Eqs. 20, 47, from Martín et al.'s Table 7); a relative
total-variation limiter keeps the nonlinear weights off in smooth flow (see
[shock sensors](/definitions/shock-sensor.md)). On a Gaussian advection
test their limited schemes match the $L_\infty$ errors of the linear
optimized schemes of three and four points, which the authors read as third
and fourth order (§3.1.1, Fig. 3); they cost 1.045 and 1.371 times WENO-JS
per point and step on the Shu–Osher problem, against 1.5 for WENO-CU6, 2.126
for TENO6 and 2.9 for TENO8 (Table 1). The formulas and the gas-dynamics
comparisons are on [WENO and hybrid schemes](/methods/weno-scheme.md).

**Minimized dispersion and controllable dissipation (MDCD) in multi-material
flow.** [Maltsev et al. (2022)](/sources/maltsev-2022.md), §IV, cite the
MDCD scheme of Sun et al., whose free parameters set dispersion and
dissipation separately, and its hybrid with WENO (Wang et al.; Ren et al.),
claimed more efficient than WENO-JS when 10 to 20 cells per
wavelength resolve the highest wavenumber. On the multi-species advection
test of Wong & Lele at 128 cells they tabulate (Table I, adapted from Wang
et al.) orders 1.666 (MUSCL), 4.743 (WENO-JS), 4.339 (bandwidth-optimized
WENO-SYMBO) and 4.619 (MDCD-WENO), with errors $1.153\times10^{-3}$,
$3.223\times10^{-8}$, $5.541\times10^{-8}$ and $2.814\times10^{-8}$; citing
Johnsen et al. and Pirozzoli, they also state that the upwind-biased
nonlinear reconstruction of WENO-JS dissipates turbulent fluctuations at the
higher resolvable wavenumbers (§IV).

## Optimizing stencils, filters and time integrators by a spectral objective

Three sources build the coefficients of their schemes by
minimizing a wavenumber-space error under order constraints, the
dispersion-relation-preserving idea of Tam & Webb cited by Luo & Wu
above. Page-local notation: $k\Delta x$ the reduced wavenumber ($k$ a
wavenumber here, not the turbulent kinetic energy), $k^*\Delta x$ the
modified wavenumber of a scheme (real part dispersion, imaginary part
dissipation), $c_j$ antisymmetric (centred, non-dissipative) and $e_j$
symmetric (dissipative) stencil coefficients.

**Centred differences and selective filters of the BASIC code.**
[Volpiani (2024)](/sources/volpiani-2024.md), §2.2, App. 1, after Bogey &
Bailly, writes the centred first derivative on $2N_p+1$ points as
$\Delta x^{-1}\sum_{j=1}^{N_p}c_j[f(x+j\Delta x)-f(x-j\Delta x)]$, with
$k^*\Delta x=2\sum_jc_j\sin(jk\Delta x)$, and the relaxation (selective)
filter as $u^{\mathrm f}=u-\chi_f\sum_{j=-N_p}^{N_p}e_ju(x+j\Delta x)$,
$e_{-j}=e_j$, with damping function $D_k(k\Delta x)=e_0+2\sum_je_j\cos(jk\Delta x)$
and strength $\chi_f=0.1$ applied every time step in each
direction ($N_p$, $\chi_f$, $D_k$ page-local; the source's
$a_j$, $d_j$, $\chi$). The new 11-point schemes minimize (Eqs. 6, 8)
$$\int_{0.2}^{1.5}\big|k^*\Delta x-k\Delta x\big|\,\mathrm d(k\Delta x)\quad\text{s.t.}\ \sum_j2jc_j=1,\ \sum_jj^3c_j=\sum_jj^5c_j=0,$$
$$\int_{0.2}^{1.3}D_k^2\,\mathrm d(k\Delta x)+\Big\|\frac{\partial D_k}{\partial(k\Delta x)}\Big\|_2^2\quad\text{s.t.}\ e_0+2\sum_je_j=0,\ \sum_jj^2e_j=\sum_jj^4e_j=0,\ e_0+2\sum_j(-1)^je_j=1,\ D_k>0,$$
by sequential least squares (SLSQP). Both are formally sixth order,
"instead of the forth order obtained in Bogey and Bailly (2004)", the
filter staying purely dissipative and removing grid-to-grid waves
($D_k(\pi)=1$); coefficients in Tables 2–3 (FDo11p:
$c_1=0.8635414482176262$, $c_2=-0.274305332247656$,
$c_3=0.08147311338115067$, $c_4=-0.01708000680758487$,
$c_5=0.0017939806729146523$). The optimized derivative beats the standard
11-point one on $0.2\le k\Delta x\le1.5$ and matches Bogey & Bailly's
there, and is worse beyond 1.5; the filter is more accurate than Bogey &
Bailly's 2004 filter at low wavenumbers and than Bogey et al.'s 2009
filter at high ones (App. 1, Figs. 19–20). The author attributes the early
kinetic-energy loss of the 2004 combination in the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) to that filter's
lower formal order, "more dissipative for long waves" (§4, p. 905). Five-
and six-stage low-storage Runge–Kutta schemes are optimized likewise up to
$\omega\Delta t=1.2$ (page-local $\omega$ an angular frequency), with lower
dissipation, phase error and larger stability limits than the standard
four-stage scheme (Eq. 20, App. 1, Fig. 21, Table 4), but the production
runs keep the standard scheme, results being independent of the time
integrator (§2.3). The filter's role as the dissipation of implicit LES
is on [explicit modal filtering](/methods/explicit-modal-filtering.md)
and [implicit LES](/definitions/implicit-les.md).

**DRP differences, selective filter and LDDRK time stepping in two
wall-modelled LES.** Two 2025 papers of one group use the classical
members of this family. In the high-order computational-aeroacoustics
finite-difference solver of [Gao et al. (2025)](/sources/gao-2025.md),
§II.A, the convective derivatives are the seven-point fourth-order
dispersion-relation-preserving scheme of Tam & Webb, time integration is
the four-step fourth-order Adams–Bashforth scheme at Courant numbers below
0.15, and the Bogey–Bailly selective filter damps grid-scale waves, with
the Vreman model as subgrid closure and a slip-wall model at the wall (on
[slip-wall models](/methods/slip-wall-model.md)). Against the OpenFOAM
wall-modelled LES of Fan et al. at $Re_\tau=1000$, which shows "an
spurious spectral peak, larger amplitude discrepancies, and premature
decay in the mid-frequency range" of the wall-pressure spectrum, the
authors' run on $127\times41\times95$ points agrees better with DNS
spectra, which they attribute to the "inherent limitations of
conventional low-order numerical schemes" (§III.A.2, Fig. 10). In
the flux-reconstruction wall-modelled LES of
[Gao et al. (2025b)](/sources/gao-2025-b.md), §II A, the time marching is
the low-dissipation low-dispersion Runge–Kutta scheme of Hu, Hussaini &
Manthey (1996) in 2N-storage form, and their periodic-hill reference LES
(Gloerfelt & Cinnella, cited) uses an 11-point DRP finite-difference
scheme on $512\times256\times256$ points (§III B; see
[wall-modelled LES](/methods/wall-modelled-les.md)).

**Split dispersion and dissipation of TENO-S.**
[Liang & Fu (2024)](/sources/liang-2024.md), §3.3.1, Eqs. (36)–(46),
optimize the two halves of an eight-point scheme separately, the
derivative written as $D=D_{\mathrm{disp}}+D_{\mathrm{diss}}$ with
$D_{\mathrm{disp}}f=\Delta x^{-1}\sum_jc_j[f(x+j\Delta x)-f(x-j\Delta x)]$ and
$D_{\mathrm{diss}}f=\Delta x^{-1}[e_0f(x)+\sum_je_j(f(x+j\Delta x)+f(x-j\Delta x))]$,
which they state removes the anti-dissipation of a joint optimization at
intermediate wavenumbers. The centred coefficients minimize
$$\int_0^\pi e^{7(\pi-k\Delta x)}\big(\mathrm{Re}(k^*\Delta x)-k\Delta x\big)^2\,\mathrm d(k\Delta x)$$
under sixth-order constraints, the weight favouring low wavenumbers
because at high ones the TENO nonlinear adaptation dominates; they give
$c_1=0.8441336457279522$, $c_2=-0.2441336457279522$,
$c_3=0.0570096576929319$, $c_4=-0.006723831837710873$, used as the
coefficients of the non-dissipative skew-symmetric flux in smooth cells
(see [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
The dissipative coefficients of the TENO background scheme take four
moment conditions and a fifth fixing $e_0=0.01$ through the
approximate dispersion relation (credited by Liang & Fu to Hu,
Tritschler, Pirozzoli & Adams and to Fu et al.), the ratio
$|\mathrm d\,\mathrm{Re}(k^*\Delta x)/\mathrm d(k\Delta x)-1|/(-\mathrm{Im}(k^*\Delta x))\approx O(10)$
(Eq. 45). The resulting background linear scheme and the TENO optimal
weights are printed to 16 digits (Eq. 46); see
[WENO](/methods/weno-scheme.md).

**Weights of a variational reconstruction for anisotropic RANS grids.**
[Huang et al. (2022b)](/sources/huang-2022-d.md), §2.4, choose the
derivative weights $\varpi_n$ (page-local) of a compact variational
reconstruction for a high-order finite-volume
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS solver by
Fourier analysis of one-dimensional upwind advection, minimizing the
objective of Ponziani et al. (page-local parameters with
subscript o)
$$\int_0^\pi e^{v_{\mathrm o}(\pi-k\Delta x)}\Big[\theta_{\mathrm o}\big(\mathrm{Re}(k^*\Delta x)-k\Delta x\big)^2+(1-\theta_{\mathrm o})\big(\mathrm{Im}(k^*\Delta x)-\gamma_{\mathrm o}\sin^{\mu_{\mathrm o}}(k\Delta x/2)\big)^2\Big]\mathrm d(k\Delta x),$$
$v_{\mathrm o}=12$, $\theta_{\mathrm o}=0.5$, $\gamma_{\mathrm o}=-1$,
$\mu_{\mathrm o}=6$, under the monotonicity constraint
$\varpi_{n_1}\le\varpi_{n_2}$ for $n_1\ge n_2$. For the cubic (fourth-order)
reconstruction this gives $\varpi_1=0.5295$, $\varpi_2=\varpi_3=0.2117$
(Table 1); the unconstrained optimum has better dispersion and
dissipation curves but is "not robust", which the authors attribute to
its much smaller dissipation (leading term $-3.23\times10^{-3}(k\Delta x)^8$
against $-2.24\times10^{-2}(k\Delta x)^8$, in units of $at/\Delta x$ with
$a$ the advection speed and $t$ the time, page-local; §2.4.1, Fig. 4). A
geometric weight $(S_{ij}/d_{ij})^{1/2}$ ($S_{ij}$ face area, $d_{ij}$
centroid distance, page-local) follows from two-dimensional analysis on
grids of aspect ratio up to $10^3$ (§2.4.2). The exponentially weighted
objectives of Liang & Fu and of Huang et al. both put the accuracy at low
wavenumbers; Volpiani's integrates the dispersion error uniformly over a
band.

Bernades et al. distinguish *numerical* dissipation (an undesired property
of the method) from *artificial* dissipation (deliberately added) (§1,
footnote 1).

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
  comparison.
- Wang et al. (2024, §2.3) state that the KGP form follows from the
  general combination of five convective forms with "$\xi=1/2$,
  $\alpha=\beta=\delta=1/4$, and $\varepsilon=0$"; $\xi$ is not defined and
  the weight of the $C^u$ form is not given. In the one-parameter family
  cited by Bernades et al. (2023) the KGP form is the parameter value
  $\tfrac12$ and carries weight $\tfrac14$ on that form too
  *(compiler check, not in the sources)*; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).
- **Constraints, checked.** The printed FDo11p coefficients of Volpiani
  (2024) give $\sum_j2jc_j=1.0000$ to the printed digits, and Liang & Fu's
  (2024) centred coefficients give $2c_1+4c_2+6c_3+8c_4=1$
  *(compiler check, not in the sources)*. Volpiani's cost weights of the
  Runge–Kutta objective are not printed, and the optimized integrators are
  not used in production.
- The spectral objectives are linear analyses: Liang & Fu (2024) and
  Huang et al. (2022b) optimize the linear part of nonlinear schemes (TENO,
  a reconstruction later limited at start-up by a WBAP limiter, §3.3), and
  the robustness verdict of Huang et al. on the unconstrained weights is
  asserted, not displayed.
- **Attribution of the workshop DRP scheme.** Wang et al. (2013)
  attribute the fourth-order DRP finite differences to "Bogey and Bailly",
  who are not in their reference list, and cite "DRP methods [35]", which
  is Kim & Lee's optimized compact schemes; the reference titled
  "dispersion-relation-preserving" is [6], Tam & Webb.
- Kumar & Ghosh (2022, Eqs. 16, 43) name the candidate-flux coefficients
  with the letter of their nonlinear weights; their reading of third and
  fourth order rests on the agreement of error curves with the linear
  optimized schemes, without tabulated rates (§3.1.1).
- Deng et al. (2022) run their scheme at $\lambda_{\mathrm{AD}}=0.5$, exactly central in
  smooth regions, in a compressible Navier–Stokes solver without a split or
  kinetic-energy-preserving form and without a filter; they report no
  instability, but the purely central setting is run in turbulence only on
  the $128^3$ isotropic-turbulence grid, while the under-resolved $64^3$
  runs use $\lambda_{\mathrm{AD}}\ge0.65$ (§4.15), and they themselves cite that "a small
  amount of dissipation is needed" against instabilities of under-resolved
  scales (§1). Their ADR claims are shown in figures only, without tabulated values.
- Ma et al.'s (2022) resolving ratios are linear analyses of the
  interpolations; their WCNS-T costs 5–7 times WCNS-E per grid point on the
  same grid ($1.26\times10^4$ against $1.83\times10^3$ CPU time units at
  2802 points, Table 2) and is cheaper only at equal error (Fig. 3).
- **Printed form of the BCD interpolation (Wu et al. 2023, Eq. 15).** The
  left state is $u_j+\tfrac12\sigma_b(u_j-u_{j-1})+\tfrac12(1-\sigma_b)(u_{j+1}-u_j)$,
  which at $\sigma_b=0$ is the central value $\tfrac12(u_j+u_{j+1})$ at
  $j+\tfrac12$; the right state is printed
  $u_j-\tfrac12(1-\sigma_b)(u_j-u_{j-1})-\tfrac12\sigma_b(u_{j+1}-u_j)$,
  which at $\sigma_b=0$ gives $\tfrac12(u_j+u_{j-1})$, the central value at
  $j-\tfrac12$ *(compiler check, not in the sources)*. The text
  calls the scheme a "second-order central flux difference" in an
  unfinished sentence (§2.2.2). The single-airfoil evidence uses one grid
  for the scheme comparison (the fine, 27 million cells).
- Printed slips: §5 attributes LD2 to "Löwe et al. [28]", while ref. [28] is
  Probst et al. and LD2 is Löwe et al. [10] elsewhere; §4.3 cites Fig. 4(b) for
  both $Re_\tau=2400$ and 18 000 (the latter is Fig. 4(c)); the text refers to
  the Ducros sensor as Eq. (14) in §4.4 and as Eq. (15) in §4.1 (Eq. 14 is the
  factor, Eq. 15 the sensor used).

# Citations

- [Bernades et al. (2023)](/sources/bernades-2023.md) — §1, footnote 1 (numerical against artificial dissipation; filtering); §3.2, Eq. (29), Table 2 (compact filter, hybrid); §4.1–4.2.
- [Wang et al. (2024)](/sources/wang-2024.md) — §2.3–2.5, Eqs. (5)–(13), Fig. 1, Table 1 (split forms, OPT6, Roe flux, approximate dispersion relation); §3.2, Figs. 3–4 (channel); §3.3, Table 2, Figs. 5–6 (periodic hill); §4–5 (30P30N DDES, recommendation).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §3.1, Fig. 1; §4, Fig. 4 (approximate dispersion relation of WENO-Z+ and WENO-Z+M against UD5); §6 (nonlinear weighting against optimized linear coefficients).
- [Volpiani (2024)](/sources/volpiani-2024.md) — §2.2.1–2.2.2, Eqs. (5)–(8), Tables 2–3 (optimized centred differences and selective filter); §2.3, Eqs. (18)–(20), Table 4 (optimized low-storage Runge–Kutta); §4; App. 1, Figs. 19–21.
- [Liang & Fu (2024)](/sources/liang-2024.md) — §3.3.1, Eqs. (36)–(46) (split dispersion/dissipation optimization, approximate dispersion relation, $e_0=0.01$).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.4.1–2.4.2, Eqs. (26)–(51), Tables 1–2, Fig. 4 (Ponziani objective for variational-reconstruction weights); §3.3 (WBAP limiter at start-up).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2, Eqs. (1)–(8) (M-Edge discretization, Kok flux, extrapolation, JST dissipation); §2.2.2, Eqs. (9)–(11) (preconditioning); §2.2.3, Eqs. (12)–(15) (Jameson and Ducros sensors); §2.3, Fig. 1 (dispersion/dissipation analysis, choice of $a$); Table 1; §4.1, Eq. (22), Fig. 2 (Sod); §4.2, Fig. 3 (decaying isotropic turbulence); §4.3, Table 2, Figs. 4–6 (channel); §4.4, Figs. 7–10 (base flow); §5.
- [Wang et al. (2013)](/sources/wang-2013.md) — §5.6, Figs. 25–27 (central and DRP finite differences on the Taylor–Green vortex).
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) — §1; §2.2.1, §2.2.6, Eqs. (20), (47) (optimized linear weights); §3.1.1, Fig. 3; §3.1.3, Table 1 (grind times).
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §IV, Table I (MDCD, MDCD-WENO, WENO-SYMBO, cited orders and errors; WENO-JS spectral dissipation, cited).
- [Deng et al. (2022)](/sources/deng-2022.md) — §1 (MDCD cited; dissipation for under-resolved scales); §3.2, Eq. (21), Remarks 1–2 (dissipation-adjusting parameter); §4.1, Figs. 1–2 (approximate dispersion relation against linear upwind and WENO-M); §4.2, Table 1.
- [Ma et al. (2022)](/sources/ma-2022.md) — §1 (CRWENO); §2.3, Table 1, Fig. 1 (Fourier and ADR resolving ratios of WCNS-E and WCNS-T); §2.3.1–2.3.2, Fig. 2, Table 2 (shock–entropy wave; cost and order).
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §2.2.1–2.2.2, Eqs. (12)–(15) (fourth-order WCNS with near-linear and Z-type weights, blended central/upwind interpolation with $\sigma_b=0.02$); §3.3, Table 2, Fig. 11 (scheme dissipation and lift of the 30P30N airfoil); §4.
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §4.8 (compact finite differences developed to minimize dispersion error; historical, passing).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B, Eqs. (8)–(9) (sixth-order compact differences with eighth-order compact filter, adaptive second-order filter at shocks).
- [Gao et al. (2025)](/sources/gao-2025.md) — §II.A (Tam–Webb DRP scheme, Adams–Bashforth, Bogey–Bailly selective filter in a WMLES solver); §III.A.2, Fig. 10 (wall-pressure spectra against a low-order WMLES).
- [Gao et al. (2025b)](/sources/gao-2025-b.md) — §II A (Hu–Hussaini–Manthey LDDRK time marching); §III B (DRP reference LES of the periodic hill; passing).
