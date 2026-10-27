---
type: Source
title: "Vadrot et al. (2023a) — Log-law recovery through reinforcement-learning wall model for large-eddy simulation"
description: "Introduces VYBA23, a multi-agent reinforcement-learning wall model whose first state is renormalized so that the neutral line of the state-action map no longer depends on the Reynolds number; trained once at Re_tau = 10^4 without high-fidelity data, it recovers the log law in half-channel LES up to Re_tau = 10^10."
resource: "doi:10.1063/5.0147570"
source_kind: paper
authors: [Vadrot A., Yang X.I.A., Bae H.J., Abkar M.]
year: 2023
venue: "Phys. Fluids 35:055122"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Physics_of_Fluids_Vadrot_Log-law_recovery_through_reinforcement-learning_wall_model_f.pdf"
tags: [wmles, wall-model, reinforcement-learning, log-layer-mismatch, data-driven]
timestamp: 2026-10-27T15:54:00Z
---

# Summary

Vadrot et al. (2023a) correct the log-law reinforcement-learning wall model
of Bae & Koumoutsakos (2022), called BK22, and propose a new
[reinforcement-learning closure](/methods/reinforcement-learning-closure.md)
for [wall-modelled LES](/methods/wall-modelled-les.md), called VYBA23. In
both models, agents placed at the matching height act multiplicatively on
the wall-shear stress, $\tau_w^{n+1}=a_t\tau_w^n$, and are rewarded for
approaching the mean wall stress $-\delta\,dp_0/dx$ fixed by the driving
pressure gradient, so no filtered-DNS data enter training. The authors
attribute BK22's large-$Re_\tau$
[log-layer mismatch](/definitions/log-layer-mismatch.md) to the rotation,
with $Re_\tau$, of the "neutral line" $u^+_{\mathrm{LES}}=u^+_{\mathrm{LL}}$
in the plane of BK22's two states, the local inverse log-law slope
$1/\kappa_{\mathrm{wm}}$ and intercept $B_{\mathrm{wm}}$. VYBA23 replaces the
first state with $(1/\kappa_{\mathrm{wm}}-1/\kappa)\ln h^+_{\mathrm{wm}}$, which
makes the neutral line the same for every Reynolds number.

Trained once at $Re_\tau=10^4$ (V-Racer through the Smarties library coupled
to [LESGO](/software/lesgo.md)), VYBA23 is tested a posteriori in the
half-channel ([turbulent channel flow](/benchmarks/turbulent-channel-flow.md))
on a $48^3$ grid at eleven Reynolds numbers from 180 to $10^{10}$, against a
retrained BK22 and the [equilibrium wall model](/methods/equilibrium-wall-model.md).
It recovers the [law of the wall](/definitions/law-of-the-wall.md) up to
$Re_\tau=10^{10}$ whenever the matching height lies in the log layer, while
BK22 keeps its high-$Re_\tau$ mismatch. A parameter study shows that the
action range and the action interval barely change the mean velocity but
change the wall-stress fluctuations, and that they act through their ratio
(a derived similarity rule). The authors display the learned policy in
the state-action map and score it by the precision, recall and accuracy of the sign
of $a_t-1$ relative to the neutral line. The paper sits in the
[machine-learning wall model](/methods/machine-learning-wall-model.md)
lineage and argues that reward-based training removes the
[a priori / a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
input inconsistency of supervised wall models. Its companion survey is
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md).

# Version read

arXiv preprint arXiv:2302.14391v3 [physics.flu-dyn], 2 May 2023 (header
"Dated: 3 May 2023"), author-formatted, 16 pages, all read. The metadata
above are those of the published article (Phys. Fluids 35:055122); the DOI is
not printed on the preprint. Page 1 title and authors match the published
record; the title is hyphenated "large-eddy" on page 1. Equation, figure,
table and reference numbers on this page are those of arXiv v3. In the
bundle this paper is Vadrot et al. (2023a);
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) is the survey.

# Key claims

Coordinates translated to the registry: the source's wall-normal $z$ is $y$
here, its spanwise $y$ is $z$ (see Notation map).

1. VYBA23 is trained at the single Reynolds number $Re_\tau=10^4$ and "does not rely on high-fidelity data, as the back-propagation process is based on a reward rather than output error" (Abstract; §II.B.3; §V). **Stated**
2. BK22, retrained by the authors in LESGO at $Re_\tau=10^4$, shows the same large-$Re_\tau$ log-layer mismatch as the original BK22 tested in LESGO; at low $Re_\tau$ the retrained model suppresses the mismatch (§II.B.2, Fig. 2). **Shown**
3. The authors attribute the differences between original and retrained BK22 to the training Reynolds number, the RL settings and possibly the solver (BK22 was trained with a second-order finite-difference code and is here run in a pseudo-spectral code) (§II.B.2). **Stated**
4. BK22's large-$Re_\tau$ mismatch is caused by the counterclockwise rotation, with increasing $Re_\tau$, of the neutral line $u^+_{\mathrm{LES}}-u^+_{\mathrm{LL}}=0$ in the $(B_{\mathrm{wm}},1/\kappa_{\mathrm{wm}})$ plane; the rotation saturates at large $Re_\tau$, as does the mismatch. The slope of the line is $-1/(\ln(\Delta y/\delta)+\ln Re_\tau)$ (§II.B.3, Eq. 9, Fig. 3a). **Derived** / **Shown**
5. With the first state $s_1=(1/\kappa_{\mathrm{wm}}-1/\kappa)\ln h^+_{\mathrm{wm}}$ (Eq. 10) and $s_2=B_{\mathrm{wm}}$, the neutral line becomes $s_1+s_2-B=0$ for every $Re_\tau$ (§II.B.3, Fig. 3b). **Derived** / **Shown**
6. VYBA23 captures the log law when $h_{\mathrm{wm}}$ lies in the log layer and predicts accurately outside its training Reynolds number, up to $Re_\tau=10^{10}$; at $Re_\tau=180$ its mean velocity lies above the DNS profile (§III.A, Fig. 6). **Shown**
7. VYBA23 outperforms BK22 in log-law recovery (Figs. 2, 6, 9). **Shown**
8. Instantaneous streamwise fluctuation fields near the wall (first point) and at $y/\delta=0.5$ are alike for the equilibrium model, BK22 and VYBA23 at $Re_\tau=10^5$, in intensity and scale (§III.A, Figs. 4–5). **Shown**
9. WMLES on the $48^3$ grid resolves neither the inner peak ($y^+\approx15$) nor the outer peak ($y^+\approx3\sqrt{Re_\tau}$) of the streamwise velocity variance; no wall model captures the outer-peak bump near $y/\delta\approx0.1$ (§III.A, Fig. 7). **Shown** / **Stated**
10. From the outer peak to the centre the streamwise variance in inner units scales as $\ln(\delta/y)$ (Eq. 11), independently of the Reynolds number, which is why the WMLES streamwise rms collapses at large $Re_\tau$ (§III.A, citing Marusic et al. 2013 and Hultmark et al. 2012). **Stated**
11. Each LES was checked for statistical convergence through the kinetic energy and the stress balance; at $Re_\tau=10^8$ the total (resolved plus modelled) stress almost overlaps the ideal linear total stress (§III.A, Fig. 8). **Shown**
12. A 2.5% uncertainty in $\kappa$ produces a 5% error in the predicted wall stress, i.e. about 1–2 plus units of log-layer mismatch (§III.B, citing Yang et al. 2019). **Stated**
13. The agent parameters (action range $\Delta a$, action interval $\Delta t_{\mathrm{RL}}$, agent spacing) have limited effect on the mean velocity, "the only exception being when the time-step between actions becomes too large" ($\Delta t_{\mathrm{RL}}>10\Delta t_{\mathrm{LES}}$) (§III.B, Fig. 9). **Shown**
14. The wall-stress fluctuations increase with the action range and decrease with the action interval; the agent spacing has minimal effect (§III.B, Fig. 10). **Shown**
15. The wall-stress fluctuations decrease with increasing $Re_\tau$ for all models, explained through Eq. 12 by their dependence on $1/(\ln h^+_{\mathrm{wm}}+B)$ (§III.B). **Derived** (heuristic; see Printed slips)
16. The setting that best matches the filtered-DNS wall-stress fluctuations is $(\Delta a;\Delta t_{\mathrm{RL}};\Delta x_a;\Delta z_a)=(0.10;5\Delta t_{\mathrm{LES}};3\Delta x;3\Delta z)$, possibly solver dependent (§III.B, Fig. 10). **Shown**
17. The agents learnt to increase $\tau_w$ when $u^+_{\mathrm{LES}}>u^+_{\mathrm{LL}}$ and decrease it otherwise; the policy remains consistent outside the training Reynolds number except when $h^+_{\mathrm{wm}}$ lies in the buffer or viscous layer, where VYBA23 overpredicts the velocity (§IV, Fig. 11). **Shown**
18. Accuracy of the sign of the action relative to the neutral line (Table III): VYBA23 0.92, 0.91, 0.83, 0.64 at $Re_\tau=180$, $10^3$, $10^5$, $10^{10}$; BK22 0.49, 0.50, 0.53, 0.49 (§IV, Eqs. 13–14). **Shown**
19. Similarity rule: two models with $(\Delta a,\Delta t_{\mathrm{RL}})=(a_1,b_1\Delta t_{\mathrm{LES}})$ and $(a_2,b_2\Delta t_{\mathrm{LES}})$ act alike if $\ln(1+a_1)/b_1=\ln(1+a_2)/b_2$, i.e. $a_1/b_1=a_2/b_2$ for $a\ll1$ (§IV, Eqs. 15–17, assuming repeated maximal actions of one sign). **Derived**; the wall-stress-fluctuation curves of (0.05; 10) against (0.10; 20) and (0.01; 1) against (0.10; 10) overlap (Fig. 12). **Shown**
20. Increasing the action range is computationally cheaper than increasing the action interval to obtain the same effect (§IV). **Stated**
21. Recommendation: reduce the action range, or set $\Delta t_{\mathrm{RL}}=5\Delta t_{\mathrm{LES}}$, which gives wall-stress fluctuations closer to filtered DNS, less log-layer mismatch and less effect on the Reynolds-number independence of the velocity fluctuations (§IV, Figs. 9, 10, 13–15). **Shown**; the relation is "not yet well understood" and solver dependent. **Stated**
22. RL wall models are interpretable: the two-dimensional state-action map displays the learned policy, which answers the "black-box" criticism (§II.B.3, §IV, §V). **Stated**
23. Training was "challenging and time-consuming": coupling the C++ Smarties library with the Fortran LESGO, "hundreds of simulations and millions of policy gradient updates", non-converging models, several reward functions tried before VYBA23 (§II.B.3). **Stated**
24. Recovering the log law is an essential step: "if a model cannot capture the log law, it would be hard for it to capture other flow phenomena" (§V). **Stated**
25. RL "surpass[es] supervised ML" because it works with a reward rather than an output error, removing the need for filtered-DNS data and the input inconsistency between a priori training and a posteriori use (§V). **Stated**

The paper does not state which subgrid-scale model its LES use; LESGO offers
the constant and dynamic Smagorinsky models, the Lagrangian dynamic model
and the anisotropic minimum-dissipation model (§II.A).

# Printed slips

- **Eq. 12 against Eq. 2 (p. 10)** *(compiler check, not in the sources)*. Eq. 2 prints $\tau_w=\rho[\kappa\tilde U_{LES}/\ln(h_{wm}/z_0)]^2$ with $z_0=\nu\exp(-\kappa B)/u_\tau$ (§II.B.1), so $\ln(h_{wm}/z_0)=\ln h^+_{\mathrm{wm}}+\kappa B$. Eq. 12, presented as a rewriting of Eq. 2, prints $\tau_w=\rho u_\tau^2=\rho\left[\kappa\tilde U_{LES}/(\ln(h^+_{wm})+B)\right]$: $B$ in place of $\kappa B$, and no square.
- **Text after Eq. 12 (p. 10):** "$1/(\ln(h^+_{wm}+B)$", with an unbalanced parenthesis, against $\ln(h^+_{wm})+B$ in Eq. 12.
- **Eq. 6 (p. 4):** the condition uses $\tau_w(x,z,t_n)$, whereas the rest of Eq. 6 and Eqs. 3–4 use $(x,y,t_n)$, the wall-parallel agent coordinates.
- **Eq. 4 sign (p. 4)** *(compiler check, not in the sources)*. The reward is printed as $r_n=\left(|\tau_w^{true}-\tau_w(t_n)|-|\tau_w^{true}-\tau_w(t_{n-1})|\right)/\tau_w^{true}+\text{Bonus}$; as printed, the first term is positive when the error grows, whereas the stated aim is convergence to $\tau_w^{true}$.
- **§II.B.3:** "horizontal ($\Delta x$) and vertical ($\Delta y$) distances between agents"; in the source $y$ is spanwise and the agents lie in the horizontal plane, so "vertical" names the spanwise spacing.
- **Fig. 4 caption:** "The flow is at $Re=10^5$" (subscript $\tau$ missing).
- **Ref. 50 (Lee & Moser 2015):** printed title truncated, "Direct numerical simulation of turbulent channel flow up to,".

# Notation map

| Vadrot et al. (2023a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $x$, $z$, $y$ | **source $z$ is wall-normal and $y$ spanwise** (LESGO convention); translated |
| $z^+$ | $y^+$ | |
| $dx$, $dy$, $dz$ | $\Delta x$, $\Delta z$, $\Delta y$ | grid spacings; $dz=L_z/(N_z-1)$ on a staggered grid, first velocity plane at $dz/2$ |
| $dt$ | $\Delta t_{\mathrm{LES}}$ (page-local) | LES time step |
| $\delta$ | $\delta$ | half-channel height; agrees |
| $u^+$, $u_\tau$, $\tau_w$, $Re_\tau$ | $u^+$, $u_\tau$, $\tau_w$, $Re_\tau$ | agree; $Re_\tau$ not defined explicitly |
| $\kappa$, $B$ | $\kappa$, $B$ | $\kappa\approx0.4$, $B\approx5$ |
| $z_0=\nu\exp(-\kappa B)/u_\tau$ | $y_0$ (page-local on the [equilibrium wall model](/methods/equilibrium-wall-model.md) page) | roughness-length form of the log law; called "viscous scale" in the source |
| $h_{wm}$, $h^+_{wm}$ | $h_{\mathrm{wm}}$, $h^+_{\mathrm{wm}}$ | $\Delta y/2$ for the equilibrium model, $\Delta y$ for the RL models |
| $U_{LES}$, $u_{LES}$ | $U_{\mathrm{LES}}$ | LES velocity at $h_{\mathrm{wm}}$ |
| $\tilde U_{LES}$ | filtered wall-model input | **tilde is a "possible filtration operation"** of the wall-model input, not a Favre filter |
| $\tau_w^{true}=-\delta\,dp_0/dx$ | mean wall stress | from the driving pressure gradient |
| $u_{\tau_{wm}}=\sqrt{\tau_w/\rho}$ | (model friction velocity) | |
| $\kappa_{wm}$, $B_{wm}$ | $\kappa_{\mathrm{wm}}$, $B_{\mathrm{wm}}$ | local log-law slope and intercept at $h_{\mathrm{wm}}$ (Eqs. 7a–b), as on [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) |
| $u^+_{LL}$ | $u^+_{\mathrm{LL}}$ (page-local) | log-law velocity at $h_{\mathrm{wm}}$ with $\kappa=0.4$, $B=5$ |
| $s_1$, $s_2$ | components of the state $s_t$ | BK22: $s_1=1/\kappa_{\mathrm{wm}}$; VYBA23: Eq. 10; $s_2=B_{\mathrm{wm}}$ |
| $a_n$, $r_n$, $\pi$ | $a_t$, $r_t$, $\pi_{\boldsymbol\theta}$ | action (multiplier of $\tau_w$, in $[1-\Delta a,1+\Delta a]$), reward, policy |
| $\Delta t$ | $\Delta t_{\mathrm{RL}}$ | action interval, in multiples of the LES time step |
| $\Delta a$ | $\Delta a$ (page-local) | action range |
| $\Delta x$, $\Delta y$ (agents) | $\Delta x_a$, $\Delta z_a$ (page-local) | **collision:** agent spacings, not grid spacings or the filter width |
| $N_{agents}$ | (number of agents) | 256 at $3\Delta x\times3\Delta z$ |
| $u^{+2}_{rms}$, $\tau^+_{w,rms}$ | (rms of streamwise velocity and wall stress, inner units) | |

# Reference list

84 printed references, numbered (AIP superscript style). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby`
vadrot-2023. Six cited works are ingested sources:
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md) (Ref. 16),
[Duraisamy (2021)](/sources/duraisamy-2021.md) (Ref. 33),
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Ref. 22, printed pages
"1–9"), [Kurz et al. (2023)](/sources/kurz-2023.md) (Ref. 25),
[Kim et al. (2022)](/sources/kim-2022.md) (Ref. 30) and
[Fowler et al. (2022)](/sources/fowler-2022.md) (Ref. 43). Ref. 34 is the
arXiv preprint (arXiv:2211.03614, 2022) of
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) and is kept as its own
preprint entry. Refs. 42 (Hansen et al., arXiv 2023) and 77 (Hansen et al.,
CTR summer program 2022) share a title with different authors and venues and
are two entries. Ref. 50 prints a truncated title; Ref. 54 prints only
"Arxiv" with no identifier; Ref. 61 is the undated LESGO web page; several
items lack volume or pages. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 5 (2026-10-26). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Lagrangian relaxation towards equilibrium (LaRTE) wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Reinforcement-learning turbulence closures](/methods/reinforcement-learning-closure.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [LESGO](/software/lesgo.md)
