---
type: Definition
title: "Stiffened-gas equation of state"
description: "The stiffened-gas law, an ideal gas shifted by a constant stiffening pressure, which models liquids in compressible multiphase solvers: its pressure, energy and temperature forms, sound speed, mixture rules, entropy, the convexity of its admissible set and the parameter values the sources use."
status: established
aliases: [stiffened gas EOS, stiffened equation of state, Tait EOS (as named by Zheng et al.), SG EOS]
tags: [multiphase, interface-capturing, positivity, entropy-stable]
timestamp: 2026-10-22T12:00:00Z
---

# Stiffened-gas equation of state

The stiffened-gas equation of state closes the Euler equations for a
fluid that resists compression much more than an ideal gas, chiefly
water. With $\gamma>1$ and a constant $p_\infty\ge0$ (page-local symbol,
the "stiffening pressure"),

$$
p=(\gamma-1)\rho e-\gamma p_\infty
\qquad\Longleftrightarrow\qquad
\rho e=\frac{p+\gamma p_\infty}{\gamma-1},
\qquad
c^2=\frac{\gamma\,(p+p_\infty)}{\rho},
$$

so that $E=\rho e+\tfrac12\rho\lvert v\rvert^2$ as in §5 of the
registry. With $p_\infty=0$ it is the ideal gas. All five sources that
use it write it in one of these forms
([Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §3, Eqs. 6–7;
[Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §2, Eq. 6;
[Wong et al. (2021)](/sources/wong-2021.md) §2, Eq. 6;
[Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) §2;
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) §1, Eq. 1.2).
Because only $p+p_\infty$ enters the sound speed, the pressure itself
may be negative: [Wong et al. (2021)](/sources/wong-2021.md) §6.4 start
a Sedov test in water at $p=-3\times10^7$ Pa, an admissible state since
$p+p_\infty>0$.

## Forms and conventions in the sources

- **Pressure law (energy form).** Bryngelson et al. and Tsoutsanis et
  al. write $p_k=(\gamma_k-1)\rho_ke_k-\gamma_kp_{\infty,k}$ per phase
  $k$; Wong et al. write $\frac{p_k}{\gamma_k-1}+\frac{\gamma_kp_{\infty,k}}{\gamma_k-1}=\rho_ke_k$;
  Zheng et al. write the total energy
  $E=\tfrac12\rho v^2+\frac{p+\gamma p_\infty}{\gamma-1}$ and call this
  relation the "Tait EOS". All are the same law.
- **Temperature form.** Li et al. close each species with
  $\rho_ke_k=C_{v,k}\rho_kT+p_{\infty,k}$ and, in thermal equilibrium,
  obtain $p=\sum_k\big(\rho_kR_kT-p_{\infty,k}\big)$ with
  $R_k=C_{v,k}(\gamma_k-1)$ (Eq. 1.2; page-local $T$, $C_{v,k}$, $R_k$).
  With $p_\infty=\sum_kp_{\infty,k}$ and the mixture ratio
  $\gamma=\sum_k\gamma_kC_{v,k}\rho_k/\sum_kC_{v,k}\rho_k$, this is the
  energy form $\rho e=(p+\gamma p_\infty)/(\gamma-1)$ for the mixture
  (Li et al. print it as $\frac{p+p_\infty}{\gamma-1}+p_\infty=\rho e$,
  the same expression). The equivalence needs
  $\gamma\sum_kC_{v,k}\rho_k=\sum_k\gamma_kC_{v,k}\rho_k$, which is the
  definition of the mixture $\gamma$ *(compiler check, not in the
  sources)*. The sound speed is $c^2=R\gamma T=\gamma(p+p_\infty)/\rho$
  for one species (§3.4).
- **Parameters for liquids.** Bryngelson et al. state that the liquid
  constants are fitted to shock-Hugoniot data (§3).

## Mixture rules

In the five-equation (single-pressure, single-velocity) model the
mixture of two stiffened gases is again a stiffened gas whose
constants depend only on the volume fractions $\phi_k$ (page-local,
$\phi_1+\phi_2=1$):

$$
\frac{1}{\gamma-1}=\sum_k\frac{\phi_k}{\gamma_k-1},\qquad
\frac{\gamma\,p_\infty}{\gamma-1}=\sum_k\frac{\phi_k\gamma_kp_{\infty,k}}{\gamma_k-1},\qquad
\rho e=\sum_k\phi_k\rho_ke_k
$$

(Wong et al. Eqs. 7–9; Tsoutsanis et al. Eqs. 7–11; the same rules
are printed by Zheng et al. §4, who use them only to plot mixed cells,
not to evolve the solution). The mixture sound speed is then
$\rho c^2=\gamma(p+p_\infty)=\gamma(\gamma-1)(\rho e-p_\infty)$
(Wong et al. Eq. 11). Bryngelson et al. instead use, for Kapila's
five-equation model, the Wood speed of sound
$\frac1{\rho c^2}=\sum_k\frac{\phi_k}{\rho_kc_k^2}$ with each $c_k$ from
the phase law above (Eq. 9); see
[five-equation model](/definitions/five-equation-model.md) for the
difference. In the multicomponent model with thermal equilibrium the
mixture follows from the temperature form instead (Li et al.; see
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).

## Admissible states and convexity

For the five-equation model, Wong et al. define the admissible set

$$
G=\{\,0\le\phi_1\le1,\ \phi_1\rho_1\ge0,\ \phi_2\rho_2\ge0,\ \rho e-p_\infty>0\,\},
$$

which is equivalent to $\rho c^2>0$ because $\gamma>1$ whenever
$0\le\phi_1\le1$ (Eqs. 10, 12). Their Lemma 1 decides when $G$ is convex,
the property every [bound-preserving](/properties/bound-preservation.md)
limiter needs: if one phase is an ideal gas ($p_{\infty,2}=0$), then
$\rho e-p_\infty$ is concave in the conserved variables
$(\phi_1\rho_1,\phi_2\rho_2,\rho v,E,\phi_1)$ if and only if the
stiffened phase has the larger ratio of specific heats,
$\gamma_1\ge\gamma_2$; "if $\gamma_2>\gamma_1$, the function cannot be
concave" (Lemma 1, Eqs. 13–14). Theorem 1 then gives convexity of $G$
by Jensen's inequality. The authors call the condition "very mild":
water has $\gamma$ between 4 and 7 in the literature (with one fit at
1.932), ethanol 2.1, mercury 8.2, against 1.4 for air and 1.67 for
monatomic gases (§2). The lemma assumes that one phase has
$p_\infty=0$; pairs of two stiffened phases lie outside it.

## Entropy

For one stiffened-gas species, Li et al. use the specific entropy
$S=C_v\ln T-R\ln\rho$ and the convex entropy $\eta=-\rho S$ with flux
$F_\eta=\eta v$ (§3.3.1, Eq. 3.13). The entropy flux potential (§6 of
the registry) is $\psi=\big(R\rho-p_\infty/T\big)v$, so the stiffening
pressure enters the potential through $p_\infty/T$ (Eq. 3.14). For
mixtures the entropy is the mass-weighted sum of species entropies
(Eqs. 3.16–3.17). With these, Li et al. derive explicit
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md)
built from [logarithmic means](/operators/logarithmic-mean.md) of the
partial densities and of $1/T$, and entropy-scaled eigenvectors with the
sound speed $c^2=\gamma(p+p_\infty)/\rho$ (§3.3–3.4).

## Parameter values used

| Source and test | $\gamma$ | $p_\infty$ | Units |
|---|---|---|---|
| Wong et al., all tests (water) | 6.12 | $3.43\times10^8$ Pa | SI |
| Tsoutsanis et al. §4.5, water column | 6.12 | $3.43\times10^8$ | SI |
| Tsoutsanis et al. §4.4, bubble collapse | 4.4 | $6\times10^8$ | SI |
| Tsoutsanis et al. §4.3, gas–liquid Riemann problem | 5.5 | 1.505 | non-dimensional |
| Zheng et al., water | 7.15 | $3.309\times10^8$ Pa | SI; non-dimensional 3309 |
| Zheng et al. Ex. 5 | 5.5 | 1.505 | non-dimensional |
| Zheng et al. Ex. 2, 9 ("gas" side of a pure interface) | 4 | 1 | non-dimensional |
| Li et al. Ex. 5.2, single-fluid shock tube | 3 | 1 | non-dimensional |
| Li et al. Ex. 5.9, 5.11, surrounding medium | 3 | 100 | non-dimensional |

The fits differ from test to test within one source (Tsoutsanis et al.
use three water fits in three tests without comment): the sources take
the constants with each benchmark setup, not from one water model.

## Qualifications

- The name is not uniform: Zheng et al. call the stiffened-gas energy
  relation the "Tait EOS"; the other sources call it stiffened gas.
- The law has no temperature in its energy form; the temperature form
  of Li et al. adds a constant heat capacity per species, which is what
  makes a thermal-equilibrium mixture and a physical entropy available.
- Wong et al.'s concavity result covers a stiffened phase paired with an
  ideal gas; it says nothing about the temperature-based multicomponent
  closure of Li et al.

# Citations

- [Wong et al. (2021)](/sources/wong-2021.md) — §2, Eqs. (6)–(14), Lemma 1, Theorem 1; §6, Table 1; §6.4 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §2, Eqs. (6)–(11); §4.3–4.5.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §3, Eqs. (6)–(9) (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2; §4, Ex. 2, 5–7, 9, 11.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §1, Eq. (1.2); §3.3–3.4, Eqs. (3.13)–(3.17); Ex. 5.2, 5.9 (arXiv v1).
