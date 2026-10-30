---
type: Method
title: "Exponential nonlinear weights (WCNS-EXP)"
description: "Chen and Deng's exponential nonlinear weights d_k exp(-β_k^λ/λ), with a stencil-local λ that tends to 1 on smooth data and to 10⁻⁶ at discontinuities, keep fifth-order interpolation at critical points of any order using local data only; the page gives the construction, the overflow-free ratio form, tests and the scale dependence."
status: established
aliases: [WCNS-EXP, exponential mapping weights, exponential-mapping nonlinear weights, unconditionally optimal weights, EXP weights]
tags: [weno, reconstruction, finite-difference, compact-scheme]
timestamp: 2026-10-30T08:43:00Z
---

# Exponential nonlinear weights (WCNS-EXP)

Chen & Deng (2023) build fifth-order nonlinear weights whose deviation from the linear weights
vanishes fast enough at smooth **critical points of every order**, using only the data of the
five-point stencil. Instead of a power law in $\beta_k$, as in [WENO-JS](/methods/weno-js-reconstruction.md)
and [WENO-Z](/methods/weno-z.md), the unnormalized weight is an exponential of a power of the
[smoothness indicator](/definitions/smoothness-indicator.md), with a stencil-local exponent that is
1 on smooth data and small at a discontinuity. The authors test the weights in a fifth-order
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md) and call the result
WCNS-EXP. They state that the weights transfer "straightforwardly" to WENO, but leave that to future
work (Abstract, §5).

## Construction

Chen & Deng (2023, §3) work with the point-value interpolation of a staggered WCNS. The three
third-order candidates $u^{(k)}_{i+1/2}$ on $S_0=\{i-2,i-1,i\}$, $S_1=\{i-1,i,i+1\}$ and
$S_2=\{i,i+1,i+2\}$ are combined with the interpolation weights $d=(\tfrac1{16},\tfrac58,\tfrac5{16})$
into the fifth-order interpolant (Eqs. (7)–(10)). The indicators are the point-value form with
coefficient 1 on the second-difference square (Eqs. (14)–(16)):

$$\beta_1=(u_{i-1}-2u_i+u_{i+1})^2+\tfrac14(u_{i-1}-u_{i+1})^2,$$

and $\beta_0$, $\beta_2$ likewise, with the one-sided first differences $u_{i-2}-4u_{i-1}+3u_i$ and
$3u_i-4u_{i+1}+u_{i+2}$. Let $\lambda_{\mathrm E}$ and $\theta_{\mathrm E}$ denote the mapping parameter
and the discontinuity measure (page-local; the source's $\lambda$, $\theta$). The weights are
(Eqs. (26)–(27), (33)–(34))

$$\alpha_k=d_k\exp\!\Big(-\frac{\beta_k^{\lambda_{\mathrm E}}}{\lambda_{\mathrm E}}\Big),\qquad
\omega_k=\frac{\alpha_k}{\sum_l\alpha_l},\qquad
\lambda_{\mathrm E}=\max\big(e^{-3\theta_{\mathrm E}},10^{-6}\big),\qquad
\theta_{\mathrm E}=\frac{\tau_5}{(\min_k\beta_k+\epsilon)^{0.8}},$$

with the WENO-Z global indicator $\tau_5=|\beta_2-\beta_0|$ and $\epsilon=10^{-40}$. The three
constants are empirical:
- the exponent 0.8 speeds up $\lambda_{\mathrm E}\to1$ near high-order critical points at practical
  resolution and machine precision, where $\tau_5\ll\min_k\beta_k$ may not yet hold;
- the factor 3 is chosen "to obtain a more stable scheme";
- the floor $10^{-6}$ keeps the fraction in $\alpha_k$ finite (§3).

## Why the order is kept

Fifth-order interpolation needs $\omega_k=d_k+O(\Delta x^2)$ (Eq. (25), recalled from Deng & Zhang).
For $\lambda_{\mathrm E}=1$, $\alpha_k=d_k e^{-\beta_k}=d_k+O(\Delta x^2)$ because $\beta_k=O(\Delta x^2)$
(Eqs. (28)–(31)). It therefore suffices that $\lambda_{\mathrm E}\to1$ as $\Delta x\to0$ (Eq. (32)). The
authors rely on the result, cited to Borges et al., that $\tau_5$ is at least one order higher in
$\Delta x$ than $\min_k\beta_k$ for smooth data at critical points of any order. Then
$\theta_{\mathrm E}\to0$ and $\lambda_{\mathrm E}\to1$. At a discontinuity $\tau_5\gg\min_k\beta_k$,
$\theta_{\mathrm E}$ is large and $\lambda_{\mathrm E}$ small, and the weights of non-smooth stencils
are suppressed. **Theorem 3.1** states that with these weights the interpolation is "unconditionally
fifth-order for smooth data". Its justification is the paragraph before it; no proof is written out
([accuracy at critical points](/properties/critical-point-accuracy.md)).

*(Compiler check, not in the sources.)*
- With generic Taylor coefficients and an $n_{\mathrm{cp}}$th-order critical point at $x_i$, the printed indicators
  give $\beta_k=O(\Delta x^{2n_{\mathrm{cp}}+2})$ and $\tau_5=O(\Delta x^{2n_{\mathrm{cp}}+3})$ for $n_{\mathrm{cp}}=1,\dots,4$. Hence
  $\theta_{\mathrm E}=O(\Delta x^{0.4n_{\mathrm{cp}}+1.4})$. Away from critical points $\beta_k=O(\Delta x^2)$ and
  $\tau_5=O(\Delta x^5)$, so $\theta_{\mathrm E}=O(\Delta x^{3.4})$.
- The interpolation condition $O(\Delta x^2)$ is weaker than the $O(\Delta x^3)$ sufficient
  condition of finite-difference flux reconstruction. The candidates are third-order values, so
  $\sum_k(\omega_k-d_k)u^{(k)}_{i+1/2}=\sum_k(\omega_k-d_k)(u^{(k)}_{i+1/2}-u_{i+1/2})=O(\Delta x^2)\cdot O(\Delta x^3)$.
  No division by $\Delta x$ follows in an interpolation.

**Small-$\lambda_{\mathrm E}$ limit** *(compiler check, not in the sources)*. Since
$\beta^{\lambda}/\lambda=1/\lambda+\ln\beta+O(\lambda\ln^2\beta)$, at the floor
$\lambda_{\mathrm E}=10^{-6}$ one gets $\alpha_k\approx e^{-10^6}d_k/\beta_k$. Near a discontinuity the
weights therefore become Jiang–Shu weights with exponent $q=1$ and no $\epsilon$, times a common
factor that underflows in double precision.

## Overflow-free evaluation

A direct evaluation of $\alpha_k$ underflows for small $\lambda_{\mathrm E}$. Chen & Deng (2023, §3,
Eqs. (35)–(36)) evaluate the normalized weights through ratios instead. Let
$\mathsf e_{kl}=\exp\!\big(-(\beta_k^{\lambda_{\mathrm E}}-\beta_l^{\lambda_{\mathrm E}})/\lambda_{\mathrm E}\big)$
(page-local). Then

$$\omega_0=\frac{d_0}{d_0+d_1/\mathsf e_{01}+d_2/\mathsf e_{02}},\qquad
\omega_1=\frac{d_1}{d_0\mathsf e_{01}+d_1+d_2/\mathsf e_{12}},\qquad
\omega_2=\frac{d_2}{d_0\mathsf e_{02}+d_1\mathsf e_{12}+d_2}.$$

*(Compiler check, not in the sources: $\mathsf e_{kl}=\alpha_kd_l/(\alpha_ld_k)$, so these are the
normalized weights exactly; the common factor $e^{-1/\lambda_{\mathrm E}}$ cancels.)*

## Tests

All runs use the WCNS framework of the [WCNS](/methods/weighted-compact-nonlinear-scheme.md) page:
- characteristic-variable interpolation with a Roe flux;
- the sixth-order explicit difference that mixes flux-point and solution-point fluxes;
- SSP-RK3 at CFL 0.6.

The comparators are WCNS-JS ($\epsilon=10^{-6}$), WCNS-Z ($q=2$, $\epsilon=10^{-40}$) and a modified
WCNS-MR ([multi-resolution WENO](/methods/multi-resolution-weno.md)) (Chen & Deng 2023, §2–4).

- **Critical points.** On $x^ke^{0.75(x-1)}$, $k=1,\dots,6$, on $[-1,1]$ in quadruple precision, only
  WCNS-EXP reaches fifth order for every $k$, and it is closest to the linear scheme. At $k=2$ (a
  first-order critical point) WCNS-MR falls to third order. WCNS-JS does too, but recovers fifth order
  on fine grids once $\beta_k<\epsilon=10^{-6}$. The orders of WCNS-Z and WCNS-MR rise from second to
  fifth as $k$ goes from 3 to 6 (§4.1, Fig. 2). The test is of the interpolation only; no PDE
  convergence test is shown.
- **Spectral behaviour.** In Pirozzoli's
  [approximate dispersion relation](/definitions/approximate-dispersion-relation.md), WCNS-EXP is
  slightly better than WCNS-JS and comparable with WCNS-Z: better at high wavenumbers, worse at
  moderate ones. WCNS-MR is the most dissipative (§3, Fig. 1).
- **Shock problems.**
  - On [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md) ($N_x=100$), WCNS-EXP is slightly better
    than the other WCNS and than FD WENO-JS, Z and MR with global Lax–Friedrichs splitting.
  - It is slightly better on [Shu–Osher](/benchmarks/shu-osher-problem.md) ($N_x=200$) and similar to
    WCNS-Z on Titarev–Toro ($N_x=1000$) (§4.2).
  - On [double Mach reflection](/benchmarks/double-mach-reflection.md) ($800\times200$) it is similar to
    WCNS-Z. It shows more structure on the [forward-facing step](/benchmarks/forward-facing-step.md)
    ($600\times200$) and the most on the
    [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md) ($100\times400$). The
    first two need a first-order fallback where the fifth-order interpolation gives negative density
    or pressure (§4.3).
  - On the first [2-D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) (initial
    data Eq. (48), $800\times800$), WCNS-EXP resolves more structure but keeps the symmetry less well and is
    more oscillatory than the others. The authors point to minimized-dispersion, adaptive-dissipation
    ideas as a remedy outside their scope (§4.3.1;
    [MDCD schemes](/methods/mdcd-scheme.md), [symmetry preservation](/properties/symmetry-preservation.md)).
- **Cost** ($N_x=1000$, hardware not stated; Table 1). The total CPU times are:

  | problem | WCNS-JS | WCNS-Z | WCNS-MR | WCNS-EXP |
  |---|---|---|---|---|
  | Sod | 110.06 s | 111.13 s | 273.04 s | 147.37 s |
  | Lax | 176.46 s | 183.87 s | 476.27 s | 210.68 s |

  FD WENO with the same weights costs about as much as WCNS.

## Position

Chen & Deng (2023, §1, §5) contrast their weights with earlier unconditionally optimal weights, which
rely on dimensional parameters or on global data and are hard to use on non-uniform grids. They also
contrast them with Baeza, Bürger, Mulet & Zorío's local-data weights, whose framework does not cover
third order. They call theirs "much simpler and also easier to understand". The same goal is pursued
in the bundle by the [WENO-ZN](/methods/weno-zn.md) weights, which reach design order up to a
scheme-dependent critical-point order through an undivided-difference term, and by the symmetric
indicators of IMWENO-P at second-order critical points
([accuracy at critical points](/properties/critical-point-accuracy.md)).

## Qualifications

- **Scale dependence.** The authors claim weights "without using any dimensional scales" (§5).
  *(Compiler check, not in the sources: for $\lambda_{\mathrm E}=1$,
  $\omega_k/\omega_l=(d_k/d_l)\,e^{-(\beta_k-\beta_l)}$. Under $u\mapsto\sigma u$, $\beta_k\mapsto\sigma^2\beta_k$,
  so the ratio changes. $\theta_{\mathrm E}$ scales as $\sigma^{0.4}$, so $\lambda_{\mathrm E}$ changes
  too. The weights are not scale-invariant, and the smooth-region estimate
  $e^{-\beta_k}=1+O(\Delta x^2)$ presumes data of moderate amplitude.)* See
  [scale invariance](/properties/scale-invariance.md).
- The comparator WCNS-MR uses weights and a global indicator that the authors declare "slightly
  different" from the published scheme, "for the purpose of reducing more oscillations"
  (Eqs. (23)–(24)).
- Positivity is not guaranteed: double Mach reflection and the forward-facing step need the
  first-order fallback.
- Printed slips: the Titarev–Toro final time is $t=5$ in the text and $t=1.8$ in the caption of
  Fig. 6. $\epsilon$ is said to be "in Eq. (12)" where it appears in Eq. (13).

# Citations

- [Chen & Deng (2023)](/sources/chen-2023.md) — Abstract; §1; §2, Eqs. (5)–(24); §3, Eqs. (25)–(36), Theorem 3.1, Fig. 1; §4.1, Fig. 2; §4.2, Table 1, Figs. 3–6; §4.3, Figs. 7–12; §5.
