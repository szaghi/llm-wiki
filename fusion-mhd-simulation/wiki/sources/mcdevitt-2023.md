---
type: Source
title: "McDevitt & Tang (2023) — Runaway electron current reconstitution after a nonaxisymmetric magnetohydrodynamic flush"
description: "Reduced 1D drift-kinetic model of an ITER-like runaway beam flushed by an imposed transient stochastic field, showing that magnetically trapped relativistic electrons populated by neon pitch-angle scattering survive the flush as a 0.1–1% seed that avalanches back after flux-surface rehealing, so that reconstitution comes with only a 2–3 MA current drop."
resource: "doi:10.1103/PhysRevE.108.L043201"
source_kind: paper
authors: [McDevitt C.J., Tang X.-Z.]
year: 2023
venue: "Phys. Rev. E 108:L043201"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Physical_Review_E_McDevitt_Runaway_electron_current_reconstitution_after_a_nonaxisymmet.pdf"
tags: [runaway-electrons, disruption, impurities, particles, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The Letter asks how much plasma current an ITER-like tokamak loses before a
[runaway-electron](/definitions/runaway-electrons.md) (RE) beam, flushed by a
3D MHD event of the kind seen in the JET and DIII-D benign-termination
experiments (deuterium injection purges high-Z impurities, then global MHD
stochastizes the field), comes back through avalanche once the flux surfaces
reheal. The model is reduced: a drift-kinetic Monte Carlo RE solver in nested
circular flux surfaces, coupled to a 1D poloidal-flux diffusion equation with
an RE current term and a 1D power balance with FLYCHK steady-state radiation
and charge states. The MHD flush is not simulated; it enters as a
Gaussian-in-time radial diffusivity acting only on passing electrons. The
central finding is a new seed: neon pitch-angle scattering on the plateau puts
relativistic electrons into the magnetically trapped region, which stochastic
transport does not reach and from which energetic electrons detrap slowly.
This remnant is 0.1–1% of the initial RE population (as stated in the text),
orders of magnitude above the few-ampere nuclear seed. After rehealing it
detraps (pitch-angle scattering plus a Ware pinch) and avalanches back.
Residual neon drains the seed but makes the avalanche more efficient; the two
effects largely cancel, so the reformed current hardly depends on the purge
fraction (0.6–0.975). A 16-fold longer open-surface time (0.09 to 1.43 ms)
only halves the reformed current. Conclusion: about a 2–3 MA current drop
before reconstitution, unless detrapping is enhanced or the surfaces are held
open longer (passive runaway coil).

# Key claims

Page-local symbols (not in the registry): $\xi=p_\parallel/p$ the pitch of an
electron, $\xi_{\mathrm{tp}}$ its trapped–passing boundary; $\psi_{10}$ the
poloidal flux needed for a tenfold avalanche gain; $D_{\mathrm{RE}}$ the
stochastic radial diffusivity of REs and $\tau_{\mathrm{st}}=a^2/D_{\mathrm{RE}}$
its transport time; $\Delta t_{\mathrm{open}}$ the duration of the MHD event;
$f_{\mathrm{purge}}$ the fraction of neon removed; $N_{\mathrm{RE}}$ the number of
REs; $I_{\mathrm{RE}}$ the RE current.

1. **Trapped electrons survive a globally stochastic field** (Fig. 1, p. 2).
   In an imposed fully stochastic field, passing electrons with
   $|\xi|\gtrsim0.5$ are lost in well under 1 ms while trapped electrons stay
   up to ≈10 ms at 3 MeV; their loss is set by detrapping, which slows with
   energy. Shown (test-particle loss-time map); physics attributed to Mynick &
   Krommes, Chandran & Cowley, Helander & Sigmar. The method behind Fig. 1 is
   not described.
2. **Upper bound on the reconstituted current** (Eq. 1).
   $I_{\mathrm{RE}}^{\max}=2\pi\int_0^a r\,J_{\mathrm{RE}}^{\mathrm{seed}}(r)\,10^{|\psi(r)/\psi_{10}(r)|}\,dr$,
   if all available flux amplifies the seed; minimizing reconstitution means a
   larger $\psi_{10}$ and a smaller seed. Stated (no derivation).
3. **Favourable on paper, not in practice** (p. 2). The purge raises
   $\psi_{10}$ and low $T_e$ removes Dreicer and hot-tail seeds, leaving tritium
   and Compton; this is "not fully borne out" because of trapped seeding.
   Stated, then Shown.
4. **Remnant seed size** (p. 4, Fig. 3, Discussion). "Between a percent to a
   tenth of a percent of the original RE beam", "orders of magnitude larger
   than the nuclear seed" of "a few ampere". Shown; the plotted Fig. 3(b) range
   differs (see Citations).
5. **Transition at $\Delta t_{\mathrm{open}}\sim\tau_{\mathrm{st}}$** (Fig. 3).
   Below it the RE number drops sharply (passing loss); above it a sharp drop is
   followed by a slow decay of the trapped population, so the minimum
   $N_{\mathrm{RE}}$ depends weakly on $\Delta t_{\mathrm{open}}$. Shown.
6. **Purge-fraction insensitivity** (Fig. 4, pp. 4–5). $f_{\mathrm{purge}}=0.6$,
   0.9, 0.975 reform ≈2.4–2.5 MA from a ≈5.4 MA plateau (plot reading).
   Retained neon increases detrapping, directly and through a larger inductive
   $E_\parallel$ in the radiatively colder plasma, whose Ware pinch moves trapped
   electrons inward where they detrap more easily; neon also lowers $\psi_{10}$
   ($\psi_{10}/(\mu_0R_0)$ ≈0.55–1.05 MA over $r/a\le0.5$). Shown. Fig. 4a also
   shows faster reconstitution at lower $f_{\mathrm{purge}}$ (≈75 against
   ≈160 ms, plot reading), not commented on.
7. **Weak dependence on MHD duration** (Fig. 5). ×16 in
   $\Delta t_{\mathrm{open}}$ (0.09 → 1.43 ms) lowers the reformed current "from
   3.9 MA to 2.0 MA"; the current drop becomes a weak function of
   $\Delta t_{\mathrm{open}}$ once $\Delta t_{\mathrm{open}}\gg\tau_{\mathrm{st}}$
   (≈1.1 MA at 0.35$\tau_{\mathrm{st}}$ to ≈3.4 MA at ≈11$\tau_{\mathrm{st}}$).
   Shown; the printed numbers do not match the figure (see Citations).
8. **Headline** (Discussion, Abstract). "For most cases of interest
   $\psi_{10}/\mu_0R_0\lesssim1$ MA, so runaway reconstitution comes with a 2-3
   MA plasma current drop." Shown for the cases computed; generalized by
   argument (Stated).
9. **Mitigation levers** (Discussion). Enhance detrapping (higher post-purge
   deuterium density, constrained by assimilation and by the density window
   for triggering the flush) or prolong $\Delta t_{\mathrm{open}}$; a passive
   runaway coil is "a more reliable alternative". Stated.
10. **Avoidance scenario** (Introduction). With a complete enough purge and not
    too much deuterium, Ohmic reheating keeps $\eta j_\parallel$ below the
    avalanche threshold field, which requires a "goldilocks" density consistent
    with an Ohmic current-decay time of 50–150 ms in ITER. Stated.
11. **Experimental premise** (p. 1). In JET and DIII-D massive deuterium
    injection purges high-Z impurities and triggers large MHD; parallel
    streaming in the stochastic field expels the beam regardless of the
    specific modes, with a broad wall load; a 15 MA ITER discharge could give
    >10 MA of RE current. Stated (attributed).
12. **Robustness** (p. 1, Discussion). The trapped-seed route makes
    reconstitution "far more robust" than initial plateau formation. Shown
    within the model.
13. **Modelling recommendation** (Discussion). Machine-specific modelling must
    follow the 3D MHD evolution, the full VDE dynamics and the impurity purge,
    all idealized here. Stated.

# Models and numerics

* **Architecture.** 1D radial disruption model with nested circular flux
  surfaces, coupling (i) a drift-kinetic Monte Carlo RE solver (McDevitt, Guo &
  Tang 2019), (ii) poloidal-flux diffusion and (iii) power balance. No MHD code;
  the code is not named.
* **Flux diffusion** (Eq. 2), with $\langle\cdot\rangle$ the flux-surface average
  and Ohm's law $E_\parallel=\eta(j_\parallel-J_{\mathrm{RE},\parallel})$:
  $$\left.\partial_t\psi\right|_r=\frac{\eta}{\mu_0}\frac{1}{\langle R^{-2}\rangle}\frac1r\partial_r\Big[r\langle R^{-2}\rangle\partial_r\psi\Big]-\frac{\eta}{B_{\phi0}R_0}\frac{\langle\mathbf J_{\mathrm{RE}}\cdot\mathbf B\rangle}{\langle R^{-2}\rangle},$$
  $B_{\phi0}$ the on-axis field; ideal conducting wall $\psi(a)=0$ (called
  idealized).
* **Power balance** (Eq. 3), one temperature $T$ for electrons, ions and
  neutrals, $p=n_eT+T\sum_jn_j$:
  $$\tfrac32\partial_tp=\frac1r\partial_r\big(rn\chi_\perp\partial_rT\big)-P_{\mathrm{rad}}+P_{\mathrm{RE}}+E_\parallel^2/\eta,$$
  $\chi_\perp=1$ m²/s, $P_{\mathrm{RE}}$ bulk heating by RE slowing-down (words;
  not registered), FLYCHK charge states and $P_{\mathrm{rad}}$ in steady state (no
  time-dependent ionization balance). The density $n$ in the conduction term is
  not defined.
* **Imposed thermal quench.** $T=[T_{\mathrm{init}}-T_{\mathrm{final}}]e^{-t/\Delta t_{\mathrm{TQ}}}+T_{\mathrm{final}}$,
  $T_{\mathrm{final}}=10\,\mathrm{eV}\,[1-0.7(r/a)^2]$,
  $T_{\mathrm{init}}=3.1\,\mathrm{keV}\,[1-0.7(r/a)^2]^2$,
  $n_e=n_{\mathrm D}=2.8\times10^{19}\,\mathrm m^{-3}\,[1-0.9(r/a)^2]^{2/3}$;
  $\Delta t_{\mathrm{TQ}}$ not given. The hot-tail seed forms and avalanches into a
  plateau.
* **Injection sequence.** Neon into the beam at $t\approx18$ ms
  ($n_{\mathrm{Ne}}=5.6\times10^{19}$ m$^{-3}$); tenfold deuterium increase at
  $t\approx28$ ms; then a fraction $f_{\mathrm{purge}}$ of neon removed by hand.
  Prescribed density changes, not material transport.
* **Flush model** (Eq. 4), Rechester–Rosenbluth-like, passing electrons only:
  $$D_{\mathrm{RE}}^{\mathrm{kin}}=\frac{|v_{\parallel p}|}{c}\,\Theta\big[|\xi|-\xi_{\mathrm{tp}}(r,\theta)\big]\,D_{\mathrm{RE}},\qquad D_{\mathrm{RE}}=\frac{1}{4N_t}\frac{a^2}{2\pi R_0/c},$$
  $N_t$ the number of toroidal transits of a stochastic field line (value not
  given), modulated by $\exp[-(t-t_{\mathrm{open}})^2/\Delta t_{\mathrm{open}}^2]$;
  $\tau_{\mathrm{st}}\approx0.26$ ms (Fig. 5 caption).
* **Fig. 1 model.** Electrons traced in $\delta\mathbf B=\nabla\times(\alpha\mathbf B)$,
  $\alpha=\sum\alpha_{m,n}(r)\cos(m\theta-n\phi+\delta_{m,n})$, $n\in[1,6]$,
  $m\in[1,24]$, amplitudes raised until no integrable region remains; start at
  $r/a=0.5$; $n_{\mathrm D}=5\times10^{20}$ m$^{-3}$, $E_\parallel/E_c=50$,
  $B=5.3$ T, $a=2$ m. Orbit model, collisions and statistics not described.
* **Main runs.** $I_p\approx8$ MA initial (plateau ≈5.4 MA), $a=2$ m,
  $B_{\phi0}=3$ T ("ITER-like"); $f_{\mathrm{purge}}$ and $\Delta t_{\mathrm{open}}$
  varied.
* **Numerics.** No information on time stepping, radial grid, marker numbers,
  solvers, parallelism or cost (NERSC, LANL Institutional Computing).

# Tests and results

No benchmark or code-to-code comparison; parameter scans of the reduced model.

| Case | Result (plot readings unless printed) |
|---|---|
| Reference, $f_{\mathrm{purge}}=0.9$, $\Delta t_{\mathrm{open}}\approx1.43$ ms (Fig. 2) | MHD peak at printed $t\approx35.8$ ms; nearly all RE current lost; trapped relativistic electrons remain; recovery to ≈2.5 MA |
| $N_{\mathrm{RE}}(t)$ (Fig. 3a) | from ≈$5\times10^{18}$ to minima ≈$1.4\times10^{17}$ (0.179 ms) and ≈$3\times10^{16}$ (1.43 ms) |
| Minimum fraction vs $\Delta t_{\mathrm{open}}/\tau_{\mathrm{st}}=0.35$–11.4 (Fig. 3b) | ≈$9\times10^{-2}$ → ≈$3\times10^{-3}$, flat beyond ≈3 |
| $f_{\mathrm{purge}}=0.6/0.9/0.975$ (Fig. 4) | final ≈2.4–2.5 MA; $\psi_{10}/(\mu_0R_0)$ ≈0.55–0.75, 0.61–0.94, 0.71–1.05 MA |
| $\Delta t_{\mathrm{open}}\approx0.09/0.36/1.43$ ms (Fig. 5) | printed 3.9 → 2.0 MA; figure final ≈4.2, 3.2, 2.4 MA; drop ≈1.1 → 3.4 MA |

# Notation map

| McDevitt & Tang (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $r$, $a$, $R$, $R_0$ | $r$, $a$, $R$, $R_0$ | $R_0$ never given numerically |
| $\theta$, $\varphi$ | $\theta$, $\phi$ | geometric; orientation not stated |
| $B_0$ | $B_{\phi0}$ (words: on-axis field) | 3 T main runs, 5.3 T in Fig. 1 |
| $\mathbf B_{eq}$, $\delta\mathbf B$, $\alpha$, $\alpha_{m,n}$ | $\mathbf B$, $\delta\mathbf B$, page-local | |
| $B_{Max}$ | maximum of $B$ on the surface (words) | |
| $\psi$ | $\psi$ | per radian inferred from Eq. 2, not stated |
| $\psi_{10}$ | $\psi_{10}$ (page-local) | not registered |
| $j_\parallel$, $j_{RE}$, $j_{RE}^{(seed)}$ | $j_\parallel$, $\mathbf J_{\mathrm{RE}}$, $J_{\mathrm{RE}}^{\mathrm{seed}}$ | |
| $I_{RE}$, $I_{RE}^{(max)}$, $\Delta I_{RE}$ | $I_{\mathrm{RE}}$ (page-local) | |
| $E_{AV}$ | words (avalanche threshold field), closest $E_c^{\mathrm{eff}}$ | not formally defined in the paper |
| $\chi$ | $\chi_\perp$ | **collision:** registry $\chi$ is the vacuum scalar potential |
| $S_{rad}$, $S_{RE}$ | $P_{\mathrm{rad}}$, $P_{\mathrm{RE}}$ (words) | **collision:** registry $S$ is the Lundquist number; $S_{\mathrm{av}}$ etc. are RE sources |
| $\xi=p_\parallel/p$, $\xi_{trap}$ | $\xi$, $\xi_{\mathrm{tp}}$ (page-local) | **collision risk:** registry $\xi_{\mathrm t}$ is a time-scheme weight |
| $\gamma$ | words (Lorentz factor) | **collision:** registry $\gamma$ is a growth rate |
| $v_\parallel$, $p_\parallel$, $p$ (momentum) | $v_{\parallel p}$; words | **collision:** $p$ is the pressure |
| $D_{RE}^{kin}$, $D_{RE}$ | $D_{\mathrm{RE}}^{\mathrm{kin}}$, $D_{\mathrm{RE}}$ (page-local) | not the fluid $D_\perp$ |
| $N_t=N_{transit}$, $\tau_{transit}$ | $N_t$, words | |
| $\tau_{trans}=a^2/D_{RE}$ | $\tau_{\mathrm{st}}$ (page-local) | |
| $t_{open}$, $\Delta t_{open}$, $f_{purge}$, $N_{RE}$ | page-local | |
| $T$, $T_e$ | $T$ | single temperature, stated |
| $n_D$, $n_{Ne}$, $n_j$ | $n_{\mathrm D}$, $n_{\mathrm{Ne}}$ (page-local), $n_{\mathrm{imp}}$ | cm$^{-3}$ and m$^{-3}$ both used |

SI with explicit $\mu_0$; no normalized units.

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below. This source is cited on:

* [Coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)
* [ITER runaway-electron benchmarks (JOREK–GO, JOREK–DINA)](/benchmarks/iter-runaway-electron-benchmarks.md)
* [Runaway current reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Runaway-electron fluid model coupled to MHD](/methods/runaway-electron-fluid-model.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Physical_Review_E_McDevitt_Runaway_electron_current_reconstitution_after_a_nonaxisymmet.pdf`.
   * **Version.** Accepted manuscript distributed via CHORUS (cover page + 5
     pp. of text and references, 7 PDF pages including a blank last page),
     manuscript dated 20 September 2023; not the publisher typeset version.
   * **Identity.** doi:10.1103/PhysRevE.108.L043201, checked on Crossref: Phys.
     Rev. E 108(4), article L043201 (Letter), issued 2023-10-16; authors
     McDevitt, Tang. The manuscript title prints "non-axisymmetric"; Crossref and
     the CHORUS cover print "nonaxisymmetric" (used here).
   * **How read.** Full text; Eqs. 1–4 checked on the rendered page; figure
     values are approximate readings.
   * **Recorded as printed.**
     * Fig. 2 caption: "after [$t-t_{TQ}\approx47$ ms, panel (c)]" should be
       panel (d); (c) is also assigned to "during". The text's MHD peak at
       $t\approx35.8$ ms is not clearly $t$ or $t-t_{TQ}$ (snapshots labelled
       33, 39, 47 ms; drop at ≈37–40 ms on the plotted axis).
     * $\xi_{trap}=1-B/B_{Max}$ as printed; the standard boundary is
       $\sqrt{1-B/B_{\max}}$, and Fig. 1's boundary $|\xi_0|\approx0.5$ at
       $r/a=0.5$ matches the square-root form ($\approx0.53$ for
       $\varepsilon\approx0.16$), not $\approx0.28$ (compiler's check).
     * $N_t$ in the formula, $N_{transit}$ in the definition; value never
       given. $D_{RE}(t)=D_{RE}^{kin}\exp[\dots]$ reuses $D_{RE}$, already the
       amplitude inside $D_{RE}^{kin}$.
     * Remnant seed: text "1% to 0.1%"; Fig. 3(b) spans ≈9% to ≈0.3%, Fig. 3(a)
       minima ≈3% and ≈0.6% (plot readings).
     * Reformed current "from 3.9 MA to 2.0 MA": Fig. 5(a) reads ≈4.2 → 2.4 MA,
       Fig. 5(b) drops imply ≈4.3 → 2.5 MA from a 5.4 MA plateau (plot
       readings).
     * Fig. 3's shortest case (0.179 ms) is called "comparable to"
       $\tau_{trans}$ (0.69$\tau_{trans}$) but is not the shortest of the
       Fig. 3(b) scan (0.35$\tau_{trans}$).
     * "ITER-like" runs use 3 T and ≈8 MA; Fig. 1 uses 5.3 T and a different
       density; $R_0$ never stated although $\tau_{transit}$ and
       $\psi_{10}/\mu_0R_0$ depend on it ($N_t\sim500$ if $R_0\approx6.2$ m,
       reader's inference).
     * Undefined: $\Delta t_{TQ}$, $n$ in Eq. 3, how $\psi_{10}$ is "inferred",
       the Fig. 1 orbit and collision model, the code name, resolution.
     * Abstract "two of which compete"; units mixed ($a=200$ cm, cm$^{-3}$ and
       m$^{-3}$).
   * **Reference list.** 47 printed entries, merged into the bibliography under
     `mcdevitt-2023`. Refs. [5] and [11] are the same work (Hender et al. 2007,
     NF 47 S128) → one entry `hender-2007`. Key decisions: Paz-Soldan et al. NF
     61:116058 (ref. [7], DIII-D) is `pazsoldan-2021-b`; C. Liu et al. NF
     61:036011 (ref. [42]) is `liu-2021-b`, not the ingested `liu-2021`;
     McDevitt arXiv:2306.13224 (ref. [36]) is `mcdevitt-2023-b`; Zhang Y.-K. CPB
     2021 (ref. [22]) is `zhang-2021-b`, not the ingested
     [Zhang et al. (2021)](/sources/zhang-2021.md); ref. [10] (ITER Physics
     Expert Group on Disruptions, NF 39:2251, author printed garbled) is
     `iter-1999-c`; [41] is `hesslow-2018-b`, [33] `matsuyama-2017-b`; [23] is
     `sarkimaki-2022` (printed NF 62:086033). No journal-article titles are
     printed; [40] lacks volume and page, [41] the article number, and [44] is a
     REM-meeting talk with a lower-case title.
