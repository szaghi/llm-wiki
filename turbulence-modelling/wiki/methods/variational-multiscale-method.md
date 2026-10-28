---
type: Method
title: "Variational multiscale method"
description: "The variational multiscale method splits the finite-element solution into resolved and fine scales and models the fine scales from the residual of the resolved ones; the sources read it as an implicit LES, budget each fine-scale term, flip an anti-dissipative one, carry it to immersed boundaries, and replace the residual model by off-line fine-scale DNS."
status: established
aliases: [VMS, residual-based VMS, residual-based variational multiscale method, RB-VMS, VMS-LES, residual-based LES, modified VMS, multiscale Smagorinsky model, CG-VMSD]
tags: [les, implicit-les, sgs-model, numerical-dissipation, immersed-boundary]
timestamp: 2026-10-28T02:14:00Z
---

# Variational multiscale method

The **variational multiscale (VMS) method** splits the solution and the
weighting functions of a Galerkin finite-element discretization into a
resolved (coarse) part, the finite-element field, and an unresolved (fine)
part, and replaces the fine part by a model driven by the residual of the
resolved equations. Written for the incompressible Navier–Stokes equations
with kinematic pressure, $\boldsymbol u=\boldsymbol u^{>}+\boldsymbol u^{<}$,
$p=p^{>}+p^{<}$, where the split is a variational projection between
finite-element spaces, not a convolution filter, so neither the registry's
overbar nor a test-filter hat applies. In the **residual-based** form the
fine scales are algebraic functions of the resolved residuals,

$$\boldsymbol u^{<}=-\tau_{\mathrm M}\,\boldsymbol r_{\mathrm M}(\boldsymbol u^{>},p^{>}),\qquad p^{<}=-\tau_{\mathrm C}\,r_{\mathrm C}(\boldsymbol u^{>}),\qquad r_{\mathrm C}=\nabla\cdot\boldsymbol u^{>},$$

with $\boldsymbol r_{\mathrm M}$ the strong momentum residual and
$\tau_{\mathrm M}$, $\tau_{\mathrm C}$ (page-local) the momentum and
continuity stabilization parameters; $\boldsymbol w$, $q$ (page-local) denote
the velocity and pressure weighting functions. No eddy viscosity and no
explicit subgrid stress appear: the closure is the set of fine-scale terms
the split leaves in the resolved equation. [Chen et al. (2022)](/sources/chen-2022-g.md)
(§1, §7) therefore classify residual-based VMS LES as an
[implicit LES](/definitions/implicit-les.md) whose "unresolved small-scale
model is an addition of purely dissipative numerical terms and no eddy
viscosity is introduced", and [Kang & Masud (2022)](/sources/kang-2022.md)
(§3.4) use the same closure, in a bubble-function form, as the turbulence
model of an [immersed boundary method](/methods/immersed-boundary-method.md).

## Fine-scale terms of the resolved equation

Inserting the split into the Galerkin form and keeping the resolved
weighting functions gives the resolved equation. [Chen et al. (2022)](/sources/chen-2022-g.md)
(§2.3, Eq. 10), citing Bazilevs et al. and Calo, list five
element-wise fine-scale terms beside the Galerkin terms:

| term | form (sum over elements) | reading cited by Chen et al. |
|---|---|---|
| I | $-(\nabla\boldsymbol w,\ \boldsymbol u^{>}\otimes\boldsymbol u^{<})$ | cross stress; equals the SUPG streamline term |
| II | $+(\boldsymbol w,\ \boldsymbol u^{<}\cdot\nabla\boldsymbol u^{>})$ | cross stress |
| III | $-(\nabla\boldsymbol w,\ \boldsymbol u^{<}\otimes\boldsymbol u^{<})$ | "Reynolds stress" of the fine scales |
| IV | $-(\nabla\cdot\boldsymbol w,\ p^{<})$ | fine-scale pressure; least-squares incompressibility (LSIC) term |
| V | $-(\nabla q,\ \boldsymbol u^{<})$ | fine-scale velocity tested by the pressure weighting function |

The quoted interpretation is that terms I+II are the analogue of the cross
stress and term III of the Reynolds part of the subgrid stress, and that "no
assumption about the effect of the small scales on the represented ones is
introduced nor is an eddy viscosity required" (§2.3). In the SUPG method
"only Terms (1) and (4) are considered" (§6).
[Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) (§1,
Eq. 10) use SUPG/PSPG stabilization without any subgrid model on the
[periodic hill](/benchmarks/periodic-hill.md).

**Stabilization parameters.** Chen et al. (Eqs. 13–15) take
$\tau_{\mathrm M}=(c_1\,\boldsymbol u^{>}\cdot\boldsymbol G\boldsymbol u^{>}+c_2\nu^2\boldsymbol G\!:\!\boldsymbol G+c_3/\Delta t^2)^{-1/2}$
and $\tau_{\mathrm C}=\boldsymbol u^{>}\cdot\boldsymbol G\boldsymbol u^{>}/\mathrm{tr}\,\boldsymbol G$,
with $\boldsymbol G=(\partial\boldsymbol\xi/\partial\boldsymbol x)^T(\partial\boldsymbol\xi/\partial\boldsymbol x)$
the element metric tensor (page-local) and $c_1=4$, $c_2=36$, $c_3=4$ for
trilinear hexahedra; the fine scales are quasi-static ("static unresolved
small-scale model terms", §1). The $1/\Delta t^2$ entry makes the
stabilization, and so the implicit dissipation, depend on the time step:
Prieto Saavedra et al. (§4.2) report that on a coarse mesh a smaller
$\Delta t$ lowers the stabilization dissipation and degrades the Reynolds
stresses of their SUPG/PSPG implicit LES.

## Dissipation of each term

Setting $\boldsymbol w=\boldsymbol u^{>}$ turns the resolved equation into a
resolved kinetic-energy equation (Chen et al. 2022, §3, Eq. 24), in which
the second line carries the four fine-scale contributions

$$(1)=(\nabla\boldsymbol u^{>})\!:\!(\boldsymbol u^{>}\otimes\boldsymbol u^{<}),\quad (2)=-\boldsymbol u^{<}\cdot\nabla\big(\tfrac12\lvert\boldsymbol u^{>}\rvert^2\big),\quad (3)=(\nabla\boldsymbol u^{>})\!:\!(\boldsymbol u^{<}\otimes\boldsymbol u^{<}),\quad (4)=(\nabla\cdot\boldsymbol u^{>})\,p^{<},$$

which "in principle transfer the kinetic energy from the resolved large
scales to the unresolved small scales". Averaged over the homogeneous
directions and time (Eqs. 31–37; negative = dissipation of resolved energy)
in a [turbulent channel](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=180$ on a coarse $32\times64\times32$ trilinear mesh
($\Delta y^+_{\min}=0.88$), Chen et al. find (§5, Figs. 3–5):

- term (1), the SUPG term, is negative across the whole channel and carries,
  with term (4), most of the dissipation; the authors argue from its dominant
  convective part that it "always stays negative when $j=k$". With the
  printed approximation $u^<_i\approx-\tau_{\mathrm M}u^>_k\partial_ku^>_i$,
  term (1) summed over all indices equals
  $-\tau_{\mathrm M}\lvert\boldsymbol u^{>}\cdot\nabla\boldsymbol u^{>}\rvert^2\le0$,
  and term (4) equals $-\tau_{\mathrm C}(\nabla\cdot\boldsymbol u^{>})^2\le0$
  *(compiler check, not in the sources)*;
- term (2) has a **positive** average over most of the channel: it "does not
  dissipate the turbulent kinetic energy but increases energy", which
  "differs from the intention of the turbulent model", against the
  large-to-small transfer reading that Chen et al. (§3) cite from Bazilevs
  and Calo;
- term (3) dissipates but is two to three orders of magnitude smaller than
  term (1);
- term (4), the LSIC term, "plays an important role in providing the
  additional dissipation", largest in the spanwise component.

Compared with the subgrid dissipation of a finite-difference
[Smagorinsky](/methods/smagorinsky-model.md) ($C_s=0.1$) and
[dynamic](/methods/dynamic-procedure.md) LES on the same mesh, the total VMS
dissipation is much smaller in the inner layer and larger in the outer
layer, and its three directional components are comparable, whereas the
classical subgrid dissipation sits mainly in the streamwise component
(§5, Fig. 3). The VMS LES gives better mean velocity, r.m.s. fluctuations and
Reynolds shear stress than both classical models on that mesh (§4.2,
Figs. 1–2). The classical runs use second-order central finite differences
on a staggered grid and the VMS runs trilinear finite elements on the same
mesh (§4.1).

## Modified VMS: reversing the anti-dissipative term

Chen et al. (2022) (§6, Eq. 38) propose a "new stabilized finite element
formulation" that keeps terms I, III, IV and V with
$\boldsymbol u^{<}=-\tau_{\mathrm M}\boldsymbol r_{\mathrm M}$ and
$p^{<}=-\tau_{\mathrm C}r_{\mathrm C}$, and **reverses the sign of term II**,
$+(\boldsymbol w,\ \tau_{\mathrm M}\boldsymbol r_{\mathrm M}\cdot\nabla\boldsymbol u^{>})$.
In its energy equation (Eq. 39) all four contributions are dissipative, and
the total numerical diffusion orders as modified VMS > SUPG > VMS
(§6.2, Fig. 8a). The formulation stays residual-based, so the authors argue
that its numerical diffusion "dynamically reduces with refinement until it
vanishes when grid spacing satisfies DNS" (§6.2, §7); no refinement study
is shown, each case uses one mesh. Results (§6.1–6.2, Figs. 6–7):

- 2-D lid-driven cavity at $Re=1000$ ($32\times32$ cells): VMS, SUPG and the
  modified form are very close; at $Re=125\,000$ ($64\times64$) "the VMS
  method does not show an advantage in comparison with the SUPG method" and
  the modified form is closest to the reference near the walls;
- channel at $Re_\tau=180$: the three agree for $y^+<10$; in the outer layer
  SUPG is slightly closer to DNS than VMS and the modified form is clearly
  best; SUPG and the modified form improve $u'_{\mathrm{rms}}$ in the buffer
  layer. The authors explain the gain by larger numerical diffusion, which
  "dissipates the bulk velocity and allows the mean velocity profile to
  become closer to the solution when using a coarse mesh" (§6.2).

Chen et al. (§1) cite Ahmed and John as having reported that
residual-based VMS shows no advantage over SUPG, with "no physical
elaboration", and present their term budget as that elaboration.

## Bubble-function VMS with fine-scale memory

[Kang & Masud (2022)](/sources/kang-2022.md) (§3.4, Eqs. 49–59) use the
residual-based VMS LES that they cite from Calderer & Masud and Masud &
Calderer, in which the fine scales are expanded in element bubble
functions (Table 2: $(1-\xi^2)(1-\eta^2)(1-\zeta^2)$ on hexahedra,
$256\,\xi\eta\zeta(1-\xi-\eta-\zeta)$ on tetrahedra) and keep their own time
history:

$$\boldsymbol u^{<}=-\boldsymbol\tau_{\mathrm M}\,\boldsymbol r_{\mathrm M}+\mathcal F\big(\boldsymbol u^{<},\partial_t\boldsymbol u^{<}\big)\big|_n,\qquad p^{<}=-\boldsymbol\tau_{\mathrm C}\,r_{\mathrm C},$$

where $\boldsymbol\tau_{\mathrm M}$ and $\boldsymbol\tau_{\mathrm C}$ are
element tensors obtained from the bubble integrals and the generalized-$\alpha$
time-integration parameters, and $\mathcal F$ (page-local) is the fine-scale
history term of the previous step. The closure in the resolved equation
(Eq. 49) contains the fine-scale inertia, a convective/inf-sup term, a
weak mass-conservation term and $-(\nabla\boldsymbol w,\ \rho\,\boldsymbol u^{<}\otimes\boldsymbol u^{<})$,
the higher-order fine-scale (cross and Reynolds-type) contribution, which
can be dropped for non-turbulent flows (Remark, §3.5). In the implementation
the velocity and pressure fine scales are uncoupled (the level-2 bubble
term is neglected). Keeping the fine-scale inertia, the authors argue, keeps
the stabilization from vanishing as $\Delta t\to0$, unlike fine-scale models
without it (citing Hsu et al.; Lemma 1, §3.2.1). A simplified variant
without the history term $(\partial_t\boldsymbol u^{<})_n$ gives "identical
results" for the sphere at $Re=10^4$ with $\Delta t=0.01$ and $0.0025$
(§5.2, Figs. 19–24).

The same split applied to the interface band of cut elements yields the
weak Dirichlet conditions, a derived Lagrange multiplier and the
parameter-free interface stabilization of their
[immersed boundary method](/methods/immersed-boundary-method.md) (§3.2–3.3).
With it the VMS LES reproduces the [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
at $Re_D=3900$ (about 1.5 million linear hexahedra) against the LES of
Kravchenko & Moin and experiments, and the sphere wake at $Re=10^4$ (7.3
million tetrahedra) with $C_D=0.410$ and $0.405$ at the two time steps
against 0.402 in the DNS of Rodríguez et al. (§5.1–5.2, Table 5).

## Projection-based and multiscale-eddy-viscosity variants (inline)

Other sources use the multiscale split to confine an *explicit* eddy
viscosity to the small resolved scales, rather than to model the fine
scales from residuals:

- [Lederer et al. (2023)](/sources/lederer-2023.md) (§3.1, Eqs. 10–14) cast
  a projection-based VMS into a mixed finite-element method: the
  [WALE](/methods/wale-model.md) eddy viscosity acts on the strain minus its
  $L^2$ projection onto element polynomials of degree $m$; an empty
  large-scale space recovers classical LES. On the channel it is no better
  than implicit LES (bulk-Reynolds error 16.3%, 4.7%, 2.7% against 13.4%,
  3.1%, 1.1% on $6^3$, $12^3$, $16^3$ elements, §4.1, Table 2); see the
  [high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md);
- [Flad & Gassner (2017)](/sources/flad-2017.md) (App. B, Eq. B.1) evaluate
  a small–small VMS [Smagorinsky](/methods/smagorinsky-model.md) model from
  high-pass filtered gradients and find no improvement over de-aliased DG
  implicit LES;
- [Volpiani (2024)](/sources/volpiani-2024.md) (App. 2) run "large–small"
  and "small–small" multiscale Smagorinsky models, which Volpiani cites
  from Hughes et al.; they improve the dissipation history of the compressible
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), most on $128^3$
  (§5, Figs. 15c–d).

## Fine scales solved numerically, and other readings (inline)

- **Fine scales from off-line DNS.** [Idelsohn et al. (2024)](/sources/idelsohn-2024.md)
  (§1.4) frame their [pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md)
  as "a variation of VMS" in which the fine-scale solution is computed
  numerically instead of being approximated through Green functions or
  residuals: the split $u_i=u^{>}_i+u^{<}_i$ takes the coarse part as the
  piecewise-linear finite-element (or finite-volume) field, the fine part
  is the DNS of a periodic representative volume element run off-line, and
  the only fine-to-coarse term kept in the coarse equation is the averaged
  fine-scale product $\rho\,u^{<}_iu^{<}_j$, the analogue of term III above
  (§2.4–2.6). They also present the method as an off-line evolution of
  FE² and as a reduced-order model (§1.4).
- **Cost of explicit fine-scale fields.** [Hausmann et al. (2022)](/sources/hausmann-2022.md)
  (§I) group VMS with multilevel methods that solve linearized equations
  for the residual (subgrid) velocity, and set them aside as reconstructions
  of the subgrid velocity because of their large overhead at high
  resolution; their own [subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)
  solves a linearized subgrid equation in Fourier modes instead.
- **High-order continuous Galerkin.** [Mani & Dorgan (2023)](/sources/mani-2023.md)
  (§4.4, Fig. 4) report from Ursachi et al. (2020) that adaptive
  continuous-Galerkin VMS with discontinuous subscales (CG-VMSD) at third
  and fourth order needs an order of magnitude less computation time than
  industry-standard second-order methods for the same accuracy (grids
  adapted to a lift-coefficient error below $10^{-4}$ on a three-element
  airfoil), provided curved high-order meshes are available; robust
  adaptation, memory and shock capturing remain open (§4.4).
- **Rotor wakes.** [Stanly et al. (2022)](/sources/stanly-2022.md)
  (§5.3.1, Fig. 15) compare their actuator-line wake with a reference that
  runs an [actuator line](/methods/actuator-line-model.md) inside a VMS
  framework (Ravensbergen et al. 2020); the VMS formulation is cited, not
  used.
- **Blended with RANS for the drag crisis (cited only).** [Mays et al. (2023)](/sources/mays-2023.md)
  (§1) list Moussaed et al. (2014), a RANS/VMS-LES blend by its
  reference-list title, among earlier studies of the supercritical
  [circular cylinder](/benchmarks/circular-cylinder-wake.md); VMS is not
  used in the paper.

## Qualifications

- **One mesh per case.** The comparisons of Chen et al. (2022) use a single
  coarse mesh per flow; the consistency argument (dissipation vanishing with
  refinement) is stated, not shown. Eq. (38) reverses the sign of a term
  that the scale split of Eq. (10) produces; the authors still call the
  result residual-based and consistent (§6).
- **Printed slips in Chen et al. (2022).** Term ④ of Eq. (38) is printed
  $(\nabla\cdot\boldsymbol w,\ \tau_{\mathrm C}\nabla\cdot\boldsymbol w)$,
  with the weighting function in both slots, while the text says it equals
  term IV and the energy equation (39) uses $\tau_{\mathrm C}\nabla\cdot\boldsymbol u^{>}$.
  §6.2 says "the replacement of Term II … with Term ①", whereas the paper's
  own statement below Eq. (38) has term ② replacing II. The pressure term of
  Eqs. (10) and (38) is printed $-(\nabla\boldsymbol w,p)$ without the
  divergence. With kinematic pressure ($\mathrm{m^2/s^2}$) and
  $r_{\mathrm C}$ in $\mathrm{s^{-1}}$, $p^{<}=-\tau_{\mathrm C}r_{\mathrm C}$
  requires $\tau_{\mathrm C}$ in $\mathrm{m^2/s}$, while the printed
  $\tau_{\mathrm C}=\boldsymbol u\cdot\boldsymbol G\boldsymbol u/\mathrm{tr}\,\boldsymbol G$
  has units $\mathrm{m^2/s^2}$ *(compiler check, not in the sources)*.
- **Classical comparison.** No near-wall damping is mentioned for the
  Smagorinsky run of Chen et al. (§4.1), whose "very high dissipation in the
  viscous sublayer ($y^+<5$)" the authors give as the explanation of its
  under-predicted statistics (§5).

# Citations

- [Chen et al. (2022)](/sources/chen-2022-g.md) — §1; §2.3, Eqs. (5)–(15); §3, Eq. (24); §4.1–4.2, Figs. 1–2; §5, Eqs. (31)–(37), Figs. 3–5; §6, Eqs. (38)–(39), Figs. 6–8; §7.
- [Kang & Masud (2022)](/sources/kang-2022.md) — §3.2–3.5, Eqs. (26)–(60), Table 2; §5.1–5.2, Table 5, Figs. 19–24.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §1; Eq. (10); §4.2.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.1, Eqs. (10)–(14); §4.1, Table 2.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, Fig. 3; App. B, Eq. (B.1).
- [Volpiani (2024)](/sources/volpiani-2024.md) — App. 2, Eqs. (26)–(32); §5, Figs. 15c–d.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §1.4; §2.4–2.6, Eqs. (19)–(27).
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §I.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.4, Fig. 4.
- [Stanly et al. (2022)](/sources/stanly-2022.md) — §5.3.1, Fig. 15.
- [Mays et al. (2023)](/sources/mays-2023.md) — §1 and reference list.
