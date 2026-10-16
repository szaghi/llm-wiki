---
type: Method
title: "Wave-frame action-angle diagnostic of chirping modes"
description: "Phase-space diagnostic for frequency-chirping Alfvén modes that writes guiding-centre motion in action-angle variables and transforms to the frame of a single chirping wave, giving a momentum that stays exactly conserved while the frequency sweeps; applied to a MEGA chirping TAE it shows holes and clumps carrying the same resonant particles (convective transport)."
status: established
aliases: [action-angle chirping diagnostic, P2 slicing, wave-frame canonical transformation, phase-space bucket diagnostic]
tags: [energetic-particles, alfven-eigenmode, hybrid-kinetic, particles, numerics]
timestamp: 2026-10-16T20:00:00Z
---

# Wave-frame action-angle diagnostic of chirping modes

Nonlinear energetic-particle (EP) driven Alfvén modes can sweep their
frequency ([frequency chirping](/definitions/energetic-particle-mode.md)).
To see how the resonant EPs move in phase space during the sweep, a
hybrid-code output must be sliced on a surface that the particles do not
leave. [Hezaveh et al. (2022)](/sources/hezaveh-2022.md) (§3) construct
such a surface for a single chirping wave: a canonical transformation to
the wave frame yields a momentum $P_2$ that is an exact constant of motion
**even while the frequency changes**. Particles then stay on fixed-$P_2$
sub-layers, and the reduced dynamics is one-dimensional in a wave-frame
momentum $P_1$ and angle. The paper's substantive contribution is this
diagnostic, applied to a [MEGA](/software/mega.md) simulation of an
$n=6$ [TAE](/definitions/toroidal-alfven-eigenmode.md).

## Construction

All symbols below except the registry's are page-local.

1. **Unperturbed guiding-centre Hamiltonian.** Start from Littlejohn's
   guiding-centre Lagrangian and the canonical straight-field-line
   coordinates of Li, Breizman and Zheng (2016), as cited: a poloidal angle
   $\theta_c$, a toroidal angle $\zeta_c$ and the gyrophase. Their
   conjugate momenta are $P_{\theta_c}=q_h\psi+m_hv_{\parallel p}b_{\theta}$,
   $P_{\zeta_c}$ (a toroidal-flux term plus $m_hv_{\parallel p}b_\zeta$, with
   $b_\theta$, $b_\zeta$ covariant components of $\mathbf b$) and
   $(m_h/q_h)\mu$ (Eqs. 7–9). The Legendre transform gives the equilibrium
   Hamiltonian $H_0$.
2. **Action-angle variables.** Write $H_0=H_0(P_{\tilde\theta},P_{\tilde\zeta},P_{\tilde g})$
   with angles $\tilde\theta$, $\tilde\zeta$, $\tilde g$ and transit
   frequencies $\omega_{\tilde\theta}=\partial H_0/\partial P_{\tilde\theta}$,
   $\omega_{\tilde\zeta}=\partial H_0/\partial P_{\tilde\zeta}$ (Eqs. 10–11).
   The paper calls these the "bounce" and "precession" frequencies, although
   the analysed particles are passing; they are the poloidal and toroidal
   transit frequencies.
3. **Isolated resonance.** The perturbation is a sum of orbit-averaged
   harmonics with wave phase $\varphi_{\mathrm w}(t)$, $\dot\varphi_{\mathrm w}=\omega(t)$.
   Near one resonance
   $$\omega=n\,\omega_{\tilde\zeta}+\ell_{\mathrm r}\,\omega_{\tilde\theta},$$
   with integer $\ell_{\mathrm r}$ (Eq. 25; the paper's $p$, and its $l=p/h$
   for harmonic $h=1$), the perturbation depends on the angles only through
   $\ell_{\mathrm r}\tilde\theta+n\tilde\zeta-\varphi_{\mathrm w}(t)$ (Eqs. 12–14).
4. **Wave-frame transformation.** The type-2 generating function
   $$G_2=P_1\left[\ell_{\mathrm r}\tilde\theta+n\tilde\zeta-\varphi_{\mathrm w}(t)\right]+P_2\tilde\zeta+P_3\tilde g$$
   (Eq. 15) gives the wave-frame angle
   $\vartheta_{\mathrm w}=\ell_{\mathrm r}\tilde\theta+n\tilde\zeta-\varphi_{\mathrm w}(t)$
   and the momenta
   $$P_1=\frac{P_{\tilde\theta}}{\ell_{\mathrm r}},\qquad P_2=P_{\tilde\zeta}-\frac{n}{\ell_{\mathrm r}}P_{\tilde\theta},\qquad P_3=P_{\tilde g}.$$
   The new Hamiltonian depends on $\vartheta_{\mathrm w}$ only, so $P_2$ and
   $P_3$ are constants whatever $\varphi_{\mathrm w}(t)$ does (Eqs. 16–17).

*Compiler's check, not a source claim.* The paper prints
$P_2=P_{\tilde\zeta}+(n/\ell_{\mathrm r})P_{\tilde\theta}$. Differentiating the
printed $G_2$ gives the minus sign above, and the paper's own numbers agree
with the minus sign: with $n=6$, $\ell_{\mathrm r}=-6$,
$P_\phi\approx155$ and $P_{\tilde\theta}\approx-115$ (Fig. 8), the minus sign
gives $P_2\approx40$, matching the analysed slice $P_2\approx39$, while the
printed sign gives about 270. Eq. 17 also omits the
$\partial G_2/\partial t=-\omega(t)P_1$ term of a time-dependent
transformation; that omission does not affect the conservation of $P_2$.
Both points are recorded on the Source page.

## Numerical action and sampling

$P_{\tilde\theta}$ has no closed form. For $\mu=0$ particles it is fitted as
a 2D polynomial in $\sqrt{\mathcal E}$ and $P_{\tilde\zeta}$, because for
highly passing particles both transit frequencies scale as
$\sqrt{\mathcal E}$. The fit is constrained by
$\partial P_{\tilde\theta}/\partial\mathcal E=1/\omega_{\tilde\theta}$ and
$\partial P_{\tilde\theta}/\partial P_{\tilde\zeta}=-\omega_{\tilde\zeta}/\omega_{\tilde\theta}$,
evaluated from orbits traced in the equilibrium, and the least-squares
problem is solved with CVX (Eqs. 18–21). Markers are recorded when they
cross the midplane on the low-field side ($Z=0$, $R>R_0$), where the
canonical angles coincide with the geometric ones and
$P_{\tilde\zeta}=P_\phi$ (§3). A Poincaré-like plot in
$(\vartheta_{\mathrm w},P_1)$ on a thin $P_2$ window, with markers coloured
by their initial $P_1$, then shows where each particle has gone.

## Application: chirping $n=6$ TAE in MEGA

The case is a circular, uniform-density plasma with aspect ratio
$R_0/a=3.2$ (printed as "inverse aspect ratio"), linear $q$ from 1.0 to 1.3,
and an isotropic slowing-down EP population with on-axis $\beta_h=0.6\%$
(§4, Eq. 22). The linear TAE has $\omega/\omega_A=0.4553$, drive
$\gamma_l/\omega_A=0.012$ and background damping $\gamma_d/\omega_A=0.0053$
(so $\gamma_d/\gamma_l=0.44$), obtained by extrapolating the linear net
growth rate to $\beta_h=0$ (§4.1, Fig. 3; $\omega_A=v_A/R_0$ on axis).
The δf weights localize on the co-passing resonance
$\ell_{\mathrm r}=-m=-6$ (§4.2, Fig. 6). Findings:

- **$P_2$ is conserved and $C$ is not.** For a tracked up-chirping particle,
  $\Delta P_2\approx0$ while $\Delta P_\phi\approx-6$ (normalized units) over
  $t\omega_A=12$–3722. The invariant
  $C=\omega P_\phi-n\mathcal E$, evaluated at the fixed linear frequency and
  used by White et al. (2020) as cited, drifts to
  $\Delta C/\omega\approx+0.8$; "slices of C = const do not represent the
  most appropriate sub-layers" during long-range chirping (§4.4, Fig. 10).
  The evidence is one tracked particle.
- **Convective transport.** Holes form on the down-chirping side and clumps
  on the up-chirping side of the flattened region and move in phase space.
  The colour labels show that "the BGK-type chirping wave carries the EPs in
  a moving phase-space bucket in a convective way" rather than perturbing
  them locally and leaving them behind (§4.4, Fig. 9). By $t\omega_A=2477.8$ the
  up and down branches have swept $+13.55\%$ and $-11.33\%$ in frequency.
- **Survival in the continuum.** Holes and clumps formed in the gap "survive
  even in the shear Alfvén continuum" once the chirping frequencies leave
  the gap (§5, Figs. 5, 9).

The paper does not compare with another code. The particle data of
Figs. 9–10 extend beyond the end of the base run and therefore come from
the run with raised dissipation (inferred on the Source page).

## Relation to other slicing choices

- For $n=0$ modes (EGAMs) $P_\phi$ itself is conserved, as used by Wang,
  Todo and Kim (2013), as cited; $P_2$ generalizes that to $n\ne0$
  (implied in §1).
- Wang X.Q. et al. (2020), as cited, find the dominant perturbation on
  different $(\mathcal E,P_\phi)$ slices at fixed $\mu$ as the frequency
  changes; Hezaveh et al. instead keep the same particles on one $P_2$
  slice. The difference is one of slicing variables; the paper does not
  frame it as a contradiction.

## Contradictions

**Choice of phase-space invariant during chirping.** Recorded, attributed.
[Hezaveh et al. (2022)](/sources/hezaveh-2022.md) (§4.4, Fig. 10) show
that $C=\omega P_\phi-n\mathcal E$, used by White et al. (2020) (not
ingested; as cited), is not conserved once the frequency chirps, while
$P_2$ is. The two claims are compatible within their assumptions: $C$ is
exact for a fixed-frequency wave, $P_2$ for a single resonance of a wave of
arbitrary $\omega(t)$. The disagreement is on which slice is appropriate for
long-range chirping, and it rests on one tracked particle. The same entry
is listed on [energetic particle mode](/definitions/energetic-particle-mode.md).

# Citations

- [Hezaveh et al. (2022)](/sources/hezaveh-2022.md): the construction (§3, Eqs. 7–21), the MEGA chirping-TAE application (§4), the comparison with $C$ (Fig. 10).
