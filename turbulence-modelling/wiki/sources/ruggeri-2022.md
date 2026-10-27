---
type: Source
title: "Ruggeri et al. (2022) — Neural-network-based Riemann solver for real fluids and high explosives; application to computational fluid dynamics"
description: "Multilayer perceptrons trained on exact Riemann-solver data predict the star state of the 1-D Euler Riemann problem for a calorically imperfect gas, supercritical CO2 (Peng–Robinson) and PBX-9502 (Davis), and serve as interface fluxes of a Godunov finite-volume code; turbulence appears only in the literature review."
resource: "doi:10.1063/5.0123466"
source_kind: paper
authors: [Ruggeri M., Roy I., Mueterthies M.J., Gruenwald T., Scalo C.]
year: 2022
venue: "Phys. Fluids 34:116121"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/0000_manual_no_journal_Unknown_10106350123466titleNeural-network-based.pdf"
tags: [neural-network, shock-capturing, real-gas, compressible, a-priori-a-posteriori]
timestamp: 2026-10-27T10:55:00Z
---

# Summary

Ruggeri et al. (2022) train fully connected feed-forward networks
(multilayer perceptrons) to solve the one-dimensional Riemann problem of the
Euler equations for three non-ideal fluids: air with a calorically imperfect
ideal-gas closure (CI), supercritical CO$_2$ with the Peng–Robinson equation
of state (SF), and the unreacted high explosive PBX-9502 with the Davis
equation of state (HE); a constant-$\gamma$ ideal gas is treated in Appendix
B. Training and test data come from an exact iterative Riemann solver for
general convex equations of state (Colella–Glaz and Kamm: secant iteration
on the star pressure, Rankine–Hugoniot shocks, Runge–Kutta integration of
the isentropes), with 100 000 training and 20 000 test samples per fluid,
balanced over the four wave configurations. Two networks are compared: NN+EE
predicts only the star pressure (the star velocity for the ideal gas) and
recovers the rest from the exact wave relations; NN predicts all four
middle-state values.

Per sample, the standalone network NN costs about 16–28 μs and NN+EE
between 42.7 μs and 1.27 s depending on the configuration, against 76.6 ms (CI), 1.6 s (SF) and 21.4 s
(HE) for the exact solver (overall rows of Tables III–V); the overall mean
absolute percentage error is at most 0.191% for NN+EE and 1.120% for NN. Used as interface
fluxes of a first-order Godunov finite-volume code on shock tubes, the
networks reproduce the exact-solver solution at a per-iteration cost two to
three orders of magnitude lower, somewhat above the Rusanov flux; on the
supercritical fluid the network flux gives a solution closer to the exact
Riemann solution than the exact solver used as flux. At fourth order, with
[flux reconstruction](/methods/flux-reconstruction.md) and the Haga–Kawai
localized [artificial diffusivity](/methods/artificial-viscosity-shock-capturing.md),
the differences between fluxes shrink. Appendix C trains an unsupervised
[physics-informed network](/methods/physics-informed-neural-network.md) for
the ideal gas with the loss $|p_{II}-p_{III}|$. The networks are evaluated twice, on test samples and then inside the
solver; the paper uses the words "a priori and a posteriori tests" only for
the cited physics-informed subgrid model of Bode et al. (§III). Turbulence enters only through
the literature review, which cites
[field inversion](/methods/field-inversion-machine-learning.md),
[gene-expression programming](/methods/symbolic-regression-closure.md) and
[super-resolution subfilter models](/methods/super-resolution-sgs-model.md).
The paper is inviscid compressible numerics with a minimal footprint in
this bundle.

# Version read

Version of record (Phys. Fluids 34:116121, submitted 30 August 2022,
accepted 15 October 2022, published online 8 November 2022): 18 PDF pages,
an AIP cover page plus article pages 116121-1 to 116121-17, all read; the
equation pages were also read visually because the text layer garbles the
equations. Page-1 title, authors, venue and DOI match the metadata above.
No identity problem. Numbering on this page is that of this version.

# Key claims

States are numbered as in the source: I (left initial), II and III (left
and right of the contact), IV (right initial); $p^*=p_{II}=p_{III}$ and
$u^*=u_{II}=u_{III}$ (page-local). $\varepsilon_X$ is the mean absolute
percentage error (MAPE) of $X$. The wave configurations are RCS, SCR, SCS
and RCR (R rarefaction, C contact, S shock, left to right).

1. For real fluids the networks are "more than five orders of magnitude faster than the exact solver, with prediction errors below 0.8%" (Abstract). **Shown** (Tables III–V; see Printed slips)
2. Embedded in a CFD code, the networks give "very good agreement with the overall exact solution, with a speed-up of three orders of magnitude" relative to the exact Riemann solver; against the Rusanov flux "the neural network is half as fast but yields a higher accuracy and is able to converge to the exact solution with a coarser grid" (Abstract, §VI, Tables VI–VII, Fig. 8). **Shown** (see Printed slips)
3. Only two earlier papers (Gyrya et al., Magiera et al.) applied machine learning to the Riemann problem, only one of them coupled to a CFD method, and only Wang treated non-ideal equations of state (a PINN for supercritical fluids) (§I). **Stated**
4. The exact Riemann solver for real fluids costs several orders of magnitude more than the ideal-gas one; its most expensive part is the Runge–Kutta integration of the rarefaction ODEs (Eqs. 9–10), because the best density step is not known a priori (§II A). **Stated** (timings in Tables III–V and IX **Shown**)
5. Adam is always the best optimizer, SGD about ten times worse in accuracy; ReLU is always the best activation; the best loss function depends on the equation of state and the case (§IV–V). **Shown** (no table)
6. For CI the 1028-512-256-128-64 architecture is best and the second thermodynamic input is best taken as the sound speed (density worst); HE and SF do best with density and worst with temperature, except the standalone HE network, where the sound speed is mildly better (§V). **Shown** (no table)
7. Predicting only $p^*$ and computing the rest from the Euler relations (NN+EE) is the most accurate route; for CI the overall $\varepsilon_{u^*}$ is 0.051% against 1.120% for NN (Table III, §V). **Shown**
8. The two-rarefaction configuration is the hardest for CI: NN+EE $\varepsilon_{p^*}=0.457\%$ against 0.087–0.125% for the other three, which the authors attribute to the non-analytic integral across a non-ideal expansion (§V, Table III). **Shown**
9. For the Davis equation of state, non-normalized data give about 30% error against about 1% with normalized data, because the variable ranges are wider (§V). **Shown** (numbers stated)
10. For HE, NN+EE can be "up to ten times more accurate" than NN, except for $p^*$, the predicted variable (Table IV, §V). **Shown**
11. For HE the exact solver takes 12.56–38.56 s on the configurations with a rarefaction and 59.41 ms on the two-shock one; the authors conclude that mixed cases need more iterations (§V, Table IV). **Shown**
12. For SF, NN+EE is the most accurate (overall $\varepsilon_{p^*}=0.061\%$, $\varepsilon_{u^*}=0.046\%$) and NN the fastest (16.4 μs overall) (Table V). **Shown**
13. A standalone network used as interface solver causes oscillations in constant regions, because it predicts slightly different values from two identical input states; NN+EE reduces them; NN is therefore used only when the initial jumps of $p$ and $u$ exceed thresholds (the jump times the network accuracy), otherwise the linearized solver (Eq. A5) is used (§VI). **Shown** (qualitatively)
14. "Assuming that the exact solution to the Riemann problem is used as a numerical flux, this does not guarantee that the CFD solver will yield the exact solution when used to solve the Riemann problem itself (discretized over multiple cells)" (§VI). **Stated**
15. HE shock tube at $t=0.047$ ms: Rusanov gives smoother waves and a larger middle-state error; the exact solver and both networks are nearly identical, except a drop of the left pressure with NN+EE; the deactivated NN is more accurate in flat regions (§VI, Fig. 5). **Shown**
16. Per-iteration CFD cost for HE: Rusanov 0.177 s, exact solver 134 s, NN+EE 0.615 s, NN 0.215 s (Table VI); for SF: 0.293 s, 204 s, 0.6 s, 0.407 s (Table VII); the text calls both networks "three orders of magnitude faster than the exact Riemann solver" (§VI). **Shown**
17. For SF at $t=0.966$ ms all methods overpredict the middle-state pressure, Rusanov the most; the network flux gives a more accurate solution than the exact-solver flux: "the small error made by the neural network … unexpectedly works in the direction of improving the CFD prediction" (§VI, Fig. 6). **Shown** (one case, first order)
18. At fourth order (flux reconstruction with Haga–Kawai shock capturing) the differences shrink, the largest being at the density contact, where Rusanov oscillates more; the network advantage decreases "because with high order, the interfaces of the mesh have a less important role than for order 1" (§VI, Fig. 7, Conclusions). **Shown** (reason **Stated**)
19. Grid convergence (PBX-9502, 100, 500 and 1000 cells, $t=0.108$ ms): NN converges faster than Rusanov and needs fewer grid points, which "can balance the computational time lost" (§VI A, Fig. 8). **Shown**
20. Coupling the network with the Euler relations gives more stable CFD results than a standalone network; safe deployment needs a PINN or the avoidance of extreme cases such as constant initial conditions (Conclusions). **Stated**
21. Outside the training range the network predictions can "blow up the simulation", so the range of values must be known a priori (Conclusions). **Stated**
22. "To our knowledge, there is no approximate Riemann solver for non-ideal EoS that we can use to compare the neural network results" (Conclusions); the reference list includes Wang and Hickey, "A class of structurally complete approximate Riemann solvers for trans- and supercritical flows" (Ref. 18). **Stated**
23. For the ideal equation of state the networks save no time: per sample, exact solver 0.512 μs, Toro's adaptive solver 0.149 μs, NN+EE 61.5 μs, NN 14.9 μs overall (Table IX); a C++/Eigen implementation of the network prediction completes in 0.55 ms (App. B 1). **Shown**
24. Ideal-gas accuracy: NN+EE overall $\varepsilon_{u^*}=0.435\%$, $\varepsilon_{p^*}=0.134\%$; NN 4.026% and 1.415%; the adaptive solver 5.480% and 19.727% (0% on the two-rarefaction case); the mirror-symmetric configurations differ strongly in accuracy, which the authors attribute to training flows with mostly positive velocity (App. B, Table VIII). **Shown**
25. The Gottlieb–Groth exact ideal-gas solver needs 3–5 Newton iterations on average for the two-shock case and is there more than four times slower than the adaptive solver (App. B, Table IX); it is "the second fastest solver (47% slower than the fastest)", Pike's being the fastest (App. A 1, as cited). **Shown** / **Stated**
26. Ideal-gas shock tube: Rusanov is smoothest; HLLC, the exact solver and NN+EE resolve the rarefaction better; NN shows a small oscillation at the rarefaction tail; per-iteration costs are Rusanov 0.170 s, HLL 0.170 s, HLLC 0.155 s, exact 0.160 s, NN+EE 0.220 s, NN 0.200 s, Rusanov and HLL being slower than HLLC because they compute two absolute values (App. B 2, Fig. 9, Table X). **Shown**
27. An unsupervised PINN (no labels; loss $|p_{II}-p_{III}|$ from a predicted $u^*$, or $10^{20}$ when infeasible) reaches overall $\varepsilon_{u^*}=0.670\%$, $\varepsilon_{p^*}=0.371\%$, $\varepsilon_{\rho_{II}}=0.475\%$, $\varepsilon_{\rho_{III}}=0.458\%$ on the ideal gas, better than the supervised NN and worse than NN+EE (App. C, Table XI). **Shown**
28. Magiera et al. used a 7-layer, 70-neuron network with constraint-resolving layers or a constraint-adapted loss, the former best; the networks did not speed up their front-capturing scheme but cut a particle simulation "from 13 h to 2 s" (§III A, as cited). **Stated**

# Printed slips

- **Eq. (D1):** the Godunov update is printed
  $\mathbf Q_i^{n+1}=\mathbf Q_i^n+\frac{1}{\Delta x}\int_{t^n}^{t^{n+1}}(\mathbf F_{i+\frac12}-\mathbf F_{i-\frac12})\,dt$;
  *(compiler check, not in the sources)* integrating the paper's own Eq.
  (1), $\mathbf Q_t+\mathbf F_x=0$, over cell $i$ puts a minus sign before
  the flux integral.
- **HLL wave speeds (App. D 1):** printed "$S_I=|u_I|+a_I$ and
  $S_{IV}=|u_{IV}|+a_{IV}$". *(compiler check, not in the sources)* Both are
  non-negative, so the branch $S_I<0<S_{IV}$ of Eq. (D2) is never reached
  and the condition $0\le S_I$ always selects $\mathbf F_I$.
- **Eq. (A1):** $R_{1IV}=a_{IV}+\delta u_{IV}$ is called "the left
  invariant of state IV" and printed with the same sign as the right
  invariant $R_{2I}=a_I+\delta u_I$.
- **Eq. (7):** the fifth term prints "$p_i$" (subscript) where the other
  terms use the iterate $p^i$. **Eq. (A2)** and the text after Eq. (A3) use
  the superscript $k$ ($a_N^k$, $\dot p_N^k$) where the iteration index is
  $i$.
- **Abstract against the tables:** *(compiler check, not in the sources)*
  the per-sample exact/NN time ratios are $76.589\ \mathrm{ms}/18.2\ \mu\mathrm s\approx4.2\times10^3$
  (CI, Table III), $1.612\ \mathrm s/16.4\ \mu\mathrm s\approx9.8\times10^4$
  (SF, Table V) and $21.36\ \mathrm s/19.3\ \mu\mathrm s\approx1.1\times10^6$
  (HE, Table IV), so "more than five orders of magnitude" holds for HE only;
  "prediction errors below 0.8%" holds for NN+EE (overall at most 0.191%)
  but not for NN (CI overall $\varepsilon_{u^*}=1.120\%$; per configuration
  up to 2.376% for CI SCR, 1.632% for SF RCS and 1.699% for HE SCR).
- **CFD speed-up:** *(compiler check, not in the sources)* exact/network
  per-iteration ratios are $134/0.215\approx623$ and $134/0.615\approx218$
  (Table VI), $204/0.407\approx501$ and $204/0.6=340$ (Table VII), 2.3 to
  2.8 orders of magnitude against the printed "three orders"; the
  network/Rusanov ratios are $0.215/0.177\approx1.21$ (HE) and
  $0.407/0.293\approx1.39$ (SF) for NN and about 3.5 and 2.0 for NN+EE,
  against "half as fast".
- **"Overall" rows:** *(compiler check, not in the sources)* the overall
  MAPE values are the means of the four configurations (e.g. Table III NN
  $\varepsilon_{u^*}$: $(0.651+0.899+2.376+0.555)/4=1.120$), the overall
  times are not: Table III exact 76.589 ms against a row mean of 80.79 ms,
  NN 18.2 μs against 27.1 μs; Table V NN+EE 472 ms against 353 ms, NN 16.4
  μs against 25.3 μs; Table IX NN+EE 61.5 μs against 141.5 μs. App. B says
  that networks processing all samples in one array are faster, which
  bears on the network columns only.
- **Conclusions:** "The standalone neural network is always the fastest
  with an average time of 28 μs", while Table IX gives 0.512 μs (exact)
  and 0.149 μs (adaptive) against 14.9 μs for the ideal gas, as App. B
  itself says.
- **HE shock tube (§VI):** "$P_I=30$" without unit in the text; the Fig. 5
  caption gives "$P_I=30$ and $P_{IV}=5$ GPa". The Fig. 5 caption says
  "Numerical reconstruction order 0" where §VI states first order in space.
- **§VI scope:** "We compare all previous cases except for calorically
  imperfect gases", then "In the case of high explosives and calorically
  imperfect gases, the results are similar" at fourth order, with no CI
  figure.
- **Architecture:** the hidden-layer width is printed "1028" (§IV, §V).
- **Table I (SF):** the sound speed is printed
  $a(T,\rho)=\sqrt{\gamma(T,\rho)(\partial p/\partial\rho)_\rho}$, a
  derivative with respect to $\rho$ at constant $\rho$.
- **Typos and references:** "Kratsion" (§I) against "A. Kratsios" (Ref.
  21); "Grind converge analysis" (Fig. 8 caption); "fir supercritical
  fluids" (§VI); Ref. 48 (Rusanov) prints pages "304–279"; Ref. 25 repeats
  the volume ("335, 736–746 (2017). (335)"); Ref. 24 prints "Symbolic
  pregression".

# Notation map

| Ruggeri et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u$, $p$, $E=\rho e+\rho u^2/2$ | $\rho$, $u$, $p$, $E$ | inviscid 1-D Euler; $e$ specific internal energy |
| $\mathbf Q$, $\mathbf F$ | (conserved state, flux) | |
| I, II, III, IV; $p^*$, $u^*$ | (page-local states and star values) | |
| $a$ | (page-local sound speed) | **collision:** also the Peng–Robinson attraction parameter (Table I) |
| $C=\rho a$ | (acoustic impedance, "mass flux") | Eqs. (6), (11) |
| $\gamma$, $\gamma(T)$ | $\gamma$ | variable in the CI and SF closures |
| $\varepsilon$ | (iteration tolerance; Gyrya's range factor) | **collision** with the dissipation rate $\varepsilon$; $\varepsilon_X$ is the MAPE of $X$ |
| $w_{ji}$, $b_j$, $\phi$ | $\boldsymbol\theta$ (weights and biases), activation | MLP, Eq. (13) |
| $F_{w,b}(x_i)$, $y_i$ | (prediction, target) | loss $\mathcal L$ = MAPE, MAE, MSE or Huber |
| $S_I$, $S_{IV}$, $S^*$, $S$, $q_K$ | (HLL, HLLC and Rusanov wave speeds; HLLC shock factor) | definitions differ between HLL and HLLC in the paper |
| $\Gamma$, $p^s$, $e^s$, $T^s$, $\rho_0$ | (Davis equation of state) | values from the cited reference, not printed |
| $p_c$, $T_c$ | (critical pressure and temperature of CO$_2$) | |
| "order 1", "order 4" | $N=0$ (first-order finite volume); $N=3$ flux reconstruction | fourth order = degree 3 |

# Reference list

50 printed references, numbered (AIP superscript style). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. 2 (Gyrya et al., "J. Comput. Phys. (submitted)", no year) is
keyed with the citing paper's year; Ref. 37 (a NASA web page, "accessed
November 8, 2021", no author or date) likewise; Ref. 41 (Abadi et al.)
prints "et al.". The arXiv preprints (Refs. 5, 7, 20, 30, 42) and the
submitted Ref. 2 stay separate entries. Same-author same-year works take
suffixes in printed order (Kim 2019 [11], [38]; Raissi 2017 [22], [25];
Raissi 2018 [23], [26]; Migliorino 2020 [15], [40]; Wang 2022 [4], [18]).
Ref. 36 is the ingested [Eivazi et al. (2022)](/sources/eivazi-2022.md). No
printed duplicates, no unparseable item.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)
- [Super-resolution subgrid-scale models](/methods/super-resolution-sgs-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
