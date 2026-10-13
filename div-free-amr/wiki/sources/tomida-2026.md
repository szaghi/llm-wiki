---
type: Source
title: "Tomida, Sadanari, Takasao & Iwasaki (2026) — Systematic comparison between constrained transport and mixed divergence cleaning methods for astrophysical MHD simulations"
description: "Same-code (Athena++) comparison of CT and Dedner GLM cleaning: a time-step-dependent cleaning speed and localized fields make GLM create spurious, non-solenoidal field (orders-of-magnitude false amplification in collapse runs); fixed parameters and the EGLM energy term help, CT remains more robust."
resource: "doi:10.3847/1538-4365/ae8785"
source_kind: paper
authors: [Tomida K., Sadanari K.E., Takasao S., Iwasaki K.]
year: 2026
venue: "Astrophys. J. Suppl. 285(2):64 (arXiv:2605.07928)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2026-ApJS-Tomida-1038471538-4365ae8785.pdf"
tags: [comparison, glm, constrained-transport, divergence-cleaning, eight-wave, amr, star-formation, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The authors add Dedner's mixed GLM cleaning to Athena++ next to its
Stone–Gardiner CT, so the two are compared on one base scheme: van Leer
integrator, PLM and HLLD. The tests are KH layers with uniform and with
localized weak fields, a time-step jump, a primordial collapsing cloud with
AMR, present-day protostellar collapse, and a 2D stratified convective
atmosphere. Appendices cover Powell's source terms and the EGLM energy
term.

The conclusion: GLM "can fail even with the optimal parameters". CT is
"less arbitrary, more robust and less prone to spurious behaviors". It is
merged mainly into [GLM cleaning](/methods/glm-divergence-cleaning.md),
and also into
[exact discrete divergence](/properties/exact-discrete-divergence.md),
[positivity–divergence coupling](/results/positivity-divergence-coupling.md)
and [eight-wave](/methods/eight-wave.md).

The PDF read is the arXiv v2 (July 2026). The published version, ApJS
285(2):64 (August 2026), was identified on Crossref. Pakmor et al. (2026)
cite the arXiv version.

# Key claims

1. **The derivation's hidden assumption** (§2.3). $\psi_h$ and the
   divergence obey the same equation only if the variables are smooth and
   the operator $\mathcal D$ commutes with time and space derivatives. The
   conventional $c_h \propto h_{\min}/\Delta t$ varies with the time step,
   which violates this. A spatially varying $c_h$, as in AMR with local
   steps, violates it in space.
2. **The dimensional damping constant** (§2.3.2). Dedner's $c_r = 0.18$
   has units. As a ratio of damping to crossing time at a scale $L$, the
   original choice is $L = 1$ in code units, while PLUTO-like codes use
   $L = h_{\min}$, which changes with AMR level.
3. **KH with a uniform weak field** (§3.1). CT is the least diffusive.
   GLM with $L = 1$ is consistent with it, while $L = h$ produces vertical
   field bumps that persist under refinement. A constant $c_h$ is unstable
   below about the maximum flow speed, about 1 here. Larger $c_h$ is more
   diffusive.
4. **Localized fields** (§3.2). GLM carries divergence error from the
   strong-field region into the weak-field one and creates non-solenoidal,
   resolution-inconsistent field there. CT keeps it confined.
5. **A time-step jump** (§3.3). With variable $c_h$, a sudden drop in
   $\Delta t$ amplifies $\psi_h$ about 40-fold within 10 steps, in
   proportion to the step ratio. When the step recovers, ripples dominate
   the weak-field region for more than 500 steps. CT and constant-$c_h$ GLM
   are unaffected.
6. **Applications** (§§3.4–3.6).
   * Primordial collapse: variable-$c_h$ GLM amplifies the field 3 to 5
     orders of magnitude beyond CT, with ripples that resemble those in
     Hirano & Machida (2022).
   * Present-day collapse: qualitatively similar, but outflow speeds differ
     by about a factor of 3.
   * Convective atmosphere: $\psi_h$-related energy flux at 1–100% of the
     Poynting flux in the stable layer, and spurious magnetization of the
     convective layer.
7. **Stability criterion** (§4.1). The scheme stayed stable with the
   Alfvén speed above $c_h$, but not with the flow speed above $c_h$. This
   is weaker than Pakmor et al.'s (2011) fastest-speed rule.
8. **Recommendations** (§§4–5).
   * Keep $L$, $c_p$ and $c_h$ fixed in space and time, with $L$ larger
     than the scale of interest and $c_h$ above any speed reached.
   * Include the EGLM energy term.
   * Before any change of $c_h$, "refresh": project out the divergence and
     reset $\psi_h$ to zero.
   * Published GLM-based amplification results should be re-examined.
9. **Appendices.**
   * A: Powell source terms in Athena++ let the divergence grow without
     crashing, and leave scaly artificial field.
   * B: on a low-$\beta$ CP Alfvén wave, CT and plain GLM both show about
     30% thermal-energy error in stripes. For CT the cause is the
     face-to-centre interpolation; for GLM it is the omitted $\psi_h$
     energy. EGLM, as a source term or in conservative form, gives a
     healthy, uniform heating.

# Notation map

| Tomida et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ | $\psi_h$ | |
| $c_h$, $c_p$ | $c_h$, $c_p$ | $c_r \equiv c_p^2/c_h$ (Dedner) |
| $L$, $C_r$ | damping scale and dimensionless ratio | $\tau_d = C_r L / c_h$ |
| D1v, Dhv, D1c, Dhc | GLM with $L = 1$ or $h$, variable or constant $c_h$ | model labels |
| face-centred $B$, edge EMFs | $B_h \in V_h^2$, $E_h \in V_h^1$ | CT |

# Pages created or updated

* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md): a section on the failure modes of the conventional implementation, with a compiler reading relating it to Pakmor et al. and to Balsara & Kim.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): where the "no difference" regime ends.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): CT's face-to-centre field as the low-$\beta$ weak point.
* Updated [Eight-wave formulation](/methods/eight-wave.md): Powell terms in the same-code comparison.

# Citations

1. `~/papers/mosaic/div-free-amr/2026-ApJS-Tomida-1038471538-4365ae8785.pdf` (doi:10.3847/1538-4365/ae8785; arXiv:2605.07928v2): text extraction, all pages including Appendices A–B and the reference list (63 entries). Figures were read from their captions and the text.
