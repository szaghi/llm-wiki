---
type: Source
title: "Wang, Butcher & Lovell (2018) — Ambiguous relative orbits in sequential relative orbit estimation with range-only measurements"
description: "Derives, for Hill–Clohessy–Wiltshire relative motion, the conditions under which different relative orbits share the same range history (three mirror, up to four deformed, and infinitely many central ambiguous orbits), examines local observability with Lie derivatives, and shows with an extended Kalman filter that the ambiguities appear in estimation and persist under small eccentricity and J2."
resource: "doi:10.1016/j.actaastro.2018.04.057"
source_kind: paper
authors: [Wang J., Butcher E.A., Lovell T.A.]
year: 2018
venue: "Acta Astronaut. 151:626–644"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Ambiguous_relative_orbits_in_sequential_relative_orbit_estim.pdf"
tags: [context, relative-navigation, orbit-determination, observability, kalman-filter]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper asks why an extended Kalman filter (EKF) estimating a
deputy's relative state from range-only measurements, with
Hill–Clohessy–Wiltshire (HCW) dynamics about a circular chief orbit, can
converge to orbits other than the true one. Writing the HCW solution in
relative orbit elements (ROEs) and expanding the squared range in nine
linearly independent time functions, it derives the conditions for two
orbits to share a range history (Eqs. 4a–4i). The ambiguous orbits are
mirror orbits (size and shape kept, orientation changed; three of them),
deformed orbits (shape changed; four of them, from at most one valid
root $K\neq1$ of a quartic, Eq. 18) and, for central orbits (zero radial
and along-track offset), infinitely many. A Lie-derivative observability
matrix gives local observability in general and its loss for central
orbits (Eqs. 37–39). EKF simulations reproduce the ambiguous orbits,
show that higher-order filter models (second and third order, full
two-body) enlarge the basin of convergence to the true orbit, and show
that the ambiguities persist under a small unmodelled chief eccentricity
and J2. The paper has no plasma or propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Ambiguity conditions** (§2.1, Eqs. 3–5): under HCW dynamics the
   squared range is a combination of nine time functions (constant,
   $\cos2nt$, $\sin2nt$, $\cos nt$, $\sin nt$, $nt\cos nt$, $nt\sin nt$,
   $nt$, $t^2$); an orbit is ambiguous if and only if its ROEs satisfy
   the nine equalities 4a–4i, among them $|a_ey_{d0}|=|a_e'y_{d0}'|$
   (Eq. 5). Shown by derivation.
2. **Mirror orbits** (§2.2, Table 1): exactly three besides the true
   one, with initial Cartesian states
   $(x_0,y_0,-z_0,\dot x_0,\dot y_0,-\dot z_0)$,
   $(-x_0,-y_0,z_0,-\dot x_0,-\dot y_0,\dot z_0)$ and the full sign
   flip; the 16 ROE combinations reduce to these four states, and they
   also satisfy 4f–4i, so drift does not exclude them. Shown.
3. **Deformed orbits** (§2.3, Eqs. 11–26, Fig. 5): they exist only for
   closed (non-drifting) orbits; with $a_e'=ka_e$, $y_{d0}'=y_{d0}/k$,
   $K=k^2$ the condition is a quartic in $K$ (Eq. 18); squaring
   introduces two extraneous roots, so at most one valid $K\neq1$ exists,
   giving four deformed orbits (one plus its three mirrors). Shown.
4. **No deformed orbit at tangency** (§2.4, Eq. 28): none exists when
   $\frac{dh}{dK}\big|_{K=1}=\frac54a_e^2-2y_{d0}^2+\frac34a_e^2\cos(2\beta_0-2\psi_0)=0$,
   independent of $z_m$; demonstrated numerically (Eqs. 29–31, double
   root at $K=1$); the existence argument is qualitative (Fig. 6), not a
   proof.
5. **Central orbits** (§2.6, Fig. 9): with zero radial and along-track
   offset there are three constraints on four unknowns, hence infinitely
   many ambiguous orbits; first analysed by Christian [15] (attributed).
   Their range history has a half-orbit period, suggested as a detection
   cue.
6. **Local observability** (§3, Eqs. 36–39): with output $\rho^2/2$, the
   Lie-derivative observability matrix has
   $\det N=27z_m^2n^{12}\mathcal G(\cdot)$; for $x_{\rm off}=0$,
   $\det N=864n^{12}z_m^2y_{\rm off}\{\dots\}$, vanishing for
   $y_{\rm off}=0$: central orbits are locally unobservable, general
   orbits locally observable except at special epochs, and $z_m=0$ only
   makes the out-of-plane mode unobservable. The conclusions say
   "proved"; the determinant expressions are shown without full
   derivation.
7. **Higher-order filter models** (§4.3, Figs. 15–17): in the small
   scenario the EKF leaves the true orbit at $\gamma=0.26$ (HCW), 0.33
   (second order) and about 0.53 (third order and full nonlinear); with
   growing separation the HCW filter departs earlier and the full
   nonlinear one later. Shown numerically.
8. **Persistence** (§4.4, Figs. 18–22): mirror (type c) and deformed
   (type d) ambiguous orbits persist under an unmodelled chief
   eccentricity of 0.05 and under J2; at 0.15 the EKF converges to no
   orbit (residual beyond $3\sigma_\rho=60$ m). Shown numerically.

# Methods

* Dynamics: HCW equations (Eq. 1) in the LVLH frame ($x$ radial, $y$
  along-track, $z$ cross-track); ROE solution (Eq. 2) with in-plane
  amplitude $a_e$, offsets $x_d$, $y_{d0}$, out-of-plane amplitude $z_m$
  and phases $\beta_0$, $\psi_0$; ROE-to-Cartesian map (Eq. 10, from
  [13]).
* Ambiguity analysis: coefficient matching of the squared range
  (Eq. 3); quartic in $K$ (Eq. 18); classification by the y–z projection
  offset and the slope of the projected ellipse's major axis (Eq. 32,
  Appendix A, Eqs. 44–52); eight types (t), (a)–(g) (Table 5).
* Observability: local nonlinear observability through Lie derivatives
  and the rank condition (Eqs. 34–36, [19,21]); the 6×6 matrix for HCW
  given explicitly (Eq. 37).
* Estimator: continuous-discrete EKF (Eqs. 40–43); range measurement
  noise $20^2$ m²; initial covariance diag($1.8\times10^7$ m² ×3,
  18 m²/s² ×3); process-noise standard deviation
  $1.05\times10^{-4}$ m/s²; measurement interval 10 s. Measurements from
  exact two-body motion of chief and deputy (§4.1), J2-perturbed for
  Figs. 21–22. Second-order, third-order and full two-body filter models
  as in [11].
* Initial-guess sweep (§4.3, Fig. 14): the guess moves from the true
  orbit toward type (c) by a coefficient $\gamma$ in steps of 0.01;
  convergence to a type is declared within 90% of its offset and slope.

# Tests and results

* True orbit (§2.2, Tables 2–3, Fig. 3): $x_0=-35.51$ km,
  $y_0=12.45$ km, $z_0=0.065$ km, $\dot x_0=0.66$ m/s, $\dot y_0=-2nx_0$,
  $\dot z_0=39.43$ m/s, $n=0.0604$ deg/s; ROEs $a_e=70.02$ km,
  $z_m=37.36$ km, $x_d=0$, $y_{d0}=12.58$ km, $\beta_0=359.90^\circ$,
  $\psi_0=270.10^\circ$.
* Deformed case (§2.3, Eqs. 20–21, Table 4, Fig. 4): quartic
  $K^4-2.4336K^3+1.629K^2-0.199K+0.004=0$ with roots 1.2837
  (extraneous), 1, 0.12549 (valid) and 0.02444 (extraneous); the deformed
  orbit has a smaller in-plane and a larger out-of-plane amplitude.
* Tangent case (§2.4, Eqs. 29–31): $y_{d0}=3.551\times10^4$ m; roots
  1.3402, a double root at 1, 0.18655; no deformed orbit.
* Central orbits (§2.6, Table 6, Fig. 8): ten ambiguous orbits sharing
  one range history, $a_e'$ from 63.92 to 70.67 km.
* EKF (§4.2, Table 7, Figs. 10–13): chief circular, radius 7100 km,
  inclination 1°; a drifting deputy (element differences $\delta a=5$ km,
  $\delta e=0.005$, $\delta i=0.3^\circ$, $\delta M_0=0.1^\circ$) reaches
  types (a), (b), (c); the non-drifting deputy reproduces type (c) and a
  deformed type (e); for a central orbit, an EKF initialised at the true
  state converges to different central ambiguous orbits in different
  runs.
* Separation scenarios (§4.3, Table 8): mean separations 60, 300 and
  600 km; along the sweep the EKF also converges to types (d), (a), (b),
  (f).
* Unmodelled perturbations (§4.4, Figs. 18–22): convergence to the
  ambiguous orbits with chief eccentricity 0.05, failure at 0.15;
  convergence regions shrink with eccentricity error (0, 0.01, 0.03);
  under J2 the EKF tracks a sequence of mirror orbits and, for type (d),
  rescales the amplitudes each period.

# Notation map

The paper is relative orbit estimation; none of its quantities has a
registry counterpart.

| Wang, Butcher & Lovell (2018) | Registry | Note |
|---|---|---|
| $x$, $y$, $z$ | words (LVLH radial, along-track, cross-track) | **collision** with the registry's $x$, $y$ and axial $z$ |
| $n$ | words (chief mean motion) | **collision** with $n_s$ |
| $\rho$, $\rho_k$ | words (inter-spacecraft range) | not the charge density $\rho_c$ |
| $a_e$, $z_m$, $x_d$ ($x_{\rm off}$), $y_{d0}$ ($y_{\rm off}$), $\beta_0$, $\psi_0$ | words (relative orbit elements) | the paper uses the two spellings interchangeably |
| $k$, $K=k^2$ | words (in-plane scale ratio of a deformed orbit) | **collision** with the wavenumber $k$; $K_k$ is also the Kalman gain |
| $\gamma$ | words (initial-guess variation coefficient) | **collision** with the polytropic index $\gamma$ |
| $s$ | words (slope of the projected ellipse) | **collision** with the species index $s$ |
| $e$, $e_c$ | words (chief eccentricity) | **collision** with the elementary charge $e$ |
| $N(\mathbf x)$, $L_f^kh$ | words (observability matrix, Lie derivative) | |
| $P$, $Q$, $R$, $H_k$, $K_k$ | words (EKF covariances, Jacobian, gain) | **collision** with power $P$ |
| $J_2$ | words (Earth oblateness coefficient) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Ambiguous_relative_orbits_in_sequential_relative_orbit_estim.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 19 pages
     (626–644).
   * **Identity.** doi:10.1016/j.actaastro.2018.04.057, printed on page 1
     and checked on Crossref: title, all three authors, Acta Astronaut.
     151:626–644 match; issue October 2018; page 1 gives received
     5 Jun 2017, revised 14 Feb 2018, accepted 29 Apr 2018, online
     10 Jul 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer; Eq. 37 and the absolute values
     of Eq. 5 read from the rendered pages (lost or garbled in the text
     layer). The function $\mathcal G$ of Eq. 38 is not given by the
     paper. The orbit and step plots are qualitative; only the Fig. 15
     thresholds are stated in the text.
   * **Recorded as printed.**
     * Eq. 38 has the prefactor $27z_m^2n^{12}$, Eq. 39 (the case
       $x_{\rm off}=0$) $864n^{12}z_m^2y_{\rm off}$; consistent only if a
       factor 32 is absorbed in $\mathcal G$, not explained.
     * Notation drift: $x_d$, $y_{d0}$ (§2) against $x_{\rm off}$,
       $y_{\rm off}$ (§2.6, §3); "a′m" for $a_e'$ in §2.6; Eqs. 13a–13b
       write $\cos(2\beta)$, $\sin(2\beta)$ where $2\beta_0$ is meant;
       $\det N_R$ in the text before Eq. 39 against $\det N$ in the
       equation.
     * §2.3 says $a_e'\neq a_e$ and $z_m'\neq z_m$ "because Eqs. (4a-f)
       imply…"; the argument uses 4a–4c.
     * §4.3 cites "Fig. 20(a)" and "Fig. 20(b)" for HCW against full
       nonlinear across separations, which is Fig. 17; Fig. 20 is the
       eccentricity study.
     * §4.4 gives $e_c=0.05$ for both halves of Fig. 18; the caption and
       the following text give 0.05 and 0.15.
     * Appendix A after Eq. 52: "$\psi_0-\psi_0=359.90^\circ-270.10^\circ$"
       should read $\beta_0-\psi_0$; Eqs. 32 and 52 print "a44" for
       $a_e^4$.
     * Table 2 gives $\dot x_0=0.66$ m/s, Table 6 (central orbit with
       otherwise similar $x_0$, $z_0$, $\dot z_0$) $-0.066$ m/s; possibly
       not a slip, since $y_0$ differs.
     * Reader's check: $\dot y_0=-2nx_0$ with $n=0.0604$ deg/s and
       $x_0=-35.51$ km gives about 74.9 m/s, consistent with Table 6's
       74.950 m/s.
     * The conclusions say local observability was "proved"; §3 shows
       only the determinant expressions and asserts $\mathcal G\neq0$
       "generally".
     * Reference list: [1] (Polites, NASA TP) carries "vol 3, 1998,
       pp. 1574–1579", identical to [2], likely a copy slip; [9] prints
       an implausible paper number "23-451" for a 2015 AAS conference and
       Lovell's initials as "A.T."; [15] prints J. Spacecr. Rockets 54(1)
       with year 2016 (volume 54 is 2017; not verified on Crossref).
     * The affiliation prints ZIP "84717" for Kirtland AFB.
   * **Reference list.** 21 printed entries, matching the Crossref
     reference count.
