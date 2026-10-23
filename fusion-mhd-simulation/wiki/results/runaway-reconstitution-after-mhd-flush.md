---
type: Result
title: "Runaway current reconstitution after an MHD flush"
description: "After a low-Z purge triggers large-scale MHD that stochastizes the field and expels a runaway beam (benign termination), magnetically trapped relativistic electrons survive as a seed of 0.1–1% of the beam and avalanche back once the flux surfaces reheal, so an ITER-like beam loses only about 2–3 MA before it reforms; 3D MHD simulations of the flush itself find more than 95% prompt loss and conversion to Ohmic current in DIII-D, but in EU-DEMO a 77% loss followed by re-avalanche of a confined core remnant."
status: established
aliases: [benign termination, runaway beam flush, RE reconstitution, trapped runaway seed]
tags: [runaway-electrons, disruption, tearing, kink]
timestamp: 2026-10-16T16:51:00Z
---

# Runaway current reconstitution after an MHD flush

**Benign termination** is a way to end a runaway-electron (RE) plateau. In
JET and DIII-D, massive deuterium injection into the plateau purges the
high-Z impurities and triggers large-scale MHD. Parallel streaming in the
stochastic field then expels the beam, whatever modes are involved (they
differ between the two machines), and the wall load is broad enough that no
appreciable localized heat load is seen
([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md), p. 1, attributing this
to the JET and DIII-D experiments). After the field reheals, the remaining
current can induce a field above the avalanche threshold, and any surviving
seed can then avalanche back. That reconstitution is the subject of this
page. The definitions are on
[runaway electrons](/definitions/runaway-electrons.md).

## The result

[McDevitt & Tang (2023)](/sources/mcdevitt-2023.md) find that
**magnetically trapped relativistic electrons survive the flush.**

- Pitch-angle scattering on neon during the plateau populates the trapped
  region of momentum space.
- Stochastic-field transport does not reach trapped electrons, and at high
  energy they detrap slowly. In an imposed, fully stochastic field, passing
  electrons with $|\xi|\gtrsim0.5$ are lost in well under 1 ms. Trapped ones
  survive up to about 10 ms at 3 MeV (Fig. 1). Here $\xi=v_{\parallel p}/|\mathbf v_p|$
  is the pitch ([notation](/notation.md), §10).
- The surviving remnant is "between a percent to a tenth of a percent of the
  original RE beam". That is orders of magnitude above the nuclear (tritium
  and Compton) seed of "a few ampere" that the paper cites (p. 4). Fig. 3(b)
  as plotted spans about 9% to 0.3%, wider than the text's range (recorded on
  the Source page).
- After rehealing the trapped electrons detrap, by pitch-angle scattering and
  a Ware pinch, and avalanche back.

**Headline.** "For most cases of interest $\psi_{10}/\mu_0R_0\lesssim1$ MA,
so runaway reconstitution comes with a 2-3 MA plasma current drop"
(Discussion). Here $\psi_{10}$ is the poloidal flux per decade of avalanche
gain ([notation](/notation.md), §10).

## Upper bound from the avalanche flux

If all available poloidal flux amplifies the seed, the reformed current is
bounded by
$$I_{\mathrm{RE}}^{\max}=2\pi\int_0^a J_{\mathrm{RE}}^{\mathrm{seed}}(r)\,10^{|\psi(r)/\psi_{10}(r)|}\,r\,dr$$
(Eq. 1, given without derivation). Here $I_{\mathrm{RE}}$ is the runaway
current and $J_{\mathrm{RE}}^{\mathrm{seed}}$ the seed current density
(page-local). The bound falls with a larger $\psi_{10}$ and a smaller seed. The
purge raises $\psi_{10}$ and the low post-flush $T_e$ removes the Dreicer and
hot-tail seeds. On paper the post-flush plasma therefore looks favourable,
but trapped-electron seeding means this is "not fully borne out" (p. 2).
Because the gain is exponential in $\psi$, the bound depends only weakly on
the seed. This agrees with the near seed-independence of the plateau in the
[ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md).

## Model behind the result

The model is reduced and does not simulate the MHD
([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md)):

- **Kinetics.** A drift-kinetic Monte Carlo RE solver runs on nested circular
  surfaces. It is coupled to 1D poloidal-flux diffusion with an RE current
  term and an ideal wall $\psi(a)=0$ (Eq. 2), and to a single-temperature 1D
  power balance (Eq. 3).
- **Atomic data.** Charge states and radiation come from steady-state FLYCHK
  data.
- **Flush.** The flush is an imposed Rechester–Rosenbluth-type diffusivity
  acting only on passing electrons, with a Gaussian time window (Eq. 4):
  $$D_{\mathrm{RE}}^{\mathrm{kin}}=\frac{|v_{\parallel p}|}{c}\,\Theta\big(|\xi|-\xi_{\mathrm{tp}}\big)\,D_{\mathrm{RE}},\qquad D_{\mathrm{RE}}=\frac{a^2}{4N_t\,\tau_{\mathrm{tr}}},\quad \tau_{\mathrm{tr}}=\frac{2\pi R_0}{c},$$
  multiplied by $\exp[-(t-t_{\mathrm{open}})^2/\Delta t_{\mathrm{open}}^2]$.
  $N_t$ is the number of toroidal transits of a stochastic field line and
  $\xi_{\mathrm{tp}}$ the trapped–passing boundary. The paper prints the
  boundary as $1-B/B_{\max}$, whereas the standard boundary is
  $\sqrt{1-B/B_{\max}}$, which matches its Fig. 1 boundary at $|\xi|\approx0.5$
  (compiler's remark). All of these symbols are page-local.
- **Injections.** The thermal quench, the neon and deuterium injections and
  the purge of a fraction $f_{\mathrm{purge}}$ of the neon are all
  prescribed.
- **Parameters.** The case has $a=2$ m and $B=3$ T on axis, with a plateau of
  about 5.4 MA formed from about 8 MA. The paper calls it "ITER-like"
  although ITER has 5.3 T and 15 MA, and $R_0$ is never stated.

## Sensitivities

The figure values below are read from the paper's figures.

- **Duration of the open-surface phase.** For $\Delta t_{\mathrm{open}}\lesssim\tau_{\mathrm{st}}=a^2/D_{\mathrm{RE}}\approx0.26$ ms
  the runaway number drops sharply through passing loss. For longer events a
  sharp drop is followed by a much slower decay of the trapped remnant (Fig. 3).
  Raising $\Delta t_{\mathrm{open}}$ 16-fold, from 0.09 to 1.43 ms, lowers the
  reformed current only from 3.9 to 2.0 MA (text). The figure reads about 4.2
  to 2.4 MA final current, which does not match the printed numbers. The
  current drop saturates once $\Delta t_{\mathrm{open}}\gg\tau_{\mathrm{st}}$
  (Fig. 5).
- **Purge fraction.** $f_{\mathrm{purge}}=0.6$, 0.9 and 0.975 reform similar
  currents of about 2.4–2.5 MA (Fig. 4a), because two effects of the retained
  neon offset each other:
  - it raises detrapping, directly and through a larger inductive field whose
    Ware pinch moves trapped electrons inward, so the seed is smaller;
  - it lowers $\psi_{10}$, so the avalanche is more efficient (Fig. 4b,
    $\psi_{10}/\mu_0R_0\approx0.55$–$1.05$ MA).
- **Levers.** Two levers remain: enhanced detrapping, for instance by a higher
  post-purge deuterium density, or a longer open-surface phase. For the
  second the paper calls a passive runaway coil "a more reliable alternative"
  (Discussion).

## 3D MHD of the flush itself

The 3D runs below resolve the flush that the reduced model imposes. They
carry no trapped-electron population.

- **DIII-D 177040 in M3D-C1.** [Liu et al. (2021)](/sources/liu-2021.md)
  (§5.3–5.4) simulate the final loss with the
  [fluid RE model](/methods/runaway-electron-fluid-model.md) and
  [advection by characteristics](/methods/runaway-electron-advection-by-characteristics.md).
  - A (2,1) resistive kink at $q_a\approx2.1$ grows, together with
    nonlinearly excited $n>1$ harmonics, and stochastizes the outer plasma.
  - More than 95% of the runaways reach the lower high-field-side wall within
    about 0.06 ms, with an $n=1$ footprint.
  - The lost runaway current is replaced by Ohmic current, with a small
    current spike.
  - $q_0$ drops to 1 and a (1,1) kink flattens the core.
  - In the post-loss phase (density raised tenfold by hand,
    Rosenbluth–Putvinski avalanche) $T_e$ rises to about 20 eV and the
    current decays in about 3 ms, "consistent with experimental observation".
    The runaway current regrows by avalanche only to about 0.12 MA, against
    about 0.03 MA without the avalanche source (Fig. 15).
- **JET double tearing in JOREK.** In JET the beam is lost in $\le100\,\mu$s
  by an $n=1$ double tearing mode at two $q=4$ surfaces
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.4.2). Without
  runaways, [Nardon et al. (2023b)](/sources/nardon-2023-b.md) find that the
  violent, helicity-conserving relaxation of that
  [double tearing mode](/definitions/double-tearing-mode.md) occurs only in
  a window of normalized $\eta=5\times10^{-7}$ to $3\times10^{-6}$ (Spitzer
  at 47 to 13 eV) (§IV). They hypothesize that the colder, more resistive
  plasma after D$_2$ injection, with $\eta$ probably above $10^{-5}$ (about
  6 eV), lets the main mode grow larger before stochasticity sets in. This
  would explain why D$_2$ injection terminates beams benignly while high-Z
  injection does not (§V). The authors flag it as a hypothesis.
- **EU-DEMO beam in JOREK.** [Vannini et al. (2025)](/sources/vannini-2025.md)
  (§5, Figs. 6–9) restart a 13 MA beam formed in a 2D mitigated VDE in 3D at
  $q_{95}\approx2.3$ with $n\le7$:
  - Edge $(8,4)$ and $(9,4)$ modes dominate first; a $(2,1)$ mode then
    saturates highest at $\sqrt{\psi_N}=0.6$, and the stochastic region grows
    from the edge inward.
  - The runaway current falls from 12.3 to 2.8 MA in 1.12 ms; the drop
    "slightly reduces" the vertical wall force.
  - The remnant sits in the core, on surfaces that the stochastic region did
    not reach. With the closed-surface region regrowing, it re-avalanches to
    about 10 MA by 457.3 ms, about 4 ms after the loss window, while the
    dominant mode moves out to $\sqrt{\psi_N}=0.85$; the beam then partly
    decays again after a new MHD burst, "and so on" (qualitative; deferred to
    future work).
  - The model is the [fluid RE model](/methods/runaway-electron-fluid-model.md)
    with a purely diffusive parallel transport. The energy of the lost part
    is deposited by test markers
    ([runaway-electron wall loads](/definitions/runaway-electron-wall-loads.md));
    the reformed beam's energy is not included.

## Scope and limits

- The reduced model idealizes the 3D mode evolution, the VDE and the purge.
  The authors ask for machine-specific modelling that follows all three
  ([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md), Discussion).
- The 3D runs cannot test the trapped seed. A fluid RE model streams every
  runaway along $\mathbf b$ and has no pitch variable, so it cannot hold a
  trapped population by construction (compiler's remark). The >95% loss in
  M3D-C1 is therefore no counter-evidence to a 0.1–1% trapped remnant.
- Nardon et al. (2023b) note that runaways carrying the current remove the
  finite-resistivity correction to the $\eta^{3/5}$ tearing scaling, which
  weakens one step of their argument. They also note that in DIII-D the
  relevant mode is the resistive external kink (§V, citing Liu et al. 2021).

## Qualifications

**Two survival channels.** McDevitt & Tang's seed is the *trapped*
population that a stochastic field cannot reach. The EU-DEMO remnant of
[Vannini et al. (2025)](/sources/vannini-2025.md) survives because the
stochastic region does not reach the core, in a model with no pitch
variable. The M3D-C1 DIII-D case (>95% loss) and the EU-DEMO case (77%
loss) differ in machine, current (0.75 against 12.3 MA) and in the VDE that
shrinks the DEMO plasma, so the different loss fractions are not a
contradiction; they show that the 3D loss fraction, and hence the seed for
reconstitution, depends on how deep the stochastization reaches
(compiler's reading). With a 23% remnant the DEMO case is far from the
small-seed regime of McDevitt & Tang, so it does not test their bound.

## Contradictions

None among the cited sources. The tension with the "all runaways lost"
reading of beam termination is recorded on
[runaway electrons](/definitions/runaway-electrons.md).

# Citations

- [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md): Eqs. 1–4, Figs. 1–5, Discussion.
- [Liu et al. (2021)](/sources/liu-2021.md): §5.3–5.4, §6, Figs. 10–16.
- [Nardon et al. (2023b)](/sources/nardon-2023-b.md): §IV–V.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): §6.4.2.
- [Vannini et al. (2025)](/sources/vannini-2025.md): §5, Figs. 6–9.
