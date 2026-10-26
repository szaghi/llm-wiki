---
type: Method
title: "Physics-informed neural networks for RANS"
description: "A neural network maps the coordinates to the mean velocity, pressure and Reynolds stresses and is trained on the RANS residuals plus boundary data; the RANS system is closed by data rather than by a turbulence model, with errors reported for boundary layers, an airfoil and the periodic hill."
status: established
aliases: [PINN, PINNs, physics-informed neural network, physics-informed RANS solver]
tags: [machine-learning, neural-network, data-driven, rans, boundary-layer]
timestamp: 2026-10-25T20:39:00Z
---

# Physics-informed neural networks for RANS

A **physics-informed neural network** (PINN) represents the solution of a
PDE by a neural network of the coordinates and trains its parameters
$\boldsymbol\theta$ on a loss that contains the PDE residuals, evaluated by
automatic differentiation, together with whatever data are available.
[Eivazi et al. (2022)](/sources/eivazi-2022.md) apply it to the
two-dimensional, incompressible, steady RANS equations. A fully connected
network maps $(x,y)$ to the six mean quantities $\langle u\rangle$,
$\langle v\rangle$, $\langle p\rangle$, $R_{11}$, $R_{12}$, $R_{22}$. The
RANS system has more unknowns than equations, and no turbulence model closes
it. The closure is supplied instead by data on the domain boundaries,
Reynolds stresses included, and by the residuals in the interior (Abstract,
§1–2). In every turbulent case the boundary data come from DNS or LES of
the flow being computed (§3), and the paper does not apply a trained network
to another flow.

## Formulation (Eivazi et al. 2022, §2, Fig. 1, Eq. 1)

With $\rho$ constant and $p$ the mean pressure, the residuals of the
momentum and continuity equations are, in registry notation,

$$\begin{aligned}
\mathcal E_1&=\langle u\rangle\partial_x\langle u\rangle+\langle v\rangle\partial_y\langle u\rangle+\rho^{-1}\partial_x\langle p\rangle-\nu\nabla^2\langle u\rangle+\partial_xR_{11}+\partial_yR_{12},\\
\mathcal E_2&=\langle u\rangle\partial_x\langle v\rangle+\langle v\rangle\partial_y\langle v\rangle+\rho^{-1}\partial_y\langle p\rangle-\nu\nabla^2\langle v\rangle+\partial_xR_{12}+\partial_yR_{22},\\
\mathcal E_3&=\partial_x\langle u\rangle+\partial_y\langle v\rangle,
\end{aligned}$$

where $\mathcal E_i$ (page-local) is the residual of equation $i$. The loss
is

$$\mathcal L=\mathcal L_e+\mathcal L_b,\qquad \mathcal L_e=\frac1{N_e}\sum_{i=1}^{3}\sum_{n=1}^{N_e}\lvert\mathcal E_i^n\rvert^2,\qquad \mathcal L_b=\frac1{N_b}\sum_{n=1}^{N_b}\lvert\boldsymbol Y_b^n-\boldsymbol Y_{\mathrm m,b}^n\rvert^2,$$

with $N_e$ residual points (interior collocation points plus boundary
points), $N_b$ boundary samples, $\boldsymbol Y_b^n$ the six reference
quantities at boundary point $n$ and $\boldsymbol Y_{\mathrm m,b}^n$ the
network's prediction there (page-local symbols; subscript $\mathrm m$ as in
the registry, the model's own output). The authors call $\mathcal L_b$ the
supervised and $\mathcal L_e$ the "unsupervised" loss. Weighting
coefficients between the two are possible, citing Jin et al. (2021), but
none is reported as used.

**Ingredients.**

- *Derivatives.* Reverse-mode automatic differentiation of the outputs with
  respect to the inputs (TensorFlow `GradientTape`).
- *Network.* Eight hidden layers of 20 neurons, $\tanh$ activations,
  stated for the laminar case and for the other cases as "similar" (§3).
- *Training.* Adam followed by BFGS, which stops on an increment tolerance.
- *Reynolds number.* It enters only through $\nu$ in the residuals (§1).
- *Not printed in the version read.* $N_e$, $N_b$, the collocation-point
  distribution, learning rates, epochs, training time and hardware.

**Variants per case (§3).** The laminar case solves the Navier–Stokes
equations without Reynolds stresses and is supervised by boundary velocity
only. The zero-pressure-gradient boundary layer solves continuity and
streamwise momentum, with outputs $\langle u\rangle$, $\langle v\rangle$,
$R_{12}$. The adverse-pressure-gradient case solves continuity and both
momentum equations. The airfoil and the hill use the full system with all
six outputs; on the hill, since velocity and stresses vanish on the walls,
data are needed only at the inlet and outlet, plus pressure on all
boundaries.

## Results

The error metric is the relative $\ell_2$ norm over all computational
points, in percent, $100\,\lVert\phi-\phi_{\mathrm m}\rVert_2/\lVert\phi\rVert_2$
for each variable $\phi$ (Eq. 2, Table 1).

| Case | Reference data | Error (%) |
|---|---|---|
| Laminar Falkner–Skan boundary layer, $Re=100$, exponent $m=-0.08$ ($\beta_{\mathrm{FS}}=2m/(m+1)=-0.1739$; separation at $-0.1988$) | analytical solution | $\langle u\rangle$ 0.07, $\langle v\rangle$ 0.12, $\langle p\rangle$ 0.001 |
| Zero-pressure-gradient [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md), $1000<Re_\theta<7000$ | DNS of Eitel-Amor et al. (2014) | $\langle u\rangle$ 1.02, $\langle v\rangle$ 4.25, $R_{12}$ 6.46 |
| Adverse-pressure-gradient boundary layer at Clauser parameter $\beta_C\simeq1$, $910<Re_\theta<3360$ | Bobke et al. (2017) | $\langle u\rangle$ 0.28, $\langle v\rangle$ 1.57, $\langle p\rangle$ 4.60, $R_{12}$ 7.96 |
| NACA4412 suction-side boundary layer, $Re_c=200{,}000$, $0.5<x/c<1$ | well-resolved spectral-element LES of Vinuesa et al. (2018) | $\langle u\rangle$ 1.56, $\langle v\rangle$ 2.17, $\langle p\rangle$ 7.30, $R_{11}$ 9.43, $R_{12}$ 11.36, $R_{22}$ 4.69 |
| [Periodic hill](/benchmarks/periodic-hill.md), $Re_h=2800$, $1<x/h<5$ | spectral-element DNS (not cited) | $\langle u\rangle$ 2.77, $\langle v\rangle$ 19.70, $\langle p\rangle$ 8.61, $R_{11}$ 28.18, $R_{12}$ 16.70, $R_{22}$ 20.24 |

Here $\beta_{\mathrm{FS}}$ is the Falkner–Skan pressure-gradient parameter
and $\beta_C=(\delta^*/\tau_w)\,\mathrm d p_\infty/\mathrm dx$ the Clauser
parameter, with $p_\infty$ the free-stream pressure (page-local; the paper
writes both with $\beta$, which the registry keeps for the field-inversion
correction). The airfoil inputs are wall-tangent and wall-normal
coordinates.

**Statements of the authors.**

- *Laminar case.* The pressure is recovered to 0.001% although no pressure
  data were supplied (§3, Fig. 2).
- *Boundary layers.* Shape factor, $C_f$ against $Re_\theta$, and
  inner-scaled profiles of $u^+$ and $R_{12}^+$ at three stations agree with
  the references ("excellent accuracy"). In the adverse-pressure-gradient
  case $R_{12}$ "coincide[s] with the reference data" although no turbulence
  model is used (§3, Figs. 3–4). The average errors are 3.91% and 3.60%
  for the two boundary layers (§4).
- *Airfoil.* Inner-scaled profiles of $u^+$ and of the three stresses at
  $x/c\simeq0.625$, 0.75 and 0.875 show "excellent agreement" (Fig. 5).
- *Hill.* The extent of the separated region and the reattachment point are
  "accurately predicted"; $\langle u\rangle$ profiles at five stations agree
  (Fig. 6). No reattachment length is printed.
- *Conclusion (§4).* For the airfoil and the hill the streamwise velocity
  error is below 3%, with "good accuracy even in the simulation of
  Reynolds-stress components".

## Place among data-driven closures

The PINN of Eivazi et al. learns no closure model: its inputs are the
coordinates, so the trained network represents the mean field of one flow,
and no map from flow features to stresses is learned (§2). The data it
uses are boundary values of the very quantities a closure would predict.
Two other routes of this bundle differ in what is inferred:

- [Field inversion](/methods/field-inversion-machine-learning.md) keeps a
  turbulence model and infers a spatial correction of it from data, then
  learns the correction as a function of local features so that it
  transfers to other flows.
- A [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
  learns the Reynolds-stress anisotropy as a function of local invariants of
  the mean flow, for use inside a RANS solver.

Eivazi et al. (2022) make neither comparison and do not discuss
generalization, uniqueness of the reconstruction or sensitivity to the
boundary data (§1–4). Their stated precedent is the direct simulation of
turbulence with PINNs by Jin et al. (2021), recalled as agreeing well with
DNS (§1). [Domingo & Vervisch (2023)](/sources/domingo-2023.md) (§7) name
physics-informed techniques that couple PDE solution and network training
as a coming perspective for combustion DNS, without a method.

## Qualifications

- **Data requirement.** The reconstruction of each turbulent case uses
  boundary values of the Reynolds stresses from DNS or LES of the same flow
  (§2–3). The paper's phrase "without any specific model or assumption for
  turbulence" (Abstract) describes the form of the closure, not an absence
  of turbulence data.
- **Accuracy on the hill.** The Reynolds-stress errors on the periodic hill
  are 16.7% to 28.2% and the wall-normal velocity error 19.7% (Table 1),
  against the paper's summary "good accuracy" for the stresses (§4). The
  hill subdomain $1<x/h<5$ is a part of the hill period. The hill reference
  DNS is described but not cited.
- **Version read.** The source page records arXiv v1 (six pages); the
  published version may differ. All numbers above are those of v1.
- **Printed slips.** Eq. 1b sums residuals over three equations, while the
  zero-pressure-gradient case solves two and the laminar case has no
  Reynolds stresses: Eq. 1 is the general form. The Fig. 4 caption labels a
  panel (d) that the figure, which has panels (a)–(c), does not contain;
  the text refers to Fig. 4(c).
- The convention of the Reynolds stresses in the version read (positive
  correlations $\overline{uv}$ on the left-hand side of momentum, kinematic)
  matches the registry $R_{ij}$; the paper writes the means as $U$, $V$,
  $P$.

# Citations

- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — arXiv v1: Abstract; §1 (underdetermined RANS, precedent); §2, Fig. 1, Eqs. 1–2 (network, residuals, loss, error metric); §3, Figs. 2–6, Table 1 (five cases); §4 (conclusions).
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §7 (physics-informed techniques as a perspective for combustion DNS).
