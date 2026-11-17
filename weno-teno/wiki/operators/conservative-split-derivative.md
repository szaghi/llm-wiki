---
type: Operator
title: "Conservative split central derivative"
description: "An explicit central split derivative ½δ(ab)+½aδb+½bδa of any half-width is exactly a flux difference whose face flux is a double sum of products of two-point arithmetic means (Pirozzoli 2010); the identity gives locally conservative Feiereisen, Blaisdell and Kennedy–Gruber fluxes of arbitrary order, cheaper than differencing the split form directly."
status: established
symbol: "$\\delta^{\\mathrm{sp}}$"
aliases: [Pirozzoli flux, Pirozzoli's conservative split flux, locally conservative split flux, conservative skew-symmetric-like flux, C-FE-SF, C-BL-SF, C-KG-SF, density-weighted split flux]
tags: [kinetic-energy-preserving, finite-difference, numerical-flux, low-dissipation, turbulence]
timestamp: 2026-11-17T08:43:20Z
---

# Conservative split central derivative

A [split convective form](/methods/split-convective-forms.md) discretized with central
differences is not written as a difference of numerical fluxes, and for a long time it was
not known whether it could be. [Pirozzoli (2010)](/sources/pirozzoli-2010.md) shows that it
always can for explicit central differences of any order: the split derivative is exactly a
flux difference, with a face flux built from products of two-point arithmetic means. The
scheme is then [locally conservative](/results/local-conservation-flux-form.md) and fits the
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
framework with no change of the split form.

**Page-local notation.** On a uniform grid of spacing $\Delta x$, the elementary central
difference of half-width $\ell$ and the explicit central first derivative are

$$\delta^{[\ell]}a_i=\frac{a_{i+\ell}-a_{i-\ell}}{\Delta x},\qquad \delta a_i=\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\,\delta^{[\ell]}a_i ,$$

with half-width $L_{\mathrm s}$ and weights $\mathsf a_\ell$ (as on
[flux differencing](/methods/flux-differencing.md)), chosen for maximum order $2L_{\mathrm s}$ or
for dispersion (DRP) properties after Tam & Webb (Eq. (6)). Consistency is
$2\sum_\ell\ell\,\mathsf a_\ell=1$; the maximum-order weights are $\mathsf a_1=\tfrac12$
($L_{\mathrm s}=1$), $\tfrac23,-\tfrac1{12}$ ($L_{\mathrm s}=2$) and $\tfrac34,-\tfrac3{20},\tfrac1{60}$
($L_{\mathrm s}=3$) *(compiler check, not in the source: the paper prints no values)*. The nodal
factors $a$, $b$, $c$ are page-local ($a$ is not the wave speed), $\phi$ is the transported
scalar of [split convective forms](/methods/split-convective-forms.md) ($1$, $v$ or $H$), and
$\{\!\{a\}\!\}_{i,\ell}=\tfrac12(a_i+a_{i+\ell})$ extends the registry's two-point mean to a
pair of nodes $\ell$ apart. $\delta$ carries no stencil subscript here and is not the TENO
cut-off flag $\delta_k$.

The **split central derivative** of a product is (Eq. (5))

$$\delta^{\mathrm{sp}}(ab)_i=\tfrac12\,\delta(ab)_i+\tfrac12\,a_i\,\delta b_i+\tfrac12\,b_i\,\delta a_i ,$$

the discrete counterpart of $\partial_x(ab)=\tfrac12\partial_x(ab)+\tfrac12a\,\partial_xb+\tfrac12b\,\partial_xa$.
$(a,b)=(\rho v,\phi)$ gives the Feiereisen split of $\partial_x(\rho v\phi)$ and
$(a,b)=(\rho\phi,v)$ the Blaisdell split (§2, Eqs. (3)–(5)).

## The identity

For one term of the sum, the split difference is the difference of two pair products
(Eqs. (9)–(10)):

$$\delta^{\mathrm{sp}}_{[\ell]}(ab)_i\equiv\tfrac12\delta^{[\ell]}(ab)_i+\tfrac12a_i\,\delta^{[\ell]}b_i+\tfrac12b_i\,\delta^{[\ell]}a_i=\frac2{\Delta x}\Big(\{\!\{a\}\!\}_{i,\ell}\{\!\{b\}\!\}_{i,\ell}-\{\!\{a\}\!\}_{i-\ell,\ell}\{\!\{b\}\!\}_{i-\ell,\ell}\Big).$$

This is not yet a flux difference, since the two pairs do not share a face. Adding and
subtracting the products of the $\ell-1$ intermediate pairs makes it one (Eq. (11)):

$$\delta^{\mathrm{sp}}_{[\ell]}(ab)_i=\frac1{\Delta x}\Big(\hat f^{[\ell]}_{i+1/2}-\hat f^{[\ell]}_{i-1/2}\Big),\qquad \hat f^{[\ell]}_{i+1/2}=2\sum_{m=0}^{\ell-1}\{\!\{a\}\!\}_{i-m,\ell}\{\!\{b\}\!\}_{i-m,\ell}.$$

The partial flux at $x_{i+1/2}$ sums the $\ell$ pairs of nodes $\ell$ apart that straddle the
face. Reassembling with the weights gives the face flux of $\delta^{\mathrm{sp}}$ (Eqs. (12)–(14)):

$$\delta^{\mathrm{sp}}(ab)_i=\frac{\hat f_{i+1/2}-\hat f_{i-1/2}}{\Delta x},\qquad \hat f_{i+1/2}=\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\,\hat f^{[\ell]}_{i+1/2}=2\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\sum_{m=0}^{\ell-1}\{\!\{a\}\!\}_{i-m,\ell}\{\!\{b\}\!\}_{i-m,\ell}.$$

*(Compiler check, not in the source: expanding both sides gives the identity term by term;
on a periodic 17-point grid with random data it holds to round-off for $\ell\le4$, with
maximum-order and with Liang & Fu's optimized weights.)* For $L_{\mathrm s}=1$,
$\mathsf a_1=\tfrac12$, the flux is $\tfrac14(a_i+a_{i+1})(b_i+b_{i+1})$, against
$\tfrac12(a_ib_i+a_{i+1}b_{i+1})$ for the divergence form $\delta(ab)$ (Eqs. (7)–(8)).
[Ducros et al. (1999)](/sources/ducros-1999.md) derived this second-order case directly in a
finite-volume scheme: the flux of the means, $\{\!\{a\}\!\}\{\!\{b\}\!\}$, makes the update the
half-divergence, half-product-rule split (§3, Eqs. (19)–(21)).

**Three factors.** For the Kennedy–Gruber split with weights
$\alpha_{\mathrm{KG}}=\beta_{\mathrm{KG}}=\tfrac14$ (page-local; the form is on
[split convective forms](/methods/split-convective-forms.md)), the same construction gives
(Eqs. (15)–(17))

$$\hat f_{i+1/2}=2\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell\sum_{m=0}^{\ell-1}\{\!\{\rho\}\!\}_{i-m,\ell}\{\!\{v\}\!\}_{i-m,\ell}\{\!\{\phi\}\!\}_{i-m,\ell},$$

whose difference is
$\tfrac14\delta(\rho v\phi)+\tfrac14\big(v\,\delta(\rho\phi)+\rho\,\delta(v\phi)+\phi\,\delta(\rho v)\big)+\tfrac14\big(\rho v\,\delta\phi+\rho\phi\,\delta v+v\phi\,\delta\rho\big)$
*(compiler check, not in the source: verified numerically for $\ell\le4$)*. Pirozzoli writes
that conservative approximations of the Kennedy–Gruber form "can be recovered only under
particular circumstances", namely $\alpha_{\mathrm{KG}}=\beta_{\mathrm{KG}}=\tfrac14$ (§2,
p. 7182). Because the density is averaged separately from the other two factors, the paper calls
this split and its flux "density-weighted" (p. 7183).

## Instances

With $\phi\in\{1,v,H\}$ for the convective terms $\partial_x(\rho v\phi)$ of the Euler equations
(§2):

- **Feiereisen** (C-FE-SF, Eq. (13)): $(a,b)=(\rho v,\phi)$. Kinetic-energy preserving when
  mass and momentum are split alike ([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
- **Blaisdell** (C-BL-SF, Eq. (14)): $(a,b)=(\rho\phi,v)$. Conservative but not
  kinetic-energy preserving: Pirozzoli (2010, p. 7181) writes that energy consistency is "only
  guaranteed" when continuity and momentum are both split as Feiereisen's form *(compiler check,
  not in the source: see the weight mapping on [split convective forms](/methods/split-convective-forms.md))*. Pirozzoli states that the explicit fluxes of Ducros et al.
  (2000, not ingested) for $L_{\mathrm s}\le3$ are this case with maximum-order weights
  (stated, not shown).
- **Kennedy–Gruber** (C-KG-SF, Eq. (16)): the triple mean. Kinetic-energy preserving
  ("one can easily prove", no proof printed; p. 7183). With $L_{\mathrm s}=1$ the face flux is
  $\{\!\{\rho\}\!\}\{\!\{v\}\!\}\{\!\{\phi\}\!\}$, the cubic split of Jain & Moin on
  [split convective forms](/methods/split-convective-forms.md).

Later uses and restatements in the bundle:

- **Fourth order.** With $L_{\mathrm s}=2$, $\mathsf a_1=\tfrac23$, $\mathsf a_2=-\tfrac1{12}$ the
  Feiereisen flux is
  $\tfrac13(m_i+m_{i+1})(\phi_i+\phi_{i+1})-\tfrac1{24}(m_i+m_{i+2})(\phi_i+\phi_{i+2})-\tfrac1{24}(m_{i-1}+m_{i+1})(\phi_{i-1}+\phi_{i+1})$,
  $m=\rho v$, the fourth-order kinetic-energy-preserving flux that
  [Coppola & Veldman (2023)](/sources/coppola-2023.md) obtain by Richardson extrapolation and
  identify with Pirozzoli's Eq. (13) for these weights (§6.2, after Eq. (78)).
- **Optimized weights.** [Liang & Fu (2024b)](/sources/liang-2024-b.md) use the triple-mean
  flux with four dispersion-optimized weights as the smooth branch of a TENO
  [hybrid](/methods/hybrid-weno.md) (§2.3).
- **Unstructured faces.** [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) use the
  $L_{\mathrm s}=1$ triple product between owner and neighbour cells (§2, Eq. (6)).
- **Curvilinear meshes.** [Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md) applies the same
  double sum to the Kennedy–Gruber split with the volume-weighted contravariant velocity in
  place of $v$, and calls the flux form "entirely equivalent to (but computationally less
  expensive than)" the split derivative form (§2.3, Eqs. (24)–(30);
  [kinetic-energy-preserving split forms in curvilinear coordinates](/methods/curvilinear-kinetic-energy-preserving-split-forms.md)).
- **Two-point-flux reading.** The double sum is the LeFloch–Mercier–Rohde construction of
  [flux differencing](/methods/flux-differencing.md) with $c_\ell=2\mathsf a_\ell$ and a product of
  means as the two-point flux *(compiler check, not in the source: Pirozzoli does not cite
  LeFloch–Mercier–Rohde and considers no nonlinear two-point flux)*.
  [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) state the general construction
  after Ranocha and Pirozzoli (App. A, Eq. (18)).

## Cost

Pirozzoli stores the pair means $\{\!\{\cdot\}\!\}_{i,\ell}$ for all $i$ and $\ell\le L_{\mathrm s}$
line by line, with no significant memory overhead, and then forms the linear combinations
(§2, App. A). Counting sums and products alike, with $1/\Delta x$ and $\tfrac14$ absorbed into
the weights, the floating-point operations per node and derivative $N_{\mathrm{op}}$
(page-local) are:

| scheme | $N_{\mathrm{op}}$ |
|---|---|
| divergence form $\delta(\rho v\phi)$ (D-CONV) | $2+2L_{\mathrm s}$ |
| Feiereisen or Blaisdell split, differenced directly (D-FE-SF, D-BL-SF) | $6+6L_{\mathrm s}$ |
| Kennedy–Gruber split, differenced directly (D-KG-SF) | $20+14L_{\mathrm s}$ |
| two-factor flux $\delta^{\mathrm{sp}}$ (C-FE-SF, C-BL-SF) | $2+\tfrac72L_{\mathrm s}+\tfrac12L_{\mathrm s}^2$ |
| triple-mean flux (C-KG-SF) | $1+\tfrac{11}2L_{\mathrm s}+\tfrac12L_{\mathrm s}^2$ (the text prints $\tfrac92$, see below) |

The conservative two-factor flux is the cheaper for $L_{\mathrm s}\le6$ and the triple-mean flux
for $L_{\mathrm s}\le18$. Ducros et al.'s fluxes, two-factor ones, are plotted at 6, 23 and 48
operations for $L_{\mathrm s}=1,2,3$: the two-factor flux is cheaper for $L_{\mathrm s}=2,3$ (11 and 17)
and equal at $L_{\mathrm s}=1$ (6) (§2, Fig. 1); the paper calls its implementation
"substantially more efficient" than Ducros et al.'s formulation. The C-KG-SF count printed in the text,
$1+\tfrac92L_{\mathrm s}+\tfrac12L_{\mathrm s}^2$, disagrees with the paper's own Fig. 1 (7, 14,
22, 31, 41, 52 for $L_{\mathrm s}=1,\dots,6$) and with its claim that the flux is cheaper
than D-KG-SF only up to $L_{\mathrm s}=18$; $\tfrac{11}2$ satisfies both *(compiler check, not in the source: App. A's rules, three
pair sums and two products per $\ell$, give $1+5L_{\mathrm s}+\tfrac12L_{\mathrm s}(L_{\mathrm s}+1)$; see
the [Source page](/sources/pirozzoli-2010.md))*. Measured CPU times of the inviscid
turbulence runs, normalized by second-order D-CONV, follow the trend: about 1.0 at
$L_{\mathrm s}=1$ rising to about 2.6–2.8 at $L_{\mathrm s}=5$ for the conservative fluxes,
1.8–2.8 for D-FE/BL-SF and 2.9–5.2 for D-KG-SF (App. A, Fig. 10).

## Scope

- **Uniform grids.** On the stretched wall-normal grid of a boundary-layer DNS Pirozzoli
  maps derivatives to a uniform computational coordinate by the chain rule and applies the
  flux form there. The paper states, after Ducros et al. (2000), that a fully conservative split
  discretization "is not possible on a mesh with variable spacing" and that "local
  conservation cannot be proved on non-uniform grids" (§3.2, §4). Coppola & Veldman's
  metric-weighted control volumes reach the opposite conclusion; the disagreement is
  recorded as an open contradiction on
  [local conservation and flux form](/results/local-conservation-flux-form.md).
- **Explicit operators only.** "Apparently, a conservative formulation cannot be arrived
  at if the explicit central difference operators are replaced with compact
  approximations" (§4; no proof). [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) repeats
  the remark (§2.3).
- **Non-dissipative.** The source tests only shock-free flows. It proposes the flux as the
  smooth-flow building block of hybrid shock-capturing schemes, for which local
  conservation makes the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) apply,
  while artificial dissipation must still select the entropy solution (§1, §4); it runs no
  hybrid itself.

# Citations

- [Pirozzoli (2010)](/sources/pirozzoli-2010.md) — §1, §2 Eqs. (5)–(17) pp. 7181–7183, Fig. 1, §3.2, §4, App. A Fig. 10.
- [Ducros et al. (1999)](/sources/ducros-1999.md) — §3 Eqs. (14)–(21).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §6.2 Eqs. (75)–(78) (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — App. A Eqs. (16)–(18) (arXiv v2).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.3 Eqs. (21)–(28).
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §2 Eq. (6).
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §2.3.
- [Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md) — §2.3 Eqs. (24)–(30).
