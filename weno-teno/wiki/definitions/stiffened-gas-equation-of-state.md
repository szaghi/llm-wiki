---
type: Definition
title: "Stiffened-gas equation of state"
description: "The stiffened-gas law, an ideal gas shifted by a constant stiffening pressure, which models liquids in compressible multiphase solvers: its pressure, energy and temperature forms, its pressure–temperature form with entropy and Gibbs function, sound speed, mixture rules, the convexity of its admissible set, its relation to the Tait law and the parameter values the sources use."
status: established
aliases: [stiffened gas EOS, stiffened equation of state, Tait EOS (as named by Zheng et al.), SG EOS]
tags: [multiphase, interface-capturing, positivity, entropy-stable]
timestamp: 2026-10-24T05:59:00Z
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
registry. With $p_\infty=0$ it is the ideal gas. The sources that use
it write it in one of these forms, possibly with an additive energy
constant (below)
([Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §3, Eqs. 6–7;
[Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §2, Eq. 6;
[Wong et al. (2021)](/sources/wong-2021.md) §2, Eq. 6;
[Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) §2;
[Li, Duan & Tang (2022c)](/sources/li-2022-c.md) §1, Eq. 1.2;
[Bai & Li (2022)](/sources/bai-2022.md) §2, Eq. 2;
[Nguyen et al. (2022)](/sources/nguyen-2022.md) §2.2, Eqs. 8–11;
[Jain & Moin (2022)](/sources/jain-2022.md) §2, Eqs. 5–9;
[Huang & Johnsen (2023)](/sources/huang-2023.md) §2.9, Eqs. 22–24;
[Long, Cai & Pan (2023)](/sources/long-2023.md) §2.2, Eq. 3;
[Paula et al. (2023)](/sources/paula-2023.md) §2.1, Eq. 3;
[Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) Appendix B;
[Wakimura et al. (2024)](/sources/wakimura-2024.md) §2.2, Eq. 4;
[Zhang et al. (2024a)](/sources/zhang-2024.md) §2.2, Eqs. 9–10;
[Huang et al. (2025b)](/sources/huang-2025-b.md) §2, Eqs. 5–6;
[Wilfong et al. (2026)](/sources/wilfong-2026.md) §2.2, after Menikoff & Plohr).
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
- **Temperature form.** Li et al. (2022c) close each species with
  $\rho_ke_k=C_{v,k}\rho_kT+p_{\infty,k}$ and, in thermal equilibrium,
  obtain $p=\sum_k\big(\rho_kR_kT-p_{\infty,k}\big)$ with
  $R_k=C_{v,k}(\gamma_k-1)$ (Eq. 1.2; page-local $T$, $C_{v,k}$, $R_k$).
  With $p_\infty=\sum_kp_{\infty,k}$ and the mixture ratio
  $\gamma=\sum_k\gamma_kC_{v,k}\rho_k/\sum_kC_{v,k}\rho_k$, this is the
  energy form $\rho e=(p+\gamma p_\infty)/(\gamma-1)$ for the mixture
  (Li et al. (2022c) print it as $\frac{p+p_\infty}{\gamma-1}+p_\infty=\rho e$,
  the same expression). The equivalence needs
  $\gamma\sum_kC_{v,k}\rho_k=\sum_k\gamma_kC_{v,k}\rho_k$, which is the
  definition of the mixture $\gamma$ *(compiler check, not in the
  sources)*. The sound speed is $c^2=R\gamma T=\gamma(p+p_\infty)/\rho$
  for one species (§3.4). Bai & Li write the same law with the heat
  capacity at constant pressure,
  $p=\frac{\gamma-1}{\gamma}C_p\rho T-p_\infty$ and
  $e=\frac{C_p}{\gamma}T+\frac{p_\infty}{\rho}$ (Eq. 2; page-local
  $C_p=\gamma C_v$), one law per fluid of their sharp-interface solver.
  Eliminating $T$ gives $p=(\gamma-1)\rho e-\gamma p_\infty$, the
  energy form *(compiler check, not in the sources)*.
- **Pressure–temperature form.** Nguyen et al. add a reference energy
  $e_{0,k}$ and a reference entropy $s_{0,k}$ (page-local symbols;
  their $q_k$, $q'_k$, with $\pi_k$ for $p_{\infty,k}$):
  $p_k=(\gamma_k-1)\rho_k(e_k-e_{0,k})-\gamma_kp_{\infty,k}$ and
  $p_k=(\gamma_k-1)\rho_kC_{v,k}T-p_{\infty,k}$ (Eqs. 8a–8b), and
  express every phase quantity in $(p,T)$, the natural variables of a
  pressure–temperature-equilibrium mixture (Eqs. 10a–10e):

  $$
  \begin{aligned}
  \rho_k(p,T)&=\frac{p+p_{\infty,k}}{(\gamma_k-1)C_{v,k}T},\qquad
  h_k(p,T)=\gamma_kC_{v,k}T+e_{0,k},\\
  e_k(p,T)&=\frac{p+\gamma_kp_{\infty,k}}{p+p_{\infty,k}}\,C_{v,k}T+e_{0,k},\qquad
  s_k(p,T)=C_{v,k}\ln\frac{T^{\gamma_k}}{(p+p_{\infty,k})^{\gamma_k-1}}+s_{0,k},
  \end{aligned}
  $$

  with Gibbs function $g_k=h_k-Ts_k$ (Eq. 10e), sound speed
  $c_k^2=(\gamma_k-1)\gamma_kC_{v,k}T=\gamma_k(p+p_{\infty,k})/\rho_k$
  (Eq. 9), and derivatives $\partial\rho_k/\partial p=1/\big((\gamma_k-1)C_{v,k}T\big)$,
  $\partial\rho_k/\partial T=-\rho_k/T$, $\partial h_k/\partial p=0$,
  $\partial h_k/\partial T=\gamma_kC_{v,k}$ (Eq. 11): the enthalpy of
  a stiffened gas depends on temperature alone. They do not print the
  $C_{v,k}$ and $e_{0,k}$ values they use.
  [Wakimura et al. (2024)](/sources/wakimura-2024.md) (§2.2, Eqs. (4)–(8)) use the
  same law with energy constant $e_{0,k}$ and entropy constant $s_{0,k}$ (their $\eta_k$,
  $\eta'_k$), the same $T_k$, $s_k$ and Gibbs function, and the phasic sound speed
  $c_k^2=\gamma_k(p_k+p_{\infty,k})/\rho_k$. The common pressure of the isobaric mixture is
  $p=\dfrac{\rho e-\sum_k\phi_k\rho_ke_{0,k}-\sum_k\phi_k\gamma_kp_{\infty,k}/(\gamma_k-1)}{\sum_k\phi_k/(\gamma_k-1)}$
  (Eq. (6)). Equal Gibbs functions of liquid (1) and vapour (2) define the saturation curve
  (Eqs. (12)–(13)), with page-local $C_{p,k}=\gamma_kC_{v,k}$:
  $$
  A_{\mathrm s}+\frac{B_{\mathrm s}}{T}+C_{\mathrm s}\ln T+D_{\mathrm s}\ln(p+p_{\infty,1})-\ln(p+p_{\infty,2})=0,
  $$
  $A_{\mathrm s}=\frac{C_{p,1}-C_{p,2}+s_{0,2}-s_{0,1}}{C_{p,2}-C_{v,2}}$,
  $B_{\mathrm s}=\frac{e_{0,1}-e_{0,2}}{C_{p,2}-C_{v,2}}$,
  $C_{\mathrm s}=\frac{C_{p,2}-C_{p,1}}{C_{p,2}-C_{v,2}}$,
  $D_{\mathrm s}=\frac{C_{p,1}-C_{v,1}}{C_{p,2}-C_{v,2}}$ (page-local coefficients).
  *(Compiler check, not in the sources: $(g_1-g_2)/\big(T(C_{p,2}-C_{v,2})\big)$
  with the Gibbs functions of the form above is exactly this left-hand side.)* It enters the
  infinite-rate chemical relaxation of their six-equation model
  ([five- and six-equation models](/definitions/five-equation-model.md)).
- **Linear form.** Jain & Moin write each phase as
  $p_k=\mathsf a_k\rho_ke_k+\mathsf b_k$, with $\mathsf a_k=\gamma_k-1$ and
  $\mathsf b_k=-\gamma_kp_{\infty,k}$ for the stiffened gas (page-local
  $\mathsf a_k$, $\mathsf b_k$, the source's $\alpha_k$, $\beta_k$, renamed to keep the registry's weights and smoothness indicators), so that the single-pressure mixture of the
  [five-equation model](/definitions/five-equation-model.md) has
  $p=\big(\rho e+\sum_k\phi_k\mathsf b_k/\mathsf a_k\big)\big/\sum_k\phi_k/\mathsf a_k$
  (Eq. 5), the same mixture rule as below. They give
  $c_k=\sqrt{\gamma_k(p+p_{\infty,k})/\rho_k}$,
  $h_k=\gamma_k(p+p_{\infty,k})/\big(\rho_k(\gamma_k-1)\big)$
  (Eqs. 8–9) and the phasic entropy
  $s_k=C_{v,k}\ln\big((p+p_{\infty,k})/\rho_k^{\gamma_k}\big)+s_{0,k}$
  (Eq. 65; page-local $C_{v,k}$, $s_{0,k}$), whose transport they use to
  measure the entropy production of interface regularization. Their
  proof that matching split forms keep interface equilibrium uses the
  linear form, through $\rho_kh_k=(p-\mathsf b_k)/\mathsf a_k+p$ (Appendix B,
  printed as "$h_l$"); they state, without showing it, that a more
  general cubic equation of state can be used.
- **Coefficient form with an energy constant.** Huang & Johnsen, after
  Le Métayer et al., write each phase as
  $\rho_k(e_k-e_{0,k})=\mathsf G_kp+\mathsf A_k=\rho_kC_{v,k}T+p_{\infty,k}$
  with $\mathsf G_k=1/(\gamma_k-1)$ and
  $\mathsf A_k=\gamma_kp_{\infty,k}/(\gamma_k-1)$ (Eq. 22; page-local
  $\mathsf G_k$, $\mathsf A_k$, as for Fujiwara et al. below, and $e_{0,k}$,
  $C_{v,k}$ for their $A^P_p$, $B^P_p$, $D_p$, $C^T_p$). The phase sound speed is
  $\rho_kc_k^2=\big((\mathsf G_k+1)p+\mathsf A_k\big)/\mathsf G_k$ (Eq. 23),
  which is $\gamma_k(p+p_{\infty,k})$ *(compiler check, not in the
  sources)*. Their mixture internal energy is linear in $p$ at fixed
  volume fractions and phase densities,
  $\rho e=p\sum_k\phi_k\mathsf G_k+\sum_k\phi_k\mathsf A_k+\sum_k\phi_k\rho_ke_{0,k}$
  (Eq. 24). Temperature equilibrium across an interface at uniform $p$ and
  $T$ follows from consistent reconstruction of the partial densities and
  volume fraction alone, because the pressure-based and temperature-based
  reconstructed internal energies then coincide (§5.2, Lemma 5.1,
  Theorem 5.2; see [five-equation model](/definitions/five-equation-model.md)).
  Long et al. write the same law as
  $e=\frac{p+\gamma p_\infty}{(\gamma-1)\rho}+e_{0}$ and
  $T=\frac{p+p_\infty}{C_v(\gamma-1)\rho}$ for liquid water and its vapour
  (Eq. 3).
- **Energy form with an energy offset.** Huang et al. (2025b) write
  $p_k=(\gamma_k-1)\rho_k(e_k-e_{\infty,k})-\gamma_kp_{\infty,k}$ with an energy constant
  $e_{\infty,k}$ (page-local) and $c_k^2=\gamma_k(p_k+p_{\infty,k})/\rho_k$ (Eqs. 5–6; the
  printed law has the mixture density $\rho$ where the phase law requires the phase density $\rho_k$, see
  Qualifications); MFC 5.0 states the inverse,
  $e_k=(p_k+\gamma_kp_{\infty,k})/((\gamma_k-1)\rho_k)$ (Wilfong et al. §2.2). Both are the
  law above.
- **Parameters for liquids.** Bryngelson et al. state that the liquid
  constants are fitted to shock-Hugoniot data (§3).

## The Tait law

[Nguyen et al. (2022)](/sources/nguyen-2022.md) §2.2 offer, for the
liquid, the barotropic Tait law
$p=B\big[(\rho/\rho_0)^{\gamma_{\mathrm T}}-1\big]+p_0$ with
$c^2=B\gamma_{\mathrm T}\rho^{\gamma_{\mathrm T}-1}/\rho_0^{\gamma_{\mathrm T}}$
and $B=\rho_0c_0^2/\gamma_{\mathrm T}$ (Eqs. 12–13; page-local
$\gamma_{\mathrm T}$ the Tait exponent, $c_0$ the reference sound
speed), with $\rho_0=1000$ kg/m³, $\gamma_{\mathrm T}=7.15$ and
$c_0=1500$ m/s, i.e. $B\approx3.15\times10^8$ Pa *(compiler check, not in the sources)*.
For very low Mach numbers they reset the bulk modulus to the artificial
$B=\rho_0\lvert v_{\mathrm{ref}}\rvert^2/(\gamma_{\mathrm T}M_{\mathrm{ref}}^2)$
with $M_{\mathrm{ref}}\in[0.1,0.3]$, which relaxes the acoustic time
step: advecting a water–air interface at 1.5 m/s took 195,249
iterations with the stiffened gas and 52,017 with the Tait liquid
(Table 1). How the barotropic law enters their pressure–temperature
formulation is not explained.

[Long, Cai & Pan (2023)](/sources/long-2023.md) §4.5 use a Tait law for
liquid water in their near-wall bubble-collapse test,
$p=B\big[(\rho/\rho_0)^{\gamma_{\mathrm T}}-1\big]+p_0$ with $B=3310$ bar,
$p_0=1$ bar and $\rho_0=1000$ kg/m³, and drop the liquid energy equation
(isothermal water at 293 K). They do not print the exponent
$\gamma_{\mathrm T}$.

The isentropes of a stiffened gas are
$(p+p_\infty)\rho^{-\gamma}=\mathrm{const}$, i.e.
$p=(p_0+p_\infty)(\rho/\rho_0)^\gamma-p_\infty$, which is the Tait
law with $\gamma_{\mathrm T}=\gamma$ and $B=p_0+p_\infty$
*(compiler check, not in the sources)*. Along an isentrope, Zheng, Shu &
Qiu's stiffened gas with $\gamma=7.15$ and $p_\infty=3.309\times10^8$
Pa, which they call the "Tait EOS", is therefore a Tait law with
exponent 7.15 and $B\approx p_\infty$; Nguyen et al.'s $B$, fixed by
$c_0=1500$ m/s, is a slightly different fit, $3.15\times10^8$ Pa
*(compiler check, not in the sources)*.

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
mixture follows from the temperature form instead (Li et al. (2022c); see
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).
Huang & Johnsen's mixture sound speed for $N$ phases depends on the
coefficient of their volume-fraction equation; with Allaire's choice it is
a convex combination of the phasic $\rho_kc_k^2$ weighted by
$\phi_k/(\gamma_k-1)$, with Kapila's it is Wood's (§2.9, Eq. 25). For a
multicomponent mixture in mass fractions, Fujiwara et al. write
$\rho e=p\,\mathsf G+\mathsf A$ with mixing rules in mass fractions and
molar masses for both $\mathsf G=1/(\gamma-1)$ and
$\mathsf A=\gamma p_\infty/(\gamma-1)$ (Appendix B, Eqs. B.1–B.2;
page-local symbols, see
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).
Huang et al. (2025b) print a different rule for the stiffening pressure,
$p_\infty/(\gamma-1)=\sum_k\phi_kp_{\infty,k}/(\gamma_k-1)$, together with
$\rho e_\infty=\sum_k\phi_k\rho_ke_{\infty,k}$ (Eq. 9), and a mixture pressure
(Eq. 10) whose $p_\infty$ term has the opposite sign of the one their phase law
implies (Qualifications); with their rule the mixture constant differs from
Wong et al.'s by the factors $\gamma_k$ *(compiler check, not in the sources)*.
Jain & Moin's Eq. (5) is the volume-fraction rule written with
$\mathsf a_k,\mathsf b_k$: with $\mathsf a_k=\gamma_k-1$ and
$\mathsf b_k=-\gamma_kp_{\infty,k}$ it reproduces $1/(\gamma-1)=\sum_k\phi_k/(\gamma_k-1)$
and $\gamma p_\infty/(\gamma-1)=\sum_k\phi_k\gamma_kp_{\infty,k}/(\gamma_k-1)$
*(compiler check, not in the sources)*.

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

For one stiffened-gas species, Li et al. (2022c) use the specific entropy
$S=C_v\ln T-R\ln\rho$ and the convex entropy $\eta=-\rho S$ with flux
$F_\eta=\eta v$ (§3.3.1, Eq. 3.13). The entropy flux potential (§6 of
the registry) is $\psi=\big(R\rho-p_\infty/T\big)v$, so the stiffening
pressure enters the potential through $p_\infty/T$ (Eq. 3.14). For
mixtures the entropy is the mass-weighted sum of species entropies
(Eqs. 3.16–3.17). With these, Li et al. (2022c) derive explicit
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
| Li et al. (2022c) Ex. 5.2, single-fluid shock tube | 3 | 1 | non-dimensional |
| Li et al. (2022c) Ex. 5.9, 5.11, surrounding medium | 3 | 100 | non-dimensional |
| Bai & Li §3.1.2, water against air | 2.788103 | $7.862511\times10^8$ Pa | SI; $C_p=4190$ J/(kg K) |
| Bai & Li §3.1.4, §3.5–3.6, water | 4.4 | $6.0\times10^8$ Pa | SI; $C_p=2653.87$ in §3.1.4, not printed for §3.5–3.6 |
| Bai & Li §3.3.2, copper-like metal | 3.0 | $4.62\times10^{10}$ (unit printed "bar") | SI; $C_p=2587$ |
| Nguyen et al. §3.3, water | 4.4 | $6\times10^8$ Pa | SI |
| Huang & Johnsen §4.2, air–water Riemann problem | 2.35 | $10^9$ Pa | energy constant $-1.167\times10^3$ J/kg |
| Huang & Johnsen §4.3, water disk advection | 6.12 | $3.43\times10^8$ Pa | §5.2: $C_v=223.37$ (water), $701.27$ (air) J/(kg K) |
| Long et al. §2.2, liquid water | 2.35 | $10^9$ Pa | energy constant $-1167\times10^3$ J/kg, $C_v=1816$ J/(kg K) |
| Long et al. §2.2, water vapour | 1.33 | 0 | energy constant $1990\times10^3$ J/kg, $C_v=1399$ J/(kg K) |
| Paula et al. §7.4.1–7.4.2, water | 4.4 | $6\times10^8$ Pa | SI |
| Paula et al. §7.4.3, underwater explosion | 5.5 | $492.115\times10^6$ Pa | SI |
| Wakimura et al. Table 1, liquid water ("for 300–500 K") | 2.35 | $10^9$ Pa | $e_0=-1167\times10^3$ J/kg, $s_0=0$, $C_v=1816$ J/(kg K) |
| Wakimura et al. Table 1, water vapour | 1.43 | 0 | $e_0=2030\times10^3$ J/kg, $s_0=-23.4\times10^3$, $C_v=1040$ J/(kg K) |
| Wakimura et al. Table 2, liquid dodecane ("for 300–500 K") | 2.35 | $4\times10^8$ Pa | $e_0=-775.269\times10^3$ J/kg, $s_0=0$, $C_v=1077.7$ J/(kg K) |
| Wakimura et al. Table 2, dodecane vapour | 1.025 | 0 | $e_0=-237.547\times10^3$ J/kg, $s_0=-24.4\times10^3$, $C_v=1956.45$ J/(kg K) |
| Zhang et al. (2024a) Table 1, water (dimensional tests, §§4.1–4.8) | 4.4 | $6.0\times10^8$ Pa | SI |
| Zhang et al. (2024a) §4.12, water in droplet collision | 5.0 | $10^8$ Pa | SI |
| Zhang et al. (2024a) §§4.9–4.11, water in capillary tests | — | 6000 | non-dimensional ($\gamma$ as Table 1) |
| Huang et al. (2025b) §4.3.1, underwater explosion (water) | 4.4 | $6\times10^8$ Pa | SI; air $\gamma=1.4$, $p_\infty=0$ |
| Jain & Moin §4, Taylor–Green and isotropic-turbulence tests | 1.4 | 0 | non-dimensional; in §5 the $p_{\infty,k}$ are chosen to equalize the turbulent Mach number, values not printed |

The fits differ from test to test within one source (Tsoutsanis et al.
use three water fits in three tests without comment, Bai & Li two): the
sources take the constants with each benchmark setup, not from one
water model. For Bai & Li's metal, $p_\infty=4.62\times10^{10}$ Pa with
$\rho=8930$ kg/m³ gives $c=\sqrt{3(p+p_\infty)/\rho}\approx3.9$ km/s,
a metal-like sound speed, while the printed unit "bar" would give about
1250 km/s; the unit is evidently pascal *(compiler check, not in the
sources)*. Huang & Johnsen's heat capacities follow from the
temperature form at $p=101325$ Pa, $T=300$ K and densities $1.204$ and
$1000$ kg/m³: $2.5\cdot101325/(1.204\cdot300)=701.3$ and
$(101325+3.43\times10^8)/(5.12\cdot1000\cdot300)=223.37$ J/(kg K)
*(compiler check, not in the sources)*; the paper prints the states of
that test in an unstated nondimensional scaling ($p=4.819\times10^{-5}$,
water density 1; §4.3, Eq. 50).

## Qualifications

- Huang & Johnsen (§4.2) and Long et al. (§2.2) give liquid water the
  same constants $\gamma=2.35$, $p_\infty=10^9$ Pa, but print its energy
  constant as $-1.167\times10^3$ J/kg and $-1167\times10^3$ J/kg, a factor
  of 1000 apart. Wakimura et al. (2024, Table 1) print $-1167\times10^3$ J/kg with
  the same $\gamma$, $p_\infty$ and $C_v=1816$ J/(kg K) as Long et al., so two sources
  agree on the larger value; their vapour constants differ from Long et al.'s
  ($\gamma=1.43$ against $1.33$, $C_v=1040$ against $1399$).
- Wakimura et al. label their dodecane fit "for 300–500 K" but start the vapour-bubble
  test at 600 K (§4.4). Their liquid densities follow from the temperature form: e.g.
  $(10^5+4\times10^8)/(1.35\cdot1077.7\cdot600)=458.3$ kg/m³, the printed $458.338$
  *(compiler check, not in the sources)*.
- Zhang et al. (2024a, Fig. 1) give the sound speeds $1625$ m/s for water at
  $\rho=1000$ kg/m³ and $374$ m/s for air at $\rho=1$ kg/m³, both at $10^5$ Pa;
  $\sqrt{4.4(10^5+6\times10^8)/1000}=1624.9$ and $\sqrt{1.4\cdot10^5}=374.2$ *(compiler
  check, not in the sources)*.

- Huang et al. (2025b) print the phase law with the mixture density, $(\gamma_k-1)\rho(e_k-e_{\infty,k})$
  (Eq. 5), and their mixture pressure (Eq. 10) as
  $p=\big(\rho e-\sum_k\phi_k\rho_ke_{\infty,k}+\sum_k\phi_kp_{\infty,k}/(\gamma_k-1)\big)\big/\sum_k\phi_k/(\gamma_k-1)$;
  inverting Eq. 5 with $\rho_k$ gives $-\sum_k\phi_k\gamma_kp_{\infty,k}/(\gamma_k-1)$ in that
  numerator. One of the two equations is misprinted, and the paper does not say which
  it implements *(compiler check, not in the sources)*.
- The name is not uniform: Zheng et al. call the stiffened-gas energy
  relation the "Tait EOS"; the other sources call it stiffened gas, and
  Nguyen et al. use "Tait" for the barotropic law of the section above.
  Nguyen et al. also call the Tait exponent "the heat capacity ratio".
- The law has no temperature in its energy form; the temperature form
  of Li et al. (2022c) adds a constant heat capacity per species, which is what
  makes a thermal-equilibrium mixture and a physical entropy available.
- Wong et al.'s concavity result covers a stiffened phase paired with an
  ideal gas; it says nothing about the temperature-based multicomponent
  closure of Li et al. (2022c).

# Citations

- [Wong et al. (2021)](/sources/wong-2021.md) — §2, Eqs. (6)–(14), Lemma 1, Theorem 1; §6, Table 1; §6.4 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §2, Eqs. (6)–(11); §4.3–4.5.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §3, Eqs. (6)–(9) (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2; §4, Ex. 2, 5–7, 9, 11.
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — §1, Eq. (1.2); §3.3–3.4, Eqs. (3.13)–(3.17); Ex. 5.2, 5.9 (arXiv v1).
- [Bai & Li (2022)](/sources/bai-2022.md) — §2, Eq. (2); §3.1–3.6, Table 3.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.2, Eqs. (8)–(13); §3.1, Table 1; §3.3, Table 2.
- [Jain & Moin (2022)](/sources/jain-2022.md) — §2, Eqs. (5)–(9); §4–5; Eq. (65); Appendix B (arXiv v1).
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §2.9, Eqs. (22)–(25); §4.2–4.3, Eqs. (49)–(50); §5.2, Lemma 5.1, Theorem 5.2.
- [Long, Cai & Pan (2023)](/sources/long-2023.md) — §2.2, Eq. (3); §4.5 (Tait law).
- [Paula et al. (2023)](/sources/paula-2023.md) — §2.1, Eq. (3); §7.4.1–7.4.3 (parameter values).
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — Appendix B, Eqs. (B.1)–(B.2) (mass-fraction mixture rule).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §2.2, Eqs. (4)–(8), (12)–(13), Tables 1–2; §4.4: caloric form, saturation curve, water and dodecane constants.
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §2, Eqs. (5)–(10); §4.3.1.
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §2.2.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §2.2–2.3, Eqs. (9)–(16), Table 1, Fig. 1; §§4.9–4.12: parameter values and sound speeds.
