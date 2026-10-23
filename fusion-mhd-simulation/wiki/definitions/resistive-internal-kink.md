---
type: Definition
title: "Resistive internal kink (m/n = 1/1)"
description: "The m/n = 1/1 mode resonant at the q = 1 surface: a rigid helical shift of the core inside q = 1 that resistivity turns into a reconnecting mode with gamma ~ eta^(1/3); its ideal, pressure-driven limit has a poloidal-beta threshold, reduced MHD models fail to reproduce that limit at finite beta, and the mode triggers the thermal quench when SPI fragments reach q = 1."
status: established
aliases: [resistive kink, internal kink, m=n=1 mode, 1/1 kink, Coppi scaling]
tags: [kink, tearing, reduced-mhd, full-mhd, verification, tokamak]
timestamp: 2026-10-16T18:35:00Z
---

# Resistive internal kink (m/n = 1/1)

The internal kink has helicity $m/n=1/1$. It exists when the safety factor
falls below unity on axis ($q_0<1$), so that a $q=1$ surface lies inside the
plasma. The mode displaces the core inside $q=1$ rigidly and helically. In the
eigenfunction of [Ma & Guo (2022)](/sources/ma-2022.md) (§4.1, Fig. 9) the
displacement is a rigid $m=1$ shift inside $q=1$. Resistivity makes the layer a reconnection layer. The
resistive internal kink is the "nonconstant-$\psi$" $m=n=1$ mode (Ma & Guo
2022, §4.1), as opposed to the constant-$\psi$ regime of the
[tearing mode](/definitions/tearing-mode.md). Its linear growth rate scales as

$$\gamma\propto\eta^{1/3},\qquad\text{equivalently}\qquad \gamma\tau_A\propto S^{-1/3}.$$

[Zhang et al. (2021)](/sources/zhang-2021.md) cite this scaling to Coppi et
al. (§1, §3.2, ref. [6]) and Ma & Guo (2022) to Ara et al. 1978 (§4.1,
ref. [22]). Zhang et al. (§1) connect the mode to the sawtooth and to
Kadomtsev-type reconnection. They do not use the word "sawtooth" for the
nonlinear crash they simulate; the crash itself is on
[sawtooth crash and Kadomtsev reconnection](/definitions/sawtooth-crash.md).

**Ideal limit.** Without resistivity, the $1/1$ mode is driven by pressure. It
becomes unstable above a poloidal-beta threshold, which Bussac et al. (1975)
give as about 0.3 in large-aspect-ratio theory. Ma & Guo (2022, §4.1, Fig. 10)
find the ideal internal kink growth rate rising from about $0.5\times10^{-3}$
to $4\times10^{-3}\,\tau_A^{-1}$ as the axis pressure is raised. They quote a
threshold $\beta_p\approx0.375$ at $R_0/a=5$ and call it "consistent" with
0.3. The figure plots $\gamma$ against axis pressure, without a $\beta_p$ axis
and without the zero crossing. The 0.375 value therefore cannot be read off
the figure.

## Linear verification

- **CLT vs M3D-C1** ([CLT](/software/clt.md), [M3D-C1](/software/m3d-c1.md)).
  - *Equilibrium:* circular, $R_0/a=10$, $\beta\approx0$, with $q_0=0.7$ and
    edge value $q(\psi_N=1)=3.6$. The axis and edge slopes of $q(\psi_N)$
    are prescribed as 2.0 and 5.0; the paper leaves them undefined and the
    reader infers them from its Eq. 1.8. The $q=1$ surface sits at
    $r/a\approx0.43$.
  - *Scan:* $\eta=10^{-7}$ to $10^{-5}$, an inverse Lundquist number built
    on $a=1$ m, with all other diffusivities $10^{-8}$.
  - *Growth rates:* run from $3.00\times10^{-3}$ to $1.11\times10^{-2}$
    (CLT) and from $3.20\times10^{-3}$ to $1.15\times10^{-2}$ (M3D-C1), in
    units of $\tau_A^{-1}$. The codes differ by 2.7–6.3%; the paper says
    "about 5%".
  - *Printed fits:* $\eta^{0.31}$ and $\eta^{0.30}$ (legend 0.312 and 0.301).

  Source: Zhang et al. (2021), §3.2, Table 2, Fig. 12. The full case is on
  [CLT–M3D-C1 tearing and resistive-kink benchmark](/benchmarks/clt-m3d-c1-benchmark.md).
- **SCELT eigenvalue code** ([SCELT](/software/scelt.md)).
  - *Equilibrium:* circular, $R_0=5$, $a=1$, $p=p_0(1-r^2)$ with
    $p_0=5\times10^{-5}$ (normalized). $q$ runs from below 1 on axis to 1.98
    at the edge, with $q=1$ at $r/a=0.48$.
  - *Result:* $\gamma\propto\eta^{0.3766}$ over
    $\log_{10}\eta\in[-8,-4.6]$, in normalized units.

  Source: Ma & Guo (2022), §4, §4.1, Figs. 7–8.
- **JOREK reduced and full MHD vs CASTOR3D.** Linear $1/1$ cases scanned in
  $\eta$. Full MHD agrees with CASTOR3D. Reduced MHD deviates at low $\eta$
  even at $\beta_N=0.4\%$, and in a $\beta$ scan it "clearly fails"
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4, Figs. 18–19).
  The mechanism is given below.
- **With runaway electrons.** JOREK resistive-kink cases with a
  runaway-electron fraction of the plasma current of 0, 0.5 and 1 ($B=1$ T,
  $I_p=0.31$ MA, axis temperature 48 eV) follow the $S^{-1/3}$ scaling at
  large $\eta$ (Hoelzl et al. 2021, §4.7, Fig. 25).

## Nonlinear evolution

In the CLT–M3D-C1 runs at $\eta=10^{-5}$, the linear-phase growth rate is
about $0.011\,\tau_A^{-1}$, consistent with Table 2. The $n=0$ and $n=2$ beat
harmonics grow at about twice that rate. The $n=1$ kinetic energy peaks at
$4.4\times10^{-5}$ (CLT) and $4.2\times10^{-5}$ (M3D-C1), in normalized units,
near $t\approx2400\,\tau_A$. The growth rate then "suddenly reduces to a
negative value" (the crash), and the post-crash oscillations stay
qualitatively the same in both codes (Zhang et al. 2021, §3.2, Figs. 14–16).
The M3D-C1 curves are shifted by $270\,\tau_A$ for comparison, so the time to
the crash is not compared.

## Reduced MHD and the finite-$\beta$ internal kink

Hoelzl et al. (2021, §2.3.3) explain why the ansatz-based
[reduced MHD](/methods/reduced-mhd.md) of JOREK fails for the pressure-driven
internal kink at finite $\beta$, following Graves et al. (their ref. [69]).
The reduced ansatz keeps the perturbation of the parallel field near zero. Full
MHD would instead have the field perturbation balance the pressure
perturbation, $B\,\delta B_\parallel/\mu_0\approx-\delta p$. The reduced
energy principle therefore contains a spurious positive-definite term,

$$\frac{1}{2\mu_0}\int\Big(\delta B_\parallel+\frac{\mu_0\,\delta p}{B}\Big)^2\,dV,$$

which stabilizes the mode. Here $\delta$ denotes the linear perturbation
and $B$ is the equilibrium field; the source writes both expressions in
JOREK units ($\mu_0=1$). Edge ballooning
modes are largely unaffected because $q\gg1$ there (see
[ballooning mode](/definitions/ballooning-mode.md)).
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§VIII) repeat the
limitation for the JOREK model family, citing Hoelzl et al. (2021): it
"cannot accurately reproduce kink modes at higher β". The two sources agree,
and so do two chunk-2 JOREK papers:
[Hu et al. (2023)](/sources/hu-2023.md) (§2.2) state that reduced MHD "tends
to underestimate" the $1/1$ resistive kink, and
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§2.3) that the finite-$\beta$
$(1,1)$ internal kink is not captured by reduced models while most other
instabilities are, both citing earlier JOREK work.

## Non-resonant kink ($q_{\min}$ slightly above 1)

With a weakly reversed $q$ profile and $q_{\min}$ just above 1, a $(1,1)$
"non-resonant kink" remains unstable. In a DIII-D hybrid equilibrium, MHD-only
M3D-C1-K runs find the $n=1$ kink unstable for $q_{\min}<1.06$, with
$\gamma\tau_A\approx0.026$ at $q_{\min}=1.00$ falling to zero at 1.06 (figure
readings). At fixed $q_{\min}=1.04$ its growth rate depends strongly on
$\beta$, rising from 0 at $\beta/\beta_{\mathrm{exp}}=0.8$ to
$\gamma\tau_A\approx0.021$ at 1.2 ($\beta_{\mathrm{exp}}$ the experimental
value), "similar to pressure-driven modes"
([Liu et al. (2022b)](/sources/liu-2022-b.md), §4, Figs. 5, 10; $\tau_A$ not
defined by the source). Kinetic thermal ions and energetic particles turn the
mode into a non-resonant [fishbone](/definitions/fishbone.md) (same source).

**In gas-injection thermal quenches.** In a SPARC target with
$q_{\min}=1.05$ and no $q=1$ surface, a large 1/1 mode grows during the
NIMROD gas-injection TQ. Its flows pull neon blobs from the edge into a
single helical flux tube at $q\approx1.05$ at mid-radius, where the
radiation flash peaks at the start of the mixing
([Izzo et al. (2025)](/sources/izzo-2025.md), §II C–D, Fig. 7). The small
$n=1$ field of a closed-circuit
[runaway-electron mitigation coil](/definitions/runaway-electron-mitigation-coil.md)
makes the large unstable $n=1$ grow and saturate earlier (§III B), and a
1000-fold mass density in the region between limiter and vessel forestalls
it, letting higher-$n$ modes collapse the mid-radius temperature first
(§III C, Fig. 9). No growth rates are given.

## Stellarators: two $\iota=1$ surfaces

In a stellarator the condition $q_0<1$ reads $\iota>1$ somewhere inside. In
M3D-C1 simulations of W7-X, near-axis current drive raises $\iota$ above 1 in
a hump, which creates two $\iota=1$ surfaces and two successive $(1,1)$
internal kinks: the inner one moves the core in one direction and lowers the
core $T_e$ only slightly, the outer one moves the new core the opposite way
and flattens it, with a crash of about 50% and $r/a\approx0.4$ inversion
radius ([Zhou et al. (2023)](/sources/zhou-2023.md), §IV, Figs. 3–6). No
growth rates are given, so nothing can be checked against $\eta^{1/3}$. A
saturated $(1,1)$ core follows ([magnetic flux pumping](/definitions/magnetic-flux-pumping.md)).

## The internal kink in applications

- **Fishbone.** With energetic particles, the $n=1$ ideal internal kink
  turns into a [fishbone](/definitions/fishbone.md) with finite real
  frequency as the energetic-particle share of $\beta$ rises from 0 to 0.75
  ([Liu et al. (2022)](/sources/liu-2022.md), §6.1, Fig. 3).
- **Flux pumping.** A $1/1$ quasi-interchange mode can keep $q_0\ge1$ when
  the pressure is peaked enough, which prevents sawteeth
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.4; see
  [magnetic flux pumping](/definitions/magnetic-flux-pumping.md)). The
  primary JOREK study of an ASDEX Upgrade hybrid discharge finds the
  saturated 1/1 state holding the axisymmetric $q_0\approx0.99$ instead,
  with two twisted 1/1 flux tubes in the core: the original one keeps a
  local $q_0\approx1.04$ (ideal quasi-interchange, topology unchanged), and
  a new island-like tube has a local $q_0\approx0.97$ (resistive tearing).
  The flow concentrates at the X-point beneath the new tube, "suggesting an
  incomplete magnetic reconnection", and the authors call the mode "a
  combination of the 1/1 ideal quasi-interchange mode and the 1/1 resistive
  tearing mode" ([Zhang et al. (2025)](/sources/zhang-2025.md), §3.4,
  Fig. 12, §6.1; local $q$ from field-line tracing about the helical axis).
  At lower Hartmann number (raised resistivity and viscosity) the state
  turns into sawtooth-like oscillations and then into a quasi-stationary
  1/1 resistive internal kink with $q_0\sim0.7$ (§6.2; stated, not shown).
  The current redistribution is carried by an
  [MHD dynamo](/definitions/mhd-dynamo.md) (same source, §4). See
  Contradictions.
- **Suppression by construction.** NIMROD NTM studies and linear M3D-C1
  resistive-wall studies raise $q_0$ above 1 to suppress the $(1,1)$ mode and
  sawteeth ([Howell et al. (2022)](/sources/howell-2022.md), §III A;
  [Strauss et al. (2022)](/sources/strauss-2022.md), §II).
- **Disruptions.**
  - In ITER $\beta$-limit disruptions, a dominant $n=1$ internal kink grows
    into the disruptive state (Hoelzl et al. 2024, §3.1; the evidence is a
    Master's thesis, their ref. [40]).
  - In shattered-pellet simulations, core mixing is better than with
    massive gas injection, and the $1/1$ kink matters for it (Hoelzl et al.
    2021, §6; see
    [shattered pellet injection](/definitions/shattered-pellet-injection.md)).
  - Core density transport depends on where material is deposited relative
    to $q=1$ (Hoelzl et al. 2024, §3.2).
  - **Core collapse at the end of an SPI TQ.** In neon-doped deuterium SPI
    into an ASDEX Upgrade H-mode, the TQ is triggered at $q=2$, and a 1/1
    mode in its second, radiative stage leads to the core collapse: core
    $T_e$ "suddenly drops to below 10 eV following the 1/1 MHD activity",
    with a second magnetic-energy and radiation peak, earlier and stronger
    at higher neon fraction; pure deuterium injection shows no such stage
    ([Tang et al. (2025)](/sources/tang-2025.md), §3.2, Figs. 5e, 11–12).
  - **SPI trigger at $q=1$.** In ITER L-mode plasmas with a large
    $q\approx1$ region, the thermal quench after neon or neon–hydrogen SPI is
    triggered when the vanguard fragments enter $q=1$: helical cooling there
    destabilizes the $1/1$ kink, whose O-point coincides with the fragments
    ([Hu et al. (2021)](/sources/hu-2021.md), §4.1, Figs. 13–14;
    [Hu et al. (2023)](/sources/hu-2023.md), §3.1, Figs. 3–4). Without
    injection the kink stays negligible on the simulated time scale, because
    $\beta$ is low and the resistive kink is slow (Hu et al. 2021, §2.4;
    Hu et al. 2023, §2.2). In a JET-like plasma with almost no $q<1$ region
    the trigger is at $q=2$ instead (Hu et al. 2021, §3; see
    [thermal quench](/definitions/thermal-quench.md)).
  - **Kink convection of injected material.** Material deposited on or inside
    $q=1$ is convected into the core by the kink displacement, so deeper
    neon–hydrogen pellets give much better core neon penetration than pure
    neon pellets (Hu et al. 2021, §4.1). Density cells move by $O(1\,\mathrm m)$
    in 0.2 ms while the fragments move 0.1 m, accompanied by a "cold bubble";
    an axisymmetric twin run stays hollow (Hu et al. 2023, §3.1, Figs. 6–7).
    After core relaxation the current flattens inside $q=1$ with a negative
    current sheet outside (Hu et al. 2023, Fig. 10).
  - **Injection symmetry.** Symmetric dual SPI makes even-$n$ modes dominate
    and removes the $1/1$ kink motion; a 1 ms injector delay restores $n=1$
    dominance and a $1/1$ kink at the thermal quench (Hu et al. 2021, §5).
  - An off-axis runaway-electron current destabilizes the $1/1$ mode
    (Hoelzl et al. 2021, §6).
  - After the runaway loss that terminates a DIII-D runaway plateau, $q_0$
    drops from 1.10 to 1.0 and a $(1,1)$ kink flattens the residual runaway
    core ([Liu et al. (2021)](/sources/liu-2021.md), §5.3, Fig. 12b).

## Qualifications

**Fitted kink exponents.** The printed exponents bracket the theoretical
$1/3$ from both sides, and none of the sources states its fit range.

- Zhang et al. (2021, Fig. 12) print 0.31 (CLT) and 0.30 (M3D-C1).
- *Compiler's check, not a source claim:*
  - Fitting all five points of their Table 2 in log–log gives 0.285 (CLT)
    and 0.281 (M3D-C1).
  - Fitting only the three lowest-$\eta$ points ($\eta\le10^{-6}$) gives
    0.313 and 0.301. These reproduce the printed values, so the printed
    exponents are presumably low-$\eta$ fits.
  - The three highest-$\eta$ points give 0.25.
  - The local exponent therefore rises toward $1/3$ as $\eta$ decreases.
- Ma & Guo (2022) obtain 0.3766, about 13% above $1/3$. Their scan reaches
  $10^{-8}$ in a different normalization ($R_0/a=5$, finite but small
  pressure).

Both results count as consistent with $1/3$ in the sense their authors claim,
but at a precision of about 15%, not the two-digit agreement the printed
exponents suggest. The ideal-limit threshold of Ma & Guo (0.375 against 0.3)
is a 25% difference at $R_0/a=5$, compared with large-aspect-ratio theory. It
is a weak check, not a confirmation.

## Contradictions

Reduced and full MHD differ on the finite-$\beta$ internal kink, but this is
a known model limitation that both citing sources state the same way, not a
disagreement between sources.

**Value of $q_0$ held by the 1/1 mode in flux pumping — Open.**
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§4.4) summarize flux
pumping as keeping $q_0\ge1$; [Zhang et al. (2025)](/sources/zhang-2025.md)
(§3.4, Figs. 9, 12), the primary JOREK study with an overlapping author
list, find the axisymmetric $q_0\approx0.99$ and a local 0.97 in the
reconnected tube, with only the original tube at 1.04. The entry is
recorded in full on [magnetic flux pumping](/definitions/magnetic-flux-pumping.md);
on this page it bears on whether the saturated state contains a resistive
1/1 component inside a $q<1$ region.

# Citations

- [Zhang et al. (2021)](/sources/zhang-2021.md) — §1, §3.2, Table 2, Figs. 10–16.
- [Ma & Guo (2022)](/sources/ma-2022.md) — §4.1, Figs. 7–10.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.3.3, §4.4, §4.7, §6.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.1, §3.2, §4.4.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §VIII.
- [Liu et al. (2022)](/sources/liu-2022.md) — §6.1, Fig. 3.
- [Liu et al. (2022b)](/sources/liu-2022-b.md) — §4, Figs. 5, 10.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §IV, Figs. 3–8.
- [Hu et al. (2021)](/sources/hu-2021.md) — §2.4, §3–5.
- [Hu et al. (2023)](/sources/hu-2023.md) — §2.2, §3.1, Figs. 3–7, 10.
- [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §2.3.
- [Howell et al. (2022)](/sources/howell-2022.md) — §III A.
- [Strauss et al. (2022)](/sources/strauss-2022.md) — §II.
- [Liu et al. (2021)](/sources/liu-2021.md) — §5.3.
- [Zhang et al. (2025)](/sources/zhang-2025.md) — §3.4, §6.1–6.2, Fig. 12.
- [Tang et al. (2025)](/sources/tang-2025.md) — §3.2, Figs. 11–12.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §II C–D, §III B–C.
