---
okf_version: "0.1"
---

# fusion-mhd-simulation — Knowledge Bundle

Numerical simulation of magnetically confined fusion plasmas with MHD,
extended-MHD and hybrid kinetic-MHD models: the nonlinear codes and their
discretizations, time integration and wall coupling; the physics modules
attached to them; disruptions, edge-localized modes, tearing, kink and
ballooning modes, energetic-particle-driven modes; stellarator MHD and 3D
equilibria; code-to-code benchmarks.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page (SI with $\mu_0$ explicit; $\psi$ per radian; $\gamma$ a
growth rate, $\Gamma$ the ratio of specific heats), and the
[update log](/log.md).

**Corpus:** all 50 of the archive's 50 files ingested. Chunk 1 (20): the
code, method, benchmark and review papers — two reviews of the JOREK code
([Hoelzl et al. 2021](/sources/hoelzl-2021.md), [Hoelzl et al. 2024](/sources/hoelzl-2024.md)),
a review of nonlinear energetic-particle code benchmarking
([Vlad et al. 2025](/sources/vlad-2025.md)) and seventeen code, method and
benchmark papers. Chunk 2 (20): application papers on disruptions and
shattered pellet injection, runaway electrons, tearing, kink and sawtooth
dynamics, ELM-free regimes and RMPs, energetic-particle modes and
stellarator β limits. Chunk 3 (10): SPI, MGI and runaway-electron
mitigation for AUG, SPARC and EU-DEMO, flux pumping, QH-mode and ELM
crashes, stellarator edge stability and kinetic ions in LHD, and two
neural-operator surrogates. Many files are preprints; each Source page
states the version read. The [bibliography](/bibliography.md) lists the
1552 works the 50 sources cite.

## Reading guide

1. **Models.** The [single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
   and its reductions: [reduced MHD for tokamaks](/methods/reduced-mhd.md)
   (ordering-based vs ansatz-based, what it cannot represent) and
   [for stellarators](/methods/stellarator-reduced-mhd.md) with the
   [Dommaschk vacuum field](/methods/dommaschk-potentials.md),
   [toroidal mode families](/definitions/toroidal-mode-family.md),
   [interchange modes and the Mercier criterion](/definitions/interchange-mode.md) and the
   [soft β limit](/definitions/soft-beta-limit.md), with the results on
   [kinetic ions in LHD](/results/kinetic-ions-prevent-core-collapse-lhd.md) and the
   [quasi-axisymmetric reactor edge](/results/stellarator-edge-instability-qa.md);
   the equilibrium code [HINT](/software/hint.md); the constraint
   [∇·B = 0](/properties/divergence-free-magnetic-field.md); initial states from the
   [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md) and
   [3D inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
   ([VMEC](/software/vmec.md), [DESC](/software/desc.md)).
2. **Discretization and time integration.**
   [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md),
   their [VMS stabilization](/methods/variational-multiscale-stabilization.md) and
   [shock capturing](/methods/shock-capturing-artificial-viscosity.md);
   [implicit time integration and preconditioned Krylov solvers](/methods/implicit-time-integration.md),
   the [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md),
   [operator splitting of atomic sources](/methods/operator-splitting-of-atomic-sources.md);
   finite differences in [field-aligned coordinates](/methods/field-aligned-coordinates.md)
   with the [hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md);
   [symbolic code generation](/methods/symbolic-code-generation.md) and
   [linear eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md).
3. **Walls and the free boundary.**
   [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
   ([STARWALL](/software/starwall.md), [CARIDDI](/software/cariddi.md)),
   [sheath boundary conditions](/methods/sheath-boundary-conditions.md).
4. **Codes.** [JOREK](/software/jorek.md) (and [JOREK3D](/software/jorek3d.md)),
   [M3D-C1](/software/m3d-c1.md), [NIMROD](/software/nimrod.md), [CLT](/software/clt.md),
   [BOUT++](/software/bout-plus-plus.md), [SCELT](/software/scelt.md), [M3D](/software/m3d.md),
   [CASTOR3D](/software/castor3d.md),
   [GMEC](/software/gmec.md).
5. **Disruptions.** [Disruption](/definitions/disruption.md) phases and the current spike;
   [thermal quench](/definitions/thermal-quench.md);
   [vertical displacement events](/definitions/vertical-displacement-event.md),
   [halo currents](/definitions/halo-current.md) and
   [wall forces](/definitions/wall-forces.md), with the results on the
   [reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md) and
   [vertical-force mitigation](/results/vertical-force-mitigation.md);
   [shattered pellet injection](/definitions/shattered-pellet-injection.md) and
   [massive gas injection](/definitions/massive-gas-injection.md) with
   [pellet ablation models](/methods/pellet-ablation-models.md),
   [plasmoid drift](/definitions/plasmoid-drift.md),
   [radiation asymmetry](/definitions/radiation-asymmetry.md) and the
   [electron temperature hole](/results/electron-temperature-hole.md);
   the [resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md) as a TQ trigger;
   [runaway electrons](/definitions/runaway-electrons.md) and their
   [fluid model](/methods/runaway-electron-fluid-model.md), its
   [advection by characteristics](/methods/runaway-electron-advection-by-characteristics.md),
   and [runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md),
   [runaway wall loads](/definitions/runaway-electron-wall-loads.md) and the
   [runaway mitigation coil](/definitions/runaway-electron-mitigation-coil.md).
6. **Physics modules.** Impurities in
   [coronal equilibrium](/methods/coronal-equilibrium-impurity-model.md) or
   [collisional-radiative](/methods/collisional-radiative-impurity-model.md) treatment;
   [fluid](/methods/fluid-neutral-models.md) and [kinetic](/methods/kinetic-neutral-model.md)
   neutrals, with the [high-field-side high-density region](/results/high-field-side-high-density-region.md);
   [particle-to-mesh projection](/methods/particle-to-mesh-projection.md);
   the [bootstrap current](/definitions/bootstrap-current.md) and
   [quasi-symmetry](/definitions/quasi-symmetry.md).
7. **MHD instabilities.** [Tearing mode](/definitions/tearing-mode.md),
   [neoclassical tearing mode](/definitions/neoclassical-tearing-mode.md) and the
   [modified Rutherford equation](/definitions/modified-rutherford-equation.md),
   [radiation-triggered tearing](/results/radiation-triggered-tearing.md),
   [double tearing mode](/definitions/double-tearing-mode.md),
   [resistive internal kink](/definitions/resistive-internal-kink.md),
   [sawtooth crash](/definitions/sawtooth-crash.md) and
   [flux pumping](/definitions/magnetic-flux-pumping.md) and the
   [MHD dynamo](/definitions/mhd-dynamo.md),
   [infernal mode](/definitions/infernal-mode.md),
   [ballooning mode](/definitions/ballooning-mode.md),
   [edge-localized modes and ELM-free regimes](/definitions/edge-localized-mode.md),
   [resonant magnetic perturbations](/definitions/resonant-magnetic-perturbation.md)
   ([MARS-F](/software/mars-f.md)), the
   [plasmoid instability](/definitions/plasmoid-instability.md), the
   [edge harmonic oscillation](/definitions/edge-harmonic-oscillation.md) and the
   [two-stage ELM crash](/results/two-stage-elm-crash.md).
8. **Energetic particles.** [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md),
   [pressure and current coupling](/methods/pressure-and-current-coupling.md),
   the [δf method](/methods/delta-f-method.md),
   [particle pushers](/methods/particle-pushers.md),
   [kinetic thermal ions](/methods/kinetic-thermal-ions.md), the
   [chirping phase-space diagnostic](/methods/chirping-phase-space-diagnostic.md); the modes
   [TAE](/definitions/toroidal-alfven-eigenmode.md), [RSAE](/definitions/reversed-shear-alfven-eigenmode.md),
   [EPM and chirping](/definitions/energetic-particle-mode.md), [fishbone](/definitions/fishbone.md);
   the codes [M3D-C1-K](/software/m3d-c1-k.md), [MEGA](/software/mega.md),
   [ORB5](/software/orb5.md), [HYMAGYC](/software/hymagyc.md), [XTOR-K](/software/xtor-k.md),
   [MIPS](/software/mips.md).
9. **Data-driven surrogates.** [Fourier neural operator surrogates](/methods/fourier-neural-operator-surrogates.md)
   trained on JOREK, NIMROD and GTC runs and on camera data, with their error growth and speed-up caveats.
10. **Benchmarks.** [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md),
   [CLT–M3D-C1 tearing and kink](/benchmarks/clt-m3d-c1-benchmark.md),
   [cbm18 ballooning](/benchmarks/cbm18-ballooning-benchmark.md),
   [DIII-D gas-injection impurity benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md),
   [ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md),
   [ITPA TAE](/benchmarks/itpa-tae-benchmark.md),
   [DIII-D RSAE](/benchmarks/diii-d-rsae-benchmark.md),
   [NLED-AUG](/benchmarks/nled-aug-benchmark.md).

**Open contradictions** are listed on the pages that hold them
(`## Contradictions` sections); the reviewer's digest is the bundle's
`INGESTION-ISSUES.md`.

## Catalog

* [Definitions](/definitions/index.md)
* [Methods](/methods/index.md)
* [Operators](/operators/index.md)
* [Results](/results/index.md)
* [Properties](/properties/index.md)
* [Benchmarks](/benchmarks/index.md)
* [Software](/software/index.md)
* [Sources](/sources/index.md)
