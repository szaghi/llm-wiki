---
type: Source
title: "Gottlieb, Shu & Tadmor (2001) — Strong stability-preserving high-order time discretization methods"
description: "Review and extension of TVD time discretizations under the new name SSP: optimal linear SSP Runge–Kutta methods of any order with CFL coefficient 1, stability for coercive operators, nonlinear and low-storage SSP Runge–Kutta, SSP multistep methods, and the nonexistence of implicit SSP methods above first order."
resource: "doi:10.1137/S003614450036757X"
source_kind: paper
authors: [Gottlieb S., Shu C.-W., Tadmor E.]
year: 2001
venue: "SIAM Rev. 43:89-112"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2001-SIAMRev-Gottlieb-101137S003614450036757X.pdf"
tags: [ssp, time-discretization, multistep, review]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper that fixes the name *strong stability preserving*: high-order
time discretizations that keep any norm or convex-functional stability
of forward Euler under a scaled step. It reviews Shu–Osher and
Gottlieb–Shu and adds four things: optimal linear SSP Runge–Kutta
methods of every order; an improved stability proof for RK4 on
coercive operators; a systematic study of SSP multistep methods; and
negative results for implicit SSP methods. Merged into
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and the new
[SSP order barriers](/results/ssp-order-barriers.md).

# Key claims

1. **Why SSP** (§2.1): a non-SSP second-order RK with TVD MUSCL
   overshoots on Burgers' equation, and the SSP one does not (Fig. 2.1).
   Since the argument rests on convexity, any norm or convex functional
   — maximum norm, cell entropy — is preserved, and TVB-type
   $(1 + O(\Delta t))$ bounds carry over.
2. **Lemmas 2.1–2.3**: $\mathcal{C} = \min a_{ik}/b_{ik}$; with
   $\tilde{\mathcal{L}}$, $\min a_{ik}/\vert b_{ik}\vert$; the same for
   multistep methods.
3. **Linear SSP RK** (§3): $\mathcal{C} \le 1$ for $m$ stages and order
   $m$ (Proposition 3.1); the optimal method of every order, with
   $\mathcal{C} = 1$ and coefficients in Table 3.1 up to $m = 8$
   (Proposition 3.2); convex decompositions of the RK3 and RK4
   polynomials.
4. **Coercive operators** (§3.2): RK4 is stable under $\Delta t \le 2\eta$
   with growth $e^{3Kt}$ (Proposition 3.3), improving Levy–Tadmor's
   $\eta/31$.
5. **Nonlinear SSP RK** (§4): optimal RK2 and RK3 with $\mathcal{C} = 1$;
   four-stage fourth order needs negative $b_{ik}$, best found
   $\mathcal{C} = 0.936$ (effective 0.624); low-storage third order
   $\mathcal{C} = 0.32$; two-step two-stage hybrids at most third order
   ($\approx 0.473$).
6. **Multistep** (§5): barriers (Proposition 5.1), optimal coefficients
   for two- to four-step methods, and fifteen schemes (Table 5.1),
   including a five-step fourth-order method with $b_i \ge 0$
   ($\mathcal{C} = 0.021$).
7. **Implicit** (§6): no SSP implicit RK or multistep method above first
   order (Propositions 6.2–6.3); a non-SSP implicit RK2 oscillates at CFL
   1.4 where backward Euler is monotone.

# Notation map

| Gottlieb, Shu & Tadmor (2001) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $L$, $\tilde L$ | $\mathcal{L}$, $\tilde{\mathcal{L}}$ | |
| $\alpha_{i,k}$, $\beta_{i,k}$ | $a_{ik}$, $b_{ik}$ | registry $\alpha$ is the LF speed |
| $\alpha_i$, $\beta_i$ (multistep) | $a_i$, $b_i$ | |
| $c$ (CFL coefficient) | $\mathcal{C}$ | |
| $\Delta t_{FE}$ | $\Delta t_{\mathrm{FE}}$ | |
| $m$ (stages or steps) | $s$ (stages), $m$ (steps) | |
| $\eta(t)$, $K$ | $\eta$, $K_{\mathrm{L}}$ | coercivity, Lipschitz constant |

# Pages created or updated

* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Order barriers and optimal coefficients of SSP time discretizations](/results/ssp-order-barriers.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2001-SIAMRev-Gottlieb-101137S003614450036757X.pdf` (doi:10.1137/S003614450036757X; typeset SIAM Review article): text extraction, all sections. The fourth-order method (4.3), the low-storage coefficients and the multistep Table 5.1 are illegible in the text layer and are not reproduced; Table 3.1 entries were checked against the recursion (3.2). Reference list: 23 entries.
