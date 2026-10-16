---
type: Definition
title: "Resistive tearing mode"
description: "Current-driven resistive instability that reconnects the magnetic field at a rational surface q = m/n and forms magnetic islands; its linear growth rate follows gamma ~ eta^(3/5) at low resistivity, the standard verification target of nonlinear MHD codes in tokamak and stellarator geometry."
status: established
aliases: [tearing mode, 2/1 tearing mode, resistive tearing, FKR scaling]
tags: [tearing, mhd, verification, tokamak, stellarator, wall]
timestamp: 2026-10-16T00:00:00Z
---

# Resistive tearing mode

A tearing mode is a resistive MHD instability of helicity $m/n$ that is
resonant at the rational surface $q=m/n$. Finite resistivity $\eta$ breaks the
frozen-in condition in a thin layer around that surface, the field reconnects
there and the flux surfaces break into a chain of $m$ magnetic islands. Linear
theory (Furth, Killeen and Rosenbluth, "FKR") gives the growth rate in the
constant-$\psi$ regime as

$$\gamma\propto\eta^{3/5},\qquad\text{equivalently}\qquad \gamma\tau_A\propto S^{-3/5},$$

with $S$ the Lundquist number. The scaling is quoted as the reference of every
tearing benchmark of this bundle
([Zhang et al. (2021)](/sources/zhang-2021.md), §1, §3.1, refs. [9,32];
[Ma & Guo (2022)](/sources/ma-2022.md), §4.2, ref. [27];
[Jiang et al. (2024)](/sources/jiang-2024.md), §IX C, which names the
constant-$\psi$ FKR scaling without citing it). The drive is the equilibrium
current gradient, measured by the stability index $\Delta'$; none of the
chunk-1 sources computes $\Delta'$ explicitly, so it enters here only as the
standard parameter of the theory.

The mode has a characteristic parity: the perturbed flux is even across the
resonant surface while its radial derivative jumps, and the perturbed pressure
is odd. [Seto et al. (2023)](/sources/seto-2023.md) (§5.3, Figs. 9–10) use
exactly this signature, a jump in the radial gradient of the parallel vector
potential $\mathbf A\cdot\mathbf b$ and an odd pressure perturbation about
$q=2$, to identify a "tearing-like" global $(m,n)=(2,1)$ structure inside a
nonlinear pedestal collapse; whether islands form there is left open.

## The m/n = 2/1 verification case

The $2/1$ mode in a circular, large-aspect-ratio, near-zero-$\beta$ plasma is
the most common verification problem in the corpus, because the result can be
checked against the analytic scaling.

| Source | Code(s) | Geometry | $\eta$ range | Fitted exponent |
|---|---|---|---|---|
| Zhang et al. (2021), Table 1, Fig. 4 | CLT vs M3D-C1 | $R_0/a=10$, $\beta\approx0$ | $10^{-7}$–$10^{-5}$ (inverse Lundquist number, $a=1$ m) | 0.601 (CLT), 0.58 (M3D-C1), as printed |
| Ma & Guo (2022), §4.2, Fig. 11 | SCELT (eigenvalue) | $R_0/a=5$, $p\propto(1-r^2)$, peak $p=5\times10^{-5}$ normalized | $\log_{10}\eta\in[-9,-6.2]$ (normalized) | 0.5590 |
| Jiang et al. (2024), §IX C, Fig. 28 | GMEC_I vs MAS | $R_0=10$ m, $a=1$ m, DESC equilibrium, no pressure | $10^{-7}$–$10^{-4}$ Ω m | follows $3/5$ for $\eta<10^{-6}$ Ω m |

All three use the same family of safety-factor profiles,
$q(\psi_N)=q_0\sqrt{1+\psi_N^2\,[(q(1)/q_0)^2-1]}$ with $q_0=1.75$ and
$q(1)=2.5$, which puts the single $q=2$ surface at $\psi_N\approx0.54$, i.e.
$r/a\approx0.74$ (Zhang et al. 2021, Eq. 1.7, Fig. 2; Ma & Guo 2022, §4,
Fig. 7; Jiang et al. 2024, Eq. 60, Fig. 24). The full benchmark of Zhang et
al. is on [CLT–M3D-C1 tearing and resistive-kink benchmark](/benchmarks/clt-m3d-c1-benchmark.md).

Other tearing verifications in the chunk:

- **JOREK, toroidal reduced vs cylindrical full MHD.** The nonlinear $2/1$
  mode at $R_0/a=10$, zero $\beta$, $S=10^6$ and negligible viscosity agrees
  with SpeCyl within about 5%, the residual attributed to toroidal vs
  cylindrical geometry; the visco-resistive layer width matches theory and
  the Phoenix code; linear $\eta$ scans of [JOREK](/software/jorek.md)
  reduced and full MHD are compared with CASTOR3D
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4, Figs. 18, 20).
  The same paper uses a full-MHD tearing mode for its finite-element
  convergence test: the growth-rate error falls as the fifth power of the
  linear grid resolution (§4.1, Fig. 13; see
  [Bézier finite elements](/methods/bezier-finite-elements.md)).
- **Stellarator.** In Wendelstein 7-A, [JOREK3D](/software/jorek3d.md)
  reproduces CASTOR3D's $(2,1)$ tearing growth rates to within 13.2% in a
  $\beta$ scan at $\eta=1.938\times10^{-6}$ Ω m and to within 26.2% in an
  $\eta$ scan from $1.938\times10^{-7}$ to $1.938\times10^{-5}$ Ω m, JOREK3D
  always higher ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI,
  Fig. 8). The authors attribute the larger gap, which sits at the highest
  $\eta$, to the neglect of $v_\parallel$ in their
  [stellarator reduced MHD](/methods/stellarator-reduced-mhd.md): $v_\parallel$
  is large in the resistive layer and the layer widens with $\eta$
  (attribution *stated*, not tested).
- **Resistive wall.** For a circular $2/1$ mode ($R_0=10$ m, $a=1$ m, wall
  at 1.1 m) the $n=1$ growth rate rises from about 630 s$^{-1}$ with an ideal
  wall to about 960 s$^{-1}$ with no wall as the wall resistivity is scanned
  over eight decades; JOREK–CARIDDI and JOREK–STARWALL agree to better than
  1% ([Isernia et al. (2023)](/sources/isernia-2023.md), §V, Fig. 7). Ports in
  an AUG-like wall raise the $n=1$ growth rate monotonically, from 509.5 to
  573.0 rad/s for 0 to 8 holes, because each hole obstructs the stabilizing
  eddy currents (§VI, Table I). See
  [resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Nonlinear evolution

- **Saturation and harmonics.** In the CLT–M3D-C1 runs at $\eta=10^{-5}$
  the $n=1$ growth rate is constant through the linear phase, decreases
  slowly in the nonlinear phase and vanishes at saturation; $n=0$ and $n=2$
  grow as beat modes at twice the $n=1$ rate; the saturated $n=1$ kinetic
  energies are $1.5\times10^{-6}$ and $1.4\times10^{-6}$ in normalized units
  (Zhang et al. 2021, §3.1, Figs. 6–8).
- **Mode families in a stellarator.** In W7-A (fivefold periodicity) $n=1$
  couples linearly through the geometry to $n=4,6,9$; at about 2 ms it drives
  $n=2$ nonlinearly, which drives $n=3,7,8$; the mode saturates at
  3–3.5 ms and excites a secondary $(3,2)$ island chain (Nikulsin et al. 2022,
  §VI, Figs. 9–10).
- **Double tearing.** For a double tearing mode with main harmonic
  $(m,n)=(4,1)$, lowering the normalized resistivity from $10^{-5}$ to
  $10^{-6}$ makes the secondary modes grow faster and the field stochastic
  earlier at the same main-mode amplitude
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5, Fig. 12).
  Double tearing at two $q=4$ surfaces is the $n=1$ mode that terminates a
  runaway beam benignly in JET (Hoelzl et al. 2021, §6; see
  [runaway electrons](/definitions/runaway-electrons.md)).

## Tearing modes in tokamak operation and disruptions

Hoelzl et al. (2021, §6) review JOREK applications in which tearing
modes are the central actor: locking of a $2/1$ mode to the AUG wall
(§6.1.1); island growth driven by
impurity radiation near the Greenwald density limit; RMP seeding of tearing
modes with hysteresis (penetration above about 2 kA of coil current,
expulsion below 1.5 kA) and their stabilization by ECCD; and the MGI-triggered
[thermal quench](/definitions/thermal-quench.md) of JET, which proceeds by a
current-profile avalanche $2/1\to3/2\to4/3$ (§6.2.1). Hoelzl et al. (2024, §2.2) add
RMP-driven island penetration at the pedestal top in ELM-suppressed AUG
plasmas and the stepwise growth of $5/1$ and $6/1$ islands that explains the
density pump-out in KSTAR (Fig. 3; see
[edge-localized modes](/definitions/edge-localized-mode.md)), and (§4.4) flux
pumping by a $1/1$ quasi-interchange mode that keeps $q_0\ge1$, prevents
sawteeth and thereby removes a seed of neoclassical tearing modes.

## Qualifications

**Fitted tearing exponents.** The exponents attributed to "$3/5$" spread
from 0.51 to 0.65 depending on code and fit range, and none of the sources
states its fit range.

- Zhang et al. (2021, Fig. 4) print $\eta^{0.601}$ (CLT) and $\eta^{0.58}$
  (M3D-C1).
- *Compiler's check, not a source claim:* a least-squares log–log fit of
  all five points of their Table 1 gives 0.54 (CLT) and 0.51 (M3D-C1). Fits
  restricted to the low-$\eta$ points come closer to the printed values: the
  three lowest points ($\eta\le10^{-6}$) give 0.65 and 0.58, and the four
  lowest give 0.60 and 0.56. The local exponent therefore steepens as $\eta$
  decreases, and the asymptotic $3/5$ is reached only at the low-$\eta$ end
  of the scan.
- Ma & Guo (2022) obtain 0.5590 over an $\eta$ range that extends two decades
  lower, at $R_0/a=5$.
- Jiang et al. (2024) find the $3/5$ slope only below $10^{-6}$ Ω m and a
  bend below the scaling at higher $\eta$, in both GMEC_I and MAS.

These results are consistent with one another and with FKR theory, which is
asymptotic in $S\to\infty$. They do not support quoting an exponent fitted
over a whole scan as a verification of $3/5$ without stating the range.
Normalizations also differ: Zhang et al. use an inverse Lundquist number
built on $a=1$ m, Ma & Guo a normalized $\eta$ built on $a$, and Jiang et
al. SI. The $\eta$ ranges are therefore not directly comparable across
rows of the table.

**Code-to-code spreads.**

- CLT and M3D-C1 differ by 7–11% for $\eta\ge3\times10^{-7}$ and by 24% at
  $\eta=10^{-7}$, while the paper says "about 10% for each case" (Zhang et
  al. 2021, Table 1).
- JOREK3D and CASTOR3D differ by up to 26.2% (Nikulsin et al. 2022, §VI).
- In Hoelzl et al. (2021, §4.4) the text describes the Fig. 18 case as "a
  low-β m=n=1 tearing-mode" while the caption calls it a $2/1$ tearing mode.

## Contradictions

None open. The sources disagree in the precision of their agreement with
theory, not in the theory.

# Citations

- [Zhang et al. (2021)](/sources/zhang-2021.md) — §1, §3.1, Table 1, Figs. 4–9.
- [Ma & Guo (2022)](/sources/ma-2022.md) — §4.2, Figs. 11–12.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §IX C, Figs. 24–28.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §VI, Figs. 8–10.
- [Isernia et al. (2023)](/sources/isernia-2023.md) — §V–VI, Fig. 7, Table I.
- [Seto et al. (2023)](/sources/seto-2023.md) — §5.3, Figs. 9–10.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §4.1, §4.4, §6.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.2, §3.5, §4.4.
