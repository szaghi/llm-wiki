---
type: Definition
title: "Morkovin's hypothesis and Reynolds analogies"
description: "Morkovin's hypothesis holds that, while density fluctuations stay small, compressible wall turbulence behaves like incompressible turbulence once mean property variations are scaled out; this page gives Morkovin scaling, the Reynolds analogies, the turbulent Prandtl number, and where DNS from Mach 0.5 to 14, cooled walls, thermally perfect channels and shock interactions confirm or break them."
status: established
aliases: [Morkovin hypothesis, Morkovin scaling, Morkovin's scaling, strong Reynolds analogy, SRA, HSRA, Reynolds analogy factor, turbulent Prandtl number]
tags: [compressible, boundary-layer, dns, hypersonic, rans]
timestamp: 2026-10-29T10:03:00Z
---

# Morkovin's hypothesis and Reynolds analogies

**Morkovin's hypothesis** (Morkovin 1962, cited by
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
2000 and 1200 respectively. In the historical account of
[Kim & Leonard (2024)](/sources/kim-2024-b.md) (§4.5), the first compressible
wall-bounded DNS (Buell's 1990 Couette flow; the supersonic channel of
Coleman et al. 1995; the supersonic boundary layer of Rai et al. 1995, as
cited) "shed light on" the hypothesis and the strong Reynolds analogy, and
Coleman et al.'s "nonphysical" experiment, with different Mach numbers in
the energy and momentum equations, found the direct compressibility effects
small at Mach 1.5 and 3.

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
Coleman & Bradshaw 1995, cited by both sources; see
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
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) compare six DNS of
  spatially developing zero-pressure-gradient layers at $M_\infty=0.5$, 2 and 8,
  each quasi-adiabatic ($T_w/T_r=1$) and cooled ($T_w/T_r=0.25$ at Mach
  0.5, 0.5 at Mach 2 and 8), at $Re_\tau\approx650$ ([STREAmS](/software/streams.md)).
  Cooling raises the rms of $u''$ over $u_\tau$ and the shear
  stress $\langle u''v''\rangle_\rho/u_\tau^2$, mainly because $u_\tau$
  falls, and moves their peaks outward; the density factors of Morkovin
  scaling improve the collapse across Mach numbers and wall temperatures,
  and the semi-local coordinate collapses the peak positions (§3,
  Fig. 4). The near-wall streak spacing is $\lambda_z^*\approx100$ in all
  six cases, which they call in accordance with Huang et al. (§4,
  Figs. 10–11).
- As a validation of the incoming layer of shock interactions:
  [Kang & Lee (2024)](/sources/kang-2024.md) (§III, Fig. 5) find the
  density-scaled intensities of a Mach 2.9 layer ($Re_\theta=2400$,
  $T_w/T_\infty=2.87$) in agreement with incompressible DNS (Wu & Moin) and
  compressible DNS (Tong et al., $Re_\theta=2300$), with the streamwise peak
  at $y^+\approx12$; [Tang et al. (2024)](/sources/tang-2024.md) (§2.3,
  Fig. 12) find the scaled $u_{\mathrm{rms}}$ of a Mach 5 cold-wall layer
  ($T_w/T_r=0.5$, $Re_\tau=700$) collapsed on incompressible data for
  $y/\delta<0.4$ and slightly above Spalart's (1988) data beyond, as
  Pirozzoli et al. (2004) also observed, closer to the higher-$Re$ data of
  Sillero et al. (2013) and within 5 % of Huang et al. (2022) at the edge
  (all as cited); and [Wei et al. (2023)](/sources/wei-2023.md) (§III B,
  Fig. 11) find the density-scaled stresses of a Mach 2.44 wall-resolved
  LES in agreement with experiments, in the ratio
  $\sqrt{R_{11}}:\sqrt{R_{33}}:\sqrt{R_{22}}\approx4:3:2$ that they cite from
  Wilcox (without naming Morkovin).

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
  [Zhang et al. (2022)](/sources/zhang-2022-b.md), Table 3, separate the
  two effects at fixed $Re_\tau\approx650$: the wall value
  $p'_{w,\mathrm{rms}}/\tau_w$ is 2.56, 2.88 and 3.00 for the
  quasi-adiabatic walls at Mach 0.5, 2 and 8, and 2.03, 2.60 and 3.41 for
  the cooled ones, so cooling suppresses the wall-pressure fluctuations in
  the subsonic and supersonic layers and enhances them near the wall at
  Mach 8 (§5, Fig. 13). The enhancement comes with travelling-wave-like
  alternating positive and negative structures of dilatation and pressure
  inside cold low-speed streaks of the viscous and buffer layers,
  streamwise wavelength $\lambda_x^+\approx100$, which they find "dominant
  near the wall" at Mach 8 where Coleman, Kim & Moser, whom they cite, had
  judged such structures a "dynamically insignificant passive effect" at
  Mach 3 (§4, §6.2, Fig. 12); see
  [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md).
- **Turbulent Mach number.** Cooling raises the turbulent Mach number
  $M_t=\sqrt{\langle u_i''u_i''\rangle}/\bar c$ (local mean sound
  speed $\bar c$, page-local) in all three regimes of Zhang et al.
  (2022); in the Mach 8 cases it exceeds 0.3 locally in the buffer and log
  layers, where the authors expect eddy shocklets (§3, Eq. 3.3, Fig. 8).
  Their synthesis is that cooling suppresses the vorticity mode and
  enhances the acoustic mode, and that at cooled Mach 8 the acoustic mode
  is "essential in both the near-wall region and the free stream, which
  should be considered when modelling high-Mach-number wall-bounded
  turbulence" (§7).

- **Hypersonic cold walls as a stated limit.** [Zhang et al. (2024b)](/sources/zhang-2024-b.md)
  (§1, §3.1, Fig. 5b) state that the hypothesis holds at moderate Mach
  number ($M<5$) on adiabatic walls (Maeder et al. 2001; Pirozzoli et al.
  2004, as cited) but "is not necessarily valid under non-adiabatic
  hypersonic conditions"; in their Mach 6 layers at $T_w/T_r=0.50$, 0.75 and
  1.0 the peak of the density-scaled fluctuations moves closer to the wall
  as the wall is cooled, as Duan et al. (2010, as cited) found.

Matching $T_w/T_r$ does not match wall-cooling effects: Cogo et al. (2022,
§2, §3.1) use the Eckert number $Ec=(\gamma-1)M_e^2T_e/(T_r-T_w)$, 3.9 at
Mach 2 and 8.0 at Mach 5.86, and find the Mach 2 cases behave as more
strongly cooled (no near-wall temperature streaks). Huang et al. (2022, §6)
leave open whether wall cooling or Mach number drives the changes they see,
saying further computations are needed.

## Mean temperature: Reynolds analogies

The mean-flow Reynolds analogy chain cited by Cogo et al. (2022, §1, §4)
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
- [Zhang et al. (2022)](/sources/zhang-2022-b.md), §3, Eqs. (3.1)–(3.2),
  Fig. 5, print both relations normalized by free-stream values
  ($T_\infty$, $U_\infty$; they list an edge temperature separately),
  $\langle T\rangle/T_\infty=T_w/T_\infty+\frac{T_\ast-T_w}{T_\infty}\frac{\langle u\rangle}{U_\infty}+\frac{T_\infty-T_\ast}{T_\infty}\Big(\frac{\langle u\rangle}{U_\infty}\Big)^2$,
  with $T_\ast=T_r$ for Walz and, for the generalized analogy,
  $T_\ast=T_\infty+r_gU_\infty^2/(2c_p)$ with the generalized recovery
  factor $r_g=2c_p(T_w-T_\infty)/U_\infty^2-2Pr\,q_w/(U_\infty\tau_w)$
  ($T_\ast$, $r_g$ page-local). Walz is accurate for the quasi-adiabatic cases and departs
  for the cooled ones; the generalized analogy fits both, in agreement
  with Cogo et al. and Huang et al.

**Reynolds analogy factor.** With the Stanton number
$C_h=q_w/(\rho_eU_ec_p(T_r-T_w))$ (registry §11), Huang et al. (2022, §3.2,
Fig. 4) find the Reynolds analogy factor $s_{\mathrm{RA}}=2C_h/C_f$ (registry §11; the source's $R_{af}$) nearly constant over their range for all
hypersonic cold-wall cases, $1.1<s_{\mathrm{RA}}<1.2$, decreasing for the Mach 10.9
case from about 1.19 at $Re_\tau\lesssim400$ to 1.16 at $Re_\tau\approx1172$
(the value that they cite as recommended by Chi & Spalding and by
Hopkins & Inouye). They call this range "consistent with the usual approximation
$R_{af}=Pr^{-2/3}\approx1.256$" (§3.2, §6), although the printed range lies
below that value *(compiler check, not in the sources)*.
For their three cooled layers at $Re_\tau\approx650$,
[Zhang et al. (2022)](/sources/zhang-2022-b.md), Table 3, find
$2C_h/C_f=1.16$, 1.14 and 1.11 at Mach 0.5, 2 and 8 (Stanton number
defined on $T_w-T_r$), "all close to 1.1, as predicted by Hopkins &
Inouye" (§3); cooling also lowers the shape factor and raises $C_f$ in
all regimes.

## The strong Reynolds analogy and its extensions

Neglecting total-temperature fluctuations, Morkovin's SRA predicts (in
the form printed by Huang et al. 2022, §4.3.2, Eqs. 4.10–4.12, who cite
it; translated to $y$ wall-normal)
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
  (the fit of Subbareddy & Candler that they cite); it overshoots near the wall where the
  wall-normal turbulent heat flux changes sign;
- the original amplitude relation does not collapse the data, while the
  HSRA collapses all cases to a value close to unity in the outer layer,
  so that $T''_{\mathrm{rms}}$ can be estimated from $u''_{\mathrm{rms}}$
  with $Pr_t\approx1$.

**A boundary layer with a non-monotonic temperature profile.**
[Wang & Xu (2024)](/sources/wang-2024-h.md) (§5.4, Eqs. 5.4–5.5,
Figs. 20–22) test the SRA amplitude relation, its variable-$c_p$ form
$\tilde c_p T''_{\mathrm{rms}}/(u''_{\mathrm{rms}}\langle u\rangle_\rho)=1$ (assuming
$\tilde c_pT''_{\mathrm{rms}}\gg c_p''\langle T\rangle_\rho$; $\tilde c_p$ the mean specific heat,
page-local) and the extensions of Cebeci (ESRA), Gaviglio (GSRA), Rubesin
(RSRA) and Huang, Coleman & Bradshaw (HSRA) on the DNS of a Mach 2.33
boundary layer under a sonic cold hydrogen film, with and without
combustion, at $Re_\tau\approx1000$ over an adiabatic wall. The SRA and its
variable-$c_p$ form are nearly constant over $10<y^+<200$, the latter
closer to one, and both deviate strongly in the outer layer; GSRA, RSRA and
HSRA deviate severely and ESRA falls outside the plotted range. The authors
trace the failures to the assumptions: the total-temperature–velocity
similarity behind ESRA is far from satisfied, and the mixing-length
proportionality $u''\,\partial_y\langle T\rangle_\rho\propto T''\,\partial_y\langle u\rangle_\rho$ behind
GSRA, RSRA and HSRA is not constant (Fig. 21). The linear coherence between
$u$ and $T$ is about 0.5 for $y^+<200$ and is lost above, which they
attribute to large-scale temperature and hydrogen fluctuations that do not
drive velocity fluctuations at the same scales (Fig. 22). Where Huang et
al. (2022) find the HSRA close to one in the outer layer of
zero-pressure-gradient layers of uniform composition, Wang & Xu's layer has
a non-monotonic mean temperature across the cold film; the papers do not
compare each other's flows.

The turbulent Prandtl and Schmidt numbers of these and of other
flows are collected on the
[turbulent Prandtl number](/definitions/turbulent-prandtl-number.md) page:
Wang & Xu (2024, §5.2) find $Pr_t\approx1.1$ in the log region and 0.5–0.9
in the outer layer, discontinuous where the wall-normal turbulent heat flux
changes sign, and [Wei et al. (2023)](/sources/wei-2023.md) (§IV F) find
$Pr_t$ and $Sc_t$ between 0 and 2 in a supersonic film-cooling LES.

## Across separated hypersonic interactions

[Helm & Martín (2022)](/sources/helm-2022.md), §IV E, test the same
relations in wall-resolved LES of two separated compression-ramp
[shock/boundary-layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
over cold walls: Mach 7.2 on a 33° ramp ($T_w/T_r=0.52$) and Mach 9.1 in
nitrogen on a 34° ramp ($T_w/T_r=0.33$; the source's "Mach 10" case, written
Mach 9 here), upstream of the interaction and in
the recovering boundary layer downstream. Their wall-normal coordinate $z'$
(distance from the local wall, over the local thickness $\delta_x$) is
written $y$ here.

- **Turbulent Prandtl number.** Upstream, $Pr_t$ is within 13% of one for
  $0.05<y/\delta_x<0.75$, about 0.75 at the edge, and fails below 0.05;
  downstream it is about 1.0 for $y/\delta_x>0.1$ at Mach 7 and about 1.4 at
  $y/\delta_x=0.3$–0.5 at Mach 9 (Fig. 29a). The outer fit
  $Pr_t=1-\tfrac14(y/\delta)$ cited by Huang et al. (2022) gives 0.75 at
  the edge, the value Helm & Martín find there *(compiler check, not in the
  sources)*.
- **SRA phase relation.** $-R_{u''T''}$ falls upstream from 0.85 at
  $y/\delta_x=0.05$ to 0.6 at the edge and changes sign at the cold wall; it
  is about 0.5 in the Mach 9 downstream layer (Fig. 29b). Helm & Martín
  (§IV E) cite about 0.6 through most of adiabatic layers up to edge Mach 12 (Duan
  et al.), only slightly reduced by wall cooling; Huang et al. (2022) find
  about 0.55 for $y/\delta\gtrsim0.2$ (above).
- **SRA magnitude relation.** About 0.65 upstream and 0.4 downstream at
  Mach 7, 0.6 and 0.35 at Mach 9, with a minimum near 0.3 close to the wall:
  the original relation fails over cold walls. The HSRA of Huang, Coleman &
  Bradshaw takes about 1.2 upstream for $y/\delta_x=0.1$–1.0 in both flows,
  about 1.2 downstream only for 0.2–0.5 at Mach 7, and fails in the Mach 9
  recovering layer (Fig. 29c–d). Huang et al. (2022) find the HSRA close to
  one in the outer layer of their zero-pressure-gradient layers; the two
  levels belong to different flows and are not compared by either source.
- **Reynolds analogy factor.** With the Stanton number defined on $T_w-T_r$
  (the opposite sign of the convention above), Helm & Martín plot
  $C_f/2C_h$: 0.85 upstream and about 0.7 downstream; the analogy with a
  factor near one fails in the separated region (Fig. 28a). The upstream
  value corresponds to $2C_h/C_f\approx1.18$, inside the range 1.1–1.2 that
  Huang et al. (2022) find for hypersonic cold-wall layers *(compiler check,
  not in the sources)*. The pressure–heat-transfer law
  $q(x)/q_u=(p(x)/p_u)^{0.85}$ of Back & Cuffel (subscript $u$ the
  undisturbed upstream layer), "shown by Priebe and Martín to be reasonably
  accurate for the attached Mach 7 interaction", over-predicts heat transfer
  at separation and in the recovering layer and misses the steep rise past
  the corner; it was derived for attached interactions (§IV E, §V, Fig. 28b).

The same factor collapses in a cold-wall compression-ramp DNS at Mach 5
($30^\circ$, $T_w/T_r=0.5$, $Re_\tau=700$, incipient separation):
[Tang et al. (2024)](/sources/tang-2024.md) (§4.1, Fig. 21b) find
$C_f/(2C_h)=1/s_{\mathrm{RA}}$ (their $S$, with their Stanton number on the recovery-to-wall enthalpy
difference) at 0.86 upstream, the turbulent-boundary-layer value of Qu et
al. (2001, as cited), drastically changing in the recirculation region and
constant at 0.5 downstream instead of recovering, as Helm & Martín (2022)
also report and call "not well understood"; Helm & Martín's own downstream
level is about 0.7 (above), in a different flow. Tang et al. replace the
pressure–heat-transfer law with exponent 0.85, which they find to
over-predict recent data by up to 72 %, with a correlation derived from
boundary-layer heat-transfer theory and oblique-shock relations (35 %
maximum error) and explain its trend with a budget of mean and turbulent
compression and dissipation heat (§3; see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

Morkovin's hypothesis also serves as a construction tool: the Mach 9 DNS of
Helm & Martín (2022, §II) was initialized with incompressible DNS
fluctuations scaled by the mean density (see
[direct numerical simulation](/definitions/direct-numerical-simulation.md)).

## Turbulent Prandtl number in a compressible RANS closure

[Chen et al. (2024)](/sources/chen-2024.md) carry these relations into an
algebraic RANS closure: a compressible recalibration of the
[Baldwin–Lomax model](/methods/baldwin-lomax-model.md), which their title
calls a "wall model" but which closes the whole boundary layer with an
eddy viscosity $\mu_t$ and an eddy conductivity $c_p\mu_t/Pr_t$, solved by
boundary-layer marching; it is not an LES wall model. They test it against
twelve DNS of zero-pressure-gradient boundary layers at free-stream Mach 2
to 13.64 with $T_w/T_r$ from 0.18 (cold) to 1.9 (heated) (Table 1).
Notation: the source writes the Reynolds average with an overbar and the
Favre average with a tilde, translated as above; $\mu_t$ is extracted from
the DNS as $-\langle\rho u''v''\rangle/\partial_y\langle u\rangle_\rho$.

**Morkovin scaling inside the mixing length.** Chen et al. (2024, §3.1,
Eqs. 3.1–3.2) write the modelled shear stress normalized by $\tau_w$, which
they identify with the semi-local stress of Morkovin scaling, and show that
the inner eddy viscosity of the semi-local Baldwin–Lomax model (mixing
length with $y^*$ in the van Driest damping) is equivalent to applying the
Trettel–Larsson transformation; their modification replaces it by the
total-stress transformation of Griffin, Fu & Moin (see
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
They recall that the transformation of Hasan et al. (HLPP), which adds a
friction-Mach-number dependence to the damping, questions Morkovin's
hypothesis through intrinsic compressibility effects (§1, §3.1), and find
mean errors of 2.2% (Griffin et al.) and 2.4% (HLPP) of the two
transformations over their database (App. B, Fig. 16).

**DNS turbulent Prandtl number.** With the definition of $Pr_t$ printed
above (their Eq. 3.15), Chen et al. (2024, §3.3, Fig. 6a) recall values of
0.7 to 1.1 above the buffer layer and about 0.85 in the log region from the
literature, and find in the DNS of three cold-wall layers that near the
temperature peak both $\partial_y\langle T\rangle_\rho$ and the wall-normal
turbulent heat flux change sign, so that $Pr_t$ becomes negative or
singular, with $Pr_t<0.5$ between the singular point and the wall; a
singular point appears also in an adiabatic Mach 2.5 layer at
$y^*\approx2$. Huang et al. (2022, §4.3.2) likewise report a near-wall
overshoot where the wall-normal heat flux changes sign (above). Chen et al.
conclude that monotone wall-distance formulae, among them the outer fit
$Pr_t=1-\tfrac14(y/\delta)$ of Subbareddy & Candler that Huang et al. use,
cannot represent this near-wall behaviour; with the baseline model that
formula behaves like $Pr_t=1$ (Fig. 6b). The two statements concern
different regions: Huang et al. fit the outer layer only.

**Consequences for the closure.** With the baseline model, the mean
temperature above $y^*\approx100$ is insensitive to $Pr_t$, while below it
the temperature falls with $Pr_t$; the constant $Pr_t=0.9$ over-predicts
the peak temperature of cold-wall layers, the best constant being 0.8 for a
Mach 7.87 layer at $T_w/T_r=0.48$ and 0.6 for a Mach 5.84 layer at
$T_w/T_r=0.25$ (§3.3). Their remedy is a two-layer temperature: the energy
equation with constant $Pr_t$ above a matching height $y_{\mathrm{mT}}$
($y^*_{\mathrm{mT}}=100$), and below it the quadratic temperature–velocity
relation of Duan & Martín and Zhang et al. anchored at that height,
$$\langle T\rangle_\rho=T_w+C_{\mathrm{DM}}(T_r-T_w)\Big(1-\frac{\langle u\rangle_\rho}{U_{\mathrm m}}\Big)\frac{\langle u\rangle_\rho}{U_\delta}+(T_{\mathrm m}-T_w)\Big(\frac{\langle u\rangle_\rho}{U_{\mathrm m}}\Big)^2,\qquad y<y_{\mathrm{mT}},$$
(Eq. 3.17; page-local: $U_{\mathrm m}$, $T_{\mathrm m}$ the mean velocity
and temperature at $y_{\mathrm{mT}}$, $U_\delta$ the edge velocity; $C_{\mathrm{DM}}$ the
relation's constant, registry §11), with $C_{\mathrm{DM}}=0.8259$ (Duan & Martín), recast by Zhang et
al. as $s_{\mathrm{RA}}Pr$ with the Reynolds analogy factor $s_{\mathrm{RA}}=1.14$, and the recovery
factor $r=Pr^{1/3}$ (§3.3, Eq. 3.16; Cogo et al. and Huang et al. take
$r=0.89$). This is one of the quadratic relations of the
"Mean temperature" section, written in two-layer form after Griffin et
al., whom they cite, and results change little for $y^*_{\mathrm{mT}}$ from
50 to 150 (App. A, Fig. 15).

**Results.** The implied $Pr_t$ of the modified model reproduces the DNS
singularity a posteriori (at $y^*\approx8$ for the Mach 7.87 case; §4,
Fig. 7). For heated and moderately cooled walls ($T_w/T_r>0.5$) the
modified eddy viscosity alone already improves the temperature; for
$T_w/T_r\le0.5$ modifying $\mu_t$ is insufficient and the
temperature–velocity relation is needed (§4, Fig. 11). Over all cases the
mean relative temperature error falls from 1.4% to 0.4% in the logarithmic
inner coordinate and from 8.8% to 3.4% in the linear outer coordinate, the
velocity errors from 1.2% to 0.7% and 2.5% to 1.3% (§4, Fig. 13). The
authors restrict these modifications to attached thin layers and expect a
smaller gain in channels and pipes, where the Trettel–Larsson
transformation is accurate and $Pr_t$ has no near-wall singularity (§5.1).

## Channel flow of a thermally perfect gas, and the numerical caveat

**The hypothesis as restated.** [Aiello et al. (2026)](/sources/aiello-2026.md),
§1, restate Morkovin's hypothesis in a weaker form than the mapping quoted
above: "at sufficiently high Reynolds number and moderate Mach number,
compressibility effects influence wall turbulence primarily through
spatial variations of mean density and transport properties, while density
fluctuations play a secondary role". They recall the support of the early
isothermal-wall channel DNS of Coleman et al. and Huang et al. (1995) up to
bulk Mach number about 3, the semi-local scalings that followed, and,
against it, recent evidence that "intrinsic compressibility effects can be
dynamically significant" near the wall (Hasan et al. 2023, 2025), with cold
walls further modifying vortex topology and production (Yu et al.). The
transformation of Hasan et al. is the one that Chen et al. (2024) recall as
questioning the hypothesis (above). Aiello et al. add that the Chu–Kovásznay split
into vortical, acoustic and entropy modes "does not constitute a derivation
of Morkovin's hypothesis" but is an interpretive frame: entropy modes are
linearly passive yet act through density, temperature and transport
properties, so all components must be computed accurately as the bulk Mach
number grows (§1).

**DNS beyond the calorically perfect gas.** Aiello et al. (2026, §2.1,
§3.3, Table 2) compute isothermal-wall channels of $\mathrm{CO_2}$ as a
thermally perfect gas (temperature-dependent specific heats from NASA
polynomials, Sutherland viscosity, $Pr=0.72$) at wall-based bulk Mach
number 3, 4 and 5 and $Re_\tau\approx470$, 630 and 800 with
[STREAmS](/software/streams.md) (sixth-order central differences,
$\Delta x^+\approx8$–10, $\Delta z^+\approx4$–5, first wall point at
$\Delta y^+\approx0.3$); for such gases "entropy variations are no longer
trivially related to temperature" (§1), and the Mach 5 centreline reaches
about 1000 K (§4.1). Their reductions use the Morkovin and semi-local forms
above: Reynolds stresses $\langle\rho\rangle\langle u_i''u_j''\rangle_\rho/\tau_w$
against $y^*$, and the Trettel–Larsson transformed mean velocity (see
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
For every scheme and Mach number the transformed profiles collapse on
the viscous-sublayer law $u^+_{TL}=y^*$, and a narrow logarithmic region
appears for $y^*\ge40$ with $\kappa=0.41$ and $B=6.0$ fitted to the
entropy-conservative runs, an intercept they attribute to the low semi-local friction Reynolds number (160 to 190), as in
low-$Re_\tau$ incompressible flow and earlier calorically perfect channel
DNS (§4.1, Fig. 1; see [law of the wall](/definitions/law-of-the-wall.md)).

**How much of the departure is numerical.** The same flows run with
different convective discretizations differ in exactly the statistics this
page uses to test the hypothesis (Aiello et al. 2026, §4.1–4.2, Table 3):

| Bulk Mach (wall) | $p'_{w,\mathrm{rms}}/\tau_w$, entropy-conservative / KEEP | max difference of the transformed velocity, KEEP | max difference of the streamwise stress $\langle\rho\rangle\langle u''u''\rangle_\rho/\tau_w$, KEEP / Gouasmi et al. |
|---|---|---|---|
| 3 | 1.97 / 2.89 | 0.23% | 0.60% / 1.38% |
| 4 | 2.33 / 3.23 | 1.05% | 1.59% / 1.21% |
| 5 | 2.57 / 3.55 | 1.98% | 10.98% / 5.25% |

(differences in the maximum norm relative to the authors' entropy-conservative
scheme, which serves as the reference; no external DNS is compared). The
kinetic-energy-preserving but not entropy-conservative KEEP scheme
over-predicts thermodynamic fluctuations, raises the streamwise stress
peak, "abnormally high" at Mach 5, and over-predicts the logarithmic-region
velocity, increasingly with Mach number; the shear stress is
scheme-independent (§4.2, Fig. 2). Aiello et al. do not discuss the
boundary-layer DNS of Cogo et al. (2022) and Huang et al. (2022) above. See [entropy conservation](/properties/entropy-conservation.md),
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [turbulent channel flow](/benchmarks/turbulent-channel-flow.md).

## In thermal wall models for LES

The review of wall models by [Bose & Park (2018)](/sources/bose-2018.md),
§2.5, Eq. (17), states the equilibrium thermal wall model as the
wall-normal total-energy balance of the wall-model layer with constant
properties, printed as
$$\frac{\partial}{\partial y}\left(-u\,\tau^{\mathrm{wm}}_{12}-q_{\mathrm{turb}}\right)+\frac{\partial}{\partial y}\left(\mu u\frac{\partial u}{\partial y}+\lambda_{\mathrm c}\frac{\partial T}{\partial y}\right)=0$$
($u$, $T$ the wall-model velocity and temperature, the source's tilde
quantities; $\tau^{\mathrm{wm}}_{12}$ the modelled turbulent shear stress,
$q_{\mathrm{turb}}$ the turbulent heat flux, $\lambda_{\mathrm c}$ the
molecular conductivity; all page-local). The turbulent heat flux is
closed by the gradient-diffusion model of Rannie,
$q_{\mathrm{turb}}\approx-\lambda_t\,\partial T/\partial y$ with the
turbulent conductivity $\lambda_t=\mu_tc_p/Pr_t$. The terms
$-u\,\tau^{\mathrm{wm}}_{12}+\mu u\,\partial u/\partial y$ carry
the inner-layer viscous heating, so the model can capture the near-wall
temperature peak; without strong viscous heating the balance gives the
strong Reynolds analogy in its mean-flow form, $C_h=C_f/2$ ($C_h$ the
Stanton number, whose normalization the review does not print). Bose & Park state, citing earlier work, that this relation has been shown
experimentally to hold within less than 30% for Mach numbers below 10,
weakly dependent on $Re_\theta$ from $10^3$ to $10^5$, and confirmed by DNS
with wall heating (Wu & Moin 2010); that it fails near separation, where
the skin friction vanishes and the heat transfer does not; and that
law-of-the-wall errors in adverse-pressure-gradient flows appear amplified
in temperature and heat-flux predictions (§2.5; see
[adverse-pressure-gradient wall laws](/definitions/adverse-pressure-gradient-wall-law.md)).
In their outlook (§4.4) they state that scaling incompressible closures to
variable inertia works when the turbulent Mach number is small
($M_t\lesssim0.2$, after Lele 1994), and that thermal predictions may fail
where the strong Reynolds analogy fails, with significant stagnation-temperature
variation at strongly heated or cooled walls. The wall-stress models these
thermal balances accompany are on
[equilibrium wall models](/methods/equilibrium-wall-model.md) and
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md).

## Near shocks and at the inflow of shock interactions

The sources below on shock/boundary-layer interactions use the analogies
or the scaling only at the inlet, and one of them declines Morkovin's
assumption downstream.

- [Yu et al. (2022)](/sources/yu-2022-e.md), §1.2, reject the spectral
  turbulent-kinetic-energy formulation of Dupuy, Toutant & Bataille for
  their oblique shock interaction (Mach 2.28) because it rests on
  Morkovin's insignificance of density fluctuations, which "may
  contribute largely to the kinetic energy near the shock wave"; they
  build their scale-by-scale budget on the density-weighted two-point
  correlation of Arun et al. instead (§3; see
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
  Their inflow temperature and its fluctuations come from the generalized
  Reynolds analogy of Zhang et al. (2014) (§2.1).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md), §2.1, generate
  the density and temperature fluctuations of their digital-filter inflow
  (Mach 2.91 compression/expansion ramp) from the strong Reynolds analogy,
  with van Driest-transformed mean profiles (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
- [Wei et al. (2023)](/sources/wei-2023.md), §II D, Eq. (24), do the same for
  the synthetic-eddy inflow of a Mach 2.44 film-cooling LES, with
  $T'/\langle T\rangle=-(\gamma-1)M^2u'/\langle u\rangle$ and, as printed,
  $\rho'/\langle\rho\rangle=T'/\langle T\rangle$ (see Qualifications).
- [Kang & Lee (2024)](/sources/kang-2024.md) (§IV) use Morkovin-scaled
  intensities only to validate the incoming layer of their Mach 2.9 ramp
  DNS (above), not inside the interaction.

## Thermodynamic fluctuations for a hypersonic inflow library

[Mo et al. (2023)](/sources/mo-2023.md) need the analogies as working
relations. Their DNS inflow takes stored velocity planes from a Mach 2.25
precursor (a turbulence fluctuation library), rescales them with
Morkovin's density scaling, and must then supply temperature and density
fluctuations that the library does not store (§III; the velocity mapping
and recovery lengths are on
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Notation: $\langle\cdot\rangle$ is the time and spanwise average, primes
are Reynolds fluctuations, $(\cdot)_e$ edge values, and $s_{\mathrm{RA}}$
(registry §11) the Reynolds analogy factor of the generalized Reynolds
analogy (GRA).

**Velocity scaling.** The rescaling keeps
$\sqrt{\langle\rho\rangle/\rho_w}\,u_i'/u_\tau$ equal between library and
target at matched coordinates: spanwise in wall units, wall-normal in wall
units near the wall and in $\delta$ in the outer layer, blended by a tanh
function between $0.2\delta$ and $0.5\delta$ (Eqs. 15–17). The authors
justify it by Morkovin's hypothesis that compressibility and heat transfer
act mainly through the mean density, and cite Duan et al. for its validity
below Mach 12 and above a wall-to-recovery temperature ratio of 0.12
(§III B).

**The SRA laws that fail.** For the Mach 2.9 adiabatic case they use
Morkovin's SRA in the form (Eqs. 18–19)
$$\frac{T'}{\langle T\rangle}\approx-(\gamma-1)M^2\frac{u'}{\langle u\rangle},\qquad \frac{\rho'}{\langle\rho\rangle}=-\frac{T'}{\langle T\rangle},$$
the second from the equation of state with $p'$ and the $\rho'T'$
correlation neglected. They state that the first assumes $Pr=1$,
negligible total-temperature fluctuations and an adiabatic wall, all
violated in a cold-wall hypersonic layer (§IV A). In their Mach 7.25
cold-wall inflow ($T_w=562$ K, $T_e=64.4$ K) the maximum relative
temperature fluctuation from the SRA exceeds one near $y/\delta=0.8$. The
density law then gives $\rho'/\langle\rho\rangle<-1$, a negative
instantaneous density (§IV B, Fig. 10c). Martin's remedy (2007, as cited),
multiplying the SRA right-hand side by a factor below 0.8, is said to
distort the PDF of positive density fluctuations.

**Replacement laws.** For temperature they combine the instantaneous form
of Gaviglio's extension, $T'\approx(\partial\langle T\rangle/\partial\langle u\rangle)\,u'$
(Yu & Xu 2022, as cited; Eq. 21), with the GRA of Zhang et al. (2013, as
cited), Eqs. (11)–(13),
$$\frac{\langle T\rangle}{T_e}=\frac{T_w}{T_e}+\frac{T_r-T_w}{T_e}\,f\!\left(\frac{\langle u\rangle}{u_e}\right)+\frac{T_e-T_r}{T_e}\left(\frac{\langle u\rangle}{u_e}\right)^2,\qquad f(\xi)=(1-s_{\mathrm{RA}}Pr)\,\xi^2+s_{\mathrm{RA}}Pr\,\xi,$$
with $s_{\mathrm{RA}}=1.16$ and $Pr=0.72$, so that
$f=0.165\xi^2+0.835\xi$ (Eq. 13). They print the resulting law as
$$T'=2\frac{\langle u\rangle}{u_e^2}\left[T_e-(1-s_{\mathrm{RA}}Pr)\,T_w-s_{\mathrm{RA}}Pr\,T_r\right]u'\approx2\frac{\langle u\rangle}{u_e^2}\left[T_e-0.165\,T_w-0.835\,T_r\right]u'$$
(Eqs. 22–23; see Qualifications). For density they keep the correlation
term of the decomposed equation of state,
$p'/\langle p\rangle=\rho'/\langle\rho\rangle+T'/\langle T\rangle+\rho'T'/(\langle\rho\rangle\langle T\rangle)$
(Eq. 24), and drop only $p'$:
$$\frac{\rho'}{\langle\rho\rangle}=-\frac{T'/\langle T\rangle}{1+T'/\langle T\rangle}\qquad(\text{Eq. 25}),$$
whose linearization is the SRA density law. The relation is a hyperbola
with asymptotes $\rho'/\langle\rho\rangle=-1$ and $T'/\langle T\rangle=-1$,
so the density stays positive whenever $T'/\langle T\rangle>-1$.

**A posteriori check in the Mach 7.25 DNS** (§IV B, Figs. 15–17):

- the rms of the total-temperature fluctuations reaches about 10%, so the
  SRA assumption of negligible total-temperature fluctuations fails;
- the ratio of the rms sides of the SRA temperature law (their
  $\Gamma_1$, Eq. 26) is about 0.8 over most of the layer, while that of
  the new law ($\Gamma_2$, Eq. 27) is close to one;
- at $y^+=10$, 20 and 100 the PDFs show that the correlation term
  $\rho'T'/(\langle\rho\rangle\langle T\rangle)$ grows with $y^+$. At
  $y^+=100$ it exceeds the temperature and density fluctuations in
  magnitude, so it cannot be dropped. $|p'/\langle p\rangle|<0.2$ is the
  high-probability event at all three heights, which justifies dropping
  $p'$;
- the SRA density law deviates increasingly from the DNS with $y^+$ and
  produces $\rho'/\langle\rho\rangle<-1$ at $y^+=20$ and 100, while
  Eq. (25) avoids these values and collapses better with the DNS over the
  whole PDF (Fig. 17).

The same DNS reproduces the GRA mean temperature–velocity relation at
Mach 2.25, 2.9 and 7.25 (§II B, §III C, §IV B), in agreement with the
mean-temperature findings of Cogo et al. (2022) and Huang et al. (2022)
above.

## Variable-property channels in a RANS closure

[Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) (§2.1–2.2) build
their [field-inversion](/methods/field-inversion-machine-learning.md)
database of 30 channel DNS on Morkovin's hypothesis as a working premise.
The database holds low-Mach channels with strong property variations
(volumetric heating, isothermal walls), the ideal-gas channels of
Trettel & Larsson up to Mach 4, and incompressible channels. They state,
citing Patel et al., that the hypothesis applies to all the
variable-property cases. Their one-dimensional RANS models the turbulent
shear stress, heat flux and dissipation in the energy equation with the
Boussinesq approximation and the strong Reynolds analogy, with $Pr_t=1$.
For the high-Mach cases "a detailed analysis showed that $Pr_t\approx1$ in
the buffer layer", and Patel found the same for the low-Mach cases (as
cited). The semi-local damping of their base model is on
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md).

## As working tools in a supersonic LES

[Gao et al. (2022)](/sources/gao-2022.md) use both relations as tools, not
as objects of study, in a high-order DG [implicit LES](/definitions/implicit-les.md)
of a Mach 2 [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
at inlet $Re_\theta=1628$. Their inflow
[synthetic eddy method](/methods/inflow-turbulence-generation.md), the
reformulation of Roidl et al. that they cite, "takes account of the
compressibility effects of high-speed flows by enforcing the strong
Reynolds analogy" (§5.2); the paper prints no formula for it. The undisturbed adiabatic
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md) is
then validated at $x=11\delta_r$, one reference thickness downstream of
the forcing zone ($\delta_r$ the boundary-layer thickness at the
reference station, registry §11), against the DNS of
Wenzel et al. that the authors cite, with the van Driest transformed
velocity and "Morkovin's density scaled Reynolds stress profiles", which
"match each other well" despite the much coarser LES grid (§5.2, Fig. 16).
The scaling formula is not printed; Morkovin scaling serves here only to
compare the LES with a reference DNS of the same layer, not to test the
hypothesis across Mach numbers. The same group repeats the check for the
shock-free layer of their elastic-panel interaction
([Gao et al. (2023)](/sources/gao-2023.md), §5.2, Fig. 18): the van Driest
velocity and the Morkovin density-scaled Reynolds stresses match the DNS of
Wenzel et al. (2018, as cited) at $17\delta_r$ and $35\delta_r$ "despite a
much coarser mesh", with the same synthetic-eddy inflow and an anisotropic
linear forcing zone.

The same use appears in a hypersonic DNS.
[Zhang et al. (2022c)](/sources/zhang-2022-g.md) validate the incoming
flat-plate layer of their Mach 6 swept-ramp interaction (cold isothermal
wall, $T_w=294$ K against the recovery temperature $T_r=585$ K printed with
$r=0.89$, so $T_w/T_r\approx0.50$ *(compiler check, not in the sources)*)
with density-scaled fluctuations written with the **Reynolds** average and
fluctuation (§II C, Eq. 3, after Pirozzoli & Bernardini 2011 as cited),
$$u_i^{\mathrm{sc}}=\frac{\sqrt{\langle\rho\rangle/\rho_w}}{u_\tau}\sqrt{\langle u_i'^2\rangle},\qquad (u_iu_j)^{\mathrm{sc}}=\frac{\langle\rho\rangle/\rho_w}{u_\tau^2}\langle u_i'u_j'\rangle$$
(page-local superscript $\mathrm{sc}$; the source writes a star, which the
registry reserves for semi-local scaling). These are the Morkovin factors
of the first section applied to Reynolds rather than Favre statistics; the
paper does not name Morkovin. The scaled fluctuations at the reference
station are "basically consistent" with other simulations and experiments
(refs. 34–38 of the paper) and show the near-wall anisotropy (Fig. 6b);
the van Driest-transformed mean velocity of the same station is on
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md).

## Qualifications

- Helm & Martín (2022) print the friction velocity with the edge density,
  $u_\tau=(\tau_w/\rho_e)^{1/2}$, and the recovery temperature without the
  factor $T_e$; the relations above do not depend on these choices. Their
  §IV E attributes the failure of the SRA magnitude relation to "Eq. (18)",
  the phase relation, where the magnitude relation, their Eq. (19), is
  meant.
- Cogo et al. (2022) and Huang et al. (2022) test the hypothesis on
  zero-pressure-gradient flat-plate boundary layers only; Huang et al. (2022) contrast them with isothermal
  cold-wall channels, where the Trettel–Larsson transformation collapses
  the data that it does not collapse in their boundary layers (§4.1).
- [Aiello et al. (2026)](/sources/aiello-2026.md) write the fitted log
  law with $y^*$ in the text and with $y^+$ in the Fig. 1 caption; the
  value $B=6.0$ is fitted to their entropy-conservative runs. Their
  Table 3 differences are taken relative to their own entropy-conservative
  scheme (Table 3 caption), not to an independent reference.
- **Derivative in the temperature law of Mo et al. (2023).** Their
  Eq. (22) prints
  $\partial\langle T\rangle/\partial\langle u\rangle=2(T_r-T_w)(1-s_{\mathrm{RA}}Pr)\langle u\rangle/u_e^2+2(T_e-T_r)\langle u\rangle/u_e^2$.
  Differentiating their own Eqs. (11)–(12) gives an additional term
  $(T_r-T_w)\,s_{\mathrm{RA}}Pr/u_e$ from the linear part of $f$. The
  second line of Eq. (22), Eq. (23) and the ratio $\Gamma_2$ (Eq. 27)
  inherit the omission *(compiler check, not in the sources)*. The file
  read carries the AIP notice that an erratum to the paper has been
  published; the erratum is not in the file and its content is not known
  here.
- Wei et al. (2023, Eq. 24) print $\rho'/\langle\rho\rangle=+T'/\langle T\rangle$;
  linearizing their own equation of state (Eq. 8), $p=\rho TR_u\sum_sY_s/W_s$, at
  fixed composition with $p'=0$ gives $\rho'/\langle\rho\rangle=-T'/\langle T\rangle$
  *(compiler check, not in the sources; $p'=0$ is not stated by the authors)*.
- Wang & Xu (2024, App. A) attribute the non-proportionality of mean
  temperature and density to "the non-ideal gas law employed", while their
  Eq. (2.5) is Dalton's law for an ideal-gas mixture, in which the mixture
  molar mass varies *(compiler check, not in the sources)*.
- Printed inconsistencies of the two papers that do not bear on these
  scalings (shape factors, Reynolds-number tables) are recorded on their
  Source pages.
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) call the relation of
  Zhang et al. (2014) the "generalized Reynolds analogy" in §3 and the
  "modified strong Reynolds analogy" in the Fig. 5 caption. They compare
  cases at matched $Re_\tau$, so the semi-local $Re_\tau^*$ ranges from 96
  to 20,696 across them (Table 3), a choice they call "a matter of
  controversy" (§2). The value they cite from Hopkins & Inouye (about
  1.1, §3) and the one [Huang et al. (2022)](/sources/huang-2022.md)
  cite from the same work (1.16, §3.2) differ; both are quoted from the
  cited work, not computed, and neither source compares them.

# Citations

- [Cogo et al. (2022)](/sources/cogo-2022.md) — §1 (Morkovin's hypothesis, Reynolds analogies, SRA); §2, Table 1 (Eckert number); §3.1; §4, Eqs. (4.3)–(4.4), Fig. 9 (temperature–velocity relations); §5.1, Eq. (5.1), Fig. 10 (Morkovin scaling); §5.2, Figs. 11–12 (TKE budget); §5.3 (pressure fluctuations).
- [Huang et al. (2022)](/sources/huang-2022.md) — §3.2, Figs. 4, 6, 8 (Reynolds analogy factor, peak stresses, wall pressure); §4.2, Figs. 13–14 (Morkovin and semi-local scaling); §4.3, Eqs. (4.9)–(4.13), Table 5, Figs. 15–18 (temperature relations, SRA, HSRA, $Pr_t$); §4.4, Fig. 19; §5, Figs. 20–21; §6.
- [Chen et al. (2024)](/sources/chen-2024.md) — §1, §3.1, Eqs. (3.1)–(3.2) (Morkovin-scaled stress in the Baldwin–Lomax mixing length; HLPP and Morkovin's hypothesis); §3.3, Eqs. (3.15)–(3.17), Fig. 6 (DNS $Pr_t$, singularity, two-layer temperature); §4, Figs. 7, 11, 13 (a posteriori $Pr_t$ and errors); §5.1; Table 1; App. A, Fig. 15; App. B, Fig. 16.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §1 (restated hypothesis, intrinsic compressibility, Chu–Kovásznay modes); §2.1–2.2 (thermally perfect gas, scalings); §3.3, Table 2 (set-up); §4.1, Fig. 1 (transformed velocity, $\kappa$, $B$); §4.2, Table 3, Figs. 2–3 (scheme dependence of stresses, wall pressure and fluctuations).
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II (Morkovin-scaled DNS initialization); §IV E, Figs. 28–29 (Reynolds analogy factor, QP85 law, $Pr_t$, SRA and modified SRA in separated hypersonic interactions); §V.
- [Gao et al. (2022)](/sources/gao-2022.md) — §5.2, Figs. 16–17 (strong Reynolds analogy in the synthetic-eddy inflow; Morkovin density-scaled Reynolds stresses as a validation of a Mach 2 DG implicit LES).
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §2, Table 1; §3, Eqs. (3.1)–(3.3), Table 3, Figs. 4–5, 8 (Morkovin density scaling, Walz and generalized Reynolds analogy, Reynolds analogy factor, turbulent Mach number under wall cooling, Mach 0.5–8); §4, Figs. 10–12; §5, Fig. 13 (wall-pressure fluctuations); §7.
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §1.2 (Morkovin-based spectral formulation rejected near shocks); §2.1 (generalized Reynolds analogy at the inflow).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §2.1 (strong Reynolds analogy for inflow thermodynamic fluctuations).
- [Mo et al. (2023)](/sources/mo-2023.md) — §II B, Eqs. (11)–(13) (GRA); §III B, Eqs. (15)–(19) (Morkovin velocity scaling, SRA laws, validity limits of Duan et al. as cited); §IV A, Eqs. (20)–(25) (GSRA, new temperature and density laws); §IV B, Eqs. (26)–(27), Figs. 10, 15–17 (a posteriori tests at Mach 7.25).
- [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) — §2.1–2.2 (Morkovin's hypothesis for variable-property channels, SRA, $Pr_t=1$).
- [Gao et al. (2023)](/sources/gao-2023.md) — §5.2, Fig. 18 (Morkovin-scaled stresses against DNS in a DG implicit LES).
- [Zhang et al. (2022c)](/sources/zhang-2022-g.md) — §II B (free-stream and wall temperatures, recovery factor); §II C, Eq. (3), Fig. 6b (density-scaled Reynolds-averaged fluctuations at the inflow station of a Mach 6 DNS).
- [Bose & Park (2018)](/sources/bose-2018.md) — §2.5, Eq. (17) (equilibrium thermal wall model, strong Reynolds analogy $C_h=C_f/2$, its range and failure near separation); §4.4 (Morkovin-type scaling of closures for $M_t\lesssim0.2$).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §4.5 (early compressible DNS; Coleman et al. 1995 as cited).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §III, Fig. 5 (Morkovin-scaled intensities of the incoming Mach 2.9 layer).
- [Tang et al. (2024)](/sources/tang-2024.md) — §2.3, Fig. 12; §3; §4.1, Fig. 21 (Morkovin scaling; Reynolds-analogy factor through a Mach 5 ramp interaction).
- [Wang & Xu (2024)](/sources/wang-2024-h.md) — §5.2; §5.4, Eqs. (5.4)–(5.6), Figs. 20–22; App. A (SRA and extensions, coherence, $Pr_t$).
- [Wei et al. (2023)](/sources/wei-2023.md) — §II D, Eq. (24); §III B, Fig. 11; §IV F.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §1; §3.1, Eq. (3.3), Fig. 5b.
