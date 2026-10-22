---
type: Benchmark
title: "Shock–bubble interaction"
description: "A planar shock hitting a circular or spherical region of different density or material: one-dimensional analogues, the Mach 1.22 air–helium and air–R22 experiments of Haas and Sturtevant, stronger air–helium and air–hydrogen cases, gas bubbles in water or stiffened gas, a relativistic version, and Baer–Nunziato and shallow-water variants; tests interface sharpness, robustness at material contrasts and the resolved roll-up."
status: established
aliases: [shock–bubble, shock-bubble interaction, shocked bubble, shock–helium bubble, shock–R22 bubble, Haas–Sturtevant experiment, shock-induced bubble collapse]
tags: [benchmark, multiphase, interface-capturing, central-scheme, finite-volume]
timestamp: 2026-10-23T16:00:00Z
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
velocities; others compare interface trajectories or shadowgraph-like
contours with the experiment or with published computations of the same
case.
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

**One-dimensional two-material slabs.** [Bai & Li (2022)](/sources/bai-2022.md)
§3.1.3–3.1.4 run slab versions with two materials, as strips
$[-10,10]\times[0,1]$ m. Air–helium (after Quirk & Karni): post-shock air
$(\rho,v,p,T)=(1.6863\ \mathrm{kg/m^3},\ 113.515\ \mathrm{m/s},\ 1.5906\ \mathrm{bar},\ 328.54\ \mathrm K)$
for $x<-1.4$, a helium slab $[-1,1]$ ($0.223$ kg/m³, $\gamma=1.648$)
in air at 1.01 bar, $t=9.74$ ms. Water–gas: shocked water
$(1125.61\ \mathrm{kg/m^3},\ 220.87\ \mathrm{m/s},\ 0.4304\ \mathrm{GPa})$
($\gamma=4.4$, $p_\infty=6\times10^8$ Pa) for $x<-2.2$, a gas slab
$[-2,2]$ ($\gamma=2.4$) at 1.03 bar in water at rest, $t\approx8.27$ ms.
Their DG solution converges under refinement (25, 50, 100 elements/m)
to a finite-volume cut-cell reference; at equal element count degrees
1 and 3 beat degree 0 but look alike, and at equal degrees of freedom
the three agree up to slight differences, which the authors attribute
to the piecewise-constant structure of the solution (Figs. 10–13).

**Mach 1.22 air–helium (Haas & Sturtevant).** A Mach 1.22 shock in air
hits a helium bubble of diameter 5 cm. Ten sources run it, in four
models:

| Source | Model and scheme | Setup as printed | Grid |
|---|---|---|---|
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.1 | five-equation model, FV-WENO5 + HLLC ([MFC](/software/mfc.md)) | spherical bubble, axisymmetric; grid, CFL, $\gamma$ deferred to an earlier MFC paper | not printed |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.6 | [five-equation model](/definitions/five-equation-model.md), unstructured CWENO5 + HLLC | $(\phi_1\rho_1,\phi_2\rho_2,v_1,v_2,p,\phi_1)$: pre-shock air $(0,1.204,0,0,101325,0)$, post-shock $(0,1.658,-114.49,0,159060,0)$, bubble $(0.158,0.061,0,0,101325,0.95)$, helium "contaminated by 28% air"; $\gamma=1.4$ (air), $1.66$ (helium); shock moving right to left | 2D mixed meshes $D_b/35$, $D_b/120$, $D_b/400$; 3D $D_b/50$; to $t=1000\,\mu$s |
| [Renac (2021)](/sources/renac-2021.md) §7.3 | [multicomponent Euler](/definitions/multicomponent-euler-equations.md), entropy-stable [DGSEM](/methods/dgsem.md), $N=3$ | $[0,6.5]\times[0,0.89]$ (unit = bubble diameter), shock at $x=4.5$ moving left, bubble at $(3.5,0)$, symmetry boundaries top and bottom; helium $\gamma=1.648$, $C_v=6.89$; air $\gamma=1.4$, $C_v=1.7857$; regularized initial interface | 238,673 unstructured elements |
| [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.8, 5.10 | multicomponent Euler, entropy-stable FD on an [adaptive moving mesh](/methods/adaptive-moving-mesh.md) | $[0,445]\times[-44.5,44.5]$, bubble radius 25 at $(225,0)$, shock at $x=275$ moving left (speed $-415.16$); helium with 28 % air; air $(1.225,0,0,101325)$, post-shock $(1.6861,-113.5243,0,159060)$; $\gamma=1.4$, $1.647$ | 2D: $800\times160$ moving vs $2400\times480$ uniform; 3D: $400\times80\times80$ moving vs $800\times160\times160$ uniform |
| [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 10 | sharp interface: level set, conservative A-WENO | non-dimensional; pre-shock air $(\rho,v_1,v_2,p)=(1,0,0,1)$, post-shock $(1.3764,0.394,0,1.5698)$ for $x<-1.2$, helium $\rho=0.138$, $\gamma=5/3$ inside the unit circle | $280\times240$ |
| [Bai & Li (2022)](/sources/bai-2022.md) §3.4 | sharp interface: level set, ghost fluid and cut cells, DG of degree 2 with HLLC–HLL flux, adaptive quadtree | diameter 5 cm, upper half domain (symmetry); air $\rho=1.225$ kg/m³, $p=1.01325$ bar, $\gamma=1.4$; helium $\rho=0.2228$ kg/m³, $\gamma=1.648$ | background $720\times40$, two to four levels (AMR1–AMR4); to $983\,\mu$s |
| [Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) §5.2.5 | sharp interface: level set of Hu et al. in the finite-volume [JAX-Fluids](/software/jax-fluids.md); scheme settings not restated for this case | helium bubble of diameter 50 mm at the origin, shock 5 mm to its left, moving right; domain $[-90,266]\times[-44.5,44.5]$ mm; gas states not printed | not printed (arXiv v1) |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.16 | [five-equation model](/definitions/five-equation-model.md), finite-difference [gradient-based reconstruction](/methods/gradient-based-reconstruction.md) (MEG6, MIG4) and TENO5, HLLC | $(\rho,v_1,v_2,p,\gamma)$: post-shock air $(1.3764,-0.3336,0,1.5698/1.4,1.4)$, helium $(0.1819,0,0,1/1.4,1.648)$, pre-shock air $(1,0,0,1/1.4,1.4)$; $[0,6.5]\times[0,1.78]$ in diameters, bubble at $(3.5,0.89)$, shock at $x=4.5$ moving left; slip walls top and bottom; CFL 0.1 | $1300\times356$, $2600\times712$ (arXiv v2) |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.8 | two-species Euler with the double-flux method, six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) (WCNS-SA, WCNS-LD, ONL6) + HLLC | the same three states and geometry as Chamarthi, after Shankar et al.; zeroth-order extrapolation left and right, slip walls top and bottom, an artificial diffusion layer at the interface; CFL 0.5 | $\Delta x=D/150$ |
| [Nguyen et al. (2022)](/sources/nguyen-2022.md) §3.4 | multicomponent Euler in $p$–$T$ equilibrium, MUSCL with overbee limiter on volume fractions, HLLC | $325\times89$ mm; shock 25 mm from the bubble, moving right to left; pre-shock air $(\rho,p)=(1.4,10^5)$, post-shock $(1.92691,\ v_1=-114.42,\ 156{,}980)$; helium $\rho=0.25463$, $\gamma=1.648$ (SI values of their Table 3, whose column headers are misaligned with the rows) | $325\times90$, $650\times180$, $1300\times360$ (about 50, 100, 200 cells per diameter) |

The post-shock pressure ratio $1.5698$ of Zheng et al. is that of a
Mach 1.22 shock in air, $1+\frac{2\gamma}{\gamma+1}(M^2-1)$ with
$\gamma=1.4$ *(compiler check, not in the sources)*, and Tsoutsanis et al.'s and
Li et al.'s $159060/101325=1.5698$ is the same, so these sources run
the same shock strength; they differ in the helium contamination, the
air state and the non-dimensionalization. Nguyen et al.'s post-shock
ratios, $156{,}980/10^5=1.5698$ and $1.92691/1.4=1.3764$, are the same
*(compiler check, not in the sources)*; Bai & Li print the pre-shock
states only.

**Mach 1.22 air–R22.** Bai & Li §3.4 also run Haas & Sturtevant's
heavy-gas case: an R22 cylinder ($\rho=3.8635$ kg/m³, $\gamma=1.249$)
of the same diameter in the same air, background $1600\times80$ with
four levels, times 55–1020 µs. The pressure contours and the positions
of the interfaces and of the incident, refracted and transmitted shocks
"almost coincide" with a front-tracking computation of Ullah et al.;
the interface carries a richer vortex head, secondary vortex and jet,
which the authors attribute to higher resolution (Figs. 27–30).

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

**A strong shock on a light bubble across block interfaces.**
[Qin et al. (2023)](/sources/qin-2023.md) (§3.5.2, Eq. (41), Fig. 11) run a rightward strong shock with $(\rho,v_1,v_2,p)=(3.81,2.85,0,10)$ in $[-0.1,0]\times[-0.5,0.5]$. It
hits a light bubble $(0.1,0,0,1)$ of radius $0.2$ centred at $(0.3,0)$ in a gas $(1,0,0,1)$. The
domain is $[-0.1,1.6]\times[-0.5,0.5]$, with reflective walls top and bottom, a Dirichlet inlet and
supersonic outflow. It is split into four blocks of $270\times150$, $320\times150$, $270\times200$
and $320\times200$ points, with interfaces at $y=0$ and $x=0.8$. The test exercises their
[shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md) for a
multi-resolution WCNS. Contacts and small scales are "well resolved" at $t=0.2$ and $0.4$ across the
interfaces. The contours are not completely symmetric, because the grid spacing differs between
blocks.

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
  Bai & Li §3.5 run the same geometry (6 mm bubble, Mach 1.72 shock;
  water $\gamma=4.4$, $p_\infty=6\times10^8$ Pa) in a 12 mm square with
  post-shock water $(\rho,v_1,p)=(1322.47\ \mathrm{kg/m^3},\ 685.86\ \mathrm{m/s},\ 1.915\ \mathrm{GPa})$,
  four levels and 80 cells per diameter: the water jet forms at about
  $2.86\,\mu$s, hits the downstream bubble wall at about $3.053\,\mu$s
  and sends out a water-hammer shock at about $3.28\,\mu$s; the bubble
  height and width histories agree with Shukla's computation
  (Figs. 31–33). The two sources' post-shock states differ slightly
  ($1.9$ against $1.915$ GPa, $681.058$ against $685.86$ m/s).
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

## Relativistic version

[Duan & Tang (2022)](/sources/duan-2022.md) Ex. 6.9 run a
three-dimensional shock–bubble problem for
[special relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
with $\gamma=5/3$, after He & Tang: on $[0,325]\times[-45,45]^2$,
pre-shock $(\rho,v_1,v_2,v_3,p)=(1,0,0,0,0.05)$ for $x_1<265$,
post-shock $(1.865225080631180,\ -0.196781107378299,\ 0,\ 0,\ 0.15)$
for $x_1>265$, and a light bubble $(0.1358,0,0,0,0.05)$ in
$(x_1-215)^2+x_2^2+x_3^2\le25$; outputs at $t=90$ to $450$. Their
fifth-order entropy-stable scheme on an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) with
$325\times90\times90$ cells (2h14m44s) is comparable to the same scheme
on a uniform $650\times180\times180$ mesh (12h34m43s, so 17.8 % of the
CPU time), and gives sharper bubble interfaces than the second-order
moving-mesh scheme, "since the high-order accurate scheme has lower
dissipation" (Table 6.2).

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

Bai & Li compare the space–time diagrams of the upstream, downstream
and jet points of the helium bubble, which converge over their four
adaptive grids, and density contours, which agree with the Haas &
Sturtevant shadowgraphs and with two computations (Figs. 22–24). Their
earlier zero-order cut-cell mixing and a DG cut-cell method with cell
merging and a Lax–Friedrichs flux give an interface evolution
"obviously delayed at later stage", and the latter fails at
$983\,\mu$s because cell merging cannot follow the topology change
(Fig. 25); the upstream and jet curves of Terashima & Tryggvason's
front-tracking/ghost-fluid computation are delayed with respect to
theirs as well (Fig. 26). Nguyen et al. find their upstream, jet and
downstream interface positions nearly identical on three grids and in
good agreement with the same Terashima & Tryggvason computation, and
the wave patterns in agreement with the shadowgraphs (Figs. 18–19);
they pick overbee over superbee on interface thickness and smoothness
(Fig. 17). The two sources thus place Terashima & Tryggvason's curves
differently relative to their own; neither measures against the
experimental velocities.

[Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) (§5.2.5, Figs. 17–18) find their
upstream, jet and downstream interface points "in very good quantitative agreement" with the same
Terashima & Tryggvason computation. Their schlieren images agree qualitatively with the
Haas–Sturtevant images and with a computation by the ALPACA code.
Three sources thus compare with Terashima & Tryggvason: Nguyen et al. and Bezgin et al. agree with it,
and Bai & Li find it delayed.

**Interface thickness at fixed grid.** Two chunk-5 sources run the same non-dimensional setup and
compare schemes on one grid. Chamarthi (Ex. 4.16, Figs. 20–21) finds no noticeable spurious
oscillations with the author's gradient-based schemes, and a material interface thinner with MIG4 than with
MEG6 and TENO5. On $2600\times712$, more secondary instabilities appear at late times. Chamarthi states that
TENO "for the 5-equation model, is not presented in the open literature"
([targeted ENO](/methods/targeted-eno.md)). Zhou et al. (§5.8, Figs. 19–20) find that WCNS-SA and
WCNS-LD capture more small-scale structures along the bubble than ONL6. *(Compiler check, not in the
sources: in both, the post-shock to pre-shock pressure ratio is $1.5698$ and the density ratio
$1.3764$, the Mach 1.22 values noted above; the helium density $0.1819$ differs from Zheng et al.'s
$0.138$.)*

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

**Mass loss of a sharp interface.** Bai & Li delete isolated
structures smaller than half a cell, followed by reinitialization, and
record the resulting mass loss for helium and R22 at 180 and 360 cells
per diameter, which they call "weak" because deletion is rare (§2.5.3,
Fig. 6; see [level-set methods](/methods/level-set-method.md)).

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
- Qin et al.'s inflow state is not a Rankine–Hugoniot post-shock state of a $\gamma=1.4$ gas
  moving into $(1,0,0,1)$ *(compiler check, not in the sources: the mass and momentum jumps give
  shock speeds $3.86$ and $3.68$, and with the printed $\rho$ and $p$ a single shock would carry
  $v_1\approx2.58$, with $\gamma=1.4$, the value the paper fixes for its Euler tests in §3.4)*.
  The paper does not comment on the inflow state.
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
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.5.3, Fig. 6; §3.1.3–3.1.4, Figs. 10–13; §3.4, Table 4, Figs. 20–30; §3.5, Figs. 31–33.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.4, Table 3, Figs. 16–20.
- [Duan & Tang (2022)](/sources/duan-2022.md) — §6, Ex. 6.9, Table 6.2 (arXiv v1).
- [Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) — §5.2.5, Figs. 17–18 (arXiv v1).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.16, Figs. 20–21 (arXiv v2).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.8, Eq. (43), Figs. 19–20.
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.5.2, Eq. (41), Fig. 11.
