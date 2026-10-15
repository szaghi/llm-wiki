---
type: Result
title: "Plasma drag augmentation of a magnetized body"
description: "A body carrying its own dipole field in a hypersonic rarefied plasma flow has a drag coefficient that grows with the ratio of surface magnetic pressure to dynamic pressure and falls with the field–flow angle, by empirical laws measured on a magnetized sphere; a plasma jet injected into its mini-magnetosphere multiplies the drag by 2.7–3.8 depending on orientation, and the source's extrapolation to the ionosphere puts a 0.6–0.8 T body field near the drag pressure of two of the four ion-beam-shepherd beams it quotes."
status: established
aliases: [magnetic drag augmentation, Lorentz drag of a magnetized spacecraft, mini-magnetosphere drag]
tags: [plasma-spacecraft-interaction, magnetic-field, drag]
timestamp: 2026-10-15T00:00:00Z
---

# Plasma drag augmentation of a magnetized body

[Shuvalov et al. (2018)](/sources/shuvalov-2018.md) measured, in a
laboratory hypersonic rarefied nitrogen plasma beam, the drag on teflon
spheres of radius $r_w=4.35\times10^{-2}$ m and $5.25\times10^{-2}$ m that
carry an internal solenoid, so that the field outside the sphere is a
dipole. Flow speeds were 11.5, 15.6 and 28.3 km/s, ion densities
$2.1\times10^{15}$–$9.6\times10^{15}$ m$^{-3}$, $T_e\approx2.6$ eV, dynamic
pressures $p_{\mathrm{dyn}}=8\times10^{-3}$–$1.3\times10^{-1}$ Pa, and the
surface field $B_w$ from $8\times10^{-3}$ T to about $2\times10^{-1}$ T;
the authors state that these similarity parameters (Mach number 3.6–8.9,
magnetic Reynolds number 1.6–6.2, ion Knudsen number 12–15) are close to
or correspond to those of an unmagnetized spacecraft of radius 0.5–1 m at
about 800 km (ionosphere: Mach 5.3–7.5, $\mathrm{Re}_m>1$). Forces were measured with two microbalances
(±4.5% and ±3%). The laws below are empirical fits to these measurements;
none is derived from a model of the flow.

## Statement

**Unmagnetized reference.** For collisionless hypersonic flow about a
sphere $C_{D0}\approx2.0$, with $C_D$ referred to the sphere
cross-section and $p_{\mathrm{dyn}}=\tfrac12 m_in_iu_i^2$ (attributed by the
source to its ref. [20]). The drag of a charged, unmagnetized sphere adds
a Coulomb component that vanishes for $r_w/\lambda_D>50$ (attributed to
its ref. [18]).

**Field aligned with the flow** (Eq. 1, Fig. 3). Over
$3\times10^1\le p_{Bw}/p_{\mathrm{dyn}}\le2\times10^5$, with
$p_{Bw}=B_w^2/(2\mu_0)$,
$$\frac{C_D}{C_{D0}}=\exp\left[5.85\times10^{-2}\left(\log_{10}\frac{p_{Bw}}{p_{\mathrm{dyn}}}\right)^2\right].$$
The ratio rises from about 1.1 at $p_{Bw}/p_{\mathrm{dyn}}=5\times10^1$
to about 4.8 near $10^5$ (read from Fig. 3; Eq. 1 itself gives 1.18 and
4.32). The fit is drawn through three
measured data sets and five literature calculations; no uncertainty is
given for the coefficient $5.85\times10^{-2}$.

**Dependence on the field–flow angle** (Eq. 2, Fig. 4). At
$p_{Bw}/p_{\mathrm{dyn}}\approx2.5\times10^4$, $C_D$ divided by its
aligned-field value is fitted by a trigonometric function of the angle
between $\mathbf B$ at the surface and the flow velocity, printed on the
[Source page](/sources/shuvalov-2018.md) (claim 3). It equals 1 for the
aligned field and 0.653 for the field perpendicular to the flow. The
general law is the product of the two factors (Eq. 3). Literature numerics
quoted in Fig. 4 lie below the fit at large angle (about 0.58 at 90°) or
above it (about 0.72), read from the figure.

**Field perpendicular to the flow: mini-magnetosphere** (Eqs. 4–6,
Table 2). The sphere then stands off the flow behind an artificial
mini-magnetosphere. Balancing the doubled dipole field at the magnetopause,
$(2B)^2/(2\mu_0)$, against the stagnation pressure $2p_{\mathrm{dyn}}$, for
an equatorial dipole whose surface field is $B_w$, gives the standoff
distance
$$L_{\mathrm{so}}=r_w\left(\frac{2p_{Bw}}{p_{\mathrm{dyn}}}\right)^{1/6}.$$
The measured perpendicular-field drag, $C_D$ = 2.7–4.2 for
$L_{\mathrm{so}}/r_w$ = 4.3–5.9, is fitted within 7% by
$$\frac{C_D}{C_{D0}}\approx(0.653\pm0.08)\,\exp\left[5.85\times10^{-2}\left(\log_{10}\left(\tfrac12\left(\frac{L_{\mathrm{so}}}{r_w}\right)^6\right)\right)^2\right],$$
which, since $\tfrac12(L_{\mathrm{so}}/r_w)^6=p_{Bw}/p_{\mathrm{dyn}}$, is the
aligned-field law times the perpendicular value 0.653 of the angular
factor. Against magnetic-sail simulations from the literature (Table 2):
measured 3.2±0.4 at $L_{\mathrm{so}}/r_w=5.0$ against computed 3.2±0.4
and 2.9 (ref. [5]) and 3.4±0.7 (ref. [6]); measured 3.89±0.25 at 5.874
against 3.813 (ref. [22]). The source calls the agreement "quite satisfactory".

**Interaction regime** (§4). At $L_{\mathrm{so}}/r_w\approx4.6$,
28.3 km/s, $n_i\approx9.6\times10^{15}$ m$^{-3}$ and
$B_w\approx3.9\times10^{-2}$ T, the inertial magnetopause thickness
$c/\omega_{pe}\approx5.7\times10^{-2}$ m is about 0.2 $L_{\mathrm{so}}$,
the inverse magnetic Reynolds number at the boundary about
$2\times10^{-2}$, the thermal-ion Larmor radius about 2.4
$L_{\mathrm{so}}$, the flow-ion Larmor radius about 7 m, and the ion–ion
$\mathrm{Kn}\approx2.6$. The source places this in a regime transitional
between MHD and kinetic, in which the Lorentz interaction predominates;
the classification is attributed to Fujita (its ref. [6]), not shown.

**Plasma-jet injection** (Eqs. 7–8, Table 3). A subsonic plasma jet,
produced by electron-heated pyrolysis of an epoxy layer at the frontal
point and ionized by the beam electrons, injected into the
mini-magnetosphere cavity adds the Lorentz force of the injected current
to the magnetic drag. With an injected current of about 1.6 A, closed on a
metal diaphragm element of radius $10^{-2}$ m, at $L_{\mathrm{so}}/r_w\approx5.0$, the measured ratio
of total to non-injected drag force is $3.81\pm0.2$, against 3.72 from
the source's formula (which uses the field at the boundary taken as
$2B_w(r_w/L_{\mathrm{so}})^3$; the $B_w$ printed in §5,
$3.9\times10^{-3}$ T, is a misprint: $3.9\times10^{-2}$ T reproduces 3.72
with the larger sphere; see the [Source page](/sources/shuvalov-2018.md),
Recorded as printed). The
injection factor is multiplicative on $C_D$ and decreases as the jet turns
from antiparallel to perpendicular to the flow (Table 3: 3.81 down to
2.56). The two combined cases measured are $C_D\approx12.2\pm1.4$
(perpendicular field, $C_D=3.2\pm0.2$ times factor $3.81\pm0.2$) and
$C_D\approx13.0\pm1.64$ (aligned field,
$p_{Bw}/p_{\mathrm{dyn}}=7.81\times10^3$, $C_D=4.85\pm0.25$ times factor
$2.68\pm0.15$): about six times $C_{D0}$. The jet's own reactive force is
neglected.

## Deorbiting estimate

Inserting ionospheric plasma parameters (medium solar activity, from the
source's refs. [12,33]) in the combined empirical law, the source
calculates the drag pressure $C_D\,p_{\mathrm{dyn}}$ on a magnetized
spacecraft at 700 km for $B_w$ = 0.1–3 T (Fig. 8), and at 250–800 km for
$B_w=0.8$ T (Fig. 9, about 1–5 mN/m$^2$, read). It compares these with
four [ion-beam-shepherd](/definitions/ion-beam-shepherd.md) beam pressures
from the literature: 8.43 and 4.04 mN/m$^2$ for a 3.5 keV Xe$^+$ beam at
7 m and 10 m (LEOSWEEP), 5.78 and 1.44 mN/m$^2$ for a 6 keV beam at 20 m
for the two beam angles printed (about 3° and 6°). The source states that
a body field of 0.6–0.8 T gives a drag pressure close to that of the
3.5 keV beam at 10 m (4.04 mN/m$^2$) and of the 6 keV beam of divergence half-angle about 6° at 20 m
(1.44 mN/m$^2$), citing the 250–800 km scan of Fig. 9; in its own Fig. 8
(700 km) the 0.6–0.8 T range matches only the latter, and the 7 m LEOSWEEP
value (8.43 mN/m$^2$) needs about 2.6 T. The neutral drag at 700–800 km, computed with
$C_{D0}=2.0$ and fully diffuse reflection (see
[gas–surface interaction](/methods/gas-surface-interaction.md)), is stated
to be nearly three orders of magnitude smaller. The source proposes a
"sleeping magnet" fitted before launch and unshielded at end of life, or a
magnetic "harpoon" attached by a servicer. This estimate is an
extrapolation of laboratory fits, not a measurement, and the ionospheric
parameters behind it are not tabulated.

## Limits

* One laboratory, one gas (N$_2$, mean ion mass 19.6 amu), spheres of two
  radii; all laws are empirical fits with stated ranges, and the angular
  law was measured at a single pressure ratio.
* The perpendicular-field fit reaches 7.7% error at $L_{\mathrm{so}}/r_w=5.9$,
  the edge of its stated 7%.
* The quoted magnetic-moment range (1.1–7.2 A·m$^2$) is not consistent
  with the quoted surface fields for a centred dipole in SI units; the
  source does not resolve it ([Source page](/sources/shuvalov-2018.md),
  Recorded as printed). The fits are in $p_{Bw}/p_{\mathrm{dyn}}$ and
  $L_{\mathrm{so}}/r_w$, which do not involve the moment.
* The Fig. 8 comparison values printed in the text and the plotted markers
  differ by a factor of about 1.3–1.5 (reader's reading of a log axis).

# Citations

1. [Shuvalov et al. (2018)](/sources/shuvalov-2018.md) — §2–§6, Eqs. 1–8, Tables 1–3, Figs. 2–4, 7–9.
