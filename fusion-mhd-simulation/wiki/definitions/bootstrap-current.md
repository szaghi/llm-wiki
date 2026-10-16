---
type: Definition
title: "Bootstrap current and its MHD implementation"
description: "The neoclassical parallel current driven by density and temperature gradients in toroidal geometry, and its inclusion in MHD codes as a non-inductive current J_x in Ohm's law toward which the plasma current relaxes resistively; M3D-C1 uses Sauter or Redl fits (mapped to quasi-symmetric stellarators), JOREK a Sauter-evolved toroidal source current, and NIMROD a heuristic neoclassical electron stress that produces the drive without an imposed current."
status: established
aliases: [bootstrap current source, non-inductive current, Sauter bootstrap model, Redl bootstrap model]
tags: [bootstrap-current, extended-mhd, tokamak, stellarator]
timestamp: 2026-10-16T12:00:00Z
---

# Bootstrap current and its MHD implementation

The bootstrap current is "a neoclassical electrical current in the plasma
driven by inhomogeneities in the magnetic field", proportional to the
density and temperature gradients; in tokamaks and quasi-symmetric
stellarators it can carry most of the current
([Saxena et al. (2025)](/sources/saxena-2025.md), §1). Single-fluid MHD
does not produce it, because it comes from trapped-particle kinetics.
MHD codes therefore impose it from an analytic closure.

## Non-inductive current in Ohm's law

The current enters as $\mathbf J_x$ in a modified Ohm's law,

$$\mathbf E=-\mathbf v\times\mathbf B+\eta\,(\mathbf J-\mathbf J_x),$$

with the matching Ohmic heating $\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$
in the pressure equation and the same term in the induction equation
([Saxena et al. (2025)](/sources/saxena-2025.md), Eq. 2.1, App. C, Eqs.
C3–C4; see [visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)).
This is equivalent to an electron force $-\eta n_ee\mathbf J_x$ that removes
$\mathbf J_x$'s share of the electron–ion friction. Collisional drag then
makes $\mathbf J=\nabla\times\mathbf B/\mu_0$ decay toward $\mathbf J_x$ on
the resistive time scale. For an internal force such as this one, an equal
and opposite force acts on the ions, so no net force enters MHD force
balance (§2).

## Closures

$\mathbf J_x$ is taken purely parallel, $\mathbf J_x=J_{x\parallel}\mathbf b$.
For it to be divergence-free, $J_{x\parallel}/B$ must be a surface function,
which gives

$$J_{x\parallel}=\frac{\langle\mathbf J_x\cdot\mathbf B\rangle}{\langle B^2\rangle}\,B,$$

with $\langle\cdot\rangle$ the flux-surface average
([Saxena et al. (2025)](/sources/saxena-2025.md), Eq. 2.2). The surface
average comes from analytic fits to drift-kinetic results (App. A):

* **Sauter et al. (1999):**
  $\langle\mathbf J_x\cdot\mathbf B\rangle=-F\Big(p\,L_{31}\dfrac{\partial\ln p}{\partial\psi}+p_e\,L_{32}\dfrac{\partial\ln T_e}{\partial\psi}+p_i\,\alpha_{\rm S}L_{34}\dfrac{\partial\ln T_i}{\partial\psi}\Big)$,
  fitted to CQL3D and CQLP. It is less accurate at effective electron
  collisionality above 1, which limits it near the edge.
* **Redl et al. (2021):**
  $\langle\mathbf J_x\cdot\mathbf B\rangle=-F\Big[p\,L_{31}\dfrac{\partial\ln n}{\partial\psi}+p_e(L_{31}+L_{32})\dfrac{\partial\ln T_e}{\partial\psi}+p_i(L_{31}+\alpha_{\rm S}L_{34})\dfrac{\partial\ln T_i}{\partial\psi}\Big]$,
  a revised fit to NEO, accurate over a broader range of collisionality.

The coefficients $L_{31}$, $L_{32}$, $L_{34}$ and $\alpha_{\rm S}$
(page-local names) depend on the trapped-particle fraction, the
collisionalities and $Z_{\rm eff}$; the source refers to the original papers
for the fits. Both fits are axisymmetric.

**Quasi-symmetric stellarators.** Using the isomorphism of Landreman,
Buller & Drevlak (2022) (see [quasi-symmetry](/definitions/quasi-symmetry.md)),

$$\langle\mathbf J_x\cdot\mathbf B\rangle=\frac{G+NI}{\iota-N}\Big[L_{31}\Big(p_e\frac{\partial\ln n_e}{\partial\psi_t}+p_i\frac{\partial\ln n_i}{\partial\psi_t}\Big)+p_e(L_{31}+L_{32})\frac{\partial\ln T_e}{\partial\psi_t}+p_i(L_{31}+\alpha_{\rm S}L_{34})\frac{\partial\ln T_i}{\partial\psi_t}\Big],$$

the "Sauter–Redl–Landreman" formula, valid only in quasi-symmetric geometry
([Saxena et al. (2025)](/sources/saxena-2025.md), Eq. 2.3, App. B). $G$
and $I$ are the Boozer covariant components and $N$ the helicity integer.

## Implementation in M3D-C1

M3D-C1 does not assume flux surfaces. Surface averages are therefore taken
on isotherms of $T_e$, which coincide with magnetic surfaces when surfaces
exist and $\kappa_\parallel\gg\kappa_\perp$, and relate to
quadratic-flux-minimizing surfaces when they do not. The isotherms are
labelled by $1-T_e/T_{e,\max}$. The averaged geometric quantities are
computed outside the code with the Fusion-IO library, read in, and
re-extrapolated to the mesh each step from the evolving temperature; the
coefficients $L_{3k}$ and $\alpha_{\rm S}$ are evaluated locally each step
([Saxena et al. (2025)](/sources/saxena-2025.md), §2).

**Verification.** On the circular tokamak case CIRC1 the bootstrap peak
lies at $\psi_N\approx0.89$ (inverse aspect ratio 0.63, collisionality
0.92). The peak values differ by 2.18% (M3D-C1 Sauter versus NEO Sauter),
0.04% (M3D-C1 versus XGCa), 2.12% (M3D-C1 Redl versus XGCa) and 1.01%
(M3D-C1 Redl versus SFINCS) (§3.1, Fig. 1b). For two QA stellarators the
profiles are "in close agreement" with SFINCS and the standalone Redl
formula; the remaining differences are attributed to numerics or to
isotherm–surface misalignment, "although the exact sources remain unclear"
(§3.2, Fig. 4).

**Nonlinear QA runs.** At $\beta=2.5\%$ with resistivity raised $10^4$
times, the bootstrap model sustains the toroidal current against resistive
decay and keeps the edge chaotic region "significantly smaller" at
$t=250\,\tau_A$. Instability growth still increases with resistivity with
and without bootstrap current, which supports the earlier conclusion of
Wright & Ferraro (2024) (§3.3, Figs. 5–7).

**Limits stated by the source.** The fits and the reference kinetic codes
are time-independent, so they cannot represent a neoclassical response on
Alfvénic time scales. Stochastic regions are outside neoclassical theory.
An error estimate away from quasi-symmetry is outlined but not shown
(§2, §4).

## Implementation in JOREK

JOREK carries a toroidal source current $\mathbf J_x=j_{\rm S}\mathbf e_\phi$
in Ohm's law, page-local $j_{\rm S}$. It is either fixed at its initial
value or evolved as the initial value plus the change of the Sauter
bootstrap current since $t=0$; this is available in reduced and full MHD
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 6, §2.12). The
JOREK source is therefore toroidal, while the M3D-C1 one is parallel. In
JOREK QH-mode simulations of ASDEX Upgrade the bootstrap current evolves
self-consistently; the nonlinear drop of $q_{95}$ through current
redistribution, bootstrap current included, reduces growth rates and acts
as a saturation mechanism ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
§2.1). In the reduced-MHD form the source enters as a relaxation term
$\eta(j-j_{\rm src})$, so the current builds up on the resistive time; the
source holds both the Sauter bootstrap and the Ohmic contribution, and the
nonlinear evolution of $q_{95}$ contributes to the saturation of the QH-mode
kink-peeling mode ([Cathey et al. (2024)](/sources/cathey-2024.md), §3.1–3.2).
With stationary profiles the Sauter source is stationary; when the profiles
change nonlinearly it follows them, and the authors associate this extension
with the presence of the radial-electric-field well $\propto\nabla p/n$ in
the EDA H-mode simulations (the referent of their sentence is ambiguous,
recorded on the Source page) ([Cathey et al. (2023)](/sources/cathey-2023.md),
§2.2).
Other MHD codes use a heuristic closure (NIMROD) or kinetic closures
that are "extremely computationally expensive"
([Saxena et al. (2025)](/sources/saxena-2025.md), §1).

## Heuristic neoclassical closure (NIMROD)

The heuristic closure of Gianakon et al. (2002) does not impose a current. It
adds to Ohm's law an electron stress that damps the electron poloidal flow
relative to its equilibrium value,

$$\mathbf E=-\mathbf v\times\mathbf B+\eta\mathbf J-\frac{1}{n_ee}\nabla\cdot\mathsf\Pi_e,\qquad
\nabla\cdot\mathsf\Pi_e=-\nu_{{\rm pol},e}\frac{m_e}{e}\langle B_0^2\rangle\frac{(\mathbf J-\mathbf J_0)\cdot\mathbf e_\Theta}{(\mathbf B_0\cdot\mathbf e_\Theta)^2}\,\mathbf e_\Theta,$$

with $\nu_{{\rm pol},e}$ the electron poloidal damping rate, $\mathbf e_\Theta$
along the equilibrium poloidal field and subscript $0$ the equilibrium
(page-local symbols), plus an ion stress of the same form in the momentum
equation ([Howell et al. (2022)](/sources/howell-2022.md), §II A, Eqs. 5,
8–10). The electron force reproduces the bootstrap current as the result of
collisional viscosity between passing and trapped electrons; the ion force
gives poloidal flow damping and the polarization-current enhancement.
Subtracting $\mathbf J_0$ and $\mathbf v_0$ holds the equilibrium. The closure
is valid to $O(m_e/m_i)$ for strong ion poloidal damping and assumes
$Z_{\rm eff}=1$. The damping rates are uniform and enhanced together with
$\eta$, keeping $\nu_{{\rm pol},e}/(\nu_{ei}+\nu_{{\rm pol},e})=0.55$ against the
experimental 0.43 in the DIII-D case (§III A, Table I). It is the closure
behind NIMROD's [neoclassical tearing mode](/definitions/neoclassical-tearing-mode.md)
simulations; XTOR, XTOR-2F, TM1 and JOREK's neoclassical ion friction use
closures of the same family (§I). The three implementations therefore differ
in kind: an imposed parallel $\mathbf J_x$ (M3D-C1), an imposed toroidal
source current (JOREK) and an electron-force closure (NIMROD).

## Consequence for stability: weak central shear

An off-axis bootstrap current flattens the core $q$ profile, and the weak
central shear it produces is the setting of
[infernal modes](/definitions/infernal-mode.md)
([Sato et al. (2024)](/sources/sato-2024.md), §1).

## Other non-inductive source currents

The same Ohm's-law slot carries driven currents. In M3D-C1 simulations of W7-X
an ECCD profile from ray tracing enters as a fixed toroidal source current
peaked at $r/a\approx0.15$; the bootstrap current is neglected as small in
the crash region ([Zhou et al. (2023)](/sources/zhou-2023.md), §II–III, Fig. 1;
see [sawtooth crash](/definitions/sawtooth-crash.md)). The heating term
printed with it is $\eta J^2$, not $\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$;
this is recorded as an open contradiction on
[visco-resistive MHD model](/methods/visco-resistive-mhd-model.md).

## Printed variants

[Saxena et al. (2025)](/sources/saxena-2025.md) print the tokamak fits
(App. A) with $-F$ and the stellarator form (Eq. 2.3) with
$+(G+NI)/(\iota-N)$. For $N=0$, $G=F$ and $\partial_{\psi_t}=\iota\,\partial_\psi$
(Eq. B1), Eq. 2.3 has the opposite sign of the Redl form it is said to
recover, and its density term splits by species where the Redl form uses
$p\,\partial\ln n$; the two agree only for $n_e\propto n_i$ and with an
unstated orientation convention for the fluxes (compiler's check). The
coefficients in their App. A5 are printed as Coulomb logarithms
$\Lambda$ where $\ln\Lambda$ is meant.

# Citations

* [Saxena et al. (2025)](/sources/saxena-2025.md) — Ohm's-law implementation, Sauter, Redl and quasi-symmetric closures, verification, nonlinear QA runs.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — JOREK bootstrap-evolving source current.
* [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — self-consistent bootstrap current in JOREK QH-mode simulations.
* [Howell et al. (2022)](/sources/howell-2022.md) — NIMROD heuristic neoclassical closure.
* [Cathey et al. (2024)](/sources/cathey-2024.md) — JOREK relaxation form of the Sauter source.
* [Zhou et al. (2023)](/sources/zhou-2023.md) — ECCD as an Ohm's-law source current.
* [Cathey et al. (2023)](/sources/cathey-2023.md) — evolving Sauter source and the E_r well.
* [Sato et al. (2024)](/sources/sato-2024.md) — off-axis bootstrap current and infernal modes.
