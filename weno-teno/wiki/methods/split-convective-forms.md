---
type: Method
title: "Split convective forms"
description: "Split forms write the convective terms of mass and momentum as weighted mixtures of divergence and advective forms; the page gives the Coppola–Veldman family and conditions, Edoh's rotational forms, De Michele and Coppola's flux form and energy splittings, the Burgers split of DG and FR, an optimized eight-point cubic split in a TENO hybrid, and the face and two-point fluxes."
status: established
aliases: [split forms, skew-symmetric form, Feiereisen splitting, Kennedy–Gruber splitting, KGP splitting, supraconservative discretization, dual-sided discretization, rotational form, Div-rot, Div-str, EMAC, Morinishi splitting, Rozema splitting, Ducros splitting, quadratic split, cubic split, quartic split, quintic split, Jameson–Pirozzoli form, KEEP scheme, energy-equation splitting]
tags: [kinetic-energy-preserving, finite-difference, finite-volume, multiphase, turbulence, low-dissipation]
timestamp: 2026-10-23T23:45:00Z
---

# Split convective forms

A **split form** rewrites a convective term with the product rule before
discretizing. The divergence form $\partial_x(\rho v\phi)$ is replaced by a
weighted mixture of algebraically equivalent forms. These forms differ only
discretely, and the choice decides which quadratic invariants the
semi-discretization conserves.
[Coppola & Veldman (2023)](/sources/coppola-2023.md) treat the model pair

$$\partial_t\rho+\partial_x(\rho v)=0,\qquad \partial_t(\rho\phi)+\partial_x(\rho v\phi)=0,$$

whose primary invariants are $\rho$ and $\rho\phi$ and whose secondary
(quadratic) invariant is $\tfrac12\rho\phi^2$. Here $\phi$ is a page-local
transported scalar, and $\phi=v$ gives momentum and the kinetic energy
$\kappa$ (§2.1, after Veldman). The source writes the operators with
$\nabla$; the 1D form is shown here.

## The split family

Mass (Eq. (7)) has two forms:

- divergence: $M^D=\partial_x(\rho v)$;
- advective: $M^A=v\,\partial_x\rho+\rho\,\partial_xv$.

Momentum (Eq. (8)) has five:

- $C^D\phi=\partial_x(\rho v\phi)$;
- $C^\phi\phi=\phi\,\partial_x(\rho v)+\rho v\,\partial_x\phi$;
- $C^v\phi=v\,\partial_x(\rho\phi)+\rho\phi\,\partial_xv$;
- $C^\rho\phi=\rho\,\partial_x(v\phi)+v\phi\,\partial_x\rho$;
- $C^L\phi=\rho\phi\,\partial_xv+\rho v\,\partial_x\phi+v\phi\,\partial_x\rho$.

The family (Eq. (9)) mixes them with page-local weights. The mass weight
$\zeta$ is the source's $\xi$. The momentum weights
$\mu_D,\mu_\phi,\mu_v,\mu_\rho,\mu_L$, summing to 1, are the source's
$\alpha,\beta,\gamma,\delta,\varepsilon$:

$$M=\zeta M^D+(1-\zeta)M^A,\qquad C=\mu_DC^D+\mu_\phi C^\phi+\mu_vC^v+\mu_\rho C^\rho+\mu_LC^L .$$

For central finite differences on uniform grids, the family is
kinetic-energy-preserving iff

$$\mu_D-\mu_L=\mu_\phi=\tfrac12\zeta,\qquad \mu_v=\mu_\rho=\tfrac12(1-\zeta)-\mu_L$$

(Eq. (10), the condition of Coppola et al. 2019, recalled). The named
members have $\mu_L=0$:

| $\zeta$ | name | face mass flux $m_{i+1/2}$ (Table 1) |
|---|---|---|
| 1 | Feiereisen | $\tfrac12(\rho_{i+1}v_{i+1}+\rho_iv_i)$ |
| 1/2 | Kennedy–Gruber, shown kinetic-energy-preserving by Pirozzoli (KGP) | $\tfrac14(\rho_i+\rho_{i+1})(v_i+v_{i+1})$ |
| 0 | Coppola et al. | $\tfrac12(\rho_iv_{i+1}+\rho_{i+1}v_i)$ |

All three take the momentum flux
$(m\phi)_{i+1/2}=\tfrac12m_{i+1/2}(\phi_i+\phi_{i+1})$. The case $\zeta=\mu_D=1$,
with the rest zero, is the pure conservation form (§2.2).

## Discrete conditions in matrix form

Coppola & Veldman discretize on periodic, possibly non-uniform 1D grids as
$V\frac{d}{dt}\phi+\mathcal C\phi=0$. Here $V$ (page-local, the source's
$H$) is the diagonal matrix of control volumes and $\mathcal C$ the
discrete convective matrix. Every operator is a banded matrix in the
circulant shift $\mathcal T$, $(\mathcal T\phi)_i=\phi_{i+1}$ (page-local,
the source's $E$). The advective terms use up to four derivative matrices:

- $D^m$ (the source's $D^{\rho u}$), acting on the mass flux;
- $D^0$;
- $D^\rho$, gradient-like;
- $D^v$ (the source's $D^u$), divergence-like.

Their results:

- **Mass** (Observation 4, Eq. (43)). The advective form
  $V\frac{d\rho}{dt}=-\big(\mathrm{diag}(\rho)D^vv+\mathrm{diag}(v)D^\rho\rho\big)$
  conserves mass, globally and locally, iff the *duality relation*
  $D^\rho=-(D^v)^\top$ holds. This is a discrete product rule. A
  directionally biased $D^v$ must be paired with an oppositely biased
  $D^\rho$. If $D^\rho=D^v$, duality forces skew-symmetry.
- **Momentum** (Observation 6, Eq. (58)). The generalized momentum operator
  conserves momentum iff $\mu_L=0$, $D^0=-(D^m)^\top$ and
  $D^\rho=-(D^v)^\top$. $\mu_L\ne0$ would need an exact discrete product
  rule, which no nonzero matrix satisfies. The proof of this
  incompatibility is not printed (§4.2).
- **Kinetic energy** (§5.3, Observation 8). The weight conditions of
  Eq. (10) together with the duality relations are necessary and
  sufficient. This extends the 2019 result from skew-symmetric operators on
  uniform meshes to non-uniform meshes and to dual, non-central operators.
  For $\mu_L=0$, energy conservation implies momentum conservation, which
  implies mass conservation. For $\mu_L\ne0$, energy conservation does not
  imply momentum conservation.
- **Supraconservative family** (Eq. (73)). With $\mu_L=0$ the weights
  reduce to $\mu_D=\mu_\phi=\tfrac12\zeta$, $\mu_v=\mu_\rho=\tfrac12(1-\zeta)$. The
  most general finite-difference scheme that conserves mass, momentum and
  kinetic energy then has two free operators, $D^m$ and $D^v$, and the
  parameter $\zeta$.

**Finite-volume equivalence** (Observation 5, Eq. (53); §5.4). Every split
discretization that conserves mass globally is a cell-centred
finite-volume scheme with an explicit face flux, mapped coefficient by
coefficient ([local conservation and flux form](/results/local-conservation-flux-form.md)).

- **Three-point stencils.** The energy-preserving finite-difference schemes
  and the three-point finite-volume schemes with linear fluxes are the
  same three-parameter family.
- **Wider stencils.** The finite-volume framework is strictly larger. Face
  products such as $\rho_{i-2}v_{i-1}$ have no advective
  finite-difference counterpart.

## Split face fluxes of products (Jain & Moin)

[Jain & Moin (2022)](/sources/jain-2022.md) write the split forms directly
as face fluxes of a second-order collocated scheme on a uniform grid,
$\partial_xq\approx(\hat q_{i+1/2}-\hat q_{i-1/2})/\Delta x$, with
$\overline{a}_{i+1/2}=\tfrac12(a_i+a_{i+1})$ the two-point average (§3.1,
Eqs. (38)–(41)). For a product $q=abc$ of three factors:

| form | face flux $\hat q_{i+1/2}$ |
|---|---|
| divergence | $\overline{abc}$ |
| quadratic split | $\overline{ab}\;\overline c$ |
| cubic split | $\overline a\;\overline b\;\overline c$ |

Jain & Moin take these splits from Blaisdell et al. and Kennedy &
Gruber, as they recall, and give their pointwise equivalents, e.g. the cubic split as the seven-term average of
$\delta(abc)$, $c\,\delta(ab)$, $a\,\delta(bc)$, $b\,\delta(ac)$,
$ab\,\delta c$, $bc\,\delta a$, $ac\,\delta b$ over $4\delta x$ (Eq. (42)).
They add **quartic** and **quintic** splits, the product of four or five
two-point averages, for the four- and five-factor products that the
interface-regularization terms of their two-phase model create
(Eqs. (40)–(41)).

Their single-phase choice is $\hat C=\overline\rho\,\overline v$ for mass
and $\hat M=\overline\rho\,\overline v\,\overline v$ for momentum
(Eq. (58)); these are the face fluxes of the Kennedy–Gruber row
($\zeta=1/2$) of the Coppola–Veldman table above *(compiler check, not in
the sources: $\overline\rho\,\overline v=\tfrac14(\rho_i+\rho_{i+1})(v_i+v_{i+1})$)*.
The divergence mass flux $\overline{\rho v}$ is the Feiereisen row
($\zeta=1$) *(compiler check, not in the sources)*. In their two-phase
Taylor–Green tests the divergence mass flux, even with a momentum and
kinetic-energy flux consistent with it, diverges, which they attribute to
aliasing (App. C, Table 2, Fig. 13). The internal-energy flux is where
the splits matter most for two phases: only the quadratic split
$\overline{\rho e}\;\overline v$ satisfies their interface-equilibrium
condition, while the cubic split $\overline\rho\,\overline e\,\overline v$
(Kennedy–Gruber, Kuya et al.) and Chandrashekar's harmonic-mean variant
violate it and diverge at density ratio 10 (Lemma 3.1, §4.1.2;
[kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
The full rule is that each internal-energy and enthalpy flux take the
same split as the mass or regularization flux it pairs with.

## Multi-component split and divergence forms (Fujiwara et al.)

[Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) carry the
KEEP-type face fluxes to the inviscid multi-component Euler equations in
$(\rho Y_k,\rho v,E)$ form ([multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)),
with the energy flux split, as in KEEP, into kinetic, internal and
pressure-work parts (§3.1, Eq. (17)). With $\overline a$ the two-point
average and page-local $\widehat{\rho Y_k}=\tfrac12(\mathsf w^-(\rho Y_k)_i+\mathsf w^+(\rho Y_k)_{i+1})$,
$\hat\rho$ the same for the density, $\mathsf G=1/(\gamma-1)$ of the mixture and the weights $\mathsf w^\pm$ (page-local, the source's $\phi^\pm$; node index $i$ for the source's $m$), their
two flux sets are (Table 1):

| face flux | FC/PE (S), split | FC/PE (D), divergence |
|---|---|---|
| species mass | $\widehat{\rho Y_k}\,\overline v$ | $\tfrac12\big(\mathsf w^-(\rho Y_kv)_i+\mathsf w^+(\rho Y_kv)_{i+1}\big)$ |
| momentum (convective) | $\hat\rho\,\overline v\,\overline v$ | $\tfrac12\big(\mathsf w^-(\rho vv)_i+\mathsf w^+(\rho vv)_{i+1}\big)$ |
| pressure | $\overline p$ | $\overline p$ |
| kinetic energy | $\hat\rho\,\overline v\,\tfrac12v_iv_{i+1}$ | $\tfrac12\big(\mathsf w^-(\rho v\tfrac{v^2}2)_i+\mathsf w^+(\rho v\tfrac{v^2}2)_{i+1}\big)$ |
| internal energy | $\overline{p\mathsf G}\,\overline v$ | $\overline{p\mathsf Gv}$ |
| pressure work | $\tfrac12(v_ip_{i+1}+v_{i+1}p_i)$ | $\overline{vp}$ |

The weights $\mathsf w^\pm$, built from the mixture molar mass and the density,
come from their pressure-equilibrium compatibility condition and tend to 1
where the composition is uniform; there the split set reduces to the
KEEP-PE scheme of Shima et al. and the divergence set to the standard
divergence scheme, with no sensor switching between them (§3.4). Its
kinetic-energy and momentum fluxes have the KEP structure
$\hat M=\hat C\,\overline v$, with $\hat C=\hat\rho\,\overline v$ the total mass flux, and kinetic-energy face flux $\hat K=\hat C\,\tfrac12v_iv_{i+1}$ of the
Jain & Moin conditions *(compiler check, not in the sources; the KEP
property of the multi-component scheme is not analysed in the paper)*.
Both sets preserve pressure equilibrium for constant initial velocity;
with a non-uniform velocity only the split set satisfies the extended
condition (Eqs. (55)–(59)), so the divergence set diverges in long runs
($t\approx3.8$ in their 1D test) while the split set shows no error growth
to $t=6$ and runs to $t=20$ (§4–5, Figs. 3–5;
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
This is a case where the split form, not the divergence form, is what
keeps a second-order central scheme stable. As with Jain & Moin, the
internal-energy flux is a quadratic split of $p\mathsf G$ times $\overline v$.

## Rotational-form splittings (Edoh)

[Edoh (2022)](/sources/edoh-2022.md) analyses split forms with
diagonal-norm finite-difference
[summation-by-parts operators](/operators/summation-by-parts-operator.md)
$D_j=M^{-1}Q_j$ in direction $j$, using their two-point-flux
representation ([flux differencing](/methods/flux-differencing.md)).
Page-local notation: $V_j=\mathrm{diag}(v_j)$ for nodal data, summation
over repeated indices, and the *splitting error operator*

$$\mathcal S_j(a,b)=AD_j\mathbf b+BD_j\mathbf a-D_jA\mathbf b,$$

which is telescoping ($\mathbf 1^\top M\mathcal S_j(a,b)=0$) and locally
of the order of the operator, a "zero-consistent" correction (Eq. (7)).

**Incompressible splittings** (Table 1, $D_jv_j=0$ for the
kinetic-energy statements):

| name | momentum convective term | kinetic-energy preserving |
|---|---|---|
| Div | $D_jV_jv_i$ | no |
| Prod | $V_jD_jv_i+V_iD_jv_j$ | no |
| EMAC-str (Charnyi et al.) | Prod $+\tfrac12\delta_{ij}\mathcal S_j(v_k,v_k)$ | no, discretely |
| Morinishi (skew-symmetric) | $\tfrac12\big(D_jV_jv_i+V_jD_jv_i+V_iD_jv_j\big)$ | yes |
| Div-rot (new) | Prod $-\tfrac12\delta_{ij}\mathcal S_j(v_k,v_k)$ | yes |
| Div-str (new) | $D_jV_jv_i+\tfrac12\delta_{ij}\mathcal S_j(v_k,v_k)$ | yes |

- **Derivation.** Writing the advective term with the antisymmetric part
  of the velocity gradient, $v_j\partial_jv_i=v_j(\partial_jv_i-\partial_iv_j)+\tfrac12\partial_i(v_jv_j)$,
  the rotational form $\omega\times v+\tfrac12\nabla\lvert v\rvert^2$ (Horiuti),
  and substituting into the product form gives Div-rot; the strain-rate
  analogue gives EMAC-str (Eqs. (13)–(14)). For a discretely solenoidal
  velocity Div-rot *is* the rotational form; earlier kinetic-energy-
  preserving splittings (Morinishi, Feiereisen, Kennedy–Gruber, Coppola,
  Rozema) reduce instead to the skew-symmetric form (§3.1). Edoh reads
  Div-rot as the advective form plus a zero-consistent correction, of
  the form $\tfrac12\mathcal S_i(v_k,v_k)$, to the static-pressure gradient
  (Remark 2).
- **Kinetic energy.** Div-rot is kinetic-energy preserving, with
  kinetic-energy flux $\tfrac12(\!(v_j;\lvert v\rvert^2)\!)$, but only in the
  summed multi-dimensional sense: the proof relabels indices under the
  double summation and does not hold component by component (Eq. (15),
  Remark 3). EMAC-str leaves an indefinite residual of the order of the
  operator, because the discrete product rule fails,
  $(\!(v_j;v_j)\!)\ne(\!(1;v_jv_j)\!)$ (Eq. (16)).
- **Div-str and the one-parameter family.** Div-str is twice Morinishi
  minus Div-rot, a kinetic-energy-preserving rendition of EMAC-str under
  SBP algebra that also preserves angular momentum (Eq. (17)). With
  page-local weight $\alpha_{\mathrm E}$,
  $\alpha_{\mathrm E}\,\text{Div-rot}+(1-\alpha_{\mathrm E})\,\text{Div-str}=\alpha_{\mathrm E}(V_iD_jv_j+V_jD_jv_i)+(1-\alpha_{\mathrm E})D_jV_jv_i+\tfrac{1-2\alpha_{\mathrm E}}2\delta_{ij}\mathcal S_j(v_k,v_k)$
  is a family of kinetic-energy-preserving splittings, Morinishi at
  $\alpha_{\mathrm E}=1/2$ (Eq. (18)).
- **Secondary invariants** (Table 2, App. A). Momentum is conserved a
  priori by all six; kinetic energy (for $D_jv_j=0$) by Morinishi, Div-rot
  and Div-str; angular momentum a priori only by Div and Div-str;
  vorticity (for a solenoidal field) by all six; helicity only by Div-rot;
  enstrophy by none.

**Compressible splittings** (Table 3). With page-local square-root-density
variables $\breve v_i=\sqrt\rho\,v_i$, applied in both the mass and the
momentum equations, compressible Div-rot reads

$$\text{mass: }\ \sqrt R\,D_j\breve v_j+\breve V_jD_j\sqrt{\boldsymbol\rho},\qquad \text{momentum: }\ \breve V_iD_j\breve v_j+\breve V_jD_j\breve v_i-\tfrac12\delta_{ij}\big[\mathcal S_j(\breve v_k,\breve v_k)-\mathcal S_j(\sqrt\rho,\breve v_kv_k)\big],$$

with $R=\mathrm{diag}(\rho)$; its two-point mass flux is
$(\!(\sqrt\rho;\breve v_j)\!)$, a geometric density average, and its
kinetic-energy flux $\tfrac12(\!(\breve v_j;v_i\breve v_i)\!)$. It is
kinetic-energy preserving without any solenoidal condition (Eq. (24)), and
Edoh calls it "the first analogue to the rotational form for compressible
flows". The compressible EMAC-str of Both et al. is not kinetic-energy
preserving under this discrete calculus (Eq. (25)). Compressible Div-str
is twice Rozema's splitting minus Div-rot, and the family
$\alpha_{\mathrm E}\,\text{Div-rot}+(1-\alpha_{\mathrm E})\,\text{Div-str}$
contains the cubic splitting of Rozema et al. at
$\alpha_{\mathrm E}=1/2$ (Eq. (26)).

Edoh contrasts this family with the one of Coppola et al., the convex
combinations of the Feiereisen and Coppola splittings with arithmetic
density averages, which contains Kennedy–Gruber at even weighting and does
not contain Rozema's splitting (§3.2). That family is the $\zeta$ family of
the table above ($\zeta=1$ Feiereisen, $\zeta=1/2$ Kennedy–Gruber, $\zeta=0$
Coppola) *(compiler check, not in the sources: Edoh does not cite
Coppola & Veldman 2023)*. The total energy is built as internal energy
plus the kinetic energy induced by mass and momentum, after Kuya et al.,
with the pressure work in product form; for Div-rot the total-energy flux
is exactly the sum of the internal- and kinetic-energy fluxes (Table 4,
Remark 4).

**Evidence** (Edoh, §4; sixth-order central differences, RK4):

- **Isentropic vortex**, about six points across the vortex, 100 vortex
  widths. Without filtering the divergence form fails within five widths
  and Div-rot within fifteen; Feiereisen and Kennedy–Gruber survive but
  are noisy. With solution filtering all are stable and Div-rot has the
  lowest density error; after 100 widths the minimum density is 0.6261
  (Div-rot), 0.5069 (Feiereisen) and 0.4490 (Kennedy–Gruber) against the
  exact 0.5479 (Figs. 1–2; [isentropic vortex](/benchmarks/isentropic-vortex.md)).
- **Taylor–Green vortex** at $\mathrm{Re}=1600$, $M_0=0.1$, $64^3$ to
  $192^3$ points. The divergence form is unstable on these grids (stable at
  $512^3$); Kennedy–Gruber and Div-rot are robust even severely
  under-resolved. At $64^3$ Div-rot shows larger density variability and
  numerical dissipation, which Edoh attributes to the aliasing of its
  product-form momentum term, but cleaner vortical structures (Figs. 3–4;
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)).

## Flux form with a pointwise weight, and the generalized kinetic-energy flux

[De Michele & Coppola (2023a)](/sources/demichele-2023.md) use the same
family, their $\xi$ being the $\zeta$ of the table above, Feiereisen at
$\zeta=1$ (Eqs. (15)–(16), §4.2.5, Table 2). They write its second-order
member as a finite-volume flux difference with the face mass flux
$m_{i+1/2}=\zeta\,\overline{\rho v}+(1-\zeta)\tfrac12(\rho_iv_{i+1}+\rho_{i+1}v_i)$,
$\overline a=\tfrac12(a_i+a_{i+1})$, mass flux $m$ and momentum flux
$\overline\phi\,m$ (Eqs. (23)–(25)), and derive the local flux of the induced
quadratic,
$$\phi_i\,[\![\overline\phi\,m]\!]-\tfrac{\phi_i^2}2[\![m]\!]=\Big[\!\Big[\tfrac12\phi_i\phi_{i+1}m_{i+1/2}\Big]\!\Big],$$
with $[\![\cdot]\!]$ here the flux difference divided by $\Delta x$ (Eqs.
(26)–(27); a high-order version is their Eq. (A.6)). Two consequences:

- **Pointwise weight.** In this form the weight may vary from face to face,
  $\zeta_i$ inside $m_{i+1/2}$, and the scheme still conserves mass,
  momentum and kinetic energy locally; the global finite-difference proof,
  which uses Eqs. (17)–(19), does not allow a variable weight (§3.2, §3.4).
- **Design rule.** To make $\phi\propto\sqrt\psi$ evolve conservatively,
  discretize the convective term of $\psi$ with this splitting (§3.4). With
  $\phi=\sqrt{2e}$ in the internal-energy equation it preserves
  $\rho\sqrt e$, proportional to $\rho c$ (§4.2.4).

## Energy-equation splittings

With KEP mass and momentum, De Michele & Coppola compare fifteen
discretizations of the energy equation, written in total energy $\rho E$,
internal energy $\rho e$, pressure, total enthalpy $\rho H$, sound speed
$\rho c$ or entropy $\rho s$ (§4; page-local $\rho$-weighted variables). Their
general formula for the discrete equation induced on any $G(\rho,v,\phi)$
uses only the chain rule in time, so it holds discretely for exact time
integration (Eq. (30)). From it (§4.2, Tables 1–2):

- a locally conservative discretization of $\rho e$, $p$, $\rho H$ or $\rho c$
  induces a locally conservative $\rho E$, and conversely $\rho E$ induces a
  locally conservative $\rho e$; for exact time integration it does not
  matter which equation is discretized, only the discrete convective and
  pressure terms do (Eqs. (35)–(41), §4.2.1);
- for the induced pressure work to be locally conservative, the
  derivative matrices of pressure and velocity must satisfy $D_p=-D_v^\top$
  (page-local; their Eq. (42), Veldman's Requirement 3.2), of the same form
  as the duality relations above *(compiler check, not in the sources)*;
- the KEEP scheme of Kuya et al. is, for exact time integration, the
  Kennedy–Gruber–Pirozzoli discretization of the internal-energy equation;
- no $\rho E$, $\rho e$, $p$, $\rho H$ or $\rho c$ scheme conserves entropy exactly;
  a direct entropy discretization (Honein–Moin) conserves $\rho s$ but loses
  $\rho E$ (Eqs. (73)–(77));
- only three are [pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md);
- the Jameson–Pirozzoli form writes the pressure work as $\rho v\,(p/\rho)$
  with the same triple-product split as $\rho E$ (§4.2).

Their tests are an isentropic vortex ($40^2$ eighth-order and $30^2$
fourth-order central derivatives, RK4, to $t=50$) and an inviscid
$32^3$ Taylor–Green vortex (§5). The internal-energy and entropy
formulations with the Kennedy–Gruber–Pirozzoli split are the most robust:
$(\rho e)$, $(\rho e)_{\mathrm{PEP}}$, the KGP sound-speed and the KGP entropy
schemes never blow up by $t=50$ at CFL 0.01, 0.1 and 0.5, while every
total-energy and total-enthalpy form does except two at CFL 0.5 (Table 3).
The KGP sound-speed scheme never diverges and Kok's Feiereisen version does
(at $t\approx46$ in the Taylor–Green vortex; §5.2). They conclude that a
KEP treatment of the energy variable itself, the customary choice that
also preserves $\rho E^2$, $\rho e^2$ or $\rho s^2$, is "not necessarily the
best option" (§6).

**As a non-dissipative reference.** [Bielawski et al. (2023)](/sources/bielawski-2023.md)
use a skew-symmetric central scheme, after Honein–Moin and Pirozzoli's
generalized split forms, as the non-dissipative baseline against HLLC and
AUSMDV in decaying compressible isotropic turbulence. At $M_{t,0}=0.3$ on
a structured $64^3$ mesh it tracks the spectral reference; at
$M_{t,0}=0.6$, with eddy shocklets, both upwind schemes are much more
dissipative than it in enstrophy and dilatation (App. A, Figs. A.13–A.16;
[decaying compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)).
They print no formula for it. [De Vanna et al. (2023a)](/sources/devanna-2023.md)
use the sixth-order fully split energy-preserving scheme of Pirozzoli in
[URANOS](/software/uranos.md), with no formula printed either, as the
zero-dissipation baseline of their
[wall-modelled LES](/methods/wall-modeled-les.md) study: it matches the DNS
of shock-free Mach 2 boundary layers best of the six schemes compared, and
diverges at Mach 5.86 because of shocklets unless hybridized with WENO or
TENO (§3.1, §4.3.1, §4.4).

## Eight-point optimized cubic split with TENO (Liang & Fu)

[Liang & Fu (2024b)](/sources/liang-2024-b.md) recall the quadratic
(Feiereisen) and cubic (Kennedy–Gruber) split forms of
$\partial_x(\rho v\phi)$ for $\phi\in\{1,v_1,v_2,v_3,E/\rho\}$, call the cubic
one the more robust, and use Pirozzoli's locally conservative form of it
(§2.3, Eqs. (21)–(26)):

$$\hat f^{\mathrm{skew}}_{i+1/2}=2\sum_{\ell=1}^{4}\mathsf a_\ell\sum_{m=0}^{\ell-1}\tfrac18\big(\rho_{i-m}+\rho_{i-m+\ell}\big)\big(\phi_{i-m}+\phi_{i-m+\ell}\big)\big(v_{i-m}+v_{i-m+\ell}\big),$$

with central first-derivative weights $\mathsf a_\ell$ (page-local, as on
[flux differencing](/methods/flux-differencing.md); Eqs. (27)–(28)). For
$\ell=1$ only, the face flux is
$\overline\rho\,\overline\phi\,\overline v$, the cubic split of the Jain &
Moin table above *(compiler check, not in the sources)*. Instead of the
maximum-order weights they impose consistency and the second- and
fourth-order conditions and fix the last degree of freedom by minimizing
the dispersion error $\int_0^\pi e^{7(\pi-\vartheta)}(\tilde\vartheta_r-\vartheta)^2d\vartheta$,
which weights low wavenumbers because at high ones the TENO branch takes
over (§3.3.1, Eqs. (36)–(42)). The resulting sixth-order weights are
$\mathsf a_1=0.8441336457279522$, $\mathsf a_2=-0.2441336457279522$,
$\mathsf a_3=0.0570096576929319$, $\mathsf a_4=-0.006723831837710873$; the
central part of the background linear scheme of their eight-point TENO has
the same weights, so the smooth and shock-capturing branches share their
dispersion (§3.3.1, Eq. (46)). The flux is used, without characteristic
decomposition, in every cell that a TENO-type discontinuity indicator on
six three-point stencils declares smooth, and the TENO flux elsewhere
(Eq. (35), Algorithm 1; [hybrid schemes](/methods/hybrid-weno.md)). The
authors report that the split branch handles more than 90 % of the cells
of the double Mach reflection (stated, no count shown), and their 2D
wall-clock times on one CPU make the hybrid 16–53 % cheaper than WENO-CU6,
TENO6 and TENO8 *(compiler check, not in the sources: ratios of the printed
timings, Tables 6–11)* (§4.5–4.8; [kinetic energy preservation](/properties/kinetic-energy-preservation.md)).

The Euler fluxes are given term by term (Eqs. (29)–(30)): mass
$\mathcal M$ as $\overline\rho\,\overline v$, momentum as
$\overline\rho\,\overline v\,\overline v_d$, energy convection
$\mathcal E$ as $\overline E\,\overline v$, pressure work $\mathcal K$ as
$\overline p\,\overline v$ and pressure gradient $\mathcal P$ as
$\overline p$, each inside the same $\ell$, $m$ double sum (page-local
symbols; their $\mathcal E$ is not the registry's energy). Algorithm 1
instead writes the energy flux with $\phi=E/\rho$, the triple average
$\overline\rho\,\overline{(E/\rho)}\,\overline v$, which differs in general
from $\overline E\,\overline v$ *(compiler check, not in the sources)*. Which
one the code uses is not stated.

## Unstructured face flux with species (Duronio & Di Mascio)

[Duronio & Di Mascio (2024)](/sources/duronio-2024.md) apply the cubic
split on unstructured OpenFOAM meshes as a face flux between owner and
neighbour cell centres $O$, $N$ (page-local), after Modesti & Pirozzoli,
splitting the inviscid flux AUSM-style into a convective part
$\rho v_n\tilde q$ and a pressure part, with $\tilde q=(1,v,H,Y_k)$
(Eqs. (4)–(6)):

$$F^C_u=\tfrac18(\rho_O+\rho_N)(\tilde q_O+\tilde q_N)(v_O+v_N)\cdot n,\qquad F^C_p=\tfrac12(p_O+p_N)\,n .$$

The species mass fractions are the only new components; the total-energy
row carries $H$, so the pressure work sits in the convective flux. A
compression-only Ducros-type sensor switches AUSM$^+$-up dissipation on the
convective part (Eqs. (7)–(8)). The assessment is on Richtmyer–Meshkov
shock–bubble interactions, a supercritical LOX/H$_2$ mixing layer with a
Peng–Robinson equation of state and a gasoline injector, with qualitative
or graphical agreement and three-grid observed orders 1.35–1.53 (§3,
Table 1); no smooth accuracy or kinetic-energy test is run. The paper
prints $H=(e+p)/\rho$ with $e$ the total energy per unit mass, where
$H=e+p/\rho$ is meant by its own definitions (§2).

## Split forms in DG and flux reconstruction

For Burgers, $\partial_tu+\partial_x(u^2/2)=0$, the split form is
$\alpha_{\mathrm s}\,\partial_x(u^2/2)+(1-\alpha_{\mathrm s})\,u\,\partial_xu$
with page-local weight $\alpha_{\mathrm s}$; $\alpha_{\mathrm s}=2/3$ makes the
volume terms cancel in the energy balance of a summation-by-parts
discretization. [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
take the split with respect to the stiffness operator, which satisfies
summation by parts for dense norms and uncollocated nodes, instead of the
differential operator, and obtain an energy-stable split form of
energy-stable flux reconstruction (§3.1;
[flux reconstruction](/methods/flux-reconstruction.md)).
[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) use the
Ducros et al. split form, which on its own is neither entropy conservative
nor kinetic-energy preserving, as the volume term of nodal DG plus
entropy and kinetic-energy correction terms; on the inviscid 2D
Taylor–Green vortex this behaves like flux differencing with an
entropy-conservative flux and does not blow up before $t=30$ (§4.2.2,
Fig. 8; [entropy correction term](/methods/entropy-correction-term.md)).

## Dual-sided discretization

A *dual-sided* scheme pairs a directionally biased operator with its
negative transpose in the dual slot. An example is
$D^m=D^\rho=I-\mathcal T^{-1}$ (backward) with $D^v=D^0=-(I-\mathcal T^{-1})^\top$.
It satisfies the duality relations and so conserves mass, momentum and
kinetic energy. The traditional upwind scheme instead uses
$I-\mathcal T^{-1}$ in all four slots and conserves none of them, except
mass for $\zeta=1$ (§7.3, Fig. 3).

On 1D Euler acoustic-wave steepening, the formally first-order dual-sided
scheme behaves as follows (§8.2, Fig. 4):

- **Setup.** $N_x=32$, internal-energy formulation, $\zeta=1/2$, central
  pressure terms.
- **Conservation.** Mass, momentum and total energy are conserved to
  machine precision. First-order upwind loses $4.5\times10^{-3}$,
  $1.2\times10^{-2}$ and $1.5\times10^{-2}$ of them by $t=5$.
- **Shock profile.** After the shock forms ($t\approx3.5$), the dual-sided
  profile "nicely fits in between" the oscillating second-order central
  scheme and the smeared upwind scheme, with no artificial dissipation.

## Relation to flux-differencing DG

In nodal DG the same split forms arise from the choice of the symmetric
two-point volume flux in [flux differencing](/methods/flux-differencing.md)
([Ranocha et al. (2023)](/sources/ranocha-2023.md), §2, citing
Gassner–Winters–Kopriva). The Shima et al. flux yields a "standard split form
discretization" (§9). Coppola & Veldman remark that all prior studies of
split forms assumed central discretization, and that biased operators are
admissible once they satisfy the duality relations (§5.4). See
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
and [kinetic energy preservation](/properties/kinetic-energy-preservation.md).

## Qualifications

- Edoh's disagreement with Charnyi et al. and Both et al. on EMAC is a
  disagreement about the discrete setting: the EMAC papers are finite
  element papers with a weakly imposed solenoidal constraint, and Edoh's
  negative result holds under diagonal-norm SBP finite-difference algebra
  (§3.1). Edoh's priority claims ("first", "only") are qualified "to the
  author's knowledge".
- Edoh does not study the temporal kinetic-energy error and presumes it
  negligible at small $\Delta t$; exact preservation in time needs
  implicit symplectic or relaxation integrators (§4.1.1).
- The theory of Coppola & Veldman is for periodic 1D grids with exact time integration. The tests
  use classical RK4 with very small steps, and non-periodic boundaries are
  only pointed to (via SBP).
- The non-dissipative dual-sided shock profile is shown on one coarse 1D
  test. The paper makes no entropy-stability claim for it (§8.2).
- Jain & Moin's split-form tests are inviscid, shock-free and at
  initial Mach numbers up to 0.4; their divergence-form failure is one
  test (App. C). Edoh's divergence-form failures are likewise on smooth
  under-resolved problems. Neither source tests the forms at shocks.
- Jain & Moin print "QS and CS stands for cubic-split and quadratic-split
  forms, respectively" (§3.5); their own definitions and Eq. (62) make QS
  the quadratic and CS the cubic split.
- In their §7.3 tests with the central split family, weights violating
  Eq. (10) still conserve mass and momentum but lose kinetic energy at
  $O(10^{-3})$–$O(10^{-4})$. The variant $\mu_\rho=1$ ("$\delta=1$" in the
  source's letters) "turned out not always to be stable" (Fig. 2).
- De Michele & Coppola (arXiv v1, §3.1) print "the cases $\xi=0$ and
  $\xi=1$ give the classical Feiereisen form and the newly derived form",
  the reverse of their own Eqs. (15)–(16), §4.2.5 and Table 2, which give
  $\xi=1$ Feiereisen. Their conditions assume exact time integration and
  periodic uniform meshes; their remark that finer and higher-order runs
  blow up earlier compares runs that differ in mesh and order at once
  (§5.1).

# Citations

- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.1–2.2 Eqs. (7)–(11), §3.3 Eq. (43), §3.4 Eq. (53), §4.2 Eqs. (56)–(58), §5.3–5.4 Eqs. (72)–(73) Table 1, §7.3 Figs. 2–3, §8.2 Fig. 4.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2, §9.
- [Edoh (2022)](/sources/edoh-2022.md) — §2 Eqs. (1)–(7), §3.1 Eqs. (9)–(18), Remarks 2–3, Tables 1–2, §3.2 Eqs. (20)–(26), Remark 4, Tables 3–4, §4 Figs. 1–4, App. A.
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §3, §3.1 Eqs. (20)–(28), §3.1.2 Eq. (46) (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §4.2.2 Fig. 8 (arXiv v4).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3.1 Eqs. (38)–(42), §3.5 Eqs. (58)–(62), §4.1.2, App. C Table 2 Fig. 13 (arXiv v1).
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §3.1–3.4 Eqs. (12)–(28), §4.1 Eq. (30), §4.2 Eqs. (32)–(77), Tables 1–3, §5, §6, App. A Eq. (A.6) (arXiv v1).
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — App. A Figs. A.13–A.16 (accepted manuscript).
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.1, §4.3.1, §4.4.
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §3.1 Eq. (17), §3.4 Table 1, §4, §5 Eqs. (55)–(59).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.3 Eqs. (21)–(30), §3.2 Eq. (35) Algorithm 1, §3.3.1 Eqs. (36)–(46), §4.5–4.8 Tables 6–11.
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §2 Eqs. (1)–(8), §3 Table 1.
