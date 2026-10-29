---
type: Source
title: "Salehi et al. (2024) — Advances and challenges of the Conditional Source-term Estimation model for turbulent reacting flows"
description: "Review of Conditional Source-term Estimation, a turbulence–chemistry closure that recovers conditional means by regularized inversion of an integral equation over cell ensembles: theory, doubly conditional and localized variants, presumed PDFs, chemistry coupling, Tikhonov regularization and RANS and LES applications to jet, premixed, lifted, spray and MILD flames."
resource: "doi:10.1016/j.pecs.2024.101172"
source_kind: paper
authors: [Salehi M.M., Devaud C., Bushe W.K.]
year: 2024
venue: "Prog. Energy Combust. Sci. 104:101172"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Progress_in_Energy_and_Combustion_Science_Salehi_Advances_and_challenges_of_the_Conditional_Source-term_Estim.pdf"
tags: [review, combustion, tabulated-chemistry, a-priori-a-posteriori]
timestamp: 2026-10-28T17:05:00Z
---

# Summary

Salehi et al. (2024) review
[Conditional Source-term Estimation](/methods/conditional-source-term-estimation.md)
(CSE), a turbulence–chemistry interaction closure for the mean or filtered
chemical source term in RANS and [LES](/definitions/large-eddy-simulation.md)
of turbulent combustion. Bushe and Steiner introduced it in 1999 as an LES
extension of conditional moment closure (CMC). Like CMC, CSE evaluates the
reaction rate at the conditional means of density, species and temperature
(the first conditional moment closure hypothesis) and integrates it against
a presumed PDF of the conditioning variable: mixture fraction in
non-premixed flames, a reaction progress variable in premixed ones, both in
partially premixed ones. Unlike CMC, it solves no transport equation for
the conditional means. It transports the unconditional Favre-filtered
scalars and recovers the conditional means by inverting a Fredholm integral
equation of the first kind over an ensemble of cells within which they are
assumed homogeneous. The authors liken this to the Germano identity of the
[dynamic procedure](/methods/dynamic-procedure.md) for the
[Smagorinsky](/methods/smagorinsky-model.md) coefficient. The inversion is
ill-posed and must be regularized.

The theory part covers the CMC hypothesis, the discretized inverse problem,
doubly conditional CSE, ensemble selection on parallel machines, presumed
PDFs (β, flamelet, linear-eddy and joint PDFs), chemistry coupling
(trajectory-generated manifolds, [flamelet tabulation](/methods/flamelet-tabulated-chemistry.md),
laminar flamelet decomposition, detailed chemistry) and regularization:
SVD, the Picard condition, zeroth- and first-order Tikhonov, truncated SVD,
parameter selection, NNLS, and a Bernstein-polynomial "localized CSE". The
applications part reviews [a priori](/definitions/a-priori-and-a-posteriori-testing.md)
tests on [DNS](/definitions/direct-numerical-simulation.md) (among them a
[temporal mixing layer](/benchmarks/temporal-mixing-layer.md) and premixed
flames in [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)),
and RANS and LES of jet, bluff-body, buoyant and sooting flames, premixed
Bunsen and V-flames, lifted flames, engines, sprays and MILD combustion.
Some runs use [OpenFOAM](/software/openfoam.md) and
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) or [$k$-$\omega$](/methods/k-omega-model.md)
RANS. The review names the presumed or joint PDF as the largest error
source in a priori tests and states that CSE "has reached a certain level of maturity" in regularization. The
[thickened flame model](/methods/thickened-flame-model.md) is listed among
the alternative closures. Most evidence is figures reproduced from the
cited works.

# Version read

Version of record (Elsevier review article; received 27 March 2022,
revised 22 June 2024, accepted 23 June 2024, available online 10 July 2024),
38 pages, all read; equation pages and Table 4 also checked visually. Page
1 matches the Crossref metadata; no identity problem.

# Key claims

Page-local symbols are defined in the Notation map ($\xi$ the
conditioning sample-space variable, $\mathsf A$, $\boldsymbol a$,
$\boldsymbol b$ the discretized inverse problem with $N_{\mathrm e}$ cells and $N_{\mathrm b}$
bins, $\lambda_{\mathrm T}$ the Tikhonov parameter, $\varsigma^{\mathsf A}_j$ the singular values of $\mathsf A$, as on the concept page).

1. Evaluating reaction rates at the mean or filtered scalars ("first-moment closure", Eq. 1) is ordinarily unacceptably inaccurate, and a turbulence–chemistry model is almost always required, in LES too, because extinction correlates with the smallest scales removed by the filter (§1). **Stated**
2. In an a priori test on DNS of a freely propagating premixed CH$_4$–air flame, the filtered CO$_2$ production rate in one LES cell is 26.2 s$^{-1}$; first-moment closure gives 37.0 s$^{-1}$ and the first conditional moment hypothesis (with the exact DNS PDF) 28.1 s$^{-1}$, errors of 41% and 7% (§2.1, Fig. 1, Eq. 3, Table 2). **Shown**
3. CSE replaces the CMC conditional transport equation (Eq. 4) by an inversion of $\tilde\varphi=\int_0^1\widetilde{\varphi|\xi}\,\tilde P(\xi)\,d\xi$ over an ensemble of cells in which the conditional means are homogeneous; Eq. (7) is a Fredholm integral equation of the first kind (§2.2). **Derived**
4. The CSE approach is analogous to the dynamic Smagorinsky procedure: the Germano identity plays the role of Eq. (6), and the homogeneity of the coefficient at the test-filter level that of the CSE homogeneity assumption (§2.2). **Stated**
5. A plain least-squares solution of $\mathsf A\boldsymbol a=\boldsymbol b$ is non-physical (oscillatory); Tikhonov regularization with a laminar-flame prior gives a smooth solution (§2.3, Eqs. 9–10, Fig. 2). **Shown**
6. The test-to-LES filter ratio is often 2 to 3 in dynamic SGS models but much larger in CMC and CSE, e.g. a $4\times4\times64$ CMC grid inside a $96\times96\times320$ LES grid for Sandia flame D, and $23\times23\times23$ for flame F (§2.2). **Stated**
7. The reacting cells per ensemble must greatly exceed the unknowns $N_{\mathrm b}$: $\mathcal O(10^3)$ for single and $\mathcal O(10^4)$ for double conditioning, from $\mathcal O(10)$ data per parameter; reacting cells are those with $\tilde c(1-\tilde c)$ above a threshold between $10^{-2}$ and $10^{-3}$ (§2.5, Eq. 15). **Stated**
8. Typical bin counts are $N_{\mathrm b}=40$ (LES of Sandia flames) and 50 (Bunsen and spray flames), and 500 to 1000 for doubly conditional CSE (e.g. 50 mixture-fraction × 10 oxidizer-split bins); examples: 1.5 million cells in 64 ensembles ($N_{\mathrm e}\approx24\,000$, $N_{\mathrm b}=500$); 1 638 400 cells in 800 ensembles of 2048 cells ($N_{\mathrm b}=50$) (§2.5). **Stated**
9. The inversion costs $\mathcal O(N_{\mathrm b}^2N_{\mathrm e})$, so on one processor the number of ensembles does not change the cost but in parallel runs it does; in LES of a lifted flame with one ensemble per processor the cost per step was 32, 67, 42, 44 and 50 CPU s for cases a–e (case a with 48, case c with 24 ensembles), the authors stating that the cost decreases as the number of ensembles increases, and 24 ensembles were chosen because 48 occasionally left too few reacting cells near the flame base (§2.5, Fig. 4). **Shown** (from ref. [39])
10. The CSE kernel is ill-posed in Hadamard's sense: zero singular values give non-uniqueness and small ones amplify modelling errors in $\boldsymbol b$; with $10^{-10}$ Gaussian noise added to experimental conditional CO$_2$ data the Picard condition fails (200 bins, one ensemble of a CH$_4$–air jet flame) (§2.9.1, Eqs. 39–41, Fig. 13). **Shown** (from ref. [173])
11. Truncated SVD and zeroth-order Tikhonov with a zero prior are both filter-function regularizations, with $f_j=1$ for $j\le k$ and 0 otherwise, and $f_j={\varsigma^{\mathsf A}_j}^2/({\varsigma^{\mathsf A}_j}^2+\lambda_{\mathrm T}^2)$ (§2.9.2, Eqs. 43–45, Fig. 14). **Derived**
12. First-order Tikhonov (first-difference smoothing matrix) needs less memory than zeroth-order Tikhonov with a previous-step prior, and is not recommended with laminar flamelet decomposition because neighbouring flamelets of a library need not have correlated weights; zeroth-order Tikhonov may need explicit smoothing afterwards (§2.9.2). **Stated**
13. NNLS enforces positive conditional averages but costs on average ten times the QR approach (§2.9.4). **Shown** (from ref. [61])
14. Expanding the conditional means in Bernstein polynomials (Eq. 53) and solving with NNLS (Eq. 56) regularizes by itself, reduces the unknowns from about 50 to fewer than 10, and allows ensembles of 16 LES cells a priori ("localized CSE"); an actual LES needs at least 27 cells per ensemble (§2.9.5, Fig. 18). **Shown** (from ref. [61])
15. In a RANS comparison of CMC and CSE in one code for Sandia flames D, E and F: similar results for D; for E CSE reproduced local-extinction effects (too strongly) where CMC did not capture the trends; neither did well for F; CMC needed more resources and was more sensitive to inlet conditions and conditional scalar-dissipation modelling (§2.10, Table 3). **Shown** (from ref. [187])
16. A priori tests on high-pressure heptane DNS: CSE with the DNS PDF performs very well, a β-PDF causes significant errors, and in doubly conditional CSE the joint-PDF model (β-PDF plus statistical independence) is by far the largest error source, larger than ensemble selection or inversion (§3.1.1, Fig. 21). **Shown** (from refs. [135, 190])
17. Laminar flamelet decomposition is bounded by its library: a steady library under-predicts NO in Sandia flame D, an unsteady one over-predicts it, and mixing libraries can "tune" the result (§3.1.2, Fig. 25). **Shown** (from ref. [168])
18. Hash tables for the manifold lookup and pre-tabulated PDF integrals cut the CSE share of total RANS cost for Sandia flames D and F from 85% (zeroth-order Tikhonov, unoptimized) to 10% with first-order Tikhonov and under 3% with degree-10 Bernstein polynomials (§3.1.2). **Shown** (from ref. [177])
19. In an a priori LES-context analysis (top-hat filter of 0.7 laminar flame thicknesses, $8\times8\times16=1024$ LES cells, DNS at Karlovitz numbers 6, 74, 540, 4100, 16 species and 35 reactions) the first conditional moment hypothesis error is insignificant at low and high Karlovitz number, the homogeneity error is significant with a single 1024-cell ensemble, and the inversion error is not significant relative to coarse-grid CMC (§3.2.1, Fig. 34). **Shown** (from ref. [61])
20. Elemental mass conservation is not guaranteed with detailed chemistry, since the conditional species come from an inverse problem; inverting for all species with an elemental-conservation constraint is proposed (§2.8.3). **Stated**
21. LES-CSE of the F3 Bunsen flame (128 disc ensembles) gives conditional H$_2$O following unstrained flamelets, while the Gülder Bunsen flame deviates from them; the over-predicted flame height is attributed to the simple scalar-dissipation model of Eq. (58) and is much improved with the linear-eddy model (§3.2.2, Figs. 38–41). **Shown** (from the cited works)
22. Localized CSE in RANS of the F3 and Gülder flames reproduces the flamelet conditional averages at 20% lower cost than regular CSE and predicts the Gülder flame height, which an unstrained flamelet model under-predicts (§3.2.2, Figs. 42–43). **Shown** (from ref. [68])
23. LES with doubly conditional CSE of lifted methane jet flames (3 302 400 cells, 24 ensembles) gives lift-off heights 30, 78 and 137 mm against the measured $30\pm7$, $80\pm11$ and $135\pm11$ mm at $Re=7000$, 12000 and 19500 (RANS: 29.5, 74.5, 129.5 mm) (§3.3.2, Table 6). **Shown** (from refs. [39, 40])
24. LES with doubly conditional CSE of the Delft jet-in-hot-coflow MILD flames under-predicts the lift-off height by 36% (DJHC-I 4100) and 44% (DJHC-I 8800) (§3.4.3). **Shown** (from ref. [57])
25. The joint or single PDF closure is the key open issue, "the largest source of error in a priori DNS calculations", whose error can exceed any improvement due to CSE; regularization has "reached a certain level of maturity" (§4.1). **Stated**
26. New users should start in RANS (the CSE routine is the same in RANS and LES) with single conditioning and Bernstein polynomials or zeroth-order Tikhonov; first-order Tikhonov is "most promising" but less tested; the extension of Bernstein polynomials to double conditioning "appears much more challenging" and Tikhonov regularization "more tractable" (§4.2–4.3). **Stated**

# Printed slips

- §1: "Many different TCI models have been proposed that can be classified into the following four categories:", followed by five numbered items.
- §2.3: "Thus, Eq. (13) is transformed into the following linear system of equations" (Eq. 8); Eq. (13) is the later doubly conditional equation, and the equation discretized is Eq. (7).
- §2.4 calls the kernel "a 2D $M\times N$ matrix", §2.9.1 "an $N\times M$ matrix"; Eq. (8) runs the row index over the $N$ cells.
- Eq. (53) sums $\sum_{j=1}^{N_B}\beta_jB_{j,N_B}$ from $j=1$, while Eq. (54), the text and Fig. 17 use $B_{0,N_B},\dots,B_{N_B,N_B}$ and name $B_{0,4}$ the reactant profile.
- Eq. (49) writes "$+\lambda^2\mathbf I\|\vec\alpha^*-\vec\alpha_0\|_2^2$", a matrix multiplying a scalar norm; §2.9.3 "the $Tr$ operator is the trance of the matrix".
- §3.2.1 cites "the CSE integral equation, Eq. (9)", the plain least-squares formula (the integral equation is Eq. 7), and "the transport equations for the conditional (Eq. (2))" scalars, where Eq. (2) is the CMC hypothesis and the conditional transport equation is Eq. (4).
- Eq. (58) writes the progress-variable scalar dissipation $\tilde\epsilon_c$, Eq. (27) and §2.7.2 $\tilde\chi_c$.
- Eq. (59): "here $T_u$ and $T_b$ are the burned and unburned temperature values".
- §3.1.3: "Also included in Figs. 29 and 30 are the previously published predictions using CMC [207] and steady flamelet model [196]", while the captions attribute the flamelet results to Brookes and Moss [206] and the printed title of ref. [196] is the measurement paper.
- §3.4.3: the vitiated-air composition of the furnace cites ref. [13], whose printed title is Williams' *Combustion Theory*; the furnace study is attributed to "Labahn and Devaud [187]", while ref. [187] is the CMC–CSE comparison for piloted jet flames by Labahn, Stanković, Devaud and Merci.
- §3.2.2: Fig. 36 is described as the RANS study of Salehi et al. [88], and its caption reads "Source: Image is taken from [68]".
- §2.9.2 "[41,54,57,64,64,67]"; nomenclature "TEI Turbulence–Chemistry Interaction" (TCI in the text) and "QMOM Quadratic Method of Moments" ("Quadrature" in §3.1.3); "Smooke and Giovangili's", "Madhipour", "Tikhonovov", "Karloitz", "Şteiner".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\varphi$ | $\langle\phi\rangle$ (RANS) or $\bar\phi$ (LES) | one symbol for both |
| $\tilde\varphi$, $\varphi''$ | $\langle\phi\rangle_\rho$, $\phi''$ (RANS) or $\tilde\phi$ (LES) | Favre average or filter |
| $\varphi'$ | fluctuation about the conditional mean (page-local) | **collision:** $\phi'$ is the Reynolds fluctuation |
| $\tilde\varphi_v$, e.g. $\tilde z_v$ | Favre variance $\widetilde{(z-\tilde z)^2}$ | |
| $\xi$, $\zeta$ | $\xi$ (page-local; $\xi_Z$ when the scalar is $Z$): sample-space variable of the conditioning scalar | the nomenclature gives $\xi$ for $c$ and $\zeta$ for $z$, §2.1 a generic $\xi$; **collision:** $\xi$ is also the reference coordinate of element methods |
| $\widetilde{\varphi\vert\xi}$, $\widehat{\varphi\vert\xi}$ | conditional mean; its value at the ensemble ("test-filter") level | **collision:** the hat is used for an ensemble, not a test-filtered field |
| $\tilde P_\xi$, $\tilde P_{zc}$ | Favre PDF of the conditioning variable; joint PDF | |
| $z$, $Z$; $c$ | mixture fraction; reaction progress variable | both cases of $z$ printed |
| $\mathbf A$, $\vec\alpha$, $\vec b$, $\vec\alpha_0$ | $\mathsf A$, $\boldsymbol a$, $\boldsymbol b$, $\boldsymbol a_0$ (page-local) | kernel, unknown conditional means, unconditional values, prior; **collision:** $\alpha$ is the DG blending factor |
| $M$, $N$ | $N_{\mathrm b}$, $N_{\mathrm e}$ (page-local) | bins and ensemble cells; **collision:** Mach number and polynomial degree |
| $\lambda$ | $\lambda_{\mathrm T}$ (page-local) | Tikhonov parameter; **collision:** Taylor microscale |
| $\sigma_j$, $\mathbf U$, $\Sigma$, $\mathbf V$ | $\varsigma^{\mathsf A}_j$, $\mathsf U$, $\Sigma$, $\mathsf V$: singular values and SVD factors of $\mathsf A$ (page-local) | §11's $\varsigma_i$ are those of the velocity gradient |
| $B_{j,N_B}$, $\beta_j$ | Bernstein basis of degree $N_B$, coefficients | **collision:** $\beta(\boldsymbol x)$ |
| $\mathcal D_k$, $\mathcal D$, $\mathcal D_t=\nu_t/Sc_t$ | $D_{\mathrm m}$ (§11), turbulent diffusivity | $Sc_t$ turbulent Schmidt number (page-local): 0.7 RANS, 0.4 or 0.7 LES |
| $\chi$, $\tilde\chi_z$, $\tilde\chi_c$, $\tilde\epsilon_c$ | scalar dissipation rates $\chi_z$, $\chi_c$ (page-local) | **collision:** bare $\chi$ is the SA ratio |
| $\tau$, $u'_\Delta$, $C_\nu$ | $\tau_{\mathrm{mix}}$, $u'_\Delta$ (§11), Lilly constant | mixing time $\Delta/u'_\Delta$ (LES) or $k/\varepsilon$ (RANS); **collision:** $C_\nu$ is the RNG constant of §11 |
| $-2C_s\Delta^2\lvert\bar S_{ij}\rvert\bar S_{ij}$ | $-2(C_s\Delta)^2\lvert\bar S\rvert\bar S_{ij}$ | the source's $C_s$ stands where the registry has $C_s^2$; $\lvert S_{ij}\rvert$ undefined in the source |
| $S_L$, $\delta_T$, Ka | $s_{\mathrm L}$ (§11), laminar thermal thickness, Karlovitz number | **collision:** $S_L$ is the Lundquist number |
| a priori | a priori | evaluation on filtered or coarsened DNS |

# Reference list

267 printed references, numbered [1]–[267] (Elsevier), with titles. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug; no cited key collides with an ingested source. Refs.
[247] and [249] print the same work (Maes et al., Combust. Flame 2016,
174:138–51) twice, and the resolver folds them. Refs. [263] and [264] print
identical titles in volumes 157 and 158. Ref. [266] prints garbled authors
("amd R. Weber SO, Bollettini U.") and ref. [209] a garbled year ("162");
their keys follow the resolver's decision. Ref. [203] is an undated web
item, ref. [217] an untitled URL and ref. [188] "submitted for
publication". Eleven articles in press print no volume or pages.

# Pages created or updated

Chunk 14 (2026-10-28), cited further in chunk 15. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Turbulent Prandtl number and turbulent heat-flux models](/definitions/turbulent-prandtl-number.md)
- [Conditional moment closure](/methods/conditional-moment-closure.md)
- [Conditional source-term estimation](/methods/conditional-source-term-estimation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Thickened flame model](/methods/thickened-flame-model.md)
- [OpenFOAM](/software/openfoam.md)
