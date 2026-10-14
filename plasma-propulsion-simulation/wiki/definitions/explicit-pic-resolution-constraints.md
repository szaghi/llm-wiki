---
type: Definition
title: "Resolution constraints of explicit PIC"
description: "The cell-size, time-step, collision-probability and particles-per-cell conditions an explicit particle-in-cell simulation of a thruster plasma must meet, with the values the sources state and use and the different criteria behind their particles-per-cell requirements."
status: established
aliases: [PIC stability constraints, Debye-length constraint, plasma-frequency time-step limit, particles per cell requirement]
tags: [pic, numerics, kinetic, hall-thruster]
timestamp: 2026-10-14T00:00:00Z
---

# Resolution constraints of explicit PIC

An explicit, fully kinetic [PIC-MCC](/methods/pic-mcc.md) simulation must
resolve the electron Debye length and plasma period, keep particles from
crossing more than a cell per step, keep collision probabilities small, and
carry enough particles per cell to hold noise down. These constraints are
what make fully kinetic thruster simulation expensive, and they motivate
the [scaling tricks](/methods/pic-acceleration-scaling.md),
[implicit and energy-conserving schemes](/methods/implicit-and-energy-conserving-pic.md)
and [reduced-order schemes](/methods/reduced-order-pic.md).

## The conditions as stated

**Cell size.** $\Delta x\le\lambda_D$
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3;
[Charoy et al. (2020)](/sources/charoy-2020.md), §II). [Taccogna et al.
(2023)](/sources/taccogna-2023.md) (§II) write $\Delta x$ at most a
constant "of order 1" times $\lambda_D$, and (§V C b) that the explicit
finite-grid instability triggers when $\Delta x$ exceeds $\lambda_D$.
[Miranda et al. (2026)](/sources/miranda-2026.md) (§3) state the looser
$\Delta x<3.4\,\lambda_D$, attributed to three cited works. This
qualifies rather than contradicts $\Delta x\le\lambda_D$: the azimuthal
spacing Miranda et al. use is about $0.95\,\lambda_D$ and the implied
axial spacing about $1.9\,\lambda_D$ at their quoted $\lambda_D$, and the
factor 3.4 is plausibly the Birdsall–Langdon weak-growth bound of the
finite-grid instability, which the compiler has not checked against the
cited works (compiler note).
[Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md) keep $\Delta x$ below
the smallest local $\lambda_D$, with a safety factor of 6, adapted during
the run.

**Time step.** Taccogna et al. (2023, §II) give $\omega_{pe}\Delta t<2$,
stated for electromagnetic codes and applied to electrostatic ones as well
(§III A). The rules used in practice are tighter: $\Delta t<1/\omega_{pe}$ (Taccogna & Garrigues 2019,
§3) and $\Delta t\le0.2/\omega_{pe}$ (Charoy et al. 2020, §II; Miranda et
al. 2026, §3). Muñoz Tejeda et al. (2025) take the minimum of the
plasma-frequency, gyro-frequency and CFL steps with a safety factor of 25.
Miranda et al. (2026, §2.1) also require $\Delta t$ below the
electron cyclotron period ($2.10\times10^{-9}$ s at their exhaust plane,
$B=0.017$ T, printed as 170 G).

**CFL.** No particle crosses more than one cell per step (Taccogna &
Garrigues 2019, §3). In electrostatic PIC the condition is set by the
fastest species, the electrons; electromagnetic explicit codes must also
satisfy the light-speed condition $c\,\Delta t\le\Delta x$, with $c$ the
speed of light, which Taccogna et al. (2023, §III B) call "typically
intractable".

**Collision probability.** Below 5–10 % per species per step for an error
under 1 % (Taccogna et al. 2023, §II; see
[Monte Carlo collisions](/methods/monte-carlo-collisions.md)).

## What the constraints cost

Taccogna & Garrigues (2019, §2.2) take $n_e\sim10^{18}$ m$^{-3}$ and
$T_e\sim50$ eV, so $\lambda_D\approx50$ µm against a 2 cm device, more
than 400 cells per direction; their typical Hall-thruster values are
$\Delta x<30$ µm and $\Delta t<5\times10^{-12}$ s (§3). Taccogna et al.
(2023, §III A) estimate, for a pulsed-arc thruster at $10^{22}$ m$^{-3}$
and $T_e\approx10$ eV, $\lambda_D$ of order $10^{-7}$ m, $\Delta t$ of
order $10^{-13}$ s and about $10^8$ steps for a few µs; for Hall, gridded
and similar thrusters at about $10^{18}$ m$^{-3}$, $\lambda_D$ of order
$10^{-5}$ m, $\Delta t$ of order $10^{-11}$ s and about $10^7$ steps to the
fractions of a millisecond that neutral dynamics need to reach steady state.

## Values used

| Source | Case | $\Delta x$ | $\Delta t$ | $N_{\mathrm{ppc}}$ |
|---|---|---|---|---|
| Charoy et al. (2020), §II | axial–azimuthal, $n\le5\times10^{17}$ m$^{-3}$, $T_e\approx50$ eV | $\approx5\times10^{-5}$ m | $\approx5\times10^{-12}$ s | 75 initial, ≈250 at steady state |
| [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods, Table 4 | same benchmark, Cases 2 / 1 / 3 | $4.88\times10^{-5}$ m (axial), $5\times10^{-5}$ m (azimuthal) | $5\times10^{-12}$ s | 75 / 150 / 300 initial; 290 / 590 / 1200 final |
| Miranda et al. (2026), §§2.1, 3 | axial–azimuthal, $\langle n_e\rangle\sim1.65\times10^{16}$ m$^{-3}$ | $7.81\times10^{-5}$ m (azimuthal) | $10^{-11}$ s | not stated |
| [Reza et al. (2022)](/sources/reza-2022.md), §§4.2, 5.1 | pseudo-2D azimuthal–radial / axial–radial | $2\times10^{-5}$ m | $4\times10^{-12}$ / $2\times10^{-12}$ s | 200 and 50 / 35 and 65 per region cell, initial |
| [Troyetsky et al. (2026)](/sources/troyetsky-2026.md) | axial–radial, $f_\varepsilon=10$ | $2\times10^{-4}$ m | $10^{-11}$ s | 40 initial |
| Taccogna et al. (2023), §V C a, Fig. 18 | ECDI, $512\times512$ cells | — | — | 400 |

Miranda et al. (2026, §3) quote $\lambda_D=8.18\times10^{-5}$ m and derive
the bound $\Delta t<1.73\times10^{-10}$ s from a printed
$\omega_{pe}\sim1.16\times10^9$ s$^{-1}$; that value is the plasma
frequency in hertz, and $0.2/\omega_{pe}$ is about $2.8\times10^{-11}$ s,
which the chosen $10^{-11}$ s still meets (reader's arithmetic, recorded
on the Source page). The axial spacing implied by their 0.04 m and 256 cells,
$1.56\times10^{-4}$ m, is not stated in the paper. Marks & Gorodetsky (2025) state that their grid resolves
$\lambda_D$ and $\omega_{pe}$ without giving the ratios. Troyetsky et al.
(2026) run with the permittivity scaled by $f_\varepsilon^2=100$, which
raises $\lambda_D$ and lowers $\omega_{pe}$ by $f_\varepsilon$.

## Particles per cell: three different criteria

The sources state particles-per-cell requirements of 50 to over 1000. They
are not competing values of one quantity: each is tied to a different
observable.

- **General noise floor.** $N_{\mathrm{ppc}}>50$–100 for explicit PIC-MCC
  of Hall thrusters (Taccogna & Garrigues 2019, §3); about 100 is enough
  for heavy-species properties in hybrid PIC (§2.1). Muñoz Tejeda et al.
  (2025) keep at least 25 per species in the text and "> 50" in their
  Table 1.
- **Spectral content of the electron drift instability.** Numerical noise
  destroys the cyclotron resonances of the
  [electron drift instability](/definitions/electron-drift-instability.md)
  and "facilitates the transition to an ion acoustic instability"; "it
  seems" that an acceptable statistical level needs
  $N_{\mathrm{ppc}}>1000$ (Taccogna & Garrigues 2019, §3.4, the review's
  own statement). Fig. 16, unattributed and presumably the
  authors' own 1D azimuthal run, uses $2.5\times10^4$.
- **Convergence of time-averaged axial profiles.** Charoy et al. (2020,
  §II) run about 250 per cell at steady state, "converged" by the
  benchmark of Charoy et al. (2019). Marks & Gorodetsky (2025, Table 4)
  report the same benchmark with 290, 590 and 1200 final particles per cell
  and the baseline (290) profiles of the axial field $E_x$ ($x$ axial, $y$
  azimuthal, as in the benchmark), $n_i$ and $T_e$ within the
  spread of the 2019 codes (Fig. 3). Troyetsky et al. (2026) find "similar
  spatial trends" with 20, 40 and 80 initial particles per cell.

So the benchmark runs at 250–290 lie below the 1000 that Taccogna &
Garrigues give for resolving cyclotron resonances. As convergence criteria
for time-averaged profiles the benchmark counts are a different criterion
from the 1000-particle requirement, not a competing value (compiler note).
The two sources do disagree on what the ion-acoustic character of the
waves at these counts means: Charoy et al. (2020, pp. 17–18) attribute it
to a physical nonlinear smearing of the cyclotron resonances (after Lampe
et al. 1972), Taccogna & Garrigues to noise. That disagreement is recorded
as an Open contradiction on the
[electron drift instability](/definitions/electron-drift-instability.md)
page. Marks &
Gorodetsky (2025, Results) add a fourth, operational criterion: particle
resampling with a threshold below the steady-state count (200 against 290)
widens the electron velocity distributions axially and azimuthally and
raises $T_e$ at the right boundary by 7 eV, so the threshold should sit
near the expected steady-state count.

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §§II, III A, III B, V C a, V C b (accepted manuscript).
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.1, 2.2, 3, 3.4, Fig. 16 (accepted manuscript).
3. [Charoy et al. (2020)](/sources/charoy-2020.md), §II, pp. 17–18 (accepted manuscript).
4. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods, Results, Table 4, Figs. 3, 5–7.
5. [Miranda et al. (2026)](/sources/miranda-2026.md), §§2.1, 3.
6. [Reza et al. (2022)](/sources/reza-2022.md), §§4.2, 5.1, Tables 2–3 (preprint).
7. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model section, set-up section.
8. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), "PlasmaSim 2D", Table 1.
