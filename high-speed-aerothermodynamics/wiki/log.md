# Directory Update Log

## 2026-10-15

* **Human ruling (2026-10-15):** the cited work Voland, Huebner & McClinton,
  *X-43A hypersonic vehicle technology development*, Acta Astronaut. 59:181, is
  re-keyed `voland-2005` → `voland-2006`: Crossref
  (doi:10.1016/j.actaastro.2006.02.021) gives print July 2006; citing works that
  print 2005 give the year of the IAC-05 conference version, a distinct work.
  No concept page cited the key.

## 2026-10-14

* **Scaffolding and founding ingestion** (D23): the bundle's papers, filed in the
  plasma-propulsion archive and copied here, read by one reader agent each
  (page 1 checked against the filename), drafted from the notes, audited
  read-only before staging and fixed (overstated factors and citations
  corrected, status labels returned to claim-kind, one page split into inward-turning intake design and shape-transition isolator design).
  * **Notation registry seeded** ([notation](/notation.md)), sections 1–6: flow variables, dimensionless groups ($\mathrm{St}$ with word subscripts), boundary layers and shocks ($\beta_s$, $\theta_w$, $\sigma_0$), coordinates and numerics, configuration and performance quantities ($\alpha$, $J$, $d_j$, $p_b$, $\varphi$, $\mathrm{CR}$, $\eta_V$, $Q$, $\mathrm{Kn}$, $\beta_B$, $ZT$), uncertainty quantification ($\boldsymbol\xi$, $\Psi_k$, Sobol' indices); station subscripts $\infty$, 1, 2, $\max$, ref, $j$.
  * **Definitions (5):** [Inlet start, unstart and hysteresis](/definitions/inlet-start-and-unstart.md), [Isolator and shock train](/definitions/isolator-shock-train.md), [Transverse jet in supersonic crossflow](/definitions/jet-in-supersonic-crossflow.md), [Shock-wave/boundary-layer interaction](/definitions/shock-wave-boundary-layer-interaction.md), [Waverider](/definitions/waverider.md).
  * **Methods (9):** [Aeroheating reduction by spikes and coolant jets](/methods/aeroheating-reduction-spikes-and-jets.md), [Boundary-layer bleed for intake control](/methods/boundary-layer-bleed.md), [Inward-turning intake design](/methods/inward-turning-intake-design.md), [Non-intrusive polynomial chaos and Sobol' indices](/methods/non-intrusive-polynomial-chaos.md), [Osculating-cone waverider design](/methods/osculating-cone-waverider-design.md), [Re-entry capsule aerodynamics across flow regimes](/methods/reentry-capsule-aerodynamics-across-regimes.md), [Shape-transition isolator design](/methods/shape-transition-isolator-design.md), [SST k–ω turbulence model in high-speed flow](/methods/sst-k-omega-model.md), [Fuel-cooled thermoelectric generators for hypersonic vehicles](/methods/thermoelectric-generator-for-hypersonic-vehicles.md).
  * **Results (1):** [Peak heating of transitional shock/boundary-layer interactions](/results/transitional-swbli-peak-heating.md).
  * **Sources (10):** [Cheng et al. (2018) — Performance evaluation and comparison of electricity generation systems based on single- and two-stage thermoelectric generator for hypersonic vehicles](/sources/cheng-2018.md), [Fedele & Mungiguerra (2018) — Aerodynamics and flight mechanics activities for a suborbital flight test of a deployable heat shield capsule](/sources/fedele-2018.md), [Knight & Mortazavi (2018) — Hypersonic shock wave transitional boundary layer interactions - A review](/sources/knight-2018.md), [Liu Y. et al. (2018) — Structures of near-wall wakes subjected to a sonic jet in a supersonic crossflow](/sources/liu-2018-c.md), [Liu H. et al. (2018) — Uncertainty and sensitivity analysis of flow parameters on aerodynamics of a hypersonic inlet](/sources/liu-2018-d.md), [Meng et al. (2018) — Parameterization and optimization for shape-transition curved isolator](/sources/meng-2018.md), [Moradi et al. (2018) — The influence of coolant jet direction on heat reduction on the nose cone with Aerodome at supersonic flow](/sources/moradi-2018.md), [Wang et al. (2018) — Design methodology of the waverider with a controllable planar shape](/sources/wang-2018-d.md), [Zhao et al. (2018) — Design and high speed aerodynamic performance analysis of vortex lift waverider with a wide-speed range](/sources/zhao-2018.md), [Zuo & Huang (2018) — Numerical investigation of bleeding control method on section-controllable wavecatcher intakes](/sources/zuo-2018.md).
  * **Contradictions:** none opened; the cross-source differences examined are
    qualifications, recorded in prose on the pages and in the bundle's
    `INGESTION-ISSUES.md`.
  * **Bibliography:** [bibliography](/bibliography.md) created from the reference
    lists with `tools/bib_merge.py` (FLAGS 0, `--dupes` clean).
