---
type: Source
title: "Schekochihin (2022) — MHD turbulence: a biased review"
description: "Pedagogical review of scaling theories of incompressible MHD turbulence in the reduced-MHD limit: weak turbulence and its condensate, critical balance, dynamic alignment as an intermittency effect, tearing-mediated turbulence, imbalance, residual energy, subviscous turbulence, decaying turbulence and its invariants, and the saturated small-scale dynamo."
resource: "doi:10.1017/s0022377822000721"
source_kind: paper
authors: [Schekochihin A.A.]
year: 2022
venue: "J. Plasma Phys. 88:155880501"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Plasma_Physics_Schekochihin_MHD_turbulence_a_biased_review.pdf"
tags: [mhd, critical-balance, dynamic-alignment, reconnection, dynamo, review]
timestamp: 2026-10-25T13:42:00Z
---

# Summary

Schekochihin (2022) is a 200-page, self-described "biased" and pedagogical
review of phenomenological scaling theories of incompressible MHD turbulence,
chiefly in the limit of a strong guide field described by
[reduced MHD](/definitions/reduced-mhd.md) in Elsasser variables
$\boldsymbol Z^\pm$. It is peripheral to closure modelling: it contains no
RANS, LES or wall model, and bears on this bundle through the cascade
phenomenology and the resolution requirements of MHD simulations. The method
throughout is order-of-magnitude scaling, checked against published and
unpublished simulations and solar-wind data.

Part I runs chronologically from Kolmogorov and Iroshnikov–Kraichnan through
Goldreich–Sridhar and [critical balance](/properties/critical-balance.md)
($\tau_A\sim\tau_{\mathrm{nl}}$, with the robust parallel spectrum
$E(k_\parallel)\propto k_\parallel^{-2}$) to Boldyrev's
[dynamic alignment](/properties/dynamic-alignment.md). Three results stand
out: weak Alfvén-wave turbulence is asymptotically irrelevant and, in its
standard form, incomplete, because its $k_\parallel=0$ condensate is strongly
turbulent; Boldyrev's alignment violates the rescaling symmetry of reduced
MHD, but survives reinterpreted as an intermittency effect in which the
parallel outer scale enters, giving $E(k_\perp)\propto k_\perp^{-3/2}$ and
$\sin\theta_\lambda\sim(\lambda/\lambda_{CB})^{1/4}$; and aligned sheets are
disrupted by tearing below
$\lambda_D\sim\lambda_{CB}Rm^{-4/7}(1+Pm)^{-2/7}$, beyond which a
[tearing-mediated cascade](/results/tearing-mediated-mhd-turbulence.md) with a
$k_\perp^{-11/5}$ envelope restores a Kolmogorov-type dissipation scale.

Part II covers a new theory of imbalanced turbulence, residual energy,
subviscous ($Pm\gg1$) turbulence, [decaying MHD turbulence](/results/decaying-mhd-turbulence.md)
as reconnection-controlled selective decay constrained by Saffman-type
invariants (the Hosking invariant of the magnetic helicity density, the
Saffman cross-helicity invariant), a new tearing-limited theory of the
saturated [small-scale dynamo](/results/small-scale-dynamo.md), and frontiers
of kinetic plasma turbulence. Appendices derive weak turbulence, the
alignment geometry, the two-dimensional spectra of critically balanced
turbulence and a primer on reconnection (tearing, Sweet–Parker, plasmoids,
stochastic reconnection).

# Version read

arXiv preprint arXiv:2010.00699v3 [physics.plasm-ph], 19 July 2022 ("Under
consideration for publication in J. Plasma Phys.", compiled 21 July 2022), not
the JPP typeset version of record; 200 pages (main text pp. 1–131, appendices
A–D pp. 131–179, references pp. 179–200), all read. The metadata above are
those of the published version (J. Plasma Phys. 88:155880501); the DOI is not
printed on the copy read. The page-1 title is set in title case ("MHD
Turbulence: A Biased Review"). Section, equation, figure and page numbers on
this page are those of the arXiv v3.

# Key claims

1. Reduced MHD is invariant under a simultaneous rescaling of amplitudes,
   parallel and perpendicular gradients, time and dissipation coefficients
   ($Z^\pm_\perp\to c\,Z^\pm_\perp$, $\nabla_\parallel\to(c/a)\nabla_\parallel$,
   $\nabla_\perp\to\nabla_\perp/a$, $t\to(a/c)t$,
   $\eta_m\to a\,c\,\eta_m$); any scaling theory must respect it, and the
   parallel-to-perpendicular aspect ratio of a simulation box is arbitrary (§3,
   Eq. 3.5; after Beresnyak). **Derived**
2. The exact third-order law of reduced MHD is
   $\langle\delta Z_L^\mp\lvert\delta Z^\pm_\lambda\rvert^2\rangle=-2\varepsilon^\pm\lambda$
   (Eq. 3.7; Politano & Pouquet, adjusted by Boldyrev et al.). **Stated**
3. Weak turbulence is irrelevant asymptotically: a weakly driven cascade
   reaches critical balance at
   $\lambda_{CB}\sim\varepsilon^{1/2}(L_\parallel/v_A)^{3/2}$, the only
   dimensionally correct scale built from $\varepsilon$ and $L_\parallel/v_A$
   (Eqs. 4.3, 4.8); the transition was first captured numerically by Meyrand
   et al. (2016). **Derived** + **Shown** (cited)
4. The balanced weak-turbulence spectrum is
   $E(k_\perp)\sim(\varepsilon/\tau_A)^{1/2}k_\perp^{-2}$ (Eq. 4.7); in
   unpublished weak runs the unforced $k_\parallel=0$ modes form a condensate
   with a spectrum near $k_\perp^0$, against the $k_\perp^{-1}$ of the author's
   earlier theory (§4.4, Fig. 4). **Derived** + **Shown**
5. With broad-band forcing, the condensate is a strongly turbulent,
   critically balanced subsystem with
   $E_{0,2D}\sim(\varepsilon L_\parallel v_A)^{1/2}k_\perp^{-2}$, a physical
   argument for spectral continuity (App. A.4, Eqs. A26–A30). **Derived**
   (new in the review)
6. Critical balance $\tau_A\sim\tau_{\mathrm{nl}}$ follows from causality and
   from the weak-to-strong transition, and gives the parallel spectrum
   $E^\pm(k_\parallel)\sim(\varepsilon^\pm/v_A)k_\parallel^{-2}$ (Eq. 5.1),
   called "the least controversial" result (§5.2). **Derived** + **Shown**
   (cited)
7. Scale-dependent anisotropy appears only when increments are measured
   along the local field (Eq. 5.9); along the global mean field, parallel
   correlations are swamped by perpendicular decorrelation (Eq. 5.8, §5.3).
   **Derived**
8. Boldyrev's alignment $\sin\theta_\lambda\sim\delta b_\lambda/v_A$ (Eq. 6.5)
   gives $E(k_\perp)\sim(\varepsilon v_A)^{1/2}k_\perp^{-3/2}$ (Eq. 6.8) but
   violates the rescaling symmetry; with $\varepsilon$, $v_A$ and $\lambda$
   alone, Goldreich–Sridhar is the unique admissible scaling (§6.3–6.4.1;
   credited to Beresnyak). **Derived**
9. Letting $L_\parallel$ enter rescues alignment:
   $\delta Z_\lambda\sim(\varepsilon L_\parallel/v_A)^{1/2}(\lambda/\lambda_{CB})^{1/4}$,
   $l_\parallel/L_\parallel\sim(\lambda/\lambda_{CB})^{1/2}$,
   $\sin\theta_\lambda\sim(\lambda/\lambda_{CB})^{1/4}$ (Eqs. 6.14–6.22, with the
   intermittency exponent $q=1/8$, the source's $\delta$). **Derived** (heuristic form of
   Mallet & Schekochihin 2017)
10. $q=1/8$ follows from an intermittency model in which the most intense
    structures are sheets of scale-independent amplitude obeying refined
    critical balance (Eqs. 6.26–6.30); Chandran et al. (2015) obtain
    $q\approx0.108$ (§6.4.2). **Derived** + **Shown** (cited)
11. Refined critical balance: the distribution of $\tau_A/\tau_{\mathrm{nl}}$,
    with the alignment angle in $\tau_{\mathrm{nl}}$, is scale-invariant to
    "truly remarkable accuracy" in a $1024^3$ simulation, and fails to collapse
    without the angle (Mallet et al. 2015; Fig. 6). **Shown** (cited)
12. The Elsasser fields have spectral exponents $-2$ along $l_\parallel$,
    $-3/2$ along $\lambda$ and $-5/3$ along the fluctuation direction $\xi$,
    with $\xi\sim\lambda_{CB}^{1/4}\lambda^{3/4}$ (Eq. 6.31, §6.5). **Derived**
    + **Shown** (cited)
13. Aligned structures are disrupted by the fastest tearing mode below
    $\lambda_D\sim Rm^{-4/7}(1+Pm)^{-2/7}\lambda_{CB}$ (Eq. 7.2), with
    $Rm\sim(\varepsilon/\eta_m)(L_\parallel/v_A)^2$ (Eq. 6.23); each disrupted
    sheet carries $N\sim Rm^{1/14}(1+Pm)^{2/7}$ islands (Eq. 7.6). **Derived**
    (Mallet et al. 2017b; Loureiro & Boldyrev 2017b)
14. The tearing-mediated cascade is a ladder of aligned mini-cascades with a
    spectrum bounded by
    $\varepsilon^{2/3}k_\perp^{-5/3}\lesssim E(k_\perp)\lesssim\varepsilon^{4/5}\eta_m^{-2/5}(1+Pm)^{1/5}k_\perp^{-11/5}$
    (Eqs. 7.9–7.15). **Derived**
15. The Kolmogorov cutoff is restored,
    $\lambda_{\mathrm d}^{\mathrm K}\sim(\nu+\eta_m)^{3/4}\varepsilon^{-1/4}$ (Eq.
    7.19), which reconciles the evidence for a Kolmogorov dissipation scale with
    an aligned $-3/2$ inertial range ("both are right, in a sense", §1,
    §7.2.2). **Derived**
16. Seeing the disruption scale in simulations needs $Rm\gtrsim10^5$ ("the
    smallest large number is 3"); fast-reconnection-mediated turbulence in the
    aligned range needs $Rm\gtrsim10^{14}(1+Pm)^3$ (Eq. 7.26; §7.2.2, §7.3).
    **Derived**
17. Dong et al. (2018) find a $k_\perp^{-11/5}$ spectrum below a break at the
    disruption scale in two dimensions at $Rm=10^6$ on a $64\,000^2$ grid
    (§7.3, Fig. 15). **Shown** (cited)
18. Critical balance and the parallel cascade are "quite safe"; the aligned
    cascade, its disruption and the tearing-mediated range are "hotly debated"
    (§8.2). **Stated**
19. "Waves against structures" is a false dichotomy, and stochastic
    reconnection does not invalidate the aligned or tearing-mediated cascade
    (§8.3, App. D.7.4). **Derived**
20. In strongly imbalanced turbulence, simulations show a steeper spectrum for
    the stronger field, an energy ratio growing at least as
    $(\varepsilon^+/\varepsilon^-)^2$ (Eq. 9.1), and a robust $k_\parallel^{-2}$
    parallel spectrum for the weaker field (§9.2, Fig. 19). **Shown** (cited and
    unpublished)
21. A new imbalanced theory with two semi-local cascades and pinning at the
    dissipation scales makes the spectral exponents of the two fields tend to
    each other asymptotically, with logarithmic finite-Reynolds-number
    corrections (§9.6, Eqs. 9.17–9.26). **Derived** (new)
22. Elsasser alignment implies nonzero residual energy; current sheets
    dominate the most intense structures, and a $k_\perp^{-2}$ residual spectrum
    is an intermittency effect (§10.4). **Derived** (heuristic, new)
23. In subviscous ($Pm\gg1$) turbulence there is no parallel cascade; the
    magnetic spectrum is $\propto k_\perp^{-1}$ (sharp stripes, Eq. 11.5) and
    the velocity spectrum $\propto k_\perp^{-4}$ (Eq. 11.9); tearing occurs in
    the subviscous range when $Pm\gtrsim Re^{1/9}$ (§11). **Derived**
24. Selective decay: two-dimensional MHD decays as $t^{-1}$ with the
    energy-containing scale growing as $t^{1/2}$ (Eq. 12.4); in
    reconnection-controlled decay the reconnection rate replaces the ideal rate
    (Eqs. 12.10–12.13). **Derived** (Zhou et al. 2019; Hosking & Schekochihin
    2021)
25. The Hosking invariant
    $I_H=\int d^3l\,\langle H_m(\boldsymbol r)H_m(\boldsymbol r+\boldsymbol l)\rangle$,
    $I_H\sim b^4L^5$, gives the non-helical decay laws: magnetic energy
    $\propto t^{-10/9}$ and scale $\propto t^{4/9}$ with fast reconnection,
    $t^{-20/17}$ and $t^{8/17}$ with Sweet–Parker reconnection (Eqs.
    12.20–12.27); hyperdissipative simulations discriminate them from earlier
    theories (Fig. 27). **Derived** + **Shown** (cited)
26. The Saffman cross-helicity invariant, together with helicity, recovers the
    Biskamp–Müller decay laws (Eq. 12.29) and, in reduced MHD, the decay
    $\langle b_\perp^2\rangle\propto t^{-1}$, $L_\perp\propto t^{1/2}$,
    $L_\parallel\propto t$ (Eqs. 12.39–12.41). **Derived**
27. In the saturated small-scale dynamo, resistive folds tear: the
    fold-reversal scale is $\lambda_R\sim L\,Rm_L^{-1/3}(1+Pm)^{-1/6}$
    (Eq. 13.9) rather than the Ohmic $L\,Rm^{-1/2}$, and torn folds seed a
    local, critically balanced, aligned and tearing-disrupted cascade
    (Eqs. 13.10–13.16); simulations up to $2240^3$ give tentative support
    (§13.3.4). **Derived** + **Stated** (cited)
28. Saturated-dynamo simulations show the kinetic-energy spectrum steepening at
    large scales and flattening at small scales, consistent with magnetic
    tension driving flows at small scales (§13.2, Fig. 33). **Stated** (cited)
29. Imbalanced cascades in low-beta kinetic plasmas are fragile (the
    helicity of kinetic Alfvén waves blocks a constant-flux state); pressure
    anisotropy alters Alfvén waves above $\delta b/v_A\gtrsim\beta_p^{-1/2}$
    (§14, Eq. 14.2). **Stated** (cited)
30. The two-dimensional spectrum of critically balanced turbulence is
    $E_{2D}\sim k_\parallel^{-6}k_\perp$ above the critical-balance line and
    $\sim k_\perp^{-2}$, flat in $k_\parallel$, below it; the flat part is the
    Fourier signature of causality, not of quasi-two-dimensional motions (App.
    C, Eq. C23). **Derived**

# Printed slips

- **Eq. (7.17), p. 46.** Printed:
  "$\lambda_\eta\sim\varepsilon^{-3/4}\eta^{3/4}(1+\mathrm{Pm})^{3/2}\sim\lambda_{CB}\mathrm{Rm}^{-3/4}(1+\mathrm{Pm})^{3/2}$".
  From Eqs. (4.3) and (6.23), $\lambda_{CB}Rm^{-3/4}=\varepsilon^{-1/4}\eta_m^{3/4}$,
  and $\varepsilon^{-3/4}\eta_m^{3/4}$ has the dimension of a time to the power
  $3/2$, not of a length; the exponent of $\varepsilon$ is $-1/4$, as in
  Eqs. (6.11), (7.16) and (7.19) *(compiler check, not in the sources)*.
- **§7.2.2, p. 46.** "the condition for the range $[\lambda_D,\lambda^K_\eta]$
  to be non-empty", but Eq. (7.18) uses $\lambda^{\rm tearing}_\eta$ of
  Eq. (7.17); $\lambda^K_\eta$ is introduced only in Eq. (7.19).
- **§12.2.1, p. 83.** "the assumption of ideal dynamics ($U\sim B$) in § 12.4
  was flawed": the two-dimensional theory with $U\sim B$ is §12.1.1, Eq. (12.4);
  §12.4 is the section on Saffman invariants.
- **§12.5.2, p. 96.** The text gives $E_{\max}\propto t^{(1+2m)/(1-h)}$ as
  "$\propto t^{-1/2}$ for the non-helical one (figure 28b)". With the
  fast-reconnection exponents $m=h=-5/4$ of Eq. (12.26) the formula gives
  $t^{-2/3}$; $t^{-1/2}$ corresponds to $m=h=-1$ *(compiler check, not in the
  sources)*. The text does not say which $(m,h)$ is meant.
- **§13.3.4, p. 111** (checked on the rendered page). Galishnikova et al.
  (2022) are reported to support "the $\lambda_{\rm R}\propto{\rm Rm}^{1/3}$
  scaling of the field-reversal scale", and footnote 79 gives their form as
  "$\lambda_{\rm R}\propto{\rm Rm}^{3/10}{\rm Pm}^{1/5}$", both with positive
  exponents, whereas Eq. (13.9), p. 109, prints
  $\lambda_R\sim L\,Rm_L^{-1/3}(1+Pm)^{-1/6}$. The same balance with the
  $n=2$ growth rate of Eq. (D40) gives $\lambda_R\sim L\,Rm_L^{-3/10}(1+Pm)^{-1/5}$
  *(compiler check, not in the sources)*.
- Typos: "saws the seeds of its own destruction" (§4.2); "tearing-mediate
  cascade" (§7.2.2); "at the and of this section" (App. D.5.2); "the the role"
  (§11.2).

# Notation map

| Schekochihin (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol B_0$, $\hat{\boldsymbol z}$ | $\boldsymbol B_0$ | guide field and its direction |
| $\mathbf b_\perp$ | $\boldsymbol b$ | velocity (Alfvénic) units throughout; agrees |
| $v_A=B_0/\sqrt{4\pi\rho_0}$ | $v_A$ | Gaussian units; agrees |
| $\mathbf Z^\pm_\perp=\mathbf u_\perp\pm\mathbf b_\perp$ | $\boldsymbol Z^\pm$ | $Z^+$ propagates along $+\boldsymbol B_0$; agrees |
| $\eta$ | $\eta_m$ | magnetic diffusivity. **Collision**: the registry $\eta$ is the Kolmogorov length; until §6.4 the source takes $\nu=\eta$ |
| $\mathrm{Pm}$, $\mathrm{Rm}$, $\widetilde{\mathrm{Re}}$ | $Pm$, $Rm$, $Re_{\mathrm{eff}}=\delta Z_{\lambda_{CB}}\lambda_{CB}/(\nu+\eta_m)$ (page-local) | $Rm$ on the outer scale $\lambda_{CB}$ (Eq. 6.23); tilde is not a Favre filter |
| $S_\lambda=v_{Ay}\lambda/\eta$ | $S_{L,\lambda}$ ($S_L$ at scale $\lambda$) | Lundquist number based on the sheet width; **not** the strain rate |
| $\varepsilon$, $\varepsilon^\pm$ | $\varepsilon$ | energy flux (injection rate) of the total and Elsasser energies |
| $\epsilon$, $a$ | $c$, $a$ (page-local rescaling factors) | amplitude and length factors of Eq. 3.5 |
| $\lambda$, $\xi$, $l_\parallel$, $L_\parallel$, $L_\perp$ | $\lambda$, $\xi$, $l_\parallel$; parallel and perpendicular outer scales | **collision**: $\lambda$ is not the Taylor microscale (MHD pages only) |
| $\lambda_\eta$ (Eq. 6.10), $\lambda^K_\eta$, $\lambda^{\rm tearing}_\eta$ | dissipation cutoffs: $\lambda_{\mathrm d}^{\mathrm B}$ (Boldyrev), $\lambda_{\mathrm d}^{\mathrm K}$ (Kolmogorov) on the concept pages | subscript $\eta$ refers to the source's diffusivity, not the Kolmogorov length |
| $\lambda_{CB}$, $\lambda_D$, $\lambda_R$ | critical-balance, disruption and fold-reversal scales | page-local on the concept pages |
| $\omega^\pm=\nabla_\perp^2\zeta^\pm$ | $\varpi^\pm$ (page-local) | Elsasser vorticities; **collision** with the registry $\omega$ (specific dissipation rate) |
| $\epsilon_{rec}$ | $\epsilon_{\mathrm{rec}}$ (page-local) | dimensionless reconnection rate |
| $\tau_A$, $\tau_{nl}$, $\tau_c$ | $\tau_A$, $\tau_{\mathrm{nl}}$, cascade time | agree |
| $\theta_\lambda$, $\theta_{ub}$ | $\theta_\lambda$; angle between $\boldsymbol u$ and $\boldsymbol b$ increments | alignment means Elsasser alignment in this review |
| $\delta$, $\sigma$ (§6.4) | $q$ (page-local) and $2q$: exponents of $L_\parallel$ in $\delta Z_\lambda$ and in $l_\parallel$ | **collision** with the registry $\delta$ (boundary-layer thickness); the source reuses $\alpha,\beta,\gamma,\delta,\sigma$ for other exponents in §9.6, §10, App. C, App. D |
| $\gamma$ | $\gamma_{\mathrm t}$ (page-local), tearing growth rate | **collision** with the registry $\gamma$ (ratio of specific heats) |
| $H=\mathbf A\cdot\mathbf B$, $X=\mathbf u\cdot\mathbf B$ | $H_m$, $H_c$ | magnetic and cross-helicity densities |
| $I_H$, $I_X$, $I_u$, $I_L$ | Hosking, Saffman cross-helicity, Saffman and Loitsyansky invariants | |
| $h$, $m$ | $h_O$, $m_O$ (page-local) | Olesen and Campanelli rescaling exponents (Eqs. 12.14, 12.35) |
| $\beta$ (§14) | $\beta_p$ | plasma beta |
| $\langle\cdot\rangle$ | ensemble or volume average | no LES filtering or Favre averaging appears |
| $E(k_\perp)$, $E(k_\parallel)$, $E_{2D}$ | spectra in perpendicular and parallel wavenumber | registry $E(k)$ is the three-dimensional spectrum |

# Reference list

The arXiv v3 prints 526 references in author-year style (JPP), with printed
a/b/c suffixes for same-author-year works and no DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby`
schekochihin-2022; keys take suffixes in printed order. The cited
"Schekochihin, A. A. 2022 *Lectures on Kinetic Theory and Magnetohydrodynamics
of Plasmas*" (Oxford lecture notes) is a different work from this review and
is recorded under a suffixed key, not under the slug of this source.
Pre-publication and non-journal items are their own entries: arXiv e-prints
(e.g. Galishnikova et al. 2022, Hosking & Schekochihin 2022a, b, Ewart et al.
2022), unpublished work (Beresnyak 2012b, Iskakov & Schekochihin 2008, Mallet &
Schekochihin 2011, Yousef & Schekochihin 2009, and two entries with no printed
title, Loureiro 2016 and Uzdensky & Boldyrev 2006), a private communication
(Meyrand & Squire 2020), a conference abstract (Dong et al. 2021) and web
items. Chandran (1997) is a thesis with no printed title; "Marsch, E. 2018 …
Ann. Geohys. 36, 1607" misprints the journal abbreviation and is kept as
printed.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2–3. This source is cited on:

- [Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md)
- [Critical balance and the anisotropic MHD cascade](/properties/critical-balance.md)
- [Dynamic alignment and intermittency in MHD turbulence](/properties/dynamic-alignment.md)
- [Compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
- [Decaying MHD turbulence and its invariants](/results/decaying-mhd-turbulence.md)
- [Small-scale turbulent dynamo](/results/small-scale-dynamo.md)
- [Tearing-mediated MHD turbulence](/results/tearing-mediated-mhd-turbulence.md)
- [Exact laws of (Hall-)MHD turbulence](/results/turbulence-exact-laws.md)
- [Weak wave turbulence (magneto-capillary waves)](/results/weak-wave-turbulence.md)
