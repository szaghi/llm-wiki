---
type: Source
title: "Müller (2023) — Exact conservation laws for neural network integrators of dynamical systems"
description: "Builds a learned integrator from a Lagrangian neural network whose first layer maps positions and velocities to invariants of a continuous symmetry group, so that Noether's theorem makes the network's linear and angular momenta exact first integrals of the learned ODE, which is then advanced with RK4."
resource: "doi:10.1016/j.jcp.2023.112234"
source_kind: paper
authors: [Müller E.H.]
year: 2023
venue: "J. Comput. Phys. 488:112234"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Journal_of_Computational_Physics_Müller_Exact_conservation_laws_for_neural_network_integrators_of_dy.pdf"
tags: [structure-preserving, geometric-integration, hamiltonian, runge-kutta]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper builds a [learned time integrator](/methods/learned-time-integrators.md)
for Lagrangian mechanical systems. A dense neural network represents the
Lagrangian $\mathcal L_{\rm NN}(q,\dot q)$, following the Lagrangian neural
networks of Cranmer et al.; the acceleration follows from the Euler–Lagrange
equations by automatic differentiation and a Hessian solve,
$\ddot q=(\partial^2_{\dot q\dot q}\mathcal L_{\rm NN})^{-1}(\partial_q\mathcal L_{\rm NN}-\partial^2_{q\dot q}\mathcal L_{\rm NN}\,\dot q)$,
and the resulting ODE is advanced with classical RK4. The contribution is a
**symmetry-enforcing input layer** that maps $(q,\dot q)$ to scalar invariants
of a continuous group (rotations, translations or both) before the dense
layers. The network Lagrangian is then exactly invariant, so by Noether's
theorem the corresponding network momenta are exact first integrals of the
learned ODE, whatever the weights.

Training data are exact trajectories (RK4, $h=10^{-2}$) with Gaussian noise
$\sigma_{\rm n}=10^{-3}$ for three systems: a particle in a $1/\lvert q\rvert$
potential in three dimensions (the [Kepler problem](/benchmarks/kepler-problem.md),
eccentricity 0.8), a massive particle in the Schwarzschild metric, and two
particles in four dimensions with a double-well interaction. Integrated with
RK4 at $h=10^{-2}$, the symmetric networks conserve their own momenta to
single-precision rounding (about $10^{-5}$ or less) and keep the true momenta
within $10^{-3}$ (Kepler, Schwarzschild) or 1% (two particles, rotations and
translations), against 10% drift or blow-up for unconstrained networks; they
also reduce the growth of $10^{-3}$ initial perturbations by about an order of
magnitude. The author likens the exactly conserved network momentum to the
shadow Hamiltonian of [symplectic integrators](/properties/symplecticity.md);
that is an analogy, not a theorem. The exactness concerns the continuous
learned flow: the RK4 map does not preserve general nonlinear invariants, and
the paper attributes the residual drift to rounding without a step-size study.

# Version read

The file is the arXiv preprint arXiv:2209.11661v2 (14 May 2023; page-1 date
16 May 2023), author-typeset, 24 pages, all read, with visual checks of pp. 8,
9, 10, 13, 16 and 20. Its acknowledgement thanks two anonymous reviewers, so
it is the post-review text. It prints neither the journal nor the DOI; the
metadata are those of Crossref. Title and author on page 1 match. Code:
release on Zenodo, doi:10.5281/zenodo.7108069 (ref. [42]).

# Key claims

1. If the Lagrangian is invariant under a one-parameter family of maps $h^\theta$ (Eq. 1), then $I=\frac{\partial\mathcal L}{\partial\dot q}\frac{dh^\theta(q)}{d\theta}\big|_{\theta=0}$ is a constant of motion (Noether's theorem, §2.1, Eqs. 1–2; proof cited to Arnold). **Stated**
2. Composing the dense layers with a first layer whose outputs are invariant under the group (Eq. 11) makes $\mathcal L_{\rm NN}$ exactly invariant, so the Noether quantities of the learned dynamics are conserved exactly, "independent of the weights of the neural network" (§2.2, §2.3.1 after Eq. 14). **Derived**
3. For rotation invariance with one position and one velocity in three dimensions the layer outputs $q\cdot q$, $\dot q\cdot\dot q$ and $q\cdot\dot q$; the conserved quantities are the network angular momenta $L^{(\rho)}_{\rm NN}=\varepsilon^{\rho\sigma\tau}q_\sigma\,\partial\mathcal L_{\rm NN}/\partial\dot q_\tau$ (Eq. 14). **Derived**
4. For two particles in $D$ dimensions a general Lagrangian depends on $4D$ variables; translation invariance reduces them to $3D$, rotation invariance to $10+\binom4D$, both to $6+\binom3D$ (§2.3.3, p. 9; Table 2: 16, 12, 11 and 6 inputs for $D=4$). **Derived**
5. The two-particle system has $\tfrac12D(D+1)$ Noether quantities: $D$ linear momenta and $\tfrac12D(D-1)$ angular momenta (Eq. 32). **Derived**
6. The $SO(D)$ invariants of $n$ vectors are the $\tfrac12n(n+1)$ dot products and the $\binom nD$ full Levi-Civita contractions; for $O(D)$ the dot products suffice (App. A, Eqs. 39–41, citing Villar et al. and Weyl). **Stated**
7. Equivariance of a learned force (as in graph-network emulators) does not imply a conserved quantity; only invariance of the Lagrangian or Hamiltonian under a continuous symmetry does (§1.1.5, citing Finzi et al.). **Stated**
8. Training reaches mean squared errors of $10^{-5}$–$10^{-6}$ (Kepler), $10^{-6}$ (Schwarzschild) and about $10^{-4}$ (two particles); the noise limits the attainable error to $\sigma_{\rm n}^2\sim10^{-6}$ (§3.1, App. B, Figs. 12–14). **Shown**
9. Kepler (three dimensions, unit mass and coupling, eccentricity 0.8, $L_z=1$, RK4 with $h=10^{-2}$, final time 128): unconstrained-network trajectories leave the ellipse and become unstable; the relative drift of the true angular momentum grows to about 1 by $t\approx50$ and diverges shortly after (§3.1.1, Figs. 3–4). **Shown**
10. Kepler with the rotation-invariant network: trajectories visually indistinguishable from the true ellipse; the drift of $L_{\rm NN}$ "remains zero within single precision rounding errors"; the drift of the true $L$ never exceeds $10^{-3}$ (§3.1.1, Fig. 4). **Shown**
11. Kepler: trajectories from initial data perturbed by $10^{-3}$ stay within 0.1 of each other up to $t=128$ for the invariant network, while for the unconstrained one they separate by more than 1 by $t\approx55$ (§3.1.1, Fig. 5). **Shown**
12. Schwarzschild (Schwarzschild radius 0.1, RK4 with $h=10^{-2}$, final time 1000): the unconstrained network does not blow up but drifts from the truth and oscillates about the $x$–$y$ plane; its true angular momentum deviates by about 10% at later times (§3.1.2, Figs. 6–7). **Shown**
13. Schwarzschild with rotation invariance: true-momentum drift below $10^{-3}$; network-momentum drift never above about $10^{-5}$, "consistent with (accumulated) rounding errors in single precision arithmetic"; perturbation growth about one order of magnitude smaller than unconstrained (§3.1.2, Figs. 7–8). **Shown**
14. Using the far-observer time itself as an input destabilizes training because it grows linearly; dropping it is consistent with the true Lagrangian (18), which depends only on its derivative (§2.3.2). **Shown** (asserted from experience; no figure)
15. Two particles in four dimensions (masses 1 and 0.8, zero total linear momentum, final time 8): the unconstrained network loses 10%–100% of the true linear and angular momenta by the final time; rotation invariance alone keeps both below about 10%; rotation and translation together keep both within 1% with no upward trend; network momenta are conserved to single-precision rounding (§3.1.3, Figs. 9–10). **Shown**
16. Two particles: the rotation-and-translation network gives the best trajectories, though the final-position distance remains $O(1)$, mainly from a phase lag (§3.1.3, Fig. 9). **Shown**
17. Two particles: perturbation growth is reduced most by the network with both symmetries, but either symmetry alone is almost as good, translation only slightly better at large $t$ (§3.1.3, Fig. 11). **Shown**
18. Although only $L_{\rm NN}$ is guaranteed conserved, the true $L$ is also much better conserved; the author compares this with the near-conservation of the true energy by symplectic integrators through exact conservation of a shadow Hamiltonian (§2.3.1, §3.1.1). **Stated** (analogy)
19. Scaling: the $d\times d$ Hessian of $\mathcal L_{\rm NN}$ in the velocities must be inverted at $O(d^3)$ cost and may be unstable for many particles; the number of invariant features grows quadratically with the number of particles (§4). **Stated**
20. Imposing a separable kinetic energy gives a constant diagonal Hessian but excludes non-separable systems such as the double pendulum (§4). **Stated**
21. LSTM integrators that predict the next state from several past states can be seen as an extension of linear multistep methods aimed at larger steps (§1.1). **Stated**
22. Hamiltonian neural networks use the non-symplectic RK4; symplectic recurrent networks use Störmer–Verlet and are argued to perform better (§1.1.1). **Stated**

# Printed slips

- §2.2 (pp. 5–6): the Lagrangian network is attributed to "[13]" ("as in [13]"; "the standard architecture already introduced in [13]"), which is the Hamiltonian neural network paper of Greydanus et al.; the Lagrangian network is ref. [16] (Cranmer et al.), as §1.2 and §4 say.
- §2.3.3 (p. 8): velocities printed "$\dot x^{(2)},\dot x^{(2)}$" for $\dot x^{(1)},\dot x^{(2)}$; Eq. (22) prints the second kinetic term with $\dot x^{(1)}$ instead of $\dot x^{(2)}$ (Eq. 33 has the right form).
- Eq. (24): "for $\in\mathbb R^D$" (variable missing). Eq. (34): last components labelled $M^{(D-1,D)}$ in the angular-momentum vectors. p. 9: the angular momenta are called $J^{(\rho,\sigma)}_{\rm NN}$ before Eq. (32) names them $L^{(\rho,\sigma)}_{\rm NN}$.
- §3.1.3 (p. 13): "total linear momentum $M=m_1x^{(1)}+m_2x^{(2)}$" lacks the dots; p. 16: the rotation set lists $\dot x^{(2)}$ twice; p. 18: "$\delta L_{\rm NN}(t)$" where the context needs the true $L$.
- §3.1 (p. 10): the output-layer initialization standard deviation is printed "$\sqrt{n_h}$" while the others are $2/\sqrt{n_h}$ and $1/\sqrt{n_h}$.
- App. A (p. 20): index bound "$\alpha_D\le D$" should be $\le n$.
- Captions of Figs. 5, 8 and 11 end in an incomplete sentence; typos "Lagriangian", "the authors on [13]".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $\dot q$, $\ddot q$ | $y=(q,\dot q)$ | second-order system written as $y'=f(y)$; $q\in\mathbb R^d$ |
| $\mathcal L$, $\mathcal L_{\rm NN}$, $\mathcal L_{\rm true}$ | $\mathcal L$ (page-local) | Lagrangian; distinct from the linear operator $L$ |
| $L^{(\rho)}$, $L^{(\rho,\sigma)}$ | $L^{(\rho)}$, $L^{(\rho,\sigma)}$ (page-local) | angular momentum; **collides** with the linear operator $L$ |
| $M^{(\alpha)}$, $\widetilde M$ | — | linear momentum; **collides** with the mass matrix $M$ |
| $J_{q,\dot q}$, $J_{\dot q,\dot q}$ | $\partial^2_{q\dot q}\mathcal L$, $\partial^2_{\dot q\dot q}\mathcal L$ | Hessians; **collide** with the Jacobian $J$ |
| $\Phi$ | $f$ | acceleration map, right-hand side of the learned ODE; **collides** with the elementary weight $\Phi(\tau)$ |
| $h^s$, $h^s_{*,q}$ | $h^\theta$ (page-local) | symmetry maps; **$h$ and $s$ collide** with step and stage count |
| $I$ | — | Noether first integral |
| $H$, $\tilde H$ | — | Hamiltonian and shadow Hamiltonian ([backward error analysis](/methods/backward-error-analysis.md)) |
| $\Delta t$ | $h$ | RK4 step $10^{-2}$ |
| $T$ | — | final time; also the translation layer and the kinetic energy |
| $\sigma$ | $\sigma_{\rm n}$ (page-local) | noise standard deviation |
| $D$, $d$ | $D$, $d$ | spatial dimension, system dimension ($d=2D$ for two particles) |
| $\varepsilon^{\rho\sigma\tau}$, $\varepsilon_{\rm ecc}$ | — | Levi-Civita symbol; eccentricity; distinct from the stiffness $\varepsilon$ |
| $\alpha$, $\mu$, $\kappa$, $r_s$, $\tau$ | — | coupling constant, double-well parameters, Schwarzschild radius, far-observer time ($t$ is proper time, reversed from common usage) |
| RK4 | — | classical fourth-order Runge–Kutta method |

# Reference list

The paper prints 44 references in numbered style ([1]–[44]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` this
slug. Ref. [42] is the author's code release with a printed Zenodo DOI; ref.
[7] (Noether) prints a EuDML URL and ref. [41] the TensorFlow URL; ref. [4]
(Einstein) is a chapter in a 1923 collection; ref. [12] is the
Hairer–Nørsett–Wanner book. Refs. [8], [14], [16], [17], [24], [25], [28] and
[30] are printed as preprints and stay preprint entries. No printed
duplicates; all items parsed.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Kepler problem](/benchmarks/kepler-problem.md)
* [Learned time integrators: neural surrogates and physics-informed Runge–Kutta networks](/methods/learned-time-integrators.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
