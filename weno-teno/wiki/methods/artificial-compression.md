---
type: Method
title: "Artificial compression"
description: "Artificial compression adds a limited anti-diffusive correction in linearly degenerate fields so that contact discontinuities stop spreading; the page gives Harten's switch in the modified-flux TVD scheme, Yang's compression in the point-value form Jiang and Shu attach to WENO, their measured costs and effects, and the alternatives the reviews list."
status: established
aliases: [artificial compression method, ACM, Harten's artificial compression, Yang's artificial compression, contact sharpening, WENO-A]
tags: [limiting, low-dissipation, interface-capturing, weno, characteristic]
timestamp: 2026-10-30T08:09:00Z
---

# Artificial compression

Contact discontinuities are harder to capture sharply than shocks: in a linearly
degenerate field the characteristics run parallel to the discontinuity instead of into
it, so nothing in the exact solution steepens a smeared contact
([Shu (2009a)](/sources/shu-2009.md), §3.5.7, Fig. 3.3). **Artificial compression**
adds, in those fields only, a limited correction that makes the effective characteristic
field slightly convergent, so that the numerical contact keeps a fixed width.
[Harten (1983a)](/sources/harten-1983.md) builds it into the limited correction of the author's
[TVD scheme](/methods/harten-tvd-scheme.md); [Jiang & Shu (1996)](/sources/jiang-1996.md)
attach Yang's version to finite-difference [WENO](/methods/weno-js-reconstruction.md)
fluxes. Both apply it in the contact field of the Euler equations through a
[characteristic decomposition](/methods/characteristic-decomposition.md).

## Why contacts spread

Harten (1983a) (§6, citing the author's earlier work) states that a first-order scheme spreads a
contact over a width growing like $\sqrt n$ after $n$ time steps and a $p$-th order scheme
like $n^{1/(p+1)}$; the second-order TVD scheme is therefore expected to spread contacts like
$n^{1/3}$.
[Liu et al. (1994)](/sources/liu-1994.md) (p. 208, Figs. 1–3) observe that their WENO
schemes smear "linear discontinuities … a bit" in square-wave, semi-ellipse and Gaussian
advection and expect to fix it with Harten's subcell resolution or Yang's artificial
compression.

## Harten's switch in the modified-flux scheme

In the characteristic form of Harten's scheme, the limited correction $\mathsf g^{(l)}_i$ of
field $l$ (a minmod of the unlimited edge corrections $\tilde{\mathsf g}^{(l)}_{i\pm1/2}$, see
[Harten's TVD scheme](/methods/harten-tvd-scheme.md)) is multiplied by $1+\theta_{\mathrm{AC},i}$
(§6, Eqs. (6.1a,b)):

$$\mathsf g^{(l)}_i\ \to\ \big(1+\theta^{(l)}_{\mathrm{AC},i}\big)\,\mathsf g^{(l)}_i,\qquad
\theta^{(l)}_{\mathrm{AC},i}=\frac{\big\lvert\delta^{(l)}_{i+1/2}-\delta^{(l)}_{i-1/2}\big\rvert}{\big\lvert\delta^{(l)}_{i+1/2}\big\rvert+\big\lvert\delta^{(l)}_{i-1/2}\big\rvert},$$

with $\delta^{(l)}_{i+1/2}=L_l(u_{i+1}-u_i)$ the wave strengths (page-local $\theta_{\mathrm{AC}}$,
not the Zhang–Shu factor $\theta$ of the registry; $\delta^{(l)}$ as on the scheme's page).
As shown in the earlier paper Harten cites, $0\le\theta_{\mathrm{AC}}\le1$,
$\theta_{\mathrm{AC}}=O(\Delta x)$ in smooth regions and $O(1)$ at discontinuities (Eq. (6.2)), so
the change alters the flux by $O(\Delta x^2)$ in smooth flow and keeps the second order.
With the switch the bound on the added Courant number doubles,
$\lvert\delta\nu\rvert\le\lvert Q(\nu)-\nu^2\rvert$; the CFL bound is unchanged for
$Q=\lvert x\rvert$ and for the smoothed $Q$ with $\varepsilon_{\mathrm H}<1/3$, and tightens to $3/4$
for $Q=x^2+\tfrac14$ (Eqs. (6.3a,b), stated without derivation).

For the Euler equations Harten applies the switch in the contact field only,
$\theta^{(1)}_{\mathrm{AC}}=\theta^{(3)}_{\mathrm{AC}}\equiv0$ (§7); using it in the genuinely
nonlinear fields to sharpen shocks is mentioned as an option (§6). The comparison scheme of
the paper's §8, Harten's earlier hybrid scheme, carries the same switch in its dissipation
coefficient, $\big[(\nu^{(l)})^2+\tfrac14\theta^{(l)}_{\mathrm{AC}}\big]\delta^{(l)}$, "for all $k$"
(Eq. (8.9)).

*(compiler check, not in the sources: for scalar data, with $\delta^{(l)}_{i\pm1/2}$ replaced by
first differences and a regularization $\epsilon$ added, $1-\theta_{\mathrm{AC},i}$ is the
"Harten" detector $1-\lvert f_{i-1}-2f_i+f_{i+1}\rvert/(\lvert f_{i-1}-f_i\rvert+\lvert f_i-f_{i+1}\rvert+\epsilon)$
recorded on [hybrid central-WENO schemes](/methods/hybrid-weno.md); Harten (1983a) prints no
threshold and no $\epsilon$.)*

## Yang's compression for WENO fluxes

Jiang & Shu (1996) (§5, Eqs. (5.1)–(5.4)) write Yang's artificial compression in the
point-value (flux) form of finite-difference ENO and WENO. For $f=au$, $a>0$, the
numerical flux $\hat f_{i+1/2}$ is corrected to

$$\hat f^{\mathrm A}_{i+1/2}=\hat f_{i+1/2}+\mathrm{minmod}\Big[\frac{\alpha_{\mathrm Y,i}}{2}\,\mathrm{minmod}\big(\hat f^{\mathrm R}_{i+1/2}-\hat f_{i+1/2},\ \hat f^{\mathrm R}_{i-1/2}-\hat f_{i-1/2}\big),\ f_{i+1}-\hat f_{i+1/2},\ \hat f^{\mathrm R}_{i-1/2}-f_{i-1}\Big],$$

$$\alpha_{\mathrm Y,i}=\alpha_{\mathrm Y}\Big(\frac{\lvert f_{i+1}-2f_i+f_{i-1}\rvert}{\lvert f_{i+1}-f_i\rvert+\lvert f_i-f_{i-1}\rvert}\Big)^2,\qquad\alpha_{\mathrm Y}=33,$$

where $\hat f^{\mathrm R}$ is the flux reconstructed "pretending $a<0$", minmod returns the
argument of smallest modulus when all signs agree and zero otherwise, and
$\alpha_{\mathrm Y}=33$ is the value "suggested by Yang" (page-local $\hat f^{\mathrm R}$,
$\alpha_{\mathrm Y,i}$, $\alpha_{\mathrm Y}$; not the WENO weights $\alpha_k$). The squared ratio is
the scalar analogue of Harten's switch, small in smooth regions and of order one at a jump.
For the Euler equations it is applied in the contact fields only, and schemes carrying it
take the suffix "-A".

**Effect** (Jiang & Shu 1996, §8):

- on [composite-wave advection](/benchmarks/jiang-shu-composite-advection.md) (200 points,
  $t=8$) WENO-Roe-5-A is the best of the schemes tested on all four waves, run at CFL 0.2;
  at CFL 0.4 the result is similar with $\alpha_{\mathrm Y}=40$ (§8.1 Ex. 1, Fig. 2);
- on the [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md) WENO-LF-5-A gives the
  sharpest contacts (§8.2 Ex. 1, Fig. 4), and a -A variant runs on the
  [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md) (§8.2 Ex. 3).

**Cost** (§7, Table 7): the compression raises the operation count by about 40 % (1D) and
65 % (2D) with the Roe building block and by 65 % (1D) and 100 % (2D) with the Lax–Friedrichs
building block. The authors propose building the compression into the weights as future
work (§9).

## Alternatives

Shu (2009a) (§3.5.7) lists three remedies for contacts, each with references: artificial
compression, subcell resolution and antidiffusive flux corrections. In the later
literature of the bundle the same goal is pursued by sharpening reconstructions such as
[THINC](/methods/thinc-reconstruction.md) and by
[boundary variation diminishing](/definitions/boundary-variation-diminishing.md) selection,
see [numerical dissipation](/definitions/numerical-dissipation.md).

## Qualifications

- Harten's statement that compression keeps contacts from spreading is argued (§6), not
  demonstrated in a contact-only test; the paper's Euler figures show sharp contacts with the
  switch on (§8).
- Jiang & Shu's evidence is visual (figures); no error norms isolate the effect of the
  compression.
- Harten's switch is printed with a garbled denominator index in Eq. (6.1b) of the version
  read (NYU report, March 1982); the form above reads the index as $i-1/2$.

# Citations

- [Harten (1983a)](/sources/harten-1983.md) — §6 (Eqs. (6.1)–(6.3)), §7, §8 (Eq. (8.9)) (NYU report DOE/ER/03077-175, March 1982).
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §5 (Eqs. (5.1)–(5.4)), §7 (Table 7), §8.1 Ex. 1 (Fig. 2), §8.2 Exs. 1, 3 (Fig. 4), §9 (author preprint).
- [Shu (2009a)](/sources/shu-2009.md) — §3.5.7 (Fig. 3.3): contacts and their remedies.
- [Liu et al. (1994)](/sources/liu-1994.md) — p. 208 (Figs. 1–3): smeared linear discontinuities, compression as the expected fix.
