---
type: Definition
title: "Ducros shock sensor"
description: "The Ducros sensor flags compressions by the share of dilatation in the velocity-gradient magnitude; the page gives its origin as a factor of Jameson's pressure sensor in second-order JST dissipation for LES, the classical squared ratio and the modified compression-only form, their use as switches of hybrid central/TENO and central/WENO schemes, as weights towards a first-order flux and as a factor of an adaptive Lax–Friedrichs coefficient, their regularization, thresholds, failures and further multiplications."
status: established
aliases: [Ducros sensor, modified Ducros sensor, improved Ducros sensor, Ducros dilatation–vorticity sensor, Ducros level, dilatation-to-vorticity ratio, modified Jameson sensor, Jameson–Ducros sensor]
tags: [central-scheme, teno, weno, finite-difference, turbulence]
timestamp: 2026-11-17T08:43:53Z
---

# Ducros shock sensor

The **Ducros sensor** is a pointwise physical shock detector built from the
velocity field alone. It compares the dilatation $\nabla\cdot v$ with the
vorticity $\nabla\times v$: at a shock the dilatation dominates and the
sensor is close to one, in vortical turbulence the vorticity dominates and the
sensor is close to zero. It does not look at the reconstructed data, unlike
the smoothness-based and TENO-flag indicators on
[troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md).
It was introduced by [Ducros et al. (1999)](/sources/ducros-1999.md) for
large-eddy simulation of shock/turbulence interaction, not as a stand-alone
detector but as a factor of Jameson's pressure sensor in the second-order
artificial dissipation of a central finite-volume scheme (see Origin below).
In the later sources of this bundle it serves two purposes. It switches a low-order dissipation
term in a central scheme with artificial dissipation
([Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)), as in the
original construction. It also selects
where a [hybrid scheme](/methods/hybrid-weno.md) leaves its central
energy-preserving flux for WENO-Z or [TENO](/methods/targeted-eno.md)
([De Vanna et al. (2023a)](/sources/devanna-2023.md);
[De Vanna et al. (2023b)](/sources/devanna-2023-b.md);
[De Vanna et al. (2023c)](/sources/devanna-2023-c.md)). In a hypersonic
Cartesian solver it weights a blend of fifth-order WENO-Z with a
first-order flux ([McQuaid & Brehm (2024)](/sources/mcquaid-2024.md)).

## Origin: a factor of Jameson's pressure sensor

[Ducros et al. (1999)](/sources/ducros-1999.md) (§3, Eqs. (8)–(13),
(22)–(24)) run a second-order, collocated finite-volume central scheme
(the flux of the mean state, which on the model law is the second-order
skew-symmetric form) with the scalar Jameson–Schmidt–Turkel (JST) dissipation
and an explicit subgrid model ([artificial viscosity](/methods/artificial-viscosity.md)).
The second-order JST coefficient is driven by Jameson's pressure sensor
$\varphi_{\mathrm J,i}=\lvert(p_{i+1}-2p_i+p_{i-1})/(p_{i+1}+2p_i+p_{i-1})\rvert$
(page-local symbols as on the artificial-viscosity page: constants $k_2$,
$k_4$, coefficients $\varepsilon_{2,i+1/2}$, $\varepsilon_{4,i+1/2}$, spectral
radius $a_{i+1/2}$ factored out of the dissipation term). To keep that
dissipation away from vortical turbulence they multiply the Jameson sensor by
the "local function"

$$\Phi_{\mathrm D}=\frac{(\nabla\cdot v)^2}{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}},\qquad\epsilon_{\mathrm D}=10^{-30},$$

with $\epsilon_{\mathrm D}$ only "to prevent numerical divergence in regions
where both $\nabla\cdot\mathbf u$ and $\omega$ are zero"; $\Phi_{\mathrm D}$
"varies between 0 for weakly compressible regions to about 1 in shock
regions". The dissipation of this "modified Jameson's approach" is

$$\mathcal D_{i+1/2}=a_{i+1/2}\,\varepsilon_{2,i+1/2}\,(u_{i+1}-u_i),\qquad
\varepsilon_{2,i+1/2}=k_2\max\big(\varphi_{\mathrm J,i}\Phi_{\mathrm D,i},\ \varphi_{\mathrm J,i+1}\Phi_{\mathrm D,i+1}\big),$$

with $k_2=1.5$ and $k_4=0$ in every run with the product, subtracted from the central flux
(Eqs. (23)–(24); the paper writes the spectral radius inside the coefficient,
$\epsilon^{(2)}=k^{(2)}\mathcal R\Psi\Phi$). The face value is the maximum
of the two **cell products**, not the product of two face maxima, and
$\Phi_{\mathrm D,i}$ is "simply a local evaluation" of the ratio; the
discretization of $\nabla\cdot v$ and $\nabla\times v$ is not printed. The
authors call the combination a "modified Jameson's sensor" ($\Phi\Psi$ in
their tables); the name "Ducros sensor" is later usage
([Pirozzoli (2011a)](/sources/pirozzoli-2011.md), §3.2: "frequently referred
to as the Ducros sensor").

**Motivation: Galilean invariance.** Earlier ways of shrinking the region
where second-order dissipation acts, an entropy-like quantity, a monotone
function of the local Mach number multiplying the scaling factor (Swanson &
Turkel) or a shock-region flag set before each Runge–Kutta step (Crumpton &
Shaw), are recalled; corrections based on the local Mach number add "a new
source on non-Galilean invariance". The velocity-gradient factor "conserves
the Galilean invariant property of the sensor" and is a smooth correction
"proportional to the level of local compressibility". The JST dissipation
itself is "no longer Galilean invariant due to the artificial viscosity", so
the coefficients hold in the shock frame, in which every run with a shock is
made (§3, pp. 524–525; §4.2, p. 532). *(Compiler check, not in the source: through the spectral radius $\lvert v\rvert+c$, which is not Galilean invariant.)* The conclusion calls the sensor "frame independent, easy to
implement in a parallel code, and relatively costless" (§6); no cost figure
is given.

## Evidence in the originating paper

[Ducros et al. (1999)](/sources/ducros-1999.md) (§4) test only the product
$\Phi_{\mathrm D}\varphi_{\mathrm J}$, with $k_2=1.5$, against the plain
Jameson sensor:

- **Decaying compressible turbulence** ($32^3$, inviscid,
  $M_t\approx0.13$, and a Comte-Bellot–Corrsin field at $M_t=0.26$;
  [compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)).
  With the product the LES without artificial dissipation is recovered (THI-4
  against THI-1, CBC-2 against CBC-1); with the plain Jameson sensor the
  second-order term perturbs the subgrid model (THI-3), and adding
  $k_4=0.02$ cuts the energy near the cut-off "by more than a decade" (THI-2);
  classical JST also departs from the reference in CBC-3 (§4.1, Figs. 1–3, 7–8). The product stays small "not only due to the
  low values of each component … but also due to their relatively weak
  correlation": during the decay the mean and rms of $\varphi_{\mathrm J}$
  fall while those of $\Phi_{\mathrm D}$ rise (Figs. 5–6).
- **2D shock–vortex interaction** ($M_1=1.1$–1.7;
  [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)). The
  product keeps the enstrophy on plateaus before and after the shock, where
  the classical JST dissipation with $k_4=0.02$ loses it on the coarser grids
  (§4.2, Fig. 10; Fig. 11 for $M_1=1.1$–1.7).
- **3D shock/turbulence LES** ($M_1=1.2$;
  [shock–turbulence interaction](/benchmarks/shock-turbulence-interaction.md)).
  Only the product gives a pre-shock decay of turbulent kinetic energy
  consistent with homogeneous decay; the plain Jameson sensor dissipates the
  incoming turbulence and its vorticity before the shock (§4.3.3–4.3.4,
  Figs. 16, 19–20). Off-shock the standard second-order dissipation is
  "around 10%" of the subgrid dissipation, and the product makes it
  negligible; in the shock the numerical dissipation dominates the subgrid one
  (§4.4, Fig. 24; "These conclusions hold for regions where the grid is
  refined"). Isosurfaces of $\Phi_{\mathrm D}$ alone at 0.1 select
  small turbulent scales, at 0.5 and 0.8 the shock region (Fig. 23).
- **Limit inside the shock.** The sensor does not remove the shock-capturing
  dissipation that eddies meet when they cross the shock: on the coarse grid,
  where the smallest resolved energetic eddies are about as wide as the
  captured shock (about three cells), it damps them and lowers the streamwise
  vorticity spuriously; refining the shock-normal mesh or pre-filtering is the
  remedy proposed (§5; [numerical dissipation](/definitions/numerical-dissipation.md)).

## Two forms

Page-local symbols: $\Phi_{\mathrm D}$ is the classical ratio,
$\Psi_{\mathrm D}$ the modified sensor, $\Psi^*$ its threshold and
$\epsilon_{\mathrm D}>0$ the regularization (the same letter as on
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

**Classical squared ratio.** The original form is that of Ducros et al.
(1999, Eq. (22)), with $\epsilon_{\mathrm D}=10^{-30}$ (Origin above). As one
factor of their product sensor $\Xi_i$, Sciacovelli et al. (§3, Eq. (36)) use
it with another regularization,

$$\Phi_{\mathrm D}=\frac{(\nabla\cdot v)^2}{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}},\qquad\epsilon_{\mathrm D}=10^{-16}.$$

This form is even in the dilatation, so it flags expansions as well as
compressions. It lies in $[0,1)$. [Pirozzoli (2011a)](/sources/pirozzoli-2011.md)
(§3.2, Eq. (29)) prints the same ratio, $0\le\Phi_{\mathrm D}\le1$, and recalls
it as Ducros et al.'s replacement, together with the Jameson sensor, of
Harten's switch in a nonlinear filter; Garnier et al. (2001), as recalled
there, found it better than Harten's switch at distinguishing turbulent
fluctuations from shocks, and Larsson et al. (2007) modified it.
*(Compiler check, not in the sources: three later product sensors of this
bundle extend the 1999 product $\Phi_{\mathrm D}\varphi_{\mathrm J}$.
Sciacovelli et al.'s $\Xi_i$ multiplies it by the Bhagatwala–Lele switch and
takes the face value $\max(\Xi_i,\Xi_{i+1})$, the rule of Ducros et al.'s
Eq. (24); Wang et al. (2023a)'s $\varphi_{\mathrm F}$ multiplies it by a
density factor $\varphi_{\mathrm J}[\rho]$; Duan et al. use $\Psi_{\mathrm D}$
in place of $\Phi_{\mathrm D}$, with face values again the maximum over the
two cells.)*

**Modified, compression-only form.** De Vanna et al. (2023a, §3.2, Eq. (9))
call the following a "modified Ducros shock sensor":

$$\Psi_{\mathrm D}=\max\Big(-\frac{\nabla\cdot v}{\sqrt{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}}},\ 0\Big),\qquad \epsilon_{\mathrm D}=\Big(\frac{v_\infty}{\delta_0}\Big)^2,$$

with $v_\infty$ the free-stream velocity and $\delta_0$ the inflow
boundary-layer thickness. The URANOS paper prints the same expression as the
"improved Ducros sensor" with $\epsilon_{\mathrm D}=(v_\infty/L)^2$, $L$ a
reference length (De Vanna et al. 2023b, §3.2, Eq. (10)). De Vanna et al.
(2023c, §3.2, Eq. (13)) write it in index notation, with the Levi-Civita
tensor for the vorticity and $\epsilon_{\mathrm D}=\epsilon_0^2$, where
$\epsilon_0=v_\infty/L_0$ is called a "reference velocity gradient". Two
changes separate it from the classical form. Only compressions are flagged,
since the max with zero discards $\nabla\cdot v>0$. The ratio is not squared.
*(Compiler check, not in the sources: with the same $\epsilon_{\mathrm D}$,
$\Psi_{\mathrm D}=\sqrt{\Phi_{\mathrm D}}$ wherever $\nabla\cdot v<0$, and
$\Psi_{\mathrm D}=0$ elsewhere. A threshold $\Psi^*$ on the modified sensor
is therefore the threshold $(\Psi^*)^2$ on the classical ratio: the values
$0.1$, $0.2$, $0.4$ below correspond to $0.01$, $0.04$, $0.16$.)*

**Naming: two "modified" Ducros sensors.** [Pirozzoli (2011a)](/sources/pirozzoli-2011.md)
(§3.2, Fig. 4) uses the name *modified Ducros sensor* for the classical
squared ratio $\Phi_{\mathrm D}$ with the flow-scale regularization
$\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$, so that it "is only activated
when the local dilatation becomes larger than a typical large-scale velocity
gradient"; it keeps the square and flags expansions. De Vanna et al. give the
same name, with the same $\epsilon_{\mathrm D}$, to the compression-only,
unsquared $\Psi_{\mathrm D}$ above. The name designates the regularization in
the first usage and the form in the second. In the review's comparison on an
instantaneous transonic shock/boundary-layer DNS field (Fig. 4), with
thresholds chosen so that each sensor gives a similar picture of the shock
system, "the modified Ducros sensor is capable of selectively isolating
genuine shocks, whereas other simple sensors", Jameson's, Hill & Pullin's and
Visbal & Gaitonde's (evaluated on pressure), "also mark smooth regions
populated by vortical structures". The review's Fig. 6 shows the
shock system of a transonic shock/boundary-layer DNS, run with a sixth-order
central split scheme switched to WENO5 by the modified sensor, as the
isosurface $\Phi_{\mathrm D}=0.0025$ (§5); the switching threshold itself
is not printed. *(Compiler check, not in the sources: with equal
$\epsilon_{\mathrm D}$, $\Phi_{\mathrm D}=0.0025$ is $\Psi_{\mathrm D}=0.05$
in compressions, the threshold of Duronio & Di Mascio below.)*

**Regularization.** The two groups set $\epsilon_{\mathrm D}$ in opposite
ways. Sciacovelli et al. take a fixed $10^{-16}$. They recall that the
remedy of an earlier work for spurious activation is to parametrize
$\epsilon_{\mathrm D}$ by the flow scales, "at the cost of generality", and
prefer to multiply by two other factors (§3). De Vanna et al. scale
$\epsilon_{\mathrm D}$ with a free-stream velocity gradient, which is that
flow-scale parametrization; so does Pirozzoli (2011a, §3.2) with
$\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$, because the original ratio "does
not perform properly outside of the wall layer", where
$\nabla\times v\approx0$, "due to excessive sensitivity to dilatational
fluctuations". The original
$\epsilon_{\mathrm D}=10^{-30}$ of Ducros et al. (1999) only prevents $0/0$. *(Compiler check, not in the sources: with
$\epsilon_{\mathrm D}>0$ the sensor stays below one, so a threshold
$\Psi^*=1$ never flags. De Vanna et al. (2023a, §6) call $\Psi^*=1$
"assumable as a pure energy-preserving strategy", which agrees.)*

## Use in hybrid central/TENO schemes

In URANOS the sensor is evaluated at cell faces. Where
$\Psi_{\mathrm D,i+1/2}>\Psi^*$, the face and a band of neighbours use
WENO-Z or TENO, and the sixth-order kinetic-energy-preserving central scheme
of Pirozzoli is used elsewhere
([split convective forms](/methods/split-convective-forms.md)). The band is
2, 3 or 4 cells for orders 3, 5 and 7 (De Vanna et al. 2023a, §3.2;
De Vanna et al. 2023b, §3.2). $\Psi^*=0$ means pure WENO or TENO everywhere.
The paper also offers two other a priori detectors, a density gradient and a
density jump. It recommends the Ducros form for wall flows and states that
$\Psi^*$ "is strongly dependent on the flow" and needs preliminary tuning
(De Vanna et al. 2023b, §3.2, Eqs. (8)–(10)).

**Thresholds measured on wall turbulence.** De Vanna et al. (2023a) run a
parameter study of $\Psi^*$ on wall-modelled LES of spatially developing
boundary layers ([wall-modelled LES](/methods/wall-modeled-les.md);
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md);
§§4.3–4.4, Figs. 5–9, Tables 2–4). The flow is nominally shock-free.

- At Mach 2, $\Psi^*=0.1$ already restores realistic wall statistics where
  pure WENO-Z or TENO damp or destroy wall turbulence. With $\Psi^*=0.2$ a
  dependence on the WENO order persists but does not significantly affect
  global accuracy. With $\Psi^*=0.4$ the WENO and TENO profiles collapse onto
  identical curves, because most of the flow is computed by the central
  scheme.
- At Mach 5.86 the pure central scheme diverges, which the authors attribute
  to shocklets. $\Psi^*=0.2$ is "the highest limit that ensures the current
  arrangement's numerical stability" (§4.4), and $\Psi^*\simeq0.2$ is the
  recommended compromise (§6).

The hybrids cost 0.90–1.00 of the pure central scheme per iteration (§4.3.1,
Table 2). The later immersed-boundary work uses $\Psi^*=0.1$ with TENO-A7 and
TENO-A5 (De Vanna et al. 2023c, §§4.3–4.4;
[adaptive TENO](/methods/adaptive-teno.md)).

**Two more switched schemes.** [Duronio & Di Mascio (2024)](/sources/duronio-2024.md)
(§2, Eq. (7)) use the modified form, compression-only and not squared,
with $\epsilon_{\mathrm D}=v_0^2/L_0^2$ from "suitable velocity and
length scales" (values not printed), calling it "the classical shock
sensor" of Ducros et al.; averaged to faces, it switches on the
AUSM$^+$-up dissipation of the convective flux of a
kinetic-energy-preserving central scheme in
[OpenFOAM](/software/openfoam.md) above $\Psi^*=0.05$. The pressure
dissipation is not switched. [Jiao et al. (2024)](/sources/jiao-2024.md)
(App. D) use the classical squared ratio with $\epsilon_{\mathrm D}=10^{-20}$,
combined with gas and vapour volume-fraction variation sensors, to
blend a fourth-order central, an upwind MUSCL and a THINC reconstruction
in an implicit-LES scheme for multiphase flow, with the threshold 0.95
they take from Egerer et al. The form Duronio & Di Mascio call
"classical" is thus neither the squared ratio Jiao et al. use nor the
original of Ducros et al. (1999), which is the squared ratio used as a factor
of Jameson's pressure sensor (see Qualifications).

## Use as a blending weight towards first order

McQuaid & Brehm (§3.8, Eq. (20)) blend, on the block-structured
Cartesian off-body grid of their overset hypersonic solver, the
fifth-order finite-difference [WENO-Z](/methods/weno-z.md) flux
(reconstruction in [characteristic variables](/methods/characteristic-decomposition.md)
on the Roe-averaged state, Steger–Warming flux splitting) with a
first-order flux $\hat f^{\mathrm O1}_{i+1/2}$ (page-local),

$$\hat f_{i+1/2}=(1-\tilde\alpha_{\mathrm D})\,\hat f^{\mathrm{WENO}}_{i+1/2}+\tilde\alpha_{\mathrm D}\,\hat f^{\mathrm O1}_{i+1/2},$$

where $\tilde\alpha_{\mathrm D}$ (page-local) is the "Ducros sensor
value" of the "classical Ducros sensor" they cite; the sensor formula,
its regularization and any threshold are not printed. The scheme thus
falls fully to first order at strong shocks; unlike the hybrid switches
above, the partner of WENO-Z is a first-order flux, not an
energy-preserving central one (see [hybrid central–WENO schemes](/methods/hybrid-weno.md)).
They motivate it by shock-induced artefacts on grids not aligned with
the shock: "even the reduced order WENO scheme can produce pre- and
post-shock artifacts". On the Mach 9.47 Mars Science Laboratory capsule
at $8^\circ$ incidence they compare four Cartesian flux treatments,
WENO-Z with local Rusanov splitting, with stencil-maximum ("global")
Rusanov splitting, with Steger–Warming splitting, and the Ducros blend
(§4.1, Fig. 14). The first three send velocity streaks from the shock
to the interface with the near-body grid, which imprint a significant
artefact in the surface heat flux; only the Ducros blend removes it, at
the cost of a slightly more diffused shock. They assume, without
testing it, that the cause is the misalignment of shock and grid, and
attribute a slight leeward over-prediction of the heating and a
somewhat low peak temperature (AS-202 capsule) to the first-order
reduction (§4.1, §4.3). They describe the sensor as detecting shocks
"with a minimal increase in computational overhead".

## Use as a factor of an exponential flux limiter

[Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) (§4.1.3, arXiv v3) use the
modified, compression-only form as one factor of a shock-sensor limiting of the
bound-preserving [Active Flux](/methods/active-flux.md) method. With cell values recovered
from the cell averages and central differences for the dilatation and the vorticity on
non-uniform meshes, they take $\Psi_{\mathrm D}$ with $\epsilon_{\mathrm D}=10^{-40}$ and multiply
it by a Jameson pressure sensor, written page-locally
$\varphi_{\mathrm J,i}=\lvert\bar p_{i+1}-2\bar p_i+\bar p_{i-1}\rvert/\lvert\bar p_{i+1}+2\bar p_i+\bar p_{i-1}\rvert$.
Face values are the maxima of the two adjacent cell values, and the blending factor
(page-local $\theta^{\mathrm s}$, the source's $\ell^{\mathrm s}$, renamed to keep the Lagrange basis $\ell_j$)

$$\theta^{\mathrm s}_{i+1/2}=\exp\big(-\kappa_{\mathrm s}\,\varphi_{\mathrm J,i+1/2}\,\Psi_{\mathrm D,i+1/2}\big)\in(0,1]$$

scales the antidiffusive part of the already [convex-limited](/methods/convex-limiting.md)
flux, $\hat f=\hat f^{\mathrm L}+\theta^{\mathrm s}\big(\hat f^{\mathrm{Lim}}-\hat f^{\mathrm L}\big)$, with
$\hat f^{\mathrm L}$ the first-order local Lax–Friedrichs flux (page-local). Since
$\theta^{\mathrm s}\le1$ the flux moves further towards $\hat f^{\mathrm L}$, so bound preservation
is kept. The strength $\kappa_{\mathrm s}$ (page-local) is problem dependent ($0.5$, $1$ or $10$ in the
tests), and "its optimal choice needs further investigation"; the limiting strongly reduces the
oscillations behind strong shocks in the forward-facing step, the double Mach reflection and a
2D Riemann problem, and accelerates the steady residual convergence of an oblique shock
reflection (§4.1.3; Examples 5.9, D.5–D.7). In 1D the factor becomes the 0/1 switch
$\max\big(-(\bar v_{i+1}-\bar v_{i-1})/(\lvert\bar v_{i+1}-\bar v_{i-1}\rvert+10^{-40}),0\big)$
(App. C.1.3). Unlike the hybrid switches above, the sensor does not choose between a central and
a shock-capturing flux; it is a continuous weight towards first order, like McQuaid & Brehm's
blend above, but multiplied by a pressure sensor.

## Use as a factor of an adaptive Rusanov coefficient

[Wang et al. (2023a)](/sources/wang-2023.md) (§3.2, Eq. (21)) multiply the classical squared
ratio, with $\epsilon_{\mathrm D}=10^{-40}$ (footnote 2: to avoid zero denominators in IEEE
double precision), by two Jameson-type normalized second differences, one of pressure and one
of density, on primitive variables and with second-order central differences for the
dilatation and the curl:

$$\varphi_{\mathrm F,i}=\Phi_{\mathrm D,i}\,\varphi_{\mathrm J,i}[p]\,\varphi_{\mathrm J,i}[\rho],\qquad \varphi_{\mathrm J,i}[q]=\left\lvert\frac{q_{i+1}-2q_i+q_{i-1}}{q_{i+1}+2q_i+q_{i-1}}\right\rvert$$

(page-local $\varphi_{\mathrm F}$; $\varphi_{\mathrm J}[q]$ is the Duan et al. pressure factor
above, applied to $q=p$ and $q=\rho$). The sensor sets the modifier
$\mathsf k_i=\max\big(\mathsf k_{\min},1-\exp(-\delta_{\mathrm F}\varphi_{\mathrm F,i})\big)$,
$\mathsf k_{\min}=0.1$, $\delta_{\mathrm F}=10^5$ (page-local), of the LLF-M flux, a
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) whose coefficient
$a_{i+1/2}$ is multiplied by $\max\{\mathsf k_i,\mathsf k_{i+1}\}$ inside fifth-order
[alternative WENO](/methods/alternative-weno.md). The authors give the product as a repair of
the stand-alone Ducros sensor's "indiscriminate activation" where dilatation and vorticity are
both small, in irrotational flow outside boundary and mixing layers, the failure Sciacovelli et
al. report below; the product of $\Phi_{\mathrm D}$ and the pressure factor is, however, the
original construction of Ducros et al. (1999), to which Wang et al. add the density factor
(Origin above). They state that the sensor is $O(1)$ where the divergence is high and tends
to zero in vortex-dominated regions, and call it "non-dimensional scale-invariant" (§3.2). On
2D Riemann configuration 6 they plot the three factors separately: $\Phi_{\mathrm D}$ marks
dilatation against vorticity, the two Jameson factors the high pressure and density gradients,
and the product keeps the smooth shear vortices unflagged (§4.7, Fig. 17). In 1D, they note,
the Ducros factor "measures only the velocity gradient" (§4.4). Unlike Duan et al.'s
exponential limiter, the weight does not move the flux towards first order: it only scales the
dissipation coefficient of a two-point flux between $0.1a_{i+1/2}$ and $a_{i+1/2}$.

## Failure modes and further multiplications

- **Smooth irrotational flow.** Where both the dilatation and the vorticity are
  small, as outside boundary and mixing layers, the classical ratio can be close
  to one. On an underexpanded jet it is near unity "even in smooth irrotational
  regions" (Sciacovelli et al. 2021, §3, §5.1, Fig. 8(a)). Pirozzoli (2011a,
  §3.2, Fig. 4) reports the same over-sensitivity outside the wall layer of a
  transonic shock/boundary-layer DNS. Ducros et al. (1999, §4.4, Fig. 23)
  already show the stand-alone factor at the level 0.1 selecting small
  turbulent scales; what keeps their sensor small off-shock is its weak
  correlation with the Jameson factor (§4.1, Figs. 5–6), i.e. the product,
  never the ratio alone, is the 1999 sensor.
- **One space dimension.** In 1D the Ducros factor is inactive (Sciacovelli et
  al. 2021, §4.3); Wang et al. (2023a, §4.4) say it "measures only the velocity
  gradient" there. *(Compiler check, not in the sources: with
  $\nabla\times v=0$, $\Phi_{\mathrm D}\to1$ wherever
  $(\nabla\cdot v)^2\gg\epsilon_{\mathrm D}$, so the factor does not separate a
  shock from a smooth compression.)*
- **Under-resolved turbulence.** De Vanna et al. (2023a, §3.2, §4.3.3) state
  that grid noise and physical turbulent fluctuations "are often read as shocks"
  by shock detectors in low-resolution settings such as WMLES. De Vanna et al.
  (2023c, §3.2) make the same point for ENO-like detection and call the modified
  Ducros sensor "peculiarly accurate" in such cases, with "minimal intrusion of
  shock-capturing where it is not required". They cite Ducros et al. (1999)
  and their 2023a study for this; the 2023a study varies the threshold of the
  Ducros sensor only and compares it with no other detector, and
  [Ducros et al. (1999)](/sources/ducros-1999.md) test only the squared
  product $\Phi_{\mathrm D}\varphi_{\mathrm J}$, on $32^3$ decaying turbulence
  and shock/turbulence LES, with neither the compression-only form nor wall
  flows (see Qualifications).
- **Case dependence.** [Fu (2023)](/sources/fu-2023.md) (§3.4) calls physical
  sensors such as Ducros' case-dependent. Fu presents the TENO-based indicator as
  "more universal" because it separates non-smooth scales in spectral space
  ([hybrid central–WENO schemes](/methods/hybrid-weno.md)). Fu also records that
  the TENO6-A variant used for transitional shock/boundary-layer interaction
  replaces the TENO discontinuity measure by a modified Ducros sensor (§4.1,
  §5.4; [adaptive TENO](/methods/adaptive-teno.md)). [Liang & Fu (2024b)](/sources/liang-2024-b.md)
  (§3.1) make the same claim for their eight-point TENO-type indicator of
  the TENO-S hybrid, which separates non-smooth high-wavenumber
  fluctuations "in the wavenumber space" and is "more universal for
  general conservation laws" than physical-variable sensors such as the
  Ducros sensor; they show indicator maps but no comparison with a
  Ducros-switched run ([targeted ENO](/methods/targeted-eno.md)).
  [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§6) finds that the Ducros
  sensor performs "reasonably well in many shock/turbulence interaction
  problems, particularly with some minor case-by-case modification and tuning
  of the threshold value", which agrees with the tuning De Vanna et al.
  (2023b) require.

**Multiplication by other sensors.** Multiplication by Jameson's pressure
sensor is the original construction of Ducros et al. (1999), not a later
repair (Origin above). Sciacovelli et al. (§3, Eq. (36)) multiply the
classical ratio by the Bhagatwala–Lele dilatation switch as well as by
Jameson's pressure sensor ($\Xi_i$, written out on
[troubled-cell indicators](/definitions/troubled-cell-indicator.md) and
[numerical dissipation](/definitions/numerical-dissipation.md)). On the
underexpanded jet the product confines the low-order dissipation to the
intercepting shocks, the Mach disk and the reflected shocks, with values below
$0.02$ elsewhere (§5.1, Fig. 8). Wang et al. (2023a) multiply the 1999 product
by a density factor instead (above). The measured failures of the stand-alone
ratio stand; what they measure is a form that the originating paper never
used alone.

## Not a Ducros sensor: Jameson-type pressure sensors

The pressure sensor of Jameson et al. that enters Sciacovelli et al.'s
product $\Xi_i$ is a different detector, a normalized second difference
of a scalar rather than a velocity-gradient ratio.
[Berta et al. (2024)](/sources/berta-2024.md) (§3.4, Eq. (35), arXiv v4)
use a Jameson-type sensor of this kind, not the Ducros sensor, in their
fourth-order MHD finite-volume scheme: per direction,
$(\bar q_{i+1}-2\bar q_i+\bar q_{i-1})/(\lvert\bar q_{i+1}\rvert+2\lvert\bar q_i\rvert+\lvert\bar q_{i-1}\rvert+\epsilon)$
on the cell averages $\bar q$ (page-local) of density, pressure and magnetic pressure, the
maximum over them and the Euclidean norm over directions compared with
a threshold whose value is not printed; flagged cells and their first
neighbours drop to a lower-order reconstruction. They note that it
keeps the stencil compact, "albeit three zones may not be sufficient to
distinguish a discontinuity from a smooth extremum", and propose a
derivatives-ratio detector beside it (see
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Qualifications

- Duan et al. print the Jameson sensor and the face blending only for $x$-faces, the
  $y$-direction counterparts being implied ("explanations will be given for the
  $x$-direction", §4.1.3).
- McQuaid & Brehm print neither the Ducros formula nor a threshold, so
  their blend cannot be compared quantitatively with the hybrid
  switches above; it is a continuous weight, not a binary switch.
- Thresholds do not transfer between the two forms. A value of $\Psi^*$ for
  the modified sensor equals $(\Psi^*)^2$ for the classical ratio (compiler
  check above), and both depend on the choice of $\epsilon_{\mathrm D}$. The
  recommended $\Psi^*\simeq0.2$ was obtained on boundary layers at Mach 2 and
  5.86 with $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ (De Vanna et al.
  2023a).
- The sensor is tested as a cell-face value $\Psi_{\mathrm D,i+1/2}$, but
  none of the three De Vanna papers states how the face value is formed from
  the velocity gradients at the grid points. For the original product,
  Ducros et al. (1999, Eq. (24)) take the maximum of the two cell products
  $\varphi_{\mathrm J,i}\Phi_{\mathrm D,i}$, $\varphi_{\mathrm J,i+1}\Phi_{\mathrm D,i+1}$;
  they do not print the discretization of the velocity gradients either.
- **The originating paper's scope.** Ducros et al. (1999) define the
  squared ratio, even in $\nabla\cdot v$ and so not compression-only, and use
  it only as a factor of Jameson's pressure sensor, with a second-order JST
  dissipation and $k_2=1.5$, on decaying turbulence, a 2D shock–vortex
  interaction and 3D shock/turbulence LES, the runs with a shock in the shock
  frame. They call
  the sensor "relatively costless" without a figure.
- **Later attributions, side by side with the original.** Duronio & Di Mascio
  (2024, §2) call the compression-only, unsquared form "the classical shock
  sensor" of Ducros et al.; the 1999 paper defines the squared ratio (Eq. (22))
  and uses it only inside the product (Eqs. (23)–(24)). De Vanna et al.
  (2023c, §3.2) cite Ducros et al. (1999) for the modified sensor being
  "peculiarly accurate" in low-resolution WMLES; the 1999 paper contains
  neither that form nor wall-bounded or wall-modelled flows. Pirozzoli (2011a,
  §3.2, §5) recalls the 1999 scheme as a nonlinear (characteristic-based)
  filter in which the product replaces Harten's switch; the 1999 paper writes
  the dissipation as part of the numerical flux (Eq. (8)) of a four-stage
  Runge–Kutta finite-volume scheme, keeps "a scalar dissipation model" (§3)
  and mentions neither filtering nor Harten's switch. Sciacovelli et al. and
  Wang et al. (2023a) present the multiplication by other sensors as a repair
  of the stand-alone ratio, which the originating paper never used alone.
  None of these is a disagreement of measured results.
- **Two meanings of "modified".** Pirozzoli (2011a) calls the squared ratio
  with $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ "modified"; De Vanna et
  al. call the compression-only, unsquared form "modified" (Naming above);
  Ducros et al. (1999) call their product a "modified Jameson's sensor".
- De Vanna et al. (2023a, §3.2, Eq. (9)) and De Vanna et al. (2023b,
  Eq. (10)) use the same symbol for the sensor regularization and for the
  WENO-Z regularization $\epsilon=10^{-12}$. The page keeps them apart.

# Citations

- [Ducros et al. (1999)](/sources/ducros-1999.md) — §1; §3, Eqs. (8)–(13), (22)–(24), pp. 522–525; §4.1, Table I, Figs. 1–3, 5–8; §4.2, Figs. 10–11; §4.3, Figs. 16, 19–20; §4.4, Figs. 23–24; §5; §6: original squared ratio as a factor of Jameson's pressure sensor in second-order JST dissipation, Galilean-invariance motivation, face rule, tests.
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §3.2, Eq. (29), Fig. 4; §5, Fig. 6; §6: the ratio recalled in nonlinear filtering, "modified Ducros sensor" with $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$, sensor comparison, tuning.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, Eq. (36); §4.3; §5.1, Fig. 8: classical Ducros factor, its failures, product sensor (arXiv v1).
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.2, Eq. (9); §§4.3–4.4, Tables 2–4, Figs. 5–9; §6: modified sensor and threshold study.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §3.2, Eqs. (8)–(10): improved Ducros sensor among URANOS detectors, flagged band, tuning.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §3.2, Eq. (13); §§4.3–4.4: index form, $\Psi^*=0.1$ with TENO-A.
- [Fu (2023)](/sources/fu-2023.md) — §3.4, §4.1, §5.4: case dependence of physical sensors; modified Ducros sensor in TENO6-A.
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §2, Eq. (7): modified form switching AUSM$^+$-up dissipation, $\Psi^*=0.05$.
- [Jiao et al. (2024)](/sources/jiao-2024.md) — App. D: classical ratio in a multiphase implicit-LES blending sensor.
- [McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) — §3.8, Eq. (20); §4.1, Fig. 14; §4.3: Ducros-weighted blend of WENO-Z with a first-order flux, heating artefacts on non-aligned grids.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §3.1: TENO-type indicator claimed more universal than the Ducros sensor.
- [Berta et al. (2024)](/sources/berta-2024.md) — §3.4, Eq. (35): Jameson-type sensor, distinct from Ducros' (arXiv v4).
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §4.1.3; App. C.1.3; Examples 5.9, D.5–D.7: modified Ducros sensor times a Jameson pressure sensor in an exponential limiting of bound-preserving Active Flux (arXiv v3).
- [Wang et al. (2023a)](/sources/wang-2023.md) — §3.2, Eq. (21), footnote 2; §4.4; §4.7, Fig. 17: classical ratio times pressure and density Jameson factors as the sensor of the LLF-M flux.
