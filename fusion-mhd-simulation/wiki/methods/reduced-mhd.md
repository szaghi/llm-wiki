---
type: Method
title: "Reduced MHD for tokamaks"
description: "MHD models that restrict the magnetic field to a poloidal flux function plus a fixed toroidal field and the perpendicular flow to an E×B stream function, removing the fast magnetosonic wave; derived either by an aspect-ratio or flute ordering or, as in JOREK, by a Galerkin ansatz without geometric approximation; energy-conserving, not locally momentum-conserving, and inaccurate for pressure-driven internal kinks at finite β."
status: established
aliases: [RMHD, reduced magnetohydrodynamics, ansatz-based reduced MHD, Strauss reduced MHD]
tags: [mhd, reduced-mhd, tokamak, kink, code]
timestamp: 2026-10-16T20:00:00Z
---

# Reduced MHD for tokamaks

Reduced MHD replaces the full
[visco-resistive MHD model](/methods/visco-resistive-mhd-model.md) by a
system for a few scalar fields. The magnetic field is written as a fixed
toroidal field plus the poloidal field of a flux function, and the
perpendicular velocity as the $\mathbf E\times\mathbf B$ flow of a stream
function. With these restrictions the fast magnetosonic wave disappears,
which removes the stiffest time scale of the system
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3;
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II;
[Isernia et al. (2023)](/sources/isernia-2023.md), §II A). The stellarator
generalization is on
[reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md).

## Two derivations

* **Ordering-based.** The classical route (Strauss; Kadomtsev–Pogutse)
  expands full MHD in a small parameter $\lambda_{\rm o}$, the inverse
  aspect ratio or $k_\parallel/k_\perp$ (flute ordering). The linear
  model A of GMEC is "consistent with" Strauss' reduced MHD apart from an
  added resistive term ([Jiang et al. (2024)](/sources/jiang-2024.md),
  §II A); BOUT++ models carry the flute ordering in their equations and,
  separately, in their field solver
  ([Seto et al. (2023)](/sources/seto-2023.md), §1).
* **Ansatz-based (Galerkin).** JOREK inserts an ansatz for $\mathbf A$ and
  $\mathbf v$ into full MHD and projects the momentum equation onto the
  matching test functions. "Once the ansatz and projection functions are
  defined, there are no approximations on geometry", so the model "is not an
  aspect ratio expansion of the full MHD model"
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.1, p. 16). The
  ansatz-based model captures 3D VDE dynamics and wall currents "even in the
  spherical tokamak limit", in contrast to ordering-based models
  ([Artola et al. (2021)](/sources/artola-2021.md), Abstract, §5).

## The JOREK ansatz-based model

**Ansatz.** With $F_0$ a constant,

$$\mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi\quad(\mathbf A=\psi\nabla\phi),\qquad
\mathbf v=-R^2\nabla u\times\nabla\phi+v_\parallel\mathbf b,\qquad u=\Phi/F_0,$$

so that the first velocity term is the $\mathbf E\times\mathbf B$ drift in
the field $F_0\nabla\phi$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 25–27;
[Artola et al. (2021)](/sources/artola-2021.md), Eqs. 5–6;
[Hu et al. (2021b)](/sources/hu-2021-b.md), Eqs. 1–3). Extended variants
add the ion diamagnetic velocity
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 26;
[Korving et al. (2023)](/sources/korving-2023.md), Eq. 7). JOREK evolves the
coefficient of $\mathbf B$ in the parallel flow, $\hat v_\parallel=v_\parallel/B$
(registry §10), not $v_\parallel$ itself
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Table 1). The toroidal
field is fixed in time. Poloidal currents still exist and evolve, but their
contribution to $B_\phi$ is dropped
([Artola et al. (2021)](/sources/artola-2021.md), §2;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 43).

**Variables.** Five evolved fields, $\psi$, $u$, $\rho$, $T$ (total
$T_e+T_i$ in the single-temperature model) and the parallel velocity, plus
two fields defined by projection,

$$j=\Delta^*\psi=-\mu_0RJ_\phi,\qquad \varpi=\frac1R\partial_R\big(R\,\partial_Ru\big)+\partial_Z^2u,$$

kept as finite-element unknowns so that the weak form needs no second
derivatives ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 38–39,
Table 1; [Isernia et al. (2023)](/sources/isernia-2023.md), Eq. 2;
[Hu et al. (2021b)](/sources/hu-2021-b.md), Eqs. 9, 13). A simplified
variant drops the parallel velocity and with it the slow magnetosonic wave
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.4). The simplest
variant in the sources keeps only $\psi$ and $u$: pressureless, no parallel
flow, flat constant density, constant $\eta$ and viscosity, the source term
$\eta(j-j_0)$ that holds the initial current, and fixed-boundary conditions
($\psi$ fixed, $u=\varpi=j=0$) ([Nardon et al. (2023b)](/sources/nardon-2023-b.md),
§II, Eqs. 1–2). In that model the magnetic helicity
$\int\mathbf A\cdot\mathbf B\,dV$, with $\mathbf A=\psi\nabla\phi-F_0(Z/R)\nabla R$,
changes only through the resistive term,
$\frac{d}{dt}\int\mathbf A\cdot\mathbf B\,dV=2F_0\int\eta(j-j_0)R^{-1}\,d\phi\,dS$
in JOREK units, the classical result that helicity is dissipated only at the
resistive rate (App. A, Eq. A4; the printed intermediate step A3 lacks a
factor $R$, compiler's check recorded on the Source page). See
[double tearing mode](/definitions/double-tearing-mode.md).

**Equations.** With the bracket
$[f,g]=\mathbf e_\phi\cdot(\nabla f\times\nabla g)$ and
$\nabla_{\rm pol}=\mathbf e_R\partial_R+\mathbf e_Z\partial_Z$, the flux and
vorticity equations in SI are

$$\begin{aligned}
\partial_t\psi&=\frac{\eta}{\mu_0}\,(j-j_x)-R\,[u,\psi]-F_0\,\partial_\phi u,\\
R\nabla\cdot\big[R^2\partial_t(\rho\nabla_{\rm pol}u)\big]&=\tfrac12\big[R^2|\nabla_{\rm pol}u|^2,R^2\rho\big]+\big[R^4\rho\varpi,u\big]-R\nabla\cdot\big[R^2\nabla_{\rm pol}u\,\nabla\cdot(\rho\mathbf v)\big]\\
&\quad+\frac1{\mu_0}\Big([\psi,j]-\frac{F_0}{R}\partial_\phi j\Big)+[p,R^2]+R\,\nu_\perp\nabla^2_{\rm pol}\varpi,
\end{aligned}$$

where $j_x=-\mu_0RJ_{x,\phi}$ is the source current
([Hu et al. (2021b)](/sources/hu-2021-b.md), Eqs. 8, 12, written there
with $\mu_0=1$; [Bandaru et al. (2024)](/sources/bandaru-2024.md),
Eqs. 2.3–2.6, which add runaway-electron and hyper-resistive terms;
[Hu et al. (2021)](/sources/hu-2021.md), Eqs. 3–9, and
[Hu et al. (2023)](/sources/hu-2023.md), Eqs. 1–9, print the same flux and
vorticity equations with $j_x=0$ and $\eta(T_e)$;
[Nardon et al. (2023b)](/sources/nardon-2023-b.md), Eqs. 1–2, the
pressureless form divided by $R$). The viscous term is printed in two forms;
see *Contradictions*. The term $[p,R^2]$ is the $\nabla B$ drive that
polarizes a high-pressure pellet plasmoid and makes it drift outward in
major radius ([Hu et al. (2024)](/sources/hu-2024.md), §3, Eq. 5; see
[plasmoid drift](/definitions/plasmoid-drift.md)). The
vorticity equation is the toroidal component of the curl of $R^2$ times the
momentum equation
([Hu et al. (2021b)](/sources/hu-2021-b.md), §2.4). The parallel momentum
equation is the projection on $\mathbf B$, and density and pressure obey
the full-MHD equations with the restricted $\mathbf v$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 30–33). The flux
equation as written here follows from $\mathbf E=-\partial_t\mathbf A-\nabla\Phi$,
the ansatz and Ohm's law; the resistive term is diffusive because
$\Delta^*$ is negative semi-definite (compiler's derivation; see
*Contradictions*).

**Boundary conditions.** Dirichlet conditions on flux-aligned boundaries
and Bohm sheath conditions where field lines cross the wall; in
free-boundary runs the Dirichlet conditions on $\psi$ and $j$ are replaced
by a natural condition coupling to the wall code
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2; see
[resistive-wall coupling](/methods/resistive-wall-coupling.md)). The
electromagnetic boundary datum the reduced model needs is only
$R^{-1}\partial\psi/\partial n$, while full MHD needs both tangential field
components ([Isernia et al. (2023)](/sources/isernia-2023.md), Eq. 3,
§II A). In the NSTX VDE case JOREK imposes $\mathbf v\cdot\mathbf n=0$,
$v_\parallel=0$ and zero toroidal vorticity on the wall
([Artola et al. (2021)](/sources/artola-2021.md), §2); the consequence for
the toroidal asymmetry of $I_p$ is on
[reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md).

**Two-temperature impurity variant.** For shattered-pellet studies JOREK
evolves a total and an impurity mass density with their own sources, an ion
and an electron pressure coupled by collisional exchange, Ohmic heating in the
electron equation, frictional heating of newly ablated particles, and the
ionization energy as potential energy; all species and charge states share one
velocity, and $\nu_\perp\propto T_e^{-3/2}$ keeps the magnetic Prandtl number
roughly fixed ([Hu et al. (2021)](/sources/hu-2021.md), Eqs. 5–12;
[Hu et al. (2023)](/sources/hu-2023.md), Eqs. 6–11, with the
collisional-radiative impurity model; [Hu et al. (2024)](/sources/hu-2024.md),
§2.1, unchanged). The radiation term is printed inconsistently between the
single- and two-temperature equations of Hu et al. (2021) (recorded on its
Source page).

**Diamagnetic and bootstrap extension for edge regimes.** The ion
diamagnetic velocity is added to the $\mathbf E\times\mathbf B$ and parallel
flows, the bootstrap current enters through a relaxation term
$\eta(j-j_{\rm src})$ with a Sauter source that also carries the Ohmic part,
and $v_\parallel$ is set only by Mach-1 conditions at the divertor targets,
with no momentum source ([Cathey et al. (2024)](/sources/cathey-2024.md),
§3.1, fn. 9; the printed diamagnetic velocity carries a spurious mass factor,
recorded on the Source page). See [bootstrap current](/definitions/bootstrap-current.md).
[Liang et al. (2025)](/sources/liang-2025.md) (§III, Eqs. 1–9) print the
same model in full for HL-3 QH-mode runs: the velocity ansatz adds
$-(\rho\,\Omega_iR_0)^{-1}R\nabla p_i\times\mathbf e_\phi$ (JOREK units) to the
$\mathbf E\times\mathbf B$ and parallel flows (the diamagnetic parameter
$1/(\Omega_iR_0)$ with $\Omega_i$ evaluated on the axis field, without the
mass factor), the flux equation carries the electron-pressure terms
$\propto[p_e,\psi]$ and $\propto\partial_\phi p_e$ with the same parameter,
the source current holds a constant Ohmic part plus an evolving Sauter
bootstrap part, $T$ is the common $T_e=T_i$ (not their sum) with $p=2\rho T$
in JOREK units, Taylor–Galerkin stabilization acts on the $u$, $\rho$, $T$ and $\hat v_\parallel$
equations, and full and reduced MHD are said to agree "excellently" for
pedestal and ELM studies (citing Pamela et al. 2020). The resistive term of
that flux equation is discussed under *Contradictions*.

**Extensions used in the sources.** Two temperatures, coronal or
collisional-radiative impurities, fluid or kinetic neutrals, a
runaway-electron fluid and energetic-particle coupling are all added to
this base ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §§2.5–2.11;
[Hu et al. (2021b)](/sources/hu-2021-b.md), Eqs. 10–17;
[Korving et al. (2023)](/sources/korving-2023.md), §II B, a visco-resistive
one-temperature model with seven variables plus neutrals;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), §II). The two-temperature
impurity variant with collisional-radiative impurity markers is also used for
ASDEX Upgrade SPI, with a constant viscosity ([Tang et al. (2025)](/sources/tang-2025.md),
§2.1, Eqs. 1–7); a single-temperature variant with coronal neon and the
runaway-electron fluid serves for EU-DEMO VDEs
([Vannini et al. (2025)](/sources/vannini-2025.md)). At the
other extreme, the model with all magnetic fields and currents set to zero,
"similar to the Euler system", evolves only $\rho$, $u$ and $T$ with the
ansatz $\mathbf v=R^2\nabla\phi\times\nabla u$; JOREK runs of it on a slab at
$R=10$ m generate the training data of neural-operator surrogates
([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.1, Eqs. 1–3; the
reduced equations are not printed there). In its isothermal form every blob
moves at the same speed whatever its density, because buoyancy and inertia
both scale with $\rho$ (§2.1).

## Ordering-based linear models

GMEC_I solves three linearized reduced models without equilibrium flow
([Jiang et al. (2024)](/sources/jiang-2024.md), §II, Eqs. 1–12). With
equilibrium quantities unmarked and perturbations prefixed by $\delta$,
model A is

$$\begin{aligned}
\partial_t\delta\varpi&=\nabla\times(\delta A_\parallel\mathbf b)\cdot\nabla\Big(\frac{\mu_0 j_\parallel}{B}\Big)+\mathbf B\cdot\nabla\Big(\frac{\mu_0\,\delta j_\parallel}{B}\Big),\qquad
\partial_t\delta A_\parallel=-\mathbf b\cdot\nabla\delta\Phi-\eta\,\delta j_\parallel,\\
\delta\varpi&=\nabla\cdot\Big(\frac{1}{v_A^2}\nabla_\perp\delta\Phi\Big),\qquad
\delta j_\parallel=-\frac{1}{\mu_0B}\nabla\cdot\Big(B^2\nabla_\perp\frac{\delta A_\parallel}{B}\Big),
\end{aligned}$$

with $A_\parallel=\mathbf A\cdot\mathbf b$. Model B adds the curvature
drive $\frac{2\mu_0}{B}\mathbf b\times(\mathbf b\cdot\nabla\mathbf b)\cdot\nabla\delta p$
to the vorticity equation and a pressure equation in the slow-sound
approximation,
$\partial_t\delta p=-\frac1B\mathbf b\times\nabla\delta\Phi\cdot\nabla p-\frac{2\Gamma p}{B}\mathbf b\times(\mathbf b\cdot\nabla\mathbf b)\cdot\nabla\delta\Phi$.
Model C adds the ion diamagnetic term (gyroviscous cancellation) and the
electron-pressure terms of Ohm's law with isothermal electrons
([Jiang et al. (2024)](/sources/jiang-2024.md), Eqs. 6–12). GMEC's hybrid
version couples the energetic-particle pressure into the same vorticity
equation ([Liu et al. (2024)](/sources/liu-2024.md), Eq. 1; see
[hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)).
BOUT++ uses a linear three-field peeling–ballooning model of the same
structure and a nonlinear four-field two-fluid model with ion
diamagnetism, gyroviscous cancellation and hyper-resistivity
([Seto et al. (2023)](/sources/seto-2023.md), Eqs. 21–35).

## Properties

* **Equilibrium.** The reduced model preserves a Grad–Shafranov
  equilibrium even with constant $F_0$ in place of $F(\psi)$: the terms in
  $F$ lie in the kernel of the momentum projectors, and the Shafranov shift
  is retained through the initial $\psi$
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.1, p. 15; see
  [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)).
* **Energy.** The single-fluid model is energy-conserving at the level of
  the equations, a consequence of the energy conservation of full MHD and
  of the Galerkin ansatz. Gyroviscous cancellation breaks this at first
  order in the diamagnetic parameter (ion mass over $eF_0\sqrt{\mu_0\rho}$,
  times magnetic pressure over $\rho v_A$), and a finite time step and the
  toroidal Fourier truncation add further errors
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3; Fig. 17).
* **Momentum.** Linear momentum is not conserved locally: there are only
  two scalar momentum equations for three Cartesian components. The
  vertical component is conserved globally (test function $\ln R$), and
  the horizontal components are conserved globally if the $n=1$ harmonic is
  excluded ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3, p. 19).
* **Current continuity.** The model satisfies $\nabla\cdot\mathbf J=0$:
  the vorticity equation is the weak form of $\nabla\cdot\mathbf J=0$, and
  the poloidal current can be reconstructed a posteriori from the momentum
  equation ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 43).
* **Waves.** The velocity ansatz keeps the $\mathbf E\times\mathbf B$
  (Alfvén) and field-aligned (slow) parts of a general flow and drops the
  perpendicular compression that carries the fast wave
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), p. 19;
  [Nikulsin et al. (2022)](/sources/nikulsin-2022.md), Eq. 2). Shear Alfvén
  propagation is retained quantitatively: in a JET plasmoid-drift run the
  wave packets travel along the field at about $4.7\times10^6$ m/s against an
  Alfvén speed of about $4.5\times10^6$ m/s
  ([Kong et al. (2025)](/sources/kong-2025.md), §4.1, Fig. 13).
* **Convergence to full MHD.** For a simplified reduced model, solutions
  of full MHD converge to those of the reduced model (Ref. 54 of
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3).

## Range of validity

**Finite-β internal kink.** The JOREK reduced model sets
$\mathbf e_\phi\cdot\delta\mathbf B=0$, so $\delta B_\parallel\approx0$,
whereas full MHD gives $B\,\delta B_\parallel\approx-\delta p$. The
fast-wave term of the energy functional,
$\tfrac12\int_V|\delta B_\parallel+\delta p/B|^2\,dV$, then contributes a
spurious stabilizing $\delta p$ part for pressure-driven modes. The $1/1$
internal kink is accurate near zero β but "the accuracy of reduced MHD
quickly deteriorates" as β rises; it deviates at low η even at
$\beta_N=0.4\%$ ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3,
p. 20; §4.4, Figs. 18–19). Edge ballooning modes are largely unaffected
because the correction enters a Mercier-type criterion through a factor
$(1-q^2)$ that is small where $q\gg1$ (same location). Reduced models that
impose $B\,\delta B_\parallel=-\delta p$ (Kruger et al.) capture most
pressure-driven modes. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
§VIII, state for the stellarator family that it "cannot accurately reproduce
kink modes at higher β", citing Hoelzl et al. (2021). The two sources agree;
see [resistive internal kink](/definitions/resistive-internal-kink.md).
Two chunk-2 JOREK papers state the same limitation, citing earlier JOREK work
([Hu et al. (2023)](/sources/hu-2023.md), §2.2;
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.3).

**Parallel flow.** Dropping $v_\parallel$ "decreases the accuracy … and
narrows the range of scenarios" ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
§II, citing earlier work); the 26.2% tearing-rate gap of JOREK3D against
CASTOR3D at the highest η is attributed to it
([JOREK3D](/software/jorek3d.md)); Ramasamy et al. (2024, §3.1) attribute it
instead to CASTOR3D resolution (open on that page). Adding $v_\parallel$ to
the stellarator model separates the two compression effects that Graves et
al. 2019 held responsible for artificial stabilization of compressible modes:
without $v_\parallel$ the compressible interchange growth rates are too low and
the error grows as $n$ falls, while with $v_\parallel$ all modes agree with full
MHD within 10%, so the eliminated fast-wave (field-compression) terms do not
matter in that low-shear case ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md),
§3.2, Figs. 5, 7; see [reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)
and [interchange modes](/definitions/interchange-mode.md)).

**Benchmarks against full MHD.** Reduced and full JOREK agree within 5% on
peeling–ballooning growth rates (JET-like X-point, with and without
diamagnetic effects); reduced JOREK agrees with BOUT++ within 4% on linear
ballooning growth rates and with the cylindrical full-MHD code SpeCyl
within about 5% on the nonlinear $2/1$ tearing mode at $S=10^6$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4–4.5, Figs. 20–22).
In the [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md) reduced
JOREK matches the full-MHD codes except for the $I_p$ asymmetry
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6); these VDE
benchmarks are the stated basis for using reduced MHD to compute ITER wall
forces ([Artola et al. (2022)](/sources/artola-2022.md), §2). JOREK's
energetic-particle work on the AUG-NLED case uses reduced MHD "as results
agree with full MHD while computational costs are lower", without showing
the comparison ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md),
§IV.B).

**Flute ordering in field solvers.** Solving the vorticity–potential
relation with $\partial_\parallel=0$ is wrong for $n=0$ and degrades at low
$n$: the linear ideal-ballooning growth rate from the flute-ordered solver
exceeds the 2D solve by about 1% at $n=20$ and about 36% at $n=5$
([Seto et al. (2023)](/sources/seto-2023.md), §4, Fig. 3; see
[hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md)).

## Contradictions

* **Sign of the resistive term in the JOREK flux equation.** *Open;
  recommended for human closure as a printed slip.*
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 28 (p. 15), prints
  the flux equation with $-\frac{\eta}{R^2}(j-j_x)$ and
  $+\frac{F_0}{R^2}\partial_\phi u$ on the right-hand side, with
  $j=\Delta^*\psi$ (Table 1). [Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
  Eq. 3d, likewise prints $-\eta(j-j_{\rm eq})$ with $j=\Delta^*\psi$
  (Eq. 3e). [Hu et al. (2021b)](/sources/hu-2021-b.md), Eq. 8, and
  [Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.3, print
  $+\eta\Delta^*\psi$ and $-F_0\partial_\phi u$. With $j=\Delta^*\psi$ and
  $\Delta^*$ negative semi-definite, only the second sign makes resistivity
  diffuse the flux; the derivation from $\mathbf E=-\partial_t\mathbf A-\nabla\Phi$
  and the ansatz gives the second form for both terms (compiler's check).
  The sign of the bracket term depends on orientation conventions (JOREK
  states COCOS 8; the other sources do not state theirs). A published
  correction, or the code's own documentation, would settle the
  printed form. Chunk 2 adds four sources on the diffusive side:
  [Nardon et al. (2023b)](/sources/nardon-2023-b.md), Eq. 1, prints
  $+\eta(j-j_0)$, $-F_0\partial_\phi u$ and $+R[\psi,u]$ with $j=\Delta^*\psi$;
  [Hu et al. (2021)](/sources/hu-2021.md), Eq. 3, and
  [Hu et al. (2023)](/sources/hu-2023.md), Eq. 5, print
  $+\eta(T_e)\Delta^*\psi-F_0\partial_\phi u$; and the stellarator form of
  [Ramasamy et al. (2024)](/sources/ramasamy-2024.md), Eq. 7, prints
  $+\eta(j-j_{\rm source})$ with $j=\Delta^*\psi_\chi$ together with a
  hyper-resistive term $-\nabla\cdot(\eta_h\nabla^\perp j)$, both of the
  diffusive sign and both opposite to Nikulsin et al. (2022), Eq. 3d. The
  printed record now stands at two sources against six. Ramasamy et al. share
  authors with Nikulsin et al. but do not comment on the sign change, so this
  is evidence for the slip reading, not an explicit supersession.
  Chunk 3 adds three printed forms.
  [Tang et al. (2025)](/sources/tang-2025.md), Eq. 1, prints
  $+\eta\Delta^*\psi-R\{u,\psi\}-F_0\partial_\phi u$, the diffusive form.
  [Vannini et al. (2025)](/sources/vannini-2025.md), App. A, Eq. 4, prints
  $R^{-1}\partial_t\psi=R^{-1}\eta(j-\dots)+[\psi,u]-R^{-1}F_0\partial_\phi u$
  with $j=\Delta^*\psi$ (Eq. 6), also the diffusive form.
  [Liang et al. (2025)](/sources/liang-2025.md), Eq. 7, prints
  $-R\eta(j-j_S)-R[u,\psi]-F_0\partial_\phi u$ with $j=\Delta^*\psi$ (Eq. 8):
  the resistive term has the non-diffusive sign of Hoelzl et al. (2021),
  with a factor $R$ in place of $1/R^2$, while the $F_0\partial_\phi u$ term
  has the sign of the diffusive side, so this form matches neither printed
  family as a whole. The record now stands at eight sources printing the
  diffusive resistive sign against three printing the other, one of them
  internally mixed. Liang et al. share authors with Hoelzl et al. (2021) and
  with the Hu papers and do not comment.
* **Viscous term of the vorticity equation.** *Open.*
  [Hu et al. (2021b)](/sources/hu-2021-b.md), Eq. 12, and
  [Hu et al. (2021)](/sources/hu-2021.md), Eq. 7, print
  $R\,\nu_\perp\nabla^2_{\rm pol}\varpi$ (as on this page);
  [Hu et al. (2023)](/sources/hu-2023.md), Eq. 8, and
  [Hu et al. (2024)](/sources/hu-2024.md), Eq. 5, print
  $R^3\nu_\perp(T_e)\nabla^2_{\rm pol}\varpi$ in an otherwise identical
  equation, and Hu et al. (2024) state that their equations are those of
  Hu et al. (2023) "without modifications". The pressureless form of
  [Nardon et al. (2023b)](/sources/nardon-2023-b.md), Eq. 2, divided by $R$
  relative to this page, carries $\nu\Delta\varpi$, which corresponds to the
  $R$ form (compiler's check; the operator $\Delta$ is not defined there).
  [Tang et al. (2025)](/sources/tang-2025.md), Eq. 2, which shares authors
  with Hu et al. (2023, 2024), prints $R\,\nu\nabla^2_{\rm pol}\varpi$ with a
  constant $\nu$, the $R$ form, and
  [Vannini et al. (2025)](/sources/vannini-2025.md), App. A, Eq. 5, prints
  $R\nabla\cdot(\nu\nabla_{\rm pol}\varpi)$, also with a single $R$;
  Liang et al. (2025) print the viscous term only in the unprojected
  momentum equation and add nothing. The printed record is now five forms
  with $R$ (counting Nardon et al.) against two with $R^3$. Either the JOREK implementation changed between papers or one
  form is a misprint; none of the sources comments.

# Citations

* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — ansatz-based JOREK reduced MHD, its properties and its finite-β limitation.
* [Artola et al. (2021)](/sources/artola-2021.md) — ansatz, boundary conditions, validity at low aspect ratio.
* [Isernia et al. (2023)](/sources/isernia-2023.md) — reduced ansatz and its electromagnetic boundary datum.
* [Jiang et al. (2024)](/sources/jiang-2024.md) — linear ordering-based models A, B, C.
* [Seto et al. (2023)](/sources/seto-2023.md) — BOUT++ reduced models and the flute-ordering error.
* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — tokamak limit, wave content, kink limitation at higher β.
* [Hu et al. (2021b)](/sources/hu-2021-b.md) — JOREK reduced equations in strong form.
* [Korving et al. (2023)](/sources/korving-2023.md) — visco-resistive one-temperature variant with neutrals.
* [Bandaru et al. (2024)](/sources/bandaru-2024.md) — JOREK reduced equations with runaway electrons.
* [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — use of reduced MHD for energetic-particle modes.
* [Liu et al. (2024)](/sources/liu-2024.md) — GMEC reduced MHD coupled to energetic particles.
* [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — pressureless two-field variant, helicity dissipation, resistive sign.
* [Hu et al. (2021)](/sources/hu-2021.md) — two-temperature impurity variant, resistive sign, viscous term.
* [Hu et al. (2023)](/sources/hu-2023.md) — two-temperature collisional-radiative variant, kink limitation, viscous term.
* [Hu et al. (2024)](/sources/hu-2024.md) — vorticity equation and the $[p,R^2]$ plasmoid drive.
* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — resistive sign, $v_\parallel$ and compressional error, kink limitation.
* [Cathey et al. (2024)](/sources/cathey-2024.md) — diamagnetic and bootstrap extension.
* [Kong et al. (2025)](/sources/kong-2025.md) — shear Alfvén propagation in reduced MHD.
* [Artola et al. (2022)](/sources/artola-2022.md) — validity basis for wall forces.
* [Tang et al. (2025)](/sources/tang-2025.md) — two-temperature SPI variant, resistive sign, viscous term.
* [Liang et al. (2025)](/sources/liang-2025.md) — diamagnetic and bootstrap variant printed in full, resistive sign.
* [Vannini et al. (2025)](/sources/vannini-2025.md) — variant with coronal impurities and runaway electrons, resistive sign, viscous term.
* [Gopakumar et al. (2024)](/sources/gopakumar-2024.md) — field-free limit used for surrogate training data.
