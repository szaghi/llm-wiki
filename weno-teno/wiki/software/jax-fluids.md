---
type: Software
title: "JAX-Fluids"
description: "JAX-Fluids is an MIT-licensed Python/JAX Cartesian finite-volume solver for compressible single- and two-phase flows, fully differentiable by automatic differentiation: WENO and TENO reconstructions with Riemann solvers or characteristic flux splitting, a sharp-interface level-set method, single-GPU performance figures, and end-to-end training of a learned Rusanov dissipation."
status: established
aliases: [JAX-FLUIDS, JAXFLUIDS]
tags: [software, machine-learning, gpu, finite-volume, weno, multiphase]
timestamp: 2026-10-23T12:00:00Z
---

# JAX-Fluids

JAX-Fluids is a three-dimensional Cartesian finite-volume solver for the
compressible Euler and Navier–Stokes equations with sharp-interface
level-set two-phase (fluid–fluid and fluid–solid) capability, written
entirely in Python with JAX, so that the whole solver can be
differentiated by automatic differentiation and runs on CPUs, GPUs and
TPUs. Its purpose is machine-learning research in fluid dynamics:
end-to-end training of data-driven submodels, with gradients propagated
through whole simulation trajectories. The bundle's account is
[Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md); the version
read is the arXiv preprint (v1, March 2022), not the published CPC
article, and all locators below are those of the preprint. The code is
released under the MIT licence.

## Numerical method

**Finite volumes.** Cell averages $\bar u_i$ on Cartesian cuboids,
dimension by dimension, with face fluxes approximated by one-point
Gaussian quadrature at the face centre (§3.1, Eq. 9). Bezgin et al.
note that higher-order face quadrature is possible, citing Coralic &
Colonius.

**Two routes to the convective flux** (§3.3):

- *High-order Godunov.* WENO reconstruction of primitive or conservative
  variables, optionally in characteristic space, to $u^\pm_{i+1/2}$,
  then an approximate Riemann solver $h(u^-_{i+1/2},u^+_{i+1/2})$ (Eq. 10):
  Lax–Friedrichs, Rusanov, HLL, HLLC, the low-Mach HLLC-LM of
  Fleischmann et al., or AUSM+, with arithmetic, Davis, Einfeldt or Toro
  wave-speed estimates ([HLL-family solvers](/methods/hll-riemann-solvers.md),
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)). The default
  "HLLC setup" reconstructs primitive variables with WENO5-JS.
- *Characteristic flux splitting.* An interface state (arithmetic or
  [Roe](/methods/roe-riemann-solver.md) average), the eigen-decomposition
  $A_{i+1/2}=R_{i+1/2}\Lambda_{i+1/2}L_{i+1/2}$, characteristic states
  and fluxes $L_{i+1/2}u_j$, $L_{i+1/2}f(u_j)$ on the stencil, a split
  $\tfrac12(L_{i+1/2}f(u_j)\pm\bar\Lambda L_{i+1/2}u_j)$ with $\bar\Lambda$
  the eigenvalue matrix of the chosen splitting (componentwise local
  Lax–Friedrichs or Roe), WENO reconstruction of each split part, and
  back-projection by $R_{i+1/2}$ (seven steps). The "ROE setup" uses Roe
  splitting with WENO5-JS. This is the finite-difference-style
  [characteristic decomposition](/methods/characteristic-decomposition.md)
  applied inside a cell-average code with one-point face quadrature.

Bezgin et al. recall, after Qiu & Shu, that component-wise reconstruction
can oscillate where discontinuities of different fields interact, and
attribute the slight oscillations of the HLLC setup on the Sod and Lax
tubes to it (§3.3, §5.1.2, Figs. 9–10).

**Catalogue** (Table 2; all components recalled from the literature,
none with formulas printed):

| Component | Options |
|---|---|
| reconstruction | WENO1; WENO3-JS, -Z, -N, -F3+, -NN; WENO5-JS, -Z; WENO6-CU, -CUM; WENO7-JS, WENO9-JS; TENO5 |
| time integration | Euler, TVD-RK2, TVD-RK3 (Gottlieb–Shu) |
| viscous fluxes | 2nd- or 4th-order central differences |
| level-set advection | HOUC-3/5/7 |
| level-set reinitialization | first order (Russo–Smereka) or HJ-WENO |
| implicit LES | ALDM |
| equations of state | ideal gas, stiffened gas, Tait |

The reconstructions are those of [WENO-JS](/methods/weno-js-reconstruction.md),
[WENO-Z](/methods/weno-z.md), [WENO-CU6](/methods/weno-cu6.md),
[TENO](/methods/targeted-eno.md), and the WENO3-NN of
[Bezgin et al. (2022)](/sources/bezgin-2022.md)
([learned WENO weights](/methods/learned-weno-weights.md)). The default
equation of state is the [stiffened gas](/definitions/stiffened-gas-equation-of-state.md),
$p=(\gamma-1)\rho e-\gamma B$ with background pressure $B$ (page-local;
the registry's $p_\infty$), $B=0$ in the tests (§2, Eq. 3). The runs of
§5 use TVD-RK3 at CFL 0.9 ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

**Viscous fluxes.** Normal derivatives at the face by second- or
fourth-order central differences (Eq. 11); tangential derivatives at
cell centres (Eq. 12), then interpolated to the face (Eq. 13) (§3.4).

**Two-phase flows.** The conservative sharp-interface
[level-set method](/methods/level-set-method.md) of Hu et al. (2006):
each phase is integrated with volume-fraction-weighted cell averages,
aperture-weighted face fluxes and an interface flux from a linearized
two-material Riemann problem with surface tension; apertures and volume
fractions follow analytically from trilinearly interpolated corner
level-set values; small, new and vanished cut cells are mixed
conservatively with a threshold of 0.6 (§3.6, Eqs. 16–31). Immersed
solid walls use the same machinery with a prescribed interface velocity
([immersed boundaries](/methods/immersed-boundary-method.md)).

## Implementation and differentiability

The fields are arrays of shape $(5,N_x+2N_h,N_y+2N_h,N_z+2N_h)$ with
$N_h$ halo cells (page-local), and every operator is written by array
slicing (§4.1–4.2, Fig. 5). JAX's just-in-time compilation requires pure
functions and control flow on static arguments only, so element-wise
conditionals are masks (`jnp.where`), the classes pass `self` as static,
and the outer time loop is not compiled; only the time-step, integration
and forcing routines are (§4.3). A `feed_forward` method, with a fixed
number of steps and a fixed $\Delta t$, batched by `jax.vmap`, is
compilable and differentiable with `jax.grad`; the ordinary `simulate`
method is not (§4.5). Neural networks (Haiku, trained with Optax) can be
inserted in the reconstruction, the Riemann solver or the forcing.

## Validation

In Bezgin et al. (2023) §5:

- linear advection of a sine on 10 to 1000 points: orders 1, 2 and 5
  for WENO1, WENO3-JS and WENO5-JS, WENO3-JS dropping to second order at
  extrema (§5.1.1, Fig. 8);
- [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md) on 100
  cells at $t=0.2$ and $t=0.14$, and a two-phase air–helium tube on 200
  cells, with slight density oscillations at the interface because no
  isobaric fix is used (§5.1.2, §5.2.1);
- lid-driven cavity at $\mathrm{Re}=5000$ on $500^2$ (§5.1.3);
- [decaying compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
  (Spyropoulos–Blaisdell cases at turbulent Mach 0.2, 0.4, 0.6): HLLC on
  $128^3$ reproduces the DNS density fluctuation; on $32^3$ ALDM agrees
  with the DNS and plain HLLC does not (§5.1.4, Fig. 12);
- bow shocks in front of an immersed [cylinder](/benchmarks/flow-past-circular-cylinder.md)
  at Mach 3 and 20 on $480\times1280$ (§5.2.2);
- an oscillating drop (period 1.16336 against Rayleigh's 1.16943) and
  shear drop deformation against Taylor's law (§5.2.3–5.2.4);
- the Mach 1.22 [shock–helium-bubble interaction](/benchmarks/shock-bubble-interaction.md),
  in "very good quantitative agreement" with Terashima & Tryggvason's
  interface-point trajectories (§5.2.5, Figs. 17–18).

## Performance

On one NVIDIA RTX A6000 (48 GB), a [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at Mach 0.1 with TVD-RK3, mean wall time per cell and time step in
nanoseconds (§6, Table 3):

| Setup | $32^3$ | $64^3$ | $128^3$ | $256^3$ | $384^3$ |
|---|---|---|---|---|---|
| HLLC, float32 | 64.41 | 24.39 | 25.09 | 28.36 | 28.11 |
| HLLC, float64 | 98.20 | 93.94 | 92.55 | 92.76 | — |
| ROE, float32 | 241.71 | 302.20 | 304.55 | 301.78 | — |
| ROE, float64 | 703.40 | 746.78 | 759.36 | 760.09 | — |

Characteristic flux splitting costs about ten times HLLC because of the
eigen-decompositions, and single precision is 2.5–3 times faster than
double; at $384^3$ only HLLC in single precision fits in memory
(29.8 GB, Table 4). Memory is the main limit; adaptive multiresolution is
hard to reconcile with JAX's static compute graphs, and multi-GPU
parallelization is future work (§8).

## Learned numerical flux

Bezgin et al. (2023) §7 use the differentiability twice:

- **Gradient check.** The derivative of the integral entropy increase
  after five steps with respect to the shock Mach number, computed by
  automatic differentiation, agrees with central finite differences,
  whose error converges at second order, for one phase and for two
  phases through the whole level-set pipeline (§7.3, Fig. 19).
- **Rusanov-NN.** In the Rusanov flux
  $h=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac12a_{\mathrm{NN}}(u^+-u^-)$
  the wave speed is replaced by the output $a_{\mathrm{NN}}\ge0$
  (page-local) of a three-layer, 32-node multilayer perceptron of the
  velocity jump, mean velocity, mean sound speed and entropy jump, with
  an exponential output activation. It is trained end-to-end on 15-step
  unrolls of the first 1000 steps of a coarse-grained ($32\times32$)
  two-dimensional implosion and, over the full 2501 steps, is less
  dissipative than Rusanov, stays stable and has lower relative $L_1$
  errors in density and pressure, also beyond the training horizon
  (§7.4, Eqs. 48–50, Figs. 20–21). Only the scalar dissipation
  coefficient is learned, so the flux keeps the conservative Rusanov
  form (see [learned WENO weights](/methods/learned-weno-weights.md) for
  the offline-trained alternative and [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

## Qualifications

- The implosion of §7.4 puts $(\rho,v,p)=(0.14,0,0.125)$ inside
  $x+y\le0.15$ on $[0,1]^2$ (Eq. 49): density and pressure are swapped
  and the domain differs with respect to the Liska–Wendroff implosion
  recorded under [explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md).
  It is a training problem, not that benchmark.
- §6 quotes "around 25 μs per time step" for HLLC in single precision;
  Table 3 gives about 25 ns per cell and time step.
- Printed slips in the preprint: the second-order cell-centre difference
  of Eq. (12) has $\Delta y$ where $2\Delta y$ is required, and the face
  interpolants of Eq. (13) are centred at $x_i$ instead of $x_{i+1/2}$
  *(compiler check, not in the sources: by Taylor expansion)*; the
  bow-shock inflow $(1,\sqrt{1.4}\,M,0,1)$ is called a post-shock state
  but is the free stream (§5.2.2).
- The CFL definition behind CFL 0.9 is not stated ("as described in"
  another paper).
- The claimed reach of "roughly 400 million degrees of freedom" on one
  GPU (§8) is not among the measured cases; $384^3$ cells with five
  variables are $2.8\times10^8$ *(compiler check, not in the sources)*.

# Citations

- [Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) — §1; §2, Eq. (3); §3.1–3.6, Eqs. (9)–(31), Table 2; §4.1–4.5; §5.1–5.2, Figs. 8–18; §6, Tables 3–4; §7.3–7.4, Eqs. (44)–(50), Figs. 19–21; §8 (arXiv v1).
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — WENO3-NN, the learned reconstruction available in the code.
