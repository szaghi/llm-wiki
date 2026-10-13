---
type: Source
title: "Balsara (1998) — Total Variation Diminishing Scheme for Adiabatic and Isothermal Magnetohydrodynamics"
description: "The second-order TVD scheme of the RIEMANN code for adiabatic (seven-wave) and isothermal (six-wave) MHD: characteristic limited slopes (MC-type in genuinely nonlinear, minmod-type in linearly degenerate fields), Yang's steepener in the entropy and Alfvén fields, Colella-type time-centred states, a characteristic-switched artificial viscosity and hyperviscosity, and a spectral Hodge projection whose symbol matches the finite-difference divergence; argues, on split-versus-unsplit comparisons, that divergence cleaning matters."
resource: "doi:10.1086/313093"
source_kind: paper
authors: [Balsara D.S.]
year: 1998
venue: "Astrophys. J. Suppl. Ser. 116:133–153"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1998-ApJS-Balsara-101086313093.pdf"
tags: [mhd, tvd, characteristic-limiting, artificial-compression, artificial-viscosity, projection, divergence-free]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds a second-order TVD (MUSCL-type, predictor–corrector)
Godunov scheme for ideal MHD, adiabatic (seven waves) and isothermal (six
waves), the scheme of the author's RIEMANN code. The corrector is the
noniterative linearized Riemann solver of the companion paper (Balsara
1998, ApJS 116:119). Piecewise-linear slopes are limited on characteristic
variables, with a monotonized-central-type limit in genuinely nonlinear
fields and a minmod-type limit in linearly degenerate fields, and Yang's
(1990) artificial-compression steepener is added in the linearly degenerate
(entropy and Alfvén) fields. Time-centred interface states follow Colella
(1990). Two dissipations are added: a characteristic-switched second-order
artificial viscosity and a fourth-order hyperviscosity, both designed not
to damage the TVD property. A spectral (FFT) Hodge projection whose discrete
symbol matches the finite-difference divergence drives that divergence to
exactly zero on periodic grids. Tests: four 1D adiabatic and two 1D
isothermal Riemann problems, an isothermal Orszag–Tang vortex, and
isothermal and adiabatic 2D blast waves. The paper argues against the view
that divergence cleaning makes no significant difference; its 2D evidence
varies the splitting and the cleaning together. Nothing is proved: "TVD"
and "second order" are design claims, not measured or derived.

# Key claims

1. **Characteristic TVD slopes** (§2.1, eqs. 2.1–2.4). The primitive vector
   is $(\rho, v_x, v_y, v_z, p, B_y, B_z)$, with $B_x$ carried separately.
   Neighbour values are projected on the left eigenvectors of zone $i$,
   $w^{(p)}_{i\pm1} = \ell^{(p)}(i)\cdot(\text{primitive state at } i\pm1)$.
   The limited coefficient is the smallest of half the central difference
   and $\Psi$ times each one-sided difference, with the sign of the
   one-sided differences when they agree, and zero otherwise (eq. 2.3).
   $\Psi = 2$ in genuinely nonlinear fields (the monotonized-central
   limit) and $\Psi = 1$ in linearly degenerate fields (a minmod-type
   limit; the limiter names are the reader's). The slope is the sum of the
   coefficients times $r^{(p)}$ (eq. 2.4). Eigenvectors: Roe & Balsara
   (1996) for adiabatic, Balsara (1996) for isothermal MHD. Motivation
   (§2): characteristic interpolation enforces entropy better, primitive
   interpolation steepens linearly degenerate fields better, and steepening
   on top of characteristic interpolation gives both.
2. **Yang steepening in linearly degenerate fields** (§2.2, eqs. 2.5–2.12;
   "we follow Yang (1990) almost entirely"). Applied to the entropy wave
   and both Alfvén waves (adiabatic), or both Alfvén waves (isothermal).
   A balance factor (eq. 2.5) with exponent constant 4.3, a squared
   normalized second-difference discontinuity detector (eq. 2.6), a slope
   modifier with compression constant 33.0 (eq. 2.7), and an extra slope
   from minmod combinations of the limited primitive slopes projected on
   $\ell^{(p)}$ (eqs. 2.8–2.12).
3. **Time stepping** (§3, eqs. 3.1–3.5). One-step, second order in space
   and time, after Colella (1990); Shu–Osher multistage Runge–Kutta is
   deliberately not used. Reference states take the extreme eigenvalues of
   the zone, and time-centred states add, per field moving toward the
   face, the difference between the extreme and the field's eigenvalue
   times its slope coefficient (eqs. 3.3–3.4), then the conservative update
   (eq. 3.5). Multi-D runs use Strang-split sweeps, or an unsplit variant
   that adds first-order transverse flux differences to the predicted
   states (citing Colella 1990). §7 calls the scheme "predictor-corrector":
   characteristic variables in the predictor, the linearized Riemann
   solver "with property U" in the corrector.
4. **Artificial viscosity and hyperviscosity** (§4, eqs. 4.1–4.18).
   * The update adds a second-difference viscosity minus a
     fourth-difference hyperviscosity of the conserved state, each with an
     interface coefficient (eqs. 4.1–4.4).
   * Per-field switch: one minus a limiter function of the ratio of
     one-sided characteristic differences, van Leer's in genuinely
     nonlinear fields and superbee in linearly degenerate fields
     (eqs. 4.5–4.8); the interface switch is the larger of the two zones'
     values, maximized over the seven fields (eqs. 4.9–4.10).
   * Hyperviscosity (eq. 4.11): a constant (tried in $[1/64, 1/32]$) times
     the largest $\vert\lambda^{(p)}\vert$ times $\max[0, 1 - 2\times(\text{switch})]$;
     it switches off when the switch exceeds 0.5, near strong
     discontinuities, which preserves TVD (citing Swanson & Turkel 1992).
   * Second-order viscosity (eq. 4.16): a constant ($[0.06, 0.1]$) times
     the largest of $\vert\lambda^{(p)}\vert$ times the switch over the
     fast and slow fields only, times a pressure switch (density for
     isothermal) in excess of 0.5. Near slow shocks it scales with the slow
     speed; it is off at entropy pulses, Alfvén shocks and weak shocks;
     it is "more than 10 times smaller" than the viscosities of centred
     schemes. That it cannot damage TVD because it is dissipative is
     asserted, not proved. Wider-support variants (eqs. 4.17–4.18) spread
     shocks over about four zones and "do not change the CFL condition"
     (asserted).
5. **Why viscosity** (§4, p. 136). Slowly moving strong shocks produce
   post-shock oscillations; Quirk's odd–even coupling at grid-aligned
   shocks persists even with an exact solver. HLLE cannot represent MHD
   slow shocks exactly, because they do not move at the extreme speeds;
   the same holds for HLLEM, and Alfvén waves are not at the arithmetic
   mean of the extreme speeds, so an MHD HLLEM is "trickier". Stated, not
   demonstrated. Quirk's entropy-fix suggestion for linearly degenerate
   fields is used "in all the examples".
6. **Spectral Hodge projection** (§5, eqs. 5.1–5.6).
   * The zone-centred divergence is a central difference (eq. 5.1).
   * The traditional projection solves a Poisson equation for the
     potential and subtracts its gradient (eqs. 5.2–5.3), in spectral
     space with the exact symbol $1/\vert\mathbf k\vert^2$ (eq. 5.4). That
     leaves the finite-difference divergence of eq. 5.1 nonzero, because
     5.4 is not the symbol of the FD operator.
   * Fix: apply the tensor projector
     $\delta_{\alpha\beta} - k_\alpha k_\beta/\vert\mathbf k\vert^2$ to all
     three field components (eq. 5.5), with $ik_x$ replaced by
     $i\sin(k_xh_x)/h_x$ and likewise in $y$ and $z$ (eq. 5.6). Eq. 5.1 is
     then "exactly zero". All three components must go to and from
     spectral space; periodic boundaries only. Cost "no more than 2%" of
     the total (§6, p. 152), stated without data.
7. **Divergence cleaning matters** (§§6.2.1–6.2.2, pp. 147, 149–152). The
   paper contests "the opinion in the literature" (Dai & Woodward 1994b;
   Zachary et al. 1994; Ryu, Jones & Frank) that dropping the cleaning
   makes no significant difference, because those authors used split
   schemes, short times and a less accurate projection. Without cleaning,
   small-scale divergence builds up slowly, mostly in stagnation regions;
   since total energy is updated, this can drive the pressure negative,
   so cleaning "is essential for physical realizability". Imposing the
   constraint at all matters more than which discretization of it is used
   (p. 149).
8. **Parallel performance** (abstract, §7). Ideal scaling to "a few
   hundred" processors with the Balsara & Melhem (1997) strategy; no
   numbers are given.

# Tests

* **1D adiabatic** (§6.1, Table 1, Figs. 1–4). $x \in [-0.5, 0.5]$, 800
  zones, CFL 0.8, jump at $x = 0$, no smoothing; $\gamma = 5/3$ except
  Fig. 2 ($\gamma = 2$); field in Gaussian units with
  $f = (4\pi)^{1/2}$; viscosity constant 0.1 and pressure-switch threshold
  0.5 unless stated; hyperviscosity off in the displayed runs (repeated
  with constant 1/32, no degradation); Figs. 1–2 without viscosity.
  * Fig. 1: $(\rho, p, B_y) = (1, 1, 1.0f \mid 0.2, 0.1, 0)$, $B_x = 1.0f$,
    $t = 0.15$: switch-on fast shock in at most 3 zones, fast and slow
    rarefactions, contact, slow shock. This is Ryu–Jones 4a in Gaussian
    units ([Ryu–Jones shock tubes](/benchmarks/ryu-jones-shock-tubes.md)).
  * Fig. 2: Brio–Wu, $(1, 1, 1.0f \mid 0.125, 0.1, -1.0f)$,
    $B_x = 0.75f$, $\gamma = 2$, $t = 0.1$: slow compound wave, contact in
    at most 4 zones, weak slow shock in little more than 2
    ([Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)).
  * Fig. 3: $\rho = 1.08 \mid 1$, $p = 0.95 \mid 1$,
    $\mathbf v = (1.2, 0.01, 0.5) \mid 0$, $B_y = 3.6 \mid 4.0$,
    $B_z = 2.0 \mid 2.0$, $B_x = 2.0$ (cgs), $t = 0.2$: seven
    discontinuities with viscosity on, contact and rotational
    discontinuities "not damaged". This is Ryu–Jones 2a (the cgs values
    divided by $\sqrt{4\pi}$, reader's check).
  * Fig. 4: $\rho = 1 \mid 1$, $p = 1 \mid 1$,
    $v_x = 36.87 \mid -36.87$, $v_y = -0.155 \mid 0$,
    $v_z = -0.0386 \mid 0$, $B_y = 4.0 \mid 4.0$, $B_z = 1.0 \mid 1.0$,
    $B_x = 4.0$, $t = 0.03$: two Mach 25.5 fast shocks; flat profiles,
    little post-shock oscillation; transverse-velocity start-up spikes
    "significantly" smaller than in Dai & Woodward (1994b) from the same
    unsmoothed data.
* **1D isothermal** (Table 2, isothermal sound speed 1). Fig. 5: six waves,
  rotational discontinuities undamaged. Fig. 6 ($\rho = 0.1$,
  $v_x = 5 \mid -5$, $B_y = 5 \mid -5$, $B_x = 0$, $t = 0.1$): two strong
  fast shocks and a persistent central density spike at the neutral
  point, read as numerical reconnection.
* **Isothermal Orszag–Tang** (§6.2.1, Figs. 7–8). $(0, 2\pi)^2$, periodic,
  $200^2$, $\rho = 1$, $\mathbf v = v_0(-\sin y, \sin x)$,
  $\mathbf B = B_0(-\sin y, \sin 2x)$ (eqs. 6.1–6.2), $v_0 = c$, $B_0$ set
  by gas pressure over rms magnetic pressure $= 10/3$, $t = 3.0$. Fig. 7:
  Strang-split, no cleaning; Fig. 8: unsplit with the accurate cleaning
  every step. Density and total pressure "reasonably similar"; the split,
  uncleaned kinetic energy shows "two tiny concentrations at the center
  that dominate the entire flow field", absent from Fig. 8c. Splitting and
  cleaning change together, so the difference cannot be attributed to
  cleaning alone (reader's observation)
  ([Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)).
* **Blast waves** (§6.2.2, Figs. 9–11). Unit square, $200^2$, uniform
  $B_x = 10.0$ G.
  * Isothermal: $\rho = 100$ inside radius 0.05, else 1, $c = 1$,
    $t = 0.09$; Fig. 9 split without cleaning, Fig. 10 unsplit with
    cleaning; without cleaning the magnetic pressure shows "a great deal of
    small-scale fluctuations especially in the center".
  * Adiabatic: $\rho = 1$, $p = 1000$ inside radius 0.05, else 1,
    $\gamma = 1.4$, $t = 0.02$; Fig. 11, split with cleaning; splitting
    "does not seem to have affected the quality"
    ([MHD blast wave](/benchmarks/mhd-blast-wave.md)).

No convergence table, timing or divergence norm is shown.

# Notation map

| Balsara (1998) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F_x$ | $u$, $f$ | |
| $V$ (eq. 2.1) | words (primitive state with $B_y$, $B_z$); cf. $\mathbf W$ | $B_x$ carried separately |
| $\lambda^\alpha_i$, $l^\alpha$, $r^\alpha$, $\alpha = 1..7$ | $\lambda^{(p)}$, $\ell^{(p)}$, $r^{(p)}$ | **collision**: registry $\alpha$ is the Lax–Friedrichs speed |
| $w^\alpha_{i,0}$, $w^\alpha_{i,\pm1}$ | $w^{(p)}_j$ (with the eigenvectors of zone $i$) | |
| $\Delta w^\alpha_i$, $\Delta V_i$ | words (limited slope coefficient, limited slope) | **collision**: unsuperscripted $\Delta$ is the PPM jump $\Delta u_i$ |
| $\Psi$ | words (2 or 1) | |
| $\beta^\alpha_i$, $b = 4.3$ | words (Yang's balance factor) | **collision**: smoothness indicator $\beta_k$ |
| $\mu^\alpha_i$, $c = 33$, $\sigma^\alpha_i$ | words (detector, compression constant, slope modifier) | **collision**: sound speed $c$, flux-limiter $\sigma$, diffusion $\mu$ |
| $m(x, y)$ | $\operatorname{minmod}$ | |
| $\phi(r)$ (eqs. 4.7–4.8) | words (limiter function) | **collision**: PPM $\phi_i$ |
| $\phi$ (eqs. 5.2–5.4) | $\Phi$ | eq. 5.2 has the registry sign; eq. 5.3 prints $\mathbf B - \nabla\phi$ (see Citations) |
| $\nu^\alpha_i$, $\nu^M$, $\nu^P$, $\bar\nu^P$ | words (viscosity switches) | **collision**: CFL number $\nu$ |
| $\kappa^{(2)}$, $\kappa^{(4)}$ and their constants | words (viscosity coefficients) | **collision**: $\kappa$, $\kappa_i$ |
| $\Delta x$, $\Delta y$, $\Delta z$ | $h_x$, $h_y$, $h_z$ | |
| $\Gamma$, $P$ | $\gamma$, $p$ | |
| $c$ (isothermal, §6.2.1) | $c$ | $p = \rho c^2$ |
| $\lambda^M_i$, $\lambda^m_i$ | largest and smallest $\lambda^{(p)}$ of zone $i$ | |
| $f = (4\pi)^{1/2}$ | words | Gaussian-unit field factor |

# Pages created or updated

* Updated [Constrained transport](/methods/constrained-transport.md) (batch-18 block: the FD-symbol-matched spectral projection, its printed sign, the claim that cleaning matters).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md) (batch-18 block: characteristic slopes with field-dependent limiting and Yang steepening).
* Updated [Positivity preservation](/properties/positivity-preserving.md) (batch-18 block: uncleaned divergence and negative pressure).
* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (batch-18 block: the isothermal variant; splitting and cleaning varied together).
* Updated [MHD blast wave](/benchmarks/mhd-blast-wave.md) (batch-18 block: the 1998 adiabatic and isothermal blasts, the likely "earlier blast").
* Updated [Ryu–Jones shock tubes](/benchmarks/ryu-jones-shock-tubes.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), [HLL Riemann solver](/methods/hll-riemann-solver.md) and [Contact sharpening](/methods/contact-sharpening.md) (sent to the compiler; not written here).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1998-ApJS-Balsara-101086313093.pdf`.
   * **Version read.** The published journal PDF, 21 pages, not a
     preprint. Received 1995 December 21; accepted 1997 December 3.
   * **Identity.** doi:10.1086/313093, checked on Crossref: title matches,
     Astrophys. J. Suppl. Ser. 116(1):133–153, May 1998, single author
     Balsara.
   * **How it was read.** The text layer has broken ligatures and garbled
     equations; every equation was read from page images at 110 dpi, and
     eqs. 2.3, 2.5, 5.1–5.4 and Table 1 were checked again at 250–300 dpi.
     The superscripts of the $R$ terms in eq. 2.10 were read at 110 dpi
     only. Plotted values were not transcribed.
   * **Recorded as printed** (reader's reading).
     - Eq. 5.3 prints $\mathbf B - \nabla\phi$ with eq. 5.2,
       $\nabla^2\phi = -\nabla\cdot\mathbf B$; as printed the divergence of
       the result is twice the original. Eqs. 5.4–5.5 are self-consistent
       with $\mathbf B + \nabla\phi$, the registry convention. The same
       printed inconsistency is recorded for Zachary et al. eq. 34, which
       Balsara cites for it.
     - Eq. 5.1 divides the central differences by $h$, not $2h$, while the
       symbol of eq. 5.6 corresponds to a $1/(2h)$ difference: a constant
       factor 2, irrelevant to "exactly zero".
     - Text vs list: "Ryu, Jones, & Frank 1996" (1995 in the list);
       "Jorgensen & Terkel 1993" (Jorgenson & Turkel in the list); "Evans &
       Hawley (1989)"; "Roe & Balsara 1996, SIAM J. Numer Anal., 56, 57"
       (SIAM J. Appl. Math.); "Collella" in Zachary & Colella 1992; "Comm.
       Pure & Appl. Math." for Harten 1977.
     - Second order and TVD are claimed, not measured or proved; the 2%
       projection cost and the scaling claim have no data.
   * **Reference list:** 34 entries, all without titles (ApJ style), all
     merged. The bibliography title of this paper was corrected to
     "scheme", as on page 1. Brackbill & Barnes is printed 35:462 (Crossref
     35:426); Harten 1977 is printed Comm. Pure Appl. Math. 30:661
     (Crossref 30:611); ApJ 465:775 is the new `balsara-1996-b`, distinct
     from `balsara-1996`; the companion Riemann-solver paper (ApJS 116:119)
     is `balsara-1998`; Balsara & Melhem is `balsara-1997` ("submitted").
     Bibliography: 3380 entries.
