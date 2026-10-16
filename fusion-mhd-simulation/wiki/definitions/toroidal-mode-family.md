---
type: Definition
title: "Toroidal mode families in stellarators"
description: "In an equilibrium with N_fp field periods, a perturbation of toroidal mode number n couples linearly only to n ± k N_fp, so the toroidal spectrum splits into independent families; single-field-period runs keep only the family of the equilibrium harmonics, low-n physics needs the full torus, a two-period quasi-axisymmetric configuration destabilizes only its even family, and 3D walls with their own periodicity couple harmonics in the same way."
status: established
aliases: [mode family, mode families, toroidal mode family, N_f families, helical mode coupling]
tags: [stellarator, spectral, numerics, mhd, wall]
timestamp: 2026-10-16T18:00:00Z
---

# Toroidal mode families in stellarators

In an axisymmetric equilibrium each toroidal Fourier harmonic $n$ of a
linear perturbation evolves independently. A stellarator equilibrium with
$N_{\rm fp}$ field periods contains the toroidal harmonics $0,\pm N_{\rm
fp},\pm2N_{\rm fp},\dots$; the product of an equilibrium harmonic
$kN_{\rm fp}$ with a perturbation harmonic $n$ produces $n\pm kN_{\rm fp}$.
The linearized problem therefore couples a harmonic only to those that
differ from it by a multiple of $N_{\rm fp}$, and the toroidal spectrum
splits into $\lfloor N_{\rm fp}/2\rfloor+1$ independent **mode families**,
labelled by $n\bmod N_{\rm fp}$ up to sign
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §V–VI;
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.4, §3.1, citing
Schwab 1993). For $N_{\rm fp}=5$:

| family | harmonics $n$ | role |
|---|---|---|
| $n\equiv0\pmod 5$ | $0,5,10,15,\dots$ | the equilibrium harmonics; the only family a single-field-period run can represent |
| $n\equiv\pm1\pmod 5$ | $1,4,6,9,11,\dots$ | symmetry-breaking |
| $n\equiv\pm2\pmod 5$ | $2,3,7,8,12,\dots$ | symmetry-breaking |

Ramasamy et al. number these families 0, 1 and 2 (§2.4). For the
ten-period LHD, [Sato & Todo (2026)](/sources/sato-2026.md) (p. 4, citing
Schwab 1993) count $1+\lfloor N_{\rm fp}/2\rfloor=6$ families, labelled
$N_f=0,\dots,5$, the same count as above. For $N_{\rm fp}=2$ the rule
leaves two families, the even and the odd harmonics. A mode is
identified by its family and by its dominant $(m,n)$; its eigenfunction
carries sidebands at the other harmonics of the family
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.1, Fig. 2b).

## Linear and nonlinear coupling

* **Linear.** In the W7-A $(2,1)$ tearing case of JOREK3D the $n=1$
  harmonic drives the instability and $n=4,6,9$ grow with it through the
  toroidal geometry; harmonics of other families are not driven linearly
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI, Figs. 9–10).
  In W7-AS the $n=1$ family again leads, $n=4,6$ being the next largest,
  then $n=9,11$ ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md),
  §3.1, Fig. 3).
* **Nonlinear.** Families couple only nonlinearly. In W7-A, $n=1$ drives
  $n=2$ at about 2 ms, which then drives $n=3,7,8$; a secondary $(3,2)$
  island chain appears at saturation
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI). In W7-AS the
  $n\equiv\pm2$ family is driven nonlinearly as the $n\equiv\pm1$ family
  saturates ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.1).
  Which family dominates the saturated state depends on resistivity: at
  artificially high $\eta$ the $n\equiv\pm1$ family stays dominant with a
  $(2,1)$ island, at Spitzer $\eta$ the $n\equiv\pm2$ family dominates
  with a $(4,2)$ deformation (§4.4, Fig. 13; see
  [soft β limit](/definitions/soft-beta-limit.md)).
* **Strength.** In more optimized configurations the coupling stays strong
  "even in the second and third toroidal sidebands"
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.4).
  The opposite limit is a "2D-type" mode with weak toroidal coupling inside
  its family, for which the toroidal mode number alone identifies the
  eigenmode: the resistive ballooning modes of high-beta LHD MHD runs are
  of this type, and no strongly coupled "3D-type" ballooning modes were
  found (Sato et al. 2017, as reviewed by
  [Sato & Todo (2026)](/sources/sato-2026.md), p. 4).
* **Only one family unstable: the two-period QA case.** In full-torus
  M3D-C1 runs of an $N_{\rm fp}=2$ quasi-axisymmetric reactor equilibrium,
  with no symmetry imposed so that odd harmonics were allowed, only even
  harmonics are destabilized: all even $n$ from 6 to 30 have positive
  maximum kinetic-energy growth rates, largest for $20\le n\le28$
  ([Wright & Ferraro (2024)](/sources/wright-2024.md), §III, Figs. 3–4).
  The authors attribute the even-only spectrum to a single unstable
  eigenmode composed of many even harmonics through the $N_{\rm fp}=2$
  coupling (§III–IV); no odd-$n$ data or eigenmode analysis is shown, so
  the single-eigenmode reading is asserted rather than demonstrated. The
  coupling rule is mis-typeset in the paper (recorded on the Source page).
  They conclude that "field-periodicity plays an important role in
  nonlinear MHD stability, especially if there is a linearly unstable
  mode" and should be considered in optimization (§IV; see
  [edge instabilities of an optimized QA reactor stellarator](/results/stellarator-edge-instability-qa.md)).

## Consequences for simulations

* **Single field period versus full torus.** A run over one field period
  keeps only the equilibrium family: it suppresses symmetry-breaking modes
  and is cheaper. JOREK3D uses it to verify equilibrium preservation and to
  relax the force imbalance after the equilibrium import before a
  full-torus run ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §V;
  [Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.4, §3.1). Low-$n$
  dynamics need the full torus (§2.4). [M3D-C1](/software/m3d-c1.md) does
  the same for W7-X, running one field period with 16 toroidal elements to
  sustain the equilibrium and then the full torus with 80, the same
  per-period resolution ([Zhou et al. (2023)](/sources/zhou-2023.md),
  §III–IV).
* **Separate periodicities.** JOREK3D gives the grid geometry and the
  physics fields separate toroidal harmonic counts and periodicities, so a
  full-torus physics run sits on a five-periodic geometry
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), App. A).
* **Preconditioning.** The JOREK mode-group preconditioner couples
  adjacent harmonics of the same family; it "has been important for making
  simulations computationally manageable"
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.4; see
  [implicit time integration](/methods/implicit-time-integration.md)).
* **Truncation.** A family truncated at a few harmonics aliases couplings
  onto the retained ones (spectral blocking): adding $n=15$ to an
  $n=0,5,10$ ballooning run lowers the JOREK3D $n=10$ growth rate by 5–6 %
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VII; see
  [CASTOR3D](/software/castor3d.md)). The highest toroidal mode number
  needed for converged nonlinear W7-AS β evolution is about 50
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §4.3.1).
* **Tokamak analogue.** A toroidal wedge of angle $2\pi/k$ restricts a
  tokamak run to the multiples of $k$ in the same way; MIPS and MEGA run
  $n=3$ infernal modes on a $2\pi/3$ wedge, keeping $n=3,6,9,\dots$
  ([Sato et al. (2024)](/sources/sato-2024.md), §2).
* **Full torus for stellarators.** The LHD MIPS and MEGA runs use 640
  toroidal grid points ([Sato & Todo (2026)](/sources/sato-2026.md), p. 3;
  a full torus is implied, the wedge is not stated), and the QA M3D-C1 runs
  of Wright & Ferraro impose no symmetry at all (§II). In LHD the
  peripheral ballooning modes ($n=10$–13) generate an $n=1$ mode that
  carries the collapse into the core, a harmonic outside the equilibrium
  family (see
  [kinetic thermal ions confine LHD pressure-driven activity to the periphery](/results/kinetic-ions-prevent-core-collapse-lhd.md));
  in the QA case the unrestricted torus is what makes the absence of odd
  harmonics a result rather than a constraint.

## Coupling by three-dimensional conductors

The same selection rule applies to any non-axisymmetric structure. In
JOREK–CARIDDI simulations of an ASDEX Upgrade $2/1$ tearing mode kept to
$n=1,2$, equally spaced wall ports in numbers 2, 4, 6 or 8 give no
wall-mediated $n=1$/$n=2$ coupling ($n=2$ is driven nonlinearly with
$\gamma_2\approx2\gamma_1$), while 1 or 3 ports couple the two directly
($\gamma_2\approx\gamma_1$, earlier onset)
([Isernia et al. (2023)](/sources/isernia-2023.md), §VI, Table I, Fig. 8).
The authors caution that more harmonics could add indirect coupling and
conclude that the toroidal harmonics kept may have to be tuned to the
periodicity of the external conductors (§VI–VII); see
[resistive-wall coupling](/methods/resistive-wall-coupling.md).

# Citations

* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — families in JOREK3D, linear and nonlinear coupling, separate periodicities, spectral blocking.
* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — family numbering, mode-group preconditioning, single-period versus full-torus runs, family dominance.
* [Zhou et al. (2023)](/sources/zhou-2023.md) — one-period and full-torus M3D-C1 runs for W7-X.
* [Isernia et al. (2023)](/sources/isernia-2023.md) — harmonic coupling by wall ports.
* [Sato et al. (2024)](/sources/sato-2024.md) — toroidal wedge in a tokamak run.
* [Wright & Ferraro (2024)](/sources/wright-2024.md) — even-family destabilization in a two-period QA configuration.
* [Sato & Todo (2026)](/sources/sato-2026.md) — six LHD families, 2D-type weakly coupled ballooning modes.
