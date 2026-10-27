---
type: Method
title: "Continuous eddy simulation"
description: "Heinz's hybrid RANS/LES whose length-scale-equation destruction coefficient varies with the ratio of modelled to total length scale, so that modelled and resolved motion stay balanced under grid and Reynolds-number changes; its derivation, its contrast with PITM, and its SST implementation in a lattice Boltzmann solver."
status: established
aliases: [CES, CES-KOS, continuous eddy simulation mode control, CES-SST]
tags: [hybrid-rans-les, rans, les, eddy-viscosity, lattice-boltzmann]
timestamp: 2026-10-26T20:48:00Z
---

# Continuous eddy simulation

Continuous eddy simulation (CES) is a [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
method of Heinz and co-workers in which a single RANS transport model runs
everywhere and the coefficient of one destruction term depends on how much
of the turbulence is resolved. In its $k$-$\varepsilon$ form that coefficient
is a function of $L_+$, the ratio of the modelled to the total (modelled plus
resolved) length scale: $L_+=1$ returns the RANS model, and the modelled
contribution grows on coarser grids and at higher Reynolds numbers only through
the modified dissipation
([Heinz (2022)](/sources/heinz-2022.md), §2, Table 2). Heinz calls the
design problem the "communication" between modelled and resolved motion: the
modelled viscosity must be small enough not to extinguish resolved motion on
coarse grids, yet increase its contribution for coarser grids and higher
$Re$, and most hybrid methods do not address it (§1). Mozaffari et al. (2024)
implement CES in an [SST](/methods/k-omega-sst-model.md) host and call the
construction "theory-based"
([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §2.3, Eqs. 33–34;
HAL accepted manuscript).

**Page-local symbols.** The subscript $+$ on this page marks a ratio of a
modelled to a total quantity, never wall units: $k_+$, $\varepsilon_+$,
$L_+$ and $\tau_+$ are the ratios of kinetic energy, dissipation, length
scale $k^{3/2}/\varepsilon$ and time scale $k/\varepsilon$ (Heinz's
"resolution ratios"). $\alpha^*_\varepsilon$ is the variable destruction
coefficient of the $\varepsilon$ equation and
$\alpha_\varepsilon=C_{\varepsilon2}/C_{\varepsilon1}$ its RANS value
(Heinz's $\alpha^*$, $\alpha$, renamed because $\alpha^*$ is a constant of
the [Wilcox $k$-$\omega$ model](/methods/k-omega-model.md)). $k_+$ is not
the registry-§11 $\beta_k$ of the [active model split](/methods/active-model-split.md):
its total energy is the time-averaged modelled plus resolved energy, not a
RANS $k$.

## The $k$-$\varepsilon$ form and its variational derivation

Heinz (2022, Eqs. 1–2) writes the filtered incompressible momentum equation
with a [$k$-$\varepsilon$](/methods/k-epsilon-model.md) eddy viscosity
$\nu_t=C_\mu k^2/\varepsilon$ acting on the filtered strain $\bar S_{ij}$, and

$$\begin{aligned}
\frac{\bar Dk}{\bar Dt}&=P_k-\varepsilon+D_k,\\
\frac{\bar D\varepsilon}{\bar Dt}&=C_{\varepsilon1}\frac{\varepsilon^2}{k}\Big(\frac{P_k}{\varepsilon}-\alpha^*_\varepsilon\Big)+D_\varepsilon,
\end{aligned}$$

with $\bar D/\bar Dt$ the material derivative along the filtered velocity,
$P_k=\nu_t|\bar S|^2$, $D_k=\partial_j(\nu_t\partial_jk)$,
$D_\varepsilon=\partial_j[(\nu_t/\sigma_\varepsilon)\partial_j\varepsilon]$,
$C_{\varepsilon1}=1.44$, $\sigma_\varepsilon=1.3$, and in RANS
$\alpha^*_\varepsilon=\alpha_\varepsilon=1.92/1.44=1.33$ (§2). The variable
coefficient thus multiplies the destruction term $C_{\varepsilon1}\alpha^*_\varepsilon\varepsilon^2/k$.

Eliminating $P_k$ with the $k$ equation and taking the variation $\delta$ of the
$\varepsilon$ equation gives an exact relation for $\delta\alpha^*_\varepsilon$
(Eqs. 3–4). Following Friess et al. and the earlier CES papers, as recalled by
Heinz (2022), the relative variations $\delta k/k$ and
$\delta\varepsilon/\varepsilon$ are assumed uniform in space and in time; Heinz
states that Chaouat & Schiestel (2021, App. E) make the same assumption
"although different language is used" (§2). The relation then reduces to

$$\delta\alpha^*_\varepsilon=(\alpha^*_\varepsilon-1)\Big[\frac{\delta k}{k}-\frac{\delta\varepsilon}{\varepsilon}\Big]-\frac{D_*}{\varepsilon}\Big[2\frac{\delta k}{k}-\frac{\delta\varepsilon}{\varepsilon}\Big],\qquad D_*=D_k-\frac{kD_\varepsilon}{C_{\varepsilon1}\varepsilon}$$

(Eq. 7; $D_*$ page-local). Three hybridization options follow, each with the
transport terms written with a viscosity $\nu_t^\star$ (Table 2; page-local
$\nu_t^\star$):

| Option | $\nu_t^\star$ in $D_k$, $D_\varepsilon$ | coefficient | assumption |
|---|---|---|---|
| O1 (CES) | $\nu_t$ | $\alpha^*_\varepsilon=1+L_+^2(\alpha_\varepsilon-1)$ | $\bar Dk/\bar Dt$, $\bar D\varepsilon/\bar Dt$ do not affect $\alpha^*_\varepsilon$ |
| O2 | $\nu_t$ | $\alpha^*_\varepsilon=1+\tau_+(\alpha_\varepsilon-1)$ | $D_k$, $D_\varepsilon$ do not affect $\alpha^*_\varepsilon$ ($D_*$ dropped) |
| O3 | total viscosity | $\alpha^*_\varepsilon=1+\tau_+(\alpha_\varepsilon-1)$ | none further |

O1 is the CES mode control (Heinz 2019, as recalled); its integration constant
is fixed by $\alpha^*_\varepsilon=\alpha_\varepsilon$ at $L_+=1$, the RANS
limit (§2). In CES the ratios are built from time averages: the modelled length
$\langle k\rangle^{3/2}/\langle\varepsilon\rangle$ against the total
$k_{\mathrm{tot}}^{3/2}/\varepsilon_{\mathrm{tot}}$, where $k_{\mathrm{tot}}=\langle k\rangle+k_{\mathrm{res}}$
with $k_{\mathrm{res}}$ half the trace of the resolved velocity covariance, and
$\varepsilon_{\mathrm{tot}}=\langle\varepsilon\rangle+\varepsilon_{\mathrm{res}}$
with $\varepsilon_{\mathrm{res}}$ the molecular dissipation of the resolved
velocity-gradient fluctuations (§2).

O3 replaces the modelled viscosity in the turbulent transport terms by the
total viscosity, on the argument that "turbulent transport of modeled
variables is managed by all the turbulence"; it reaches the O2 coefficient
without further assumption, but needs gradients of resolved quantities and
lets resolved motion act on turbulent transport, so its computational
suitability "needs evidence that is currently missing"; it has never been
applied (§2, §4).

## Consistency argument against the PITM coefficient

Heinz (2022) uses the options to criticize the energy-partition control of the
partially integrated transport model (PITM) of Schiestel, Dejoan and Chaouat,
as recalled from Chaouat & Schiestel (2021):

- O2 with ordinary turbulent transport ($\nu_t^\star=\nu_t$) is consistent
  only for homogeneous flow. For non-homogeneous flow it adds a spurious
  source, the difference of the O3 and O2 transport terms, so O2 "can only be
  used as the homogeneous-flow version of O3" (§2, observation 2; the term is
  argued, not written out).
- Under the common assumption $\varepsilon_+=1$, $L_+^2=k_+^3$ and
  $\tau_+=k_+$, so O1 becomes $1+k_+^3(\alpha_\varepsilon-1)$ and O2 the
  PITM-type form $1+k_+(\alpha_\varepsilon-1)$. Chaouat & Schiestel recommend
  the latter with $\nu_t^\star=\nu_t$ for non-homogeneous flow, which the
  argument above rules out; $\varepsilon_+=1$ is also said to be
  inappropriate near walls (§3).
- Without $\varepsilon_+=1$, the Chaouat–Schiestel analysis implies
  $\alpha^*_\varepsilon=1+k_+\varepsilon_+^{-2}(\alpha_\varepsilon-1)$, and Heinz
  asks why resolution should be measured by $k_+\varepsilon_+^{-2}=\tau_+^4/L_+^2$ (§3).
- If CES and PITM are driven by $L_+^2=k_+^3$ and $\tau_+=k_+$ respectively,
  the relative difference $(k_+-k_+^3)/k_+^3$ is 2400%, 300% and 56% at
  $k_+=0.2$, 0.5 and 0.8 (§1). These figures compare two mode-control
  assumptions; they are not errors measured against data.

The evidence is a figure reproduced from Heinz et al. (2020): periodic-hill
runs at "$Re=37$K" (as printed, without its reference length and velocity) on grids of 120 000, 250 000 and 500 000 points with a
CES $k$-$\omega$ model ("CES-KOS") whose mode control is replaced by a
PITM-type grid prescription of the energy ratio, $R=C_\Delta(\Delta/L_{\mathrm{tot}})^{2/3}$
with $\Delta=(\Delta x\Delta y\Delta z)^{1/3}$ and $C_\Delta=1.06$ (page-local
$R$, $C_\Delta$, $L_{\mathrm{tot}}$). The prescribed $R$ does not control the
actual $k_+$ at $x/h=4$, and small changes in $R$ imply significant changes
in $k_+$ (§3, Fig. 1; see [periodic hill](/benchmarks/periodic-hill.md)).

Heinz concludes that CES with O1 is "a simple and stable way" to obtain
correct mode communication, and that it overcomes the PITM problems and
"similar problems" seen in [PANS](/methods/partially-averaged-navier-stokes.md)
(§4). Table 1 of the paper contrasts the two families: PITM rests on spectral
theory, uses $k$-$\varepsilon$ and related Reynolds-stress models with one
hybridization type and needs empirical closures; CES is derived by variational
analysis, exists for $k$-$\varepsilon$, $k$-$\omega$, Reynolds-stress and PDF
models with "three equivalent types" of hybridization, and needs "no empirical
closures". The conclusions are said to carry over to $k$-$\omega$,
[Reynolds-stress](/methods/reynolds-stress-model.md) and PDF forms (§4).

## SST implementation

Mozaffari et al. (2024, §2.3, Eqs. 33–34) apply the same idea to the
$k$-destruction of SST in the lattice Boltzmann solver
[ProLB](/software/prolb.md):

$$\beta^*\omega k\;\to\;\beta^*\omega k\,\psi_\beta,\qquad \psi_\beta=\beta_{\mathrm{CES}}+L_+^2(1-\beta_{\mathrm{CES}}),\qquad
L_+=\frac{\Delta_{C+}}{(1+\Delta_{C+}^3)^{1/3}},\quad \Delta_{C+}=C_+\frac{\Delta}{L_{\mathrm{tot}}},\quad L_{\mathrm{tot}}=\frac{\sqrt k}{C_\mu\omega},$$

with page-local $\psi_\beta$, $\beta_{\mathrm{CES}}$, $\Delta_{C+}$, $C_+$. Here $L_+$ is a
grid-based estimate of the length ratio, not the time-averaged ratio of
Heinz (2022). The source writes $\beta_{\mathrm{CES}}$ as $\beta$, the SST destruction
symbol, and prints neither its value nor $C_+$ nor the definition of
$\Delta$. For $\Delta_{C+}\to\infty$, $L_+\to1$ and $\psi_\beta\to1$, the
RANS dissipation; for $\Delta_{C+}\to0$, $\psi_\beta\to\beta_{\mathrm{CES}}$ *(compiler
check, not in the sources)*. Both forms interpolate a destruction
coefficient linearly in $L_+^2$, from the RANS value at $L_+=1$ to a limit
value at $L_+=0$; Heinz's O1 sets that limit to $C_{\varepsilon1}$ in the
$\varepsilon$ equation ($\alpha^*_\varepsilon=1$), Mozaffari et al. to
$\beta_{\mathrm{CES}}\beta^*$ in the $k$ equation *(compiler check, not in the sources)*.

Results (Mozaffari et al. 2024):

- on a three-dimensional [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
  $10^\circ$ CES, IDDES and RANS give identical mean $C_p$, and the RANS–LES
  transition is "smooth and continuous" in CES, thin in IDDES (§3.2, Figs.
  10–11);
- at $45^\circ$, CES gives $C_L=1.192$, $C_D=0.993$ and IDDES 1.231, 1.038,
  against the reference 1.097 and 1.180 and RANS 2.238, 2.053; the hybrids
  perform "almost the same without any superiority" (Table 2);
- on the $35^\circ$ [Ahmed body](/benchmarks/ahmed-body.md), with the
  algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
  neither hybrid separates on the slant (CES drag 0.2738); with a
  zero-velocity wall condition CES separates already on the roof, the
  separation extends into the wake, and its drag is 0.3779, where IDDES
  matches the wake with 0.2819 (§3.3, Table 3, Figs. 17–20).

Heinz (2022, §2, observation 1) states that O1 "is known to be very successful" with
ordinary transport terms, by reference to the CES papers; the reproduced
periodic-hill figure tests a PITM-type prescription inside CES, not CES
itself.

## Qualifications

- Heinz's criticism addresses a simplified PITM: what the paper calls "the
  usual computational implementation of PITM methods" includes a relaxation
  mechanism that forces the energy ratio to its target, and the paper
  explicitly excludes it (§1). The periodic-hill
  evidence uses a CES $k$-$\omega$ model with a PITM-type energy prescription,
  not the PITM model of Chaouat & Schiestel.
- The claim that CES with O1 overcomes "similar problems" in PANS is made
  without a PANS computation in Heinz (2022, §4).
- The two sources leave the free constants of the SST form unspecified
  (Mozaffari et al.) or recall them from earlier papers (Heinz), so the
  method cannot be reproduced from these pages alone.

# Citations

- [Heinz (2022)](/sources/heinz-2022.md) — §1, §2 Eqs. 1–7 Table 2, §3 Fig. 1, §4 Table 1.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.3 Eqs. 33–34, §3.2 Figs. 10–11 Table 2, §3.3 Figs. 17–20 Table 3 (HAL accepted manuscript).
