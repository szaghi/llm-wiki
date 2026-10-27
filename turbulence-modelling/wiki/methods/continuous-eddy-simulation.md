---
type: Method
title: "Continuous eddy simulation"
description: "Heinz's hybrid RANS/LES whose length-scale-equation destruction coefficient varies with the ratio of modelled to total length scale, so that modelled and resolved motion stay balanced under grid and Reynolds-number changes; its variational derivation, four model variants, its equivalence with DES and contrast with PANS and PITM, and its SST implementation in a lattice Boltzmann solver."
status: established
aliases: [CES, CES-KES, CES-KEK, CES-KOS, CES-KOK, continuous eddy simulation mode control, CES-SST]
tags: [hybrid-rans-les, rans, les, eddy-viscosity, lattice-boltzmann]
timestamp: 2026-10-27T15:55:00Z
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

**Symbols.** The subscript $+$ on this page marks a ratio of a
modelled to a total quantity, never wall units (registry §11): $k_+$, $\varepsilon_+$,
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
(Eqs. 3–4). Following Friess et al. and the earlier CES papers, which
Heinz (2022) cites, the relative variations $\delta k/k$ and
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

O1 is the CES mode control (Heinz 2019, cited there); its integration constant
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

## The 2020 derivation, four variants and the DES equivalence

The review of hybrid methods by [Heinz (2020)](/sources/heinz-2020.md),
§4, summarizes the author's earlier variational analysis (Heinz 2019, cited there)
in a different but convergent form. With the same $k$-$\varepsilon$ model
and variable $\alpha^*_\varepsilon$, the exact variation of the
$\varepsilon$ equation (Eq. 39) is closed by two assumptions: the variation
does not depend on the material derivatives of $k$ and $\varepsilon$
(the term $Q$ of Eq. 40 vanishes), and $\delta k/k$ and
$\delta\varepsilon/\varepsilon$ are spatially constant (after Friess et al.
and Manceau et al., whom the review cites). The variations of the transport terms are
then linearized, $\delta D_k/D_k=3\,\delta k/k-\delta\varepsilon/\varepsilon$
and $\delta D_\varepsilon/D_\varepsilon=2\,\delta k/k$ (Eq. 41), which,
unlike Friess et al., keeps the $\varepsilon$ variations; the
transport contribution cancels and
$$\delta\alpha^*_\varepsilon=(\alpha^*_\varepsilon-1)\Big(3\frac{\delta k}{k}-2\frac{\delta\varepsilon}{\varepsilon}\Big)=2(\alpha^*_\varepsilon-1)\frac{\delta L}{L},\qquad \alpha^*_\varepsilon=1+L_+^2(\alpha_\varepsilon-1)$$
(Eqs. 42–44), the O1 coefficient of the 2022 paper above, reached there
through a different intermediate relation (Eq. 7 of Heinz 2022). The
author calls $L_+^2$ the "mathematical identification" of the resolution
measure. The same measure follows for three further hybridizations
(§4.3, Eqs. 45–51), which name the four CES models:

| Model | Host | Where the resolution enters |
|---|---|---|
| CES-KES | $k$-$\varepsilon$ | $\varepsilon$ destruction, $\alpha^*_\varepsilon=1+L_+^2(\alpha_\varepsilon-1)$ |
| CES-KEK | $k$-$\varepsilon$ | $k$ destruction, $\bar Dk/\bar Dt=P_k-\psi_\alpha\varepsilon+D_k$ with $\psi_\alpha=1+\alpha_\varepsilon-\alpha^*_\varepsilon$ |
| CES-KOS | $k$-$\omega$ | $\omega$ destruction, $\alpha^*_\omega=1+L_+^2(\alpha_\omega-1)$ |
| CES-KOK | $k$-$\omega$ | $k$ destruction, $\psi_\beta=1+\alpha_\omega-\alpha^*_\omega$ |

Here $\alpha_\omega=C_{\omega2}/(C_\mu C_{\omega1})\approx1.63$ is the RANS
ratio of the $k$-$\omega$ model in Heinz's form (constants of Bredberg et
al., $C_{\omega1}=0.49$, $C_{\omega2}=0.072$, $C_\mu=0.09$; the source's
$\beta$, renamed because $\beta^*$ is an SST constant), $\alpha^*_\omega$
its variable form (the source's $\beta^*$) and $\psi_\alpha$ the
$k$-destruction multiplier of the $k$-$\varepsilon$ host (page-local);
$\psi_\beta$ is the registry's CES factor. In the $k$-$\omega$ derivation the
linearized transport variation is $\delta D_\omega/D_\omega=\delta k/k$ and
the remainder term vanishes (Eq. 48). From these forms the author
concludes that several RANS models "can generate resolved motions if
$L_+\le1$", while §4.1 concedes that an "exact mathematical proof" is
missing. With Eq. (44), the $k$-equation multiplier is
$\psi_\alpha=\alpha_\varepsilon+L_+^2(1-\alpha_\varepsilon)$, linear in
$L_+^2$ from the RANS value 1 at $L_+=1$ to $\alpha_\varepsilon$ at
$L_+=0$, the same form as the $\psi_\beta$ of Mozaffari et al. below with
$\beta_{\mathrm{CES}}$ in place of $\alpha_\varepsilon$ *(compiler check, not
in the sources)*.

**The length-scale law.** For the resolution itself the review takes,
after Chaouat & Schiestel (cited there),
$$L_+=\frac{\Delta_{C+}}{(1+\Delta_{C+}^p)^{1/p}},\qquad \Delta_{C+}=C_+\frac{\Delta}{L_{\mathrm{tot}}},\qquad C_+=\frac{(3C_K/2)^{3/2}}{\pi},$$
with $p=3$ in practice, $C_K$ the Kolmogorov constant and
$L_{\mathrm{tot}}=k_{\mathrm{tot}}^{3/2}/\varepsilon_{\mathrm{tot}}$
(§2.3, App. C, Eq. 58); the filter width $\Delta$ is not defined in cells.
For small $\Delta/L_{\mathrm{tot}}$ the modelled length is
$C_+\Delta$, and the author reads $C_K=1.3$, 1.43, 1.5 as giving
$C_+\approx0.9$, 1.0, 1.07, "hence $L=\Delta$ is very reasonable"; for
large $\Delta/L_{\mathrm{tot}}$, $L_+\to1$. The author supports the form
probabilistically: $L_+^2$, read as a cumulative distribution in
$\Delta_{C+}$, has a density proportional to a one-parameter beta
distribution, a maximum-entropy distribution under log-moment
constraints (from Heinz 2019). This is the formula Mozaffari et al. use
below, with $p=3$.

**Equivalence with DES.** Equating the CES-KEK dissipation with that of
[detached-eddy simulation](/methods/detached-eddy-simulation.md) in its
$k$-equation form, $\psi_{\mathrm{DES}}=\max\big(1,L_+/(C_{DES}\Delta/L_{\mathrm{tot}})\big)$,
gives (§4.4, Eqs. 53–54)
$$L_+=\min\left\{\frac{\sqrt{1+4\alpha_\varepsilon(\alpha_\varepsilon-1)C_{DES}^2(\Delta/L_{\mathrm{tot}})^2}-1}{2(\alpha_\varepsilon-1)C_{DES}\Delta/L_{\mathrm{tot}}},\;1\right\},$$
which solves $\alpha_\varepsilon-L_+^2(\alpha_\varepsilon-1)=L_+/(C_{DES}\Delta/L_{\mathrm{tot}})$
*(compiler check, not in the sources)* and tends to
$L_+\approx\alpha_\varepsilon C_{DES}\Delta/L_{\mathrm{tot}}$ on fine grids;
Eq. (55) is the $k$-$\omega$ analogue with $\alpha_\omega$. Matching this
limit to $L_+=C_+\Delta/L_{\mathrm{tot}}$ with $C_+=1$ gives
$C_{DES}=1/\alpha_\varepsilon=0.75$ and $1/\alpha_\omega=0.61$, which the
author calls close to 0.65 (Fig. 5). From this the review
concludes that CES "generalizes DES" and that "the technical solution to
adjust $\Delta_+$ to $L_+$ is absurd", DES being unstable under grid
variation (§4.4, citing the author's earlier work); the review shows no
computation for the second claim.

**Comparison with PANS.** With $\varepsilon_+=1$,
[PANS](/methods/partially-averaged-navier-stokes.md) uses
$\alpha^*_\varepsilon=1+L_+^{2/3}(\alpha_\varepsilon-1)$ against the CES
$1+L_+^2(\alpha_\varepsilon-1)$; since $L_+^{2/3}\ge L_+^2$, the author
concludes that PANS and PITM "require a much finer grid" for the same
resolution (§4.4, citing the cost analysis of Heinz 2019). Inserting the
PANS coefficient into Eq. (42) is consistent only with vanishing
transport, so the review confines PANS to homogeneous turbulence (Eq. 52),
the 2020 counterpart of the O2 observation below.
The review runs no simulations; its benchmark compilation (periodic hill,
NASA hump, Bachalo–Johnson bump, NACA 4412) is on
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and the benchmark pages.

## Consistency argument against the PITM coefficient

Heinz (2022) uses the options to criticize the energy-partition control of the
partially integrated transport model (PITM) of Schiestel, Dejoan and Chaouat,
which Heinz describes after Chaouat & Schiestel (2021):

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
  (Mozaffari et al.) or take them from earlier papers (Heinz), so the
  method cannot be reproduced from these pages alone.
- [Heinz (2020)](/sources/heinz-2020.md) prints $C_+=(0.876,1.0,1.074)$ for
  $C_K=(1.3,1.43,1.5)$ (§2.3 and App. C); the printed formula gives 0.867,
  1.000 and 1.074 *(compiler check, not in the sources)*. The Kolmogorov
  constant is printed both $C_K$ and $C_k$ in the same sentence. The
  derivation of Eqs. (42)–(44) rests on the two stated assumptions and on
  first-order linearizations of the transport variations; the
  review calls the result a "mathematical identification" of the resolution
  measure, and the claim that RANS models generate resolved motion for
  $L_+\le1$ follows from the equivalence of coefficient structures, not
  from a proof (§4.1, §4.3).

# Citations

- [Heinz (2022)](/sources/heinz-2022.md) — §1, §2 Eqs. 1–7 Table 2, §3 Fig. 1, §4 Table 1.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.3 Eqs. 33–34, §3.2 Figs. 10–11 Table 2, §3.3 Figs. 17–20 Table 3 (HAL accepted manuscript).
- [Heinz (2020)](/sources/heinz-2020.md) — §2.3, Eqs. (8)–(11), App. C, Eq. (58) (length-scale law, $C_+$); §4.1–4.2, Eqs. (38)–(44) (variational derivation); §4.3, Eqs. (45)–(51) (CES-KES, KEK, KOS, KOK); §4.4, Eqs. (52)–(55), Fig. 5 (PANS and DES equivalence, $C_{DES}$); §6.
