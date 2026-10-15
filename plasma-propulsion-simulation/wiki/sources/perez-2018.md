---
type: Source
title: "Perez, Geller & Lovell (2018) — Non-iterative angles-only initial relative orbit determination with J2 perturbations"
description: "Derives a non-iterative angles-only initial relative orbit determination algorithm with the J2 perturbation, using equatorial spherical relative dynamics, second-order line-of-sight expansions, an SVD and the Matrix Determinant Lemma to reduce the problem to a polynomial of degree at most 15 in the range scale, and tests it on LEO and GEO formation scenarios with and without angle noise."
resource: "doi:10.1016/j.actaastro.2018.06.033"
source_kind: paper
authors: [Perez A.C., Geller D.K., Lovell T.A.]
year: 2018
venue: "Acta Astronaut. 151:146–159"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Perez_Non-iterative_angles-only_initial_relative_orbit_determinati.pdf"
tags: [context, relative-navigation, orbit-determination, angles-only, j2-perturbation]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper derives a non-iterative, approximate algorithm for angles-only
initial relative orbit determination (IROD): estimating the six-component
relative state of a deputy spacecraft from line-of-sight (LOS) angles
measured by a chief of known orbit, including the $J_2$ zonal
perturbation. The relative dynamics are written in spherical coordinates
referred to the Earth's equatorial plane, not the chief's orbit plane, so
that the exact, non-averaged $J_2$ acceleration enters. The dynamics are
linearized along the chief orbit (state transition matrix), the
measurement equations are expanded to second order, the SVD of the
first-order measurement matrix gives a dominant solution direction, and
an expansion about it with the Matrix Determinant Lemma reduces the
problem to one polynomial of degree at most 15 in a range scale.
Simulations of LEO ($a=7000$ km) and GEO ($a=42{,}164$ km)
leader-follower, flyby and 2×1 football formations show good accuracy at
low inclination and eccentricity, strong degradation at high
inclination, a clear benefit of modelling $J_2$ (large in LEO, smaller in
GEO), and severe sensitivity to angle noise, especially at small
separation.

# Key claims

Symbols are the paper's own (see the notation map). Errors are percent
position errors of the best feasible root.

1. **Non-iterative** (abstract, §6, §10). The algorithm needs one SVD and
   the roots of a polynomial of degree at most 15 in $k_0$ (Eq. 65), no a
   priori information, and is meant to initialize a Kalman or batch
   least-squares filter.
2. **$J_2$ in equatorial spherical coordinates** (§3, Eq. 4, attributed
   to Schaub & Junkins):
   $\mathbf a_{J_2}=-\tfrac34J_2k_2\bigl[(3\cos2\phi-1)\mathbf i_\rho+2\sin2\phi\,\mathbf i_\phi\bigr]$
   with $k_2=\frac{\mu}{\rho^2}\bigl(\frac{r_{eq}}{\rho}\bigr)^2$. The
   equatorial reference plane is stated to be the key difference from
   earlier curvilinear derivations.
3. **Linearization domain** (§4). Right ascension does not appear in the
   nonlinear equations, so its difference need not be small; the
   linearization requires $\delta\rho\ll\rho_c$, $\delta\phi\ll1$,
   $\delta\dot\rho\ll\omega_o\rho_c$, $\delta\dot\theta\ll\omega_o$,
   $\delta\dot\phi\ll\omega_o$. The equations are singular at
   $\phi=\pi/2$ and $\delta\dot\theta$ grows without bound near the pole
   (stated).
4. **Range unobservability at first order** (§5.1, Eqs. 28–31). The
   first-order LOS equations give $2n$ homogeneous equations in 6
   unknowns, so no unique solution exists (the range-observability
   problem).
5. **Solution direction** (§6, Eqs. 44–45). The right-singular vector
   chosen as $\mathbf v_0$ is the one with the largest dot product with the
   initial LOS unit vector, not the one with the smallest singular value;
   the solution is $\mathbf X_0=k_0\mathbf v_0+V_5\,\delta\mathbf k$ with
   $\delta\mathbf k$ small.
6. **Polynomial reduction** (§6, Eqs. 52–65). $\delta\mathbf k$ follows by
   least squares on $2n-1$ equations; substitution into the remaining one
   and the Matrix Determinant Lemma give a 5×5 determinant equation, a
   polynomial of degree at most 15 in $k_0$. Feasible roots: real part
   kept, $k_0>0$, 100 m to 10,000 km; typically 1–6 feasible roots. Root
   disambiguation is left open: the tests report the root with the lowest
   true error.
7. **Measurement count** (§7, from the cases of the authors' ref. [49]).
   Three measurements perform poorly when the cross-track amplitude is
   under 10% of the in-plane range; with zero cross-track motion at least
   4 are needed; 13 or 25 observations did not beat 4 overall, attributed
   empirically to nonlinearity bias.
8. **LEO accuracy** (§7.1, Tables 3–5). Good at low inclination and
   eccentricity, poor at high inclination (attributed to the
   $\delta\dot\theta$ assumption breaking down); flyby uniformly better
   than leader-follower and football (Table 4: all at most 22%).
9. **$J_2$ in LEO** (§7.2, Tables 6–8). Removing $J_2$ from the IROD model
   while the truth keeps it gives no solution or large errors in many LEO
   cases; the penalty is smaller at large separation because the $J_2$
   effect on relative motion is "approximately independent of the
   relative separation" (stated, not shown).
10. **GEO** (§8, Tables 9–12). All noise-free cases are accurate (at most
    17%); omitting $J_2$ matters less than in LEO but still at 5 km for
    flyby and football (e.g. 3.1% → 26%).
11. **Angle noise** (§9, Tables 13–16). For a 5 km leader-follower,
    acceptable errors need $\sigma\approx10^{-7}$–$10^{-8}$ rad in LEO and
    $\sigma<10^{-8}$ rad in GEO; at 500 km, $\sigma\lesssim10^{-3}$ rad
    (LEO) and $\lesssim10^{-4}$ rad (GEO) suffice. Typical space cameras
    give $10^{-3}$–$10^{-5}$ rad (Hubble resolution $2\times10^{-7}$ rad,
    stated); monocular angles-only IROD in GEO at 5 km "may be
    impossible".

# Methods

* **Dynamics** (§3, Eqs. 1–10): point mass plus $J_2$ in inertial
  spherical coordinates $(\rho,\theta,\phi)$ (radius, right ascension,
  declination), $X$-axis at the chief's initial ascending node:
  $$\begin{aligned}
  \ddot\rho&=\rho\dot\theta^2\cos^2\phi+\rho\dot\phi^2-\frac{\mu}{\rho^2}-\frac34J_2\frac{\mu r_{eq}^2}{\rho^4}(3\cos2\phi-1),\\
  \ddot\theta&=-\frac{2\dot\rho\dot\theta}{\rho}+2\dot\phi\dot\theta\tan\phi,\\
  \ddot\phi&=-\frac{2\dot\rho\dot\phi}{\rho}-\dot\theta^2\sin\phi\cos\phi-\frac32J_2\frac{\mu r_{eq}^2}{\rho^5}\sin2\phi
  \end{aligned}$$
  (the last printed with $r^5$; see Recorded as printed); state
  $[\rho,\theta,\phi,\dot\rho,\dot\theta,\dot\phi]^T$.
* **Linearization** (§4, Eqs. 11–19): relative state
  $\mathbf X=\mathbf x_d-\mathbf x_c$; Jacobian along the chief written in
  full (Eqs. 14–17; consistent with Eq. 9 on the reader's
  differentiation); state transition matrix with
  $\dot\Phi=F\Phi$, $\Phi(t_0,t_0)=I$.
* **Measurements** (§5, Eqs. 20–27): a local non-LVLH frame ($x$ the
  projection of the chief position on the equatorial plane, $z$ the
  inertial $Z$); new LOS angles
  $\tan\alpha=\mathbf r_{rel}\cdot\mathbf i_{\rho c}/\mathbf r_{rel}\cdot\mathbf i_{\theta c}$,
  $\tan\beta=\mathbf r_{rel}\cdot\mathbf i_{\phi c}/\mathbf r_{rel}\cdot\mathbf i_{\theta c}$,
  because LVLH azimuth and elevation cannot be written explicitly in the
  relative spherical state; undefined when
  $\mathbf r_{rel}\cdot\mathbf i_{\theta c}=0$. First-order (Eqs. 28–34)
  and second-order (Eqs. 35–40) expansions, third-order terms assumed
  negligible.
* **Solver** (§6, Eqs. 41–66): SVD $B=U\Sigma V^*$; second-order terms in
  $\delta\mathbf k$ dropped; pseudo-inverse for $\delta\mathbf k$; Matrix
  Determinant Lemma; recovery (Eq. 66).
* **Simulations** (§7, Table 1): truth is nonlinear two-body plus $J_2$
  with exact nonlinear LOS angles. Chief $a_c=7000$ km, $e_c=0$, 0.01,
  0.1, $i_c=0$, 10°, 45°, 60°; leader-follower, flyby and football
  deputies by element offsets; separations 0.5, 5, 50, 500 km (flyby
  altitude offsets 0.07, 0.7, 7, 70 km): 48 cases per scenario. LEO: 4
  measurements 1000 s apart (3000 s span); GEO: $a=42{,}164$ km,
  $e=0$, 0.001, $i=0$, 5°, 9600 s apart. Bands: 0–20% good, 21–50% poor,
  at least 50% bad. Velocity errors "commensurate", not tabulated.
* **Noise** (§9): 100-run Monte Carlo with zero-mean white Gaussian noise
  on the nonlinear angles.

# Tests and results

* **Table 3, LEO leader-follower with $J_2$**: $i=0$, $e=0$: $2.0\times10^{-4}$,
  $3.2\times10^{-2}$, 4.8, 2.6% for 0.5/5/50/500 km; $i=45^\circ$, $e=0.01$,
  0.5 and 5 km: no solution; $i=60^\circ$, $e=0.01$: $1.8\times10^6$% (0.5 km)
  and $1.8\times10^5$% (5 km); $i=60^\circ$, $e=0.1$, 0.5 km: no solution;
  $e=0.1$ errors 12–82%.
* **Table 4, LEO flyby**: all cases 3.3–22%; 5 feasible roots at $i=0$
  for 5–500 km, otherwise 1.
* **Table 5, LEO football**: $i\le10^\circ$: 4.7–25%; $i=45^\circ$: 18–33%;
  $i=60^\circ$: 35–63%.
* **Tables 6–8, LEO without $J_2$ in the model**: leader-follower,
  $i=10^\circ$, $e=0$, 0.5 km: 0.10% → $9.3\times10^7$%; flyby: no solution for
  every 0.5 and 5 km case, comparable at 500 km (e.g. 3.3 against 2.0% at
  $i=e=0$); football, $i=45^\circ$, 0.5 km: 22% → $1.5\times10^4$%.
* **Tables 9–10, GEO with $J_2$**: $e=0$: 0.2–8.6%; $e=0.001$: 0.02–17%
  (leader-follower 500 km, $i=5^\circ$: 17%).
* **Tables 11–12, GEO without $J_2$**: flyby 5 km 3.1 → 26% ($e=i=0$);
  football 5 km 5.6 → 35%; leader-follower $e=0.001$, 50 km 0.3 → 24%;
  leader-follower $e=0$, $i=5^\circ$, 5 km: no solution. Some no-$J_2$ entries
  are lower than the $J_2$ ones (football 50 km: 5.6 against 1.5).
* **Noise, mean/standard deviation of the error [%]**:

| Case | $\sigma$ [rad] → mean/std | Noise-free |
|---|---|---|
| Table 13, LEO, 5 km, $i=5^\circ$, $e=0.01$ | $10^{-3}$: 9789/37260; $10^{-4}$: 1772/2406; $10^{-5}$: 508/432; $10^{-6}$: 217/174; $10^{-7}$: 27.9/25.1; $10^{-8}$: 4.55/2.57 | 4.4 |
| Table 14, LEO, 500 km | $10^{-3}$: 56.5/71.8; $10^{-4}$: 33.8/10.9; $10^{-5}$ to $10^{-8}$: 36.5 (std 0.11 → 0.001) | 36.5 |
| Table 15, GEO, 5 km, $i=5^\circ$, $e=0$ | $10^{-6}$: 35120/128724; $10^{-7}$: 1773/3028; $10^{-8}$: 51.8/54.4; $10^{-9}$: 4.09/4.29; $10^{-10}$: 5.67/5.78; $10^{-11}$: 4.77/4.47 | 3.7 |
| Table 16, GEO, 500 km | $10^{-3}$: 42232/89001; $10^{-4}$: 60.75/42.35; $10^{-5}$: 24.8/18.6; $10^{-6}$: 8.78/1.45; $10^{-7}$: 9.07/0.15 | 9.2 |

# Notation map

The paper is outside the bundle's domain; its symbols are kept in words.

| Perez et al. (2018) | Registry | Note |
|---|---|---|
| $\rho$, $\theta$, $\phi$ | words (inertial spherical radius, right ascension, declination) | **collisions:** registry $\theta$ azimuthal coordinate, $\phi$ electrostatic potential; the paper's $\rho_c$ (chief radius) collides with the charge density $\rho_c$ |
| $\delta\rho$, $\delta\theta$, $\delta\phi$, $\mathbf X$ | words (relative spherical state) | |
| $J_2$, $r_{eq}$ ($R_{eq}$) | words (Earth oblateness coefficient, equatorial radius) | the paper alternates $r_{eq}$ and $R_{eq}$ |
| $\mu$ | words (Earth gravitational parameter) | **collision** with $\mu_0$, $\mu_\perp$, $\mu_\parallel$ |
| $\alpha$, $\beta$ | words (LOS angles) | not $\alpha_{\mathrm B}$, $\alpha_E$ |
| $\Phi$, $F$ | words (state transition matrix, Jacobian) | **collision:** registry $F$ is thrust |
| $k_0$, $\delta\mathbf k$, $\mathbf v_i$, $V_5$ | words (solution scale, SVD basis) | **collisions:** registry $k$ wavenumber, $\mathbf v$ particle velocity |
| $\omega_o$ | words (orbital angular rate) | not a mode or plasma frequency |
| $\sigma$ | words (angle-noise standard deviation) | not a cross section $\sigma_{sk}$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Perez_Non-iterative_angles-only_initial_relative_orbit_determinati.pdf`.
   * **Version.** Publisher's final typeset PDF (version of record), 14
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.033, printed on page 1
     and checked on Crossref: title ($J_2$ in MathML), the three authors,
     Acta Astronaut. 151:146–159 match; published in print October 2018
     (no published-online field on Crossref). Page 1 gives received 14 Feb
     2017, revised 13 Oct 2017, accepted 13 Jun 2018, online 19 Jun 2018.
     Page 1 matches the filename title.
   * **How it was read.** Full text layer; Eqs. 4–17 and 35–66 and Table 1
     checked on rendered pages (149, 151, 152). Table 2's colour coding is
     lost in the text layer (the bands are recorded); table numbers were
     read from the text. Figs. 1–6 (trajectory plots) were not digitised.
   * **Recorded as printed.**
     * Eqs. 6 and 9, declination row: the $J_2$ term has $r^5$ in the
       denominator where every other term uses $\rho$; Eq. 15's last row,
       $15J_2\mu R_{eq}^2\sin2\phi/(2\rho^6)$, confirms $\rho^5$.
     * §4 states $\delta\dot\theta\ll\omega_o$ (consistent); §7.1 restates
       it as "$\delta\dot\theta\ll\omega_o\rho_c$" (dimensionally
       inconsistent).
     * §§5.1–5.2 call Eqs. 26–27 "the measurement equations in 28 and 29";
       §5.1 expands about $\rho_c$, $\phi_c$ and $\delta\theta=0$, §5.2
       "about $\rho_c,\theta_c,\phi_c$".
     * The abstract and §10 say "SVD of a 6 × 6 matrix"; $B$ is $2n\times6$
       (Eqs. 41–43), only $V$ is 6×6.
     * Table 13 is described as one of the §7 leader-follower scenarios
       but uses $i=5^\circ$, which §7 does not; its noise-free 4.4% matches no
       5 km, $e=0.01$ entry of Table 3 (1.1% at $i=0$, 16% at $i=10^\circ$).
       Table 14 (500 km, $i=5^\circ$, noise-free 36.5%) likewise has no §7
       counterpart (Table 3: 20% at $i=0$, 33% at $i=10^\circ$). Table 16's
       noise-free 9.2% differs from 8.6% in Table 9 for the apparently
       same case; Table 15's 3.7% matches Table 9.
     * §10 says the LEO error is "generally < 25%" for $e<0.1$, $i<60^\circ$;
       Table 3 has 41% ($i=45^\circ$, $e=0$, 50 km) and 27%, Table 5 26–33% at
       $i=45^\circ$.
     * §10 requires errors below $10^{-3}$ rad for LEO at 500 km, but
       Table 14 gives 56.5% (against 36.5% noise-free) at exactly
       $10^{-3}$; the 5 km threshold of $10^{-7}$ rad is consistent with
       Table 13.
     * The claim of "higher fidelity than any other currently available"
       IROD algorithm (§1) is not backed by a head-to-head comparison.
     * Typos and attributions: Table 8 prints "1.1.e4"; refs. [5] and [11]
       print "relaitve"; §1 cites "Newman [30]" for Volterra theory but
       ref. [30]'s first author is Stringer; ref. [44] (Gobetz,
       power-limited variable-thrust transfer) is cited for a
       curvilinear-linearization point, an unverified attribution.
   * **Reference list.** 51 printed entries, matching the Crossref
     reference count. Same-first-author-year keys in printed order:
     geller-2015 = [5], geller-2015-b = [13]; geller-2014 = [43],
     geller-2014-b = [51]; tschauner-1965 = [18], tschauner-1965-b = [19].
     The two master's theses ([9], [10]) are encoded as theses with the
     note "Master's thesis".
