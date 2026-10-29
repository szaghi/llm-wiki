---
type: Method
title: "Conditional source-term estimation"
description: "Conditional source-term estimation closes the mean or filtered reaction rate of RANS and LES with the conditional moment closure hypothesis, recovering the conditional means by a regularized inversion of an integral equation over ensembles of cells instead of transporting them; this page gives the inversion, its regularization, presumed PDFs, double conditioning and the assessed errors."
status: established
aliases: [CSE, conditional source-term estimation, doubly conditional source-term estimation, DCSE, localized CSE, first conditional moment closure hypothesis, presumed PDF, beta PDF, Tikhonov regularization]
tags: [combustion, les, rans, a-priori-a-posteriori, presumed-pdf]
timestamp: 2026-10-28T17:46:00Z
---

# Conditional source-term estimation

**Conditional source-term estimation** (CSE), introduced by Bushe and
Steiner in 1999 as an LES extension of conditional moment closure (CMC), is
a closure of the turbulence–chemistry interaction: it models the
Favre-averaged (RANS) or Favre-filtered (LES) chemical source term of a
reacting flow. Like CMC it evaluates the reaction rate at **conditional**
means of density, species and temperature and integrates the result
against a presumed probability density function (PDF) of a conditioning
scalar, mixture fraction in non-premixed, a reaction progress variable in
premixed and both in partially premixed flames. Unlike CMC it transports
no conditional quantity: the ordinary unconditional scalars are
transported, and the conditional means are recovered by inverting an
integral identity over an **ensemble** of cells in which they are assumed
spatially uniform. The inversion is an ill-posed problem and must be
regularized. The bundle's account is the review of
[Salehi et al. (2024)](/sources/salehi-2024.md), whose evidence is mostly
reproduced from the works it cites; the method belongs to the
turbulent-combustion closures next to
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
and the [thickened flame model](/methods/thickened-flame-model.md).

Page-local notation (none of these symbols is in the registry):
$\dot\omega_k$ the net production rate of species $k$ and $Y_k$ its mass
fraction; $Z$ the mixture fraction and $c$ the normalized progress
variable ($c=0$ in reactants, 1 in products); $\xi$ the sample-space
variable of the conditioning scalar ($\xi_Z$ when that scalar is $Z$; not
the reference coordinate of element methods); $\tilde P(\xi;\boldsymbol x)$
its Favre PDF at $\boldsymbol x$; $\widetilde{\varphi\,|\,\xi}$ the
Favre-averaged or filtered conditional mean of a quantity $\varphi$;
$Q_\varphi(\xi)$ the conditional mean assumed uniform over an ensemble
(the source's $\widehat{\varphi|\xi}$, which is not a test-filtered field
in the registry's sense); $N_{\mathrm b}$ the number of conditional bins
(the unknowns) and $N_{\mathrm e}$ the number of cells of an ensemble (the
source's $M$ and $N$); $\mathsf A$, $\boldsymbol a$, $\boldsymbol b$ the
kernel matrix, the unknown conditional means and the unconditional data;
$\lambda_{\mathrm T}$ the Tikhonov parameter (not the Taylor microscale);
$\varsigma^{\mathsf A}_j$ the singular values of $\mathsf A$ (the registry's
$\varsigma_i$ belong to the velocity gradient); $Z_v=\widetilde{(Z-\tilde Z)^2}$
and $c_v$ the Favre variances; $\chi_Z$, $\chi_c$ the scalar dissipation
rates of $Z$ and $c$ ($\chi$ alone is the Spalart–Allmaras ratio);
$\mathcal D$, $\mathcal D_t=\nu_t/Sc_t$, $\mathcal D_T=\mathcal D+\mathcal D_t$
the molecular, turbulent and total diffusivities, $Sc_t$ the turbulent
Schmidt number.

## Conditional moment closure: the hypothesis CSE inherits

The parent model, its transport equation, closures, cost and engine
applications are on [conditional moment closure](/methods/conditional-moment-closure.md);
this section keeps what CSE inherits from it.

Evaluating the rate at the mean or filtered state,
$\tilde{\dot\omega}_k\approx\dot\omega_k(\bar\rho,\tilde Y_k,\tilde T)$
("first-moment closure"), is "ordinarily unacceptably inaccurate", and a
turbulence–chemistry closure is needed in LES too, because extinction
correlates with the smallest scales, which the filter removes
([Salehi et al. (2024)](/sources/salehi-2024.md), §1, Eq. 1). The **first
conditional moment closure hypothesis** of Bilger and of Klimenko and
Bilger, as Salehi et al. cite it, evaluates the rate at the conditional
means (§2.1, Eq. 2):

$$\tilde{\dot\omega}_k\approx\int_0^1\dot\omega_k\big(\overline{\rho\,|\,\xi},\widetilde{Y_k\,|\,\xi},\widetilde{T\,|\,\xi}\big)\,\tilde P(\xi)\,\mathrm d\xi .$$

The review's a priori illustration (§2.1, Fig. 1, Eq. 3, Table 2) uses a
DNS of a freely propagating premixed methane–air flame and the two-reaction
CO$_2$ subset of the Smooke–Giovangigli mechanism, conditioned on the
normalized CO$_2$ mass fraction: in one LES cell the directly filtered
CO$_2$ rate is 26.2 s⁻¹, first-moment closure gives 37.0 s⁻¹ (41% error)
and the CMC hypothesis with the exact DNS PDF 28.1 s⁻¹ (7%).

CMC proper transports the conditional means
$Q_k=\widetilde{Y_k\,|\,\xi}$ (§2.1, Eq. 4):

$$\partial_tQ_k+\widetilde{u_i\,|\,\xi}\,\partial_iQ_k+\frac{\partial_i\big(\bar\rho\,\tilde P\,\mathcal F_{k,i}\big)}{\bar\rho\,\tilde P}=\widetilde{\chi_\xi\,|\,\xi}\;\partial_\xi^2Q_k+\widetilde{\dot\omega_k\,|\,\xi},$$

with $\mathcal F_{k,i}$ (page-local) the conditional turbulent flux of
species $k$ and $\widetilde{\chi_\xi\,|\,\xi}$ the conditional scalar
dissipation rate. Non-premixed CMC typically uses 50–100 mixture-fraction
points and a spatial grid much coarser than the flow grid, since
conditional gradients are small, for example a $4\times4\times64$ CMC grid
inside a $96\times96\times320$ LES of Sandia flame D, and $23\times23\times23$
for flame F, with frequent local extinction (§2.1, §2.2, as cited).

The review classifies closures of the filtered rate into five numbered
families: algebraic (eddy break-up), reactor-type (eddy dissipation
concept, partially stirred reactor), flamelet (steady and unsteady
flamelets with presumed PDFs, and topology-based models: flame surface
density, G-equation, thickened flamelet), CMC, and transported PDF, with
hybrids such as multiple mapping conditioning (§1).

## The inversion

CSE transports the unconditional Favre scalars (§2.2, Eq. 5),

$$\bar\rho\,\partial_t\tilde Y_k+\bar\rho\,\tilde u_i\,\partial_i\tilde Y_k+\partial_i\big(\bar\rho\,\widetilde{u_i''Y_k''}\big)=\partial_i\big(\bar\rho\,\mathcal D_k\,\partial_i\tilde Y_k\big)+\bar\rho\,\tilde{\dot\omega}_k ,$$

with gradient transport for the turbulent flux, and starts from the
identity $\tilde\varphi=\int_0^1\widetilde{\varphi\,|\,\xi}\,\tilde P(\xi)\,\mathrm d\xi$
(Eq. 6). Assuming the conditional means uniform over an ensemble of cells
$\mathbb E$ (page-local; the authors call it a "test filter", of width
larger than $\Delta$) gives a Fredholm integral equation of the first kind
for the unknown $Q_\varphi$ with the PDF as kernel (Eq. 7):

$$\tilde\varphi(\boldsymbol x_i)=\int_0^1Q_\varphi(\xi)\,\tilde P(\xi;\boldsymbol x_i)\,\mathrm d\xi,\qquad \boldsymbol x_i\in\mathbb E .$$

Discretized into $N_{\mathrm b}$ bins it becomes the linear system
$\mathsf A\boldsymbol a=\boldsymbol b$ of $N_{\mathrm e}$ equations, with
$A_{ij}=\int_{\xi_{j-1/2}}^{\xi_{j+1/2}}\tilde P(\xi;\boldsymbol x_i)\,\mathrm d\xi$,
$b_i=\tilde\varphi(\boldsymbol x_i)$ and $a_j=Q_\varphi(\xi_j)$ (Eq. 8).
The conditional means so obtained enter the CMC hypothesis to give the
closed rate. Initial guesses in the cited works are a flamelet solution
integrated forward for a few steps, equilibrium products, a zero prior or
burning conditional products (§2.2).

**The analogy with the dynamic procedure.** The authors present the
inversion as the analogue of the
[dynamic procedure](/methods/dynamic-procedure.md) for the Smagorinsky
coefficient: the Germano identity plays the role of the identity (6), and
the uniformity of the coefficient at the test-filter level the role of the
CSE homogeneity assumption, with a least-squares solution over the
equations in both cases (§2.2). They note the difference in scale: the
test-to-grid filter ratio is 2 to 3 in dynamic subgrid models, much larger
in CMC and CSE (§2.2). The assumption-by-assumption comparison of their
Table 1: both rest on the CMC hypothesis and on a presumed PDF; CSE
transports unconditional and CMC conditional moments; only CSE inverts an
integral; CSE requires conditional homogeneity, which CMC does not need
but uses predominantly to cut cost.

**Double conditioning.** Doubly conditional CSE (DCSE; first applied by
Dovizio et al., as cited) conditions on two scalars, typically $Z$ and $c$,
with a joint PDF $\tilde P(\xi_Z,\xi)$; the discretized problem has the
same form with $N_{\mathrm b}=N_Z\times N_c$ unknowns (page-local bin
counts; §2.4, Eqs. 11–14). Double conditioning is motivated by local
extinction, ignition, stratified and supercritical flames and
"substantially" reduces the spatial gradients of the conditional averages
(as cited); the two conditioning variables can be selected by principal
component analysis. For partially premixed flames the four-dimensional
table $(c,Z,Y_{\mathrm{CO_2}},Y_{\mathrm{H_2O}})$ is reduced to three
dimensions by defining $c$ from CO$_2$ normalized by its equilibrium value
at the given $Z$ (§2.4, Fig. 44).

## Ensembles

The number of reacting cells per ensemble must greatly exceed the number
of unknowns: the review recommends $\mathcal O(10^3)$ reacting cells for
single and $\mathcal O(10^4)$ for double conditioning, from the rule that
regression needs $\mathcal O(10)$ data per parameter; reacting cells are
selected by $\tilde c(1-\tilde c)>\epsilon$ with $\epsilon$ between
$10^{-2}$ and $10^{-3}$ (§2.5, Eq. 15). Typical sizes in the cited works:
$N_{\mathrm b}=40$ in LES of the Sandia flames and 50 for a premixed Bunsen
flame or a spray flame; $N_{\mathrm b}=500$ to 1000 in DCSE (for example
50 mixture-fraction by 10 oxidizer-split bins); 1.5 million cells in 64
ensembles of about 24,000 cells with $N_{\mathrm b}=500$; 1,638,400 cells
in 800 ensembles of 2048 cells with $N_{\mathrm b}=50$ (§2.5).

The inversion costs $\mathcal O(N_{\mathrm b}^2N_{\mathrm e})$, so on one
processor the number of ensembles does not change the cost, but in
parallel runs it does: in an LES-DCSE of a lifted flame with one ensemble
per processor the cited study found that the cost decreases as the number
of ensembles increases (Fig. 4: 32, 67, 42, 44 and 50 CPU s per step for
the five ensemble layouts (a)–(e), (a) with 48 and (c) with 24
ensembles), and 24 ensembles were kept because 48 occasionally left too
few reacting cells near the flame base (§2.5, Fig. 4, as reproduced). Laboratory axisymmetric flames use
discs, disc sectors or conical frustums as ensembles, complex geometries a
modified Morton-ordering partition (Fig. 3); a dynamic selection lets
processors report reacting-cell counts to a master that forms the
ensembles, with the system solved by parallel LSQR (Fig. 5). Overlapping
ensembles are used in two-dimensional RANS, non-overlapping ones in LES
(§2.5–2.6).

## Presumed PDFs

The PDF is presumed, not transported (§2.7):

- **$\beta$-PDF** in mixture fraction,
  $\tilde P_\beta(\xi_Z)=\xi_Z^{a_\beta-1}(1-\xi_Z)^{b_\beta-1}\Gamma(a_\beta+b_\beta)/[\Gamma(a_\beta)\Gamma(b_\beta)]$
  with $a_\beta=\tilde Z^2(1-\tilde Z)/Z_v-\tilde Z$ and
  $b_\beta=a_\beta(1/\tilde Z-1)$ (page-local parameters; Eqs. 17–19). $Z$
  and $Z_v$ are transported (Eqs. 20–21) with
  $\widetilde{u_i''Z''}=-\mathcal D_t\partial_i\tilde Z$ and the variance
  sink $2\bar\rho\tilde\chi_Z$ closed by linear relaxation
  $\tilde\chi_Z=c_d\,Z_v/\tau_Z$, $c_d=\mathcal O(1)$, with $\tau_Z=\Delta/u'_\Delta$
  in LES and $\tilde k/\tilde\varepsilon$ in RANS ($c_d$, $\tau_Z$
  page-local; $u'_\Delta$ the subgrid velocity scale of registry §11).
  $Sc_t=0.7$ in RANS; in LES dynamic, 0.4 or 0.7, a range one cited study
  found not significant (§2.7.1). For the turbulent Prandtl analogue see
  [turbulent Prandtl number](/definitions/turbulent-prandtl-number.md).
- **Premixed flames.** The progress variable and its variance are
  transported (Eqs. 22, 26–27), the variance equation with a chemical
  source $2\bar\rho\,(\widetilde{\dot\omega_cc}-\tilde{\dot\omega}_c\tilde c)$;
  the $\beta$-PDF over-predicts mean premixed rates in RANS and the
  filtered flame speed in LES unless $\Delta$ is of the order of the
  laminar flame thickness (as cited, Fig. 6). The **flamelet PDF** of Bray
  et al., $\tilde P_{\mathrm f}=c_0\delta(\xi)+c_\nabla\rho(\xi)/(\bar\rho\,|\mathrm d\xi/\mathrm dx|)+c_1\delta(1-\xi)$
  with the profile of a one-dimensional laminar flame (Eq. 23), holds at
  high variance and is clipped or blended with the $\beta$-PDF at low
  variance; the **linear-eddy-model PDF** matches the DNS PDF best but is
  costly (Fig. 7).
- **Joint PDFs** for DCSE: statistical independence
  $\tilde P(\xi_Z,\xi)\approx\tilde P(\xi_Z)\tilde P(\xi)$ (Eq. 28), which
  fails when the covariance $\widetilde{c''Z''}$ is significant (0.17
  against 0.02 in a supercritical mixing-layer DNS, Fig. 8); a Bayes
  decomposition with a conditional PDF of $c$ given $Z$ (Eq. 29), a
  four-Dirac correlated PDF (Eq. 30), copulas (Eq. 31) and deep-learning
  PDFs are the alternatives listed (§2.7.3).

Chemistry enters through trajectory-generated or flamelet tables, a
laminar-flamelet decomposition of the conditional means, or detailed
chemistry; these, and their cost, are on
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).

## Regularization of the inversion

A plain least-squares solution of $\mathsf A\boldsymbol a=\boldsymbol b$
is oscillatory and non-physical (§2.3, Eq. 9, Fig. 2). The kernel is
ill-posed in Hadamard's sense: zero singular values make the solution
non-unique and small ones amplify the modelling errors in $\boldsymbol b$.
With the singular value decomposition
$\mathsf A=\mathsf U\Sigma\mathsf V^{\mathsf T}$ the solution is
$\boldsymbol a=\sum_{j}(\boldsymbol U_j\cdot\boldsymbol b/\varsigma^{\mathsf A}_j)\boldsymbol V_j$,
and the **Picard condition** requires the coefficients
$\boldsymbol U_j\cdot\boldsymbol b$ to decay faster than $\varsigma^{\mathsf A}_j$; with
Gaussian noise of $10^{-10}$ added to measured conditional CO$_2$ data (200
bins, one ensemble of a methane jet flame) it fails (§2.9.1, Eqs. 39–41,
Fig. 13, as reproduced). The remedies (§2.9.2–2.9.4, Eqs. 10, 42–52):

| Method | Form | Remarks in the review |
|---|---|---|
| zeroth-order Tikhonov | $\boldsymbol a=\arg\min\big\lVert[\mathsf A;\lambda_{\mathrm T}\mathsf I]\boldsymbol a^*-[\boldsymbol b;\lambda_{\mathrm T}\boldsymbol a_0]\big\rVert_2^2$ | prior $\boldsymbol a_0$: null vector, previous time step ("similar to Kalman filtering", as cited), Burke–Schumann flame or unstrained laminar premixed flame; may need smoothing afterwards |
| truncated SVD | sum kept to $j\le k_{\mathrm s}<N_{\mathrm b}$ (page-local) | with zero-prior Tikhonov, a filter-function method: filter factor 1 for $j\le k_{\mathrm s}$ and 0 beyond, against ${\varsigma^{\mathsf A}_j}^2/({\varsigma^{\mathsf A}_j}^2+\lambda_{\mathrm T}^2)$ for Tikhonov |
| first-order Tikhonov | $\lambda_{\mathrm T}\mathsf I\to\lambda_{\mathrm T}\mathsf L$, zero prior, $\mathsf L$ the $(N_{\mathrm b}-1)\times N_{\mathrm b}$ first-difference matrix | less memory than a previous-step prior; not recommended with the flamelet decomposition, whose neighbouring library members need not have correlated weights |
| non-negative least squares | positivity of the conditional means enforced | about ten times the cost of the QR solution (as cited) |

The parameter is set by $\lambda_{\mathrm T}^2=\mathrm{tr}(\mathsf A^{\mathsf T}\mathsf A)/\mathrm{tr}(\mathsf I)$
(Eq. 48, as cited), by the L-curve, applied automatically at every step in
one cited LES, or by generalized cross-validation. The systems are solved
by LU on the normal equations $(\mathsf A^{\mathsf T}\mathsf A+\lambda_{\mathrm T}^2\mathsf L^{\mathsf T}\mathsf L)\boldsymbol a=\mathsf A^{\mathsf T}\boldsymbol b$
for 50–500 unknowns, by QR of the augmented matrix, or iteratively by
LSQR for $\mathcal O(10^4)$ rows and sparse kernels (§2.9.4, Eqs. 50–52).
Bayesian and neural-network inversions are judged too expensive per time
step, though Bayesian credible intervals would quantify the inversion
uncertainty (§2.9.4, Fig. 15).

**Localized CSE.** Expanding the conditional means in Bernstein polynomials
of degree $n_{\mathrm B}$, $\mathcal B_{j,n_{\mathrm B}}(\xi)=\binom{n_{\mathrm B}}{j}\xi^j(1-\xi)^{n_{\mathrm B}-j}$
(page-local), whose end members resemble reactant and product profiles and
whose interior members resemble radical profiles, and solving for
non-negative coefficients (Eqs. 53–56) is itself a regularization: no
Tikhonov term is needed, the unknowns fall from about 50 to fewer than 10,
and a priori ensembles of 16 cells suffice, at least 27 in an actual LES
(§2.9.5, Figs. 17–18; contribution of Mahdipour and Salehi, the review's
first author being a co-author). The review states that CSE "has
reached a certain level of maturity on the aspect of regularization
technique" (§4.1) and recommends a new user to start in RANS, with
single conditioning and Bernstein polynomials or zeroth-order Tikhonov;
first-order Tikhonov is the "most promising" for future development but
less tested; the extension of Bernstein polynomials to double
conditioning "appears much more challenging", Tikhonov regularization
"more tractable" (§4.2–4.3).

## Error sources and assessment

CSE separates four errors, each testable
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) on
[DNS](/definitions/direct-numerical-simulation.md) data: the CMC
hypothesis, conditional homogeneity over the ensemble, the presumed PDF,
and the inversion. The cited a priori studies, as the review reports them:

- the first CSE test, on a [temporal mixing layer](/benchmarks/temporal-mixing-layer.md)
  DNS with one-step chemistry ($128\times64\times64$, top-hat filter of
  $16\times8\times8$ cells, four ensembles), with scalar dissipation as a
  second condition (§3.1.1, Figs. 19–20);
- high-pressure heptane mixing-layer DNS (Peng–Robinson equation of
  state, one-step chemistry): CSE with the DNS PDF performs very well,
  with a $\beta$-PDF it shows significant errors, and in DCSE the joint
  PDF ($\beta$ in $c$ plus independence) is "by far" the largest error,
  larger than ensemble selection or inversion (§3.1.1, Fig. 21);
- freely propagating premixed flames at Karlovitz numbers 6, 74, 540 and
  4100 (top-hat filter $\Delta/\delta_{\mathrm L}=0.7$ with
  $\delta_{\mathrm L}$ page-local the laminar thermal thickness, 1024 LES
  cells, 16 species and 35 reactions): the CMC-hypothesis error is
  insignificant at low and high Karlovitz number, the homogeneity error is
  significant with a single 1024-cell ensemble, and the inversion error is
  not significant relative to coarse-grid CMC (§3.2.1, Fig. 34); a
  premixed flame in an [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
  box was the RANS-context test (Fig. 33).

The review's conclusion is that the joint or single PDF closure is "the
largest source of error in a priori DNS calculations", an error that can
exceed any improvement CSE brings (§4.1).

**Against CMC.** In one RANS code for Sandia flames D, E and F (cited),
CSE and CMC are similar for D; for E CSE reproduces the local-extinction
effects, too strongly, while CMC "could not capture the correct trends";
neither does well for F; CMC needs more resources and is more sensitive to
inlet conditions and to the conditional scalar-dissipation model (§2.10,
Table 3).

CSE has also served as the LES formulation of CMC itself: in the
review of engine combustion models by
[Posch et al. (2025)](/sources/posch-2025.md), Huang et al. apply CMC in
LES of a diesel-pilot natural-gas dual-fuel engine and "used conditional
source term estimation" for the CMC LES formulation, with
low-dimensional manifolds for the chemistry, and claim agreement with
measured in-cylinder pressure and emissions (§4.7, §5.2.3, Table 10;
the review reports the claim without assessing it).

**Applications** reported in the review (§3, as reproduced):

| Flame | Model | Result |
|---|---|---|
| lifted methane jets in still air, $Re=7000$, 12,000, 19,500 | LES-DCSE, 3,302,400 cells, 24 ensembles | lift-off 30, 78, 137 mm against measured $30\pm7$, $80\pm11$, $135\pm11$ mm (RANS-DCSE 29.5, 74.5, 129.5 mm) (§3.3.2, Table 6) |
| Delft jet-in-hot-coflow MILD flames | LES-DCSE with a second mixture fraction tracking oxygen | lift-off under-predicted by 36% and 44% (§3.4.3) |
| F3 and Gülder Bunsen flames | LES-CSE, 128 disc ensembles | F3 conditional H$_2$O follows unstrained flamelets, the Gülder flame (thin and broken reaction zones) deviates; the flame height improves when the simple subgrid dissipation $\tilde\chi_c=\mathcal D_tc_v/\Delta^2$ (Eq. 58) is replaced by a linear-eddy model (§3.2.2, Figs. 38–41) |
| F3 and Gülder flames | localized RANS-CSE | flamelet conditional averages at 20% lower cost than regular CSE; Gülder flame height predicted, where an unstrained-flamelet model under-predicts it (§3.2.2, Figs. 42–43) |

Other reviewed cases are bluff-body and V-flames, sooting, buoyant and
spray flames, engines and a semi-industrial furnace, several run in
[OpenFOAM](/software/openfoam.md), several with the
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) as RANS closure
(§3).

## Qualifications

- **Evidence.** Except for the a priori illustration of Fig. 1 and two
  flamelet calculations, the review's results are reproduced from the
  cited works; no new CSE computation is reported. The comparisons with
  experiment and with CMC are those of the original studies.
- **Statements on LES resolution.** The authors' argument that premixed
  flames are thinner than the Kolmogorov length and "very unlikely" to be
  resolved on an LES mesh (§1) motivates a closure of the filtered rate;
  the [thickened flame model](/methods/thickened-flame-model.md), which
  the review lists among the topology-based flamelet approaches (§1),
  widens the front instead.
- **Elemental conservation.** With detailed chemistry the conditional
  species come from an inverse problem, so elemental mass conservation is
  not guaranteed; a single DNS snapshot did not show the error, which the
  authors expect to accumulate in RANS or LES, and they propose inverting
  for all species under an elemental-conservation constraint (§2.8.3).
- **Printed slips in Salehi et al. (2024).** §1 announces "four
  categories" of closures and numbers five. §2.3 says "Eq. (13) is
  transformed" into the single-conditioned system Eq. (8), whose source is
  Eq. (7). The kernel is called "$M\times N$" in §2.4 and "$N\times M$" in
  §2.9.1; Eq. (8), with $i$ over cells, makes it $N_{\mathrm e}\times N_{\mathrm b}$.
  The Bernstein sum of Eq. (53) starts at $j=1$, while Eq. (54) and
  Fig. 17 use $\mathcal B_{0,n_{\mathrm B}}$ to $\mathcal B_{n_{\mathrm B},n_{\mathrm B}}$.
  Eq. (49) multiplies the scalar norm $\lVert\boldsymbol a^*-\boldsymbol a_0\rVert_2^2$
  by $\lambda_{\mathrm T}^2\mathsf I$; left-multiplying the augmented system
  of Eq. (10) by $[\mathsf A^{\mathsf T}\ \lambda_{\mathrm T}\mathsf I]$
  gives $(\mathsf A^{\mathsf T}\mathsf A+\lambda_{\mathrm T}^2\mathsf I)\boldsymbol a=\mathsf A^{\mathsf T}\boldsymbol b+\lambda_{\mathrm T}^2\boldsymbol a_0$
  *(compiler check, not in the sources)*. Eq. (58) writes $\tilde\epsilon_c$
  for the progress-variable dissipation that Eq. (27) calls
  $\tilde\chi_c$. After Eq. (59), $T_u$ and $T_b$ are called "the burned
  and unburned temperature values", reversed against the subscripts and
  the equation.
- **Citation labels.** In §3.1.3 the steady-flamelet predictions of
  Figs. 29–30 are attributed to ref. [196], which the printed list gives
  as the measurement paper; the captions attribute them to ref. [206]. In
  §3.4.3 the furnace's vitiated-air composition is cited to ref. [13], a
  combustion textbook in the list, and the furnace study to "Labahn and
  Devaud [187]", while ref. [187] is the four-author CMC–CSE comparison.
- **Notation of the Germano analogy.** §2.2 prints the dynamic
  Smagorinsky model with the coefficient to the first power,
  $-2C_s\Delta^2|\bar S_{ij}|\bar S_{ij}$, the role of $C_s^2$ in the
  registry form $\nu_t=(C_s\Delta)^2|\bar S|$ of the
  [Smagorinsky model](/methods/smagorinsky-model.md).

# Citations

- [Salehi et al. (2024)](/sources/salehi-2024.md) — §1, Eq. (1) (first-moment closure, closure families, LES resolution); §2.1, Eqs. (2)–(4), Fig. 1, Table 2 (CMC hypothesis and transport, a priori illustration); §2.2, Eqs. (5)–(7), Table 1 (CSE identity, ensembles, Germano analogy); §2.3, Eqs. (8)–(10), Fig. 2; §2.4, Eqs. (11)–(14), Fig. 44 (DCSE); §2.5–2.6, Eq. (15), Figs. 3–5 (ensemble selection, cost, parallel inversion); §2.7, Eqs. (16)–(31), Figs. 6–8 (presumed and joint PDFs, scalar transport); §2.8.3 (detailed chemistry, elemental conservation); §2.9.1–2.9.5, Eqs. (39)–(56), Figs. 13–18 (ill-posedness, Picard condition, Tikhonov, TSVD, parameter choice, solvers, NNLS, Bernstein polynomials); §2.10, Table 3 (CSE against CMC); §3.1.1, Figs. 19–21; §3.2.1, Fig. 34; §3.2.2, Eq. (58), Figs. 38–43; §3.3.2, Table 6; §3.4.3; §4.1–4.3.
- [Posch et al. (2025)](/sources/posch-2025.md) — §4.7; §5.2.3, Table 10 (CMC in LES of a dual-fuel engine with CSE as its LES formulation; passing mention).
