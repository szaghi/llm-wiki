---
type: Definition
title: "Morkovin's hypothesis and Reynolds analogies"
description: "Morkovin's hypothesis holds that, while density fluctuations stay small against the mean, compressible wall turbulence behaves like incompressible turbulence once mean property variations are scaled out; this page gives Morkovin scaling, the strong Reynolds analogy and its extensions, and how DNS up to Mach 11 confirm or break them."
status: established
aliases: [Morkovin hypothesis, Morkovin scaling, Morkovin's scaling, strong Reynolds analogy, SRA, HSRA, Reynolds analogy factor]
tags: [compressible, boundary-layer, dns, hypersonic, rans]
timestamp: 2026-10-25T19:47:00Z
---

# Morkovin's hypothesis and Reynolds analogies

**Morkovin's hypothesis** (Morkovin 1962, as recalled by
[Cogo et al. (2022)](/sources/cogo-2022.md), §1) states that, "when density
fluctuations are small compared with the mean value, the mean velocity and
Reynolds stress profiles in a compressible boundary layer can be mapped to
equivalent incompressible distributions … by taking into account the mean
density variation across the boundary layer". In Cogo et al.'s words this
assumption is "the cornerstone at the base of the 'Morkovin's hypothesis'",
from which consequences such as the van Driest velocity scaling derive, the
first of the [compressible velocity transformations](/definitions/compressible-velocity-transformation.md).
Its companion, also due to Morkovin, is the **strong Reynolds analogy
(SRA)**: the extension of the Reynolds analogy between momentum and heat
transport to the fluctuating fields, "a set of relations between the
velocity and temperature fluctuations" (Cogo et al. 2022, §1), obtained "by
neglecting the total temperature fluctuations" (Huang et al. 2022, §4.3.2).
Cogo et al. (2022, §1) note that the SRA relations "have been extensively
used to formulate turbulence models", although compressibility effects can
undermine their accuracy, especially at large heat fluxes. The DNS of
[Cogo et al. (2022)](/sources/cogo-2022.md) and
[Huang et al. (2022)](/sources/huang-2022.md) test them on spatially
developing zero-pressure-gradient [boundary layers](/benchmarks/turbulent-boundary-layer.md)
from Mach 2 to 14, with adiabatic and cooled walls, at $Re_\tau$ up to about
2000 and 1200 respectively.

Notation: Huang et al. write $z$ for the wall-normal coordinate and $y$ for
the spanwise one; both are swapped here to the registry's $y$ wall-normal.
Both sources write the Reynolds average with an overbar and the Favre average
with a tilde; here $\langle\cdot\rangle$ and $\langle\cdot\rangle_\rho$, with
$\phi''$ the Favre fluctuation. $T_r$ is the recovery temperature,
$T_r=T_e(1+r\frac{\gamma-1}{2}M_e^2)$ with recovery factor $r=0.89$ in both
sources, $q_w$ the wall heat flux and $(\cdot)_e$ free-stream (edge) values
(page-local).

## Morkovin scaling of the Reynolds stresses

The density-weighted Reynolds stress, normalized by the wall shear stress,
$$\frac{\langle\rho u_i''u_j''\rangle}{\tau_w}=\frac{\langle\rho\rangle}{\rho_w}\,\frac{\langle u_i''u_j''\rangle_\rho}{u_\tau^2},$$
is the form "which should collapse compressible data to the incompressible
ones" (Cogo et al. 2022, Eq. 5.1; Huang et al. 2022, §4.2, write the left-hand
side). The two printed forms are identical, since
$\langle\rho u_i''u_j''\rangle=\langle\rho\rangle\langle u_i''u_j''\rangle_\rho$
and $\tau_w=\rho_wu_\tau^2$ *(compiler check, not in the sources)*. It is
plotted against $y^+$ or against the semi-local coordinate $y^*$ (Huang,
Coleman & Bradshaw 1995, as recalled by both sources; see
[semi-local scaling](/definitions/compressible-velocity-transformation.md)).

**Where it works.**

- Supersonic cases at Mach 2 (cold wall, $T_w/T_r=0.76$) agree well with
  incompressible boundary-layer DNS at matching $Re_\tau$ (445 and 1989), the
  main difference being a higher streamwise peak (Cogo et al. 2022, §5.1,
  Fig. 10). Huang et al. (2022, §4.2) find the same for an adiabatic Mach 2.5
  case at $Re_\tau$ up to 1172 against incompressible and Mach 2 data, and a
  good collapse between the two nearly adiabatic cases (Mach 2.5 and 4.9),
  except for a rise of the streamwise peak with Mach number.
- The semi-local coordinate $y^*$ collapses the near-wall **peak locations**
  of all Reynolds-stress components at all Mach numbers (Huang et al. 2022,
  §4.2, Figs. 13–14) and the near-wall streak sizes, $\lambda_x^*\approx1000$
  and $\lambda_z^*\approx120$, which in wall units more than double in the
  cold-wall Mach 11 case (§5, Figs. 20–21).
- In semi-local scaling the dissipation term of the turbulent kinetic energy
  budget is almost independent of Reynolds and Mach numbers (Cogo et al.
  2022, §5.2, Fig. 11).
- Huang et al. (2022, §4.4, Fig. 19) find skewness and flatness of $u''$ at
  Mach 2.5 and 4.9 close to Gaussian over $30\lesssim y^*\lesssim1000$ and
  similar to incompressible channel data, which "supports the belief that
  without intense wall cooling, the turbulence dynamics is essentially
  incompressible up to Mach" 4.9.

**Where it breaks.**

- Morkovin scaling collapses profiles at equal $Re_\tau$ but not at different
  Mach numbers in $y^+$; $y^*$ increases the outer-layer discrepancies,
  although the semi-local friction Reynolds number $Re_\tau^*$ is not matched
  between cases (Cogo et al. 2022, §5.1).
- Under strong cooling at high Mach number (Mach 10.9, $T_w/T_r=0.20$) the
  streamwise normal stress has a much larger peak and the spanwise and
  wall-normal peaks are reduced (Huang et al. 2022, §4.2); Cogo et al. (2022,
  §5.1) likewise see reduced outer-layer $v$ and $w$ intensities at their
  highest Reynolds and Mach numbers (Mach 5.86), "suggesting a less efficient
  redistribution of the turbulent energy from the streamwise component".
  The near-wall streamwise peak $(\langle\rho u''u''\rangle/\tau_w)^{1/2}$
  rises from 2.9 at Mach 2.5 to 3.5 at Mach 10.9 at $Re_\tau=1138$ (Huang et
  al. 2022, §3.2, Fig. 6).
- Production and turbulent transport keep a Mach dependence in semi-local
  scaling, and at Mach 5.86 production exceeds dissipation farther out in
  the log layer, balanced by turbulent transport (Cogo et al. 2022, §5.2,
  Figs. 11–12).
- At Mach 10.9 with strong cooling, skewness and flatness of $u''$ are
  reduced in the viscous sublayer and depart more from Gaussian values in
  the log layer (Huang et al. 2022, §4.4).
- Wall-pressure fluctuations: Cogo et al. (2022, §5.3) find $p_{\mathrm{rms}}/\tau_w$
  controlled by $Re_\tau$ and almost Mach-independent except very near the
  wall and in the free stream, with no improvement from semi-local scaling;
  Huang et al. (2022, §3.2, Fig. 8) find the wall value
  $p'_{w,\mathrm{rms}}/\tau_w$ at 2.6–2.8 for (nearly) adiabatic walls but
  about 3.6 at Mach 6–8 and 4.5 at Mach 11–14 for cold walls
  ($T_w/T_r<0.5$). The two statements concern different wall conditions:
  Cogo et al.'s cases share $T_w/T_r=0.76$.

Matching $T_w/T_r$ does not match wall-cooling effects: Cogo et al. (2022,
§2, §3.1) use the Eckert number $Ec=(\gamma-1)M_e^2T_e/(T_r-T_w)$, 3.9 at
Mach 2 and 8.0 at Mach 5.86, and find the Mach 2 cases behave as more
strongly cooled (no near-wall temperature streaks). Huang et al. (2022, §6)
leave open whether wall cooling or Mach number drives the changes they see,
saying further computations are needed.

## Mean temperature: Reynolds analogies

The mean-flow Reynolds analogy chain recalled by Cogo et al. (2022, §1, §4)
runs from Reynolds (1874) through the laminar adiabatic Crocco–Busemann
relation and Walz's correction for $Pr\ne1$ to the empirical improvements of
Duan & Martín and the generalized Reynolds analogy of Zhang et al. (2014),
which includes the wall heat flux. All are quadratic,
$\langle T\rangle=T_w-a_1\langle u\rangle-a_2\langle u\rangle^2$ (Huang et
al. 2022, Eq. 4.9, Table 5; page-local $a_1$, $a_2$), with $a_1$ fixed by the
edge state and $a_2=r/(2c_p)$ for Walz, $Pr_t/(2c_p)$ with $Pr_t=0.9$ for
Huang et al. (1993), and a generalized recovery factor for Duan & Martín and
Zhang et al. The relation used in compressible wall models is on
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md).

- Cogo et al. (2022, §4, Fig. 9) find Zhang et al.'s relation more accurate
  than Walz at both Reynolds numbers, with Walz within 3% of the DNS, which
  they attribute to wall cooling too mild to stress it.
- Huang et al. (2022, §4.3.1, Fig. 15) find all relations agree at Mach 2.5
  (adiabatic), but at Mach 10.9 with $T_w/T_r=0.20$ only Duan & Martín and
  Zhang et al. fit; Duan & Martín is "significantly simpler".

**Reynolds analogy factor.** With the Stanton number
$C_h=q_w/(\rho_eU_ec_p(T_r-T_w))$ (page-local), Huang et al. (2022, §3.2,
Fig. 4) find $R_{af}=2C_h/C_f$ nearly constant over their range for all
hypersonic cold-wall cases, $1.1<R_{af}<1.2$, decreasing for the Mach 10.9
case from about 1.19 at $Re_\tau\lesssim400$ to 1.16 at $Re_\tau\approx1172$
(the value recommended by Chi & Spalding and by Hopkins & Inouye, as
recalled). They call this range "consistent with the usual approximation
$R_{af}=Pr^{-2/3}\approx1.256$" (§3.2, §6), although the printed range lies
below that value.

## The strong Reynolds analogy and its extensions

Neglecting total-temperature fluctuations, Morkovin's SRA predicts (as
recalled by Huang et al. 2022, §4.3.2, Eqs. 4.10–4.12, translated to
$y$ wall-normal)
$$R_{u''T''}=\frac{\langle u''T''\rangle_\rho}{\sqrt{\langle T''^2\rangle_\rho}\sqrt{\langle u''^2\rangle_\rho}}=-1,\qquad Pr_t=\frac{\langle\rho u''v''\rangle\,\partial_y\langle T\rangle_\rho}{\langle\rho v''T''\rangle\,\partial_y\langle u\rangle_\rho}=1,\qquad \frac{\sqrt{\langle T''^2\rangle_\rho}/\langle T\rangle_\rho}{(\gamma-1)M^2\sqrt{\langle u''^2\rangle_\rho}/\langle u\rangle_\rho}=1,$$
with $M$ the local mean Mach number. The extension of Huang, Coleman &
Bradshaw (1995) (HSRA) multiplies the last ratio by
$(1-\partial\langle T_0\rangle/\partial\langle T\rangle)Pr_t$, $T_0$ the total
temperature (Eq. 4.13). Gaviglio (1987) and Rubesin (1990) proposed other
non-adiabatic extensions, which Cogo et al. (2022, §1) list as "still under
validation" and do not test.

Huang et al. (2022, §4.3.2, Figs. 17–18) find:

- velocity and temperature fluctuations are nowhere perfectly
  anticorrelated; $R_{u''T''}$ is positive very near the wall, and for
  $y/\delta\gtrsim0.2$ it is about $-0.55$, independent of Reynolds number,
  Mach number and wall cooling;
- $Pr_t$ is of order one and insensitive to the flow parameters away from
  the wall, fitted in the outer region by $Pr_t=1-\tfrac14(y/\delta)$
  (Subbareddy & Candler, as recalled); it overshoots near the wall where the
  wall-normal turbulent heat flux changes sign;
- the original amplitude relation does not collapse the data, while the
  HSRA collapses all cases to a value close to unity in the outer layer,
  so that $T''_{\mathrm{rms}}$ can be estimated from $u''_{\mathrm{rms}}$
  with $Pr_t\approx1$.

## Qualifications

- Both sources test the hypothesis on zero-pressure-gradient flat-plate
  boundary layers only; Huang et al. (2022) contrast them with isothermal
  cold-wall channels, where the Trettel–Larsson transformation collapses
  the data that it does not collapse in their boundary layers (§4.1).
- Printed inconsistencies of the two papers that do not bear on these
  scalings (shape factors, Reynolds-number tables) are recorded on their
  Source pages.

# Citations

- [Cogo et al. (2022)](/sources/cogo-2022.md) — §1 (Morkovin's hypothesis, Reynolds analogies, SRA); §2, Table 1 (Eckert number); §3.1; §4, Eqs. (4.3)–(4.4), Fig. 9 (temperature–velocity relations); §5.1, Eq. (5.1), Fig. 10 (Morkovin scaling); §5.2, Figs. 11–12 (TKE budget); §5.3 (pressure fluctuations).
- [Huang et al. (2022)](/sources/huang-2022.md) — §3.2, Figs. 4, 6, 8 (Reynolds analogy factor, peak stresses, wall pressure); §4.2, Figs. 13–14 (Morkovin and semi-local scaling); §4.3, Eqs. (4.9)–(4.13), Table 5, Figs. 15–18 (temperature relations, SRA, HSRA, $Pr_t$); §4.4, Fig. 19; §5, Figs. 20–21; §6.
