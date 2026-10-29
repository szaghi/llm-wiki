---
type: Method
title: "Conditional moment closure"
description: "Conditional moment closure models turbulent reaction rates by transporting species means conditioned on mixture fraction or progress variable and evaluating the rate at these conditional means, integrated against a presumed PDF; this page gives its hypothesis, transport equation, closures, cost, relation to flamelets and engine applications."
status: established
aliases: [CMC, first conditional moment closure, first conditional moment closure hypothesis, conditional moment closure model, incomplete stirred reactor, ISR]
tags: [combustion, rans, les, presumed-pdf]
timestamp: 2026-10-29T05:12:00Z
---

# Conditional moment closure

**Conditional moment closure** (CMC), introduced by Klimenko and by Bilger,
closes the mean (RANS) or filtered (LES) chemical source term of a
turbulent reacting flow by working with species and temperature
**conditioned** on a scalar that describes the state between fuel and
oxidizer (mixture fraction, non-premixed) or between fresh and burnt gas
(a progress variable, premixed). The reaction rate is evaluated at the
conditional means and integrated against a presumed PDF of the
conditioning scalar; the conditional means obey their own transport
equations, solved on a grid coarser than the flow grid because conditional
quantities vary little in space. The bundle's accounts are two reviews:
[Posch et al. (2025)](/sources/posch-2025.md), §4.7 and §5.2.3, for
internal-combustion-engine CFD, and
[Salehi et al. (2024)](/sources/salehi-2024.md), §2.1, §2.10, as the
parent model of [conditional source-term estimation](/methods/conditional-source-term-estimation.md),
which keeps the CMC hypothesis but replaces the conditional transport by an
inversion. Posch et al. place CMC next to transported PDF methods, to which
it is "related" while considering only conditional moments, and next to
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
and the [thickened flame model](/methods/thickened-flame-model.md) (§4).

**Page notation** (page-local, as on the conditional source-term estimation
page): $Y_k$ and $\dot\omega_k$ the mass fraction and net production rate
of species $k$; $Z$ the mixture fraction; $\xi$ the sample-space variable of
the conditioning scalar; $\tilde P(\xi;\boldsymbol x,t)$ its Favre PDF
(Posch et al. write $\bar P$ in Eq. 51, kept below as printed);
$\overline{\varphi\,|\,\xi}$ the mean of $\varphi$ conditioned on the scalar
taking the value $\xi$, $\widetilde{\varphi\,|\,\xi}$ its Favre form;
$Q_k(\xi)=\overline{\rho Y_k\,|\,\xi}/\overline{\rho\,|\,\xi}$ the Favre
conditional mean of $Y_k$; $\chi_\xi$ the scalar dissipation rate of the
conditioning scalar (bare $\chi$ is the Spalart–Allmaras ratio of the
registry); $\mathcal D$ the molecular diffusivity.

## The conditional moment closure hypothesis

The unconditional and conditional means are linked by the PDF (Posch et
al., Eq. 51):
$$\bar\rho\,\tilde Y_k=\int_0^1\overline{\rho Y_k\,|\,\xi}\;\bar P(\xi;\boldsymbol x,t)\,\mathrm d\xi .$$
The **first conditional moment closure hypothesis**, as Salehi et al. cite
it from Bilger and from Klimenko and Bilger, evaluates the rate at the
conditional means (§2.1, Eq. 2):
$$\tilde{\dot\omega}_k\approx\int_0^1\dot\omega_k\big(\overline{\rho\,|\,\xi},\widetilde{Y_k\,|\,\xi},\widetilde{T\,|\,\xi}\big)\,\tilde P(\xi)\,\mathrm d\xi .$$
Evaluating the rate at the unconditional mean state instead is
"ordinarily unacceptably inaccurate" (Salehi et al., §1, Eq. 1); in their a
priori illustration on a DNS of a premixed methane–air flame the filtered
CO$_2$ rate in one LES cell is 26.2 s⁻¹, the unconditional evaluation
gives 37.0 s⁻¹ (41% error) and the conditional hypothesis with the exact
DNS PDF 28.1 s⁻¹ (7%) (§2.1, Fig. 1, Table 2). Posch et al. contrast the
two families: flamelet models compute flame-surface statistics and a
laminar reactive–diffusive structure in the distance normal to the flame
surface, whereas CMC computes conditional moments "at a fixed point in
space and time" in mixture-fraction space (§4.7).

## Transport of the conditional means

The balance equation of the Favre conditional means, as Posch et al. print
it after Klimenko and Bilger (§4.7, Eq. 53), is
$$\overline{\rho\,|\,\xi}\;\frac{\partial Q_k}{\partial t}=-\overline{\rho u_j\,|\,\xi}\;\frac{\partial Q_k}{\partial x_j}+\overline{\rho\chi_\xi\,|\,\xi}\;\frac{\partial^2Q_k}{\partial\xi^2}+\overline{\dot\omega_k\,|\,\xi}+E_{Q,k}+E_{Y,k},$$
with $E_{Q,k}$ a molecular-diffusion term and $E_{Y,k}$ a
turbulent-fluctuation term (page-local), both neglected, as the authors
cite Veynante and Vervisch. Salehi et al. write the same balance per unit
conditional density with the conditional turbulent flux in divergence form
(§2.1, Eq. 4):
$$\partial_tQ_k+\widetilde{u_j\,|\,\xi}\,\partial_jQ_k+\frac{\partial_j\big(\bar\rho\,\tilde P\,\mathcal F_{k,j}\big)}{\bar\rho\,\tilde P}=\widetilde{\chi_\xi\,|\,\xi}\;\partial_\xi^2Q_k+\widetilde{\dot\omega_k\,|\,\xi},$$
$\mathcal F_{k,j}$ (page-local) the flux of fluctuations about the
conditional means. Three terms are unclosed (Posch et al., §4.7):

- the **conditional velocity**, in general replaced by the Favre mean
  velocity;
- the **conditional reaction rate**, closed at first order by a Taylor
  expansion of the Arrhenius rate constants in the conditional mean
  temperature with the higher moments neglected, after Swaminathan and
  Bilger;
- the **conditional scalar dissipation rate**, modelled with a presumed
  $\beta$-shaped PDF.

## Grids and cost

The number of additional balance equations is the number of species times
the number of conditioning values, which makes CMC "computational
demanding" (Posch et al., §4.7). According to Salehi et al., non-premixed
CMC typically uses 50–100 mixture-fraction points, and its spatial grid is
much coarser than the flow grid since conditional gradients are small: they
cite a
$4\times4\times64$ CMC grid inside a $96\times96\times320$ LES of Sandia
flame D and a $23\times23\times23$ CMC grid for flame F, with frequent
local extinction (§2.1, §2.2). In engine CFD the CMC domain is reduced
further: collapsing the azimuthal direction gives a two-dimensional CMC
grid inside a three-dimensional CFD case, which De Paola et al., as Posch
et al. cite them, found to reproduce the full three-dimensional
formulation; all five RANS diesel studies of their Table 10 use such
two-dimensional axisymmetric CMC grids with reduced n-heptane mechanisms
(§4.7, §5.2.3, Table 10). Posch et al. name the collapse of a spatial
dimension and low-dimensional manifolds for the chemistry as the remedies
for the cost (§5.2.3).

## Relation to flamelets

The conditioning on mixture fraction ties CMC to the
[flamelet concept](/methods/flamelet-tabulated-chemistry.md). Posch et al.
(§4.7) print two positions side by side:

- Swaminathan and Bilger: the first-moment CMC equations are identical to
  the flamelet equation for homogeneous isotropic turbulence, but their
  physical meaning differs substantially: the flamelet approach is local
  and CMC semi-global, CMC needs no assumption on the flame topology, and
  it accounts for convective fluxes in all three directions in
  inhomogeneous flows, the flamelet approach only normal to the
  stoichiometric surface;
- Peters: since the different derivations lead to the same equations,
  "the essential underlying assumptions must be the same and the same
  physics is captured".

Klimenko's overview of the relation between CMC and unsteady flamelets is
cited without detail.

## Against conditional source-term estimation

In a RANS comparison of CMC and CSE in one code for the Sandia flames D, E
and F, which Salehi et al. reproduce (§2.10, Table 3), both give similar
results for flame D; for flame E CSE reproduces the local-extinction
effects, too strongly, while CMC "could not capture the correct trends";
neither does well for flame F; CMC needs more computational resources and
is more sensitive to the inlet conditions and to the model of the
conditional scalar dissipation. Salehi et al.'s Table 1 sets out the
difference of principle: both rest on the CMC hypothesis and on a presumed
PDF, CMC transports the conditional moments and CSE the unconditional ones,
and only CSE needs conditional homogeneity over an ensemble of cells,
which CMC does not need but uses predominantly to reduce cost (detail on
[conditional source-term estimation](/methods/conditional-source-term-estimation.md)).

## Engine applications

Posch et al. (§5.2.3, Table 10) review CMC on compression-ignition engine
platforms; they report the claims of the cited studies without
independent assessment:

- De Paola et al. integrate a first-order CMC solver into a finite-volume
  RANS code with a sliding-grid convective term and a 31-species
  n-heptane mechanism, and conclude that further pollutant and flame-front
  measurements are needed for a detailed validation;
- Bolla et al. add a two-equation soot model to the same methodology for
  an optical heavy-duty diesel engine;
- Trivedi et al. propose an **incomplete stirred reactor** (ISR), a spatial
  integration of the CMC equations as a post-processing step for soot
  models, and find the CMC two-equation soot approach in good agreement
  with experiment while ISR overestimates soot mass fraction and particle
  size;
- Huang et al. apply CMC in LES to a diesel-pilot natural-gas dual-fuel
  engine, using conditional source-term estimation for the LES formulation
  and low-dimensional manifolds for 159-species and 55-species
  mechanisms, and claim agreement with measured in-cylinder pressure and
  emissions.

## Qualifications

- **Evidence.** Both sources are reviews; neither source reports
  a new CMC computation, and the comparisons with experiment and with CSE
  are those of the cited studies.
- **Scalar-dissipation factor in Posch et al.** The review defines
  $\chi_{\mathrm{st}}=2\mathcal D_{\mathrm{st}}|\nabla Z|^2_{\mathrm{st}}$
  (Eq. 20), prints the unsteady flamelet equation with $(\chi/2)\,\partial^2Y_k/\partial Z^2$
  (Eq. 54) and the CMC balance with $\overline{\rho\chi\,|\,Z}\,\partial^2Q_k/\partial Z^2$
  without a factor one half (Eq. 53), and states that the first-moment
  CMC equations are identical to "the flamelet equation (Eq. (55))"; Eq.
  (55) is the PDF mapping integral, and with one definition of $\chi$ the
  dissipation coefficients of Eqs. (53) and (54) differ by a factor two
  *(compiler check, not in the sources)*. Salehi et al.'s Eq. (4) also
  carries the conditional dissipation without a factor; their variance
  equation has the sink $-2\bar\rho\tilde\chi_Z$ (Eq. 21).
- Posch et al. index species and space with the same letter $i$ in Eq.
  (53); the page writes $k$ for species and $j$ for space.

# Citations

- [Posch et al. (2025)](/sources/posch-2025.md) — §4 (classification); §4.7, Eqs. (51)–(53) (CMC hypothesis, balance equation, closures, cost, relation to flamelets); §4.8, Eq. (54); §3.3.2, Eq. (20); §5.2.3, Table 10 (engine applications, two-dimensional CMC grids, ISR, CMC-LES with CSE).
- [Salehi et al. (2024)](/sources/salehi-2024.md) — §1, Eq. (1); §2.1, Eqs. (2)–(4), Fig. 1, Table 2 (first conditional moment hypothesis, a priori illustration, CMC transport, CMC grids); §2.2, Table 1 (CMC against CSE assumptions); §2.7.1, Eq. (21); §2.10, Table 3 (RANS comparison with CSE for Sandia flames D, E, F).
