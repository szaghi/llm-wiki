---
type: Method
title: "Entropy-conservative and kinetic-energy-preserving two-point fluxes"
description: "Two-point fluxes satisfying Tadmor's jump condition conserve entropy, and entropy-dissipative ones satisfy it as an inequality; the page states the condition in Cartesian, directional, moving-mesh and non-conservative form and gives the Ranocha, Shima, asymptotically entropy-conservative algebraic, multicomponent, vibrating-air, stiffened-gas, GLM-MHD, relativistic and scalar fluxes and their entropy-stable dissipation."
status: established
aliases: [EC flux, entropy-conservative flux, entropy-dissipative flux, ED flux, Tadmor flux, KEP flux, KEEP flux, Ranocha flux, Shima flux, AEC flux, asymptotically entropy-conservative flux]
tags: [entropy-stable, kinetic-energy-preserving, numerical-flux, dg]
timestamp: 2026-10-24T06:02:00Z
---

# Entropy-conservative and kinetic-energy-preserving two-point fluxes

Let $\eta(u)$ be a convex entropy of $\partial_tu+\sum_d\partial_{x_d}f^{(d)}(u)=0$,
with entropy fluxes $F_\eta^{(d)}$, entropy variables $w=\eta'(u)$ and flux
potentials $\psi^{(d)}=w\cdot f^{(d)}-F_\eta^{(d)}$. A consistent two-point
flux $f^{(d)}(u^-,u^+)$ is **entropy-conservative** (EC) when it satisfies
Tadmor's condition

$$[\![w]\!]\cdot f^{\mathrm{ec},(d)}(u^-,u^+)=[\![\psi^{(d)}]\!],$$

and **entropy-dissipative** (ED) when
$[\![w]\!]\cdot f^{(d)}-[\![\psi^{(d)}]\!]\le0$
([Ranocha et al. (2023)](/sources/ranocha-2023.md), Def. 2.5, after Tadmor).
A **directional** flux $f(u^-,u^+,n)$, consistent with $\sum_dn_df^{(d)}(u)$,
is EC when $[\![w]\!]\cdot f(u^-,u^+,n)=\sum_dn_d[\![\psi^{(d)}]\!]$. It must also
satisfy $f(u^-,u^+,n)=-f(u^+,u^-,-n)$ (Def. 2.4).
[Renac (2021)](/sources/renac-2021.md) states the same requirements,
symmetry, consistency, Tadmor's condition and the conservation relation,
and adds Lipschitz continuity for the entropy-stable flux (§3.1,
Eqs. (19)–(23)).

The matching **numerical entropy flux** is
$F^{\mathrm{num}}_\eta=\{\!\{w\}\!\}\cdot f^{\mathrm{ec}}-\{\!\{\psi\}\!\}$
([Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md), Eqs.
(27)–(28); the alternative $\{\!\{w\}\!\}\cdot f^{\mathrm{ec}}-\psi(\{\!\{w\}\!\})$
also works, Remark 2.6).
[Duan & Tang (2022)](/sources/duan-2022.md) use the same form, with metric
terms, for their moving-mesh scheme (Eqs. (3.20)–(3.21)).

## Role in DG

Abgrall et al. (2022) point out that with EC surface fluxes, element-wise
conservation and element-wise entropy conservation are compatible: if the
DG solution is constant in every element the scheme is an EC
finite-volume scheme, and the two element constraints can only conflict
for a constant element state (Remarks 2.5–2.7, Eq. (29)). This is what
lets an [entropy correction term](/methods/entropy-correction-term.md)
enforce both at once.

Used as the symmetric volume flux of
[flux differencing](/methods/flux-differencing.md) on a diagonal-norm
[SBP](/operators/summation-by-parts-operator.md) element, an EC flux makes
the volume term entropy-conservative. Pairing it with an EC or ED surface
flux gives an EC or ED DG scheme (Ranocha et al. (2023), §2;
[entropy stability](/properties/entropy-stability.md)).
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) use
two such pairings:

- an EC volume flux with a local Lax–Friedrichs (Rusanov) surface flux on
  the KPP problem (§5.1);
- the Chandrashekar flux in the volume with a Rusanov surface flux for Euler
  (§5.2).

In a modal DG scheme solved in conservative variables and evaluated at
projected entropy variables, the EC flux enters only at the interfaces.
[Alberti et al. (2025)](/sources/alberti-2025.md) state Tadmor's condition,
in their orientation of the jump, as
$[\![w_h]\!]^\top h-[\![\psi_d]\!]n_d\ge0$, with equality for an EC flux, and
show that once the quadrature error of each element is removed by an
[entropy correction term](/methods/entropy-correction-term.md), the scheme
is entropy conservative or stable exactly when the interface flux
satisfies it (§2.1.1, Eqs. (19), (25)). On the isentropic vortex the
Ismail–Roe EC flux gives exact (machine-level) entropy conservation and
order $N$, one below the $N+1$ of an entropy-stable Godunov flux with an
exact Riemann solver, whose entropy error converges at $2N+1$ (§3.1.1,
Figs. 1–2). They prefer EC fluxes to the alternative correction of
Abgrall, Öffner & Ranocha, which is EC for any flux but needs a numerical
entropy flux and gives a larger correction, and keep that alternative for
cases with no EC flux, such as real-gas equations of state (§2.1.1).

## Fluxes for the compressible Euler equations

Let page-local $(\!(a;b)\!)=\tfrac12(a^+b^-+a^-b^+)$ be the product mean,
with $\{\!\{\cdot\}\!\}$ and $\{\!\{\cdot\}\!\}_{\log}$ the arithmetic and logarithmic
means of the registry and $n$ the direction. Ranocha et al. (2023) give the
directional forms of two fluxes (§3.2).

**Shima et al. flux** (kinetic-energy- and pressure-equilibrium-preserving,
*not* EC; the "cheap" flux; Eq. (3.7)):

$$\begin{aligned}
f_\rho&=\{\!\{\rho\}\!\}\{\!\{v\cdot n\}\!\},\qquad f_{\rho v}=f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\}\,n,\\
f_E&=f_\rho\tfrac12(\!(v;v)\!)+\frac{\{\!\{p\}\!\}\{\!\{v\cdot n\}\!\}}{\gamma-1}+(\!(p;v\cdot n)\!).
\end{aligned}$$

**Ranocha flux** (EC, kinetic-energy- and pressure-equilibrium-preserving;
the "expensive" flux; Eq. (3.10)):

$$\begin{aligned}
f_\rho&=\{\!\{\rho\}\!\}_{\log}\{\!\{v\cdot n\}\!\},\qquad f_{\rho v}=f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\}\,n,\\
f_E&=f_\rho\tfrac12(\!(v;v)\!)+\frac{f_\rho}{(\gamma-1)\{\!\{\rho/p\}\!\}_{\log}}+(\!(p;v\cdot n)\!).
\end{aligned}$$

The properties of both fluxes are cited from the literature, not proved
in the paper (§3.2). A division-saving rewrite of the last term uses
$1/\{\!\{\rho/p\}\!\}_{\log}=p^+p^-/\{\!\{\rho p\}\!\}^{\times}_{\log}$. Here
$\{\!\{\rho p\}\!\}^{\times}_{\log}$ (page-local) is the logarithmic mean of the two
numbers $\rho^+p^-$ and $\rho^-p^+$ (Eq. (3.11)). The same optimizations
apply to the Ismail–Roe and Chandrashekar EC fluxes (§3.2).
Rueda-Ramírez et al. (2022) describe the Chandrashekar flux as EC and
kinetic-energy-preserving, and use its MHD relative, the
Chandrashekar–Klingenberg flux, for GLM-MHD (§4, §5.3).

**Shared structure** *(compiler check, not in the sources)*. Both fluxes
share three features:

- The momentum flux is the mass flux times the arithmetic mean of the
  velocity, plus a central pressure.
- The kinetic part of the energy flux is $\tfrac12f_\rho\,v^-\cdot v^+$,
  since $(\!(v;v)\!)=v^-\cdot v^+$.
- They differ only in the mass flux and in the internal-energy term, the
  one carrying $1/(\gamma-1)$; the pressure-work term $(\!(p;v\cdot n)\!)$ is
  common.

This is the structure that
[Coppola & Veldman (2023)](/sources/coppola-2023.md) prove necessary and
sufficient for kinetic-energy preservation of three-point finite-volume
schemes: momentum flux $m_{i+1/2}\{\!\{v\}\!\}$ with a free mass flux $m_{i+1/2}$,
and kinetic-energy flux $\tfrac12m_{i+1/2}v_iv_{i+1}$ (Observation 7). The
Shima et al. mass flux $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ equals their Kennedy–Gruber–Pirozzoli
face mass flux $\tfrac14(\rho_i+\rho_{i+1})(v_i+v_{i+1})$ ($\zeta=1/2$ on
[split convective forms](/methods/split-convective-forms.md)) *(compiler check, not in the
sources: neither paper makes the identification)*. Coppola &
Veldman add that no finite-difference equivalent of the logarithmic-mean
fluxes of Chandrashekar or Ranocha is known (§5.4). Their in-passing
remark, after Chandrashekar, is that the free mass-flux choice can be used
to induce entropy conservation. See
[kinetic energy preservation](/properties/kinetic-energy-preservation.md).

Abgrall et al. (2022) state the kinetic-energy-preserving condition on a
surface flux in the same form, $f_{\rho v_m}=\{\!\{v_m\}\!\}f_\rho+\{\!\{p\}\!\}\,n_m$
for any mass flux $f_\rho$, with the kinetic-energy numerical flux
$\tfrac12(v^-\cdot v^+)f_\rho+\tfrac12(p^+\,v^-\cdot n+p^-\,v^+\cdot n)$
(Eq. (40), §3.3, after Jameson and Ranocha). In their Taylor–Green tests,
flux differencing with the Ranocha flux or with Pirozzoli's
kinetic-energy-preserving flux outlasts every central scheme with
correction terms (§4.2.2, App. A.3;
[flux differencing](/methods/flux-differencing.md)).

**Square-root-density kinetic-energy fluxes.** Written as two-point
fluxes, the split forms of finite differences imply kinetic-energy fluxes
in the product mean $(\!(a;b)\!)$ of this page
([Edoh (2022)](/sources/edoh-2022.md), Eqs. (3)–(6); Edoh's $\tilde F(a,b)$).
Edoh states that every kinetic-energy-preserving split form the author knows
implies a kinetic-energy flux built on $(\!(v_m;v_m)\!)=v_m^-v_m^+$, a
geometric-type average of the velocities on the two sides, while Edoh's
Div-rot splitting squares one variable: its kinetic-energy flux is
$\tfrac12(\!(\sqrt\rho\,v_j;\sqrt\rho\,\lvert v\rvert^2)\!)$ in direction $j$; Edoh argues this promotes
realizability when the interface velocities change sign, and that it lets
the total-energy flux be exactly the internal-energy flux plus the
kinetic-energy flux (Remark 4, Table 4). The realizability argument is
stated, not tested. The splittings are on
[split convective forms](/methods/split-convective-forms.md).

**Two-phase KEEP face fluxes.** [Jain & Moin (2022)](/sources/jain-2022.md)
build a second-order central scheme for a diffuse-interface five-equation
two-phase model from face fluxes chosen to satisfy kinetic-energy,
mass-summation, interface-equilibrium and pressure-work consistency
conditions (§3, Eq. (58)). In this page's notation, with $\{\!\{\cdot\}\!\}$
the two-point average, their single-phase part is

$$f_\rho=\{\!\{\rho\}\!\}\{\!\{v\}\!\},\quad f_{\rho v}=f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\},\quad f_E=f_\rho\tfrac12(\!(v;v)\!)+\{\!\{\rho e\}\!\}\{\!\{v\}\!\}+(\!(p;v)\!),$$

with $\rho e$ the internal energy per unit volume. For an ideal gas,
$\rho e=p/(\gamma-1)$ and $\{\!\{\rho e\}\!\}=\{\!\{p\}\!\}/(\gamma-1)$, so this is the
Shima et al. flux above *(compiler check, not in the sources: neither
source compares the two)*. Jain & Moin call the scheme kinetic-energy-
and entropy-preserving, but its entropy conservation is the approximate
conservation of the physical phase entropies observed in their tests,
not Tadmor's condition; they also call Chandrashekar's flux an
"approximate entropy conserving flux formulation" (§3.5). Their
comparison concerns the internal-energy part of $f_E$ only:

| internal-energy flux | as named by Jain & Moin | interface equilibrium |
|---|---|---|
| $\{\!\{\rho e\}\!\}\{\!\{v\}\!\}$ | quadratic split (theirs) | yes |
| $\{\!\{\rho\}\!\}\{\!\{e\}\!\}\{\!\{v\}\!\}$ | cubic split (Kennedy–Gruber, Kuya et al.) | no |
| $\{\!\{\rho\}\!\}\dfrac{2e^-e^+}{e^-+e^+}\{\!\{v\}\!\}$ | Chandrashekar's harmonic mean | no |

(Eqs. (60)–(62), Table 1; $e$ the specific internal energy). All three
run stably in single-phase tests; only the first survives at density
ratio 10 ([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
The two-phase part of the scheme adds regularization fluxes in quartic
and quintic splits (Eq. (59);
[split convective forms](/methods/split-convective-forms.md)).

## Asymptotically entropy-conservative algebraic fluxes

[De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) write the
Ranocha flux in internal-energy form for a perfect gas, convective parts
only, with the pressure term $p\,\partial_xv$ discretized centrally:
$f_\rho=\{\!\{\rho\}\!\}_{\log}\{\!\{v\}\!\}$, $f_{\rho v}=f_\rho\{\!\{v\}\!\}$,
$f_{\rho e}=f_\rho/\{\!\{1/e\}\!\}_{\log}$, with $e$ the specific internal
energy (§2, Eq. (2); arXiv v2). It agrees with the total-energy form above
because $\rho/p=1/((\gamma-1)e)$ gives
$(\gamma-1)\{\!\{\rho/p\}\!\}_{\log}=\{\!\{1/e\}\!\}_{\log}$ *(compiler check,
not in the sources)*. Its only non-algebraic ingredients are the two
logarithmic means. The authors replace them by algebraic means and order
the candidates with the mean inequalities. With page-local geometric and
harmonic means $\{\!\{a\}\!\}_{\mathrm G}=\sqrt{a^-a^+}$,
$\{\!\{a\}\!\}_{\mathrm H}=a^-a^+/\{\!\{a\}\!\}$ and the page-local relative jump
$\mathsf j_a=[\![a]\!]/(2\{\!\{a\}\!\})$, $\lvert\mathsf j_a\rvert<1$ for $a>0$:

$$\{\!\{a\}\!\}_{\mathrm G}\le\{\!\{a\}\!\}_{\log}\le\{\!\{a\}\!\},\qquad \{\!\{a\}\!\}_{\mathrm H}\le\big(\{\!\{1/a\}\!\}_{\log}\big)^{-1}\le\{\!\{a\}\!\}_{\mathrm G},$$

strict for $a^-\ne a^+$, with $\{\!\{a\}\!\}_{\mathrm G}=\{\!\{a\}\!\}(1-\mathsf j_a^2)^{1/2}$
and $\{\!\{a\}\!\}_{\mathrm H}=\{\!\{a\}\!\}_{\mathrm G}(1-\mathsf j_a^2)^{1/2}$ (Eqs.
(5)–(8); the first chain recalled from Carlson). Hence the arithmetic mean
is the natural algebraic surrogate for the density in the mass flux, but
the harmonic or geometric mean, not the arithmetic one, for the internal
energy (§3). The fluxes compared, named by the mean of $\rho$ in $f_\rho$
and of $e$ in $f_{\rho e}$, all with $f_{\rho v}=f_\rho\{\!\{v\}\!\}$:

| flux | $f_\rho$ | $f_{\rho e}$ | properties stated |
|---|---|---|---|
| Aρ-Ae | $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ | $f_\rho\{\!\{e\}\!\}$ | KEP, not PEP; equals KGP($\rho e$) and, for exact time integration, the KEEP scheme of Kuya et al. |
| Aρ-Ge | $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ | $f_\rho\{\!\{e\}\!\}_{\mathrm G}$ | KEP, not PEP |
| Gρ-Ge | $\{\!\{\rho\}\!\}_{\mathrm G}\{\!\{v\}\!\}$ | $f_\rho\{\!\{e\}\!\}_{\mathrm G}$ | KEP and PEP |
| Aρ-He (new) | $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ | $f_\rho\{\!\{e\}\!\}_{\mathrm H}$ | KEP and PEP |
| Aρ-Ap | $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ | $\{\!\{v\}\!\}\{\!\{p\}\!\}/(\gamma-1)$ | KEP and PEP (KEEP-PE of Shima et al.) |

(Eqs. (3), (4), (9), (10), (15)). PEP is
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md).
The last row is the Shima et al. flux of the previous section.

**The AEC($N_{\mathrm T}$) hierarchy.** The exact series
$[\![\ln a]\!]=\frac{[\![a]\!]}{\{\!\{a\}\!\}}\sum_{n\ge0}\frac{\mathsf j_a^{2n}}{2n+1}$
(Eqs. (11)–(12)) inserted in both logarithmic means and truncated at
order $N_{\mathrm T}$ (page-local truncation order, not a DG degree) gives

$$f_\rho=\{\!\{\rho\}\!\}\{\!\{v\}\!\}\Big(\sum_{n=0}^{N_{\mathrm T}}\frac{\mathsf j_\rho^{2n}}{2n+1}\Big)^{-1},\qquad f_{\rho e}=f_\rho\,\{\!\{e\}\!\}_{\mathrm H}\sum_{n=0}^{N_{\mathrm T}}\frac{\mathsf j_e^{2n}}{2n+1}$$

(Eq. (13)): $N_{\mathrm T}=0$ is Aρ-He and $N_{\mathrm T}\to\infty$ the Ranocha flux. The
internal-energy factor comes from $[\![\ln e]\!]$ expanded while
$[\![1/e]\!]$ is kept exact, which produces the harmonic mean. The authors
call the family asymptotically entropy conservative: the entropy
production of the spatial discretization can be reduced at will by
raising $N_{\mathrm T}$, with algebraic operations only (§1, §4). The series is the
one Ranocha et al. truncate to evaluate the logarithmic mean (Algorithm 2,
below, with $\varsigma=\mathsf j_a^2$) *(compiler check, not in the
sources)*; here it is truncated by design, not to machine precision.

- **PEP for every $N_{\mathrm T}$.** With $v\equiv v_0$ and $p\equiv p_0$ constant,
  $\{\!\{e\}\!\}_{\mathrm H}=p_0/\big((\gamma-1)\{\!\{\rho\}\!\}\big)$ and
  $\mathsf j_e=-\mathsf j_\rho$, so the two truncated sums cancel and
  $f_{\rho e}=v_0p_0/(\gamma-1)$, provided the same $N_{\mathrm T}$ is used in both
  expansions (§4, Eq. (14)).
- **Against KEEP($N_{\mathrm T}$).** The expansion of Tamaki, Kuya & Kawai also
  expands $[\![1/e]\!]$; its $N=1$ member,
  $f_{\rho e}=f_\rho\{\!\{e\}\!\}(1+\mathsf j_e^2/3)/(1+\mathsf j_e^2)$ in this
  notation, is not PEP (§4, §5).
- **Evidence.** On a 1D [density wave](/benchmarks/density-wave-advection.md) ($\rho_0=1+\exp(\sin2\pi x)$,
  $v=p=1$, 61 points, RK4, CFL 0.01) Aρ-Ae diverges at $t\approx22$ while
  Aρ-He and Gρ-Ge run to $t=100$; AEC(1) and KEEP(1) conserve entropy
  best, but KEEP(1) shows spurious pressure oscillations (Fig. 1b plots
  $p-p_0$ on a $10^{-7}$ scale) and AEC(1) none (§5, Fig. 1); the authors
  state that the Ranocha flux gives entropy production at machine zero
  (§5, not plotted). On the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($32^3$, fourth
  and sixth order by flux differencing) Aρ-He and Gρ-Ge beat Aρ-Ap and
  Aρ-Ae in entropy conservation, and AEC(1) and KEEP(1) keep the entropy
  integral most nearly constant (Fig. 2).

The authors state that the AEC fluxes are cheaper than logarithmic-mean
fluxes and need no protection against division by zero, without timings
(§1, §6). Their observation that, with a pure sine density, global entropy
was conserved by symmetry despite local non-conservation is why they use
a non-sinusoidal profile (§5).

## Five-species air with vibrational energy

[Peyvan et al. (2023)](/sources/peyvan-2023.md) derive EC fluxes for the
1D Euler equations of five-species air ($N$, $O$, $NO$, $N_2$, $O_2$) with
a rigid-rotor harmonic-oscillator internal energy (§3, Eqs. (60)–(91);
arXiv v1). Page-local symbols, per species $k$: partial density $\rho_k$,
gas constant $r_k$, formation energy $e^0_k$, vibrational characteristic
temperature $T^{\mathrm v}_k$, $\mathsf a_k=3/2$ for atoms and $5/2$ for
diatomic molecules, and the vibration switch $\mathsf b_k\in\{0,1\}$, so
that $e_k=e^0_k+\mathsf a_kr_kT+\mathsf b_kr_kT^{\mathrm v}_k/(e^{T^{\mathrm v}_k/T}-1)$.
The entropy is the multicomponent entropy of Gouasmi et al.,
$\rho s=\sum_k\rho_ks_k$ with $s_k=\int c_{v,k}/T\,dT-r_k\ln\rho_k$, and
Tadmor's condition is worked in the parameter vector $(\rho_k,v,1/T)$.
The vibrational term needs the jump of $\ln(e^{T^{\mathrm v}_k/T}-1)$, which
the authors write with a new composite mean: for $z=1/T$,

$$[\![\ln(e^{T^{\mathrm v}_kz}-1)]\!]=\frac{[\![z]\!]}{\{\!\{z\}\!\}_{\ln\exp,k}},\qquad \{\!\{z\}\!\}_{\ln\exp,k}=\{\!\{e^{T^{\mathrm v}_kz}-1\}\!\}_{\log}\,\{\!\{z\}\!\}_{\exp,k},\quad \{\!\{z\}\!\}_{\exp,k}=\frac{[\![z]\!]}{[\![e^{T^{\mathrm v}_kz}]\!]}$$

(Eqs. (78)–(82); page-local means, details on
[logarithmic mean](/operators/logarithmic-mean.md)). The flux is

$$\begin{aligned}
f_{\rho_k}&=\{\!\{v\}\!\}\{\!\{\rho_k\}\!\}_{\log},\qquad f_{\rho v}=\frac{\sum_kr_k\{\!\{\rho_k\}\!\}}{\{\!\{1/T\}\!\}}+\{\!\{v\}\!\}\sum_kf_{\rho_k},\\
f_E&=\sum_k\Big(e^0_k-\mathsf b_kr_kT^{\mathrm v}_k+\frac{\mathsf a_kr_k}{\{\!\{1/T\}\!\}_{\log}}+\frac{\mathsf b_kr_k}{\{\!\{1/T\}\!\}_{\ln\exp,k}}-\tfrac12\{\!\{v^2\}\!\}\Big)f_{\rho_k}+\{\!\{v\}\!\}f_{\rho v}
\end{aligned}$$

(Eqs. (89)–(91)). The authors state that EC fluxes had not been derived
before for hypersonic gases whose internal energy has translational,
rotational and vibrational parts; Gouasmi et al. covered constant or
polynomial-in-$T$ heat capacities (§1). With $\mathsf b_k=0$ the flux has
the structure of a frozen multicomponent EC flux, its momentum flux is
$\{\!\{v\}\!\}$ times the total mass flux plus a pressure mean, and the
kinetic part of $f_E$ is $\big(\{\!\{v\}\!\}^2-\tfrac12\{\!\{v^2\}\!\}\big)\sum_kf_{\rho_k}=\tfrac12v^-v^+\sum_kf_{\rho_k}$,
the kinetic-energy-preserving structure of the previous section *(compiler
check, not in the sources)*; the authors state the KEP property by citing
Ranocha, without showing it (end of §3).

With EC volume and surface fluxes and no stabilization, a smooth periodic
five-species problem keeps the global entropy rate at order $10^{-5}$ up to
$t=0.1$ instead of machine zero. The authors attribute the residual to the
$\sim10^{-7}$ tolerance of the Newton inversion from energy to temperature
in Mutation++, without varying the tolerance (§4.4, Fig. 4). The flux is
the volume flux of their entropy-stable [DGSEM](/methods/dgsem.md) with
subcell blending.

## Multicomponent Euler

Renac (2021) derives a new EC flux for a mixture of $n_c$ polytropic ideal
gases in thermal and mechanical equilibrium, written in the variables
$(\rho Y,\rho,\rho v,E)$ (Lemma 3.1, Eq. (24);
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).
Page-local symbols: mass fractions $Y_i$, $i<n_c$; species heat capacities
$C_{v,i}$ and gas constants $r_i=(\gamma_i-1)C_{v,i}$; mixture gas constant
$r(Y)$; and $\rho_{n_c}=\rho\,r(Y)/r_{n_c}$ the density of the last
component. With $\tilde p=\{\!\{p/T\}\!\}/\{\!\{1/T\}\!\}$ (page-local), the flux
$h=f^{\mathrm{ec}}$ in direction $n$ is

$$\begin{aligned}
h_\rho&=\{\!\{\rho\}\!\}_{\log}\{\!\{v\cdot n\}\!\},\qquad h_{\rho Y_i}=\frac{r_{n_c}\big(\{\!\{\rho_{n_c}\}\!\}_{\log}-\{\!\{\rho\}\!\}_{\log}\big)}{\{\!\{r(Y)\}\!\}-r_{n_c}}\{\!\{Y_i\}\!\}\{\!\{v\cdot n\}\!\},\\
h_{\rho v}&=h_\rho\{\!\{v\}\!\}+\tilde p\,n,\\
h_E&=\sum_{i<n_c}\frac{C_{v,i}-C_{v,n_c}}{\{\!\{1/T\}\!\}_{\log}}h_{\rho Y_i}+\Big(\frac{C_{v,n_c}}{\{\!\{1/T\}\!\}_{\log}}+\tfrac12v^-\cdot v^+\Big)h_\rho+\tilde p\,\{\!\{v\}\!\}\cdot n .
\end{aligned}$$

- **Cost.** It needs three [logarithmic means](/operators/logarithmic-mean.md),
  of $\rho_{n_c}$, $\rho$ and $1/T$, for any $n_c$. The alternative of
  Gouasmi et al., re-derived in App. B (Eq. (B.1)), builds each partial
  flux from the logarithmic mean of its own component density and needs
  $n_c+1$. Renac counts three means as cheaper for $n_c>2$ and less exposed
  to floating-point exceptions (Remark 3.1).
- **Kinetic energy.** The flux is formally kinetic-energy preserving in
  Jameson's sense, a property that "can fail discretely" (Remark 3.2;
  [kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
- **One component.** For $n_c=1$ the flux reduces to the Chandrashekar flux
  *(compiler check, not in the sources: $p/T=\rho r_1$ gives
  $\tilde p=r_1\{\!\{\rho\}\!\}/\{\!\{1/T\}\!\}$, and
  $\{\!\{v\}\!\}\cdot\{\!\{v\}\!\}-\tfrac12\{\!\{\lvert v\rvert^2\}\!\}=\tfrac12v^-\cdot v^+$)*.

## Moving curvilinear meshes: stiffened gas and relativistic MHD

[Duan & Tang (2022)](/sources/duan-2022.md) and
[Li, Duan & Tang (2022c)](/sources/li-2022-c.md) work in time-dependent
curvilinear coordinates ([adaptive moving mesh](/methods/adaptive-moving-mesh.md)).
The sufficient condition for an EC flux $\hat F_k$ in computational
direction $k$ weights the jumps of the page-local entropy potential
$\phi=w\cdot u-\eta$ and of the flux potentials with averaged metric terms
(Duan & Tang, Def. 3.1, Eq. (3.1); Li, Duan & Tang, Prop. 3.1, Eq. (3.5)).
For relativistic MHD in the symmetrizable form of Wu & Shu, Duan & Tang's
condition carries the extra term
$-\sum_j\{\!\{J\partial_{x_j}\xi_k\}\!\}\{\!\{B_j\}\!\}[\![\Phi]\!]$ of the
non-conservative source, page-local $\Phi$ the degree-one homogeneous
function of the entropy variables whose gradient multiplies
$\nabla\cdot B$ (Eqs. (2.4)–(2.5), (3.1)). It is met by
$\hat F_k=\{\!\{J\partial_t\xi_k\}\!\}\tilde u+\sum_j\{\!\{J\partial_{x_j}\xi_k\}\!\}f^{\mathrm{ec},(j)}$,
where $f^{\mathrm{ec},(j)}$ is a Cartesian EC flux (satisfying the
Cartesian condition with the source term, for MHD) and the page-local
"entropy-conservative state" $\tilde u$ satisfies
$[\![w]\!]\cdot\tilde u=[\![\phi]\!]$ (Duan & Tang, Eqs. (3.2)–(3.3);
Li, Duan & Tang, Eqs. (3.11)–(3.12)). The mesh motion enters only through
$\tilde u$. Duan & Tang prove that the resulting scheme is entropy
conservative (Thm. 3.2), which is the proof Li, Duan & Tang defer to them.

**Relativistic MHD.** Duan & Tang take the Cartesian relativistic-MHD EC
flux from their earlier DG work and derive the new state $\tilde u$ in
arithmetic and [logarithmic means](/operators/logarithmic-mean.md) of the
rest-mass density $\rho$, of $\rho/p$, of the Lorentz factor $W$ and of
the four-velocity and four-magnetic-field components (§3.1; its mass
component is $\{\!\{\rho\}\!\}_{\log}\{\!\{W\}\!\}$). The entropy pair is
$\eta=-\rho W s/(\gamma-1)$, $F^{(j)}_\eta=\eta v_j$ (Eq. (2.3);
[relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)).

For one stiffened gas, $p=\rho r_{\mathrm g}T-p_\infty$ with page-local gas
constant $r_{\mathrm g}$ and heat capacity $c_v$, and $p_\infty$ the
stiffened-gas constant $p_{\infty,k}$ of the registry for the single phase
([stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)),
they write the jumps of $w$, $\phi$ and $\psi$ in the parameter vector
$(\rho,v,1/T)$ with the product rule and the logarithmic mean (Eq. (3.15)).
The resulting flux in the first direction is (§3.3.1)

$$\begin{aligned}
f^{\mathrm{ec}}_\rho&=\{\!\{\rho\}\!\}_{\log}\{\!\{v_1\}\!\},\qquad f^{\mathrm{ec}}_{\rho v_m}=\{\!\{v_m\}\!\}f^{\mathrm{ec}}_\rho+\delta_{m1}\Big(\frac{r_{\mathrm g}\{\!\{\rho\}\!\}}{\{\!\{1/T\}\!\}}-p_\infty\Big),\\
f^{\mathrm{ec}}_E&=\Big(\frac{c_v}{\{\!\{1/T\}\!\}_{\log}}-\tfrac12\sum_m\{\!\{v_m^2\}\!\}\Big)f^{\mathrm{ec}}_\rho+\sum_m\{\!\{v_m\}\!\}f^{\mathrm{ec}}_{\rho v_m}+p_\infty\{\!\{v_1\}\!\}.
\end{aligned}$$

With $p_\infty=0$ it is the Chandrashekar flux *(compiler check, not in the
sources: $\rho/(2p)=1/(2r_{\mathrm g}T)$ turns Chandrashekar's
$\{\!\{\rho\}\!\}/(2\{\!\{\rho/(2p)\}\!\})$ and $1/(2(\gamma-1)\{\!\{\rho/(2p)\}\!\}_{\log})$ into the
terms above)*. For two components they give the analogous flux with the
logarithmic means of both partial densities (§3.3.2). Fluxes in other
directions follow from rotational invariance,
$f(u^-,u^+;\varphi_1,\varphi_2)=T_{\mathrm{rot}}^{-1}f^{\mathrm{ec}}(T_{\mathrm{rot}}u^-,T_{\mathrm{rot}}u^+)$
with page-local rotation $T_{\mathrm{rot}}$ and angles $\varphi_1,\varphi_2$,
because $w(T_{\mathrm{rot}}u)=T_{\mathrm{rot}}w(u)$ (Eqs. (3.19)–(3.20)). High
order comes from the LeFloch–Mercier–Rohde combination of the two-point
flux over wider stencils, applied to the metric terms as well (Li, Duan &
Tang, Eqs. (3.6)–(3.7); Duan & Tang, Prop. 3.1, who prove order
$2n_{\mathrm o}$ for $n_{\mathrm o}$ two-point terms, page-local;
[flux differencing](/methods/flux-differencing.md),
[TeCNO schemes](/methods/tecno-scheme.md)).

## Relativistic hydrodynamics with three velocity components

[Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) build
entropy-stable finite differences for the two-fluid relativistic plasma
equations, two special-relativistic fluids (ions and electrons) coupled to
Maxwell's equations through Lorentz-force sources
([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)).
Each fluid block gets the EC flux of the authors' earlier one-dimensional
construction, extended to three velocity components (§4.1.1, Eqs. (18)–(19)).
Page-local symbols, per species: $W$ the Lorentz factor (registry §5),
$\mathsf u_d=Wv_d$ the spatial four-velocity, so $W^2=1+\sum_d\mathsf u_d^2$,
and $b=\rho/p$. The entropy pair is $\eta=-\rho Ws/(\gamma-1)$,
$F^{(d)}_\eta=\eta v_d$, with entropy variables
$w=\big(\tfrac{\gamma-s}{\gamma-1}+b,\ \mathsf u_1b,\ \mathsf u_2b,\ \mathsf u_3b,\ -Wb\big)$
and potentials $\psi^{(d)}=\rho\mathsf u_d$ (Eqs. (13)–(14), from the earlier
work). Using the logarithmic mean, the product rule
$[\![ab]\!]=\{\!\{a\}\!\}[\![b]\!]+\{\!\{b\}\!\}[\![a]\!]$ and
$[\![W]\!]=\sum_d\{\!\{\mathsf u_d\}\!\}[\![\mathsf u_d]\!]/\{\!\{W\}\!\}$, they
write $[\![w]\!]$ in the jumps of $(\rho,b,\mathsf u_1,\mathsf u_2,\mathsf u_3)$
and match coefficients in Tadmor's condition, following Chandrashekar. The
flux in the first direction, components (mass, three momenta, energy), is

$$\begin{aligned}
f_D&=\{\!\{\rho\}\!\}_{\log}\{\!\{\mathsf u_1\}\!\},\qquad
f_E=\frac{-\{\!\{W\}\!\}\Big(k\,\{\!\{\rho\}\!\}_{\log}\{\!\{\mathsf u_1\}\!\}+\{\!\{\mathsf u_1\}\!\}\dfrac{\{\!\{\rho\}\!\}}{\{\!\{b\}\!\}}\Big)}{\sum_d\{\!\{\mathsf u_d\}\!\}^2-\{\!\{W\}\!\}^2},\\
f_{M_1}&=\frac{\{\!\{\mathsf u_1\}\!\}}{\{\!\{W\}\!\}}f_E+\frac{\{\!\{\rho\}\!\}}{\{\!\{b\}\!\}},\qquad
f_{M_d}=\frac{\{\!\{\mathsf u_d\}\!\}}{\{\!\{W\}\!\}}f_E\ \ (d=2,3),\qquad
k=\frac{1}{(\gamma-1)\{\!\{b\}\!\}_{\log}}+1 .
\end{aligned}$$

*(Compiler check, not in the sources: the momentum and energy components
follow from the printed coefficient matching on p. 9 of the arXiv v2; the
first momentum component is printed as $\frac1{\{\!\{b\}\!\}}\big(\frac{\{\!\{b\}\!\}\{\!\{\mathsf u_1\}\!\}}{\{\!\{W\}\!\}}f_E+\{\!\{\rho\}\!\}\big)$,
which is the form above. The term $\{\!\{\rho\}\!\}/\{\!\{b\}\!\}$ in $f_{M_1}$
stands where the Chandrashekar flux has its pressure mean.)* The scheme with
this flux is second-order and entropy conservative (Thm. 4.2). Fourth order
uses the LeFloch–Mercier–Rohde combination
$\tfrac43f^{\mathrm{ec}}(u_i,u_{i+1})-\tfrac16\big[f^{\mathrm{ec}}(u_{i-1},u_{i+1})+f^{\mathrm{ec}}(u_i,u_{i+2})\big]$;
only even orders exist, so an odd target order $q$ takes the order-$(q+1)$
flux (Remarks 4.1–4.2).

The entropy-stable flux subtracts
$\tfrac12\tilde R\Lambda\tilde R^\top[\![\tilde w]\!]$, with $\tilde R$ the
right eigenvectors scaled after Barth so that
$\partial u/\partial w=\tilde R\tilde R^\top$, given in closed form for the
3D relativistic block (App. B.2), $\Lambda$ the largest wave speed times the
identity (a Rusanov-type choice), and $[\![\tilde w]\!]$ the jump of the
entropy variables recovered from an ENO reconstruction of the scaled
variables $\tilde R^\top w$ (Eq. (22),
[TeCNO schemes](/methods/tecno-scheme.md)). The paper calls the operator
"similar to the Roe diffusion operator" (§4.1.2). The Maxwell block, which
is linear, uses a plain Rusanov flux with minmod or WENO reconstruction
(§4.2); its discretization does not enter the fluid entropy estimate
([entropy stability](/properties/entropy-stability.md)).

## GLM-MHD with non-conservative terms

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) use the EC flux
of Derigs et al. for GLM-MHD (App. A, Eqs. (102)–(103)). Its mass flux is
$\{\!\{\rho\}\!\}_{\log}\{\!\{v_1\}\!\}$, its energy flux carries
$1/\{\!\{\rho/(2p)\}\!\}_{\log}$, and the induction and cleaning components
are products of arithmetic means. It is EC only together with the surface
non-conservative term, in the generalized Tadmor condition that includes
the Powell and GLM terms (Eq. (51);
[entropy stability](/properties/entropy-stability.md),
[flux differencing](/methods/flux-differencing.md)).

## Ideal MHD with the Godunov–Powell term

The conservative ideal MHD system is not symmetrizable. Adding the
[Godunov–Powell term](/definitions/godunov-powell-source-term.md)
$(\nabla\cdot B)\,(0,B,v,v\cdot B)^\top$ to the left-hand side makes it
symmetrizable by the entropy variables of $\eta=-\rho s/(\gamma-1)$.
[Liu et al. (2025b)](/sources/liu-2025-b.md) (§2, Eqs. (2.7)–(2.9)) and
[Liu et al. (2025c)](/sources/liu-2025-c.md) (§2, Eq. (7)) recall this
after Godunov. With $w=\eta'(u)$ the term is $\phi_{\mathrm G}'(w)$ for the
degree-one homogeneous function

$$\phi_{\mathrm G}=\frac{\rho}{p}\,(v\cdot B),\qquad w=\Big(\frac{\gamma-s}{\gamma-1}-\frac{\rho\lvert v\rvert^2}{2p},\ \frac\rho pv,\ \frac\rho pB,\ -\frac\rho p\Big)$$

(page-local $\phi_{\mathrm G}$, the sources' $\phi$ with $\beta=\rho/(2p)$;
components in Liu et al. (2025b)'s order $(\rho,\rho v,B,E)$). The
entropy-conservation condition gains a term in the jump of
$\phi_{\mathrm G}$. Liu et al. (2025b) write it (Def. 3.1, Eq. (3.12)) as

$$[\![w]\!]\cdot f^{\mathrm{ec}}+[\![\phi_{\mathrm G}]\!]\,\{\!\{B_1\}\!\}=[\![\psi^{(1)}_{\mathrm G}]\!],\qquad \psi^{(1)}_{\mathrm G}=\rho v_1+\frac{\rho}{2p}v_1\lvert B\rvert^2,$$

with page-local $\psi^{(1)}_{\mathrm G}=w\cdot f^{(1)}+\phi_{\mathrm G}B_1-F_\eta^{(1)}$.
Entropy stability is the same expression with $\le$ (Def. 3.2). Liu et
al. (2025c) print (Def. 2, Eq. (9); with $\le$ for entropy stability,
Eq. (10))

$$[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi^{(1)}]\!]-[\![\phi_{\mathrm G}]\!]\,\{\!\{B_1\}\!\},\qquad \psi^{(1)}=w\cdot f^{(1)}-F_\eta^{(1)},$$

with the registry's potential $\psi$, which has no $\phi_{\mathrm G}B_1$ term
(§2). The two papers define the potential differently: Liu et al.
(2025b)'s $\psi^{(1)}_{\mathrm G}$ includes $\phi_{\mathrm G}B_1$. Both use the
Chandrashekar–Klingenberg flux and write it out in full. Its mass flux is
$\{\!\{\rho\}\!\}_{\log}\{\!\{v_1\}\!\}$, and its energy flux carries
$1/\{\!\{\rho/(2p)\}\!\}_{\log}$. The momentum and induction components are
products of arithmetic means, the induction ones weighted by $\rho/(2p)$
(Liu et al. (2025b), §3.1; Liu et al. (2025c), App. A.1).

The surface fluxes differ:

- **Entropy-variable Lax–Friedrichs.** Liu et al. (2025b) take
  $f^{\mathrm{ec}}-\tfrac12a\,\mathcal H[\![w]\!]$. Here $\mathcal H$ is the
  discrete entropy Jacobian of Derigs et al. (page-local), with
  $[\![u]\!]=\mathcal H[\![w]\!]$, so the flux reduces to Lax–Friedrichs.
  They recommend the local $a=\max(\lvert\lambda^-_{\max}\rvert,\lvert\lambda^+_{\max}\rvert)$
  (Eq. (3.14); [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).
- **HLL.** Liu et al. (2025c) use HLL with the three-wave relaxation
  speed estimates of Bouchut, Klingenberg & Waagan. They state, citing
  the literature, that HLL and Lax–Friedrichs are entropy stable when the
  speed estimates bound the true ones (App. A.2;
  [HLL-type solvers](/methods/hll-riemann-solvers.md)).

Liu et al. (2025c) avoid the non-conservative term in the scheme. They
discretize the conservative form and show that the $\phi_{\mathrm G}$ terms
cancel exactly when the nodal field is globally divergence-free
([entropy stability](/properties/entropy-stability.md),
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

## From EC to entropy-stable fluxes

An EC flux becomes entropy stable when a dissipation with a provable sign
is subtracted.

- **Dissipation on the entropy variables.** Rueda-Ramírez et al. (2021)
  write $h=f^{\mathrm{ec}}-\tfrac12R\lvert\Lambda\rvert R^{-1}\frac{\partial u}{\partial w}[\![w]\!]$,
  page-local $\Lambda$ the eigenvalue matrix, with $\partial u/\partial w$ at
  a mean state and Barth's eigenvector scaling, so the production is a
  negative quadratic form in $[\![w]\!]$ (Eqs. (57)–(60)). They state,
  after Derigs et al., that the "Lax–Friedrichs type" dissipation
  $\tfrac12\mathcal D[\![u]\!]$ of their Eq. (52), used with the Roe-type
  matrix $\mathcal D=R\lvert\Lambda\rvert R^{-1}$ (Eq. (53)), is not entropy
  stable for MHD *(compiler check, not in the sources: for the scalar case
  $\mathcal D=aI$, $a\ge0$, the production $-\tfrac12a[\![w]\!]\cdot[\![u]\!]$ is
  non-positive for a convex entropy; see [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md))*.
- **Roe-type scalar dissipation.** Renac (2021) uses the author's EC flux minus a
  scalar multiple of the largest wave speed times a matrix applied to
  $[\![w]\!]$, with no dissipation on the mass fractions (App. D, Eq. (D.1)),
  and proves it entropy stable (App. D.1). Renac finds it less robust than
  the relaxation flux of the paper.
- **Reconstructed dissipation.** Applying the dissipation to reconstructed
  jumps with the sign property gives high-order entropy-stable fluxes
  ([TeCNO schemes](/methods/tecno-scheme.md)). Duan & Tang (2022) use a
  scalar maximal wave speed (including the mesh velocity) times the scaled
  eigenvector matrix, not a Roe-type $R\lvert\Lambda\rvert R^{-1}$ (§4).
- **Dissipation on reconstructed jumps, third-order WENO.**
  [Charles & Ray (2025)](/sources/charles-2025.md) use the fourth-order
  LeFloch–Mercier–Rohde combination of Tadmor-type fluxes. For
  advection the base flux is the arithmetic mean, for Burgers
  $(u_i^2+u_iu_{i+1}+u_{i+1}^2)/6$, and for Euler Chandrashekar's
  kinetic-energy-preserving EC flux. They add Roe-type dissipation on
  jumps reconstructed with [sign-preserving WENO](/methods/sign-preserving-weno.md)
  (§2, Eqs. (5)–(11), (33)–(34); arXiv v2).
- **Correction instead of flux design.** Abgrall et al. (2022) avoid the
  construction of an EC flux altogether: an element-wise
  [entropy correction term](/methods/entropy-correction-term.md) makes any
  baseline scheme entropy conservative or dissipative (§5).

## Scalar case: the KPP flux

For a scalar law with $\eta=\tfrac12u^2$, the entropy variable is $w=u$,
and Tadmor's condition fixes the flux whenever $u^-\ne u^+$:
$f^{\mathrm{ec},(d)}=[\![\psi^{(d)}]\!]/[\![u]\!]$, with
$f^{\mathrm{ec},(d)}=f^{(d)}(u^-)$ if $u^-=u^+$. For the KPP flux
$f=(\sin u,\cos u)$, the potentials are $\psi=(-\cos u,\sin u)$
(Rueda-Ramírez et al. (2022), Eqs. (39)–(40)). The authors call it "the unique
two-point entropy conservative flux". Uniqueness holds because, for a scalar,
the EC condition is one linear equation in one unknown *(compiler check, not
in the sources)*. It does not carry over to systems. Abgrall et al. (2022)
state the same uniqueness for a scalar law and a fixed entropy,
$f^{\mathrm{ec}}=[\![\psi]\!]/[\![w]\!]$, and conclude that the surface
fluxes of DG cannot in general make several entropies conserved at once;
Osher's E-schemes satisfy all entropy inequalities but are at most first
order (Remark 3.3).

**Burgers.** For $f=u^2/2$ and $\eta=u^2/2$,
[Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
write the interface flux as
$\tfrac12\big(\tfrac12(u^-)^2+\tfrac12(u^+)^2\big)-\lambda_{\mathrm F}(u^+-u^-)$
with page-local dissipation coefficient $\lambda_{\mathrm F}$. With their
split form at weight $2/3$, the interface energy contribution is
$(u^+-u^-)^2\big(\tfrac1{12}(u^+-u^-)-\lambda_{\mathrm F}\big)$, so the
scheme is energy stable for $\lambda_{\mathrm F}\ge\tfrac1{12}(u^+-u^-)$
and energy conservative at equality; local Lax–Friedrichs,
$\lambda_{\mathrm F}=\tfrac12\max(\lvert u^-\rvert,\lvert u^+\rvert)$, satisfies the bound
(Eqs. (47)–(50)). The energy-conservative choice is
$\big((u^-)^2+u^-u^++(u^+)^2\big)/6$, which equals Tadmor's
$[\![u^3/6]\!]/[\![u]\!]$ *(compiler check, not in the sources)*.

## The logarithmic mean and its evaluation

The operator, its identity and the fluxes that use it are collected on
[logarithmic mean](/operators/logarithmic-mean.md).

The logarithmic mean
$\{\!\{a\}\!\}_{\log}=[\![a]\!]/[\![\ln a]\!]$ (Ismail–Roe) is ill-conditioned
when $a^-\approx a^+$. Ranocha et al. (2023), §3.1, give division-reduced
algorithms. Let page-local $\varsigma=\big((a^+-a^-)/(a^++a^-)\big)^2$, computed with
one division as $\big(a^-(a^--2a^+)+(a^+)^2\big)/\big(a^-(a^-+2a^+)+(a^+)^2\big)$.

- If $\varsigma<10^{-4}$ (64-bit), Algorithm 2 returns
  $\{\!\{a\}\!\}_{\log}\approx(a^-+a^+)/\big(2+\varsigma(2/3+\varsigma(2/5+\varsigma\,2/7))\big)$.
- Otherwise it returns $(a^+-a^-)/\ln(a^+/a^-)$.
- Algorithm 3 computes the inverse logarithmic mean the same way.

The series follows from $\ln(a^+/a^-)=2\operatorname{artanh}\sqrt\varsigma$
*(compiler check, not in the sources)*. The paper's variant (3.6)
multiplies by $\tfrac12+\varsigma\big(-\tfrac16+\varsigma(-\tfrac2{45}-\varsigma\tfrac{22}{945})\big)$.
These are the Taylor coefficients of
$\tfrac12/(1+\varsigma/3+\varsigma^2/5+\varsigma^3/7)$ to $O(\varsigma^3)$
*(compiler check, not in the sources: expand $1/(1+s)$)*. It gives no
significant performance difference on the authors' hardware (§3.1).

Logarithms are expensive. On a 2019 laptop, $\ln x+\ln y$ took
$11.5\pm3.8$ ns against $1.7\pm0.4$ ns for $2x+3y$. Precomputing $\ln\rho$
and $\ln p$ per node cuts the logarithm count from $O(d(N+1)^{d+1})$ to
$O((N+1)^d)$ per element. The resulting speed-up depends on the data: about
10 % for the isentropic vortex, 25–55 % for sinusoidal data and 60–75 % for
random data (§7.2, Fig. 6). In the flux microbenchmarks, LLF and HLL
surface fluxes cost between the Shima and the Ranocha fluxes (§4.2,
Table 2).

## Qualifications

- Ranocha et al. (2023) do not state the entropy sign convention
  explicitly. With a convex mathematical entropy, ED means entropy
  production $\le0$, the convention used here and in the registry
  ($\eta=-\rho s/(\gamma-1)$ for Euler).
- In Ranocha et al.'s Def. 2.4, directional fluxes take unit normals, but
  the curvilinear volume term evaluates them at unnormalized averaged
  contravariant vectors (Eq. (2.19)). The scaling is linear, as their
  rotation Algorithm 4 makes explicit.
- Abgrall et al. (2022) argue that the construction of EC fluxes hinges on
  the structure of a calorically perfect gas, and that for temperature-
  dependent or tabulated heat capacities the algebra becomes case by case
  (§1, §5). The EC fluxes on this page are consistent with that scope:
  Renac's mixture of polytropic gases and Li, Duan & Tang's stiffened gas
  both have constant heat capacities *(compiler check, not in the
  sources)*.
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) deliberately
  leave Tadmor-type EC fluxes out of their split-form study: they need the
  logarithmic mean, are hard to recast as classical finite-difference
  split forms, need protection against division by zero and cost more
  (§1, citing Tamaki et al.). They state that their induced-equation
  entropy analysis is "basically equivalent" to Tadmor's theory with
  $\eta=-\rho s$, without proving it (§4.2.5). Their later note (De
  Michele & Coppola (2023b)) approaches the same fluxes from the other
  side, with algebraic truncations of the logarithmic means.
- Peyvan et al. print the stable form of the exponential mean as
  $\frac{\{\!\{a\}\!\}}{e^{T^{\mathrm v}_k\{\!\{a\}\!\}}}\frac{\mathsf j_a}{\sinh(T^{\mathrm v}_k\mathsf j_a)}$
  (Eq. (86)); the argument of $\sinh$ must be $T^{\mathrm v}_k\{\!\{a\}\!\}\mathsf j_a$,
  which their Eq. (87) uses. The truncation error of their series, which
  has only even powers, is $O(x^8)$, not the printed $O(x^9)$ *(compiler
  check, not in the sources)*.
- Peyvan et al.'s Eq. (62) prints a negative vibrational heat capacity;
  the derivative of $T^{\mathrm v}_k/(e^{T^{\mathrm v}_k/T}-1)$ in $T$ is
  positive, and their entropy (64) follows from the positive sign
  *(compiler check, not in the sources)*. Their entropy variables (66)
  differ from the Gibbs form by a constant $r_k$, which does not change
  the jumps or the flux.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Defs. 2.4–2.5, §2, §3.1 Algorithms 1–3 Eqs. (3.3)–(3.6), §3.2 Eqs. (3.7)–(3.11), §4.2 Table 2, §7.2 Fig. 6.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §4, §5.1 Eqs. (39)–(40), §5.2, §5.3.
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §5.2 Observation 7, §5.4, Table 1.
- [Renac (2021)](/sources/renac-2021.md) — §3.1 Eqs. (19)–(24), Lemma 3.1, Remarks 3.1–3.2, App. B Eq. (B.1), App. D Eq. (D.1) (arXiv v3).
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — Prop. 3.1 Eq. (3.5), Eqs. (3.6)–(3.7), (3.11)–(3.20), §3.3.1–3.3.2 (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §3.3.1 Eqs. (51)–(60), App. A Eqs. (102)–(103) (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §1, Remarks 2.5–2.7 Eqs. (27)–(29), Remark 3.3, §3.3 Eq. (40), §4.2.2, §5 Eq. (45), App. A.3 (arXiv v4).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2 Eqs. (2.3)–(2.6), §3.1 Def. 3.1 Eqs. (3.1)–(3.3), Prop. 3.1, Thm. 3.2 Eqs. (3.20)–(3.21), §4 (arXiv v1).
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §3.1.2 Eqs. (46)–(50) (arXiv v1).
- [Edoh (2022)](/sources/edoh-2022.md) — §2 Eqs. (3)–(6), §3.2 Remark 4, Table 4.
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3, §3.5 Eqs. (58)–(62), Table 1, §4.1 (arXiv v1).
- [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) — §4.1.1 Eqs. (13)–(19), Thm. 4.2, Remarks 4.1–4.2, §4.1.2 Eqs. (20)–(22), §4.2, App. B.2 (arXiv v2).
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §1, §4.2.5 (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — §1–§6, Eqs. (1)–(15), Figs. 1–2 (arXiv v2).
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §1, §3 Eqs. (60)–(91), §4.4 Fig. 4 (arXiv v1).
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §2 Eqs. (2.7)–(2.9), §3.1 Defs. 3.1–3.2 Eqs. (3.12)–(3.14).
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §2 Eq. (7), §3.1 Defs. 2–3 Eqs. (9)–(10), Thm. 1, App. A.1–A.2.
- [Charles & Ray (2025)](/sources/charles-2025.md) — §2 Eqs. (5)–(11), §5 Eqs. (33)–(34) (arXiv v2).
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §2.1.1 Eqs. (19), (25)–(26), §3.1.1 Figs. 1–2.
