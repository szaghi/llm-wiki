---
type: Source
title: "Vadrot et al. (2023b) — Survey of machine-learning wall models for large-eddy simulation"
description: "A posteriori comparison of three published machine-learning wall models (two supervised networks and a multi-agent reinforcement-learning model) against the equilibrium wall model in half-channel LES from Re_tau = 180 to 10^10, explaining their log-layer behaviour through the extrapolation properties of the activation functions and the state-action map."
resource: "doi:10.1103/physrevfluids.8.064603"
source_kind: paper
authors: [Vadrot A., Yang X.I.A., Abkar M.]
year: 2023
venue: "Phys. Rev. Fluids 8:064603"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Physical_Review_Fluids_Vadrot_Survey_of_machine-learning_wall_models_for_large-eddy_simula.pdf"
tags: [wmles, wall-model, reinforcement-learning, log-layer-mismatch]
timestamp: 2026-10-25T13:45:00Z
---

# Summary

Vadrot et al. (2023b) implement three published
[machine-learning wall models](/methods/machine-learning-wall-model.md) in the
pseudo-spectral code [LESGO](/software/lesgo.md) and compare them a posteriori
with the algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
in [wall-modelled LES](/methods/wall-modelled-les.md) of
[half-channel flow](/benchmarks/turbulent-channel-flow.md) at eleven friction
Reynolds numbers from $Re_\tau=180$ to $10^{10}$. The models, used as trained
by their authors without re-training, are HYK19 (a small sigmoid network
predicting the departure of the LES velocity from an empirical mean-flow
scaling for spanwise-rotating channels), ZHY21 and its re-trained version
ZYZY22 (deeper networks fed with velocity and pressure-gradient data at three
off-wall points, trained on channel and [periodic-hill](/benchmarks/periodic-hill.md)
data), and BK22 (a multi-agent [reinforcement-learning](/methods/reinforcement-learning-closure.md)
log-law wall model trained inside wall-modelled LES without high-fidelity
data, an instance of [model-consistent training](/methods/model-consistent-training.md)).
The SGS model is the anisotropic minimum-dissipation model, with a Lagrangian
scale-dependent [dynamic](/methods/dynamic-procedure.md) model as a check;
LESGO also offers [Smagorinsky](/methods/smagorinsky-model.md) variants.

HYK19 preserves the [law of the wall](/definitions/law-of-the-wall.md) at all
Reynolds numbers, seen and unseen; ZHY21 fails a posteriori, which an a
priori law-of-the-wall test traces to an overprediction of $\tau_w$ that
grows with $Re_\tau$; ZYZY22 recovers a logarithmic layer but
with $\kappa=0.32$, and only on the grid whose matching-point spacing equals
its training value; BK22 shows a [log-layer mismatch](/definitions/log-layer-mismatch.md)
that is positive at low and negative at high $Re_\tau$. The authors explain
these behaviours with the extrapolation theorem of Bin et al. (sigmoid
networks tend to a constant, ReLU networks grow linearly), with
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) law-of-the-wall
tests that trace ZYZY22's error to the LES side, and with a neutral-line
analysis of BK22's state–action map scored by precision, recall and accuracy.
An operation count makes all three learned models cheaper per evaluation than
the ODE-based equilibrium model. The paper also cites the
[grid-point requirements](/results/les-grid-point-requirements.md) that
motivate wall modelling, and cites the
[LaRTE model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
([Fowler et al. 2022](/sources/fowler-2022.md)) in its wall-modelling background.

# Version read

Accepted manuscript made available via CHORUS (cover page: published 7 June
2023; manuscript dated 25 May 2023, with line numbers): one cover page plus 23
manuscript pages, all read; not the typeset version of record. The metadata
above are those of the published version (Phys. Rev. Fluids 8:064603).
Manuscript page numbers equal the PDF page number minus one; section,
equation, figure, table and line numbers on this page are those of the
accepted manuscript. The label is 2023b because another 2023 paper by the same
first author is Vadrot et al. (2023a) in this bundle.

# Key claims

1. Citing Yang & Griffin, the grid-point count for a flat-plate boundary layer
   scales as $N\sim Re_{L_x}^{1.86}$ for wall-resolved LES and
   $N\sim Re_{L_x}^{1.0}$ for wall-modelled LES, $Re_{L_x}=L_xU_0/\nu$ (§I,
   l. 49–52). **Stated**
2. Log-layer mismatch causes a 15% error in $\tau_w$ (citing Spalart);
   remedies are matching away from the wall, random forcing and filtering the
   wall-model input (§I, l. 97–100). **Stated**
3. Earlier machine-learning wall models reported good a priori but poor a
   posteriori results on periodic hills (Zhou et al.), poor results in
   separation zones (Lozano-Durán & Bae), or no a posteriori validation (§I,
   l. 66–89). **Stated**
4. All learned models were used as trained by their original authors; their
   performance is affected by differences in the flow solver (§III,
   l. 207–210). **Stated**
5. The equilibrium wall model captures the log law when $h_{\mathrm{wm}}$ is in
   the log layer; at $Re_\tau=180$, with the matching point in the viscous
   layer, it yields a profile above DNS (§III A, Fig. 5; App. A, Fig. 16).
   **Shown**
6. HYK19, trained for $180<Re_\tau<1500$, gives the right mean flow at all
   Reynolds numbers from 180 to $10^{10}$ irrespective of $h_{\mathrm{wm}}$
   (§III A, Fig. 5; §IV A). **Shown**
7. ZYZY22 predicts a log law with $\kappa=0.32$ and errors at $Re_\tau=180$;
   its mismatch grows with $Re_\tau$ as
   $(1/\kappa_{\mathrm{ZYZY22}}-1/\kappa)\ln y^+$ (Eq. 9); "it is not clear to
   the authors why ZYZY22 yields a small von Kármán constant" (§III A, §IV B).
   **Shown**
8. ZYZY22 deteriorates on grids other than $32^3$, where neighbouring matching
   points are not $0.03\delta$ apart ("not shown") (§IV B, l. 282–284).
   **Stated**
9. BK22, trained at $Re_\tau=2000$, 4200 and 8000, gives a positive mismatch
   at low and a negative mismatch at high $Re_\tau$ and errors at
   $Re_\tau=180$; it does best near $Re_\tau=10^5$, where $h^+_{\mathrm{wm}}$ is
   close to the training conditions (§III A, §IV C, Table III). **Shown**
10. At fixed $y/\delta$, $u^+_{\mathrm{rms}}$ becomes Reynolds-number
    independent at high $Re_\tau$ for all wall models; ZYZY22 gives a large
    $u^+_{\mathrm{rms}}$ at $Re_\tau=180$ and BK22 a slightly larger value than
    the equilibrium model at the first off-wall point (§III A, Fig. 7).
    **Shown**
11. The number of BK22 agents (16, 64, 128) has negligible effect on the
    mismatch; above $Re_\tau=10^9$ the 16-agent run did not converge (§III B,
    Figs. 8–9). **Shown**
12. Grid resolution ($24^3$, $48^3$, $72^3$) has negligible effect on the
    equilibrium model and HYK19 and a weak effect on BK22; BK22 at
    $Re_\tau=10^{10}$ on $72^3$ did not converge, "likely because of too few
    agents (64)" (§III B, Fig. 10). **Shown**
13. HYK19's output $U^+-\kappa^{-1}\ln y^+$ follows the law of the wall up to
    $y^+=30$ and tends to a constant at large $y^+$, a consequence of the
    sigmoid activation through the extrapolation theorem (§IV A, Fig. 11).
    **Shown**
14. HYK19 improves predictions "in and only in rotating channels" and gives the
    same results as the equilibrium model elsewhere (§IV A, l. 273–275).
    **Stated**
15. In a priori tests with law-of-the-wall input, pressure terms set to zero
    and matching points at $0.03\delta$, $0.06\delta$, $0.09\delta$, ZHY21
    overpredicts $\tau_w$ increasingly with $Re_\tau$, while ZYZY22 is accurate
    except at $Re_\tau=180$ (§IV B, Fig. 12). **Shown**
16. ZHY21's failure is due also to its ReLU activation: since its input
    $\ln(h_{\mathrm{wm}}/y^*)$ grows without bound with the Reynolds number, its
    output $\tau_w/(\rho U_b^2)$ does too, whereas it should tend to zero; a
    suitably designed ReLU network can still reach the right asymptote (§IV B,
    l. 296–308). **Derived** (via the cited theorem) + **Shown** (Fig. 12)
17. Varying the first matching height with the spacing fixed at $0.03\delta$
    causes no error in ZYZY22; setting the spacing to the grid spacing does
    (§IV B, Fig. 13). **Shown**
18. BK22's mismatch comes from the gap between the neutral line, where the LES
    velocity at $h_{\mathrm{wm}}$ equals the log law (Eqs. 10–12), and the line
    separating actions $a_t>1$ from $a_t<1$ in the state map: the latter barely
    moves with $Re_\tau$ while the neutral line does; a neutral line above the
    separating line gives a positive mismatch, and vice versa (§IV C,
    Figs. 14–15; §V). **Shown**
19. The neutral line has slope $-1/(\ln(\Delta y/\delta)+\ln Re_\tau)$ in the
    plane of the states $(B_{\mathrm{wm}},1/\kappa_{\mathrm{wm}})$, which
    explains BK22's grid dependence (§IV C, Eq. 12). **Derived**
20. BK22's accuracy (fraction of desired actions) is about 0.50 at all
    $Re_\tau$, with recalls near 0.5; the mismatch correlates with precision,
    not with accuracy or recall (§IV C, Table III). **Shown**
21. Table III gives BK22 mismatches in wall units of $+2.2$ (180), $+1.1$
    ($10^3$), $+1.5$ ($2\times10^3$), $+2.0$ ($5.2\times10^3$), $+2.0$ ($10^4$),
    $+1.0$ ($10^5$), $-0.9$ ($10^6$), $-2.2$ ($10^7$), $-3.2$ ($10^8$), $-3.1$
    ($10^9$), $-3.2$ ($10^{10}$). **Shown**
22. The algebraic equilibrium model costs 5 operations per evaluation; a
    feed-forward network costs $\sum_{i=2}^{L}(n_{i-1}+2)n_i$ operations
    (Eq. 15); HYK19, ZYZY22 and BK22 cost 56, 1609 and 17412 operations (§IV D).
    **Derived**. The counts 56 and 1609 follow from the layer sizes the paper
    gives (2-4-4-2-1 and 18-15×6-2); BK22's architecture is not given *(compiler
    check, not in the sources)*.
23. The ODE-based equilibrium model adds 10–30% overhead to LES; a timing on
    one cluster gives a cost ratio of about four between it and BK22, so all
    three learned models are cheaper per evaluation; training cost (BK22: about
    $10^7$ gradient steps) is excluded (§IV D). **Shown** (rough timing) /
    **Stated** (overhead)
24. Domain size has minimal effect on the equilibrium model and HYK19 at
    $Re_\tau=5200$ (App. B, Fig. 17). **Shown**
25. Replacing the anisotropic minimum-dissipation SGS model by the Lagrangian
    scale-dependent dynamic model changes little at $Re_\tau=5200$, "indicating
    that the learned models are not significantly adjusted to compensate for
    deficiencies in the SGS model" (App. B, Fig. 18). **Shown**
26. At $Re_\tau=1000$ and 180 the equilibrium model follows the log law and
    gives a positive mismatch; HYK19 reproduces DNS reasonably through its
    varying intercept, but a negative mismatch remains (App. A, Fig. 16).
    **Shown**
27. A learned model must preserve known empiricism (the law of the wall) and
    must not degrade the baseline; the authors advocate "progressive learning"
    and channel flow as a sanity check (§V). **Stated**

# Printed slips

- **Abstract against Table III.** The abstract says BK22 "has errors at both
  low ($Re_\tau<10^3$) and high Reynolds numbers ($Re_\tau>10^6$)", but
  Table III gives $+1.5$, $+2.0$, $+2.0$ at $Re_\tau=2\times10^3$,
  $5.2\times10^3$, $10^4$, larger than $+1.1$ at $10^3$, and §IV C (l. 364)
  itself reports "positive mismatches at $Re_\tau$ between 2000 and $10^4$".
- **§IV C, l. 365 against Table III.** "The precisions for both the $a_n>1$
  and the $a_n<1$ actions are low at $Re_\tau=180$ and $10^3$ and the effects
  cancel, leading to a small LLM", while Table III gives $+2.2$ at
  $Re_\tau=180$, the largest positive mismatch of the table, and l. 349 reports
  "a positive log layer mismatch at $Re_\tau=180$ and 1000".
- **Rotation length scale.** l. 139: "$l^+_\Omega=u_\tau/(2\Omega)$ is the
  non-dimensional rotation length scale"; l. 143: "$l_\Omega=u_\tau/(2\Omega)$
  is the rotation induced length scale". The same expression is given for the
  inner-scaled and the dimensional quantity; $u_\tau/(2\Omega)$ is a length, so
  the inner-scaled value is $l_\Omega u_\tau/\nu$ *(compiler check, not in the
  sources)*.
- Eq. (12) writes $1/\kappa_m$ where Eqs. (8a) and (11) write
  $1/\kappa_{wm}$.
- Eq. (12): "the slope of the neutral line decreases as the Reynolds number
  increases and increases as the grid resolution increases". The printed slope
  $-1/(\ln(dz/\delta)+\ln Re_\tau)$ is negative and tends to zero as
  $Re_\tau$ grows, so the statement holds for its magnitude *(compiler check,
  not in the sources)*.
- Fig. 12 caption: "Here, $\tau_{mw_{wm}}$ is the wall-shear stress", for
  $\tau_{w_{wm}}$. Fig. 3 and Fig. 10 captions write "$Re=10^5$" and
  "$Re=10^{10}$" for $Re_\tau$.
- ZHY21 output normalization: Table I gives $\tau_{xz_{wm}}/u_b^2$, the text
  (l. 300) $\tau_w/(\rho U_b^2)$.
- Table I lists the features $\frac{\delta}{h_{wm}}\frac{v}{u_b}$ and
  $\frac{h_{wm}}{\rho u_b^2}\frac{\partial p}{\partial z}$ and the output
  $\tau_{yz_{wm}}$, while the paper's wall-normal direction is $z$; the paper
  does not say which coordinate convention Table I follows.
- Typos: "LES is a scale-resolve tool" (l. 42); "Smagorinksy" (l. 9); "form
  $Re_\tau=180$" (l. 403); "improvements offer by" (l. 416).

# Notation map

| Vadrot et al. (2023b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $x$, $z$, $y$ | **source $z$ is wall-normal and $y$ spanwise** (LESGO convention); translated |
| $z^+$, $dz$ | $y^+$, $\Delta y$ | wall-normal coordinate in wall units; wall-normal grid spacing, $L_z/(N_z-1)$ in the source |
| $\bar u^+$ | $u^+=\langle u\rangle/u_\tau$ | source overbar is the mean, **not** the LES filter |
| $\tilde U_{LES}$ | filtered wall-model input | tilde is a sharp filter of width twice the grid spacing, **not** a Favre filter |
| $U_{LES}$, $h_{wm}$ | $U_{\mathrm{LES}}$, $h_{\mathrm{wm}}$ | agree; $h_{\mathrm{wm}}=\Delta y/2$ for the equilibrium model, HYK19 and ZHY21/ZYZY22, $\Delta y$ for BK22 |
| $\delta$ | $\delta$ | half-channel height; agrees |
| $u_\tau$, $\tau_w$, $Re_\tau$ | $u_\tau$, $\tau_w$, $Re_\tau$ | agree; $Re_\tau$ not defined explicitly |
| $\kappa$, $B$ | $\kappa$, $B$ | $\kappa\approx0.4$, $B\approx5$ in the source |
| $z_0=\nu\exp(-\kappa B)/u_\tau$ | roughness-length form of the log law | called "viscous scale" in the source |
| $\Omega$, $l_\Omega$ | $\Omega_{\mathrm{rot}}$, rotation length $u_\tau/(2\Omega_{\mathrm{rot}})$ | system rotation rate |
| $s_n$, $a_n$, $r_n$ | $s_t$, $a_t$, $r_t$ | RL state, action (multiplicative factor on $\tau_w$, in $[0.9,1.1]$), reward |
| $\kappa_{wm}$, $B_{wm}$ ($\kappa_m$ in Eq. 12) | $\kappa_{\mathrm{wm}}$, $B_{\mathrm{wm}}$ | BK22 states, Eq. (8) |
| $u_b$, $U_b$ | bulk velocity | both spellings in the source |
| $Re_h$ | $Re_h$ | hill-height Reynolds number; agrees |
| LLM | log-layer mismatch in wall units | against $\kappa^{-1}\ln y^++B$, $\kappa=0.4$, $B=5$ |
| $N$, $L$, $n_i$ | operation count, number of layers, neurons per layer | Eq. (15); $N$ is not the polynomial degree |

# Reference list

The accepted manuscript prints 116 numbered references ([1]–[116]) in
Physical Review style (first page or article number only). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby`
vadrot-2023-b; same-key works take suffixes in printed order. Four cited works
are ingested sources or planned ones: [Duraisamy et al. (2019)](/sources/duraisamy-2019.md)
(ref. [16]), [Goc et al. (2021)](/sources/goc-2021.md) (ref. [45]), [Fowler et
al. (2022)](/sources/fowler-2022.md) (ref. [76]) and Bae & Koumoutsakos (2022) (ref. [83], printed "Nat.
Commun. 13, 1 (2022)"). Two printed works share a bundle slug without being
that source: ref. [9] (Cai et al. 2022, physics-informed networks review, Acta
Mech. Sin.) and ref. [41] (Li, Yang & Kunz 2022, Phys. Fluids) are recorded
under distinct keys. Pre-publication items are their own entries (ref. [82],
Zhou et al. 2022, arXiv; ref. [85], Lozano-Durán & Bae 2020, arXiv). Ref. [92]
is the LESGO web page, undated, keyed with the citing year and a corporate
author. Several items print no volume or pages ([9], [18], [41]–[43]); ref.
[19] (Prandtl) mixes the German title, the congress and the NACA translation;
ref. [78] ends its author list with "et al.".

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunk 2 (2026-10-25). This source is cited on:

- [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Lagrangian relaxation towards equilibrium (LaRTE) wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Reinforcement-learning turbulence closures](/methods/reinforcement-learning-closure.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [LESGO](/software/lesgo.md)
