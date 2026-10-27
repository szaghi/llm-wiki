---
type: Definition
title: "Morkovin's hypothesis and Reynolds analogies"
description: "Morkovin's hypothesis holds that, while density fluctuations stay small, compressible wall turbulence behaves like incompressible turbulence once mean property variations are scaled out; this page gives Morkovin scaling, the strong Reynolds analogy, the turbulent Prandtl number, and where DNS to Mach 14, thermally perfect channel DNS and separated-flow LES confirm or break them."
status: established
aliases: [Morkovin hypothesis, Morkovin scaling, Morkovin's scaling, strong Reynolds analogy, SRA, HSRA, Reynolds analogy factor, turbulent Prandtl number]
tags: [compressible, boundary-layer, dns, hypersonic, rans]
timestamp: 2026-10-26T20:49:00Z
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
  $Pr_t=1-\tfrac14(y/\delta)$ recalled by Huang et al. (2022) gives 0.75 at
  the edge, the value Helm & Martín find there *(compiler check, not in the
  sources)*.
- **SRA phase relation.** $-R_{u''T''}$ falls upstream from 0.85 at
  $y/\delta_x=0.05$ to 0.6 at the edge and changes sign at the cold wall; it
  is about 0.5 in the Mach 9 downstream layer (Fig. 29b). Helm & Martín
  recall about 0.6 through most of adiabatic layers up to edge Mach 12 (Duan
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
$$\langle T\rangle_\rho=T_w+C_T(T_r-T_w)\Big(1-\frac{\langle u\rangle_\rho}{U_{\mathrm m}}\Big)\frac{\langle u\rangle_\rho}{U_\delta}+(T_{\mathrm m}-T_w)\Big(\frac{\langle u\rangle_\rho}{U_{\mathrm m}}\Big)^2,\qquad y<y_{\mathrm{mT}},$$
(Eq. 3.17; page-local: $U_{\mathrm m}$, $T_{\mathrm m}$ the mean velocity
and temperature at $y_{\mathrm{mT}}$, $U_\delta$ the edge velocity, $C_T$ the
relation's constant), with $C_T=0.8259$ (Duan & Martín), recast by Zhang et
al. as $sPr$ with the Reynolds analogy factor $s=1.14$, and the recovery
factor $r=Pr^{1/3}$ (§3.3, Eq. 3.16; Cogo et al. and Huang et al. take
$r=0.89$). This is one of the quadratic relations of the
"Mean temperature" section, written in two-layer form after Griffin et
al. (as recalled), and results change little for $y^*_{\mathrm{mT}}$ from
50 to 150 (App. A, Fig. 15). The value $s=1.14$ lies inside the range
$1.1<R_{af}<1.2$ that Huang et al. (2022) measure for $2C_h/C_f$
*(compiler check, not in the sources; Chen et al. do not print the
definition of $s$)*.

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
questioning the hypothesis (above), so the two sources agree on where the
current challenge comes from. Aiello et al. add that the Chu–Kovásznay split
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
- Printed inconsistencies of the two papers that do not bear on these
  scalings (shape factors, Reynolds-number tables) are recorded on their
  Source pages.

# Citations

- [Cogo et al. (2022)](/sources/cogo-2022.md) — §1 (Morkovin's hypothesis, Reynolds analogies, SRA); §2, Table 1 (Eckert number); §3.1; §4, Eqs. (4.3)–(4.4), Fig. 9 (temperature–velocity relations); §5.1, Eq. (5.1), Fig. 10 (Morkovin scaling); §5.2, Figs. 11–12 (TKE budget); §5.3 (pressure fluctuations).
- [Huang et al. (2022)](/sources/huang-2022.md) — §3.2, Figs. 4, 6, 8 (Reynolds analogy factor, peak stresses, wall pressure); §4.2, Figs. 13–14 (Morkovin and semi-local scaling); §4.3, Eqs. (4.9)–(4.13), Table 5, Figs. 15–18 (temperature relations, SRA, HSRA, $Pr_t$); §4.4, Fig. 19; §5, Figs. 20–21; §6.
- [Chen et al. (2024)](/sources/chen-2024.md) — §1, §3.1, Eqs. (3.1)–(3.2) (Morkovin-scaled stress in the Baldwin–Lomax mixing length; HLPP and Morkovin's hypothesis); §3.3, Eqs. (3.15)–(3.17), Fig. 6 (DNS $Pr_t$, singularity, two-layer temperature); §4, Figs. 7, 11, 13 (a posteriori $Pr_t$ and errors); §5.1; Table 1; App. A, Fig. 15; App. B, Fig. 16.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §1 (restated hypothesis, intrinsic compressibility, Chu–Kovásznay modes); §2.1–2.2 (thermally perfect gas, scalings); §3.3, Table 2 (set-up); §4.1, Fig. 1 (transformed velocity, $\kappa$, $B$); §4.2, Table 3, Figs. 2–3 (scheme dependence of stresses, wall pressure and fluctuations).
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II (Morkovin-scaled DNS initialization); §IV E, Figs. 28–29 (Reynolds analogy factor, QP85 law, $Pr_t$, SRA and modified SRA in separated hypersonic interactions); §V.
