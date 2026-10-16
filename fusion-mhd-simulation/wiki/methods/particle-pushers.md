---
type: Method
title: "Particle pushers: Boris, slow-manifold Boris, guiding-centre and gyrokinetic"
description: "Orbit integrators that advance the markers of the kinetic modules attached to MHD codes: the full-orbit Boris scheme, its slow-manifold variant for Pauli particles with time steps above the gyro-period, its massless limit for tracing runaway-electron characteristics, RK4 and variational guiding-centre integrators, and gyrokinetic gyrocentre equations with N-point gyroaverages, with their conservation properties as measured in this bundle's sources."
status: established
aliases: [Boris pusher, Boris–Buneman, slow manifold Boris, guiding-centre pusher, gyrocentre pusher, orbit integrator]
tags: [particles, energetic-particles, hybrid-kinetic, numerics, time-integration, gpu]
timestamp: 2026-10-16T12:00:00Z
---

# Particle pushers: Boris, slow-manifold Boris, guiding-centre and gyrokinetic

The kinetic modules of MHD codes advance markers in the fields of the MHD
solution. These modules handle energetic particles (EPs), impurities,
neutrals, runaway electrons and ITG ions. Four families of orbit integrator
appear in this bundle. They differ in what they resolve (gyration or only the
guiding centre), in the field derivatives they need, and in what they conserve
over long times. Each choice sets the kinetic ordering of a
[hybrid kinetic-MHD model](/methods/hybrid-kinetic-mhd.md).

## Full orbit: the Boris scheme

The Boris scheme is a leapfrog that staggers positions on integer steps and
velocities on half steps:

$$\frac{\mathbf x_p^{l}-\mathbf x_p^{l-1}}{\Delta t}=\mathbf v_p^{l-1/2},\qquad\frac{m_h}{q_h}\,\frac{\mathbf v_p^{l+1/2}-\mathbf v_p^{l-1/2}}{\Delta t}=\mathbf E(\mathbf x_p^{l})+\frac{\mathbf v_p^{l+1/2}+\mathbf v_p^{l-1/2}}{2}\times\mathbf B(\mathbf x_p^{l}).$$

The scheme is volume-preserving and solved explicitly
([Liu et al. (2022)](/sources/liu-2022.md), Eqs. 5–6, with the effective
field below set to $\mathbf E$). It retains all finite-orbit-width and
finite-Larmor-radius (FLR) effects. It must resolve the gyration, so the
time step is a fraction of the gyro-period.

- **JOREK.** JOREK pushes fast ions, impurities and neutrals with Boris in
  $(R,Z,\phi)$ coordinates, with a correction for the toroidal geometry. The
  local element coordinates are recovered by Newton iterations, and an RTree
  search locates particles that cross many elements. Following the particle in
  real space means that element crossings do not perturb the scheme
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.10).
  - *Accuracy.* On the 26-period banana-orbit benchmark of Qin and Kraus,
    Boris conserves energy close to machine precision, and its
    toroidal-momentum error scales as $\Delta t^2$ (§4.9, Fig. 31).
  - *Step sizes.* Fast ions take 100–1000 particle steps per fluid step
    (§2.10).
  - *EP runs.* The EP runs of
    [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§§II, IV.A) use a
    step of $2\times10^{-10}$ s. The growth rate is converged within 5% over
    50–200 steps per gyro-orbit (Fig. 2b). The text says
    "$2\cdot10^{-10}$ s ≈ 200$\tau_g$", which inverts the ratio shown on the
    figure axis.
  - *Neutrals.* The same Boris pusher (Qin 2013) moves JOREK's
    [kinetic neutrals](/methods/kinetic-neutral-model.md)
    ([Korving et al. (2023)](/sources/korving-2023.md), §IV A).
- **XTOR-K.** XTOR-K uses a Boris–Buneman full-orbit push with 24 steps per
  cyclotron gyration and 16 particle steps per fluid step, nested in a Picard
  iteration with the implicit fluid solver
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §6).

## Slow-manifold Boris (Pauli particles)

The slow-manifold Boris algorithm of Xiao and Qin (2021) applies the Boris
update above to the Pauli particle. The mirror force is folded into an
effective electric field,

$$\mathbf E\;\to\;\mathbf E-\frac{\mu}{q_h}\nabla B,$$

with $\mu$ held invariant. The time step can then exceed the gyro-period,
$\Delta t>2\pi/\Omega_h$, "as long as particles stay close to the slow
manifold" ([Liu et al. (2022)](/sources/liu-2022.md), §2, Eqs. 5–6).
Liu et al. print the effective field as $\mathbf E-\mu\nabla B$, without
the $1/q_h$; that is a force, not a field, and the dimensionally consistent
form is written here.

- **Initialization.** The scheme is bootstrapped by one RK4 guiding-centre
  step, $\mathbf v_p^{1/2}=(\mathbf x_p^1-\mathbf x_p^0)/\Delta t$. Without it,
  the markers oscillate across the slow manifold. The weight equation uses the
  average of the two half-step velocities (ibid., footnote 1).
- **Derivatives.** The curvature drift comes out of the Boris rotation
  itself, so only first derivatives of the finite-element field polynomials
  are needed, for $\nabla B$. RK4 guiding-centre integration needs second
  derivatives for the curvature, which profiling shows dominates its cost
  (ibid., §2; no numbers given).
- **Conservation.** The test uses a DIII-D-like static field. RK4 is run at
  $\Delta t=3.2\times10^{-7}$ s and Boris at a 4× smaller step, at similar
  cost, to 2 s.
  - RK4 errors in $P_\phi$ and $\mathcal E$ grow secularly, to about
    $5.5\times10^{-3}$ and $-1.5\times10^{-3}$ relative for a passing
    particle.
  - Boris errors stay bounded oscillations of about $10^{-4}$.
  - The benefit is "only significant for long time simulations
    ($t>500$ ms)"; RK4 is more accurate over short times (ibid., §2,
    Fig. 1, values read off the plot).
- **GPU.** The Boris push on GPUs is 1.23× faster than GPU RK4 at a 4×
  smaller step (ibid., §5).
- **Proposed use.** Liu et al. propose the scheme for
  [runaway electrons](/definitions/runaway-electrons.md) (§7).

### Massless limit for runaway-electron characteristics

[Liu et al. (2021)](/sources/liu-2021.md) (§4, Eqs. 15–19) trace the
characteristics of the M3D-C1 runaway-electron density with a "modified
Boris algorithm". They subtract $\mathbf v_E$ before the rotation and add
it back after. In the limit $m\to0$ the rotation becomes a reflection that
keeps the velocity component along $\mathbf b$ and reverses the
perpendicular one. The scheme uses the same RK4 bootstrap and runs at a 4×
smaller step than RK4, as in the slow-manifold test above.

In a static DIII-D field it keeps the total runaway current within about 1%
over 0.2 ms, where RK4 drifts by about 20%. The flux error of a single tracer
stays bounded, while RK4's grows secularly (Fig. 2, read off the plot). The
equations and the root selection are on
[advection by characteristics](/methods/runaway-electron-advection-by-characteristics.md).

## Guiding-centre (drift-kinetic) integration

The drift-kinetic guiding-centre equations follow from Littlejohn's
Lagrangian:

$$\frac{\mathrm d\mathbf X}{\mathrm dt}=\frac{1}{B^*_\parallel}\left[v_{\parallel p}\mathbf B^*-\mathbf b\times\left(\mathbf E-\frac{\mu}{q_h}\nabla B\right)\right],\qquad m_h\frac{\mathrm dv_{\parallel p}}{\mathrm dt}=\frac{1}{B^*_\parallel}\,\mathbf B^*\cdot\left(q_h\mathbf E-\mu\nabla B\right),$$

$$\mathbf B^*=\mathbf B+\frac{m_hv_{\parallel p}}{q_h}\nabla\times\mathbf b,\qquad B^*_\parallel=\mathbf B^*\cdot\mathbf b,$$

in a 5D phase space with ignorable gyrophase
([Liu et al. (2022)](/sources/liu-2022.md), Eqs. 1–4, the M3D-K form).
M3D-C1-K integrates them by RK4.

JOREK offers RK4 and the modified variational integrator of Qin for
guiding centres ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.9,
Fig. 31). On the banana-orbit benchmark:

- RK4 error scales between $\Delta t^4$ and $\Delta t^5$.
- The variational integrator's energy error scales as $\Delta t^2$, and its
  error stays bounded in time. It becomes smaller than RK4's for integration
  times $\gtrsim0.1$ s. It is unstable above about 1000 gyro-periods per
  step.

JOREK also has a relativistic full-orbit and guiding-centre tracer for
runaway electrons. It agrees with ASCOT5 on 5000 passing 1 MeV electrons in
JET thermal-quench fields (ibid., §4.10, Fig. 32).
[MEGA](/software/mega.md) is drift-kinetic, with FLR added as an ad-hoc
$N$-point gyroaverage ([Vlad et al. (2025)](/sources/vlad-2025.md), §4).

## Gyrokinetic gyrocentre integration

Gyrokinetic pushers replace the perturbed fields in the guiding-centre
equations by their gyroaverages $\langle\cdot\rangle$. In
[GMEC](/software/gmec.md) the drift becomes

$$\frac{\mathrm d\mathbf X}{\mathrm dt}=\frac{1}{B^*_\parallel}\left\{v_{\parallel p}\mathbf B^*-\mathbf b\times\left[\langle\delta\mathbf E\rangle-\frac{\mu}{q_h}\nabla\left(B+\langle\delta B\rangle\right)\right]\right\},$$

with $\mathbf B^*$ now including $\langle\delta\mathbf B\rangle$, and with
$\delta\mathbf E=-\nabla\delta\Phi-\partial_t\delta A_\parallel\,\mathbf b$.
GMEC integrates the equations by RK4 at the MHD step
([Liu et al. (2024)](/sources/liu-2024.md), Eqs. 5–7, after Fu 2006).

- **Gyroaverage.** It uses $N=4$ points. GMEC adapts the GTC scheme to
  non-orthogonal field-aligned coordinates and approximates the gyro-plane
  by the poloidal plane (Eqs. 13–14). M3D-C1-K uses the same 4-point
  average, written
  $\langle\delta\mathbf B\rangle(\mathbf X)\approx\tfrac14\sum_{j=1}^4\delta\mathbf B(\mathbf X+\boldsymbol\rho_{L,j})$,
  for its FLR option ([Liu et al. (2022)](/sources/liu-2022.md), Eq. 14).
- **Verification.** The tests cover orbit widths and the bounce, transit and
  precession frequencies. They agree with analytic $O(\varepsilon^2)$
  formulas and the FP3D code. The relative variations of $\mathcal E$ and
  $P_\phi$ stay below $10^{-7}$ over $10^4\tau_A$ at $\Delta t=0.01\tau_A$
  ([Liu et al. (2024)](/sources/liu-2024.md), §III A).
- **Cost.** Gyroaveraging dominates the cost. The gyrokinetic run costs
  about 8× the drift-kinetic one (Table I).
- **HYMAGYC.** HYMAGYC integrates Brizard's gyrocentre equations, expanded to
  $O(\epsilon^2)$ and $O(\epsilon\epsilon_B)$ in $\rho_L$ over the density
  and field scale lengths, with an $N=32$-point gyroaverage
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §3, Eqs. A1–A4, written in
  Gaussian units).
- **ORB5.** ORB5 pushes its gyrocentres by RK4
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §5).
- **JOREK.** JOREK's gyrocentre option uses RK4 with an orbit-averaged
  electric field ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.9).

## FLR in benchmark results

In the linear growth rates of the
[NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md), FLR lowers $\gamma$
in MEGA, HYMAGYC with its $(R,Z)$ stress tensor, and ORB5. It raises
$\gamma$ in HYMAGYC with its $(s,\chi)$ stress tensor (174,606 →
199,841 s$^{-1}$). Its effect on the frequency has no common sign across
codes ([Vlad et al. (2025)](/sources/vlad-2025.md), §4, Table 2). Vlad et
al.'s general statement that FLR "typically" lowers growth rates (§7)
therefore fails for one of the four rows. On the
[ITPA TAE](/benchmarks/itpa-tae-benchmark.md), FLR roughly halves the
growth rate in both M3D-C1-K and GMEC
([Liu et al. (2022)](/sources/liu-2022.md), §6.2;
[Liu et al. (2024)](/sources/liu-2024.md), §III C).

## Contradictions

None on the integrators themselves. The three characterisations of RK4 are
consistent. Liu et al. (2022) report bounded slow-manifold Boris errors
against secular RK4 errors over 2 s. Liu et al. (2021) report the same
contrast for massless runaway tracers over 0.2 ms at equal cost. Hoelzl et
al. (2021) report the variational guiding-centre integrator beating RK4 only
beyond about 0.1 s. All three describe long-time secular drift of a
non-structure-preserving integrator.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): Eqs. 1–6 and 14; slow-manifold Boris; orbit-conservation test; GPU timings.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): JOREK Boris, RK4, variational and relativistic pushers; banana-orbit and ASCOT5 tests.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): the full-orbit EP push and its time-step convergence.
- [Korving et al. (2023)](/sources/korving-2023.md): the Boris pusher for kinetic neutrals.
- [Liu et al. (2024)](/sources/liu-2024.md): gyrokinetic RK4 push, 4-point gyroaverage in field-aligned coordinates, orbit verification.
- [Liu et al. (2021)](/sources/liu-2021.md): the massless-limit Boris integrator for runaway characteristics and its conservation test (§4, Fig. 2).
- [Vlad et al. (2025)](/sources/vlad-2025.md): the HYMAGYC, MEGA, ORB5 and XTOR-K pushers; the FLR effects in Table 2.
