---
type: Source
title: "Zaghi (2026) — ADAM FLUME MHD kernels: the conservative magnetic flux and the EGLM sources"
description: "Frozen capture of three source files of the ADAM code's FLUME MHD solver: a conservative Maxwell-stress momentum flux, plain GLM with only a damping source, and EGLM, which adds the momentum source −(∇·B)B so that flux plus source give (∇×B)×B; implicit, hypothesis-grade evidence on the sign of the parallel force."
resource: "https://github.com/szaghi/adam (commit 4a3a0815aa364d53340b44779fb13bf796282ca2, branch develop)"
source_kind: code
authors: [Zaghi S.]
year: 2026
venue: "ADAM repository: FLUME source code"
local_file: "/home/stefano/llm-wiki/high-order-capturing-schemes/raw/docs/zaghi-2026/"
tags: [mhd, glm, divergence-cleaning, source-terms, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Three source files of FLUME, the MHD solver of the ADAM code (WENO finite
differences in flux-divergence form), captured verbatim at one commit. They
show how the code writes the momentum flux and which momentum source, if
any, each divergence-control model adds.

The record is the human's own code. Every claim compiled from it carries
`status: hypothesis`; it can neither promote a claim to `established` nor
close a `Contradictions` entry (bundle law, D12 amendment).

# Key claims

1. **Conservative momentum flux** (`adam_flume_mhd_library.F90`,
   `mhd_flux`, lines 438–466). The physical flux along the normal $\mathbf n$
   is printed as `(rho u_n, rho u u_n + p_t n - B B_n, (E + p_t) u_n - (u.B) B_n, B u_n - u B_n)`,
   with $p_t = p + \tfrac12\vert\mathbf B\vert^2$. The magnetic part of the
   momentum flux is the Maxwell stress, so the force it carries is the
   conservative force
   $\nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right)$.
2. **Plain GLM adds no momentum source**
   (`adam_flume_cpu_mhd_glm_kernels.F90`, `add_glm_damping`, lines 47–69):
   the only source is the damping of the cleaning scalar (mixed GLM, after
   Dedner et al. 2002). With this model any force along $\mathbf B$ carried
   by the conservative flux stays in the solution.
3. **EGLM adds the momentum source $-(\nabla\cdot\mathbf B)\,\mathbf B$**
   (`adam_flume_cpu_mhd_eglm_kernels.F90`, `add_eglm_sources`, lines 58–112,
   momentum line 102; the same vector in `eglm_source_vector`), citing
   Derigs et al. (2018) eqs. 3.16–3.18. The full source vector is printed as
   `-(div B) (0, B, u.B, u, 0) - (u.grad psi) (0, 0, psi, 0, 1)` in the order
   `(rho, rho u, E, B, psi)`, applied as a local residual in every
   Runge–Kutta stage, never in the fluxes; $\nabla\cdot\mathbf B$ is a centred
   difference of the WENO order.
4. **What flux plus source imply (compiler's reading, not stated in the
   code).** The EGLM momentum equation carries
   $\nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - (\nabla\cdot\mathbf B)\mathbf B = (\nabla\times\mathbf B)\times\mathbf B$,
   which has no component along $\mathbf B$. For the source to remove the
   parallel force, the conservative force must have the component
   $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$ along $\mathbf B$. The code
   never states the sign, and its comments do not discuss the parallel
   force.

# Tests

None in the captured files.

# Notation map

| Code symbol | Registry symbol | Note |
|---|---|---|
| `B`, `B_n` | $\mathbf B$, normal component | |
| `u` | $\mathbf v$ | velocity |
| `p_t` | $p + \tfrac12\vert\mathbf B\vert^2$ | total pressure, written out |
| `psi` | $\hat\psi_{\mathrm{GLM}}$ | GLM cleaning scalar (code's scaling not checked against the registry's) |
| `n` (in `p_t n`) | $\mathsf I$ row along $\mathbf n$ | identity tensor applied to the normal |

# Pages created or updated

* Created this Source page.
* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md) (a hypothesis-grade bullet in the Open `Contradictions` entry on the sign of the parallel force).

# Citations

1. `/home/stefano/llm-wiki/high-order-capturing-schemes/raw/docs/zaghi-2026/`.
   * **Version read.** Three files captured verbatim on 2026-10-13 with
     `git show 4a3a0815aa364d53340b44779fb13bf796282ca2:<path>` from the
     ADAM repository (branch develop, pushed); the working tree, which had
     uncommitted edits to two of these files, was not read for the capture.
     Files: `src/app/flume/cpu/adam_flume_cpu_mhd_eglm_kernels.F90`,
     `src/app/flume/cpu/adam_flume_cpu_mhd_glm_kernels.F90`,
     `src/app/flume/common/adam_flume_mhd_library.F90`
     (`CAPTURE.md` in the capture directory).
   * **Identity.** No DOI: a code repository, cited by URL and commit.
   * **How it was read.** The three captured files, read in full where
     cited; line numbers refer to the captured files.
   * **Reference list.** The code comments cite two works, Derigs et al.
     (2018) and Dedner et al. (2002); both merged. The bibliography also
     carries an entry for the record itself. Bibliography: 3185 entries.
