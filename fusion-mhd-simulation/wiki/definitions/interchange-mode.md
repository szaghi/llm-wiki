---
type: Definition
title: "Interchange modes and the Mercier criterion"
description: "Pressure-driven instabilities localized at rational surfaces where unfavourable average curvature beats magnetic shear; their ideal local limit is the Mercier criterion (shear, current, well and geodesic terms), their resistive counterpart the Glasser–Greene–Johnson parameter; in low-shear stellarators they are benchmarked between reduced and full MHD and need parallel flow to be captured at finite compressibility, a resonant ideal interchange collapses the high-beta LHD core in MHD but is stabilized by kinetic thermal ions, and the 1/1 quasi-interchange drives flux pumping in tokamaks."
status: established
aliases: [interchange instability, Mercier criterion, Mercier stability, resistive interchange, quasi-interchange]
tags: [mhd, stellarator, tokamak, equilibrium, verification, benchmark, reduced-mhd, hybrid-kinetic]
timestamp: 2026-10-16T20:00:00Z
---

# Interchange modes and the Mercier criterion

An interchange mode exchanges two flux tubes across a rational surface
without bending the field lines appreciably: the perturbation is nearly
constant along $\mathbf B$, so the field-line-bending energy is small, and
the drive is the pressure gradient in a region of unfavourable average
curvature. Magnetic shear stabilizes it by making the perturbation bend
field lines away from the rational surface. In stellarators without net
current the drive is concentrated at low-order rational surfaces in
low-shear regions; the stability limit, Mercier's criterion, "can be
exceeded experimentally" in net-current-free stellarators
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §1, §3.2). LHD is a
further case: inward-shifted discharges hold volume-averaged
$\beta\approx5\,\%$ without significant MHD activity although
fixed-boundary linear MHD predicts strong instability
([Sato & Todo (2026)](/sources/sato-2026.md), Introduction).
High-$n$ localized interchange and [ballooning modes](/definitions/ballooning-mode.md)
are the two limits of pressure-driven instability; the ballooning mode
localizes additionally along the field line on the bad-curvature side.

## The Mercier criterion

The Mercier criterion is the local ideal-MHD stability condition for
interchange perturbations about a flux surface. In the form used by
[Panici et al. (2023)](/sources/panici-2023.md) (§5.4, Eqs. 5.7–5.8, after
Bauer, Betancourt & Garabedian 1984), translated to the registry
($\psi_t$ the toroidal flux per radian, $V(\psi_t)$ the enclosed volume,
$G$, $I$ the Boozer covariant profile functions), stability requires

$$D_{\rm Merc}=D_{\rm Shear}+D_{\rm Curr}+D_{\rm Well}+D_{\rm Geod}>0,$$

$$\begin{aligned}
D_{\rm Shear}&=\frac{1}{16\pi^2}\Big(\frac{d\iota}{d\psi_t}\Big)^2,\qquad
D_{\rm Curr}=-\frac{\operatorname{sgn}G}{(2\pi)^4}\frac{d\iota}{d\psi_t}\int\mathrm dS\,\frac{\boldsymbol\Xi\cdot\mathbf B}{|\nabla\psi_t|^3},\qquad \boldsymbol\Xi=\mu_0\mathbf J-\frac{dI}{d\psi_t}\mathbf B,\\
D_{\rm Well}&=\frac{\mu_0}{(2\pi)^6}\frac{dp}{d\psi_t}\Big(\operatorname{sgn}\psi_t\,\frac{d^2V}{d\psi_t^2}-\mu_0\frac{dp}{d\psi_t}\int\frac{\mathrm dS}{B^2|\nabla\psi_t|}\Big)\int\mathrm dS\,\frac{B^2}{|\nabla\psi_t|^3},\\
D_{\rm Geod}&=\frac{1}{(2\pi)^6}\Big(\int\mathrm dS\,\frac{\mu_0\mathbf J\cdot\mathbf B}{|\nabla\psi_t|^3}\Big)^2-\frac{1}{(2\pi)^6}\Big(\int\mathrm dS\,\frac{B^2}{|\nabla\psi_t|^3}\Big)\int\mathrm dS\,\frac{(\mu_0\mathbf J\cdot\mathbf B)^2}{B^2|\nabla\psi_t|^3},
\end{aligned}$$

with the surface integrals over Boozer angles,
$\mathrm dS=|\nabla\psi_t|\sqrt g\,\mathrm d\theta\,\mathrm d\zeta$
(page-local: $\sqrt g$ the Jacobian, $\boldsymbol\Xi$ an auxiliary vector).
The four terms are the stabilizing shear, the parallel-current drive, the
magnetic well (the sign of $d^2V/d\psi_t^2$ against the pressure gradient)
and the geodesic-curvature term. $D_{\rm Shear}\ge0$ always; a low-shear
stellarator relies on the well.

**Numerical sensitivity.** $D_{\rm Geod}$ involves $\mathbf J$ and hence
higher radial derivatives of the equilibrium. On a quasi-helically symmetric
finite-β equilibrium (aspect ratio about 20, Mercier-unstable), $D_{\rm Merc}$
from DESC matches near-axis asymptotic formulae (Landreman & Jorge 2020) down
to the axis, while VMEC deviates inside about $s=0.6$ with 65 surfaces and
inside about $s=0.25$ with 801 surfaces ($s=\sqrt{\psi_{t,N}}$, read from the
figure), the deviation being dominated by $D_{\rm Geod}$
([Panici et al. (2023)](/sources/panici-2023.md), §5.4, Figs. 15–16). The
onset correlates with the radius where VMEC's force error rises; "one
possible explanation" is the accuracy of its radial derivatives (same
section). A Mercier evaluation is therefore a test of the equilibrium
solver, not only of the plasma; see
[three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md),
[VMEC](/software/vmec.md) and [DESC](/software/desc.md).

**A Mercier-unstable outer region.** The [HINT](/software/hint.md)
equilibria of high-beta LHD ($\beta_0=7.5\,\%$, $9.2\,\%$), re-solved with
VMEC inside the last closed surface, have a Mercier-stable core, where the
large Shafranov shift creates a magnetic well, and a Mercier-unstable outer
region with a magnetic hill ([Sato & Todo (2026)](/sources/sato-2026.md),
p. 3, Fig. 1).

**Tokamak edge form.** For edge ballooning in the large-$q$ limit,
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§2.3.3) quote a modified
Mercier criterion $4\alpha_{\rm b}(1-q^2)>\hat s^2q^2+\alpha_{\rm b}^2$,
with $\hat s$ and $\alpha_{\rm b}$ the shear and normalized pressure
gradient of ballooning theory, to argue that the reduced model of JOREK
leaves edge ballooning modes largely unaffected by its missing
parallel-field compression.

## Resistive interchange

With resistivity the field lines can slip across the rational surface and
the interchange becomes a resistive mode. In tokamak tearing theory the
finite-pressure toroidal-curvature correction is the Glasser–Greene–Johnson
resistive-interchange parameter, which [Zeng et al. (2023)](/sources/zeng-2023.md)
(§3, p. 6) write approximately as

$$D_R\approx\frac{\epsilon_s^2\beta_p}{\hat s}\frac{L_q}{L_p}\Big(1-\frac{1}{q^2}\Big),\qquad L_p=\frac{p}{dp/dr},\quad L_q=\frac{q}{dq/dr},$$

evaluated at the rational surface (page-local: $\epsilon_s$ the local inverse
aspect ratio, $D_R$; the source does not define $\epsilon_s$ and $\hat s$,
and the reading as inverse aspect ratio and shear is the reader's). $D_R$
is "in general negative and stabilizing" because $L_p<0$ for a monotonic
pressure. A locally hollow pressure makes $L_p>0$ and $D_R>0$; Zeng et al.
show that impurity radiation can produce exactly this on the $q=2$ surface
and trigger a $2/1$ tearing mode (§§1, 3; see
[radiation-triggered tearing](/results/radiation-triggered-tearing.md) and
[tearing mode](/definitions/tearing-mode.md)). They also cite the
destabilizing resistive interchange of negative-central-shear plasmas as
the same sign reversal (§1, citing Chu et al. 1996).

After kinetic thermal ions stabilize the ideal $(3,2)$ interchange in LHD
(next section), "the resistive interchange mode remains the dominant
unstable mode" ([Sato & Todo (2026)](/sources/sato-2026.md), p. 7); the
Fig. 4 caption of the same paper labels the modes only as $(3,2)$
interchange without the ideal/resistive distinction (recorded on the
Source page).

The W7-AS soft-β-limit activity at intermediate β is a low-$n$ resistive
pressure-driven activity whose $(2,1)$ component is reproduced only at
artificially high $\eta$
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §4, §4.4; see
[soft β limit](/definitions/soft-beta-limit.md)).

## Ideal interchange in high-beta LHD

In MIPS simulations of the LHD equilibria above, resistive
[ballooning modes](/definitions/ballooning-mode.md) dominate for
$10^4\le S\le10^6$; for $S>10^6$ a **resonant** $(3,2)$ ideal interchange
on the $\iota=2/3$ surface takes over, with $\gamma\tau_A\approx0.009$–0.01
nearly independent of $S$ (Fig. 4, figure reading), extends toward the
core and collapses it, by $t=3326\tau_A$ at $S=10^7$
([Sato & Todo (2026)](/sources/sato-2026.md), p. 5, Figs. 4, 7). The
authors contrast it with the non-resonant $m=n>1$ interchange behind a
tokamak sawtooth-like crash (Jardin et al. 2020, as cited). With
drift-kinetic thermal ions in MEGA, the precession of helically trapped
ions is faster than the interchange growth and stabilizes it; the
nonlinear activity then stays peripheral (p. 7–8). A $(1,1)$ interchange,
weakly unstable linearly, grows after the $n=2$ interchange saturates and
dominates the late nonlinear phase, with or without energetic ions (p. 9,
Fig. 11). Details on
[kinetic thermal ions confine LHD pressure-driven activity to the periphery](/results/kinetic-ions-prevent-core-collapse-lhd.md).

## Interchange-like edge modes despite a magnetic well

In the two-period quasi-axisymmetric reactor equilibrium of
[Wright & Ferraro (2024)](/sources/wright-2024.md), an a posteriori
analysis finds a magnetic well on all surfaces (§II; no method or figure
given), yet full-torus M3D-C1 runs show "interchange-like
pressure-driven" instabilities at the edge that destroy the flux surfaces
on Alfvénic time scales (Abstract, §III; see
[edge instabilities of an optimized QA reactor stellarator](/results/stellarator-edge-instability-qa.md)).
The paper defines the magnetic well loosely, as "the average curvature on
a magnetic surface", and equates possessing one with linear stability to
local pressure perturbations (§II); neither a Mercier nor a ballooning
evaluation, nor a mode-structure analysis, is shown. The tension with the
stability role of the well is recorded under *Contradictions*.

## Interchange modes as a reduced-MHD benchmark

Ramasamy et al. use ideal interchange modes in a five-period $l=2$
classical stellarator with ellipticity ratio 1.6, low shear and $\iota$
between 0.64 and 0.71 crossing $2/3$, to test JOREK3D's
[stellarator reduced MHD](/methods/stellarator-reduced-mhd.md) against the
full-MHD code [CASTOR3D](/software/castor3d.md) at
$\eta=1.93\times10^{-8}\ \Omega$ m and without viscosity, approaching the
ideal limit ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.2,
Table 2):

* **Incompressible ($\Gamma=0$).** The $(15,10)$ mode grows to about
  $1.0\times10^5\ \mathrm s^{-1}$ at $\beta\approx0.86\,\%$; the reduced
  model without parallel flow "agrees very well with full MHD", including
  the marginal-stability point (Fig. 5a).
* **Compressible ($\Gamma=5/3$).** Without parallel flow the reduced model
  is too stable (about $0.7$ against $1.0\times10^5\ \mathrm s^{-1}$ for
  $n=15$ near $\beta\approx1\,\%$, read from the figure); with parallel
  flow it agrees (Fig. 5b).
* **Full torus, $\beta=0.86\,\%$.** With parallel flow all modes $n=2$ to
  15 agree with CASTOR3D within 10 %, the $n=2$ structure matching the
  $(3,2)$ mode in its four largest harmonics. Without parallel flow the
  error grows as $n$ decreases and the $n<7$ modes, notably $(3,2)$, are
  not observed (Fig. 7). The authors explain this as artificial compression
  of radially broad, global modes, "similar to the axial compression of a
  tube of fluid" (§3.2).
* **Field compression.** Since the error with parallel flow does not grow
  as $n$ decreases, the eliminated fast-magnetosonic (field-compression)
  terms "are not playing an important role in the given test case". This
  answers, for this case, the concern of Graves et al. (2019) that reduced
  models stabilize compressible modes in low-shear regions artificially
  (§2.3, §3.2).
* A $(7,5)$ external mode near the boundary interferes with the internal
  modes and limits the benchmark to $\beta\le0.86\,\%$ (§3.2, Fig. 6).

## Quasi-interchange

The $1/1$ quasi-interchange is the interchange-like limit of the internal
kink in a low-shear core with $q\approx1$. Neglecting the parallel velocity
overestimates its growth rate by a factor $\sqrt{1+2q_s^2}$, $q_s$ the
safety factor at the mode surface (Waelbroeck 1989, cited by
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI, as an analogy for
the JOREK3D tearing gap). At high β the Wesson quasi-interchange model is
offered as an alternative to Kadomtsev reconnection for sawtooth crashes
([Zhou et al. (2023)](/sources/zhou-2023.md), §I; see
[sawtooth crash](/definitions/sawtooth-crash.md)), and flux pumping by a
$1/1$ quasi-interchange can hold $q_0\ge1$
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.4; see
[magnetic flux pumping](/definitions/magnetic-flux-pumping.md)).

[Zhang et al. (2025)](/sources/zhang-2025.md) characterize the mode in
full visco-resistive JOREK MHD of the sawtooth-free ASDEX Upgrade hybrid
discharge #36663 (§1, §2.2, §3.2, §3.4, Figs. 6, 12):

* **Drive and structure.** An ideal, pressure-gradient-driven instability
  of shear-free equilibria with $q_0\simeq1$ (Wesson 1986, as cited). Its
  $n=1$ flow is a core-wide convection cell, "quite distinct" from the
  internal kink, whose flow peaks at $q=1$.
* **Growth.** $\gamma=19.46\ \mathrm{ms}^{-1}$ for an initial $q_0=1.04$;
  the growth rate is "very sensitive to the initial value of $q_0$", the
  saturated state is not. $n=2$–4 are driven only by coupling.
* **Model requirement.** Full rather than reduced MHD is used because the
  mode has $B\,\delta B_\parallel/\mu_0\sim-\delta p$ (citing Pamela et al.
  2020).
* **Saturated state.** The mode clamps the axisymmetric $q_0$ at about
  0.99 over $s<0.3$ ($s=\sqrt{\psi_N}$) for hundreds of milliseconds,
  through a slow negative dynamo of a few mV/m; the core holds two twisted
  $1/1$ flux tubes, the original one with local $q_0\approx1.04$ (topology
  unchanged, ideal) and a new island-like one with local $q_0\approx0.97$,
  which the authors read as a combination of the $1/1$ ideal
  quasi-interchange and the $1/1$ resistive tearing mode (see
  [resistive internal kink](/definitions/resistive-internal-kink.md)).
  The value of "$q_0$" in their time traces is taken at $s=0.1$, not on
  axis (Fig. 9c).

## Contradictions

* **Does flux pumping hold $q_0\ge1$?** *Open.* Hoelzl et al. (2024, §4.4)
  summarize flux pumping by the quasi-interchange as keeping $q_0\ge1$.
  Zhang et al. (2025), the primary JOREK study of an experimental case,
  with authors in common, find a clamped axisymmetric $q_0\approx0.99$ and
  a local $q_0\approx0.97$ in the reconnected flux tube; only the original
  tube keeps 1.04 (§3.4, Figs. 9, 12). The paper does not comment on the
  review's wording. The normative entry is on
  [magnetic flux pumping](/definitions/magnetic-flux-pumping.md).
* **Interchange-like instability with a magnetic well on every surface.**
  *Open.* Wright & Ferraro (2024) report a well on all surfaces (§II) and
  call the edge instability "interchange-like pressure-driven" (Abstract).
  On this page the well is the stabilizing term a low-shear stellarator
  relies on. The two are not logically incompatible (compiler's reading):
  the well is one of four terms of $D_{\rm Merc}$, and in a configuration
  with a finite bootstrap current the current and geodesic terms can make
  $D_{\rm Merc}<0$ despite a well, while ballooning modes are not
  controlled by the well at all. Without a Mercier or ballooning
  evaluation of the equilibrium, the "interchange-like" classification is
  unverified; the entry stays open until a source computes it.

# Citations

* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — stellarator interchange benchmark, compressibility and parallel flow, Mercier limit exceeded experimentally.
* [Panici et al. (2023)](/sources/panici-2023.md) — Mercier criterion and its numerical sensitivity in VMEC and DESC.
* [Zeng et al. (2023)](/sources/zeng-2023.md) — Glasser–Greene–Johnson resistive-interchange parameter and its reversal.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — modified Mercier criterion for edge ballooning in reduced MHD.
* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — quasi-interchange overestimate without parallel velocity.
* [Zhou et al. (2023)](/sources/zhou-2023.md) — quasi-interchange sawtooth model at high β.
* [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — flux pumping by the quasi-interchange.
* [Sato & Todo (2026)](/sources/sato-2026.md) — Mercier-unstable LHD edge, resonant $(3,2)$ ideal interchange, its kinetic-ion stabilization, the $(1,1)$ interchange.
* [Wright & Ferraro (2024)](/sources/wright-2024.md) — interchange-like edge modes despite a magnetic well.
* [Zhang et al. (2025)](/sources/zhang-2025.md) — quasi-interchange structure, growth rate and saturated $q_0$ in ASDEX Upgrade.
