---
type: Method
title: "Entropy-conservative and kinetic-energy-preserving two-point fluxes"
description: "Two-point fluxes that satisfy Tadmor's jump condition conserve entropy, and entropy-dissipative fluxes satisfy it as an inequality; the page states the condition in Cartesian, directional, moving-mesh and non-conservative form, gives the Ranocha, Shima, multicomponent, stiffened-gas, GLM-MHD and KPP fluxes, the dissipation that makes them entropy stable, the relativistic-MHD case, the Burgers flux and the logarithmic mean."
status: established
aliases: [EC flux, entropy-conservative flux, entropy-dissipative flux, ED flux, Tadmor flux, KEP flux, KEEP flux, Ranocha flux, Shima flux]
tags: [entropy-stable, kinetic-energy-preserving, numerical-flux, dg]
timestamp: 2026-10-22T18:00:00Z
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
([Edoh (2022)](/sources/edoh-2022.md), Eqs. (3)–(6); his $\tilde F(a,b)$).
Edoh states that every kinetic-energy-preserving split form he knows
implies a kinetic-energy flux built on $(\!(v_m;v_m)\!)=v_m^-v_m^+$, a
geometric-type average of the velocities on the two sides, while his
Div-rot splitting squares one variable: its kinetic-energy flux is
$\tfrac12(\!(\sqrt\rho\,v_j;\sqrt\rho\,\lvert v\rvert^2)\!)$ in direction $j$; he argues this promotes
realizability when the interface velocities change sign, and that it lets
the total-energy flux be exactly the internal-energy flux plus the
kinetic-energy flux (Remark 4, Table 4). The realizability argument is
stated, not tested. The splittings are on
[split convective forms](/methods/split-convective-forms.md).

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
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) work in time-dependent
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

## From EC to entropy-stable fluxes

An EC flux becomes entropy stable when a dissipation with a provable sign
is subtracted.

- **Dissipation on the entropy variables.** Rueda-Ramírez et al. (2021)
  write $h=f^{\mathrm{ec}}-\tfrac12R\lvert\Lambda\rvert R^{-1}\frac{\partial u}{\partial w}[\![w]\!]$,
  page-local $\Lambda$ the eigenvalue matrix, with $\partial u/\partial w$ at
  a mean state and Barth's eigenvector scaling, so the production is a
  negative quadratic form in $[\![w]\!]$ (Eqs. (57)–(60)). Plain
  $\tfrac12a[\![u]\!]$ is not entropy stable for MHD, as they recall from
  Derigs et al. (Eq. (52)).
- **Roe-type scalar dissipation.** Renac (2021) uses his EC flux minus a
  scalar multiple of the largest wave speed times a matrix applied to
  $[\![w]\!]$, with no dissipation on the mass fractions (App. D, Eq. (D.1)),
  and proves it entropy stable (App. D.1). He finds it less robust than
  his relaxation flux.
- **Reconstructed dissipation.** Applying the dissipation to reconstructed
  jumps with the sign property gives high-order entropy-stable fluxes
  ([TeCNO schemes](/methods/tecno-scheme.md)). Duan & Tang (2022) use a
  scalar maximal wave speed (including the mesh velocity) times the scaled
  eigenvector matrix, not a Roe-type $R\lvert\Lambda\rvert R^{-1}$ (§4).
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
$\tfrac12\big(\tfrac12(u^-)^2+\tfrac12(u^+)^2\big)-\lambda_{\mathrm s}(u^+-u^-)$
with page-local dissipation coefficient $\lambda_{\mathrm s}$. With their
split form at weight $2/3$, the interface energy contribution is
$(u^+-u^-)^2\big(\tfrac1{12}(u^+-u^-)-\lambda_{\mathrm s}\big)$, so the
scheme is energy stable for $\lambda_{\mathrm s}\ge\tfrac1{12}(u^+-u^-)$
and energy conservative at equality; local Lax–Friedrichs,
$\lambda_{\mathrm s}=\tfrac12\max(\lvert u^-\rvert,\lvert u^+\rvert)$, satisfies the bound
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

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Defs. 2.4–2.5, §2, §3.1 Algorithms 1–3 Eqs. (3.3)–(3.6), §3.2 Eqs. (3.7)–(3.11), §4.2 Table 2, §7.2 Fig. 6.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §4, §5.1 Eqs. (39)–(40), §5.2, §5.3.
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §5.2 Observation 7, §5.4, Table 1.
- [Renac (2021)](/sources/renac-2021.md) — §3.1 Eqs. (19)–(24), Lemma 3.1, Remarks 3.1–3.2, App. B Eq. (B.1), App. D Eq. (D.1) (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Prop. 3.1 Eq. (3.5), Eqs. (3.6)–(3.7), (3.11)–(3.20), §3.3.1–3.3.2 (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §3.3.1 Eqs. (51)–(60), App. A Eqs. (102)–(103) (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §1, Remarks 2.5–2.7 Eqs. (27)–(29), Remark 3.3, §3.3 Eq. (40), §4.2.2, §5 Eq. (45), App. A.3 (arXiv v4).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2 Eqs. (2.3)–(2.6), §3.1 Def. 3.1 Eqs. (3.1)–(3.3), Prop. 3.1, Thm. 3.2 Eqs. (3.20)–(3.21), §4 (arXiv v1).
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §3.1.2 Eqs. (46)–(50) (arXiv v1).
- [Edoh (2022)](/sources/edoh-2022.md) — §2 Eqs. (3)–(6), §3.2 Remark 4, Table 4.
