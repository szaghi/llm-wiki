---
type: Benchmark
title: "Shock–bubble interaction"
description: "A planar shock hitting a circular or spherical region of different density or material: the one-dimensional Euler analogue, the Mach 1.22 air–helium experiment of Haas and Sturtevant, stronger air–helium and air–hydrogen cases, gas bubbles in water or stiffened gas, and Baer–Nunziato and shallow-water variants; tests interface sharpness, robustness at material contrasts and the resolved roll-up."
status: established
aliases: [shock–bubble, shock-bubble interaction, shocked bubble, shock–helium bubble, Haas–Sturtevant experiment, shock-induced bubble collapse]
tags: [benchmark, multiphase, interface-capturing, central-scheme, finite-volume]
timestamp: 2026-10-22T12:00:00Z
---

# Shock–bubble interaction

A planar shock travels through a uniform medium and hits a circular
(in one dimension, an interval; in three, spherical) region whose
density, and in multiphase versions whose material, differs from its
surroundings. The waves refracted and reflected at the interface deform
the bubble and roll it up; the benchmark tests how sharply a scheme
keeps the interface, whether it survives the material contrast, and how
much of the roll-up it resolves. It is the one test of this family with
an experiment behind it: the Mach 1.22 air–helium case of Haas &
Sturtevant, against which two sources measure feature or interface
velocities; a third compares interface trajectories with a published
computation of the same case.
The sources use the geometry in four quite different settings.

Throughout, $\phi_k$ denotes the volume fraction of component $k$ and
$(\gamma_k,p_{\infty,k})$ its [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md)
constants (page-local symbols). States are listed in the variables the
source prints.

## Euler and two-material Euler versions

**One-dimensional analogue.** [Chertock et al. (2023)](/sources/chertock-2023.md)
Ex. 1 run, on $[-1,1]$ with $\gamma=1.4$, a left-moving shock at
$x=0.75$ hitting a heavy "bubble" of radius $0.25$ at the origin:

$$
(\rho,v,p)(x,0)=\begin{cases}
(13.1538,\ 0,\ 1), & \lvert x\rvert<0.25,\\
(1.3333,\ -0.3535,\ 1.5), & x>0.75,\\
(1,\ 0,\ 1), & \text{otherwise},
\end{cases}
$$

solid wall on the left, free boundary on the right, $t=3$,
$\Delta x=1/100$, reference on $\Delta x=1/2000$, after a work they
list as in preparation. Their [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
is "sharper and less oscillatory" than the earlier
[central-upwind scheme](/methods/central-upwind-scheme.md), which has
lower shock resolution and an oscillation at the contact (Fig. 5.1).

**Mach 1.22 air–helium (Haas & Sturtevant).** A Mach 1.22 shock in air
hits a helium bubble of diameter 5 cm. Five sources run it, in three
models:

| Source | Model and scheme | Setup as printed | Grid |
|---|---|---|---|
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.1 | five-equation model, FV-WENO5 + HLLC ([MFC](/software/mfc.md)) | spherical bubble, axisymmetric; grid, CFL, $\gamma$ deferred to an earlier MFC paper | not printed |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.6 | [five-equation model](/definitions/five-equation-model.md), unstructured CWENO5 + HLLC | $(\phi_1\rho_1,\phi_2\rho_2,v_1,v_2,p,\phi_1)$: pre-shock air $(0,1.204,0,0,101325,0)$, post-shock $(0,1.658,-114.49,0,159060,0)$, bubble $(0.158,0.061,0,0,101325,0.95)$, helium "contaminated by 28% air"; $\gamma=1.4$ (air), $1.66$ (helium); shock moving right to left | 2D mixed meshes $D_b/35$, $D_b/120$, $D_b/400$; 3D $D_b/50$; to $t=1000\,\mu$s |
| [Renac (2021)](/sources/renac-2021.md) §7.3 | [multicomponent Euler](/definitions/multicomponent-euler-equations.md), entropy-stable [DGSEM](/methods/dgsem.md), $N=3$ | $[0,6.5]\times[0,0.89]$ (unit = bubble diameter), shock at $x=4.5$ moving left, bubble at $(3.5,0)$, symmetry boundaries top and bottom; helium $\gamma=1.648$, $C_v=6.89$; air $\gamma=1.4$, $C_v=1.7857$; regularized initial interface | 238,673 unstructured elements |
| [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.8, 5.10 | multicomponent Euler, entropy-stable FD on an [adaptive moving mesh](/methods/adaptive-moving-mesh.md) | $[0,445]\times[-44.5,44.5]$, bubble radius 25 at $(225,0)$, shock at $x=275$ moving left (speed $-415.16$); helium with 28 % air; air $(1.225,0,0,101325)$, post-shock $(1.6861,-113.5243,0,159060)$; $\gamma=1.4$, $1.647$ | 2D: $800\times160$ moving vs $2400\times480$ uniform; 3D: $400\times80\times80$ moving vs $800\times160\times160$ uniform |
| [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 10 | sharp interface: level set, conservative A-WENO | non-dimensional; pre-shock air $(\rho,v_1,v_2,p)=(1,0,0,1)$, post-shock $(1.3764,0.394,0,1.5698)$ for $x<-1.2$, helium $\rho=0.138$, $\gamma=5/3$ inside the unit circle | $280\times240$ |

The post-shock pressure ratio $1.5698$ of Zheng et al. is that of a
Mach 1.22 shock in air, $1+\frac{2\gamma}{\gamma+1}(M^2-1)$ with
$\gamma=1.4$ *(compiler check, not in the sources)*, so all five run
the same shock strength; they differ in the helium contamination, the
air state and the non-dimensionalization.

**Mach 6 air–helium interaction.** [Huang et al. (2026)](/sources/huang-2026.md)
§6.12, Eqs. (6.11)–(6.12), after a cited multiphase work: in
$(\rho,v_1,v_2,p,\gamma)$, pre-shock air $(1,0,0,1,1.4)$, post-shock air
$(5.268,5.752,0,41.83,1.4)$, helium $(0.138,0,0,1,1.667)$; the helium
bubble is given by the level set
$-0.025+\sqrt{(x-0.15)^2+(y-0.0445)^2}$, a circle of radius $0.025$
about $(0.15,0.0445)$; the shock starts at $x=0.1$;
domain $[0,0.356]\times[0,0.089]$, walls top and bottom, inflow left
and outflow right; multi-resolution grid with $L_{\max}=3$ levels and
finest $1024\times256$; snapshots at $t=0.006$, $0.012$, $0.018$,
$0.024$. [ROUND and LD-ROUND](/methods/round-scheme.md) are comparable to
WENO5-JS; ROUND is slightly more dissipative at the two later times and
LD-ROUND develops more complex vortical structures than WENO5-JS
(Fig. 17). The test is presented as evidence of robustness in
multiphase flow.

**Mach 2 air–hydrogen.** Renac §7.5 runs a Mach 2 shock in air
(pre-shock $T=1000$ K, $p=1$ atm, $v_1=1240$ m/s) on a hydrogen bubble
of diameter 5.6 centred at $(4,0)$ in $[0,22.5]\times[0,7.5]$ (unit
1 mm); hydrogen $\gamma=1.41$, $C_v=7.424$, air $\gamma=1.353$,
$C_v=0.523$; 74,504 unstructured elements, $t$ up to $13.6\,\mu$s. The
results "compare well" with three earlier computations, and the case is
offered as evidence of robustness on unstructured meshes (Fig. 8).

## Gas bubbles in liquids and stiffened gases

The heavy medium is now a liquid (water) or a stiffened gas and the
bubble a light ideal gas: the shock collapses the bubble instead of
being refracted by it.

- **Gas bubble collapse in water.** Tsoutsanis et al. §4.4, after two
  earlier computations: a Mach 1.72 shock in water,
  $(\rho,v_1,v_2,p,\gamma,p_\infty,\phi_1)$ post-shock
  $(1323.65,681.058,0,1.9\times10^9,4.4,6\times10^8,0)$, pre-shock
  $(1000,0,0,10^5,4.4,6\times10^8,0)$, air bubble
  $(1,0,0,10^5,1.4,0,1)$ of diameter $D_b=6$ mm at the centre of
  $[0,0.024]^2$ m, shock at $x=0.0066$ m; about $10^6$ quadrilaterals,
  edge $\approx D_b/250$, CWENO5, $t=6.2\,\mu$s. Peak pressure 7.7 GPa
  and peak temperature about 15,670 K; the earlier computations report
  10.1 GPa at $D_b/800$ and 7.8 GPa at $D_b/300$, a spread the authors
  attribute to resolution (Figs. 6–8).
- **Underwater shock on a gas bubble.** Zheng et al. Ex. 11: pre-shock
  water $(\rho,v_1,v_2,p,\gamma,p_\infty)=(1000,0,0,1,7.15,3309)$,
  post-shock $(1176.3576,1.1692,0,9120,7.15,3309)$ for $x<-1.2$, gas
  $(1,0,0,1,1.4,0)$ in the unit circle; $280\times240$ cells; density at
  $t=0.06$, $0.19$, $0.357$, $0.471$, stopped before collapse (Fig. 15).
- **Ideal-gas bubble in a stiffened gas, Mach 10.** Li et al. Ex. 5.9
  and 5.11 (3D): bubble $(\rho_1,\rho_2,v_1,v_2,p)=(0.05,4.95,0,0,100)$
  in a stiffened gas $(0.95,0.05,0,0,100)$, post-shock
  $(1.930198,0.05,-121.2497,0,29800)$ (Li et al. write the trace
  partial density $0.05$ as a symbol and subtract it from the main one);
  stiffened gas $\gamma_1=3$, $p_{\infty,1}=100$, bubble gas
  $\gamma_2=1.4$; $t=0.8$ (2D), $0.64$ (3D).

[Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §6.1 show a
related illustration rather than a benchmark: a 40 MPa shock collapsing
a 20 µm air bubble inside a water-filled vessel in gelatin, with
qualitative claims only.

## Non-conservative multiphase and shallow-water versions

[Balsara et al. (2024)](/sources/balsara-2024.md) §IX use the geometry
for systems with non-conservative products, computed with their
[FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md):

- **Baer–Nunziato shock–bubble** (§IX.a, Table IX, Fig. 11; after
  Dumbser and co-workers): domain $[-0.5,3]\times[-0.75,0.75]$,
  $700\times300$ zones, CFL 0.4, $t=0.025$; phases with stiffened-gas
  parameters $(\gamma_1,p_{\infty,1})=(3,100)$ and $(\gamma_2,p_{\infty,2})=(1.4,0)$;
  bubble of radius $0.25$ at $(0.5,0)$ with solid volume fraction 0.25
  against 0.75 outside; shock at $x=0$, left state
  $(\rho_1,v_1,p_1,\rho_2,v_2,p_2,\phi_1)=(1999.939402,\ 49.998485,\ 4999849.5,\ 1,\ 0,\ 1,\ 0.75)$,
  right and bubble states $(1000,0,1,1,0,1,\phi_1)$; Dirichlet left and
  right, periodic top and bottom ($\phi_1$ is the solid volume
  fraction).
- **Two-layer shallow-water shock–"bubble"** (§IX.c, Fig. 13) and
  **debris-flow shock–"bubble"** (§IX.e, Fig. 15), both new: the
  "bubble" is a smooth depression of the bottom,
  $b(r)=-0.25+0.25\tanh\big((r-0.25)/(2\Delta x)\big)$ (debris flow:
  amplitude 0.5) centred at $(0.5,0)$, hit by a bore at $x=0$;
  $700\times300$ (debris flow $700\times500$) zones, CFL 0.4, $t=0.30$.

Fifth and seventh order resolve the structures "much more crisply" than
third order, and the authors present the shallow-water and debris-flow
cases as genuinely new multidimensional tests (§IX).

## Findings across sources

**Agreement with the Haas–Sturtevant experiment.** Bryngelson et al.
report that the simulated velocities of the incident, reflected and
transmitted shocks, of the upstream and downstream interfaces and of
the jets are within 10 % of the measured ones, and generally within
about 5 % of the experimental means, with no spurious oscillations in
numerical schlieren (§5.1, Fig. 1). Tsoutsanis et al. average three
interface velocities (m/s) and find all within the experimental
variation (Table 2):

| Interface velocity | 2D fine | 3D | WENO5 of Coralic & Colonius (as quoted) | Experiment |
|---|---|---|---|---|
| upstream | 181.242 | 178.402 | 173 | $170\pm17$ |
| jet | 237.086 | 228.375 | 230 | $230\pm23$ |
| downstream | 145.895 | 144.197 | 145 | $145\pm15$ |

Renac compares the space–time trajectories of three interface points
with the high-order computation of Kawai & Terashima, not with the
experiment, and finds "close agreement", without significant spurious
oscillations (Figs. 5–6). Bryngelson et al. and Tsoutsanis et al. thus
find their diffuse-interface schemes within the experimental scatter of
the measured kinematics; Renac's conservative multicomponent scheme
agrees with a reference computation.

**Resolution of the roll-up and symmetry.** In two dimensions the
Kelvin–Helmholtz roll-up of the interface sharpens with refinement from
$D_b/35$ to $D_b/400$, while the 3D mesh at $D_b/50$ does not capture it
(Tsoutsanis et al., Figs. 16–18). On the medium and fine unstructured
meshes the 2D solution loses its symmetry at late times, which the
authors attribute to the multidimensional reconstruction and the
arbitrary elements in the interaction zone; see
[symmetry preservation](/properties/symmetry-preservation.md).

**Cost of resolution.** Li et al. find their moving-mesh runs better
than, or comparable to, uniform-mesh runs with three times (2D) or
twice (3D) as many cells per direction, at 26.2 % (2D helium), 23.6 %
(2D stiffened), 29.2 % (3D helium) and 18.0 % (3D stiffened) of their
CPU time; per step the moving mesh costs roughly 4.3–7 times the
uniform mesh with the same cell count, as their Table 5.3 shows (e.g.
1h4m against 9m12s on $800\times160$).

**Sharp-interface start-up.** Zheng et al. first run the pure shock
until it settles into a "numerical shock" before it reaches the bubble,
to avoid the start-up error of a shock initialized as a discontinuity;
the main features are "correctly captured" with "high resolution", a
qualitative claim with no reference comparison (Figs. 13–15).

## Qualifications

- The settings share only the geometry; neither the equations nor the
  measures of success (interface sharpness in one dimension,
  interface kinematics against experiment, roll-up in two-material
  Euler, bubble collapse pressures in water, order comparisons for
  non-conservative systems) carry over between them.
- The Haas–Sturtevant setups differ in the helium state: Tsoutsanis et
  al. and Li et al. model the contamination with air (28 % air), while
  Renac and Zheng et al. use a single helium gas with their own
  constants ($\gamma=1.648$ and $5/3$). Interface-velocity agreement is
  therefore model-dependent within the experimental scatter.
- Balsara et al. print the post-shock two-layer state with labels
  "$h_{1L},u_{1L},v_{1L},h_{1R},u_{1R},v_{1R}$" for what are the left
  states of both layers.
- Tsoutsanis et al.'s quoted Coralic & Colonius velocities come from a
  different code and are reproduced here as quoted, not as read.
- Apart from the interface velocities of Tsoutsanis et al. and the
  feature velocities of Bryngelson et al., the evidence is from contour
  plots; no source reports an error norm.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.1, Ex. 1, Fig. 5.1 (arXiv v2).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.12, Eqs. (6.11)–(6.12), Fig. 17.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.a, §IX.c, §IX.e, Table IX, Figs. 11, 13, 15.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §5.1, Fig. 1; §6.1 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.4, Figs. 6–8; §4.6, Table 2, Figs. 15–18.
- [Renac (2021)](/sources/renac-2021.md) — §7.3, Figs. 5–6; §7.5, Fig. 8 (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.8–5.11, Table 5.3 (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 10–11, Figs. 13–15.
