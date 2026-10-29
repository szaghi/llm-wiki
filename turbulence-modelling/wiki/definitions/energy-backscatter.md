---
type: Definition
title: "Energy backscatter and the subgrid energy flux"
description: "Energy backscatter is a negative local subgrid energy flux, energy moving from subgrid to resolved scales; the sources define the flux, show that its local sign depends on the gauge of the subgrid stress and on the filter, and disagree in emphasis on whether models must reproduce it, remove it for stability, or admit it in stable form."
status: established
aliases: [backscatter, inverse energy transfer, subgrid-scale energy flux, interscale energy flux, local SGS dissipation]
tags: [les, sgs-model, eddy-viscosity, filtering]
timestamp: 2026-10-29T16:19:00Z
---

# Energy backscatter and the subgrid energy flux

The **local subgrid-scale energy flux** is

$$\Pi=-\tau_{ij}\bar S_{ij},$$

the rate at which the [subgrid stress](/definitions/large-eddy-simulation.md)
removes kinetic energy from the resolved field. $\Pi>0$ is forward transfer
(resolved to subgrid) and $\Pi<0$ is **backscatter**.
[Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.1, Eqs. 2.4–2.7)
writes the resolved energy budget with this flux. With the registry sign,
the subgrid term in the resolved-energy equation splits as

$$-\bar u_i\partial_j\tau_{ij}=D-\Pi,\qquad D=-\partial_j(\bar u_i\tau_{ij}),$$

where $D$ (page-local symbol) is a conservative spatial flux with zero
domain average. Hence $\langle\Pi\rangle$ is the net cascade rate, equal to
the dissipation $\varepsilon$ for a filter in the inertial range. The author
prints the stress with the opposite sign (the paper's $T=\bar S_{ij}\tau^S_{ij}$
is the registry's $\Pi$) and uses $\Pi$ as the cascade flux because it is
Galilean-invariant, scale-local and free of sweeping (citing Eyink and
co-workers).

For an eddy-viscosity model $\Pi=\nu_t\lvert\bar S\rvert^2$, so backscatter
requires $\nu_t<0$. Vela-Martín (2022, §2.2) recalls that negative eddy
viscosity "generally leads to critical numerical instabilities", as in the
local [dynamic procedure](/methods/dynamic-procedure.md), and is removed by
clipping or averaging.

## How much backscatter, and with which filter

In filtered DNS of linearly forced isotropic turbulence at $Re_\lambda=140$,
240 and 324 ($256^3$ to $1024^3$, 290 independent fields, filter scales
$0.08$–$0.65$ of the integral scale), Vela-Martín (2022, §5.3, Fig. 2)
measures the backscatter volume fraction $v^-$ (the fraction of the domain
with $\Pi<0$) and the net backscatter $f^-$ (minus the integral of the
negative part of $\Pi$ divided by the integral of $\Pi$); both symbols are
in registry §11:

- sharp Fourier filter: $v^-\approx0.5$, $f^-$ close to one;
- Gaussian filter: $v^-\approx0.15$, $f^-\approx0.05$;
- both grow as the filter scale decreases.

Backscatter is therefore not a property of the flow alone: its amount
depends on the filter kernel. The literature values that Vela-Martín
(§2.1) cites are about 40% of the domain for sharp filters and 15% for
Gaussian filters.

With a three-dimensional box filter at grid and test level,
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (§III.2, p. 15,
Fig. 5) find backscatter at 26% of the points of filtered DNS of forced
isotropic turbulence at $Re_\lambda=240$ for the smaller of their two
filters (filter size $\ell_\Delta=4$, with $\ell_\Delta$ the filter width
over twice the DNS grid spacing, registry §11, as on the
[fractional SGS model](/methods/fractional-sgs-model.md) page), and 30%
for a filter twice as wide ($\ell_\Delta=8$). They state, citing Piomelli et al. (1991), that the
fraction depends on the filter type.
The box-filter fractions lie between the Gaussian and sharp-filter values
above, from a different flow and filter scales *(compiler check, not in
the sources)*.

[Domaradzki (2024)](/sources/domaradzki-2024.md) (§3.1) cites
Piomelli et al. (1991) and Domaradzki, Liu & Brachet (1993) for the
finding that with a
sharp spectral filter the forward and inverse subgrid transfers are of the
same order and the net forward transfer is much smaller than each, in line
with the sharp-filter values of Vela-Martín (2022, §5.3) above; Domaradzki's
own conclusions are drawn for graded (Gaussian and box) filters.

In channel flow, [Kim et al. (2022)](/sources/kim-2022.md) (§III E,
Fig. 14a) filter DNS with a cut-off filter in the homogeneous directions
and describe the backscatter of the filtered DNS as "a non-negligible
quantity" with "considerably large negative dissipation" in the PDF of
the subgrid dissipation at $y^+\approx15$ and 50 (§III C).

In a transitional flow, [Cao et al. (2022b)](/sources/cao-2022-c.md)
(§IV B, Eqs. 17–18, Figs. 5–6, Table I) box-filter their DNS (case TG3
of their earlier paper, cited) of the compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
($M=0.1$, $Re=1600$) by merging $2^3$ cells, a positive kernel that keeps
$k_{\mathrm{sgs}}>0$, and find forward and backward Favre-filtered
transfer $\Pi=-\tau_{ij}\tilde S_{ij}$ coexisting in space at
$t=2.5$–15. Its volume average is small: $1.3\times10^{-5}$,
$1.3\times10^{-4}$, $5.1\times10^{-4}$ and $1.3\times10^{-4}$ at $t=2.5$,
5, 10, 15, against a solenoidal physical dissipation of $8.8\times10^{-4}$,
$4.1\times10^{-3}$, $1.1\times10^{-2}$ and $4.5\times10^{-3}$, and the
volume-averaged kinetic energy is $10^2$–$10^4$ times the mean subgrid
energy. They conclude that on such grids the numerical dissipation of the
scheme can exceed the filtered subgrid production, so that explicit
modelled dissipation is "not required" (see
[implicit LES](/definitions/implicit-les.md)).

The filter dependence extends to filters that mimic a solver.
[Wu & Lele (2026)](/sources/wu-2026.md) (§3.2.2, Fig. 4) compare the
filtered-DNS fields of $\Pi$ for three kernels at the same width: a box
filter, a compact positive raised-cosine kernel, and a box filter followed
by the two-thirds dealiasing cutoff of a Fourier-spectral code. The box and
raised-cosine fields look alike. The dealiased one is "far more
oscillatory", and its probability density of $\Pi$ has "far more variance";
the density peak is highest for the box filter, then the raised-cosine
kernel, with "quite a large gap" to the dealiased filter. The authors do not
discuss the sign of $\Pi$. They conclude that a network trained on
box-filtered data meets a different flux distribution in a dealiased
spectral solver, and train on several filters instead (see
[neural-network SGS models](/methods/neural-network-sgs-model.md)); their
training loss includes the error in $\Pi$ beside the stress error (§3.1,
Eq. 3.9).

## Gauge dependence

The resolved equations depend on $\tau_{ij}$ only through its divergence,
so adding any symmetric divergence-free tensor leaves the dynamics, the
total term $D-\Pi$ and $\langle\Pi\rangle$ unchanged, but changes the local
$\Pi$ and $D$ (Vela-Martín 2022, §3, Eqs. 3.1–3.5; idea attributed to
Jiménez 2016). Vela-Martín minimizes $\langle\Pi^2\rangle$ over all
admissible stresses, i.e. symmetric tensors with the divergence of the
filtered-DNS stress. The method is a projected gradient descent with an
$L^2$ projector solved spectrally (§4, Apps. A–B). Starting from the
filtered-DNS stress, the optimization:

- reduces backscatter by about three orders of magnitude, to
  $v^-\approx10^{-3}$ and $f^-\approx10^{-4}$, nearly independently of
  Reynolds number, filter scale and filter type (§6.1–6.2, Figs. 3–4);
- leaves the spatial flux almost unchanged (correlation 0.9 between old
  and new $D$) while the new $\Pi$ is nearly uncorrelated with the old one
  (correlation about 0.01) (§6.3, Fig. 5);
- removes the scale growth of the flatness of $\Pi$, whereas the flatness
  of the gauge-invariant $D-\Pi$ still grows (§6.3, Fig. 6). Intermittency
  need not be modelled in the flux but persists in the total subgrid
  interaction;
- leaves isolated backscatter spots of size about three filter widths and
  intensity about $-0.1\langle\Pi\rangle$ (§6.4, Fig. 7).

The equivalent stresses (filtered-DNS and optimized) correlate only at
0.4–0.6 with each other (§6.3), so poor a priori correlation of a model with
the filtered-DNS stress is not by itself evidence of poor modelling (§8).

## Optimal eddy viscosity (inline)

The eddy viscosity that best fits a given stress in the $L^2$ sense
reproduces its local flux exactly (Vela-Martín 2022, §7.1, Eqs. 7.2–7.5).
Translated to the registry sign, minimizing
$\int(-2\nu_t\bar S_{ij}-\tau_{ij})^2\,dV$ pointwise gives

$$\nu_t^*=-\frac{\tau_{ij}\bar S_{ij}}{2\bar S_{ij}\bar S_{ij}}=\frac{\Pi}{\lvert\bar S\rvert^2},\qquad \nu_t^*\lvert\bar S\rvert^2=\Pi$$

*(compiler check, not in the sources)*. It is gauge-dependent:
negative over a large fraction of the domain for the filtered-DNS stress,
positive almost everywhere for the optimized one. In this sense a purely
dissipative "perfect" eddy-viscosity model exists for the flux. The author
cautions that it may be hard to express in resolved quantities.

The same projection is used as an a priori diagnostic by [Abe (2021)](/sources/abe-2021.md)
(§IV C, Eq. 17): the "equivalent SGS eddy viscosity"
$-\tau^d_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})$ of a reference or model
stress, which the author notes reproduces exactly its resolved/subgrid
energy transfer, forward and backward. It equals $\nu_t^*$
above, since $\bar S_{ii}=0$ *(compiler check, not in the sources)*. Abe
compares it between filtered fine-LES data and five models in a free shear
layer (see [Smagorinsky model](/methods/smagorinsky-model.md) and
[scale-similarity models](/methods/scale-similarity-model.md)).

[Zhao et al. (2021)](/sources/zhao-2021-c.md) (§III.D, Eqs. 21–23) use the
same projection as a coupling device, not a diagnostic: their gas-kinetic
solver accepts only a scalar eddy viscosity, so the stress of a dynamic
Clark (gradient plus Smagorinsky) model is replaced by
$\nu_t=-\tau_{ij}\bar S_{ij}/(2\bar S_{ij}\bar S_{ij})$, obtained by matching
the dissipation $-\tau_{ij}\bar S_{ij}=2\nu_t\bar S_{ij}\bar S_{ij}$. This is
$\nu_t^*$ of the model stress, so the local flux $\Pi$ of the
model is kept, backscatter included, while its tensorial structure is lost
*(compiler check, not in the sources)*. Whether negative values of this
viscosity are clipped is not stated (see
[gradient model](/methods/gradient-model.md)).

## Energy-transfer-free remainder and anisotropic redistribution

[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§II A, Eqs. 3–5;
following Abe 2019 and Inagaki & Kobayashi 2020, as cited there) use the same
optimal eddy viscosity to split the deviatoric subgrid stress of filtered
DNS into a part that carries the whole local energy transfer and a
remainder that carries none:

$$\tau^d_{ij}=-2\nu_t^*\bar S_{ij}+\tau^{\mathrm{ani}}_{ij},\qquad \tau^{\mathrm{ani}}_{ij}\bar S_{ij}=0,$$

with $\tau^{\mathrm{ani}}_{ij}$ (registry §11) the "extra anisotropic" stress.
The authors' "ideal" eddy viscosity $-\tau_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})$
is $\nu_t^*$ above; they note that it is negative where the
flow backscatters and call the decomposition "arbitrary" (§II A).
Inserting it in the budget of the resolved Reynolds stress
$R^{\mathrm{res}}_{ij}=\langle\bar u_i'\bar u_j'\rangle$ (fluctuations about
the Reynolds average of the filtered field) splits the subgrid
dissipation tensor into an eddy-viscosity dissipation and an **anisotropic
redistribution** $\xi^{\mathrm{AR}}_{ij}=\langle\tau^{\mathrm{ani}}_{i\ell}\partial_\ell\bar u_j'+\tau^{\mathrm{ani}}_{j\ell}\partial_\ell\bar u_i'\rangle$
(registry §11; positive = productive) (§II C, Eqs. 8–9). Unlike the
pressure redistribution it is not traceless; from
$\langle\tau^{\mathrm{ani}}_{ij}\bar S_{ij}\rangle=0$ its trace is the
exchange of the anisotropic stress with the mean strain,
$\xi^{\mathrm{AR}}_{ii}=-\langle\tau^{\mathrm{ani}}_{ij}\rangle\langle\bar S_{ij}\rangle$
(Eq. 10).

In channel flow at $Re_\tau=400$, filtered with a sharp cut-off in $x$ and
$z$ at a medium filter ($\Delta x^+,\Delta z^+=52.4,26.2$) and a coarse one
($105,52.4$) (§III, Figs. 3–8):

- for the medium filter $\tau^{\mathrm{ani}}_{ij}$ is negligible in the mean
  shear stress and $\xi^{\mathrm{AR}}$ negligible in the resolved kinetic
  energy budget; for the coarse filter the mean anisotropic shear stress is
  comparable to the eddy-viscosity part and $\xi^{\mathrm{AR}}$ is
  productive near the wall;
- for the coarse filter the total subgrid dissipation of the resolved energy
  is productive, an averaged backscatter, at $y^+\approx12$;
- the spanwise component $\xi^{\mathrm{AR}}_{33}$ is productive at all
  heights for both filters and, for the coarse filter, comparable to the
  pressure redistribution for $y^+<100$; its spectrum peaks at
  $\lambda_z^+\approx130$, the streak spacing, from which the authors infer
  a role of the anisotropic stress in generating streamwise vortices
  (§IV A 2, Fig. 12).

They argue that a stochastic backscatter forcing $a_i$ (Leith; Langford &
Moser, as cited there) cannot reproduce this productive term, because
$\langle\bar u_i'a_j\rangle=0$; a deterministic anisotropic stress is needed
(§IV B). Which a priori models reproduce $\xi^{\mathrm{AR}}$ is on the
[scale-similarity](/methods/scale-similarity-model.md) and
[gradient-model](/methods/gradient-model.md) pages.

## Model backscatter and stability

[Prakash et al. (2022)](/sources/prakash-2022.md) (§II, Eqs. 4–8) treat
backscatter of a *model* stress $\tau^{\mathrm M}_{ij}$ (page-local) as a
stability risk. With periodic or homogeneous boundaries and no forcing the
resolved energy decays if and only if
$\int_\Omega\tau_{ij}\bar S_{ij}\,d\Omega\le\int_\Omega2\nu\bar S_{ij}\bar S_{ij}\,d\Omega$,
so excessive model backscatter can make it grow. They enforce the
sufficient pointwise condition of no model backscatter,
$\Pi^{\mathrm M}=-\tau^{\mathrm M}_{ij}\bar S_{ij}\ge0$, and say it is
sufficient, not necessary. Two procedures do so for structural models such
as the [gradient model](/methods/gradient-model.md): standard clipping,
which zeroes the model stress where $\Pi^{\mathrm M}<0$ (attributed to Liu,
Meneveau & Katz), and their optimal clipping, which subtracts from the
stress its projection on $\bar S_{ij}$ there, i.e. adds the eddy viscosity
$\max(-\Pi^{\mathrm M},0)/\lvert\bar S\rvert^2$. Both set the local model
flux to zero where the base model backscatters. A priori on box-filtered
isotropic turbulence at $Re_\lambda=418$, anisotropic (book- and
pencil-type) filters lower the mean model dissipation, which the authors
partly attribute to more model backscatter (§III.A.2, Figs. 2–3).

The founding paper of the [dynamic procedure](/methods/dynamic-procedure.md)
keeps the negative coefficient.
[Germano et al. (1991)](/sources/germano-1991.md) (§I) list the inability
to represent backscatter among the limits of the
[Smagorinsky model](/methods/smagorinsky-model.md). Their modelled
dissipation, $\varepsilon_{\mathrm{SGS}}=m^{\mathrm G}_{ij}\bar S_{ij}$
(page-local, the model stress contracted with the strain, i.e. $-\Pi$ of
the model in the registry sign), is proportional to the plane average
$\langle L_{ij}\bar S_{ij}\rangle$ of the resolved stress. That average
can take either sign, so the model does not rule out backscatter (§II).
With plane averaging the backscatter is not localized; averaging Eq. (15)
locally would localize it. No clipping is applied. In their LES of
transitional channel flow, "for $t\le185$ the eddy viscosity was negative
for significant regions of the channel", which they present as evidence
that the model predicts average backscatter (§III; time units not
stated, no figure).

Two further sources tie the removal of backscatter from the
[dynamic procedure](/methods/dynamic-procedure.md) to stability.
Zhao et al. (2021, §III.A, Eq. 16) clip the plane-averaged dynamic
Smagorinsky coefficient to its positive part "so that backscatter is
eliminated", in wall-resolved channel LES at $Re_\tau=180$ and 395.
[Heinz (2020)](/sources/heinz-2020.md) (§2.1), reviewing hybrid RANS/LES,
states that dynamic LES which does not honour realizability, the dynamic
Smagorinsky model, is often computationally unstable, and that the
remedies, averaged dynamic parameters or added clipping parameters,
"reduce the backscatter ability of LES"; "fully realizable dynamic LES" is
said to be stable without either (citing Mokhtarpoor & Heinz).

Prakash et al. and Vela-Martín (2022) both arrive at models without local
backscatter, from different premises: stability of the resolved energy for
Prakash et al., the gauge freedom of the stress and the statistics of the
flux for Vela-Martín. The clipping constraint is imposed on one
representative of the model stress; by the gauge argument above, adding
to it a symmetric divergence-free tensor $T_{ij}$ (page-local) leaves the
resolved dynamics unchanged but shifts the local flux by
$-T_{ij}\bar S_{ij}$, which is not zero in general, so the constraint is
not gauge-invariant *(compiler check, not in the sources)*.

Clipping of this kind recurs as a stability device in the sources. Cao
et al. (2022b, §IV B) note that backscatter "cannot be modelled" by
implicit LES nor by explicit eddy-viscosity LES with positive static
coefficients, and that the dynamic coefficient, "usually clipped" to
non-negative values for stability, then misses it too.
[Li et al. (2022)](/sources/li-2022-k.md) (§II C, Eq. 15) read a negative
dynamic $C_s^2$ in their Reynolds-stress-model IDDES as backscatter and set
it to zero. [Wang et al. (2022)](/sources/wang-2022-j.md) (§IV) turn off
the backscatter of subgrid energy for their structural spatial
[gradient model](/methods/gradient-model.md) "to avoid numerical
instabilities", without printing the clipping formula.

## Backscatter of nonlocal and learned models

The sources reach different design choices from different questions.

- **Backscatter as a design goal.** [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md)
  (§I) list the absence of backscatter among the defects of earlier
  nonlocal models and design the dynamic
  [fractional SGS model](/methods/fractional-sgs-model.md) to produce it.
  A priori, only that model and
  the dynamic Smagorinsky model, of the four tested, give $\Pi<0$: 24% and
  20% of the points at the smaller filter, 25% and 18% at the larger,
  against 26% and 30% in filtered DNS. The dynamic Smagorinsky model
  over-predicts the tails of the PDF of $\Pi$, which the authors link to
  its need for averaging a posteriori (§III.2, Fig. 5). The dynamic
  coefficient is assumed spatially uniform and averaged over homogeneous
  directions against instability from "negative eddy-viscosity in
  prolonged periods of time" (§II.2); the a posteriori tests (spectra,
  energy decay, structure functions) do not measure backscatter (§IV).
- **Backscatter not needed.** In the reinforcement-learning SGS model of
  [Kim et al. (2022)](/sources/kim-2022.md) (§III C, §III E, Fig. 14) for
  channel flow at $Re_\tau=180$, a variant with negative dissipation
  clipped to zero (DRL180(clip)) predicts the mean velocity and the mean
  Reynolds shear stress almost as well as the unclipped model, and no
  model, learned or conventional, reproduces the large negative tail of
  the filtered DNS. The authors conclude that backscatter "is not a
  necessary condition" for at least those two statistics, the only
  training targets, and recall that the dynamic Smagorinsky model
  eliminates it by homogeneous averaging because inaccurate backscatter
  can make LES diverge. The unclipped model shows weak backscatter at
  $y^+\approx50$ without instability, so backscatter "does not necessarily
  cause numerical instability" (Fig. 14b). They add that backscatter is
  correlated with strong Reynolds shear stress in near-wall events
  (citing Piomelli et al.) and that training on more statistics
  (skewness, temporal correlation) might be needed to produce it. See
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

- **Backscatter predicted and stable.** The neural-network mixed SGS model
  of [Kang et al. (2023)](/sources/kang-2023.md) (§3.1, §3.3, Figs. 4, 6,
  8, 20) predicts all six stress components from $\bar S_{ij}$ and the
  resolved stress $L_{ij}$. With $\bar S_{ij}$ alone the network returns a
  stress aligned with $\bar S_{ij}$ and, like eddy-viscosity models, no
  backscatter. With $L_{ij}$ added it reproduces the PDF of $\Pi$ of
  filtered DNS, backscatter included, a posteriori in forced isotropic
  turbulence, and "LES becomes stable without any ad hoc procedures". The
  algebraic dynamic models (dynamic Smagorinsky and dynamic mixed) without
  averaging and clipping "significantly overestimate both backscatter and
  forward scatter", and "the excessive backscatter causes LES to diverge
  within tens of time steps" (§3.3, Fig. 20a). For the mixed network the
  authors write that it "predicts backscatter accurately" and that
  "consequently" the LES is stable (§3.1). See
  [neural-network SGS models](/methods/neural-network-sgs-model.md).
- **Backscatter of kinetic energy and of temperature variance, without
  clipping, in compressible wall-bounded LES.** [Xu et al. (2023)](/sources/xu-2023.md)
  (§3.2, §4.1) measure two fluxes, $\Pi=-\tau_{ij}\partial_j\tilde u_i$
  (equal to $-\tau_{ij}\tilde S_{ij}$ for the symmetric stress, *compiler
  check, not in the sources*; their stress is per unit mass) and the
  subgrid flux of temperature variance $\Pi_Q=-Q_j\partial_j\tilde T$,
  with $Q_j=\widetilde{u_jT}-\tilde u_j\tilde T$ the subgrid heat flux
  ($Q_j$, $\Pi_Q$ page-local), both normalized in wall units. Their learned
  nonlinear algebraic model (see
  [neural-network SGS models](/methods/neural-network-sgs-model.md))
  differs from the eddy-viscosity baselines in sign structure:
  - **A priori** (filtered DNS of a channel at $Re=3000$, $M=1.5$), the
    plane-averaged fluxes of the learned model "almost collapse" on
    filtered DNS, while the [Vreman](/methods/vreman-model.md), dynamic
    Smagorinsky and [WALE](/methods/wale-model.md) models and the dynamic
    version of the same nonlinear model "significantly underestimate" them
    (§3.2, Fig. 12).
  - **A posteriori** (untrained grid), the eddy-viscosity models give only
    $\Pi>0$ and $\Pi_Q>0$, no inverse transfer, whereas the learned model
    produces both signs at $y^+=15$, as filtered DNS does, and its
    probability densities of both fluxes collapse on filtered DNS, with no
    clipping (§4.1, Figs. 18–20). In the plane averages Vreman and WALE
    underestimate both fluxes, the dynamic Smagorinsky model "strongly
    overestimates" the kinetic-energy flux and underestimates the
    temperature-variance flux, and the learned model is accurate except
    for slightly larger values in the buffer layer (Fig. 17).

  The authors (§1) set this against the multi-point network of Park &
  Choi (cited), which needs backscatter clipping. In the same paper the
  dynamic Smagorinsky model underestimates the mean flux a priori (model
  evaluated on filtered DNS, §3.2, Fig. 12) and "strongly overestimates"
  it a posteriori (model run in the LES on an untrained grid, §4.1,
  Fig. 17).
- **Backscatter bounded by design.** In the reinforcement-learning closure
  of [Kurz et al. (2023)](/sources/kurz-2023.md) (§3.4) the learned
  Smagorinsky coefficient is restricted to $C_s\in[0,0.5]$ (negative values
  excluded, §3.4), so its eddy viscosity is non-negative and it cannot
  backscatter *(compiler check, not in the sources)*; their dynamic-Smagorinsky baseline in a DG code is
  clipped to $-100\mu\le\mu_t\le1000\mu$, which admits bounded backscatter
  (App. A).

- **Backscatter in a learned model of a separated flow.**
  [Kim et al. (2024)](/sources/kim-2024.md) (§4.1, Fig. 6) measure the
  backward subgrid dissipation $\langle\Pi^-\rangle=\tfrac12\langle\Pi-\lvert\Pi\rvert\rangle$
  ($\Pi^-$ page-local; average over span and time) a priori in the
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) at
  $Re_D=3900$. Their pointwise
  [neural-network models](/methods/neural-network-sgs-model.md), all six
  variants, predict mean backscatter better than the dynamic Smagorinsky
  model, whose backscatter is zero. The variants that concatenate grid- and
  test-filtered inputs in one network produce wrong-signed subgrid shear
  stress and dissipation in the near shear layers, and degrade a
  posteriori (recirculation lengths 0.79 and 1.28 against 1.56 in DNS,
  Table 3, §4.2.1). On two very coarse grids the networks run only with
  the stress set to zero wherever backscatter occurs (App. C; see
  [gradient model](/methods/gradient-model.md) for clipping).
- **Too much backscatter in a structural model.** In forced isotropic
  turbulence [Wang et al. (2023c)](/sources/wang-2023-c.md) (§III, Fig. 8)
  compare a posteriori PDFs of $\Pi$: the dynamic Smagorinsky model is
  strictly positive, the dynamic mixed model gives some backscatter through
  its similarity part, and the pure [gradient model](/methods/gradient-model.md)
  gives a PDF wider than filtered DNS, over-estimating backscatter, which
  the authors attribute mostly to its poor prediction of the filtered
  strain; it diverges at $Re_\lambda=259$ with filter width $16$ DNS grid
  spacings (App. B). Their mixed model, the
  gradient term plus an ensemble-Kalman-calibrated Smagorinsky term, gives
  the PDF closest to filtered DNS.
- **Backscatter from a symbolic-regression tensor model.**
  [Li et al. (2021)](/sources/li-2021.md) (§III C, Eq. 21, Fig. 6) compare a
  posteriori PDFs of $\Pi$ in LES of forced isotropic turbulence ($128^3$,
  filter width 16 DNS spacings, $Re_\lambda\approx260$) against filtered
  DNS. The dynamic Smagorinsky model gives a strictly positive flux, no
  backscatter; it and the dynamic mixed model "differ significantly" from
  filtered DNS. Their gene-expression-programming model, four
  integrity-basis tensors with constant coefficients (see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)),
  and the neural-network model of Xie et al. (2020) used as comparator
  "predict both forward transfer and backscatter satisfactorily". The
  coefficient of the learned model's linear (eddy-viscosity) basis tensor
  is $-0.01$, against $-0.1$, $0.07$ and $-0.11$ for the other three
  (Eq. 22); the authors connect its accuracy to the rotation-containing
  terms and to the model being less dissipative (§III D). The test is at
  nearly the Reynolds number and the filter width of the comparison of
  Wang et al. (2023c) above ($Re_\lambda$ 260 against 259, 16 DNS
  spacings), and both find the dynamic Smagorinsky flux strictly positive
  *(compiler check, not in the sources)*.
- **Backscatter in an eddy viscosity, stable.** The
  [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
  of Domaradzki (2024, §3.1) has regions of negative eddy viscosity, local
  backscatter, yet none of its isotropic-turbulence runs at $32^3$ and
  $64^3$ showed "any hints of instability". The total forward transfer
  exceeded backscatter by at least an order of magnitude, which the author
  suspects explains the stability. Its viscosity is the flux of a
  similarity stress filtered once more, a smoothing the author introduces
  because the pointwise version "will cause numerical instabilities"
  (§2.4). Domaradzki sets this against the common view that backscatter in
  an eddy-viscosity model leads to instability (§3.1), the view that
  Vela-Martín (2022, §2.2) states above for the local dynamic coefficient,
  with the qualifier "generally". Domaradzki states the same instability
  for the pointwise (unfiltered) viscosity (§2.4) and reports stability
  only for the filtered one.
- **Backscatter by energy exchange with subgrid variables, stable by
  construction.** [van Gastelen et al. (2024)](/sources/vangastelen-2024.md)
  build a learned closure for 1D Burgers and Korteweg–de Vries equations
  on a discrete box filter (cell average) with piecewise-constant
  reconstruction, for which the discrete energy splits exactly into a
  resolved and a subgrid part, $E=\bar E+E'$ (page-local; §2.5, Eq. 28,
  App. A). In the inviscid limit only the sum is conserved, so the resolved
  energy can rise, backscatter, while the total falls (Eq. 29). Their model
  adds one subgrid variable per coarse cell, a linear compression of the
  subgrid content whose square approximates $E'$ (§3.2), and closes the
  extended state with a skew-symmetric learned operator, which exchanges
  energy between resolved and subgrid variables without creating it, plus
  a negative semi-definite dissipative one. The model energy then obeys
  $dE_s/dt=(\text{coarse-scheme term})-(\text{non-negative dissipation})$
  (Eq. 37; $E_s$ page-local), so stability holds for any network weights
  when the coarse discretization conserves energy, while backscatter
  remains possible (§3.1). On Burgers the resolved energy of the model
  oscillates through backscatter while its total energy decreases, as in
  filtered DNS (§4.5, Fig. 10). The authors contrast this with
  eddy-viscosity models and clipping, which remove backscatter for
  stability (§1). See [discretization-consistent closure](/definitions/discretization-consistent-closure.md).
- **Backscatter as the mechanism of a coarse wall-bounded LES.**
  [Maejima & Kawai (2025)](/sources/maejima-2025.md) credit their
  [super-resolution SGS model](/methods/super-resolution-sgs-model.md)'s
  success on a very coarse channel grid to backscatter. The test is a
  posteriori LES at $Re_\tau\approx1000$ with
  $(\Delta x^+,\Delta z^+)\approx(72,36)$ and a non-dissipative
  kinetic-energy- and entropy-preserving central scheme.
  - **Budget evidence (§6.2.1, Fig. 25).** In the budget of the resolved
    Reynolds stresses, the subgrid term of the spanwise component is
    productive (backscatter) for $y^+\lesssim100$ with their model, and
    dissipative with the conventional selective mixed-scale model. The
    wall-normal subgrid term is negligible for both.
  - **Spectral evidence (§6.2.2, Fig. 27).** The pressure–strain term then
    moves energy from the spanwise to the wall-normal component at resolved
    wavelengths $130\lesssim\lambda_z^+\lesssim210$, peaking near
    $\lambda_z^+\approx160$. In DNS this redistribution occurs at
    $\lambda_z^+\lesssim60$, which the grid cannot resolve.
  - **Proposed mechanism (§6.2.3, §8).** Spanwise backscatter raises
    $\langle w'w'\rangle$ near the wall. Redistribution raises
    $\langle v'v'\rangle$ and the near-wall Reynolds shear stress, and the
    mean velocity then follows DNS. The mass flow rate is overpredicted by
    10%, against 23% with the conventional model (§6.1).
  - **Agreement with Inagaki & Kobayashi.** The authors call this
    consistent with the productive spanwise subgrid term of
    [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) above. It also
    agrees, by the authors' account, with the redistribution produced by
    Abe's stabilized mixed model in coarse LES (Inagaki & Kobayashi 2020,
    cited by Maejima & Kawai, §6.2.3).
  - **Bounded, not removed (App. C).** The model admits backscatter down to
    an effective viscosity of about −2 times the mean wall viscosity.
    Allowing more backscatter improves the mean velocity, and −3 is
    unstable. The floor construction is on the
    [gradient-model](/methods/gradient-model.md) page.
- **Backscatter as a selection criterion for a discovered closure, in two
  dimensions.** [Jakhar et al. (2026)](/sources/jakhar-2026.md) discover
  closures for LES of forced two-dimensional (geophysical) turbulence by
  sparse Bayesian regression and select them with a criterion that
  requires the correlation with filtered DNS of the total inter-scale
  energy transfer and of its parts of either sign, "diffusion" and
  "backscattering", not only of the stress (p. 3, Fig. 1b). Their transfer
  has the sign convention of $\Pi$ (positive = diffusion, negative =
  backscatter); its definition is in the Supplemental Material, which is
  not in the version read. The second-order
  [gradient model](/methods/gradient-model.md) has zero inter-scale energy
  transfer in two dimensions, "neither diffusion nor backscattering", and
  is unstable a posteriori in every case (p. 3, p. 4). For a traceless
  two-dimensional velocity gradient $A_{ij}=\partial_j\bar u_i$
  (page-local) the Cayley–Hamilton identity gives
  $A^2=-\det(A)\,I$, so both terms of
  $\Pi\propto-A_{ik}A_{jk}(A_{ij}+A_{ji})$ are traces of $A^{\mathsf T}A^2$
  or $A(A^{\mathsf T})^2$, which vanish: the transfer is zero pointwise
  *(compiler check, not in the sources)*. The closures selected with the
  new criterion add the next Taylor-series terms (fourth and sixth order in
  $\Delta$) and "capture the energy backscatter that is seen in the FDNS".
  A priori, the domain-averaged energy transfer, as a ratio to filtered
  DNS, is $0.62\pm0.04$ and $0.78\pm0.04$ for the fourth- and sixth-order
  models, $0$ for the gradient model, and $-62.24\pm37.80$, $-28.48\pm15.38$
  and $-6.91\pm2.73$ for Smagorinsky, dynamic Smagorinsky and dynamic Leith,
  which are "purely and excessively diffusive" (Fig. 2, mean over four
  setups). The fourth-order model runs stably a posteriori without
  clipping when the LES resolves more than 80% of the DNS enstrophy (p. 4).
  A negative ratio for purely diffusive models means that the
  domain-averaged transfer of the filtered DNS has the backscatter sign in
  these flows *(compiler check, not in the sources)*: a net inverse
  transfer, the two-dimensional case that Vela-Martín (2022, §8) places
  outside the scope of its conclusions (see Interpretation and scope).

The two claims of Seyedi & Zayernouri and Kim et al. concern different
flows (isotropic turbulence against a channel) and different measures (a priori stress correlation and a
posteriori decay against two trained mean statistics). Kim et al. also find that the mean subgrid
dissipation $\langle\Pi\rangle$ is not determined by the two target
statistics: equally trained models give different values (§III C).

[Helm & Martín (2022)](/sources/helm-2022.md) (§IV F, §V) describe the
scale-similar part of their dynamic mixed model as a "conservative energy
exchange" between the smallest resolved scales and the subgrid scales,
beside the "dissipative drain" of the eddy viscosity (see
[scale-similarity models](/methods/scale-similarity-model.md)); the paper
does not use the word backscatter.

[Fang et al. (2026)](/sources/fang-2026.md) (§4.2.4), a review that runs no
test, list "explicit modeling of backscatter dynamics", together with
transfer learning, among the remedies that Guan et al. (their ref. [55])
applied to convolutional SGS closures that are accurate a priori but show
"instability and energy divergence during a posteriori rollout" (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
The review gives no form of that backscatter model.

[Hu & Yang (2026)](/sources/hu-2026.md) (§II C–E, §IV A), another review
that runs no test, tie backscatter to the absence of scale separation:
with no spectral gap the subgrid term "exchanges energy with the resolved
field in both directions—forward (dissipation) and, intermittently,
backward (backscatter)" (see [spectral gap](/definitions/spectral-gap.md)).
They state that the constant-coefficient
[Smagorinsky model](/methods/smagorinsky-model.md) is purely dissipative,
$\nu_t\ge0$, and cannot represent backscatter. The
[dynamic model](/methods/dynamic-procedure.md) can in principle, through a
locally negative $\nu_t$, but the averaging or clipping used for
stability suppresses some or all of it, the practice Vela-Martín (2022,
§2.2) describes above. A learned closure "obtained by minimizing a
pointwise regression loss" on filtered DNS "tends to average out the
backscatter", and mis-modelled backscatter, a closure that locally
injects energy, is the first of three a posteriori failure modes they
list for learned SGS models (§IV A; see
[neural-network SGS models](/methods/neural-network-sgs-model.md)). The
same review cites the convolutional model of Guan et al. for
two-dimensional turbulence, which stays stable a posteriori while
reproducing "both forward scatter and backscatter", the work Fang et al.
(2026) cite above.

Kim et al. (2022) and Maejima & Kawai (2025) both work in channel flow
and reach different emphases. Kim et al. find backscatter unnecessary for
the mean velocity at $Re_\tau=180$ on
$(\Delta x^+,\Delta z^+)=(70.7,35.3)$. Maejima & Kawai find that admitting
more backscatter brings the mean velocity closer to DNS at
$Re_\tau\approx1000$ on $(72,36)$. Their own run with no projected
backscatter (floor zero) still beats the conventional model (App. C). The
models, Reynolds numbers and training targets differ between the two
papers.

## Compressible flows: the spherical part of the flux

In compressible LES the Favre subgrid stress has a trace,
$\tau_{kk}=2\bar\rho k_{\mathrm{sgs}}$, and the local flux
$\Pi=-\tau_{ij}\tilde S_{ij}$ splits into a deviatoric and a spherical part,

$$\Pi=\Pi^{d}+\Pi_{\mathrm{sph}},\qquad \Pi^{d}=-\tau^d_{ij}\tilde S^d_{ij},\qquad \Pi_{\mathrm{sph}}=-\tfrac23\,\bar\rho k_{\mathrm{sgs}}\,\nabla\cdot\tilde{\boldsymbol u},$$

with $\Pi^{d}$ page-local and $\Pi_{\mathrm{sph}}$ the spherical part of registry §11 (as on the [pressure-dilatation](/definitions/pressure-dilatation.md) page). [Tonicello et al. (2022)](/sources/tonicello-2022.md)
(§5, Eqs. 5.1–5.3) introduce this split as an a priori diagnostic. Their
stress carries the opposite sign to the registry, their budget term $K_3$
equals $-\Pi$, their spherical transfer $\Lambda$ equals $\Pi_{\mathrm{sph}}$, and their
"deviatoric contribution" $K_3+\Lambda$ equals $-\Pi^{d}$
*(compiler check, not in the sources)*. With a deviatoric eddy viscosity,
$\Pi^{d}=\bar\rho\nu_t\lvert\tilde S^d\rvert^2$, which defines an equivalent
eddy viscosity from filtered DNS (Eq. 5.3). Because
$k_{\mathrm{sgs}}>0$ for non-spectral filters (citing Vreman et al. 1994),
$\Pi_{\mathrm{sph}}$ is forward in compression and backscatter in expansion.

The authors evaluate the terms in their DNS of a Mach 2.91 boundary layer
over a $24^\circ$ compression ramp followed by an expansion corner (see
[shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)),
with both Favre time–span averaging (the RANS sense) and Germano's
differential filter at $\Delta=2h$, $4h$, $8h$ (the LES sense, $h$ the DNS
spacing):

- **Mean backscatter.** Even in the Favre mean, a large region near the
  expansion corner shows $\Pi<0$, energy returned from the fluctuations to
  the mean flow (§4.1, Fig. 14). The authors take this as confirming "also
  on average" the link of compression with forward transfer and of
  expansion with backscatter that they cite from O'Brien et al. (2014) and
  Wang et al. (2018a, 2020).
- **Filtered fields.** Probability densities of $\Pi$ are much wider than
  for the averaged fields but with a similar mean, consistent with
  eddy-viscosity models reproducing the mean transfer but not the local one
  (§4.2, Fig. 19). Compression enhances forward transfer and expansion
  backscatter, more so for wider filters (Figs. 23–24). The correlation of
  $\Pi$ with the resolved [pressure dilatation](/definitions/pressure-dilatation.md)
  $\bar p\,\nabla\cdot\tilde{\boldsymbol u}$ is 0.2775 for the averaged
  field and 0.1936 and 0.2682 for $\Delta=4h$ and $8h$ (Table 4); the
  authors conclude that the weight of compressibility in modelling is set
  "not entirely by the physics of the problem" but strongly by the filter
  width (§4.2). The subgrid Mach number, $M_{\mathrm{sgs}}=\sqrt{2\bar\rho k_{\mathrm{sgs}}/(3\gamma\bar p)}$
  (registry §11, Eq. 4.14), reaches about 0.32 in the mean and about 0.42 for
  the filtered fields, above the value 0.3 at which they expect
  compressibility effects (Figs. 20–22).
- **The deviatoric part does not backscatter on average.** The averaged
  $\Pi^{d}$ is positive in the whole domain: the mean backscatter near the
  expansion corner comes entirely from $\Pi_{\mathrm{sph}}$, so a positive eddy
  viscosity is "fairly accurate" on average for the deviatoric stress
  (§5, Figs. 27–28). In filtered fields a large share of the equivalent eddy
  viscosity is negative. Removing $\Pi_{\mathrm{sph}}$ also removes most of the
  correlation with the pressure dilatation: 0.1081 (averaged), 0.0370
  ($4h$) and 0.0889 ($8h$) (Table 6, Fig. 29).

They conclude that an eddy viscosity suits the deviatoric part, that the
trace needs a different model, and propose by analogy, without testing it,
a [bulk-viscosity](/definitions/bulk-viscosity.md)-type subgrid model for
the trace, $\tfrac23\bar\rho k_{\mathrm{sgs}}\sim-\mu_b\nabla\cdot\tilde{\boldsymbol u}$
with $\mu_b$ a subgrid bulk viscosity (registry §11; the source's $\beta$)
(§5, Eq. 5.5; §6).

[Qi et al. (2022)](/sources/qi-2022-b.md) (§3.2, Eqs. 3.13–3.21) build a
compressible one-equation model, the quasi-dynamic $k_{\mathrm{sgs}}$
model, on the same split: the isotropic stress is set to
$2\bar\rho k_{\mathrm{sgs}}$ from the transported $k_{\mathrm{sgs}}$, and the
Smagorinsky coefficient is fixed by equating the anisotropic part of the
model flux to that of a gradient-model estimate of $\Pi$ (see the
[dynamic procedure](/methods/dynamic-procedure.md) and
[gradient model](/methods/gradient-model.md) pages). Inserting their
Eq. (3.21) into their eddy viscosity cancels $\Delta$ and $\lvert\tilde S\rvert$
and gives $\nu_t=\Pi^{d}_{\mathrm{est}}/\big(2\bar\rho\tilde S^d_{ij}\tilde S_{ij}\big)$,
with $\Pi^{d}_{\mathrm{est}}$ (page-local) the anisotropic part of the
estimated flux, so the model viscosity is negative wherever that estimate
backscatters *(compiler check, not in the sources)*; the paper states no
clipping. A posteriori, on a supersonic flat-plate boundary layer at
$y^+=15$, the model's flux field resembles the DNS flux "in distribution,
intensity, structure and even the energy backscatters" (§4.2, Fig. 19).

**Backscatter grows with the turbulent Mach number.** In decaying
compressible isotropic turbulence two papers of one group find a longer
negative (backscatter) tail of the probability density of the subgrid flux
as $M_t$ rises from 0.4 to 0.8, in filtered DNS with a Gaussian filter of
width 16 DNS spacings:
[Zhang et al. (2022b)](/sources/zhang-2022-f.md) (§IV B, Fig. 9), with a
density-unweighted filter and the full (not deviatoric) density-weighted
stress in $\Pi$, conclude that "compressibility enhances the energy
transfer from small to large scales"; [Zhang et al. (2022d)](/sources/zhang-2022-h.md)
(§IV B, Fig. 8), for a dense gas with Favre filtering, read it as more
local inverse transfer under strong compressibility. In both, iterative
approximate deconvolution reproduces the filtered-DNS densities including
the tail, while dynamic Smagorinsky gives densities that are too narrow
(see [scale-similarity models](/methods/scale-similarity-model.md)); the
dynamic coefficients there are domain averages (Zhang et al. 2022b, App.;
2022d, Eqs. 33–36).

## Backscatter-like transfers outside the subgrid flux (inline)

- **A numerical closure term.** In residual-based
  [variational multiscale](/methods/variational-multiscale-method.md) LES,
  [Chen et al. (2022)](/sources/chen-2022-g.md) (§5, Figs. 4–5) find that
  one cross-stress term of the resolved-energy budget has a positive average
  over most of a channel at $Re_\tau=180$: it "increases energy" of the
  resolved field, contrary to "the intention of the turbulent model", and
  they reverse its sign in a modified formulation. The authors do not call
  it backscatter.
- **Spectral transfer in a DNS.** [Yu et al. (2022)](/sources/yu-2022-e.md)
  (§6.4, Fig. 13) derive a scale-by-scale budget in spanwise wavenumber for
  an impinging-shock boundary-layer interaction at Mach 2.28. The
  inter-scale transfer is forward overall; upstream of the interaction a
  small inverse transfer from $\lambda_z^+\approx100$ to
  $\lambda_z/\delta_0\gtrsim1$ exists, as in the channel flows of Lee &
  Moser (2015) and Cho et al. (2018) that the authors cite, but contributes
  little to the genesis of
  the large scales beside production. This is a transfer between resolved
  scales of a DNS, not a subgrid flux; the authors leave its use for
  subgrid modelling to future work (§8).
- **"Bottom-up" transfer as a motivation for stochastic subgrid
  closures.** [Chen et al. (2024b)](/sources/chen-2024-c.md) (§4.1), a
  review of [one-dimensional turbulence](/methods/one-dimensional-turbulence.md)
  (ODT), call conventional subgrid closures "parameterization" (after
  Kerstein, cited) and "top-down": they rely on subgrid isotropy, which
  fails near walls, and cannot capture "bottom-up" transport of energy and
  species from small to large scales. ODT, which generates small-scale
  structure autonomously on embedded one-dimensional lines and feeds it
  back to the LES, is offered as a remedy: such models give a
  bidirectional rather than a top-down transfer (§4.1). The review defines
  and measures no local flux $\Pi$. Of LES-ODT it writes in §2.4.1 that the
  "top-down" strategy is "abandoned" and in §3.3 that LES-ODT is a
  "top-down" strategy.

## Interpretation and scope

Vela-Martín (2022, §7.2, §8) concludes that, in isotropic turbulence away
from walls, backscatter is conservative spatial redistribution rather than
a local inverse cascade, and need not be modelled to reproduce the local
resolved/subgrid energy exchange. The author supports this with a
statistical-mechanics argument, presented as an argument rather than a
proof: global inverse cascades are possible but highly improbable. The
conclusions are limited to isotropic turbulence; global
inverse cascades with $\langle\Pi\rangle<0$, and flows with additional
sign-definite invariants (2D, homochiral, MHD), are outside it; and
eliminating backscatter may be unnecessary or undesirable for models with
numerically stable backscatter such as
[similarity models](/methods/scale-similarity-model.md) (§8).

Other sources treat backscatter as a physical effect to be represented:

- [Li & Liu (2022)](/sources/li-2022.md) (§2.3) justify the helicity
  correction of the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
  for compressor corner separation by the statement that velocity helicity
  "is correlated with the turbulent energy backscatter", citing earlier
  work (their ref. [22]). They attribute the lower eddy viscosity of the
  corrected model to strong backscatter in strongly rotating turbulence
  (§3.2). Vela-Martín (2022, §8) limits the conclusions to isotropic turbulence
  and names shear- or rotation-dominated flows as a further application of
  the method.
- The [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  of [Agrawal et al. (2022)](/sources/agrawal-2022.md) dissipates only
  through its Smagorinsky-type coefficient; its antisymmetric part changes
  the stress without exchanging energy (§III.A). The dynamic Smagorinsky
  model needs clipping near the wall in their WMLES channel, where the
  tensor model does not (§VII.D).
- In the spectral view of [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
  (§2.2), the shell-averaged transfer across the cutoff defines the
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md). This
  measures the net transfer at each wavenumber and cannot show the spatial
  sign of $\Pi$ *(compiler check, not in the sources)*.
- In the same spectral view, [Rajek & Pozorski (2026)](/sources/rajek-2026.md)
  (§II D, §III B, Fig. 5) compute the "theoretical" spectral eddy
  viscosity $\nu_t(k\mid k_c)$ a priori, from the transfer across a sharp
  cutoff in DNS of forced isotropic turbulence, by the method of
  Domaradzki et al. (1987), as cited. At $Re_\lambda\approx100$ and
  $k_c=30$ it is negative for $k<0.4k_c$, "with absolute values close to
  the molecular viscosity", in agreement with Domaradzki et al. The
  authors read such negative values as "possibly imitating the backward
  energy transfer" and call them "clearly in contradiction with the
  general eddy-viscosity concept". They cite Lesieur's EDQNM result that
  the spectral eddy viscosity becomes negative if the spectrum beyond the
  cutoff falls as $k^{-m}$ with $m>5$. Used as the closure of an LES, this
  theoretical viscosity recovers the DNS spectrum at $Re_\lambda\approx100$.
  It needs DNS data, so it has no predictive value beyond DNS-attainable
  Reynolds numbers (§III B). Their adaptive model keeps the viscosity
  non-negative by construction: the control operator of the regulator
  never lets it fall below zero (Eq. 26; see
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)). By
  their Eq. (16), which defines it from the shell-averaged transfer, a
  negative $\nu_t(k\mid k_c)$ is a net inverse transfer at wavenumber $k$,
  not a spatial sign of $\Pi$ *(compiler check, not in the sources)*.
- Jakhar et al. (2026, p. 1) call backscatter "an important process in
  atmospheric and oceanic flows", which eddy-viscosity closures "miss".
  They note that their higher-order gradient closures violate the
  [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md), "the need
  to go beyond classical turbulence tensors to represent backscatter"
  (p. 5), and propose them for weather and climate models, which run as
  [implicit LES](/definitions/implicit-les.md), where "an explicit
  representation of backscatter is desired" (p. 6).

[Caban et al. (2026)](/sources/caban-2026.md) (§2) recall that
[approximate deconvolution and other scale-similarity models](/methods/scale-similarity-model.md)
have no explicit dissipative character and, depending on the local flow,
"may cause energy transfer from small to large scales (backscatter)", a
phenomenon that "occurs in real flows and may lead to solution instability
in practical LES applications", with the nonlinear (Clark) model as their
cited example. In their own LES of the Taylor–Green vortex at $Re=1600$ on
$64^3$ the Layton–Lewandowski model ($N_{\mathrm{AD}}=0$, with
$N_{\mathrm{AD}}$ the number of deconvolution terms, registry §11) is stable with
every explicit filter tested and non-dissipative interpolation, while the
deconvolution model with $N_{\mathrm{AD}}=5$ needs added numerical
dissipation; they attribute its instability to the amplification of
subfilter energy and of the aliasing of the deconvolved product, not to
backscatter (§5.4.1–5.4.2). Vela-Martín (2022, §8) instead names
similarity models as models with numerically stable backscatter. Both
statements are hedged ("may"; "may be unnecessary or undesirable").

## Qualifications

- **Sign of the flux in Zhang et al. (2022d).** They print the subgrid flux
  as $\tau_{ij}\tilde S_{ij}$, without the minus sign, and call positive
  values forward transfer. With their own stress (positive trace, Eq. 19)
  and their dynamic Smagorinsky closure (Eq. 33), the flux
  $\tau_{ij}\tilde S_{ij}$ of a purely dissipative model is negative, so the
  printed sign statement holds only for $-\tau_{ij}\tilde S_{ij}$, the
  registry's $\Pi$ *(compiler check, not in the sources)*. Their figures
  read the long negative tail as backscatter (§IV B, Fig. 8).
- **"About 20 times".** Cao et al. (2022b) state that the solenoidal
  dissipation is "approximately 20 times larger" than the mean filtered
  subgrid production; their Table I gives ratios of about 68, 32, 22 and 35
  at $t=2.5$, 5, 10 and 15, so 20 is the smallest of the four
  *(compiler check, not in the sources)*.
- Vela-Martín (2022) prints several slips that do not affect the results:
  Eq. (3.5) uses the unfiltered velocity and swapped indices, and its sign
  disagrees with Eqs. (2.5) and $\langle D\rangle=0$, which give
  $\langle\bar u_i\partial_j\tau^S_{ij}\rangle=-\langle T\rangle$ in the
  paper's notation *(compiler check, not in the sources)*. §6.3 writes
  $\rho(T^S_s,T^O_g)$ for the correlation of the two standard fluxes. The
  Fig. 6 and Fig. 7 captions and §6.4 give $Re_\lambda=320$ where Table 1
  gives 324. The PGD algorithm is called "PSD" once (§6.1).
- Inagaki & Kobayashi (2023, §II C) print the channel-flow form of
  $\langle\tau^{\mathrm{ani}}_{ij}\rangle\langle\bar S_{ij}\rangle$ as
  "$\langle\tau^{\rm ani}_{xy}\rangle\partial U_x/\partial y/2$"; with
  $\langle\bar S_{xy}\rangle=\langle\bar S_{yx}\rangle=\tfrac12\partial_y\langle\bar u\rangle$
  the contraction is $\langle\tau^{\mathrm{ani}}_{xy}\rangle\partial_y\langle\bar u\rangle$,
  without the factor $\tfrac12$ *(compiler check, not in the sources)*. The
  sign conclusions they draw from it are unaffected.
- At $\Delta=0.33L$, $Re_\lambda=240$ the sharp-filter starting values are
  given as $f^-\approx0.6$, $v^-\approx0.4$ (§6.1), against the general
  "$v^-\approx0.5$" and $f^-$ "close to unity" of §5.3.

# Citations

- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.1–2.2, Eqs. (2.4)–(2.8); §3, Eqs. (3.1)–(3.5); §4; §5.3, Eqs. (5.7)–(5.8), Fig. 2; §6.1–6.4, Figs. 3–7; §7.1, Eqs. (7.2)–(7.5); §7.2; §8; Apps. A–B.
- [Li & Liu (2022)](/sources/li-2022.md) — §2.3, Eqs. (19)–(22); §3.2.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §III.A; §VII.D.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.2, Eqs. (16)–(22).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II, Eqs. (4)–(15); §III.A.2, Figs. 2–3.
- [Abe (2021)](/sources/abe-2021.md) — §IV C, Eq. (17).
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §I; §II.2; §III.2, p. 15, Fig. 5.
- [Kim et al. (2022)](/sources/kim-2022.md) — §III C; §III E, Fig. 14.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §IV F; §V.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §II A, Eqs. (3)–(5); §II C, Eqs. (8)–(10); §III, Figs. 3–8; §IV A 2, Fig. 12; §IV B.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.1, Figs. 4, 6, 8; §3.3, Fig. 20a.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §3.4; App. A.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §2.4; §3.1.
- [Kim et al. (2024)](/sources/kim-2024.md) — §4.1, Fig. 6; §4.2.1; App. C.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §III, Eq. (21), Fig. 8; App. B.
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — §1; §2.5, Eqs. (28)–(29); §3.1–3.2, Eqs. (33)–(39); §4.5, Fig. 10; App. A.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §3.2, Eq. (3.2); §6.1; §6.2.1–6.2.3, Figs. 25–27; §8; App. C, Fig. 37.
- [Wu & Lele (2026)](/sources/wu-2026.md) — §3.1, Eq. (3.9); §3.2.2, Fig. 4.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — pp. 1–6, Eq. (4), Figs. 1–2.
- [Caban et al. (2026)](/sources/caban-2026.md) — §2; §5.4.1–5.4.2.
- [Li et al. (2021)](/sources/li-2021.md) — §III C, Eqs. (21)–(22), Fig. 6; §III D.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §III.A, Eq. (16); §III.D, Eqs. (21)–(23).
- [Heinz (2020)](/sources/heinz-2020.md) — §2.1.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §4.1, Eqs. (4.4)–(4.10), Fig. 14; §4.2, Eq. (4.14), Table 4, Figs. 19–24; §5, Eqs. (5.1)–(5.5), Tables 5–6, Figs. 27–29; §6.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §3.2, Eqs. (3.13)–(3.21); §4.2, Fig. 19.
- [Chen et al. (2022)](/sources/chen-2022-g.md) — §5, Figs. 4–5; §6, Eq. (38).
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §6.4, Fig. 13; §8.
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §IV B, Eqs. (17)–(18), Figs. 5–6, Table I.
- [Li et al. (2022)](/sources/li-2022-k.md) — §II C, Eq. (15).
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §IV.
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §IV B, Fig. 9.
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — Eqs. (19), (33); §IV B, Fig. 8.
- [Xu et al. (2023)](/sources/xu-2023.md) — §1; §3.2, Fig. 12; §4.1, Figs. 17–20.
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §2.4.1; §3.3; §4.1.
- [Fang et al. (2026)](/sources/fang-2026.md) — §4.2.4 (backscatter modelling named among stabilizations of CNN closures, Guan et al. cited). Review, citation only.
- [Hu & Yang (2026)](/sources/hu-2026.md) — review: §II C–E (two-way exchange without a spectral gap; Smagorinsky and dynamic model); §IV A (pointwise training averages out backscatter; failure modes; Guan et al. as cited). Review, citation only.
- [Rajek & Pozorski (2026)](/sources/rajek-2026.md) — §II D, Eq. (16); §III B, Fig. 5 (negative a priori spectral eddy viscosity at low $k$; Lesieur as cited); §IV, Eq. (26) (non-negative adaptive viscosity).
- [Germano et al. (1991)](/sources/germano-1991.md) — §I; §II, Eqs. (15)–(17); §III (negative plane-averaged eddy viscosity in transition, no clipping).
