---
type: Method
title: "Pressure coupling and current coupling"
description: "The two ways a hybrid kinetic-MHD code closes the bulk momentum equation with kinetic particles (energetic particles, or kinetic thermal ions): by the divergence of the kinetic pressure tensor or by the kinetic current; analytically equivalent in the perpendicular direction in the drift-kinetic limit, yet reported to differ in noise and suspected of driving nonlinear benchmark discrepancies."
status: established
aliases: [pressure-coupling scheme, current-coupling scheme, Park coupling, CGL pressure coupling]
tags: [hybrid-kinetic, energetic-particles, particles, mhd, numerics]
timestamp: 2026-10-16T16:51:00Z
---

# Pressure coupling and current coupling

In a [hybrid kinetic-MHD model](/methods/hybrid-kinetic-mhd.md) the
energetic particles (EPs) act on the bulk fluid through its momentum
equation. Two closures are in use, both going back to Park et al. (1992), as
cited by [Liu et al. (2022)](/sources/liu-2022.md) (§4),
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§II) and
[Vlad et al. (2025)](/sources/vlad-2025.md) (§§1, 3). For energetic
particles both assume $n_h\ll n_i$; the kinetic-thermal-ion variants below
do not. Equations are written here in SI. Liu et al. (2022) write
$\mathbf J=\nabla\times\mathbf B$ with $\mu_0=1$.

## Pressure coupling

The momentum equation of bulk plus EPs is

$$\rho\left(\frac{\partial\mathbf v}{\partial t}+\mathbf v\cdot\nabla\mathbf v\right)+\frac{\partial\mathbf K_h}{\partial t}=\mathbf J\times\mathbf B-\nabla p-\nabla\cdot\mathsf P_h,$$

where $\mathbf J=\nabla\times\mathbf B/\mu_0$ is the total current and
$\mathbf K_h$ the EP momentum density
([Liu et al. (2022)](/sources/liu-2022.md), Eq. 19). The pressure tensor is
taken gyrotropic (CGL form),

$$\mathsf P_h=p_{\parallel h}\,\mathbf b\mathbf b+p_{\perp h}\,(\mathsf I-\mathbf b\mathbf b),\qquad p_{\parallel h}=m_h\!\int(\mathbf v\cdot\mathbf b)^2f_h\,d^3v,\qquad p_{\perp h}=\frac{m_h}{2}\!\int|\mathbf v\times\mathbf b|^2f_h\,d^3v,$$

([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II;
[Liu et al. (2022)](/sources/liu-2022.md), Eq. 19). With markers of weight
$w_p$ the tensor becomes a weighted marker sum with the field direction
$\mathbf b$ evaluated at each marker
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II). The variants
differ in which part of $\nabla\cdot\mathsf P_h$ they keep and in whether
they drop $\partial_t\mathbf K_h$.

- **M3D-K and M3D-C1-K** keep every component of $\nabla\cdot\mathsf P_h$
  and drop $\partial_t\mathbf K_h$ in all directions. For $\delta f$ runs,
  the equilibrium balance $\mathbf J_0\times\mathbf B_0=\nabla p_0+\nabla p_{h0}$
  (with an isotropic EP equilibrium pressure) is subtracted, so only
  $\nabla\cdot\delta\mathsf P_h$ enters
  ([Liu et al. (2022)](/sources/liu-2022.md), Eqs. 20–21).
- **Park et al. (1999)** keep only the perpendicular part, as cited by
  [Liu et al. (2022)](/sources/liu-2022.md) (§4). Liu et al. justify
  dropping the perpendicular $\partial_t\mathbf K_h$ by $n_h\ll n_i$ when
  both species $E\times B$-drift. They add that "in the parallel direction
  $\partial\mathbf K_h/\partial t$ cannot be safely ignored", although
  M3D-C1-K ignores it there too.
- **JOREK** adds $-(\nabla\cdot\mathsf P_h)_\perp$ to the right-hand side of
  the momentum equation, in both its reduced and full MHD models. The EPs
  are full-$f$, and $\mathbf J$ there is the total current of bulk and EPs
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), Eq. 2). Bogaarts et
  al. define $\mathsf P_h=m_h\int\mathbf v\mathbf v f_h\,d^3v$ as the
  uncentred second moment. With a mean EP flow this includes a
  Reynolds-stress part, which the paper does not discuss. The full (non-CGL)
  tensor "proved to be unstable and noisy", so the CGL form is used
  throughout. An earlier JOREK version used an isotropic scalar EP pressure
  in reduced MHD (Dvornova, cited ibid., §I).
- **XTOR-K** applies a kinetic pressure term in the perpendicular equation
  of motion only ([Vlad et al. (2025)](/sources/vlad-2025.md), §6).
- **HYMAGYC** computes $\nabla\cdot\mathsf P_h$ on the $(s,\chi)$ grid or on
  an auxiliary Cartesian $(R,Z)$ grid. The $(s,\chi)$ evaluation is prone to
  short-scale perpendicular noise and to numerical instability in the
  nonlinear phase. The coarser $(R,Z)$ grid acts as a filter: 121², 181² and
  361² grids are compared in Fig. 7
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §3).
- **GMEC** inserts the scalar EP pressure perturbation in the curvature term
  of the reduced-MHD vorticity equation,
  $$\frac{\partial\delta\varpi}{\partial t}=\dots+\frac{2\mu_0}{B}\,\mathbf b\times(\mathbf b\cdot\nabla\mathbf b)\cdot\nabla(\delta p_b+\delta p_h),$$
  where $\delta p_b$ is the bulk pressure perturbation
  ([Liu et al. (2024)](/sources/liu-2024.md), Eq. 1). The paper defines the
  scalar as $\delta p_h=(\delta p_{\parallel h}+\delta p_{\perp h})/2$, as
  printed (§II C). The usual isotropic average is
  $(\delta p_{\parallel h}+2\delta p_{\perp h})/3$, so this is recorded as
  an unusual printed definition, not corrected here.
- **M3D-C1-K with kinetic thermal ions** puts both ion tensors in the
  perpendicular momentum equation, $-\nabla_\perp\cdot\mathsf P_i-\nabla_\perp\cdot\mathsf P_h$
  with $\mathsf P_i=p_{\parallel i}\mathbf b\mathbf b+p_{\perp i}(\mathsf I-\mathbf b\mathbf b)$,
  and drops the fluid parallel-momentum equation, taking $\delta v_\parallel$
  from the markers ([Liu et al. (2022b)](/sources/liu-2022-b.md), Eq. 2.1,
  Eqs. 2.17–2.20; see [kinetic thermal ions](/methods/kinetic-thermal-ions.md)).
  Liu et al. (2022b) describe a thermal-ion version of Park et al. (1999) in
  which the fluid parallel-momentum equation carries
  $-\nabla_\parallel\cdot(\mathsf P_i+\mathsf P_h)-\nabla_\parallel p_e$
  (their Eq. 2.23) and $n_i$, $v_\parallel$ stay fluid. They call it "in
  principle" equivalent to their scheme, but in M3D-C1's sequential solve
  it lets the fluid and marker $\delta n$, $\delta v_\parallel$ drift apart
  and produces parasitic modes (§2). This description of Park et al. (1999)
  and the perpendicular-only one above (from Liu et al. 2022) are
  compatible: the perpendicular-only statement concerns the EP term of the
  perpendicular momentum balance, the Eq. 2.23 form the parallel equation
  of the thermal-ion version. Both are second-hand, Park et al. not being
  ingested.

## Current coupling

If the momentum equation describes the bulk plasma alone, the EPs enter
through their current density $\mathbf J_h$:

$$\rho\left(\frac{\partial\mathbf v}{\partial t}+\mathbf v\cdot\nabla\mathbf v\right)=(\mathbf J-\mathbf J_h)\times\mathbf B-\nabla p$$

([Liu et al. (2022)](/sources/liu-2022.md), Eq. 22; the printed equation
omits $\rho$ on the convective term). The EP current has three parts:
parallel streaming, the drift current
$q_h\int\mathbf v_d f_h$ with
$\mathbf v_d=\frac{m_hv_{\parallel p}^2}{q_hB}\nabla\times\mathbf b+\frac{\mu}{q_hB}\mathbf b\times\nabla B$,
and the magnetization current $\nabla\times\mathbf M_h$ obtained by a
pull-back transformation (Eqs. 23–24). Liu et al. omit the electric force
$-q_hn_h\mathbf E$ that Park et al. (1992, 1999) keep on the non-neutral
bulk plasma. Their argument (citing Zhao 2020) is that this force cancels
the $\mathbf J_h\times\mathbf B$ contribution of the EP $E\times B$ current.
[MEGA](/software/mega.md) uses current coupling
([Vlad et al. (2025)](/sources/vlad-2025.md), §4), with the momentum
equation in the form $(\mathbf J-\mathbf J_h)\times\mathbf B$ and the EP
current deposited as marker sums of the parallel-plus-curvature and
$\nabla B$ drift currents, minus the curl of $\mathbf b$ times the marker sum
of $\mu$, the magnetization current
([Hezaveh et al. (2022)](/sources/hezaveh-2022.md), Eqs. 1, 5–6). The EP
current contains no $E\times B$ drift "due to quasi-neutrality" (ibid., §2,
citing Todo & Sato 1998), which agrees with Liu et al.'s argument for
omitting $-q_hn_h\mathbf E$. For kinetic thermal ions MEGA writes the ion
perpendicular current through the marker pressures,
$$\mathbf J_i=\frac1B\left(p_{\parallel i}\nabla\times\mathbf b-p_{\perp i}\nabla\ln B\times\mathbf b\right)-\nabla\times\left(\frac{p_{\perp i}}{B}\mathbf b\right),$$
entering as $(\mathbf J-\mathbf J_i)\times\mathbf B$
([Sato et al. (2024)](/sources/sato-2024.md), Eqs. 20, 25), i.e. current
coupling expressed in the two pressure moments; the LHD runs of
[Sato & Todo (2026)](/sources/sato-2026.md) (pp. 2, 8) add energetic ions
to the same kinetic-thermal-ion MEGA. JOREK implemented it but
found it "too noisy to obtain useful results"
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II).
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§§2.10, 2.15) report both
schemes implemented in JOREK and an effort towards an *energy-conserving*
current-coupling scheme.

## Equivalence in the drift-kinetic limit

In the drift-kinetic limit, with the curvature and $\nabla B$ drifts above,
the EP Lorentz force reduces to the perpendicular part of the pressure-tensor
divergence:

$$\mathbf J_h\times\mathbf B=(\nabla\cdot\mathsf P_h)_\perp,\qquad\text{hence}\qquad(\mathbf J-\mathbf J_h)\times\mathbf B=\mathbf J\times\mathbf B-(\nabla\cdot\mathsf P_h)_\perp$$

([Liu et al. (2022)](/sources/liu-2022.md), Eq. 25). The same
$p_{\parallel h}$, $p_{\perp h}$ moments therefore serve both schemes.
Current coupling is then pressure coupling stripped of its component along
$\mathbf b$. Park et al.'s perpendicular-only pressure coupling "is exactly
the same as" Eq. 25 and equivalent to MEGA's simplified current coupling.
MEGA's simplification writes the equilibrium EP current force
$\mathbf J_{h0}\times\delta\mathbf B$ through $\nabla p_{h0}$, assuming
$\mathbf J_{h0}\perp\mathbf B_0$ and $\mathbf J_{h0}\times\mathbf B_0=\nabla p_{h0}$
(ibid., Eqs. 26–27).

*Compiler's check, not a source claim.* Liu et al. print the magnetization
as $\mathbf M_h=+p_{\perp h}\mathbf b/B$ and the result of Eq. 25 with a
trailing "$\times\mathbf b\times\mathbf b$". The diamagnetic magnetization
of gyrating particles is $-p_{\perp h}\mathbf b/B$. The form above is the
one consistent with the equilibrium relation
$\mathbf J_{h0}\times\mathbf B_0=\nabla p_{h0}$ that the same paper uses in
Eq. 27. Two chunk-2 sources print the magnetization current with the
diamagnetic sign, $-\nabla\times(p_\perp\mathbf b/B)$:
[Sato et al. (2024)](/sources/sato-2024.md) (Eq. 25, thermal ions) and
[Hezaveh et al. (2022)](/sources/hezaveh-2022.md) (Eq. 5, as
$-\nabla\times(\mathbf b\sum_p\mu w_p\,\cdot)$ over marker shape functions,
whose sum is $p_{\perp h}/B$). Both support the sign used above.

In M3D-C1-K the two schemes "give almost the same results" for every
simulation conducted ([Liu et al. (2022)](/sources/liu-2022.md), §4). The
paper shows this for the linear
[fishbone](/definitions/fishbone.md) (Fig. 3) and calls the two results
"equal" for the [ITPA TAE](/benchmarks/itpa-tae-benchmark.md) (§6.2,
Fig. 5). [Liu et al. (2022b)](/sources/liu-2022-b.md) (§2) restate,
citing Liu et al. (2022), that pressure coupling (M3D-C1-K) and current
coupling (MEGA) "are equivalent for calculating $v_\perp$", and apply this
to the kinetic-thermal-ion case.

## Energy exchange

Pressure coupling as implemented in JOREK "does not conserve energy exactly".
On the ITPA TAE, Bogaarts et al. (2022, §IV.A, Fig. 7) state that the energy
lost by EPs and gained by the fluid are "conserved rather well until the
saturation phase". Fig. 7b shows a relative mismatch of about $10^{-1}$
throughout the linear phase, rising to about 15% late. Reducing dissipation
by 10× lowers the late value only slightly. The authors blame the fixed
$n=0$ component and the resistive and viscous dissipation for the nonlinear
mismatch ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md)).

## Contradictions

**Pressure vs current coupling — analytic equivalence vs observed behaviour.** Open.
[Liu et al. (2022)](/sources/liu-2022.md) (§4, Eq. 25) derive that
current coupling equals perpendicular pressure coupling in the drift-kinetic
limit, given $n_h\ll n_i$, the neglect of $\partial_t\mathbf K_h$ and the
omission of $-q_hn_h\mathbf E$. They observe "almost the same results" from
the two schemes in M3D-C1-K (linear fishbone and TAE).
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§II) found current
coupling in JOREK "too noisy to obtain useful results"; no evidence is
shown in that paper.
[Vlad et al. (2025)](/sources/vlad-2025.md) (§§5, 7) name current coupling
(MEGA) versus pressure coupling (HYMAGYC, XTOR-K) as a candidate, unquantified
cause of MEGA's roughly 15× lower saturation energy and weaker EP
redistribution in the [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md).

The three statements are not logically incompatible, because their
assumptions differ in four ways:

- Liu et al.'s equivalence is analytic and drift-kinetic, and its
  confirmation is $\delta f$ and linear.
- JOREK's markers are full-$f$ and full orbit. There $\mathbf J_h$ must be
  deposited directly from gyrating markers, including the magnetization
  current, which is not reduced to the two pressure moments.
- Vlad et al.'s case is nonlinear, at a high EP fraction where the dropped
  inertia and $-q_hn_h\mathbf E$ terms are least negligible.
- MEGA differs from HYMAGYC in more than the coupling: the MHD is nonlinear
  rather than linear, and the EPs are drift-kinetic rather than gyrokinetic.

A same-code comparison would settle the question: one code, both schemes,
the nonlinear NLED-AUG case, and the same EP model. The comparison would
also need the full-$f$/full-orbit current-coupling noise measured against
marker number.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): Eqs. 19–27, the equivalence derivation and the M3D-C1-K comparisons.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): anisotropic CGL pressure coupling in JOREK; current coupling too noisy; energy exchange.
- [Vlad et al. (2025)](/sources/vlad-2025.md): the coupling choices of HYMAGYC, MEGA and XTOR-K; the coupling as a candidate cause of the discrepancies.
- [Liu et al. (2024)](/sources/liu-2024.md): pressure coupling through the reduced-MHD curvature term.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): both schemes in JOREK; the energy-conserving current coupling planned.
- [Liu et al. (2022b)](/sources/liu-2022-b.md): pressure coupling of kinetic thermal and fast ions; the thermal-ion Park scheme and its failure under sequential splitting.
- [Hezaveh et al. (2022)](/sources/hezaveh-2022.md): MEGA's current coupling and deposited EP current with magnetization term.
- [Sato et al. (2024)](/sources/sato-2024.md): MEGA's kinetic-thermal-ion current written through the pressure moments.
- [Sato & Todo (2026)](/sources/sato-2026.md): kinetic thermal and energetic ions together in MEGA.
