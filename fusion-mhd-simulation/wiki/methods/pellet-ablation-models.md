---
type: Method
title: "Pellet ablation and fragmentation models"
description: "The source models that MHD codes use for shattered pellet injection: neutral-gas-shielding ablation scalings per fragment (with mixture and magnetic-field factors, evaluated locally or on flux-surface averages), a statistical fragmentation size distribution, straight-line fragment trajectories, and Gaussian or tanh density sources whose toroidal width is set by resolution."
status: established
aliases: [NGS ablation, neutral gas shielding, pellet ablation model, statistical fragmentation model, SPI source model, fragment ablation]
tags: [disruption, impurities, numerics, mhd]
timestamp: 2026-10-16T20:00:00Z
---

# Pellet ablation and fragmentation models

[Shattered pellet injection](/definitions/shattered-pellet-injection.md)
enters an MHD code as a set of moving point sources: each fragment carries
a mass, follows a prescribed trajectory, loses mass at an ablation rate set
by the local plasma, and deposits it through a smooth density source. The
codes of this bundle (JOREK in all cases below) do not resolve the
ablation cloud; the source model is the closure.

Page-local symbols: $r_{\mathrm f}$ the fragment radius, $\dot M$ the
fragment's mass ablation rate, $X$ the molar fraction of the hydrogenic
species in a mixed pellet, $k_{\mathrm f}$ the inverse characteristic
fragment size, $(R_{\mathrm f},Z_{\mathrm f},\phi_{\mathrm f})$ the fragment
position.

## 1. Neutral-gas-shielding ablation

The ablation rate is the one at which the neutral cloud just shields the
incoming parallel electron heat flux (neutral gas shielding, NGS); the
resulting scalings are $\dot M\propto T_e^{5/3}r_{\mathrm f}^{4/3}n_e^{1/3}$.

- **JOREK base model.** NGS-type scalings, fragments on straight lines at
  constant velocity ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8).
- **Radius form.** $\frac{d}{dt}r_{\mathrm f}^{5/3}=-\mathcal R\,n_e^{1/3}T_e^{5/3}$
  with a per-fragment coefficient $\mathcal R$, equivalent to a mass rate
  $\propto r_{\mathrm f}^{4/3}n_e^{1/3}T_e^{5/3}$
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.1, Eq. 47).
- **Mixed pellets (Parks).** In practical units ($\dot M$ in g/s, $T_e$ in
  eV, $r_{\mathrm f}$ in cm, $n_e$ in $10^{14}$ cm$^{-3}$)
  $$\dot M=\lambda(X)\,\zeta_B\Big(\frac{T_e}{2000}\Big)^{5/3}\Big(\frac{r_{\mathrm f}}{0.2}\Big)^{4/3}n_e^{1/3},\qquad \lambda(X)=27.08+\tan(1.49X),$$
  with the neon and D$_2$ molar rates in proportion $(1-X):X$ divided by the
  mean molar mass ([Hu et al. (2021)](/sources/hu-2021.md), §2.2,
  Eqs. 13–16, without $\zeta_B$; [Hu et al. (2023)](/sources/hu-2023.md),
  §2.1, Eqs. 14–15, with it; [Tang et al. (2025)](/sources/tang-2025.md),
  §2.2, Eq. 11, for neon-doped deuterium pellets in ASDEX Upgrade, without
  $\zeta_B$ and with $X$ the molecular ratio $N_{\mathrm D_2}/(N_{\mathrm D_2}+N_{\mathrm{Ne}})$;
  Tang et al. do not state whether the evaluation is local or flux-averaged). Pure-impurity pellets use Sergeev's model in
  Hu et al. (2021). Argon–D$_2$ pellets are assumed to separate into pure
  fragments because the triple points differ, with $\lambda_{\mathrm{Ar}}=36.63$
  and $\lambda_{\mathrm D_2}=39.00$ (Hu et al. 2021, Eq. 17).
- **Magnetic reduction.** $\zeta_B\simeq\big(2/\max(B[\mathrm T],2)\big)^{0.843}$
  (Hu et al. 2023, §2.1; its §2.4 scaling uses the exponent 0.842, a
  printed inconsistency). Removing $\zeta_B$ raises radiation strongly but
  assimilation only mildly (§4.1, Fig. 18).
- **Local against non-local evaluation.** "Local" ablation uses $T_e$, $n_e$
  at the fragment; "non-local" uses their flux-surface averages, to represent
  the long-mean-free-path hot electrons that actually reach the fragment.
  The local scheme suffers from the
  [electron temperature hole](/results/electron-temperature-hole.md) that the
  fragment's own cloud digs, which cuts ablation; the 3D non-local
  assimilation converges to the 2D result (Hu et al. 2023, §3.2, §4.1,
  Fig. 16).
- **Electron temperature.** Ablation is driven by electrons; a
  single-temperature model, which lets ions heat electrons artificially,
  overestimates it (Hu et al. 2021, §4.2, stated, not tested).

## 2. Fragmentation

The statistical fragmentation model gives the fragment-radius density

$$P(r_{\mathrm f})=k_{\mathrm f}^2\,r_{\mathrm f}K_0(k_{\mathrm f}r_{\mathrm f}),$$

normalized since $\int_0^\infty r K_0(k r)\,dr=k^{-2}$
([Hu et al. (2021)](/sources/hu-2021.md), Eq. 18;
[Hu et al. (2023)](/sources/hu-2023.md), Eqs. 18–19, where the fragment
number $N_{\mathrm f}$ follows from $N_{\mathrm f}\,n_{\mathrm{solid}}\,6\pi^2k_{\mathrm f}^{-3}=N_0$
with $N_0$ the atoms in the pellet; [Bhole et al. (2023)](/sources/bhole-2023.md),
§4.1). Fragments get a uniform speed spread and a 20° cone (Hu et al. 2021,
2023; [Hu et al. (2024)](/sources/hu-2024.md), §2.1); there is no rocket
effect, drag or size–velocity correlation (Hu et al. 2023, §2.3).
[Tang et al. (2025)](/sources/tang-2025.md) (§2.2) sample the radii from
Parks' fragmentation model by rejection sampling, stopped when the
accumulated volume equals the pellet volume, and draw speeds from a
**Gaussian** with mean $(v_{\mathrm{par}}+v_{\mathrm{pel}})/2$ and standard
deviation 20% of the mean ($v_{\mathrm{pel}}$ the injection speed,
$v_{\mathrm{par}}$ its component along the shatter plane; page-local), a
spread taken from laboratory observation, instead of the uniform spread of
Hu et al.; directions are uniform in a 20° cone and all fragments start at
the midpoint between the bend and the exit of the shatter tube. The impact
speed normal to the shatter plane sets the fragment size and the component
along it sets the fragment velocities, so a slower pellet at a steeper
shatter angle reproduces the same fragments (25° at 222 m/s for 12.5° at
443 m/s, Table 1; the compiler checked $443\sin12.5°\approx96$ against
$222\sin25°\approx94$ m/s). Shatter angles of 12.5°, 20° and 25° give 53,
199 and 1105 fragments. No rocket effect is modelled, which the authors
name as a candidate cause of their size-effect discrepancy (§3.3, §4).
Used
values: 100–1000 fragments; $k_{\mathrm f}^{-1}\simeq1.43$ mm for an ITER
pellet of $5\times10^{22}$ Ne and $1.8\times10^{24}$ D in 300 fragments (Hu
et al. 2023), a value the compiler could not reproduce without an
unstated solid density.

**Size effect.** Because $k_{\mathrm f}^{-1}$ scales with the pellet length,
$N_{\mathrm f}$ is roughly independent of pellet size, and the ablation time
of the plume scales as $N_0^{5/9}B^{0.842}$; at fixed injected quantity per
plasma volume this is $\propto R^{5/3}B^{0.842}$
([Hu et al. (2023)](/sources/hu-2023.md), §2.4, a scaling argument). With
current redistribution scaling as the square of the size and fragment
flight time linearly, larger devices respond more slowly
(same section; [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.1).
In ASDEX Upgrade, more and smaller fragments of a 0.12%-neon pellet give
a shorter TQ and a higher assimilation, because ablation ends when the
fragments leave the plasma; experiments show the opposite trend
([Tang et al. (2025)](/sources/tang-2025.md), §3.3, §3.5; see
[shattered pellet injection](/definitions/shattered-pellet-injection.md)).

## 3. Deposition

- **tanh profile.** $S_\rho\propto[0.5-0.5\tanh(\cdot)]$ in poloidal distance
  and in $\phi-\phi_{\mathrm f}$, with widths $\delta r_c$, $\delta\phi_c$
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8, Eq. 44).
- **Gaussian profile.**
  $$S_\rho\propto\exp\Big(-\frac{(R-R_{\mathrm f})^2+(Z-Z_{\mathrm f})^2}{\Delta r^2}\Big)\exp\Big(-\frac{(\phi-\phi_{\mathrm f})^2}{\Delta\phi^2}\Big)$$
  with $\Delta r=2$ cm, $\Delta\phi=1$ rad ([Hu et al. (2021)](/sources/hu-2021.md),
  Eq. 19), $\Delta r=0.08$ m and $\Delta\phi=0.3$ or 0.5 rad
  ([Hu et al. (2023)](/sources/hu-2023.md), Eq. 13;
  [Hu et al. (2024)](/sources/hu-2024.md), Eq. 1), $\Delta r=0.03$ m and
  $\Delta\phi=0.8$ rad for $n=0$–7 in ASDEX Upgrade, the poloidal width
  being about the grid spacing ([Tang et al. (2025)](/sources/tang-2025.md),
  Eq. 12, §3.1), Gaussian in $(R,Z)$ and $\phi$ in
  [Bhole et al. (2023)](/sources/bhole-2023.md) (Eq. 48).
- **The toroidal width is set by resolution.** All sources call the
  toroidal elongation artificial: it is what $n\le11$ toroidal harmonics can
  represent (Hu et al. 2023, §2.2, which keeps the source's Fourier content
  to first order for 0.3 rad). Tang et al. (2025, §3.1) set 0.8 rad by the
  toroidal resolution of eight harmonics and 0.03 m by the poloidal grid
  spacing, below which the source would be under-resolved. The poloidal
  width is insensitive as long as it stays below the plume width (Hu et
  al. 2023, 2024).

## Consequences of the toroidal width

The width is the most consequential free parameter of the model:

- Results converge in it for deuterium pellets but not necessarily for
  impurity pellets, whose radiated power scales as its inverse
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8).
- Narrowing it from 0.5 to 0.3 rad raises radiation less than
  proportionally, attributed to parallel relaxation and merging of plasmoids
  ([Hu et al. (2023)](/sources/hu-2023.md), §4.2, Fig. 19).
- A wide source mitigates radiation peaking artificially
  ([Hu et al. (2021)](/sources/hu-2021.md), §2.2), although the AUG runs
  at 0.8 rad *over*estimate the early peaking relative to experiment
  ([Tang et al. (2025)](/sources/tang-2025.md), §3.5; see
  [radiation asymmetry](/definitions/radiation-asymmetry.md)), and it
  under-predicts
  [plasmoid drift](/definitions/plasmoid-drift.md)
  ([Kong et al. (2025)](/sources/kong-2025.md), §3.2, §5).

The contradiction between the first two items is recorded on
[shattered pellet injection](/definitions/shattered-pellet-injection.md).

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8, §6.2.1, Eq. 44.
- [Bhole et al. (2023)](/sources/bhole-2023.md), §4.1, Eqs. 47–48.
- [Hu et al. (2021)](/sources/hu-2021.md), §2.2, §4.2, Eqs. 13–19.
- [Hu et al. (2023)](/sources/hu-2023.md), §2.1–2.4, §3.2, §4.1–4.2, Eqs. 13–19.
- [Hu et al. (2024)](/sources/hu-2024.md), §2.1, Eq. 1.
- [Kong et al. (2025)](/sources/kong-2025.md), §3.2, §5.
- [Tang et al. (2025)](/sources/tang-2025.md), §2.2, §3.1, §3.3, §3.5, §4, Eqs. 11–12, Table 1.
