---
type: Source
title: "Volpe, Palmerini & Sabatini (2018) — A passive camera based determination of a non-cooperative and unknown satellite's pose and shape"
description: "Proposes an unscented Kalman filter with a feature-sorting algorithm that estimates the relative pose, angular velocity, inertia and shape of a tumbling unknown satellite from monocular-camera features and a range sensor, tested on synthetic features in MATLAB simulations."
resource: "doi:10.1016/j.actaastro.2018.06.061"
source_kind: paper
authors: [Volpe R., Palmerini G.B., Sabatini M.]
year: 2018
venue: "Acta Astronaut. 151:805–817"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Volpe_A_passive_camera_based_determination_of_a_non-cooperative_an.pdf"
tags: [context, relative-navigation, pose-estimation, kalman-filter, non-cooperative-target]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes an unscented Kalman filter (UKF) that estimates, for a
non-cooperative, free-tumbling target satellite of unknown shape, the
relative position and velocity, the attitude quaternion, the angular
velocity, the inertia matrix and the 3-D coordinates of tracked surface
points (hence the shape). The chaser carries a monocular camera and a
range sensor; relative orbital motion follows the Clohessy–Wiltshire
model, target attitude Euler's equations with gravity-gradient torque,
and features a pinhole projection. The claimed novelty (§8) is a
feature-sorting algorithm that handles appearing, disappearing and
recurring features: new measurements are matched to stored features
through a 2-D distance matrix, the state is augmented, and unmatched
features get a measurement variance of $10^9$ so that they are only
propagated. No real image is processed: the features are synthetic
projections of 38 body points with Gaussian noise. MATLAB simulations
(§9) show convergence for two sample times, a performance index against
sample time, shape reconstruction to a mean error of about 9 cm, and
eleven further initial-condition cases. The paper has no plasma or
propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Feature sorting** (§8): the algorithm handles newly appearing,
   disappearing, variable-number and recurring features; this is stated
   as the difference from the authors' earlier filter [23].
2. **Unmatched features** (§8): a measurement-variance entry of $10^9$
   makes their Kalman-gain rows near zero, so they are only propagated.
   State and covariance never shrink: the state covariance is
   $(6n_{t,3}+19)\times(6n_{t,3}+19)$ and the measurement covariance
   $(2n_{t,3}+1)\times(2n_{t,3}+1)$.
3. **Sample time** (§9.1–9.2, Tables 2–3, Figs. 6–7, 11–14): with a
   2 s sample time (case A) the relative angular-velocity error first
   converges (about 200 s) then grows, and the quaternion error does not
   converge; with 1 s (case B) all errors converge. Shown by simulation.
4. **Performance index** (§9.3, Eqs. 21–23, Table 4, Fig. 15):
   $\eta=1/\xi$ with $\xi=\xi_\rho+\xi_{\dot\rho}+\xi_\omega+\xi_q$
   (normalised mean errors) decreases monotonically with sample time:
   $\eta=8.05$, 5.38, 4.36, 3.58, 2.99 for 1, 1.5, 2, 2.5, 3 s.
5. **Real-time feasibility** (§9.3): one filter step costs about 0.05 s in
   MATLAB on an Intel i5; adding about 0.8 s for feature extraction and
   matching (not simulated; stated from refs. [26,27]) gives about
   0.85 s, below the 1 s sample time.
6. **Shape** (§9.4, Table 5, Fig. 17b): tracked points are reconstructed
   to a mean final error modulus of about 9 cm on a 10 m × 7 m × 1 m
   target; three outliers (A, B, C) have a mean final error of 73 cm and
   covariances one to two orders of magnitude larger than a
   well-estimated point, so the covariance can reject them; they do not
   degrade the pose estimate.
7. **Out-of-view convergence** (§9.4, Fig. 16a): a point leaving the
   field of view (point 3, after 50 s) keeps converging, attributed to
   off-diagonal covariance coupling through the sigma points.
8. **Initial conditions** (§9.5, Tables 6–8): mean errors are weakly
   affected across eleven cases; drifting (non-closed) relative
   trajectories are worst; case 8 is "not acceptable" because the
   angular-velocity estimate does not improve.
9. **Generality** (§10): the conclusions state that the approach imposes
   no limitation on target shape, relative attitude, position or
   velocity (see Recorded as printed).

# Methods

* Scenario (§2–3): target non-cooperative, free-tumbling, of unknown
  shape (sample: 10 m high, 7 m wide, 1 m deep), no CAD model; chaser
  with a passive camera whose optical axis is kept on the target centre
  of mass, and a distance sensor.
* Frames (§3): Hill, camera, principal-body, user-chosen body (parallel
  to the camera frame at start) and Earth-centred inertial; the
  Hill-to-camera rotation is a 3-1 sequence of two angles fixed by the
  line of sight (Eqs. 1–2).
* Orbital dynamics (§4): full relative equation (Eq. 3), then the
  Clohessy–Wiltshire equations (Eq. 4) for a circular target orbit and
  small separation.
* Attitude (§5): relative angular velocity (Eq. 5), Euler equations with
  gravity-gradient torque and full inertia matrix (Eq. 6), orbital and
  line-of-sight rates (Eqs. 7–8), quaternion kinematics (Eq. 9).
* Measurements (§6): feature position relative to the camera (Eq. 10)
  and pinhole projection $u_i=p^{CRF}_{i,x}f/p^{CRF}_{i,z}$,
  $v_i=p^{CRF}_{i,y}f/p^{CRF}_{i,z}$ (Eq. 11); 38 tracked body points
  (Fig. 2); occlusion is modelled when generating the synthetic
  observables; Gaussian noise added.
* Filter (§7): UKF [21] with a variable-size state of feature positions
  (camera and body frames), quaternion, angular velocity, relative
  position and velocity, and inertia (Eq. 13); rigid body and constant
  inertia in propagation (Eqs. 14a–h); observables: range (Eq. 15) and
  pixel coordinates (Eqs. 16–17).
* Sorting (§8): matched-feature arrays between consecutive images, a
  distance matrix between newly matched and previously used features,
  matching by column minimum; new features initialised from pixel
  coordinates and measured range (Eqs. 18a–c); new covariance diagonal
  1 m²; measurement noise 0.5 px and $10^{-3}$ m; $10^9$ for unmatched
  features.
* Implementation: a MATLAB script on an Intel i5 (§9, §9.3).

# Tests and results

* Common setup (Table 1, §3): known target orbit $a=7000$ km, $e=0$,
  $i=40^\circ$; true initial relative position $(40,0,5)$ m, guess
  $(42,2,7)$ m; true relative velocity $(0,-8.624\times10^{-2},0)$ m/s,
  guess zero; true angular velocity $(0.3,0.2,0.1)$ deg/s, guess
  $(0.8,0.7,0.6)$ deg/s; quaternion $(1,0,0,0)$ true and guess. Closed
  elliptical relative orbit of mean angular velocity
  $6.18\times10^{-2}$ deg/s; focal length 1300 px; 700 s simulated.
* Case A, 2 s (§9.1, Table 2), initial / final / mean errors: angular
  velocity 0.866 / 0.033 / 0.037 deg/s; quaternion 0 /
  $2.13\times10^{-3}$ / $2.71\times10^{-2}$; position 3.46 /
  $8.31\times10^{-2}$ / 0.574 m; velocity $8.62\times10^{-2}$ /
  $1.42\times10^{-4}$ / $7.95\times10^{-3}$ m/s. The number of allocated
  features never decreases (Fig. 5).
* Case B, 1 s (§9.2, Table 3): angular velocity 0.866 /
  $8.71\times10^{-3}$ / $1.86\times10^{-2}$ deg/s; quaternion 0 /
  $4.31\times10^{-5}$ / $5.89\times10^{-3}$; position 3.46 /
  $2.41\times10^{-2}$ / 0.382 m; velocity $8.62\times10^{-2}$ /
  $1.11\times10^{-4}$ / $4.59\times10^{-3}$ m/s; 16 visible features at
  the first iteration (Fig. 10).
* Sample-time sweep (§9.3, Table 4): $\xi=0.1242$, 0.1859, 0.2291,
  0.2795, 0.3341 for 1, 1.5, 2, 2.5, 3 s.
* Shape (§9.4, case B): point 3 error modulus from 1.32 m to
  $7.96\times10^{-2}$ m (Eq. 24); final standard deviations (Table 5)
  of a few millimetres to 2 cm for point 3 against 0.2–0.9 m on some
  axes for the outliers.
* Eleven cases (§9.5, Tables 6–8): semi-major axis up to 8000 km,
  eccentricity up to 0.2, inclination 0–80°, and varied initial relative
  state and angular velocity; mean position errors 0.172–0.505 m, final
  angular-velocity errors $5.41\times10^{-3}$ to 0.110 deg/s (case 8 the
  worst).

# Notation map

The paper is relative navigation; none of its quantities has a registry
counterpart.

| Volpe et al. (2018) | Registry | Note |
|---|---|---|
| $\boldsymbol\rho=[x,y,z]^T$ | words (relative position) | **collision** with $\rho_c$; $x,y,z$ are Hill-frame coordinates, not the registry's $x$, $y$, $z$ |
| $\varrho$ | words (measured range) | |
| $n$ | words (orbital mean motion) | **collision** with $n_s$ |
| $\mu$ | words (Earth gravitational parameter) | **collision** with $\mu_0$, $\mu_\perp$ |
| $\boldsymbol\omega_{X/Y}$ | words (angular velocity of frame X relative to Y) | **collision** with $\omega$ |
| $\Omega$ | words (4×4 quaternion-rate matrix, Eq. 9; right ascension of the ascending node, Table 1) | **collision** with $\Omega_e$; two meanings in the paper |
| $f$ | words (focal length, px) | **collision** with $f_s$, $f_\varepsilon$, $f_m$, $f_g$ |
| $\eta$ | words (performance index) | **collision** with thrust efficiency $\eta$ |
| $\xi$, $\xi_\rho$, $\xi_{\dot\rho}$, $\xi_\omega$, $\xi_q$ | words (normalised mean errors) | |
| $P$, $R$, $K_k$ | words (state covariance, measurement covariance, Kalman gain) | **collision** with power $P$ |
| $\mathcal I$ | words (target inertia matrix) | |
| $\mathbf p_i$, $\mathbf d_i$, $\mathbf q_{B/C}$, $u_i$, $v_i$ | words (feature positions in camera and body frames, quaternion, pixel coordinates) | $\mathbf d_i$ is not the data vector $\mathbf d$ |
| $a$, $e$, $i$, $\omega$, $\nu_0$ | words (orbital elements) | **collisions** with $e$, $\omega$, $\nu_{sk}$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Volpe_A_passive_camera_based_determination_of_a_non-cooperative_an.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 13 pages
     (805–817).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.061, printed on page 1
     and checked on Crossref: title, all three authors, Acta Astronaut.
     151:805–817 match; issue October 2018; page 1 gives received
     6 Mar 2018, revised 14 May 2018, accepted 30 Jun 2018, online
     4 Jul 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer; Eqs. 1b–1c, 8, 9, 10, 13, 14a
     and 18 checked on rendered pages 807–810, all legible. The sorting
     flow chart (Fig. 4) and the plots (Figs. 5–17) were read as images
     and captions only; no number was taken from a plot.
   * **Recorded as printed.**
     * §1: "While the steps 3 and 3 have been discussed … there still are
       not reliable methods for what step 3 concerns", evidently steps 1
       and 2.
     * Section cross-references are off by one throughout: the §1
       roadmap puts the scenario in section 3 and the results in section
       10 (printed: §2 and §9); §9 cites "the approach presented in
       section 9" (the sorting is §8); §9.5 cites "cases A (section 10.1)
       and B (section 10.2)" (§9.1, §9.2); §8 says the extraction
       algorithms are "listed in section 3" (they are in §1).
     * Angle naming: the text after Eq. 1c calls $\varphi$ and $\psi$
       "azimuth and elevation" respectively; the Fig. 1 caption calls
       $\psi$ azimuth and $\phi$ elevation.
     * The orbital elements are ordered $(a,e,i,\omega,\Omega,\nu_0)$ in
       Table 1 and $(a,e,i,\Omega,\omega,\nu_0)$ in Table 6.
     * Eq. 6 is printed with "+ +3", Eq. 18 with "+ +" and numbered "(18)"
       beside 18a–c.
     * §8 calls the diagonal entries of the measurement covariance "the
       square of the variance"; the values given (0.5 px, $10^{-3}$ m)
       are standard deviations, so the entries are variances.
     * §9.4: the point-3 estimate is "refined by two orders of
       magnitude", but 1.32 m to $7.96\times10^{-2}$ m is a factor of
       about 17.
     * Reader's check: recomputing $\xi$ from Table 3 (case B) with the
       initial norms (40.31 m, $8.624\times10^{-2}$ m/s, 0.374 deg/s)
       gives $\xi_\rho\approx9.5\times10^{-3}$,
       $\xi_{\dot\rho}\approx5.3\times10^{-2}$,
       $\xi_\omega\approx4.97\times10^{-2}$ against Table 4's
       $1.12\times10^{-2}$, $5.65\times10^{-2}$, $5.06\times10^{-2}$; for
       case A the mismatch is larger ($\approx1.42\times10^{-2}$,
       $9.2\times10^{-2}$, $9.9\times10^{-2}$, $2.71\times10^{-2}$ against
       $2.28\times10^{-2}$, 0.101, $8.53\times10^{-2}$, $2.00\times10^{-2}$).
       Either the Table 4 runs are separate noise realisations or the
       normalisation differs from Eq. 21 as printed; the paper does not
       say.
     * Table 4: the 3 s row components sum to 0.3337, printed
       $\xi=0.3341$; the 2.5 s row prints ".2.57".
     * §10 states no limitation on relative attitude, velocity and
       position, while §9.5 reports degraded drifting cases and an
       unacceptable case 8, and §9.1 a degradation with sample time.
     * §2 describes the range as the distance "of the target", §7 as the
       distance to the intersection of the target surface with the
       relative position vector, while the computed observable (Eq. 15)
       is the distance to the centre of mass; the mismatch is not
       discussed.
     * Reference list: [6] Sabatini et al. printed Acta Astronaut. 117
       (2017) 184–196, Crossref gives issue December 2015
       (doi:10.1016/j.actaastro.2015.07.026); [24] Clohessy printed
       single-author "J. Aero. Sci. 97 (2012) 653–658", while the
       Clohessy–Wiltshire paper is classically J. Aerosp. Sci. 27 (1960)
       653–658 with Wiltshire as co-author (not verified on Crossref);
       [3] Foix et al. printed "IEEE Sensor. J. 3 (2017) 1–11", commonly
       cited as vol. 11 (2011) (not verified); [12] author list garbled
       ("G. Martinez, H.,G. Giorgi, B. Eissfeller").
   * **Reference list.** 27 printed entries ([1]–[27]), matching the
     Crossref reference count.
