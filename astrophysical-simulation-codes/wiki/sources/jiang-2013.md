---
type: Source
title: "Jiang et al. (2013) — A New Way to Conserve Total Energy for Eulerian Hydrodynamic Simulations with Self-Gravity"
description: "Writes the self-gravity energy equation in conservative form with a gravitational energy flux built from the potential and its time derivative, discretizes it in Athena with an extra Poisson-type solve for the time derivative from the Riemann mass fluxes, and shows round-off total-energy conservation and second-order Jeans-wave convergence, against energy errors, symmetry loss and spurious rotation of a non-conservative energy source in Jeans and polytrope collapse."
resource: "doi:10.1016/j.newast.2012.08.002"
source_kind: paper
authors: [Jiang Y.-F., Belyaev M., Goodman J., Stone J.M.]
year: 2013
venue: "New Astron. 19:48–55"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2013-NewAstron-Jiang-101016jnewast201208002.pdf"
tags: [self-gravity, conservation, hydro, unsplit, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper writes the self-gravity energy equation in conservative form,
$\partial_t(E + \tfrac12\rho\phi) + \nabla\cdot[(E+P)\mathbf v + \mathbf F_g] = 0$, with
the gravitational energy flux
$\mathbf F_g = \frac{1}{8\pi G}(\phi\nabla\dot\phi - \dot\phi\nabla\phi) + \rho\mathbf v\phi$
(§2, eqs. 9–14), alongside the already-standard conservative momentum equation
with the gravitational stress tensor (eqs. 7–8). In
[Athena](/software/athena.md), $\dot\phi$ comes from a second Poisson-type solve
whose right-hand side is $-4\pi G\nabla\cdot(\rho\mathbf v)$ built from the Riemann
mass fluxes, and momentum and total energy are updated by face differences of
$\mathsf T_g$ and $\mathbf F_g$ evaluated with the time-averaged potential (§3,
eqs. 15–16). Total energy is conserved to round-off and the scheme is second
order on 1D and 2D Jeans waves (§4.1). A non-conservative energy source (with
the conservative momentum flux kept) gives fractional total-energy errors from
0.65 down to 0.03 in 2D Jeans collapse, roughly $O(1/N)$, with loss of symmetry
and spurious rotation; a 3D near-$\gamma = 4/3$ polytrope collapse loses
spherical symmetry and develops a central hole (§4.2). Cost: one extra Poisson
solve per step (§5). Merged into
[conservative self-gravity coupling](/methods/conservative-self-gravity.md),
[Athena](/software/athena.md) and [Jeans wave](/benchmarks/jeans-wave.md).

# Key claims

1. **Source-term form** (§1, eqs. 1–6). Momentum source $-\rho\nabla\phi$, energy
   source $-\rho\mathbf v\cdot\nabla\phi$, $E$ internal plus kinetic only;
   $E_{tot} \equiv E + \tfrac12\rho\phi$ is globally conserved for an isolated
   system. Momentum and energy "are usually not conserved to roundoff" in this
   form (asserted).
2. **Conservative momentum** (eqs. 7–8), with
   $\mathsf T_g = \frac{1}{4\pi G}(\nabla\phi\nabla\phi - \tfrac12(\nabla\phi)\cdot(\nabla\phi)\mathsf I)$,
   "already been implemented in many grid-based codes, such as Athena" (§1);
   not new here.
3. **Conservative energy — the contribution** (§2, eqs. 9–14). Eq. 9 requires
   eq. 11; with $\nabla^2\dot\phi = -4\pi G\nabla\cdot(\rho\mathbf v)$ (eq. 12) it
   becomes a divergence (eq. 13), giving eq. 14 for $\mathbf F_g$. $\mathbf F_g$
   must fall off faster than $r^{-2}$ for eq. 9 to imply global conservation. A
   similar flux "has been proposed by Pen (1998)". The flux is not unique
   (App. A). Derivation (continuum).
4. **Discretization** (§3, five steps added to Athena's CTU). (i) Poisson for
   $\phi^n$ (FFT, periodic); (ii) half-step gravitational acceleration added to
   the interface velocities in the predictor; (iii) after the Riemann fluxes,
   solve eq. 12 for $\dot\phi^{n+1/2}$ with the right-hand side built from "the
   density flux from the Riemann solvers at each interface", a cell-centred,
   time-averaged value; (iv) update density, solve for $\phi^{n+1}$, form
   $\mathsf T_g$ and $\mathbf F_g$ from $(\phi^n + \phi^{n+1})/2$ and
   $\dot\phi^{n+1/2}$, face potentials by spatial averaging; (v) update momentum
   and total energy by face differences (eqs. 15–16), the energy update also
   exchanging $\tfrac12(\rho\phi)^n - \tfrac12(\rho\phi)^{n+1}$ cell-locally. The
   face stencils for $\nabla\phi$, $\nabla\dot\phi$ and $\mathsf T_g$ are not
   given.
5. **Ordering.** The Poisson solve for $\phi^{n+1}$ sits after the continuity
   update and before the momentum and energy updates (§3 step iv). No
   gravity time-step constraint is stated; Courant number 0.8 in all runs
   (Table 1).
6. **Cost** (§5). One extra Poisson solve per step; "slowed down by almost a
   factor of two" if the Poisson solver dominates, "almost as efficient as the
   original method" with FFTs. Asserted, no timings.
7. **Conservation** (§§4.1.1, 4.1.2, 6; measured). Total energy conserved "to
   round-off error" in 1D, 2D (including a Mach-10 advected background) and
   3D; no numerical round-off level printed.
8. **Accuracy** (§4.1; measured). Second order in the relative L2 norm (eq. 18)
   for a stable Jeans wave ($\lambda = \lambda_J/2$) after one period: 1D error in
   $\Phi$ (Fig. 1), 2D error in $\rho$ (Fig. 2). The non-conservative algorithm is
   "essentially identical" on the stable 2D mode.
9. **Non-conservative energy error** (Table 2; measured). Fractional
   total-energy error from start to virialization, 2D unstable Jeans collapse:
   $\gamma = 5/3$: .65, .32, .18, .09, .05 (runs H–L, $22^2$ to $362^2$);
   $\gamma = 4/3$: .09, .05, .03 (M–O). "Roughly $O(1/N)$". In 1D the
   non-conservative algorithm conserves energy "to very high precision".
   The error accumulates where $\phi$ changes fastest (Fig. 3); attributed
   ("likely") to grid-misaligned wavevectors and filament collapse.
10. **Dynamical consequence** (Figs. 5–8; measured). Non-conservative 2D
    collapse loses symmetry and rotates from zero angular momentum; 3D
    $\gamma = 1.36$ polytrope: higher peak central density, non-spherical by
    $t = 460$, central hole by $t = 900$; the conservative run stays near
    periodic and spherical.
11. **Not always needed** (§6). For $\gamma = 5/3$ small polytrope oscillations
    both algorithms agree and the old one is "just as good"; recommended where
    small energy errors matter, e.g. radiation-dominated, $\gamma \approx 4/3$
    flows. Applicability to operator-split codes such as ZEUS asserted, not
    implemented.
12. **Non-uniqueness and Galilean covariance** (App. A, eqs. A1–A5). Gauge
    freedom in $(E_g, \mathbf F_g)$; the alternative
    $E_g = \rho\phi + \vert\nabla\phi\vert^2/(8\pi G)$,
    $\mathbf F_g = \rho\phi\mathbf v - \frac{1}{4\pi G}\dot\phi\nabla\phi$ (A1) is
    Galilean-covariant, the eq. 14 pair is not. The authors keep
    $E_g = \tfrac12\rho\phi$ for robustness: (A1)'s $E_g$ is non-negative in near
    vacuum, so small errors in $\vert\nabla\phi\vert^2/8\pi G$ could cause large
    errors in specific energies. A modified stress tensor $\tilde{\mathsf T}_g$
    (A4) gives covariance with $E_g = \tfrac12\rho\phi$.

**Tests** (§4; Athena, HLLC, Courant number 0.8, uniform cells, periodic, FFT
Poisson). 1D Jeans instability ($\lambda = 2\lambda_J$, $\delta\rho/\rho = 10^{-6}$):
linear growth follows the dispersion relation up to saturation. 1D
[Jeans wave](/benchmarks/jeans-wave.md) convergence ($\lambda = \lambda_J/2$, 32 to 512
cells per Jeans length, one period): second order in $\Phi$. 2D oblique Jeans
wave ($k_x/k_y = 1$, $23^2$ to $362^2$): second order in $\rho$. 2D Jeans collapse
($\lambda = 2\lambda_J$, density perturbation increased 2% at the box centre):
Table 2 errors for the non-conservative source, round-off for the
conservative one. 2D Mach-10 advected background ($91^2$): energy conserved. 3D
$n = 3$ polytrope ($\gamma = 1.36$, $256^3$, central pressure reduced to 0.93 of
equilibrium): see claim 10. 3D $\gamma = 5/3$ small oscillations: both algorithms
"very similar" (no figure).

# Notation map

| Jiang et al. (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ (eqs. 1–16), $\Phi$ (eqs. 18–19, figures) | $\Phi$ | the paper uses both |
| $\dot\phi$ | $\partial_t\Phi$ | |
| $P$, $p$ (App. A) | $p$ | |
| $\rho$, $\mathbf v$, $G$, $\gamma$, $c_s$ | $\rho$, $\mathbf v$, $G$, $\gamma$, $c_s$ | $c_s^2 = \gamma P/\rho$ |
| $E$ | $E$ | internal plus kinetic; excludes potential energy |
| $E_{tot} = E + \tfrac12\rho\phi$; $E_g$ (App. A) | $E + E_{\mathrm g}$; $E_{\mathrm g}$ | |
| $\mathbf T_g$; $\tilde{\mathbf T}_g$ | $\mathsf T_{\mathbf g}$; words | identical definition; (A4) variant in words |
| $\mathbf F_g$ | none (words: gravitational energy flux) | distinct from $\mathbf F_{\mathrm r}$ |
| $\mathbf I$ | $\mathsf I$ | |
| $\delta t$; $\delta x$, $\delta y$, $\delta z$ | $\Delta t$; $h$ | |
| $n$ (time level); $n$ (polytropic index, §4.2) | $t^n$; words | **collision** within the paper |
| $\lambda_J$, $k_J$, $k$, $\omega$ | none (words) | Jeans length and wavenumber, wavenumber, angular frequency |
| $u$ (App. A) | $\rho e$ | **collision:** registry $u$ is the conserved state |
| $\mathbf j$, $\mathbf T$ (App. A) | $\rho\mathbf v$, $\rho\mathbf v\mathbf v + p\mathsf I$ | |
| $\epsilon$ (eq. 18 and eq. 22); $M$ (eq. 21) vs $M_0$ (Table 1) | none (local) | paper reuses $\epsilon$; $M$ is a mass, $M_0$ a Mach number |
| $\mathbf a$, $\mathbf b$ (App. A) | none (local) | gauge fields |

# Pages created or updated

* Updated [Conservative self-gravity coupling](/methods/conservative-self-gravity.md),
  [Athena (astrophysical MHD code)](/software/athena.md),
  [Jeans wave](/benchmarks/jeans-wave.md).
* Also cited on [Self-gravitating polytrope](/benchmarks/self-gravitating-polytrope.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2013-NewAstron-Jiang-101016jnewast201208002.pdf`.
   * **Version.** arXiv:1208.1795v2 (1 Oct 2012; page header "August 8th,
     2012"), AAS LaTeX preprint, 19 pages; not the typeset New Astronomy
     article. Section and equation numbers are the preprint's. Host code
     Athena (Stone et al. 2008), no version; hydrodynamics only (§3 asserts the
     gravity implementation is unchanged by MHD, untested).
   * **Identity.** doi:10.1016/j.newast.2012.08.002, checked on Crossref:
     title as on page 1, authors Jiang, Belyaev, Goodman, Stone, New Astron.
     19:48–55, issued 2013-02 (no issue number on Crossref).
   * **How it was read.** Text extraction, all sections; the derivation of
     eqs. 10–13 and (A1) checked line by line. Fig. 1–2 values read from log
     plots only (approximate); Figs. 4–7 are density images, captions used.
   * **Recorded as printed.** App. A refers to "equation (13) for
     $\mathbf F_g$" where eq. 14 is meant. Fig. 5's time "t = 1.1" has no units
     and does not match the $(k_Jc_s)^{-1}$ scale of Figs. 3–4. §4.1.2 says
     "three snapshots" for Fig. 4 but lists and shows four. Run G (512/1024) is
     in Table 1 but not named in the Fig. 1 caption.
   * **Reference list:** 12 printed entries (AAS style, no titles, no DOIs).
     Stone & Norman 1992 (ApJS 80:753) must resolve to the bundle's existing
     `stone-1992-c`, not `stone-1992` (ApJ 388:415). Edgar et al. 2005 printed
     "in Protostars and Planets V, 8005" (abstract number, kept in a note).
     Binney & Tremaine 2008 printed with "ed. Binney, J. & Tremaine, S."
     (editors omitted).
