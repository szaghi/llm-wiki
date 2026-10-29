---
type: Result
title: "Exact laws of (Hall-)MHD turbulence"
description: "Exact laws relate the energy cascade rate of MHD turbulence to two-point increments under statistical homogeneity; the page gives the reduced-MHD third-order law and the compressible Hall-MHD laws, their general non-stationary form, and DNS evidence that two such laws agree and survive decaying turbulence."
status: established
aliases: [exact law, third-order law, Politano–Pouquet law, Kolmogorov–Yaglom law, energy cascade rate, A18 law, F21 law, compressible Hall MHD exact law]
tags: [mhd, plasma, astrophysics, dns, compressible]
timestamp: 2026-10-29T07:40:00Z
---

# Exact laws of (Hall-)MHD turbulence

An **exact law** of turbulence expresses the rate $\varepsilon$ at which
energy flows to small scales — the cascade rate, equal to the dissipation
rate in a statistically steady state — through averages of two-point
increments or correlators at separation $\boldsymbol l$, without any closure
model. [Ferrand et al. (2022)](/sources/ferrand-2022.md) (§1) state the
derivation: statistical homogeneity alone gives a general equation, and
adding time stationarity, forcing restricted to the largest scales and
infinite kinetic and magnetic Reynolds numbers gives the stationary
inertial-range form, which they describe as the one generally used "in
numerical simulations and spacecraft data to infer the cascade rate"
(§2.1, p. 3); exact laws need no closure model (§1). The bundle meets them
in two settings, [reduced MHD](/definitions/reduced-mhd.md)
and compressible Hall MHD.

Page-local notation: $\boldsymbol l$ is the separation (the source writes
$\boldsymbol\ell$); for any field $\phi$, $\phi^\dagger=\phi(\boldsymbol r+\boldsymbol l)$
is its value at the second point (the source writes a prime, which the
registry reserves for the Reynolds fluctuation),
$\delta\phi=\phi^\dagger-\phi$ the increment and
$\{\!\{\phi\}\!\}=\tfrac12(\phi+\phi^\dagger)$ the two-point mean (the
registry's mean of two states; the source writes $\bar\delta\phi$);
$\nabla_l$ is the gradient with respect to $\boldsymbol l$, and homogeneity
gives $\langle\nabla^\dagger\cdot(\cdot)\rangle=-\langle\nabla\cdot(\cdot)\rangle=\nabla_l\cdot\langle\cdot\rangle$.
$\langle\cdot\rangle$ is an ensemble average, computed as a volume average.

## The reduced-MHD third-order law

For the Elsasser fields of [reduced MHD](/definitions/reduced-mhd.md),
[Schekochihin (2022)](/sources/schekochihin-2022.md) (§3, Eq. 3.7) records
the exact law

$$\langle\delta Z^\mp_L\,|\delta\boldsymbol Z^\pm_\lambda|^2\rangle=-2\varepsilon^\pm\lambda,$$

with $\delta Z_L$ the longitudinal increment, $\lambda$ the perpendicular
separation and $\varepsilon^\pm$ the Elsasser cascade rates; the review
cites it as derived for isotropic MHD by Politano & Pouquet (1998) and adapted to
RMHD by Boldyrev et al. (2009), with the derivation sketched in the review's
footnote 9. The review lists it among the properties of RMHD that every
scaling theory must satisfy, and uses it as a consistency check on
[dynamic alignment](/properties/dynamic-alignment.md) (footnote 19).

## Compressible Hall MHD

Ferrand et al. (2022, §2.1, Eqs. 1–6) write isothermal compressible Hall MHD
(CHMHD) in SI form:

$$\begin{aligned}
&\partial_t\rho+\nabla\cdot(\rho\boldsymbol u)=0,\qquad \rho(\partial_t\boldsymbol u+\boldsymbol u\cdot\nabla\boldsymbol u)=-\nabla p+\boldsymbol J\times\boldsymbol B+\boldsymbol d_\nu+\boldsymbol f,\\
&\partial_t\boldsymbol B=\nabla\times(\boldsymbol u\times\boldsymbol B)-\alpha_H\nabla\times\!\left(\frac{\boldsymbol J}{\rho}\times\boldsymbol B\right)+\boldsymbol d_\eta,\qquad \nabla\cdot\boldsymbol B=0,
\end{aligned}$$

with $\boldsymbol J=\nabla\times\boldsymbol B/\mu_0$, the Hall coefficient
$\alpha_H=m_i/q_e$ (registry §11; the source writes $\lambda$, which the
registry uses for the perpendicular scale), the ion inertial length
$d_i=\alpha_H/\sqrt{\mu_0\rho}$, the dissipative terms
$\boldsymbol d_\nu=\nu\nabla^2\boldsymbol u+\tfrac{\nu}{3}\nabla(\nabla\cdot\boldsymbol u)$ and
$\boldsymbol d_\eta=\eta_m\nabla^2\boldsymbol B$ (page-local), a large-scale
forcing $\boldsymbol f$, and the isothermal closure $p=c_s^2\rho$ ($c_s$
the sound speed). Let $\boldsymbol j=\boldsymbol J/\rho$ (page-local; the
source writes $\boldsymbol J_c$) and $e_{\mathrm{int}}$ the internal energy
per unit mass (page-local), so that the total energy density is
$E^{\mathrm{tot}}=\rho|\boldsymbol u|^2/2+|\boldsymbol B|^2/(2\mu_0)+\rho e_{\mathrm{int}}$.

### The F21 law

The law of Ferrand et al. (2021a), as restated in Ferrand et al. (2022,
§2.1), is built on the modified second-order structure function (Eq. 7)

$$\langle S_2\rangle=\left\langle\tfrac12\{\!\{\rho\}\!\}|\delta\boldsymbol u|^2+\frac{1}{2\mu_0}|\delta\boldsymbol B|^2+\tfrac12\delta\rho\,\delta e_{\mathrm{int}}\right\rangle$$

($S_2$ page-local; the registry's $S$ is the strain rate). With stationarity,
large-scale forcing and infinite Reynolds numbers it reads (Eq. 9)

$$\begin{aligned}
-4\varepsilon_{F21}=\ &\nabla_l\cdot\left\langle\{\!\{\rho\}\!\}|\delta\boldsymbol u|^2\delta\boldsymbol u+\frac{1}{\mu_0}|\delta\boldsymbol B|^2\delta\boldsymbol u-\frac{2}{\mu_0}(\delta\boldsymbol u\cdot\delta\boldsymbol B)\delta\boldsymbol B\right\rangle\\
&-\tfrac12\left\langle\left(\rho\,\nabla^\dagger\!\cdot\boldsymbol u^\dagger+\rho^\dagger\,\nabla\cdot\boldsymbol u\right)|\delta\boldsymbol u|^2\right\rangle+2\left\langle\delta\rho\,\delta\boldsymbol u\cdot\{\!\{\boldsymbol j\times\boldsymbol B\}\!\}\right\rangle\\
&+\frac{\alpha_H}{\mu_0}\nabla_l\cdot\left\langle2(\delta\boldsymbol B\cdot\delta\boldsymbol j)\delta\boldsymbol B-|\delta\boldsymbol B|^2\delta\boldsymbol j\right\rangle-2\alpha_H\left\langle\delta(\boldsymbol J\times\boldsymbol B)\cdot\delta\boldsymbol j\right\rangle .
\end{aligned}$$

The first line is the flux term of incompressible MHD; the second line
carries the compressible source terms (dilatation and density increments);
the third line, proportional to $\alpha_H$, is the Hall part. The split
$\varepsilon=\varepsilon_{\mathrm{MHD}}+\varepsilon_{\mathrm{Hall}}$ assigns
to $\varepsilon_{\mathrm{Hall}}$ all terms with the factor $\alpha_H$ (§4).

### The A18 law

The law of Andrés et al. (2018), labelled A18 by Ferrand et al. (2022, §2.2,
Eq. 20), is written instead with the local Alfvén velocity
$\boldsymbol v_A=\boldsymbol B/\sqrt{\mu_0\rho}$ (page-local vector; the
registry's $v_A$ is the scalar of the mean field) and the two-point energy
correlator $R_E=\tfrac{\rho}{2}(\boldsymbol u\cdot\boldsymbol u^\dagger+\boldsymbol v_A\cdot\boldsymbol v_A^\dagger)+\rho e_{\mathrm{int}}^\dagger$
(page-local), with cross-helicity and magnetic correlators and many source
terms; it is not reproduced here. Ferrand et al. cite "Andrés et al. (2018)"
without a suffix while their reference list holds two 2018 papers by Andrés
and coauthors, so which of the two carries the A18 law cannot be decided from
the citing paper.

### General, non-stationary form

The contribution of Ferrand et al. (2022, §2) is to keep the time
derivatives, the dissipation and the forcing, so that the only hypothesis is
statistical homogeneity:

$$\begin{aligned}
&2\varepsilon_{F21}+\partial_t\langle E^{\mathrm{tot}}\rangle-\partial_t\langle S_2\rangle+\mathcal D_{F21}+\mathcal D^{\mathrm{loc}}_{F21}+\mathcal F_{F21}+\mathcal F^{\mathrm{loc}}_{F21}=0,\\
&2\varepsilon_{A18}+\partial_t\langle R_E+R_E^\dagger\rangle+\mathcal D_{A18}+\mathcal F_{A18}=0
\end{aligned}$$

(Eqs. 10, 21), with $\mathcal D$ and $\mathcal F$ (page-local) the two-point
dissipative and forcing terms and "loc" the products taken at a single
point (Eqs. 11–14). In Eq. (10), $\varepsilon_{F21}$ is defined by
identification with the right-hand side of Eq. (9), so the equation "remains
very general" (§2.1). The authors derive the A18 dissipative and forcing
terms, which Andrés et al. (2018) did not write out (Eqs. 22–25); the
forcing terms of the two laws coincide, $\mathcal F_{A18}=\mathcal F_{F21}$:

$$\mathcal F_{F21}=-\tfrac12\left\langle\left(1+\frac{\rho^\dagger}{\rho}\right)\boldsymbol u^\dagger\cdot\boldsymbol f+\left(1+\frac{\rho}{\rho^\dagger}\right)\boldsymbol u\cdot\boldsymbol f^\dagger\right\rangle$$

(Eqs. 13, 25). For free decay ($\boldsymbol f=0$) the balances become
(Eqs. 29–30)

$$2\varepsilon_{F21}+\partial_t\langle E^{\mathrm{tot}}\rangle-\partial_t\langle S_2\rangle+\mathcal D_{F21}+\mathcal D^{\mathrm{loc}}_{F21}=0,\qquad 2\varepsilon_{A18}+\partial_t\langle R_E+R_E^\dagger\rangle+\mathcal D_{A18}=0,$$

with two limits for A18 (§5.1): at large and intermediate scales, where the
dissipative term is negligible, $2\varepsilon_{A18}+\partial_t\langle R_E+R_E^\dagger\rangle=0$
(Eq. 33); at small scales $R_E+R_E^\dagger\to2E^{\mathrm{tot}}$, giving
$2\varepsilon_{A18}+2\partial_t\langle E^{\mathrm{tot}}\rangle+\mathcal D_{A18}=0$
(Eq. 34).

## Numerical evaluation

Ferrand et al. (2022, §3) evaluate both laws term by term on three $1024^3$
pseudo-spectral DNS of freely decaying isothermal CHMHD with the GHOST code
(periodic box $L_0=2\pi$, $\nu=\eta_m=3\times10^{-4}$, i.e.
$Re=Rm\simeq3\times10^3$, $d_i=0.02L_0$, initial random-phase modes in the
shell $1\le k\le3$; Table 1): Run I with mean field $B_0=2$ and initial sonic
Mach number $0.25$, Run II with $B_0=0$ and $0.25$, Run III with $B_0=0$ and
$0.5$; plus Run I-512 at $512^3$, $\nu=\eta_m=8\times10^{-4}$ and a larger
$d_i$ (see Qualifications). See also [compressible MHD
turbulence](/results/compressible-mhd-turbulence.md) and [decaying MHD
turbulence](/results/decaying-mhd-turbulence.md).

- **Increment-space divergence.** Increments are integer multiples of 73
  lattice base vectors joining grid points (the decomposition the authors cite
  from Taylor, Kurien & Eyink 2003), so no interpolation is needed; under
  isotropy $\nabla_l\cdot\langle\boldsymbol F\rangle=l^{-2}\partial_l[l^2\langle F_l\rangle(l)]$,
  the radial projection averaged over the 73 directions (§3.2, Eqs. 26–28;
  $\boldsymbol F$ a flux vector, page-local). An axisymmetric variant with
  the 57 directions at $\ge45^\circ$ from $\boldsymbol B_0$, keeping only the
  perpendicular flux, matched the two laws less well even for Run I; the
  authors advise choosing "on a case-by-case basis" (Appendix, Fig. 10).
- **Time derivatives** by a five-point stencil over snapshots: 11 snapshots
  between 8 and 9 turnover times for Run I, five around 5.4 and 5.7 for
  Runs II and III (§3.3, Eq. 31).
- **Equivalence of the two laws.** A18 and F21 give "closely similar
  components (MHD and Hall) of the cascade rate nearly at all scales", which
  the authors present as numerical validation of their inertial-range
  equivalence (§4, Fig. 3); a mathematical proof is lacking, whereas it
  exists for the incompressible Hall-MHD laws (the authors cite Ferrand et
  al. 2019; §6).
- **Cascade rate against decay rate.** The inertial-range rate, centred
  around $l/d_i\simeq2$, roughly matches the energy decay rate from a linear
  fit, $\approx0.047$ (Run I) and $\approx0.087$ (Runs II–III) in code units
  (§3.1, §4).
- **Mach number.** Raising the initial sonic Mach number from 0.25 to 0.5
  "does not bring significant changes", in agreement with Andrés et al.
  (2018) up to 0.5; supersonic flows can develop a dominant compressible
  cascade component (the authors cite Ferrand et al. 2020; §4, Fig. 4).
- **Hall range.** The Hall component never dominates the MHD one at sub-ion
  scales, "in contrast with" the CGL-closure simulations of Ferrand et al.
  (2021b) that they cite; the authors attribute it to dissipation acting
  before the Hall range develops. Run I-512 strengthens the Hall electric
  field at small scales (Fig. 5) but brings "little enhancement" of the Hall
  cascade (Fig. 7). The magnetic spectrum of Run I scales as $k^{-5/3}$ over
  $kd_i\in[0.1,0.7]$ and shows no clear $k^{-7/3}$ range below the ion scale
  (Fig. 6). Raising $d_i$ further is impractical because whistler dispersion
  limits the explicit time step roughly as $(dx)^2/(d_iB)$; the authors
  recommend hyperviscosity and hyperdiffusivity instead (§4).
- **Closure of the general laws.** In all three runs the sum of all terms
  of Eq. (30) lies 1 to 1.5 orders of magnitude below the individual terms
  (§5.1, Fig. 8). The large-scale limit (33) holds for Runs II and III but
  not for Run I, whose residual rises at large scales — "the reason for this
  odd behavior is not fully understood yet"; the small-scale limit (34) holds
  in all runs. The F21 balance (29) "still perfectly holds for Run I", which
  the authors say "may suggest" that it is the more robust form (§5.2,
  Fig. 9).

## Exact laws in decaying turbulence

Free decay breaks the stationarity assumed by Eq. (9). Ferrand et al. (2022,
§5–§6) find that the time-derivative terms, $-\partial_t\langle R_E+R_E^\dagger\rangle$
for A18 and $-\partial_t\langle S_2\rangle$ for F21, act as a scale-dependent
energy "reservoir" that replaces the large-scale forcing and is split
between the cascade ($\varepsilon$) and dissipation; at large scales the
dissipative term vanishes and nearly all of it feeds the cascade (Eq. 35).
They conclude that the stationary inertial-range form remains valid in
decaying turbulence, for instance in the solar wind far from the Sun (§6),
and that the reservoir "overall coincides with the energy dissipation rate",
suggesting that the cascading energy is "ultimately bound to be fully
dissipated" (§6).

## Qualifications

- **Evidence base.** The decaying-turbulence conclusion rests on three
  subsonic runs at $Re\simeq3\times10^3$, each analysed over one time
  window, and Run I's large-scale A18 balance fails without explanation; the
  extension to the solar wind is the authors' statement. The isotropic
  increment averaging was preferred even with $B_0=2$, and the appendix
  concedes that this may not hold for stronger mean fields.
- **Printed slips** (arXiv v1). §4 gives Run I-512 "an ion inertial length
  $d_i=0.05/L_0$", dimensionally a length only as $0.05L_0$ (Table 1 lists
  $d_i/L_0$). *(Compiler check, not in the sources: with
  $\boldsymbol v_A=\boldsymbol B/\sqrt{\mu_0\rho}$ and $\boldsymbol d_\eta=\eta_m\nabla^2\boldsymbol B$
  as defined in Eq. 6, each left-hand term of Eq. 23, e.g.
  $\rho\boldsymbol v_A\cdot\boldsymbol d_\eta^\dagger/\sqrt{\rho^\dagger}=\sqrt{\rho/\rho^\dagger}\,\boldsymbol B\cdot\boldsymbol d_\eta^\dagger/\sqrt{\mu_0}$,
  carries $1/\sqrt{\mu_0}$, while the right-hand side prints $1/(2\mu_0)$.
  The right-hand side and Eq. 24 follow if the resistive term of the
  $\boldsymbol v_A$ equation, Eq. 17, is $\boldsymbol d_\eta/\sqrt{\mu_0\rho}$,
  which is what $\partial_t(\boldsymbol B/\sqrt{\mu_0\rho})$ gives; Eq. 17 and
  the left side of Eq. 23 print $\boldsymbol d_\eta/\sqrt\rho$; with
  $\boldsymbol d_\eta/\sqrt{\mu_0\rho}$ the printed $\mathcal D_{A18}$ of
  Eq. 24 follows.)*
- **Viscosity.** On this page $\nu$ is the source's coefficient, which it
  calls "the dynamic viscosity" (§2.1) and places in the
  $\rho$-weighted momentum equation (Eq. 2); the Alfvén-speed form (Eq. 16)
  adds $\boldsymbol d_\nu$ to $\partial_t\boldsymbol u$ without a factor
  $1/\rho$, and §3.1 sets $Re=1/\nu$ "due to the normalization of the
  variables".
- Ferrand et al. (§1) state that exact laws need no closure model; neither
  source uses them as a subgrid model.

# Citations

- [Ferrand et al. (2022)](/sources/ferrand-2022.md) — §1; §2.1, Eqs. (1)–(14); §2.2, Eqs. (15)–(25); §3.1, Table 1, Figs. 1–2; §3.2, Eqs. (26)–(28); §3.3, Eq. (31); §4, Figs. 3–7, Eq. (32); §5.1–§5.2, Eqs. (29)–(30), (33)–(35), Figs. 8–9; §6; Appendix, Eqs. (36)–(37), Fig. 10.
- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §3, Eq. (3.7); footnotes 9, 19.
