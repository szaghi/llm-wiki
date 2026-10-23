---
type: Source
title: "Strauss et al. (2022) — Resistive wall tearing mode disruptions in DIII-D and ITER tokamaks"
description: "Identifies the resistive wall tearing mode, a (2,1) tearing mode stable with an ideal wall but destabilized by wall resistivity, as the cause of the thermal quench in DIII-D locked-mode shot 154576, using a cylindrical thin-wall dispersion relation, linear M3D-C1 and nonlinear M3D simulations, and extrapolates 75–125 ms thermal quenches for ITER."
resource: "doi:10.1063/5.0107048"
source_kind: paper
authors: [Strauss H.R., Lyons B.C., Knolker M.]
year: 2022
venue: "Phys. Plasmas 29:112508"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/0000_manual_no_journal_Unknown_10106350107048titleResistive.pdf"
tags: [tearing, disruption, wall, mhd, tokamak]
timestamp: 2026-10-16T16:51:00Z
---

# Summary

This short paper (cylindrical theory, linear M3D-C1, nonlinear M3D)
argues that the thermal quench (TQ) of a typical DIII-D locked-mode
disruption, shot 154576, is caused by a resistive wall tearing mode
(RWTM): a [tearing mode](/definitions/tearing-mode.md) that is stable with
an ideally conducting wall but becomes unstable because its flux diffuses
through a resistive wall. The measured TQ lasts about half a wall time
($\approx2.5$ ms with $\tau_w=5$ ms), as in JET. A cylindrical thin-wall
dispersion relation combining the tearing layer with a
logarithmic-derivative wall condition gives asymptotic growth-rate
scalings in $S$ and in the wall Lundquist number
$S_{\mathrm{wall}}=\tau_w/\tau_A$. Linear
[M3D-C1](/software/m3d-c1.md) runs on the equilibrium reconstruction at
3312 ms find a (2,1) mode unstable with a resistive wall and stable with an
ideal wall, with $\gamma\tau_A\propto S_{\mathrm{wall}}^{-2/3}$ at large
$S_{\mathrm{wall}}$. Nonlinear M3D runs ($S=10^6$, 16 poloidal planes,
$S_{\mathrm{wall}}=10^3$–$3.3\times10^4$) show the RWTM growing to large
amplitude and producing a complete TQ by parallel transport, with a TQ
time of about $3.4/\gamma$ and, at the experimental
$S_{\mathrm{wall}}=1.2\times10^4$, $\tau_{\mathrm{TQ}}/\tau_A\approx
S_{\mathrm{wall}}/2$. The simulated peak wall perturbation
($8.8\times10^{-3}$) matches the measured $8.4\times10^{-3}$. The onset
condition is the $q=2$ surface lying close enough to the wall (radius
ratio above 0.65 in a step-current model), consistent with a DIII-D
locked-mode database. With ITER's 250 ms wall time the authors extrapolate
TQ times of 75–125 ms and call ITER disruptions potentially "significantly
more benign than previously predicted".

# Key claims

1. **Experimental TQ time** (§I, Fig. 1). In DIII-D 154576 the TQ takes
   about 2.5 ms (27.5–30 ms on the Fig. 1 time base),
   $\tau_{\mathrm{TQ}}\approx0.5\tau_w$ with $\tau_w=5$ ms; JET 81540 had
   $\tau_{\mathrm{TQ}}=0.3\tau_w=1.5$ ms. Stated (data reproduced from
   Sweeney et al. 2018 and Strauss 2021).
2. **TQ time tracks the mode growth** (§I). "The TQ time is proportional
   to the experimental growth time of the n = 1 magnetic perturbations".
   Stated; no experimental growth time is quoted.
3. **Against the critical-amplitude picture** (§I). In many cases (e.g.
   Fig. 1) the mode amplitude does not rise before the TQ, which the
   authors oppose to island overlap at a critical amplitude (de Vries et
   al.). Stated.
4. **RWTM dispersion relation** (§II, Eqs. 1–5). Combining the tearing
   layer with a thin-wall condition gives Eq. 2 (Models and numerics) with
   the limits: no wall effect for $S_{\mathrm{wall}}\to\infty$; highly
   resistive wall, $\gamma\tau_A=(\Delta_i+\Delta_x)^{4/5}S^{-3/5}$
   (Eq. 3); $\Delta_i=0$ with $\gamma\tau_A\hat S_{\mathrm{wall}}\gg1$,
   $\gamma\tau_A=\Delta_x^{4/9}S^{-1/3}\hat S_{\mathrm{wall}}^{-4/9}$
   (Eq. 4); and, for $\Delta_i<0<\Delta_i+\Delta_x$ with the layer term
   neglected, an RWM-like branch with a rational surface,
   $\gamma\tau_A=-(1+\Delta_x/\Delta_i)\hat S_{\mathrm{wall}}^{-1}$
   (Eq. 5). No instability if $\Delta_i+\Delta_x<0$. Derived (cylindrical
   theory attributed to refs. 1, 11). Compiler's check: Eqs. 3–5 follow
   algebraically from Eq. 2.
5. **Two-fluid and rotation effects small** (§II). Generalized-Ohm's-law
   effects "are expected to be small, particularly in the limit (5) which
   does not contain the resistivity"; residual rotation after locking "is
   not enough to stabilize the mode". Stated.
6. **Linear M3D-C1** (§II, Fig. 2). The reconstruction is unstable with a
   resistive wall and stable with an ideal wall; the mode is (2,1) and
   penetrates the wall; $\gamma\tau_A$ against $S_{\mathrm{wall}}$ is
   fitted by Eq. 2 with $\Delta_x=1$, $\Delta_i=-1/5$ and asymptotes to
   $S_{\mathrm{wall}}^{-2/3}$, between scalings (4) and (5). Shown for the
   resistive-wall scan; ideal-wall stability Stated (not plotted).
7. **Nonlinear M3D: complete TQ** (§III, Figs. 3–4). The RWTM grows to
   large amplitude and causes a complete TQ through parallel heat
   transport; the perturbed flux is predominantly (2,1). Shown.
8. **TQ-time scaling** (§III, Fig. 4b). $\tau_{\mathrm{TQ}}$ is fitted by
   $3.4/\gamma$ ($\gamma$ measured from the wall-field histories) and by
   $S_{\mathrm{wall}}^{2/3}$; at the experimental $S_{\mathrm{wall}}$,
   $\tau_{\mathrm{TQ}}/\tau_A\approx S_{\mathrm{wall}}/2$, "as in the
   experimental data". Shown.
9. **Parallel transport time** (§III, Eq. 6, Figs. 4b, 5). The time
   $a^2/(\chi_\parallel b_n^2)$, with $b_n$ the normal perturbed field at
   the wall normalized to $B$, tracks $\tau_{\mathrm{TQ}}$; its
   $S_{\mathrm{wall}}^{2/3}$ scaling implies $b_n\propto
   S_{\mathrm{wall}}^{-1/3}$, matching Fig. 5. Shown (fit).
10. **Precursor drop** (§III, Fig. 4a). The small drop of the volume
    pressure at $t\approx3000\tau_A$ comes from internal modes and
    resembles minor precursor disruptions in JET and DIII-D. Stated
    (interpretation).
11. **Why the amplitude gets large** (§III). The external parameter
    $\Delta_x$ depends only on the radius ratio, "independent of island
    size. It is not saturated by local flattening of the current profile",
    unlike $\Delta_i$. Stated (hedged in the text: "may be").
12. **Amplitude matches experiment** (§III, Fig. 5). Measured (2,1)
    $\delta B\approx480$ G at the rational surface ($\delta B/B=2.8\times
    10^{-2}$, $B=1.7$ T), mapped to the wall by $x_s^3=0.3$, gives
    $8.4\times10^{-3}$; the simulated peak transverse wall field is
    $8.8\times10^{-3}$ at $S_{\mathrm{wall}}=1.2\times10^4$, from the fits
    $b_n\approx0.05S_{\mathrm{wall}}^{-1/3}$ and
    $b_l=b_n+6.7\times10^{-3}$. Shown.
13. **Onset condition** (§IV, Eqs. 7–8). The RWTM threshold is
    $\Delta_i=0$; a step-current model gives instability for
    $x_s^4>(4/q_0^2)(q_0-1)$, i.e. $x_s>0.65$ for $q_0=1.05$. Derived.
    Compiler's check: $(4/1.05^2)\times0.05=0.181$, fourth root 0.653.
14. **Database consistency** (§IV). The DIII-D locked-mode database
    boundary $r_{q=2}/a>0.75$ (Sweeney et al. 2017) corresponds to
    $x_s>0.625$ for $r_w/a\approx1.2$; the simulation has $r_{q=2}/a=0.8$,
    $x_s=0.67$; $r_{q=2}/a$ grows during the locked phase. Stated
    (database attributed).
15. **ITER extrapolation** (Abstract, §V). With $\tau_w=250$ ms (50× JET
    and DIII-D) the TQ could last 75–125 ms; with the
    $\hat S_{\mathrm{wall}}^{4/9}$ scaling and a 500 eV edge, 70 ms (from
    ref. 2). "ITER disruptions may be significantly more benign than
    previously predicted", which could relax mitigation, prediction and
    runaway-electron requirements. Stated (extrapolation). For contrast,
    [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) quote unmitigated ITER
    VDE thermal quenches of order 20 ms, a different scenario; the paper
    does not cite it.

# Models and numerics

* **Codes.** Linear study with M3D-C1 with a resistive wall (refs. 15–16);
  nonlinear study with M3D (ref. 17) with a thin resistive wall (ref. 18).
  **The paper writes no MHD equations for either code**; only parameters
  are given.
* **Analytic model** (§II), cylindrical, thin wall at $r_w$, perturbation
  $\delta\psi\propto\exp(\gamma t+im\theta+in\phi)$. Thin-wall condition,
  with the vacuum solution $\delta\psi_{\mathrm{vac}}\propto r^{-m}$
  matched at the wall:
  $$\gamma\,\delta\psi=\frac{\eta_w}{\mu_0d_w}\left(\partial_r\delta\psi_{\mathrm{vac}}-\partial_r\delta\psi\right),\qquad \partial_r\delta\psi_{\mathrm{vac}}=-\frac{m}{r_w}\delta\psi,$$
  equivalently (Eq. 1)
  $$\left(1+\frac{\gamma\tau_w}{m}\right)\delta\psi=-\frac{r_w}{m}\partial_r\delta\psi,\qquad \tau_w=\frac{\mu_0r_wd_w}{\eta_w}.$$
* **Dispersion relation** (Eq. 2):
  $$(\gamma\tau_A)^{5/4}S^{3/4}=\Delta_i+\frac{\Delta_x}{\gamma\tau_A\hat S_{\mathrm{wall}}+1},$$
  with $\tau_A=R_0/v_A$, $S_{\mathrm{wall}}=\tau_w/\tau_A$,
  $\hat S_{\mathrm{wall}}=S_{\mathrm{wall}}(1-x_s^{2m})/(2m)$,
  $x_s=r_s/r_w$ ($r_s$ the rational-surface radius),
  $\Delta_i=r_s\Delta'_{\mathrm{ideal}}/m$ ($\Delta'$ with an ideal wall at
  $r_w$) and $\Delta_x=2x_s^{2m}/(1-x_s^{2m})$.
* **Parallel transport time** (Eq. 6): $a^2/(\chi_\parallel b_n^2)$.
* **Step-current model** (§IV, Eq. 7; refs. 11, 19), constant current
  inside $r_0$, $r_s/r_0=(2/q_0)^{1/2}$, $(m,n)=(2,1)$:
  $$\Delta_i=-2\,\frac{q_0-1-(q_0^2/4)x_s^4}{\left(q_0-1-q_0^2/4\right)(1-x_s^4)},$$
  so that $\Delta_i\le0$ for $x_s^4>(4/q_0^2)(q_0-1)$ (Eq. 8).
* **Linear runs (M3D-C1).** Reconstruction of DIII-D 154576 at 3312 ms,
  axisymmetric, no islands, $q_0>1$ imposed to suppress the (1,1) mode;
  scan $S_{\mathrm{wall}}\approx50$ to $5\times10^4$. Mesh, resolution and
  time step not given.
* **Nonlinear runs (M3D).** As in refs. 1–2: $S=10^6$;
  $\chi_\parallel=10R_0^2/\tau_A$; $\chi_\perp=\nu=10^{-4}a^2/\tau_A$; 16
  poloidal planes ("adequate to resolve low toroidal mode numbers"); small
  arbitrary initial perturbations in all $n$;
  $S_{\mathrm{wall}}=10^3,\ 3.3\times10^3,\ 10^4,\ 3.3\times10^4$. Spatial
  discretization, time integration, solvers, parallelism and costs not
  given. See [resistive-wall coupling](/methods/resistive-wall-coupling.md)
  for how the bundle's codes treat walls.

# Tests and results

* **Fig. 1** (experiment, from Sweeney 2018): $I_p\approx1.3$ MA (read);
  core $T_e$ collapse at 27.5–30 ms, current spike, then current quench;
  $n=1$-dominated probe signals with harmonics (2,1), (3,1), (3,2), (1,1).
* **Fig. 2a** (M3D-C1): $\gamma\tau_A$ from about $6\times10^{-3}$ at
  $S_{\mathrm{wall}}\approx50$ to about $6\times10^{-4}$ at
  $S_{\mathrm{wall}}\approx4\times10^4$ (read); Eq. 2 fit with
  $\Delta_x=1$, $\Delta_i=-1/5$. **Fig. 2b**: perturbed flux, (2,1),
  penetrating the wall.
* **Fig. 3** (M3D, $S_{\mathrm{wall}}=10^4$, $t=5690\tau_A$): total
  pressure at about 20% of its initial value; perturbed flux mainly (2,1).
* **Fig. 4**: TQ completes at about 3000, 3500, 6000 and $10500\tau_A$ for
  the four $S_{\mathrm{wall}}$ values (read); the curves of
  $\tau_{\mathrm{TQ}}$, the parallel transport time, $3.4/\gamma$ and
  $S_{\mathrm{wall}}^{2/3}$ agree.
* **Fig. 5**: peak $b_l$ about $10.2\to8.2\times10^{-3}$ and peak $b_n$
  about $4.5\to1.4\times10^{-3}$ across the scan; simulated $8.8\times
  10^{-3}$ against measured $8.4\times10^{-3}$.
* **Onset numbers**: $q_0=1.05\Rightarrow x_s>0.65$; database
  $r_{q=2}/a>0.75\Leftrightarrow x_s>0.625$; simulation $x_s=0.67$.
* **ITER**: $\tau_w=250$ ms, $\tau_{\mathrm{TQ}}=75$–125 ms (or 70 ms).
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§6.3) use $\tau_w=0.5$
  s for ITER; neither paper says which wall time (mode $n$, vessel layer)
  it means, so the two numbers are recorded, not reconciled.

# Notation map

| Strauss et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$, $\psi'$, $\psi_{\mathrm{vac}}$ | $\delta\psi$, $\partial_r\delta\psi$, $\delta\psi_{\mathrm{vac}}$ | perturbation in a cylinder; per-radian vs full flux not stated (irrelevant for a homogeneous condition) |
| $\gamma$, $\hat\gamma$, $\gamma_s$ | $\gamma$, $\gamma\tau_A$, $\gamma$ (measured) | |
| $\theta$, $\phi$, $m$, $n$ | same | orientation not stated |
| $\eta_w$, $\delta_w$ | $\eta_w$, $d_w$ | |
| $\tau_{wall}$ | $\tau_w$ | $\mu_0r_wd_w/\eta_w$ |
| $\tau_A=R/v_A$, $R$ | $\tau_A$ with length $R_0$, $R_0$ | |
| $S$ | $S$ | |
| $S_{wall}$, $S_w$ | $S_{\mathrm{wall}}$ (§10), $\hat S_{\mathrm{wall}}$ (page-local) | **collision risk:** native $S_w$ is the reduced quantity, not $\tau_w/\tau_A$ |
| $\Delta_i$, $\Delta'_{ideal}$, $\Delta_x$, $x_s$ | page-local $\Delta_i$, $\Delta'$ (ideal wall), $\Delta_x$, $x_s$; $r_s$ (§10) | not registered (except $\Delta'$, $r_s$) |
| $r_w$, $r_s$, $r_0$, $a$ | $r$ with subscripts, $a$ | |
| $\chi_\parallel$, $\chi_\perp$ | $\chi_\parallel$, $\chi_\perp$ | called "conductivity" but in diffusivity units |
| $\mu$ | $\nu$ | **collision:** registry $\mu$ is the magnetic moment |
| $P$ | words (volume-integrated pressure) | **collision:** not the registry $p$ |
| $b_n$, $b_l$, $b_w$ | words (normal and transverse wall field over $B$; measured value mapped to the wall) | page-local |
| $\tau_\parallel$, $\tau_{TQ}$ | words (parallel transport time), $\tau_{\mathrm{TQ}}$ (§10) | $\tau_{\mathrm{TQ}}$ here is the time to a complete TQ in the M3D runs |
| $\rho_{q2}$ | $r_{q=2}/a$ | **collision:** registry $\rho$ is the mass density |
| $q_0$, $T_e$, $I_p$, $B$ | same | |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [M3D](/software/m3d.md)
* [M3D-C1](/software/m3d-c1.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md)
* [Sawtooth crash and Kadomtsev reconnection](/definitions/sawtooth-crash.md)
* [Thermal quench](/definitions/thermal-quench.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/0000_manual_no_journal_Unknown_10106350107048titleResistive.pdf`.
   * **Version.** Publisher version of record (AIP, "Published under an
     exclusive license by AIP Publishing"), with an AIP download cover
     (stamped 16 October 2026); 6 PDF pages = cover + article pages
     112508-1 to -5. The archive filename carries no metadata; identity
     from page 1.
   * **Identity.** doi:10.1063/5.0107048, checked on Crossref: Strauss
     H.R., Lyons B.C., Knolker M., Phys. Plasmas 29(11), article 112508,
     issue November 2022 (submitted 1 July, accepted 26 October, online 15
     November 2022), 19 references.
   * **How read.** Full text; the sign of $\Delta_i=-1/5$ (Fig. 2 caption
     and §II) was read from the rendered page because text extraction
     drops the minus sign. Plot values are the reader's approximate
     readings.
   * **Recorded as printed.**
     * Eq. 3 carries a redundant bracket, $[(\Delta_i+\Delta_x)]^{4/5}$.
     * §IV after Eq. 7 equates $\Delta_i\le0$ with RWTM instability ("If
       this is not satisfied, the RWTM is unstable"); §II also requires
       $\Delta_i+\Delta_x>0$, which §IV does not restate. The sign logic
       of the sentence on Eq. 7 is otherwise correct (compiler's check:
       the denominator equals $-(q_0/2-1)^2(1-x_s^4)\le0$).
     * §V: the 75–125 ms range is attributed to "$\tau_{TQ}\approx
       \tau_{wall}/2$ scaling", but 125 ms is $0.5\tau_w$ and 75 ms is
       $0.3\tau_w$ (the JET ratio); the range uses both ratios.
     * Fig. 4b legend writes "S_w 2/3" where caption and text use
       $S_{wall}^{2/3}$; $S_w$ and $S_{wall}$ differ by
       $(1-x_s^{2m})/(2m)$ in §II.
     * $\chi_\parallel$, $\chi_\perp$ are called thermal "conductivity" but
       are given in diffusivity units ($R^2/\tau_A$, $a^2/\tau_A$).
     * The Fig. 1 time axis is offset: the equilibrium "at time 3312 ms
       (27.2 ms in Fig. 1)".
     * Consistency checks that pass (compiler's): 480 G / 1.7 T =
       $2.8\times10^{-2}$; $0.67^3=0.30$; 250 ms is 50 × 5 ms.
     * No model equations of M3D or M3D-C1 and no resolution beyond "16
       poloidal planes" are given.
   * **Reference list.** 19 printed entries, merged into the bibliography
     under `strauss-2022`. Refs. 1 and 2 are two different 2021 Strauss
     papers (JET; ITER), keyed `strauss-2021` and `strauss-2021-b` in
     order of appearance; de Vries et al. (printed 2016) reuses the
     existing `devries-2015`; Gerasimov et al. is `gerasimov-2020` (a
     different work from the IAEA TM 2020 talk that hu-2021 cites,
     `gerasimov-2020-b`). Printed defects: ref. 11 first author "J. A.
     Finn" (J. M. Finn, Phys. Plasmas 2, 198 (1995)); ref. 15 "F. Zang"
     (F. Zhang) and "tokakmak"; ref. 4 stray "Piron1"; ref. 10 title
     garbled with "EFDA JET contributors" inside the quotes; refs. 16 and
     18 printed without titles.
