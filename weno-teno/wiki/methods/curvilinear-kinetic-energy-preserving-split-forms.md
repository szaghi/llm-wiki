---
type: Method
title: "Kinetic-energy-preserving split forms in curvilinear coordinates"
description: "Central finite differences on curvilinear meshes keep the volume-weighted discrete kinetic energy when the Jacobian is absorbed into the density or the contravariant velocity and continuity and momentum are split alike; Pirozzoli's Kennedy–Gruber U/J scheme in two-point flux form, its metric treatment, its evidence against filtered and unfiltered central differencing, and its limits on non-smooth meshes."
status: established
aliases: [SCFD, split convective finite differences, KG-U/J, RHO/J formulation, U/J formulation, curvilinear KEP scheme]
tags: [kinetic-energy-preserving, finite-difference, central-scheme, low-dissipation, turbulence]
timestamp: 2026-11-17T08:42:21Z
---

# Kinetic-energy-preserving split forms in curvilinear coordinates

The Cartesian [split convective forms](/methods/split-convective-forms.md) stabilize
non-dissipative central schemes by making the semi-discretization conserve kinetic energy
([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
[Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md) extends them to central finite
differences of any order on structured curvilinear meshes, for the compressible Euler
equations, without upwinding or filtering.

## Strong conservation form

Let $x(\xi)$ be a time-independent, smooth and locally invertible map from computational
coordinates $\xi_j$ with unit spacing (registry §10; not the DG nodes $\xi_j$) to
physical space, $J$ its Jacobian (the cell volume) and $Ja^{(j)}=J\nabla\xi_j$ the
contravariant metric terms. The Euler equations, $u=(\rho,\rho v,E)$, in the strong
conservation form of Vinokur read ([Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md), Eq. (1))

$$J\,\partial_tu+\sum_j\partial_{\xi_j}\big(\rho\hat v_j,\ \rho v\,\hat v_j+p\,Ja^{(j)},\ \rho H\hat v_j\big)=0,\qquad \hat v_j=Ja^{(j)}\cdot v ,$$

with $\hat v_j$ (registry §10) the contravariant velocity weighted by the cell volume and
$\rho H=E+p$. The flux in direction $j$ is the Cartesian flux contracted with the metric
terms, $\sum_d(Ja^{(j)})_df^{(d)}(u)$, and a uniform state is a steady solution because of the
metric identity $\sum_j\partial_{\xi_j}Ja^{(j)}=0$, whose discrete form decides
[free-stream preservation](/properties/free-stream-preservation.md) *(compiler check, not in
the sources: the paper writes only the Euler case)*. Leaving out the
pressure, every component has the form

$$J\,\partial_t(\rho\phi)+\sum_j\partial_{\xi_j}(\rho\hat v_j\phi)=0,\qquad \phi\in\{1,\ v_i,\ H\},$$

with $\phi$ the page-local transported scalar of the split-form pages (Eq. (2)).

## Where the Jacobian goes

The Cartesian splits of $\partial(\rho v\phi)$ need a triple product. On a curvilinear mesh
the Jacobian has to be absorbed into one of its three factors (§2.2):

- **into $\phi$** fails. The continuity equation then transports $\hat\phi=J\phi=J\ne1$ (the source's $1/J$), so its split
  form differs from that of the momentum equation, and combining the two leaves an extra
  term;
- **into the density (RHO/J):** $\partial_t(J\rho\phi)+\sum_j\partial_{\xi_j}(J\rho\,\tilde v_j\phi)=0$, with
  $\tilde v_j=\nabla\xi_j\cdot v=\hat v_j/J$ the contravariant velocity (Eqs. (13)–(15));
- **into the velocity (U/J):** $J\partial_t(\rho\phi)+\sum_j\partial_{\xi_j}(\rho\hat v_j\phi)=0$ (Eqs. (17)–(19)).

Let $\delta_j$ be a central first-derivative operator along $\xi_j$,

$$\delta_jf_i=\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\,(f_{i+\ell}-f_{i-\ell})\quad\text{(shifts along direction }j),$$

of order $2L_{\mathrm s}$ for the maximum-order weights (registry §10 $\mathsf a_\ell$, $L_{\mathrm s}$, as on
[flux differencing](/methods/flux-differencing.md); DRP weights are allowed, Eq. (3)). On a
periodic direction it satisfies $\sum_if_i\,\delta_jg_i+\sum_ig_i\,\delta_jf_i=0$ for any grid
functions, which holds for explicit and implicit (compact) central operators of any order
(Eq. (12), citing Mansour et al.;
[summation-by-parts operator](/operators/summation-by-parts-operator.md)). Let continuity
and momentum be split by the same rule, Feiereisen's or Kennedy–Gruber's, the latter with
$\alpha_{\mathrm{KG}}=\beta_{\mathrm{KG}}=\tfrac14$ (registry §10; §2.1). For U/J with the
Feiereisen split, the momentum equation times $v_i$ minus continuity times
$\tfrac12\lvert v_i\rvert^2$ then gives

$$J_i\frac{d\kappa_i}{dt}+\tfrac12\,v_i\cdot\sum_j\delta_j(\rho\hat v_jv)_i+\tfrac12\sum_j(\rho\hat v_jv)_i\cdot\delta_jv_i=0$$

(Eq. (19); RHO/J gives the analogue, Eq. (15), and the Kennedy–Gruber split the same
conclusion, "easy to show" according to the paper). Summed over a periodic grid the last two terms
cancel, so both formulations conserve the **volume-weighted kinetic energy**
$\sum_iJ_i\kappa_i$, "a legitimate discrete surrogate for the kinetic energy" (Eq. (16)),
under exact time integration.

Of the four KEP combinations (Feiereisen or Kennedy–Gruber, RHO/J or U/J), Pirozzoli
retains **KG-U/J**. The author reports Kennedy–Gruber as more robust than Feiereisen, which
the author explains by the form of its numerical flux, in which "density variations are
more effectively averaged out", and U/J as more robust than RHO/J in preliminary tests
(§2.2, §3.1.1). The convective split is

$$J\partial_t(\rho\phi)+\tfrac14\partial_{\xi_j}(\rho\hat v_j\phi)+\tfrac14\big(\rho\,\partial_{\xi_j}(\hat v_j\phi)+\hat v_j\,\partial_{\xi_j}(\rho\phi)+\phi\,\partial_{\xi_j}(\rho\hat v_j)\big)+\tfrac14\big(\rho\hat v_j\,\partial_{\xi_j}\phi+\rho\phi\,\partial_{\xi_j}\hat v_j+\hat v_j\phi\,\partial_{\xi_j}\rho\big)=0$$

(Eq. (20), summed over $j$). The pressure term may be centrally differenced as it is
"without major drawbacks"; the paper splits it "in the spirit of aliasing minimization",

$$\partial_{\xi_j}\big(p\,Ja^{(j)}\big)=\tfrac12\partial_{\xi_j}\big(p\,Ja^{(j)}\big)+\tfrac12p\,\partial_{\xi_j}Ja^{(j)}+\tfrac12Ja^{(j)}\,\partial_{\xi_j}p,$$

for "marginally superior robustness" (Eq. (21); metric written as in Eq. (1), see the
Qualifications). The baseline keeps the total-energy equation; the internal-energy or
entropy equation (Honein & Moin) and the sound-speed equation (Kok) are recalled as more
robust options (§2.2). Replacing every derivative by $\delta_j$ gives the semi-discretization,
Eq. (22): seven derivative terms per direction in each momentum and energy row, three of them
shared with continuity, plus three for the split pressure *(compiler count; the source says
"many applications of the discrete first derivative operator")*.

**Franck & Colonius's split** is not KEP. They start from the Cartesian Feiereisen form and
replace each Cartesian derivative by its strong-conservation curvilinear expression
(Eq. (23)). As recalled, this is more stable than the unsplit form, but it "does not guarantee
discrete energy preservation from convection", whereas the RHO/J form (14) does (§2.2).

## Two-point flux form

Eq. (22) is expensive. Following Pirozzoli (2010) (see
[conservative split derivative](/operators/conservative-split-derivative.md)), the KG-U/J
semi-discretization is written as a flux difference (§2.3, Eqs. (27)–(30)). With
$\{\!\{a\}\!\}_{k,\ell}=\tfrac12(a_k+a_{k+\ell})$ along direction $j$,

$$\frac{du_i}{dt}=-\frac1{J_i}\sum_j\Big(\hat F^{(j)}_{i+1/2}-\hat F^{(j)}_{i-1/2}\Big),\qquad
\hat F^{(j)}_{i+1/2}=2\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\sum_{m=0}^{\ell-1}\begin{pmatrix}\{\!\{\rho\}\!\}\{\!\{\hat v_j\}\!\}\\ \{\!\{\rho\}\!\}\{\!\{\hat v_j\}\!\}\{\!\{v\}\!\}+\{\!\{p\}\!\}\{\!\{Ja^{(j)}\}\!\}\\ \{\!\{\rho\}\!\}\{\!\{\hat v_j\}\!\}\{\!\{H\}\!\}\end{pmatrix}_{i-m,\,\ell}.$$

The triple product of arithmetic means is the paper's two-point, three-variable average
(Eq. (26)); the pressure term is the same average applied to $(p,Ja^{(j)},1)$ (Eq. (28)). The
paper calls this form "entirely equivalent to (but computationally less expensive than)" Eq.
(22), taking the equivalence from Pirozzoli (2010) *(compiler check, not in the sources: the
flux difference reproduces the Kennedy–Gruber split derivative to round-off for
$L_{\mathrm s}=1,\dots,4$ on random periodic data)*. Its stated benefits are global conservation of
mass, momentum and total energy by telescoping, simple insertion into existing conservative
solvers, and straightforward hybridization with shock-capturing schemes, which is not tested
([local conservation and flux form](/results/local-conservation-flux-form.md);
[hybrid central-WENO schemes](/methods/hybrid-weno.md)). The averages are stored line by line
for all $\ell\le L_{\mathrm s}$, with "insignificant" memory overhead (§2.3).

The metric enters the momentum and energy fluxes through $\{\!\{\hat v_j\}\!\}$, the average
of the nodal product $Ja^{(j)}\cdot v$, not as $\{\!\{Ja^{(j)}\}\!\}\cdot\{\!\{v\}\!\}$ as in
the DG two-point fluxes of [flux differencing](/methods/flux-differencing.md) *(compiler
check, not in the sources)*.

**Divergence-form central differencing** (DFD), the comparison scheme, is the same double sum
with the averages of the products, $\{\!\{\rho\hat v_j\}\!\}$,
$\{\!\{\rho\hat v_jv\}\!\}+\{\!\{p\,Ja^{(j)}\}\!\}$, $\{\!\{\rho\hat v_jH\}\!\}$ (Eqs. (31)–(32)).

**Metrics.** "To minimize sources of errors associated with failure to preserve the
undisturbed free-stream conditions", after Visbal & Gaitonde, every metric derivative is
computed with the same $\delta_j$, $\partial x_k/\partial\xi_j\approx\delta_jx_k$ (§3, Eq. (33)). The
paper claims no exactness. In 2D this makes the free stream exact for both the split and the
divergence schemes, because the tensor-product central operators commute; in 3D the
products of metric derivatives need the conservative form instead
([free-stream preservation](/properties/free-stream-preservation.md); *compiler check, not
in the sources*).

## Evidence

All runs are 2D, with classical fourth-order Runge–Kutta at Courant number 0.25 and orders 2
to 8 ($L_{\mathrm s}=1,\dots,4$). The split scheme (SCFD in the paper) is compared with DFD and with
DFD plus the eighth-order [compact low-pass filter](/methods/compact-low-pass-filter.md) at
$\alpha_{\mathrm P}=0.495$ after every step (FDFD). Over DFD the filter costs about 30 % and the
split scheme about 50 % (§3).

- **Vortex on a smooth wavy mesh** ([isentropic vortex](/benchmarks/isentropic-vortex.md);
  Kawai–Lele mesh, $81\times41$, periodic; §3.1.1). DFD diverges before the final time at every
  order. At second order both stable schemes are "extremely poor", and the contours become
  rounder with order, the split scheme somewhat better, "especially for the strong vortex"
  (Figs. 2–3). For the weak vortex ($M_{\mathrm v}=0.1$, three flow-throughs) the split scheme keeps
  $\sum_iJ_i\kappa_i$ constant to plotting accuracy at every order plotted ($L_{\mathrm s}=2,3,4$), while FDFD drifts up or down
  with the order, by up to about $1.5\times10^{-3}$ (read from Fig. 6a). For the strong vortex
  ($M_{\mathrm v}=0.5$, fifteen flow-throughs, eighth order) the kinetic energy oscillates as it
  exchanges with internal energy, and the split scheme drifts less than FDFD; its velocity
  profiles show dispersive oscillations that the filter controls better (Figs. 5, 6b).
- **Convergence.** At $L_{\mathrm s}=3$ on four grids halved in both directions, the error norms of
  the vertical velocity "scale consistently with the nominal order of accuracy on the
  curvilinear mesh", i.e. sixth order (read from Fig. 7).
- **Randomized mesh** (a $51\times51$ mesh with interior points displaced by 20 % of the spacing in
  random directions, $M_{\mathrm v}=0.0012$, after Visbal & Gaitonde; §3.1.2). Both the split scheme and,
  less, FDFD develop strong dispersive oscillations that "eventually lead to divergence at
  later times". FDFD diverges by unbounded growth of the velocity maximum; the split scheme
  "more or less maintains the velocity maximum while oscillations become wilder" (Fig. 9).
  The stronger filtering Visbal & Gaitonde found necessary was not tried.
- **Head-on collision of two Lamb–Chaplygin dipoles** (the paper cites Lamb only; the name is the compiler's identification) on a distorted $60\times60$ mesh, eighth
  order, inviscid and $\mathrm{Re}=10^4$, $5000$, $1000$ (§3.2). Inviscid, the split scheme places the
  dipoles correctly, but with "substantial numerical dispersion associated with mesh
  distortion, that may lead to divergence over longer times"; on a uniform grid it is much
  smoother, and FDFD is smooth. At $\mathrm{Re}=1000$ the two fields are "virtually indistinguishable",
  whereas DFD is stabilized only for $\mathrm{Re}\lesssim100$ (not shown) (Fig. 12), and their
  kinetic-energy histories nearly coincide with a $400\times400$ Cartesian run (Fig. 13). The inviscid split scheme's discrete enstrophy
  grows by about 11 % over the run (read from Fig. 13b), read by the author as small-scale energy pile-up; FDFD keeps the enstrophy
  nearly constant inviscid but below the split scheme's in the resolved case, a sign of
  dissipation at the highest resolved wavenumbers (Fig. 13).

## Qualifications

- **Assumptions.** The conservation of $\sum_iJ_i\kappa_i$ is proved for periodic directions
  (SBP) and exact time integration, without pressure work; walls are not treated, and all
  tests are 2D (§2, §4).
- **A weak norm.** Kinetic energy is not an energy norm of the compressible Euler equations,
  and the volume weight lets the velocity become very large where the mesh is fine without
  much growth of $\sum_iJ_i\kappa_i$: "kinetic energy stability is a rather weak form of nonlinear
  stability for compressible flows in curvilinear coordinates". No a-priori nonlinear
  stability is claimed for inviscid runs (§4).
- **Scope.** Arbitrary order is claimed "at least for smooth meshes". For complex geometries
  or non-smooth meshes the author refers to finite volumes or immersed boundaries, and in LES
  on non-smooth or skewed meshes "judicious use of filtering is still necessary" (§4).
- **Pressure metric.** Eq. (1) carries the pressure flux $p\,Ja^{(j)}$ (the source's $pJ_{ji}/J$),
  but Eqs. (21), (22), (28), (30) and (31) differentiate or average $pJ_{ji}$ without the
  $1/J$. Read literally this is inconsistent with Eq. (1), and with the unscaled metric a
  uniform pressure would not be steady, since $\sum_j\partial_{\xi_j}\nabla\xi_j\ne0$ in general; the
  formulas above follow Eq. (1) *(compiler check, not in the sources)*.
- **U/J against RHO/J.** The captions of Figs. 4–5 announce dotted curves for the RHO/J
  formulation, but no third curve can be told apart in the version of record, so the claim
  that U/J is better under compressibility rests on the text (§3.1.1).
- **"Not strictly skew-symmetric."** The paper repeats the remark of Pirozzoli (2010) that the
  usual label is not strictly correct, because "the integral of $\rho\varphi^2$ ... is not
  preserved". With continuity split by the same rule its own derivation conserves
  $\sum_i\tfrac12\rho_i\phi_i^2$ for any $\phi$, so the remark concerns the convective operator
  alone *(compiler check, not in the sources)* (a terminological point; see [split convective forms](/methods/split-convective-forms.md)).
- **Positioning.** The author places the scheme after the kinetic-energy-consistent finite
  volumes of Subbareddy & Candler (second order) and Kok (up to fourth order) and claims
  "superior computational efficiency" over finite volumes; no finite-volume scheme is run (§4).

# Citations

- [Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md) — §1, §2 Eqs. (1)–(4), §2.1 Eqs. (6)–(12), §2.2 Eqs. (13)–(23), §2.3 Eqs. (24)–(32), §3 Eqs. (33)–(34), §3.1 Figs. 2–9, §3.2 Figs. 12–13, §4.
