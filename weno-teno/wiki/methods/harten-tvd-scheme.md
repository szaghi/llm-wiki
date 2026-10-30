---
type: Method
title: "Harten's high-resolution TVD scheme"
description: "Harten's 1983 scheme applies a first-order total-variation-nonincreasing three-point scheme to a modified flux whose minmod-limited correction cancels the leading viscous error, giving a five-point second-order scheme that keeps the original CFL bound; the page gives the scalar construction, its lemmas, the characteristic extension to systems, the choices of viscosity, and the Euler tests."
status: established
aliases: [Harten's TVD scheme, modified-flux TVD scheme, Harten's second-order TVNI scheme, ULT1, ULT2, high resolution scheme]
tags: [limiting, numerical-flux, finite-difference, characteristic]
timestamp: 2026-10-30T08:43:00Z
---

# Harten's high-resolution TVD scheme

[Harten (1983a)](/sources/harten-1983.md) constructs explicit, conservative, five-point
schemes for hyperbolic conservation laws that are second-order accurate away from
extrema and **total variation nonincreasing** (TVNI, the property later called
[TVD](/definitions/total-variation-diminishing.md); the paper never prints "TVD") in the
scalar case. The idea is to take a first-order TVNI three-point scheme and apply it, not
to $f$, but to a **modified flux** $f+\frac{\Delta x}{\Delta t}\mathsf g$, where the
correction $\mathsf g$ is a limited approximation of the leading viscous term of the
first-order scheme; the modified scheme is second order and TVNI under the same CFL
restriction as the original (§3, Lemmas 3.2–3.4). Systems are treated by applying the
scalar scheme to each characteristic field of a local linearization (§4).

## First-order three-point schemes and the viscosity function $\mathfrak Q$

Harten writes every three-point conservative scheme with a differentiable flux as

$$\hat f_{i+1/2}=\tfrac12\Big[f(u_i)+f(u_{i+1})-\frac{\Delta x}{\Delta t}\,\mathfrak Q(\nu_{i+1/2})\,(u_{i+1}-u_i)\Big],\qquad
\nu_{i+1/2}=\frac{\Delta t}{\Delta x}\,\bar a_{i+1/2},$$

with the divided-difference speed $\bar a_{i+1/2}=\big(f(u_{i+1})-f(u_i)\big)/(u_{i+1}-u_i)$
($f'(u_i)$ when $u_{i+1}=u_i$), the signed local Courant number $\nu_{i+1/2}$, and the
function $\mathfrak Q$ that "is often referred to as the coefficient of numerical viscosity" (§3,
Eqs. (3.1), (3.4a); page-local $\mathfrak Q$, $\bar a_{i+1/2}$, $\nu_{i+1/2}$; $\mathfrak Q$ is the source's $Q$, renamed
to keep the SBP matrix $Q$ of the registry free, and $\bar a_{i+1/2}$ is the Rankine–Hugoniot speed of
the [Roe solver](/methods/roe-riemann-solver.md) page, not a cell average). In Harten's incremental form
$u^{n+1}_i=u_i+C^+_{i+1/2}(u_{i+1}-u_i)-C^-_{i-1/2}(u_i-u_{i-1})$ the coefficients are
$C^\pm_{i+1/2}=\tfrac12\big[\mathfrak Q(\nu_{i+1/2})\mp\nu_{i+1/2}\big]$, $C^++C^-=\mathfrak Q$ (Eqs.
(3.5a,c); page-local $C^\pm$). **Lemma 3.1:** the scheme is TVNI under
$\frac{\Delta t}{\Delta x}\max_i\lvert\bar a_{i+1/2}\rvert\le\nu_{\max}\le1$ if

$$\lvert x\rvert\le \mathfrak Q(x)\le1\qquad\text{for }0\le\lvert x\rvert\le\nu_{\max}$$

(Eqs. (3.2)–(3.3); page-local bound $\nu_{\max}$, the source's $\mu$), a consequence of the
sufficient incremental-form condition of Lemma 2.2 (see
[TVD](/definitions/total-variation-diminishing.md)). The Lax–Wendroff scheme is
$\mathfrak Q(x)=x^2$, which violates (3.2); every admissible $\mathfrak Q$ gives a flux that differs from the
Lax–Wendroff flux by $\frac{\Delta x}{2\Delta t}\big[\mathfrak Q(\nu)-\nu^2\big]\,(u_{i+1}-u_i)=O(\Delta x)$,
so the TVNI three-point schemes are first order (Eqs. (3.6)–(3.7)).

## The modified-flux scheme

Let $\mathsf g_i=\mathsf g(u_{i-1},u_i,u_{i+1})$ (page-local; not the constraint functions
$g_i$ of the registry). Harten applies the three-point scheme to the modified point
fluxes $f(u_i)+\frac{\Delta x}{\Delta t}\mathsf g_i$ (§3, Eqs. (3.8a–d)):

$$\hat f^{\mathrm M}_{i+1/2}=\tfrac12\big[f(u_i)+f(u_{i+1})\big]+\frac{\Delta x}{2\Delta t}\Big[\mathsf g_i+\mathsf g_{i+1}-\mathfrak Q\big(\nu_{i+1/2}+\delta\nu_{i+1/2}\big)(u_{i+1}-u_i)\Big],\qquad
\delta\nu_{i+1/2}=\frac{\mathsf g_{i+1}-\mathsf g_i}{u_{i+1}-u_i},$$

($\delta\nu_{i+1/2}$ page-local, the source's $\gamma_{j+1/2}$: the modified flux carries the
modified Courant number $\nu+\delta\nu$). The correction is limited as

$$\tilde{\mathsf g}_{i+1/2}=\tfrac12\big[\mathfrak Q(\nu_{i+1/2})-\nu_{i+1/2}^2\big]\,(u_{i+1}-u_i),\qquad
\mathsf g_i=s_{i+1/2}\max\big[0,\ \min\big(\lvert\tilde{\mathsf g}_{i+1/2}\rvert,\ s_{i+1/2}\,\tilde{\mathsf g}_{i-1/2}\big)\big],$$

$s_{i+1/2}=\mathrm{sign}\,\tilde{\mathsf g}_{i+1/2}$ (Eq. (3.11); page-local
$\tilde{\mathsf g}$, $s$). *(compiler check, not in the sources: this is
$\mathrm{minmod}(\tilde{\mathsf g}_{i-1/2},\tilde{\mathsf g}_{i+1/2})$, the two-argument minmod
of the [TVD page](/definitions/total-variation-diminishing.md); the paper uses neither the
word minmod nor limiter.)*

- **Lemma 3.2.** If $\mathfrak Q$ is Lipschitz and $\mathsf g_i+\mathsf g_{i+1}=[\mathfrak Q(\nu)-\nu^2]\,(u_{i+1}-u_i)+O(\Delta x^2)$,
  $\mathsf g_{i+1}-\mathsf g_i=O(\Delta x^2)$ (Eq. (3.9)), the modified flux differs from the
  Lax–Wendroff flux by $O(\Delta x^2)$, i.e. the scheme is second order.
- **Lemma 3.3.** The limited $\mathsf g$ of (3.11) satisfies (3.9), and
  $\lvert\delta\nu_{i+1/2}\rvert\le\tfrac12\lvert \mathfrak Q(\nu_{i+1/2})-\nu_{i+1/2}^2\rvert$ (Eq. (3.12)).
- **Lemma 3.4.** The five-point scheme is TVNI under the same restriction (3.3) as the
  three-point one; the proof bounds the modified Courant number,
  $\lvert\nu+\delta\nu\rvert\le1-\tfrac12(\lvert\nu\rvert-1)^2\le1$.

**Why it works** (§3, Eqs. (3.15)–(3.16)). The first-order scheme approximates to second
order the modified equation $\partial_tu+\partial_x\big[f-\frac{\Delta t}{2}\big(\frac{\Delta x}{\Delta t}\big)^2[\mathfrak Q(\nu)-\nu^2]\,\partial_xu\big]=0$,
$\nu=\frac{\Delta t}{\Delta x}f'(u)$, so $\tilde{\mathsf g}$ and $\mathsf g$ approximate
$\tfrac12[\mathfrak Q(\nu)-\nu^2]\,\Delta x\,\partial_xu$; applied to $f+\frac{\Delta x}{\Delta t}\mathsf g$
the scheme cancels its own leading viscosity. Taking $\mathsf g_i$ at points rather than
$\tilde{\mathsf g}_{i+1/2}$ at interfaces gives $\mathsf g$ a bounded derivative.

**Where order is lost** (§3, Remark 2; §5). Condition (3.9) is sufficient for second
order only where $s_{i+1/2}$ is continuous; at points where $\partial_xu=0$ or
$\mathfrak Q(\nu)=\nu^2$ the scheme may degenerate locally, and elsewhere its truncation error is
$O(\Delta x^3)$ independently of $\mathfrak Q$. In the constant-coefficient scalar case it is
convergent although nonlinear (§3, Remark 1).

## Systems: one scalar scheme per characteristic field

For $u\in\mathbb R^m$, Harten takes a symmetric average state $u_{i+1/2}=\mathsf V(u_i,u_{i+1})$,
$\mathsf V(u,v)=\mathsf V(v,u)$, $\mathsf V(u,u)=u$, its eigenvalues $\lambda_l$ and eigenvectors
$R_l$, $L_l$ (columns of $R$, rows of $L$), and the wave strengths
$\delta^{(l)}_{i+1/2}=L_l(u_{i+1/2})(u_{i+1}-u_i)$ (§4, Eqs. (4.6)–(4.7); page-local $\mathsf V$,
$\delta^{(l)}$, the source's $V$, $\alpha^k$). The flux is

$$\hat f_{i+1/2}=\tfrac12\big[f(u_i)+f(u_{i+1})\big]+\frac{\Delta x}{2\Delta t}\sum_{l=1}^mR_l\Big[\mathsf g^{(l)}_i+\mathsf g^{(l)}_{i+1}-\mathfrak Q_l\big(\nu^{(l)}_{i+1/2}+\delta\nu^{(l)}_{i+1/2}\big)\,\delta^{(l)}_{i+1/2}\Big]$$

(Eq. (4.8b)), with $\nu^{(l)}_{i+1/2}=\frac{\Delta t}{\Delta x}\lambda_l(u_{i+1/2})$ and the scalar
formulas field by field: $\tilde{\mathsf g}^{(l)}_{i+1/2}=\tfrac12[\mathfrak Q_l(\nu^{(l)})-(\nu^{(l)})^2]\delta^{(l)}_{i+1/2}$,
$\mathsf g^{(l)}_i$ its minmod, and $\delta\nu^{(l)}_{i+1/2}=(\mathsf g^{(l)}_{i+1}-\mathsf g^{(l)}_i)/\delta^{(l)}_{i+1/2}$,
zero when $\delta^{(l)}_{i+1/2}=0$ (Eqs. (4.8c–e)). The author calls it "a somewhat
generalized version" of Roe's procedure: any symmetric average is allowed, and each field
may have its own $\mathfrak Q_l$ or even its own scalar scheme (§4, Remark 1). This is a flux-level
[characteristic decomposition](/methods/characteristic-decomposition.md) of the jumps
with per-interface eigenvectors.

- **Proved.** Lemma 4.1: the flux is the Lax–Wendroff flux up to $O(\Delta x^2)$ for
  Lipschitz $\mathfrak Q_l$. Lemma 4.2 and Corollary 4.3: for a **constant** Jacobian the scheme is
  TVNI in the characteristic total variation $\sum_i\sum_l\lvert\delta^{(l)}_{i+1/2}\rvert$
  (Eq. (4.12)) under $\frac{\Delta t}{\Delta x}\max\lvert\lambda_l\rvert\le\min_l\nu_{\max,l}\le1$,
  convergent for bounded-variation data and second order.
- **Not proved.** No estimate of total-variation growth exists for nonlinear systems, and
  convergence there is not proved (§4, Remark 3).
- **Roe's average.** With Roe's mean-value Jacobian the scheme for $m=1$ coincides with the
  scalar one, and if $\mathfrak Q_l(0)=0$ a stationary discontinuity with $f(u)=f(v)$ is a steady
  solution (§4). Harten calls Roe's averaging for the Euler equations (Eq. (7.4)) "rather
  expensive" and the arithmetic mean one that "will do just as well" in many applications;
  replacing $\tfrac12[f(u_i)+f(u_{i+1})]$ by $f(u_{i+1/2})$ is cheaper but may lose the
  perfect resolution of stationary discontinuities (§4, Remark 2; §7). See
  [Roe solver](/methods/roe-riemann-solver.md).

## Choices of the viscosity function

| $\mathfrak Q(x)$ | name in §8 | property (Harten 1983a) |
|---|---|---|
| $\lvert x\rvert$ | ULT1 | least dissipative TVNI three-point scheme; a generalization of Courant–Isaacson–Rees upwind differencing with the monotonicity property for CFL $\le1$ (Eq. (5.1), Lemma 5.1); see [Godunov scheme](/methods/godunov-scheme.md) |
| $\dfrac{x^2}{4\varepsilon_{\mathrm H}}+\varepsilon_{\mathrm H}$ for $\lvert x\rvert<2\varepsilon_{\mathrm H}$, $\lvert x\rvert$ otherwise | — | positive viscosity at zero Courant number, "with say $\varepsilon=0.05$" (Eq. (5.3); page-local $\varepsilon_{\mathrm H}$), with CFL $\nu_{\max}<1$, "say 0.95"; called "the best choice of $\mathfrak Q(x)$" |
| $x^2+\tfrac14$ | ULT2 | Lax–Wendroff plus the linear viscosity $\tfrac18(u_{i+1}-2u_i+u_{i-1})$ (citing earlier work, including Harten's hybrid scheme); $\mathfrak Q-\lvert x\rvert=(\lvert x\rvert-\tfrac12)^2\ge0$; $\mathfrak Q\le1$ limits the CFL bound to $\sqrt3/2\approx0.866$ |

**Entropy.** With $\mathfrak Q(0)=0$ the viscosity coefficient of the modified equation vanishes at
$\nu=0$, so stationary jumps, admissible or not, are steady solutions and the scheme may
select an entropy-violating weak solution; the smoothed $\mathfrak Q$ of (5.3) removes this but cannot
resolve a stationary shock perfectly (§5). Its argument is the Courant number
$x=\frac{\Delta t}{\Delta x}\bar a$, so $\varepsilon_{\mathrm H}$ is a fraction of the CFL number,
not a speed. Harten conjectures that if the three-point scheme is entropy consistent, so
is the modified second-order scheme (§5); there is no proof. Later sources call
smoothings of $\lvert\lambda\rvert$ near zero "Harten" or "Harten–Hyman" entropy fixes
([Roe solver](/methods/roe-riemann-solver.md)); Harten (1983a) names (5.3) neither.

**Contacts.** In linearly degenerate fields Harten multiplies $\mathsf g^{(l)}$ by
$1+\theta_{\mathrm{AC}}$ with a switch that is $O(\Delta x)$ in smooth regions and $O(1)$ at
discontinuities, so contacts stop spreading (§6;
[artificial compression](/methods/artificial-compression.md)).

## Euler implementation and tests

For the Euler equations (§7) the steps are: primitive variables; Roe averages; the time
step $\frac{\Delta t}{\Delta x}=\nu_{\max}/\max_i(\lvert\hat v_{i+1/2}\rvert+\hat c_{i+1/2})$
(page-local Roe averages $\hat v$, $\hat c$); Courant numbers per field; $\tilde{\mathsf g}^{(l)}$;
the compression switch for the contact field only; $\mathsf g^{(l)}$, $\delta\nu^{(l)}$ and the
flux (4.8b). All runs use Roe's linearization (§8):

- **Riemann problems** (§8 I; [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
  On the first data set (conservative states $(0.445,0.3111,8.928)$ and $(0.5,0,1.4275)$,
  140 cells, 100 steps, CFL 0.95) ULT1 resolves shock and contact sharply, without the
  oscillations of Lax–Wendroff and the smearing of Roe's first-order scheme (Figs. 2a–c); on
  Sod's data (100 cells, 50 steps) ULT2 "look[s] almost identical" to ULT1, with "almost no
  dependence on the CFL number" (Figs. 3a–c).
- **Quasi-1D nozzles** (§8 II; [steady shock problems](/benchmarks/steady-shock-problems.md)):
  steady standing shocks in a divergent and a convergent–divergent nozzle with ULT1,
  meshes not quantified (Figs. 4–6, courtesy of H. C. Yee).
- **Mach 3 step** (§8 III; [forward-facing step](/benchmarks/forward-facing-step.md)):
  $10\times30$ grid, CFL 0.75, $t=4$; ULT2 against Harten's earlier hybrid scheme (Fig. 7).
  ULT1, with $\mathfrak Q(0)=0$, shows part of the sonic line at the corner turning into an expansion
  shock, as in the Godunov results of Woodward and Colella that the paper cites. Splitting
  in 2D is $L_xL_yL_yL_x$ ([operator splitting](/methods/operator-splitting.md)).
- **Cost.** The scheme is "simple to program" and needs only slightly more CPU time than
  Lax–Wendroff with artificial viscosity (§8); no timings are printed.

## Qualifications

- The section 8 experiments use $\mathfrak Q=\lvert x\rvert$ (ULT1) and $\mathfrak Q=x^2+\tfrac14$ (ULT2), not the
  smoothed (5.3) that section 5 recommends, and the expansion shock on the step appears
  with ULT1.
- Convergence is proved for scalar laws (fully in the constant-coefficient case) and for
  constant-coefficient systems only; the nonlinear-system scheme rests on the scalar
  analysis field by field.
- Printed slips in the version read (NYU report DOE/ER/03077-175, March 1982): Eq. (3.5b)
  prints $C_\pm=\tfrac12[\mathfrak Q\pm\nu]$ *(compiler check, not in the sources: (3.1) gives
  $C^\pm=\tfrac12[\mathfrak Q\mp\nu]$)*; Eq. (3.10a) prints the factor $\frac1\lambda$ and the argument
  $\bar\nu_{j+1}$ *(compiler check, not in the sources: subtracting (3.1) from (3.8d) gives
  $\frac{1}{2\lambda}$ and $\bar\nu_{j+1/2}$, which the following (3.10b) agrees with)*; the
  proof of Lemma 3.3 drops the factor $\tfrac12$ of (3.12) in its last line; the
  compression switch (6.1b) prints a garbled index in its denominator; Eqs. (8.4)–(8.5) omit
  the wave-strength factor that (8.2) requires. The page uses the consistent forms.
- The CFL statements for the compression variant ($\varepsilon_{\mathrm H}<1/3$ keeps the bound;
  ULT2 tightens to $3/4$, Eqs. (6.3a,b)) are printed without derivation.

# Citations

- [Harten (1983a)](/sources/harten-1983.md) — §2 (Lemma 2.2), §3 (Eqs. (3.1)–(3.16), Lemmas 3.1–3.4, Remarks 1–2), §4 (Eqs. (4.6)–(4.18), Lemmas 4.1–4.2, Corollary 4.3, Remarks 1–3), §5 (Eqs. (5.1)–(5.3), Lemma 5.1), §6 (Eqs. (6.1)–(6.3)), §7 (Eqs. (7.1)–(7.4)), §8 (Eqs. (8.1)–(8.9), Figs. 1–7) (NYU report DOE/ER/03077-175, March 1982).
