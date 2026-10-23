---
type: Method
title: "Composition methods and Runge–Kutta–Nyström splittings"
description: "Composition methods raise the order of a basic one-step map by chaining it with weights $\\gamma_j$ (triple and quintuple jump, Suzuki–Yoshida recursion, compositions with the adjoint); specialised splittings exploit structure (RKN, modified potentials, near-integrable, linear systems). The page records the recommended schemes of Blanes, Casas and Murua's catalogue."
status: established
aliases: [triple jump, quintuple jump, Yoshida composition, Suzuki composition, symmetric composition, RKN splitting, force-gradient method, modified-potential splitting, near-integrable splitting, generalized order]
tags: [splitting, geometric-integration, order-conditions, structure-preserving]
timestamp: 2026-10-19T07:44:00Z
---

# Composition methods and Runge–Kutta–Nyström splittings

A composition method builds a high-order map from a basic one-step method $\chi_h$:

$$\psi_h=\chi_{\gamma_sh}\circ\dots\circ\chi_{\gamma_2h}\circ\chi_{\gamma_1h},\qquad \sum_{j=1}^s\gamma_j=1.$$

The basic method is usually time-symmetric and second order (Strang splitting,
Störmer–Verlet, implicit midpoint), and the composition inherits its geometric
properties (symplecticity, time-reversibility, volume preservation) whenever every
$\chi_{\gamma_jh}$ has them ([Blanes et al. 2024](/sources/blanes-2024.md), §2.1). It is
the route to high order for [operator splitting](/methods/operator-splitting.md), where it
needs no knowledge of the parts beyond the basic map. The order conditions are on
[splitting order conditions](/results/splitting-order-conditions.md); every real
composition of order $\ge3$ has a negative weight
([negative-coefficient barrier](/results/negative-coefficient-barrier.md)).

## Adjoint and symmetric maps

The adjoint of $\psi_h$ is $\psi_h^*=\psi_{-h}^{-1}$; $\psi_h$ is time-symmetric if
$\psi_h=\psi_h^*$. Both $\psi^*_{h/2}\circ\psi_{h/2}$ and $\psi_{h/2}\circ\psi^*_{h/2}$ are
symmetric of order $\ge2$; explicit and implicit Euler are mutual adjoints, the
trapezoidal rule is (implicit Euler)∘(explicit Euler) with half steps and the implicit
midpoint rule the reverse, and the two are conjugate (Blanes et al. 2024, §1.3, Eq. 1.17).
A map is time-symmetric iff the logarithm of its Lie transform is odd in $h$, so
**symmetric methods have even order** (§2.1.1, statement (2)).

## Compositions of a symmetric second-order map

With $\chi_h$ symmetric of order 2, the composition has order $\ge3$ iff
$\sum_j\gamma_j=1$ and $\sum_j\gamma_j^3=0$; the smallest $s$ with real solutions is 3
(Blanes et al. 2024, §2.1.1, Eqs. 2.1–2.2). Classical families (§2.1.1, §8.1):

- **Triple jump** (Creutz & Gocksch 1989, Suzuki 1990, Yoshida 1990): from a symmetric
  method $\chi^{[2k-2]}$ of order $2k-2$,
  $\chi^{[2k]}_h=\chi^{[2k-2]}_{\gamma_1h}\circ\chi^{[2k-2]}_{(1-2\gamma_1)h}\circ\chi^{[2k-2]}_{\gamma_1h}$,
  $\gamma_1=1/(2-2^{1/(2k-1)})$ (page-local superscript $[2k]$ = order). For $k=2$,
  $\gamma_1=1/(2-2^{1/3})\approx1.35$ and the middle weight is negative. It reaches any even
  order, at the cost of large coefficients of both signs.
- **Quintuple jump** (Suzuki): five maps with $\gamma_1=1/(4-4^{1/(2k-1)})$; smaller
  coefficients; used in quantum simulation (Eq. 2.5, Eq. 9.38).
- **General recursion** (Eq. 8.2): $(\chi_{\gamma_1h})^{q}\circ\chi_{(1-2q\gamma_1)h}\circ(\chi_{\gamma_1h})^{q}$
  with $\gamma_1=1/(2q-(2q)^{1/(2k+1)})$ (page-local integer $q\ge1$; here the basic map has
  order $2k$ and the result order $2k+2$, so $k$ is shifted by one against the triple jump
  above); $q=1$ is Yoshida's,
  $q=2$ Suzuki's.
- **Optimised symmetric compositions** (labelled MCL95, KR97, SS05 in the catalogue)
  use more stages than the recursions to minimise the error coefficients.

## Compositions of a first-order map and its adjoint

With a first-order $\chi_h$ (e.g. Lie–Trotter), compositions of $\chi$ alone need
$\sum\gamma_j=1$, $\sum\gamma_j^2=0$ for order 2, which has no real solution (Blanes et al.
2024, Eq. 2.14). One therefore alternates the map and its adjoint (page-local weights
$\alpha_j$):

$$\psi_h=\chi_{\alpha_{2s}h}\circ\chi^*_{\alpha_{2s-1}h}\circ\dots\circ\chi_{\alpha_2h}\circ\chi^*_{\alpha_1h},$$

of order 2 iff $\sum_j\alpha_j=1$ and $\sum_j(\alpha_{2j}^2-\alpha_{2j-1}^2)=0$ (Eq. 2.15).
With Lie–Trotter $\chi_h=\varphi^{[1]}_h\circ\varphi^{[2]}_h$ (so $\chi^*_h=\varphi^{[2]}_h\circ\varphi^{[1]}_h$) this **is** a splitting method
$\psi_h=\varphi^{[1]}_{a_{s+1}h}\circ\varphi^{[2]}_{b_sh}\circ\dots\circ\varphi^{[2]}_{b_1h}\circ\varphi^{[1]}_{a_1h}$ (Eq. 2.17) with
$a_1=\alpha_1$, $a_{j+1}=\alpha_{2j}+\alpha_{2j+1}$, $b_j=\alpha_{2j-1}+\alpha_{2j}$ (Eq. 2.18);
conversely every splitting with $\sum a_j=\sum b_j$ is such a composition (as recalled from
McLachlan 1995). Splitting and composition are thus two parametrisations of one class.
**Palindromic** splittings ($a_{s+2-j}=a_j$, $b_{s+1-j}=b_j$) are time-symmetric (§2.1.2).
Compositions with the adjoint also apply to non-splitting basic methods, e.g. explicit
Euler with implicit Euler as adjoint (Appendix A, case 2).

## Runge–Kutta–Nyström splittings

For $y''=g(y)$ written as a first-order system with $f^{[1]}=(0,g(y))$ (kick) and
$f^{[2]}=(v,0)$ (drift), the Lie derivatives satisfy the extra identity that the triple
bracket of the kick with itself and the drift vanishes, so many order conditions drop out
(Blanes et al. 2024, §3.1, Eq. 3.2). The counts $d_n$ of independent conditions at order
$n=1,\dots,11$ are $2,1,2,2,4,5,10,14,25,39,69$, against $2,1,2,3,6,9,18,30,56,99,186$
for general splittings (Table 2.1). The same reduction holds when the kinetic energy is
quadratic in the momenta, and for the Schrödinger equation split into potential and
kinetic parts (§3.1). **Labelling warning** (§8.3): in all published RKN splittings the
first flow in the bracket identity is the potential (kick, "B") and the second the kinetic
(drift, "A"); families are labelled AB, BA, ABA, BAB, with S (symmetric) or N
(non-symmetric).

## Modified potentials (force-gradient methods)

Including the flow of a double commutator — in the RKN case the "modified potential"
$2a_2V(q)+d_2h^2(\nabla V)^\top M^{-1}\nabla V$ (page-local $V$ potential, $d_2$
coefficient), explicitly computable — evades the negative-coefficient barrier. The
fourth-order scheme of Koseleff (1993) and Chin (1997),
$\varphi^{[1]}_{a_1h}\circ\varphi^{[2]}_{b_1h}\circ\varphi^{[1]}_{a_2h}\circ(\text{commutator flow, }d_2h^3)\circ\varphi^{[1]}_{a_2h}\circ\varphi^{[2]}_{b_1h}\circ\varphi^{[1]}_{a_1h}$,
has the unique coefficients, with all splitting coefficients positive, $a_1=\tfrac16$, $b_1=\tfrac12$, $a_2=\tfrac13$,
$d_2=-\tfrac1{72}$ (Blanes et al. 2024, §3.2, Eqs. 3.4–3.7). Sixth order with positive
coefficients is impossible in general (Chin 2005), but a processed sixth-order method with
positive $a_j,b_j$ exists for cubic potentials (Blanes et al. 2023, as recalled, §3.2).

## Near-integrable systems and generalized order

For $y'=f^{[1]}(y)+\varepsilon f^{[2]}(y)$ with $f^{[1]}$ exactly integrable (Kepler
motion in planetary problems), the error terms at each $h^k$ split into one of size
$\varepsilon h^k$, $\tfrac12(k-1)$ of size $\varepsilon^2h^k$ and $\tfrac16(k-1)(k-2)$ of
size $\varepsilon^3h^k$. A method has **generalized order** $(r_1,r_2,\dots,r_m)$ if its
local error is $O(\varepsilon h^{r_1+1}+\varepsilon^2h^{r_2+1}+\dots+\varepsilon^mh^{r_m+1})$;
Strang is $(2,2)$ (Blanes et al. 2024, §3.3, as recalled from McLachlan 1995). The
palindromic schemes and their conditions (Table 3.1, in the multi-index notation of
[splitting order conditions](/results/splitting-order-conditions.md)):

| Generalized order | Lyndon multi-indices to annul |
|---|---|
| $(2n,2)$ | (3), (5), …, $(2n-1)$ |
| (8,4) | (3), (5), (7), (1,2) |
| (10,4) | (3), (5), (7), (9), (1,2) |
| (8,6,4) | (3), (5), (7), (1,2), (1,4), (2,3) |
| (10,6,4) | (3), (5), (7), (9), (1,2), (1,4), (2,3) |

On the outer Solar System over $2\times10^5$ days, splittings of generalized order (2,2),
(8,2) and (10,6,4) beat extrapolation of orders 2–12 and MATLAB ode23/ode45/ode113 at all
accuracies, in energy and in position error per force evaluation (§9.4, Fig. 9.1); in the
Appendix A matrix tests with small $\varepsilon$ the near-integrable methods dominate all
others.

## Linear systems

For $iu'=Hu$ with real symmetric $H$, writing $u=q+ip$ gives $q'=Hp$, $p'=-Hq$ with
nilpotent parts; one condition raises the order from $2k-1$ to $2k$ and two from $2k$ to
$2k+1$, so orders $p=2,4,\dots,12$ are reached with $s=p$ exponentials, against at least
15 and 31 for orders 8 and 10 with general splittings (Blanes et al. 2024, §3.4, as
recalled from Gray & Manolopoulos 1996 and Blanes et al. 2008). The schemes are not
unitary but conjugate to unitary maps for small $h$. A splitting algorithm of this kind
for $e^{-ihH}v$ is 1.4–2 times faster than Chebyshev at equal accuracy (§6.3).

## Catalogue and recommendations

Blanes et al. (2024, §8) catalogue more than 80 published methods and box the recommended
ones (coefficients at the authors' web site). Methods are labelled "$s$-AUTHORyy" by stage
count; "P:" marks processed kernels (see
[processing](/methods/processing-and-effective-order.md)). Optimisation targets are the
2-norm $E_{p+1}$ of the order-$(p+1)$ error coefficients in a Lyndon basis, and
$\sum_j(\lvert a_j\rvert+\lvert b_j\rvert)$ or $\max_j(\lvert a_j\rvert,\lvert b_j\rvert)$.

| Class (table) | Order | Boxed method |
|---|---|---|
| Symmetric compositions of a 2nd-order symmetric map (8.1) | 4 / 6 / 8 / 10 | 5-SUZ90 or 5-MCL95 / 13-SS05 / 21-SS05 / 35-SS05 |
| — processed (8.1) | 6 / 8 / 10 | P:11-BCM06 / P:13-BCM06 / P:23-BCM06 |
| Two-part splitting or first-order-plus-adjoint compositions (8.2) | 2 / 4 / 6 | 2-MCL95 / 6-BM02 / 10-BM02 |
| — processed (8.2) | 4 / 6 | P:4-BCR99 / P:6-BCM06, P:9-BCM06 |
| RKN (8.3) | 4 / 5 / 6 / 8 | 6S-BM02 / 6N_AB-MA92 / 14S_ABA-BM02 / 19-BCE22 |
| RKN with modified potentials (8.4) | 4 / 6 | 4S (CHI06/OMF02) / 5S-OMF02 |
| Near-integrable (8.5) | $(2n,2)$ / $(8,4)$ / $(8,6,4)$, $(10,6,4)$ | 1- and $n$-stage / 5(8,4) / 7(8,6,4), 8(10,6,4) |

A non-symmetric eighth-order composition needs at least 16 stages (16 equations), against
15 for a symmetric one (8 equations) (§8.1). The Appendix A comparison on random
$50\times50$ matrix exponentials concludes that **no single method is best**.

## Further constructions

- **Extrapolation:** Gragg's (GBS) method is Strang applied to a doubled system, hence its
  even error expansion; symmetric splittings can be extrapolated likewise. Multi-product
  expansions $\sum_ic_i(S_{h/k_i})^{k_i}$ with $c_i=\prod_{j\ne i}k_i^2/(k_i^2-k_j^2)$
  (page-local $k_i$ integers, $S_h$ a symmetric second-order map) reach order $2m$ with
  $m$ terms and keep the geometric properties of the basic method up to order $4n+1$ when
  it has order $2n$; some $c_i<0$ is unavoidable when the inner compositions have positive
  weights (Blanes et al. 2024, §9.1, as recalled from Blanes et al. 1999, Chan & Murua 2000,
  Sheng 1989).
- **Hamiltonian Monte Carlo:** the 3-stage palindromic integrator with $a_1=0.11888010966548$,
  $b_1=0.29619504261126$, $a_2=\tfrac12-a_1$, $b_2=1-2b_1$ minimises the energy error at
  large $h$ rather than as $h\to0$ (§9.6).
- **Langevin dynamics:** BAOAB (kick, drift, exact Ornstein–Uhlenbeck, drift, kick) is
  superior within its family (§9, as recalled from Leimkuhler & Matthews 2013).
- **Crouch–Grossman Lie-group methods** of order 3 and 4 follow from Strang on a doubled
  system with 3 and 7 exponentials (§9).

## Qualifications

- The recommendations differ between two places of the version read: Appendix A recommends
  non-processed symmetric compositions with $s=5,13,19,35$ for orders 4–10 and processed
  kernels with $s=13,19,23$ for orders 6–10, while Table 8.1 boxes 21 (not 19) stages at
  order 8 and P:11, P:13 (not 13, 19) for the processed orders 6 and 8. The table above
  follows Table 8.1. This is an internal inconsistency of the source (arXiv v3), not a
  contradiction between sources.
- Blanes et al. label WHT96 "P:1(17,2)" in Table 8.5 but describe it as "(k,2) with
  $k=16$" in the text (printed slip in one of the two places).
- Koseleff's 1993 fourth-order modified-potential scheme carries a misprinted coefficient,
  corrected by Chin (1997) (§8.3, as recalled).

# Citations

- [Blanes et al. (2024)](/sources/blanes-2024.md) — §1.3 (adjoints), §2.1 (compositions, Eqs. 2.1–2.5, 2.14–2.18), §3.1–3.4 (RKN, modified potentials, near-integrable, linear systems; Tables 2.1, 3.1), §8 (catalogue, Tables 8.1–8.5, Eq. 8.2), §9.1–9.6 (extrapolation, multi-product expansions, Crouch–Grossman, HMC, Langevin), Appendix A.
