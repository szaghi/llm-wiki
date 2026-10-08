# Benchmarks

Standard test problems.

* [Composite-profile linear advection (Jiang–Shu test)](/benchmarks/composite-advection-profile.md) — Linear advection on a periodic domain of a combination of narrow Gaussians, a square wave, a sharp triangle and a half-ellipse: separates smooth-but-sharp peaks from true discontinuities, and exposes extremum clipping and phase error over long times.
* [Double Mach reflection](/benchmarks/double-mach-reflection.md) — A Mach 10 shock hitting a 30° wedge (posed as a 60° shock on a flat wall): two Mach stems, a wall jet and slip-line roll-up; the standard 2D robustness and resolution test.
* [Lax shock tube](/benchmarks/lax-shock-tube.md) — The 1D Riemann problem (0.445, 0.698, 3.528 | 0.5, 0, 0.571), with a strong contact and an intermediate state that must be built up; a hard test for component-wise high-order schemes.
* [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md) — Woodward–Colella Mach 3 inflow over a step (0.2 high at x = 0.6 in a [0,3]×[0,1] tunnel): reflected shocks, a Mach stem and a vortex sheet from it, plus a corner singularity.
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) — A small isentropic vortex convected through a stationary Mach 1.1 shock: tests capture of weak acoustic and vortical structure crossing a shock, grid-aligned or oblique.
* [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md) — A Mach 3 shock running into a sinusoidal density (entropy) field: smooth structure behind a shock, where high-order capturing schemes show their largest advantage over TVD schemes.
* [Sod shock tube](/benchmarks/sod-shock-tube.md) — The 1D Riemann problem (1, 0, 1 | 0.125, 0, 0.1): rarefaction, contact and shock with a monotone density profile; the baseline check of shock, contact and rarefaction resolution.
* [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md) — Two strong blast waves between reflecting walls that collide (pressures 1000, 0.01, 100; t = 0.038): tests robustness, positivity and contact resolution in a confined, strongly interacting flow.
