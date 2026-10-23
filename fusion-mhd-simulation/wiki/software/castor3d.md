---
type: Software
title: "CASTOR3D"
description: "Linear full-MHD stability code for three-dimensional (stellarator and tokamak) equilibria with visco-resistive and extended-MHD effects and thin conductors, used as the linear reference of JOREK and JOREK3D: tokamak kink, tearing and passive-coil VDE benchmarks, and stellarator tearing, ballooning and interchange benchmarks whose agreement ranges from about 3 % to 26 %."
status: established
aliases: [CASTOR-3D, CASTOR 3D]
tags: [stellarator, tokamak, spectral, verification, tearing, ballooning]
timestamp: 2026-10-16T18:35:00Z
---

# CASTOR3D

CASTOR3D is a linear stability code for three-dimensional equilibria,
developed by Strumberger and Günter (2017, 2019; not ingested). The
sources of this bundle describe it as "a full MHD model including
viscoresistive and extended MHD effects"
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3) and use it as the
linear full-MHD reference against which the nonlinear initial-value code
[JOREK](/software/jorek.md) and its stellarator version
[JOREK3D](/software/jorek3d.md) are verified
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI–VII;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4, §4.8). It belongs to
the family of [linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md).

## Capabilities named in the sources

* **Full MHD, linear.** CASTOR3D retains the compressional and parallel
  dynamics that the [stellarator reduced MHD](/methods/stellarator-reduced-mhd.md)
  model of JOREK3D drops, which is why it is the reference for testing that
  reduction ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI;
  [Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.2).
* **Free-boundary external modes.** In a five-period $l=2$ classical
  stellarator it identifies an $n=5$ free-boundary external mode that grows
  faster than the internal interchange modes above $\beta\approx0.6\,\%$
  (about $1.5\times10^5\ \mathrm s^{-1}$ at $\beta=1.3\,\%$, read from the
  figure); JOREK3D, being fixed-boundary, cannot benchmark it
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.2, Fig. 5b).
* **Conductors.** CASTOR3D, like VALEN and [MARS-F](/software/mars-f.md),
  is a linear code that treats conducting structures as thin conductors
  only ([Isernia et al. (2023)](/sources/isernia-2023.md), §I). In the
  tokamak passive-coil benchmark it treats the scrape-off layer as vacuum,
  so the JOREK runs need a high scrape-off-layer resistivity to match it
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8).
* **W7-X studies.** Linear CASTOR3D calculations find W7-X-type equilibria
  unstable to single and double tearing modes and to resistive kinks, cited
  as motivation for nonlinear stellarator MHD
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VIII;
  [Zhou et al. (2023)](/sources/zhou-2023.md), §I, both citing Strumberger
  et al. 2020).
* **Planned tokamak use.** A CASTOR3D linear stability analysis of the
  saturated, flux-pumped states of an ASDEX Upgrade hybrid scenario is
  announced as future work, not performed
  ([Zhang et al. (2025)](/sources/zhang-2025.md), §6.2; see
  [magnetic flux pumping](/definitions/magnetic-flux-pumping.md)).

## Benchmarks

| Case | Partner | Agreement | Source |
|---|---|---|---|
| tokamak $1/1$ resistive kink, $2/1$ tearing, $\eta$ scan | JOREK full MHD | agrees; JOREK reduced MHD deviates at low $\eta$ for the kink and "clearly fails" at finite $\beta$ | [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4, Figs. 18–19 |
| ASDEX Upgrade passive-coil VDE growth rate | JOREK–STARWALL | within about 20 % over orders of magnitude of coil conductivity | [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8, Fig. 30 |
| W7-A $(2,1)$ tearing, $\beta$ scan | JOREK3D ($v_\parallel=0$) | within 13.2 %, JOREK3D higher | [Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI, Fig. 8a |
| W7-A $(2,1)$ tearing, $\eta$ scan | JOREK3D ($v_\parallel=0$) | within 26.2 %, at the highest $\eta$ | same, Fig. 8b |
| W7-A ballooning, $n=0,5,10$ | JOREK3D | within 6.4 %, three of four cases below 3 % | same, §VII, Fig. 12 |
| W7-AS $(2,1)$ tearing, $\eta$ scan | JOREK3D ($v_\parallel=0$) | maximum deviation about 3 %; eigenfunctions agree, CASTOR3D sidebands below 6 % larger | [Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.1, Fig. 2 |
| low-shear $l=2$ stellarator interchange, $\Gamma=0$ | JOREK3D without parallel flow | "agrees very well", marginal point included | same, §3.2, Fig. 5a |
| same, $\Gamma=5/3$, $n=2$–15 | JOREK3D with parallel flow | within 10 %; without parallel flow JOREK3D is too stable and misses $n<7$ | same, §3.2, Figs. 5b, 7 |

The stellarator cases are described on
[JOREK3D](/software/jorek3d.md) and
[interchange modes](/definitions/interchange-mode.md).

## Numerical behaviour

* **Insensitivity to spectral truncation.** Adding the harmonic $n=15$ to
  the W7-A ballooning case changes the CASTOR3D $n=10$ growth rate by less
  than 0.003 %, against 5–6 % for JOREK3D; the authors attribute most of the
  ballooning discrepancy to spectral blocking in the nonlinear code
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VII).
* **Poloidal resolution.** Ramasamy et al. state that in the W7-A tearing
  study of Nikulsin et al. "the helical mode coupling was not correctly
  resolved … due to the use of insufficient poloidal resolution in
  CASTOR3D", and that at higher poloidal resolution the agreement is
  similar to their 3 % ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md),
  §3.1). No figure or number is given for the re-run; the conflict with the
  original attribution is recorded below.
* In the W7-AS tearing scan CASTOR3D reaches lower resistivities (about
  $2\times10^{-7}\ \Omega$ m) than JOREK3D (about $6\times10^{-7}\ \Omega$ m)
  and follows an $\eta^{0.6}$ line at low $\eta$, bending below it at high
  $\eta$ (same source, §3.1, Fig. 2a; see
  [tearing mode](/definitions/tearing-mode.md)).

## Contradictions

* **Cause of the 2022 JOREK3D–CASTOR3D tearing gap.** *Open; kept Open by human decision (2026-10-16): the later attribution shows no re-run, so it does not supersede.*
  [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§VI) attribute the
  26.2 % deviation at high $\eta$ "most likely" to the neglect of
  $v_\parallel$ in JOREK3D.
  [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§3.1), with two of
  the same authors, attribute it to insufficient CASTOR3D poloidal
  resolution and state that the gap closes at higher resolution, without
  showing the re-run. The later paper is an explicit re-attribution by the
  original authors; whether a statement without data supersedes the shown
  2022 result is left to the human. The same entry is kept on
  [JOREK3D](/software/jorek3d.md).

# Citations

* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — W7-A tearing and ballooning benchmarks, spectral blocking, W7-X outlook.
* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — W7-AS tearing and interchange benchmarks, external mode, resolution re-attribution.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — tokamak kink, tearing and VDE benchmarks.
* [Isernia et al. (2023)](/sources/isernia-2023.md) — thin-conductor limitation.
* [Zhou et al. (2023)](/sources/zhou-2023.md) — cited linear W7-X kink studies.
* [Zhang et al. (2025)](/sources/zhang-2025.md) — planned stability analysis of flux-pumped states.
