---
type: Method
title: "Machine-learning wall models"
description: "Wall-stress models for wall-modelled LES learned by supervised regression or multi-agent reinforcement learning: the published models, their a posteriori behaviour in channel flow up to Re_tau = 10^10, the extrapolation argument from activation functions, log-law preservation as the acceptance test, and cost."
status: established
aliases: [MLWM, ML wall model, neural-network wall model, data-driven wall model, reinforcement-learning wall model, RLWM, SciMARL wall model]
tags: [wall-model, wmles, machine-learning, neural-network, reinforcement-learning]
timestamp: 2026-10-25T13:44:00Z
---

# Machine-learning wall models

A machine-learning wall model (MLWM) is a wall-stress boundary condition for
[wall-modelled LES](/methods/wall-modelled-les.md) whose map from the LES state
near the wall to $\tau_w$ is learned rather than derived from the
[law of the wall](/definitions/law-of-the-wall.md). Two families exist in the
sources: supervised networks trained on high-fidelity data, and
reinforcement-learning (RL) agents trained inside the WMLES itself. The main
evidence is the comparative a posteriori study of [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md),
which implements three published models in [LESGO](/software/lesgo.md), uses
them as trained by their authors (no re-training), and compares them with the
algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md) in
half-channel flow at eleven $Re_\tau$ from 180 to $10^{10}$, on grids of
$24^3$, $48^3$, $72^3$ (and $32^3$). Their motivation is the demand, recalled
from Rumsey et al., that a learned model must not degrade the baseline.

## Models tested

| Model (label of Vadrot et al.) | Kind | Inputs → output | Training | Network |
|---|---|---|---|---|
| HYK19 (Huang, Yang & Kunz 2019) | supervised | $y^+$, $y^+/l^+_\Omega$ → departure of $U^+_{\mathrm{LES}}$ from an empirical rotating-channel profile; $u_\tau$ found iteratively | DNS of spanwise-rotating channels, $Re_\tau=180$–$1500$ | 4-4-2 hidden neurons, sigmoid |
| ZHY21 (Zhou, He & Yang 2021) | supervised | velocity components and pressure gradients at three heights $h_{\mathrm{wm}}$, $+0.03\delta$, $+0.06\delta$, scaled with $\delta$, bulk velocity and a near-wall scale → two wall-stress components | channel and [periodic hill](/benchmarks/periodic-hill.md) at hill Reynolds numbers 5600–10 595 | 6 × 20, ReLU |
| ZYZY22 (Zhou, Yang, Zhang & Yang 2022) | supervised | as ZHY21 | re-trained with another activation, adding law-of-the-wall channel data $Re_\tau=10^3$–$10^9$ | 6 × 15 |
| BK22 (Bae & Koumoutsakos 2022) | multi-agent RL | states $1/\kappa_{\mathrm{wm}}$, $B_{\mathrm{wm}}$ → action $a_t\in[0.9,1.1]$ with $\tau_w(t_{n+1})=a_t\,\tau_w(t_n)$ | inside WMLES at $Re_\tau=2000$, 4200, 8000, from equilibrium-model fields, no high-fidelity data | not given in the source read |

(Vadrot et al. 2023b, §II.B, Eqs. 3–8, Table I, Figs. 1–2; $l_\Omega$ is a
rotation length, page-local.) The BK22 states are the local log-law slope and
intercept seen by the agent at $h_{\mathrm{wm}}$,
$1/\kappa_{\mathrm{wm}}=(h_{\mathrm{wm}}/u_{\tau,\mathrm{wm}})\,\partial u/\partial y|_{h_{\mathrm{wm}}}$
and $B_{\mathrm{wm}}=U_{\mathrm{LES}}/u_{\tau,\mathrm{wm}}-\kappa_{\mathrm{wm}}^{-1}\ln(h_{\mathrm{wm}}u_{\tau,\mathrm{wm}}/\nu)$,
with $u_{\tau,\mathrm{wm}}=\sqrt{\tau_w/\rho}$ (Eq. 8; page-local). Agents sit
in the wall-parallel plane (16, 64 or 128), share one policy, and $\tau_w$
elsewhere is bilinearly interpolated; at run time the solver must be coupled
to the RL library. The RL notation is that of
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

Vadrot et al. (2023b, §I) also recall earlier models they do not test: the
first network wall model of Yang et al. (2019), trained at $Re_\tau=1000$;
the classifier-plus-predictor of Lozano-Durán & Bae, poor in separation zones
of the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md); gradient-boosted
trees of Radhakrishnan et al., whose a posteriori results match their own
equilibrium model including its log-layer mismatch; and a CNN of Moriya et al.,
trained at $Re_\tau=180$, which deteriorates for $\Delta y^+>10$.
[Beck & Kurz (2023)](/sources/beck-2023.md) (§II.A) list the RL wall models of
Bae and colleagues among the first applications of RL to closure modelling.

## A posteriori findings

- **HYK19** gives the right mean velocity at every $Re_\tau$, seen and unseen,
  wherever $h_{\mathrm{wm}}$ lies, and beats the equilibrium model when the
  matching point is in the viscous or buffer layer; elsewhere it reproduces the
  equilibrium model (§III.A, §IV.A, Fig. 5). Appendix A notes a residual
  negative mismatch at low $Re_\tau$.
- **ZHY21** over-predicts $\tau_w$, increasingly with $Re_\tau$ (§IV.B).
- **ZYZY22** recovers a log law, but with $\kappa=0.32$, so its
  [log-layer mismatch](/definitions/log-layer-mismatch.md) grows with
  $Re_\tau$; it works only on the $32^3$ grid, where the spacing of its three
  input heights equals the training value $0.03\delta$ (§III.A, §IV.B, Eq. 9).
  The authors first find it "not clear … why" $\kappa$ is small, and in §V
  point to the LES side (solver, SGS model).
- **BK22** recovers the log law with a positive mismatch at low and a negative
  one at high $Re_\tau$ (from $+2.2$ at 180 to about $-3.2$ for $10^8$–$10^{10}$),
  best near $Re_\tau=10^5$, where $h^+_{\mathrm{wm}}$ is close to training
  conditions; it shows weak grid dependence; the number of agents barely
  matters, though 16 agents failed to converge above $Re_\tau=10^9$ (§III.B,
  Table III, Figs. 8–10). The mismatch is traced to the fixed learned action
  boundary against a neutral line that moves with $Re_\tau$ and grid (§IV.C;
  details on the log-layer-mismatch page). Vadrot et al. attribute the
  differences from Bae & Koumoutsakos's own results mainly to grid resolution.
- The SGS model (anisotropic minimum dissipation against a Lagrangian
  scale-dependent dynamic model) and the domain size barely affect the learned
  models, "indicating that the learned models are not significantly adjusted to
  compensate for deficiencies in the SGS model" (App. B).

## A priori against a posteriori

The ZHY21 history is an instance of the gap described on the
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
page: good a priori, poor a posteriori on periodic hills (as recalled by Vadrot
et al. 2023b, §I), and poor a posteriori in channel flow here. Conversely, fed
an exact law of the wall a priori (pressure terms zero, inputs at
$0.03\delta$, $0.06\delta$, $0.09\delta$), ZYZY22 is accurate at all $Re_\tau$
except 180 and ZHY21 still over-predicts $\tau_w$, with an error growing with
$Re_\tau$ (§IV.B, Figs. 12–13); ZYZY22's a posteriori error is therefore
located on the LES side. Varying the first input height with the spacing fixed
at $0.03\delta$ gives no error; tying the spacing to the grid does.

[Duraisamy (2021)](/sources/duraisamy-2021.md) states the general principle
for learned closures: a priori training "establishes the consistency of the ML
model with the DNS field, but does not guarantee consistency with the RANS or
LES environment" (§IV.A), whence [model-consistent training](/methods/model-consistent-training.md);
RL training inside the WMLES, as in BK22, is one way to obtain it. Duraisamy
(2021, §V) also names wall-distance and wall-stress measures among the
non-local features that have proved important, and records that the goal of
generalizable learned models "has, however, not been achieved" (§VII).

## Extrapolation and the activation function

Vadrot et al. (2023b, §IV) explain the high-$Re$ behaviour with the
extrapolation theorem of Bin, Chen, Huang & Yang (2022), as they state it: a
non-trivial feed-forward network from $\mathbb R$ to $\mathbb R$ tends to a
finite constant at infinity if all neurons use the sigmoid, and grows like
$x$ (including $0\cdot x$) if all use the ReLU. The theorem was proved for
bias-free networks and is "often applicable" to general ones.

- HYK19 (sigmoid) outputs the log-law intercept; its output tends to a
  constant at large $y^+$, which is the right asymptote (Fig. 11).
- ZHY21 (ReLU) takes $\ln(h_{\mathrm{wm}}/y_p)$ as input ($y_p$ its near-wall
  length, page-local), which diverges as $Re\to\infty$, so its normalized wall
  stress diverges where it should tend to zero; a ReLU network can still be
  designed with the right asymptote (§IV.B).

## Position: preserve the law of the wall

Vadrot et al. (2023b, §V) conclude that a learned wall model must preserve the
known empiricism — the law of the wall — and must not degrade the baseline
model; they recommend "progressive learning", channel flow as a sanity check,
and attention to extrapolation and interpretability. HYK19 improves "in and
only in" rotating channels and reproduces the equilibrium model elsewhere,
which they hold up as the desired behaviour (§IV.A).

## Cost

With $N_{\mathrm{op}}=\sum_{i=2}^{L}(n_{i-1}+2)\,n_i$ operations for a
feed-forward network of $L$ layers with $n_i$ neurons (Eq. 15; page-local),
HYK19, ZYZY22 and BK22 cost 56, 1609 and 17 412 operations per evaluation
(BK22 with one agent per grid point), against 5 for the algebraic log-law
model. The ODE-based equilibrium model, which adds 10–30 % to an LES, measured
about four times the cost of BK22 on one cluster, so all three learned models
are estimated cheaper than it. Training cost is excluded (about $10^7$ gradient
steps for BK22) (§IV.D). The counts 56 and 1609 follow from Eq. (15) with
layers $(2,4,4,2,1)$ and $(18,15,15,15,15,15,15,2)$; BK22's architecture is not
printed, so 17 412 cannot be checked *(compiler check, not in the sources)*.

## Qualifications

- All evidence is channel flow, plus the original authors' training cases;
  no learned wall model is tested here in a separated or three-dimensional
  flow.
- Vadrot et al. print $l^+_\Omega=u_\tau/(2\Omega_{\mathrm{rot}})$ and
  $l_\Omega=u_\tau/(2\Omega_{\mathrm{rot}})$ for the inner-scaled and the
  dimensional rotation length (§II.B.2, l. 139, 143); the expression has units
  of length, so the inner-scaled one is $l_\Omega u_\tau/\nu$ *(compiler check,
  not in the sources)*.
- Their Table I mixes a $y$-wall-normal convention (features with $\partial p/\partial z$,
  $v$, output $\tau_{yz}$) with the paper's $z$-wall-normal convention; the
  table is translated here by meaning, not symbol.
- The cost ratio of about four rests on one rough timing without hardware
  detail and excludes the run-time coupling to the RL library.

# Citations

- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I; §II.B, Eqs. (1)–(8), Tables I–II; §III, Figs. 5–10; §IV, Eqs. (9)–(15), Figs. 11–15, Table III; §V; Apps. A–B.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.A; §V; §VII.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §II.A.
