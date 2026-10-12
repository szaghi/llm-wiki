---
type: Source
title: "Skinner & Ostriker (2013) — A two-moment radiation hydrodynamics module in Athena using a time-explicit Godunov method"
description: "Describes Hyperion, a gray mixed-frame M1 radiation hydrodynamics module for Athena: explicit unsplit VL transport with an HLL solver using closed-form multidimensional M1 eigenvalues, radiation subcycled under a reduced speed of light bounded by c_hat >> v_max max(1, tau_max), and a local implicit quartic for the gas-radiation energy exchange; verified on nine tests."
resource: "doi:10.1088/0067-0049/206/2/21"
source_kind: paper
authors: [Skinner M.A., Ostriker E.C.]
year: 2013
venue: "Astrophys. J. Suppl. 206:21"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2013-ApJS-Skinner-1010880067-0049206221.pdf"
tags: [software, radiation, reduced-speed-of-light, riemann-solver, unsplit, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Hyperion is a gray two-moment radiation hydrodynamics module for
[Athena](/software/athena.md). It solves the mixed-frame moment equations,
keeping source terms to order $\beta\tau$ (velocity over light speed times
optical depth), closed with the local M1 tensor (§2). Gas and radiation
transport use Athena's explicit unsplit VL (MUSCL-Hancock) integrator with
piecewise-linear reconstruction; the radiation uses an HLL solver whose wave
speeds the paper gives in closed form for the multidimensional M1 system
(eq. 41). Gas and radiation are operator-split, and the radiation is
subcycled about $\hat c/v_{\max}$ times per gas step under a reduced speed
of light. The stiff energy exchange is integrated locally and implicitly as
a quartic in the gas internal energy (§3.4). The paper derives validity
criteria for the reduced speed of light and checks them with a linear-wave
analysis (§3.2, §4.3.4). Merged into [Athena](/software/athena.md),
[M1 radiation transport](/methods/m1-radiation-transport.md),
[reduced speed of light](/definitions/reduced-speed-of-light.md),
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md) and
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
The module shares its name with the unrelated Monte Carlo radiative transfer
code HYPERION, which this paper does not cite.

# Key claims

1. **Equations** (§2.1, eqs. 1, 8). Lab-frame Euler equations plus the
   frequency-integrated zeroth and first radiation moments in the mixed frame
   (comoving material coefficients). Gray, no scattering, one absorption
   opacity $\kappa$ for the Planck, energy and flux means. The reduced speed
   $\hat c$ multiplies only the radiation time derivatives; the true $c$
   stays in the sources and in the flux-to-energy ratio, so quasi-steady
   radiation fields do not depend on $\hat c$. For $\hat c \ne c$ total energy
   and momentum are **not** conserved; the conserved combinations are
   $E + (c/\hat c)E_{\mathrm r}$ and $\rho\mathbf v + \mathbf F_{\mathrm r}/(c\hat c)$.
   MHD terms "can be added" through Athena's constrained transport but are
   not exercised. Gravity enters only as a given $\Phi$.
2. **Regimes** (§2.2). Streaming ($\tau \ll 1$), static diffusion
   ($\beta\tau \ll 1$) and dynamic diffusion ($\beta\tau \gg 1$), with
   $\beta\tau \sim t_{\mathrm{diff}}/t_{\mathrm{flow}}$.
3. **M1 closure** (§2.3, eqs. 11–17).
   $\mathsf f_{\mathrm E} = \tfrac{1-\chi_{\mathrm E}}{2}\mathsf I + \tfrac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n}$,
   $\chi_{\mathrm E} = \frac{3+4f_{\mathrm r}^2}{5+2\sqrt{4-3f_{\mathrm r}^2}}$,
   mapping $f_{\mathrm r} \in [0,1]$ to $\chi_{\mathrm E} \in [1/3, 1]$; exact in
   the diffusion and streaming limits. Stated failures: the two-beam
   instability and distributed sources interacting in optically thin
   regions. The closure module can be replaced by a variable Eddington tensor
   from short characteristics (Davis et al. 2012).
4. **Splitting** (§3.1, eqs. 19–28). A non-stiff hyperbolic part with
   explicit sources, split into gas and radiation subsystems, and a stiff
   energy-exchange ODE. Formally first order in time; Strang splitting was
   "not found particularly advantageous". Splitting gas from radiation also
   breaks strict conservation of the combined energy and momentum.
5. **Time steps** (§3.1, eqs. 29–32). The gas step uses a
   radiation-modified sound speed (Krumholz et al. 2007),
   $\Delta t_{\mathrm{gas}} = \nu h/v_{\max}$, and the radiation step
   $\Delta t_{\mathrm{rad}} = \nu h/\hat c = \Delta t_{\mathrm{gas}}/R$, with
   $\nu$ "usually 0.4" for VL. $R$ varies because $\hat c$ is fixed and
   $v_{\max}$ is not.
6. **Algorithm** (§3.1, 7 steps). Implicit exchange over the gas step; gas
   Godunov step with first-order explicit sources using the radiation at
   $t^n$; about $R$ radiation Godunov substeps with second-order sources;
   second-order correction of the gas sources with the radiation at $t^{n+1}$
   (eq. 53).
7. **Reduced speed of light** (§3.2, eqs. 33–36). Newtonian limit:
   $\hat c \gg v_{\max}$; preserving the ordering of time scales in static
   diffusion: $\hat c \gg v_{\max}\tau_{\max}$; combined,
   $\hat c \gg v_{\max}\max\{1, \tau_{\max}\}$ (eq. 35), i.e.
   $R \gg \max\{1,\tau_{\max}\}$ (eq. 36). In practice $R \sim 10$ for
   optically thin problems and $10$–$100$ for $\tau_{\max} \sim 10$. Not
   viable in dynamic diffusion; "generally" practical for optical depths up
   to about 10 (§5).
8. **Radiation transport** (§3.3, eqs. 37–39). VL integrator (Stone &
   Gardiner 2009), piecewise-linear reconstruction, HLL solver with
   $S_R = \max\{\lambda^{\max}(u^-), \lambda^{\max}(u^+)\}$ and
   $S_L = \min\{\lambda^{\min}(u^-), \lambda^{\min}(u^+)\}$. HLL is chosen as
   robust and "positivity-preserving for one-dimensional problems", at the
   cost of dissipation. Reconstruction variables are not stated.
9. **Closed-form M1 eigenvalues** (§3.3, eq. 41), the paper's named
   contribution, generalizing Audit et al. (2002) to several dimensions,
   with $\mu = \hat{\mathbf x}\cdot\hat{\mathbf n}$:
   $$\frac{\lambda^{(1,3)}}{\hat c} = \frac{\mu f_{\mathrm r} \pm \left[\frac23\left(4-3f_{\mathrm r}^2-\sqrt{4-3f_{\mathrm r}^2}\right)+2\mu^2\left(2-f_{\mathrm r}^2-\sqrt{4-3f_{\mathrm r}^2}\right)\right]^{1/2}}{\sqrt{4-3f_{\mathrm r}^2}},\qquad \frac{\lambda^{(2)}}{\hat c} = \frac{\mu}{f_{\mathrm r}}\left(2-\sqrt{4-3f_{\mathrm r}^2}\right).$$
   As $f_{\mathrm r} \to 1$ all three tend to $\hat c\mu$ (shadowing); as
   $f_{\mathrm r} \to 0$, $\lambda^{(1,3)} \to \mp\hat c/\sqrt3$. The system is
   hyperbolic but not strictly; only $\lambda^{(1,3)}$ are used.
10. **Flux absorption** (§3.4, eq. 43). A direct θ-scheme, $\theta = 0.51$
    "in most cases" and $\theta = 1$ when stiff.
11. **Implicit energy exchange** (§3.4, eqs. 44–50). Conserving
    $\rho e + (c/\hat c)E_{\mathrm r}$, a θ-scheme reduces to a quartic in the
    new internal energy density, bracketed when its constant term is
    non-positive (guaranteed for $\theta = 1$ or from radiative equilibrium),
    solved by Newton–Raphson with bisection fallback, tolerance $10^{-10}$.
    The $\mathcal O(\beta\tau)$ terms are explicit and assumed never stiff,
    which confines the method to static diffusion.
12. **Gas integrator and parallelism** (§3.4, §5). Unsplit VL or CTU, 1D to
    3D, MPI. Uniform Cartesian grids only; no AMR, no scaling data, no
    threading or GPU.
13. **Linear-wave analysis** (§4.3.4, eqs. 87–93). Dispersion relations
    extended to $\hat c$. When radiation pressure is small, acoustic modes
    are unaffected if $\hat c$ exceeds the sound speed by more than
    $\max\{1, \tau_\lambda\}$. When radiation pressure dominates in the
    optically thick limit, the radiation-modified acoustic mode is always
    affected (eq. 91) and is correct only as $\hat c \to c$.

**Tests** (§4; $\theta = 0.51$ and no $\mathcal O(\beta\tau)$ terms unless
stated; radiation-only tests with $\hat c = c$):
shadow by a dense cloud ($280\times80$; sharp shadow without emission,
softer with it; flux-limited diffusion "fails immediately");
radiation linear waves inclined to the grid in 1D, 2D and 3D, "nearly
second-order" against a slope −2 line (Fig. 4; see
[linear wave convergence](/benchmarks/linear-wave-convergence.md));
non-equilibrium Marshak wave (Su & Olson 1996, $N = 128$);
radiatively inhibited accretion and driven wind (maximum relative errors
0.0098% and 0.070%, with $\hat c = 10v_{\max}$); advected radiation pulse
(errors below 6.6% with the $\mathcal O(\beta\tau)$ terms, below 7.7%
without, $\hat c = 100c_s$); radiation pressure tube (maximum relative error
$5.1\times10^{-6}$ in temperatures, $1.4\times10^{-5}$ in density);
RHD linear waves (phase speed and damping match the dispersion roots when
$\hat c/c_s \gtrsim \tau_\lambda$); sub-critical radiative shock (Lowrie &
Edwards 2008; errors 1.7%, 6.1%, 7.8% with M1 eigenvalues, 0.42%, 0.49%,
0.42% with eigenvalues fixed at $\mp\hat c/\sqrt3$); radiation-driven dusty
shell in a 3D octant at $128^3$ (errors grow from 3.1% / 7.0% to 8.5% / 23%
in mean radius and velocity as $\hat c/c_s$ falls from 860 to 215). A 1D
timing comparison with Enzo's implicit flux-limited diffusion (§4.2): the
Hyperion wall time scales as $\mathcal O(N)$, Enzo's is about constant in
$N$; the authors claim the crossover lies above most practical resolutions.

# Notation map

| Skinner & Ostriker (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P$, $E$ | $p$, $E$ | |
| $e$ | $\rho e$ | **collision:** the paper's $e$ is the internal energy density |
| $\mathcal E$, $\mathbf F$, $\mathbb P$, $\mathbb T$ | $E_{\mathrm r}$, $\mathbf F_{\mathrm r}$, $\mathsf P_{\mathrm r}$, $\mathsf f_{\mathrm E}$ | bold $\mathbf F$ is also reused for the numerical flux (§3.3) |
| $\chi$, $f$, $\hat{\mathbf n}$ | $\chi_{\mathrm E}$, $f_{\mathrm r}$, $\hat{\mathbf n}$ | $\chi$ is also a coordinate in the tests |
| $c$, $\hat c$ | $c$, $\hat c$ | |
| $\kappa_0$ | $\kappa$ | Planck, energy and flux means set equal |
| $\tau$, $\tau_{\max}$, $\tau_\lambda$ | $\tau_{\max}$, $\tau_\lambda$ | **collision:** unsubscripted $\tau$ is the Valencia energy |
| $\beta = v/c$ | words | collides with the shift $\beta^i$; also a wave angle (§4.1.2) |
| $\mathbf U$, $\mathbb F$, $\mathbf S$ | $u$, $\mathbf f(u)$, $s(u)$ | |
| $\lambda_{1,2,3}$ | $\lambda^{(p)}$ | |
| $\Delta x$, $K_0$ | $h$, $\nu$ | |
| $\Delta t_{\mathrm{gas}}$, $\Delta t_{\mathrm{rad}}$, $R$ | $\Delta t$, words | |
| $a_0$ | $c_s$ | |
| $\mu$ | words | direction cosine; also the mean particle mass (eq. 2) |
| $\alpha$, $\theta$, $a_{\mathrm R}$, $P_0$, $C$, $\hat C$ | words | test- or scheme-local |

# Pages created or updated

* Updated [Athena](/software/athena.md) (the Hyperion module).
* Created [M1 radiation transport](/methods/m1-radiation-transport.md),
  [Reduced speed of light](/definitions/reduced-speed-of-light.md).
* Updated [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Linear wave convergence](/benchmarks/linear-wave-convergence.md).
* Also cited on [Enzo (AMR code for cosmological and astrophysical fluid flow)](/software/enzo.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2013-ApJS-Skinner-1010880067-0049206221.pdf`.
   * **Version.** arXiv:1306.0010v1 (31 May 2013), 30 pages, emulateapj; the
     header date "November 27, 2024" is the LaTeX date of a re-render, not a
     revision. Not the typeset article. The abstract says the module "will be
     made freely available on the Web"; no URL, licence, language or version
     is printed.
   * **Identity.** doi:10.1088/0067-0049/206/2/21, checked on Crossref (title
     and authors match): Astrophys. J. Suppl. Ser. 206(2):21, online
     2013-06-03.
   * **How it was read.** Text extraction, all sections; eq. 56 checked on
     the rendered page. The dispersion relations (eqs. 88, 93) and eqs.
     54–55, 62–70 and 83–86 were read from the text layer (partly garbled);
     only parameters are recorded. No error tables are printed; figure
     values are not reproduced.
   * **Recorded as printed.** Algorithm step 2 (§3.1) and §3.4 say the
     energy exchange is computed on the gas step, but eqs. 47 and 49 are
     written with $\Delta t_{\mathrm{rad}}$. The timing benchmark range is
     $N = 16$ to 2048 in the text and $N = 32$ to 2048 in the Fig. 7 caption.
   * **Reference list:** 49 entries, equal to the Crossref reference count;
     no article titles printed (book titles for LeVeque 2002, Mihalas &
     Weibel-Mihalas 1999, Zel'dovich & Raizer 2002); two arXiv-only entries
     (Audit et al. 2002, Frank et al. 2012). Commerçon et al. (2011) is
     printed as A&A 529:35 and merged into `commercon-2011` (529:A35);
     `krumholz-2007-c` and `krumholz-2012-b` are distinguished by volume and
     page.
