---
type: Method
title: "Integrating cooling and chemistry source terms"
description: "How codes advance stiff, point-local radiative cooling and non-equilibrium chemistry operator-split from the hydrodynamics: Townsend's exact integration of the isochoric cooling step for a temperature-only cooling function, the multiple-root failure of implicit cooling updates, and sequential first-order backward-difference chemistry updates sub-cycled under a priori (Grackle, Enzo) or a posteriori (RAMSES-RT) 10% change limits."
status: established
aliases: [radiative cooling integration, exact integration scheme, EI scheme, Townsend cooling, cooling sub-cycling, thermochemistry integration, 10% rule]
tags: [time-integration, cooling, chemistry, radiation]
timestamp: 2026-10-12T00:00:00Z
---

# Integrating cooling and chemistry source terms

Radiative cooling and non-equilibrium chemistry are point-local source
terms whose time scales can be far shorter than the hydrodynamic step.
The codes in the bundle split them from the hydrodynamics and integrate
them cell by cell, either exactly or by sub-cycling.

## Operator splitting

[Townsend (2009)](/sources/townsend-2009.md) (§§1–2, eqs. 1–3) writes the
ideal-gas pressure equation with optically thin losses,
$\frac{Dp}{Dt} - \frac{\gamma p}{\rho}\frac{D\rho}{Dt} = -(\gamma-1)n_{\mathrm e}n_{\mathrm H}\Lambda(T)$,
and splits it into an adiabatic part, applied with the mass and momentum
updates, and a cooling part applied afterwards at constant density
("e.g., Mignone 2005"). Keeping the advection stage adiabatic keeps
characteristic Godunov schemes such as PPM usable (footnote 1). The paper
asserts that the isochoric stage also handles isobaric systems such as
cooling flows; the splitting error itself is neither analysed nor tested.
[Grackle](/software/grackle.md) likewise receives a host time step and
updates species and internal energy in place, point by point
([Smith et al. (2017)](/sources/smith-2017.md), §3.2, §7.2.1), and
RAMSES-RT splits its thermochemistry from both the radiation transport
and the Euler equations
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3, §5).

## Exact integration of a temperature-only cooling function

With $p = n_{\mathrm{tot}} k_{\mathrm B}T$ and constant mean molecular weight $\mu$ (mass per particle $\mu m_{\mathrm H}$), the
isochoric cooling step for the cell average $T_i$ is the ODE
$$\frac{dT_i}{dt} = -\frac{(\gamma-1)\rho_i\,\mu}{k_{\mathrm B}\,\mu_{\mathrm e}\,\mu_{\mathrm H}\,m_{\mathrm H}}\,\Lambda(T_i),\qquad t_{\mathrm{cool}} = \left[\frac{(\gamma-1)\rho_i\,\mu\,\Lambda(T_i^n)}{k_{\mathrm B}\,\mu_{\mathrm e}\,\mu_{\mathrm H}\,m_{\mathrm H}\,T_i^n}\right]^{-1}$$
([Townsend (2009)](/sources/townsend-2009.md), eqs. 5, 9, 13), where
$\mu m_{\mathrm H}$, $\mu_{\mathrm e}m_{\mathrm H}$, $\mu_{\mathrm H}m_{\mathrm H}$ are the mass per particle, per
electron and per hydrogen nucleus (Townsend writes these dimensional
masses as $\mu$, $\mu_{\mathrm e}$, $\mu_{\mathrm H}$; the registry's are
dimensionless, hence the factor $m_{\mathrm H}$). Constant $\mu$ is called "a reasonable
approximation for temperatures $\gtrsim10^4$ K" and can fail far from
ionization equilibrium (§2).

Because $\Lambda$ depends on $T$ alone the ODE is separable. With the
temporal evolution function
$$Y(T) = \frac{\Lambda(T_{\mathrm{ref}})}{T_{\mathrm{ref}}}\int_T^{T_{\mathrm{ref}}}\frac{dT'}{\Lambda(T')}$$
($T_{\mathrm{ref}}$ arbitrary), the **exact integration (EI)** update is
$$T_i^{n+1} = Y^{-1}\!\left[Y(T_i^n) + \frac{T_i^n}{T_{\mathrm{ref}}}\frac{\Lambda(T_{\mathrm{ref}})}{\Lambda(T_i^n)}\frac{\Delta t}{t_{\mathrm{cool}}}\right]$$
(§3.3, eqs. 24–26). It solves the semi-discrete cooling ODE exactly for
any $\Delta t$; the error of the advection–cooling split remains.
* **Closed forms** (Appendix, eqs. A1–A7): for a power law
  $\Lambda = \Lambda_{\mathrm{ref}}(T/T_{\mathrm{ref}})^{\alpha_{\mathrm c}}$,
  $Y(T) = \frac{1}{1-\alpha_{\mathrm c}}\left[1-(T_{\mathrm{ref}}/T)^{\alpha_{\mathrm c}-1}\right]$
  ($\ln(T_{\mathrm{ref}}/T)$ for $\alpha_{\mathrm c} = 1$), with an explicit inverse.
  For a piecewise power law the segment constants follow a downward
  recurrence from the top node. Mignone's (2005) analytic cooling is the
  power-law special case (§3.3).
* **Requirement:** $\Lambda = \Lambda(T)$ only, with $1/\Lambda$
  integrable in closed form, "rarely an issue" for piecewise power-law or
  polynomial fits (§5). Extension to non-equilibrium ionization networks
  "is not yet clear" (§2).

## Explicit and implicit updates

* **Explicit** (§3.1, eqs. 11–15): forward Euler gives
  $T_i^{n+1} = T_i^n(1 - \Delta t/t_{\mathrm{cool}})$; second-order
  Runge–Kutta adds one $\Lambda$ evaluation. Both depart strongly from the
  exact solution as $\Delta t\to t_{\mathrm{cool}}$ (Fig. 1).
* **Implicit updates are not robust** (§3.2, eqs. 16–21, Figs. 2–4).
  Backward Euler and Crank–Nicolson need a root-find (secant with
  bisection fallback, or Brent, to a fractional change below $10^{-4}$).
  At $T_i^n = 10^6$ K and $\Delta t = 0.3\,t_{\mathrm{cool}}$ the
  backward-Euler equation has **five** roots (Fig. 3); the update
  underestimates $T$ for $0.3$–$0.7\,t_{\mathrm{cool}}$, overestimates it
  above, and jumps between roots as $\Delta t$ varies; Crank–Nicolson
  jumps over a smaller range. The paper calls the "unconditionally stable"
  reputation of implicit cooling (Strickland & Blondin 1995; Pittard et
  al. 2004; Stone et al. 1997, none ingested) "misplaced": von Neumann
  stability is a linear result. It asserts, without a hydrodynamic
  demonstration, that root-jumping makes neighbouring cells cool to
  different temperatures and drives spurious flows.
* **Time-step interplay** (§4, eqs. 28–30): with a Courant step and
  subsonic post-shock flow, $\Delta t/t_{\mathrm{cool}}\lesssim1/N$, $N$
  the number of cells across the cooling layer. A resolved cooling layer
  makes every scheme accurate; non-EI schemes fail when it is
  under-resolved. A limiter on the anticipated fractional change of
  temperature or pressure per step is mentioned as an option, with no
  threshold given.

**Measured** (§4, Table 1): one cooling step on a frozen steady radiative
shock (Strickland & Blondin 1995 profile), Courant number 1, upstream Mach
3, 10 and 100, $N = 1, 10, 100$ cells, error relative to EI. At $N = 10$
all schemes are below 10% except first-order explicit at Mach 3 (14.1%);
at $N = 100$ all are below 1%; at $N = 1$ the implicit schemes reach
99.9% at Mach 100. First-order explicit costs about 100 ns per cell;
second-order explicit and EI about twice that; the implicit schemes 2.5–12
times. EI is "the cooling scheme of choice" for simple, fast optically thin
losses, with ionization-tracking treatments (Mignone et al. 2007) still the
state of the art for fidelity (§5). No time-dependent hydrodynamic run and
no convergence order are reported.

## Sequential backward-difference chemistry with sub-cycling

When species are evolved, the codes use the fixed-order sequential update
of Anninos et al. (1997):
* **Grackle** ([Smith et al. (2017)](/sources/smith-2017.md), §3.2,
  eqs. 5–9, 11): each species obeys $\partial_t n_i = C_i - D_in_i$ and is
  advanced by $n_i^{\mathrm{new}} = (C_i\Delta t_{\mathrm{sub}} + n_i^{\mathrm{old}})/(1 + D_i\Delta t_{\mathrm{sub}})$,
  in a fixed order, each using the densities already updated; a true BDF
  scheme is not implemented because $C_i$, $D_i$ at the advanced time are
  hard to evaluate. The authors cite Anninos et al. (1997) for higher-order
  alternatives not being better "for the level of accuracy required"
  (asserted). Chemistry and cooling share "a simple first-order
  integrator".
* **Enzo** ([Bryan et al. (2014)](/sources/bryan-2014.md), §6.1,
  §6.2.1): one Jacobi iteration of backward Euler (semi-implicit, first
  order), H$^-$ and H$_2^+$ set to equilibrium.
* **RAMSES-RT** ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3.3,
  App. A): photon densities and fluxes, thermal energy and the H II,
  He II and He III fractions are updated sequentially in a fixed order,
  each semi-implicit in itself.

**Step control: the 10% rules.**

| code | rule | kind |
|---|---|---|
| Grackle | sub-step $0.1\min(n_{\mathrm H}/\dot n_{\mathrm H}, n_{\mathrm e}/\dot n_{\mathrm e})$ and $0.1\,e/\dot e$; numerical derivatives after 50 sub-steps | a priori |
| Enzo | at most 10% change of the electron fraction per sub-cycle, and at most 10% of the cooling time | a priori |
| RAMSES-RT | redo a sub-step with half the step if any quantity changes by more than 10%; double the next below 5% | a posteriori |

Sources: [Smith et al. (2017)](/sources/smith-2017.md), eqs. 9, 11;
[Bryan et al. (2014)](/sources/bryan-2014.md), §6.2.1;
[Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3.3. In RAMSES-RT
photons are therefore conserved only "at the 10% level" in the
thermochemistry, while the transport step conserves them (§3.3,
footnote 4). Grackle's switch to numerical derivatives after 50 sub-steps
targets near-equilibrium stalling and overshoot
([Smith et al. (2017)](/sources/smith-2017.md), §3.2). In Grackle's
benchmark a non-equilibrium solve takes 2.67 sub-cycles on average and
cost scales with the sub-cycle count (§7.2.2). None of the three papers
presents a time-step convergence study or a comparison with a stiff
reference integrator.

**Resolution.** Grackle requires the cooling length $c_s t_{\mathrm{cool}}$
to be resolved, or losses are over-predicted in a run-away cycle
([Smith et al. (2017)](/sources/smith-2017.md), §8.1); Townsend's
$\Delta t/t_{\mathrm{cool}}\lesssim1/N$ argument makes the same point for
cooling layers ([Townsend (2009)](/sources/townsend-2009.md), §4). Enzo
can refine where the cooling time is shorter than the sound-crossing time
([Bryan et al. (2014)](/sources/bryan-2014.md), §3.6).

# Citations

1. [Townsend (2009)](/sources/townsend-2009.md), §§1–5, eqs. 1–30,
   A1–A7, Table 1, Figs. 1–4 (arXiv v2).
2. [Smith et al. (2017)](/sources/smith-2017.md), §§3.2, 4, 7.2, 8.1,
   eqs. 5–11 (arXiv v2).
3. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§3, 3.3, 5,
   App. A.
4. [Bryan et al. (2014)](/sources/bryan-2014.md), §§3.6, 6.1, 6.2.1
   (arXiv v1).
