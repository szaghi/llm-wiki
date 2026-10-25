---
type: Benchmark
title: "Homogeneous isotropic turbulence (decaying and forced)"
description: "Turbulence in a triply periodic box, decaying from a prescribed spectrum or sustained by forcing, used as a priori database and a posteriori test of subgrid-scale closures: here Re_λ from 70 to 324, LES of 24³ to 144³ degrees of freedom against filtered DNS spectra."
status: established
aliases: [HIT, DHIT, forced HIT, decaying isotropic turbulence, forced isotropic turbulence, periodic box turbulence]
tags: [benchmark, les, sgs-model, data-driven, dns]
timestamp: 2026-10-25T13:45:00Z
---

# Homogeneous isotropic turbulence (decaying and forced)

Homogeneous isotropic turbulence (HIT) is computed in a periodic cube,
with no walls and no mean flow. In the **decaying**
variant a random field with a prescribed spectrum evolves freely and its
kinetic energy $K=\int E(k)\,dk$ and dissipation $\varepsilon$ decrease in
time. In the **forced** variant a body force $f_i$ injects energy at a rate
that keeps the flow statistically stationary. Because the flow is
homogeneous, the energy spectrum $E(k)$ and the time histories of $K$ and
$\varepsilon$ characterize the solution completely at the level the sources
compare. An LES is judged against a DNS filtered to the LES cutoff. The case
isolates the [subgrid-scale closure](/definitions/large-eddy-simulation.md)
and the [numerical dissipation](/properties/numerical-dissipation.md) of the
discretization from wall and inflow effects. (On this spectral page $k$ is
the wavenumber magnitude and $K$ the kinetic energy, as fixed in the
notation registry.)

## Set-ups in the sources

| Source | Variant | $Re_\lambda$ | Reference DNS | LES resolution | Initial field and forcing |
|---|---|---|---|---|---|
| [Flad & Gassner (2017)](/sources/flad-2017.md), §1, §3–5 | decaying | from about 162 to 97 over the run | pseudo-spectral, $512^3$, 2/3-rule de-aliasing | DG, $N=7$: $18^3$ elements ($144^3$ DOF) and $6^3$ elements ($48^3$ DOF) | filtered DNS field; maximum local Mach about 0.1 |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.A | decaying | 70 | $128^3$ | $32^3$ | Passot–Pouquet spectrum, $u_{\mathrm{rms}}=1$ |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.B–C | forced | 315; and $Re_\lambda\to\infty$ | filtered $1024^3$ DNS of Cardesa et al. | $128^3$ | linear momentum forcing at constant kinetic energy |
| [Beck & Kurz (2023)](/sources/beck-2023.md), §IV A | forced | about 180 | DG $N=7$, $64^3$ elements, 512 points per direction, run to $t=10$ (about 14 large-eddy turnovers) | DG, 24 or 36 DOF per direction, $N=3,5,8$ | Rogallo initialization, linear forcing applied at the nodes |
| [Vela-Martín (2022)](/sources/velamartin-2022.md), §5.1, Table 1 | forced | 140, 240, 324 | $256^3$, $512^3$, $1024^3$, with $k_{\max}\eta=1.5,1.5,2.0$; 290 independent fields | a priori only: filter scales $\ell/L$ from 0.65 to 0.08 | linear forcing |
| [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), §5, App. G.2 | forced (3D) | not stated ($Re=2000$) | $1024^3$, single precision | $32^3$, $64^3$ | random field with spectrum peaked at wavenumber 20; Kolmogorov force $\sin(8\pi x_2)$ on $[0,1]^3$ |

The beck-2023 DNS used 16,384 cores of the HAWK system for almost two hours
(about 30,000 CPU hours). [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
run their main experiments in two dimensions: Kolmogorov-forced turbulence
at $Re=6000$ (DNS $4096^2$, LES $\bar n=32$ to 256 per direction) and a 2D
decaying case (App. G.1). These are periodic-box turbulence but neither
three-dimensional nor isotropic in the 3D sense, and the paper does not
state the reference velocity and length behind $Re$.

## What the case tests

**Dissipation by implicit and explicit closures.**
[Flad & Gassner (2017)](/sources/flad-2017.md) use decaying HIT to show that
no-model DG LES with Riemann-solver dissipation and polynomial de-aliasing
matches the DNS at $144^3$ DOF, where 43.2% of the dissipation is resolved
at their 3-points-per-wavelength cutoff $k_c=48$, but fails at $48^3$ DOF,
where 0.9% is resolved at $k_c=16$ (energy pile-up at mid-range wavenumbers,
then a sharp drop). From these two resolutions they infer that roughly 40%
of the dissipation must be resolved for this
[implicit LES](/definitions/implicit-les.md) practice to work. On the
kinetic-energy-preserving split form they show that a
[Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.12$ (in the
squared form of their Eq. A.1) beats no-model DG LES at $48^3$ DOF (§4,
Fig. 7). [Beck & Kurz (2023)](/sources/beck-2023.md) find no single best
baseline across polynomial degrees: no-model LES is best at $N=3$,
Smagorinsky with $C_s=0.17$ over-damps high wavenumbers at $N=5$, and the
[dynamic procedure](/methods/dynamic-procedure.md) is close to DNS at 36 DOF
but deviates at 24 DOF; their
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
reach or exceed the best baseline in all cases except no-model LES at $N=3$
(§V, Figs. 8–14).

**Dissipation of a non-Boussinesq model.**
[Agrawal et al. (2022)](/sources/agrawal-2022.md) use decaying HIT to show
that the [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
dissipates as well as the dynamic Smagorinsky model: both follow filtered DNS
in kinetic energy and dissipation after a transient of up to one eddy
turnover, with decay exponents $K\sim t^{-1.35}$ for both against
$t^{-1.37}$ for the box-filtered DNS (Figs. 3–4). In forced HIT at
$Re_\lambda=315$ both models recover the $k^{-5/3}$ range of the filtered
DNS spectrum (Fig. 5).

**Equipartition without dissipation.** Three sources agree that a
discretization without subgrid dissipation drives the resolved spectrum
towards energy equipartition, $E(k)\sim k^2$, near the cutoff:
[Agrawal et al. (2022)](/sources/agrawal-2022.md) for a no-model LES as
$Re_\lambda\to\infty$ (§VII.C, Fig. 6);
[Flad & Gassner (2017)](/sources/flad-2017.md) for the dissipation-free split-form
DG scheme at $48^3$ DOF, which stays stable (§3, Fig. 4); and, on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) for
truncated Euler and no-model runs (§6.2). This is the statement of the
benchmark that a stable, energy-conserving scheme must be supplemented by
dissipation, explicit or numerical.

**A priori structure of the subgrid flux.**
[Vela-Martín (2022)](/sources/velamartin-2022.md) uses the forced database
to show that the mean local SGS flux $\langle\Pi\rangle$ equals $\varepsilon$
at all filter scales tested (inertial-range filtering) and that the
backscatter it contains can be moved into a conservative spatial flux by a
gauge transformation of the SGS stress (see
[energy backscatter](/definitions/energy-backscatter.md)). The flux the
paper writes $T$ equals the registry's $\Pi$, because the paper's SGS
stress has the opposite sign.

**Learned closures, a priori against a posteriori.**
As recalled by [Duraisamy (2021)](/sources/duraisamy-2021.md), §IV.B, Fig. 2,
from Sirignano, MacArt & Freund, an a priori-trained SGS closure
over-predicts the resolved kinetic energy of decaying HIT, while a
model-consistent (differentiable-physics) closure follows the filtered DNS.
[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), App. G.2, find
that in 3D forced turbulence ($\bar n=32,64$) a CNN closure in their
divergence-consistent formulation beats no model and Smagorinsky
($C_s=0.17$) in a priori and a posteriori error, while Smagorinsky is too
dissipative at high wavenumbers. See
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [model-consistent training](/methods/model-consistent-training.md).

**Closure constants.** As recalled by
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md), decay rates of grid
turbulence (Comte-Bellot & Corrsin 1966) constrain the coefficients of RANS
closures (the coefficient layer of their taxonomy of
[model-form uncertainty](/definitions/model-form-uncertainty.md)). As recalled by
[Agrawal et al. (2022)](/sources/agrawal-2022.md), §II.A, Lilly derived
$C_s\approx0.17$ for isotropic turbulence with an inertial-range cutoff;
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), §6.5,
quote Lilly's analytical value $C_s=\pi^{-1}(3C_K/2)^{-3/4}=0.18$ with
Kolmogorov constant $C_K=1.4$. The Chollet–Lesieur spectral eddy viscosity,
whose plateau 0.267 holds for an infinite Kolmogorov spectrum, is the
spectral reference used with HIT in both
[Flad & Gassner (2017)](/sources/flad-2017.md), App. C, and
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), Eq. (55)
(see [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)).

## Qualifications

- Forcing differs between sources (linear forcing at the nodes; linear
  momentum forcing; Kolmogorov forcing at a single wavenumber). [Beck & Kurz (2023)](/sources/beck-2023.md)
  note that their nodal forcing injects energy at all wavenumbers present
  and causes a slight departure of the spectrum from $k^{-5/3}$.
- [Flad & Gassner (2017)](/sources/flad-2017.md), §1, print the large-eddy
  turnover time as "$T=\bar v(t_{\mathrm{start}})/L_{\mathrm{int}}\approx1.3$",
  a velocity over a length; a time is length over velocity.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) prints $Re_\lambda=320$
  in the Fig. 6 and Fig. 7 captions and in §6.4 for the $1024^3$ case, for
  which Table 1 and §5.1 give 324.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) name the 3D
  case of App. G.2 both "forced" (title) and "decaying" (first sentence)
  while applying a body force, and print its amplitude as 5 while Eq. (31)
  of the 2D case has amplitude 1 and App. G.2 calls it "the same body force".

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, §3–5, Figs. 1–10, App. C.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.A, §VII.A–C, Figs. 3–6.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §IV A–B, §V, Figs. 6–14, App. A.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §5.1–5.3, Table 1, Figs. 1–7.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §5, App. B.2, App. G.1–G.2.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.B, Fig. 2 (recalled result).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — test-problem list (recalled grid-turbulence calibration).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.2, §6.4–6.5, Eq. (55).
