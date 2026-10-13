---
type: Method
title: "Eight-wave formulation"
description: "Powell's non-conservative source-term formulation: advects divergence errors with the flow, holding the constraint to truncation error only."
status: established
aliases: [Powell source terms, 8-wave]
tags: [eight-wave, source-terms, divergence-constraint, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Eight-wave formulation

Powell's modification of the conservative MHD system
([Powell et al. (1999)](/sources/powell-1999.md)): the equations are solved
in their **symmetrizable form** — Godunov's result that pure divergence form
is not symmetrizable, and becomes so exactly when a multiple of
$\nabla\cdot\mathbf{B}$ is added to each equation. The added source terms
(momentum, induction, energy rows) give the Roe-type Riemann solver an
eighth wave: the *divergence wave*, advecting at the flow speed $u$.

**The primary report (1994).** The scheme first appeared in
[Powell (1994)](/sources/powell-1994.md), an ICASE report, by a different
route. In primitive variables the multi-dimensional system has a singular
flux Jacobian: the row of the normal field is zero, giving a zero
eigenvalue that Powell calls "clearly non-physical" (§2, eq. 8). He
replaces the Jacobian by a non-singular $8\times8$ matrix found "with
Maple" from four criteria: the seven 1D eigenpairs unchanged, an eighth
eigenvalue equal to $u$, sensible eighth eigenvectors, and reduction to the
seven-wave problem when the normal field is constant (eq. 9). The eighth
wave, which Powell names the "divergence wave", has speed $u$ and carries
only the jump of the normal field; the other seven carry none (eqs.
10–13). In conservative variables the modification is the source term
$$-(0,\ \mathbf B,\ \mathbf u,\ \mathbf u\cdot\mathbf B)^T\,\nabla\cdot\mathbf B$$
(eq. 14): zero on the mass row, nonzero on the momentum, induction and
total-energy rows. It
removes exactly the terms proportional to $\nabla\cdot\mathbf B$ hidden in
the conservative system (eq. 15), and turns $\partial_t(\nabla\cdot\mathbf
B) = 0$ into the passive-scalar law below (eqs. 16–17), "clearly the more
numerically stable of the two"; no stability proof is given. The solver is
first-order Roe-type with an arithmetic-average interface state, and the
source "is calculated in each cell, and added to the residual" with no
discrete divergence formula printed (p. 8). Powell's motivation is the
discrete constraint itself: the face-flux divergence
$D_h^{\mathrm f}B_h = 0$ allows a jump of the normal field across one face
if the other faces balance it (§1, eq. 5).
*Correction of scope:* the 1994 report contains no symmetrizability
argument, no Godunov citation, no Galilean invariance and no entropy law.
The attributions of these properties on this page are to
[Powell et al. (1999)](/sources/powell-1999.md) and stand; none of them
belongs to the 1994 report. Its own statement of the conservation trade is
weaker: "the deviations from conservation will be very small" (p. 6).

**Lineage: Brackbill & Barnes.** Powell (1994, pp. 6–7) presents the
source term as explaining an earlier observation, that "solving the
momentum equation in non-conservative form can remove instabilities
related to non-zero $\nabla\cdot\mathbf B$"
([Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md)). Brackbill
& Barnes put only the momentum equation in nonconservative form
(force $-\mathbf B\times(\nabla\times\mathbf B)$) and keep the induction and
energy equations conservative; momentum is then
conserved only to truncation error. They scope the risk to shocks:
conservation form "may be imperative only for high-speed flows where
Rankine–Hugoniot conditions across shocks would not be satisfied
otherwise" (p. 427).
*Compiler reading:* their nonconservative momentum equation is the
conservative one minus $\mathbf B\,(\nabla\cdot\mathbf B)$, the momentum row
of the eight-wave source. Brackbill & Barnes never write it as a source
term.

## The analytical mechanism

With the source terms,
$$\partial_t(\nabla\cdot\mathbf{B}) + \nabla\cdot(\mathbf{u}\,\nabla\cdot\mathbf{B}) = 0,$$
i.e. $\nabla\cdot\mathbf{B}/\rho$ is a passively convected scalar: clean
initial and boundary data stay clean along particle paths, to truncation
error. Divergence errors are not eliminated but *advected with the flow*,
preventing local accumulation. What the symmetrizable form buys: Galilean
invariance, an entropy conservation law, and no zero eigenvalue in the flux
Jacobian — none of which the unmodified conservative system has. Known
ambiguity, acknowledged in the primary source: isolated recirculating
regions cut off from boundaries. Discretely, the cell source uses the
face-integral divergence
$\frac{1}{V_i}\sum_{\text{faces}} \mathbf{B}\cdot\hat{n}\,dS$ — evaluated as
a source, never held as an invariant; the constraint guarantee is the
weakest among the families compared by [Tóth (2000)](/sources/toth-2000.md).

## Properties, per [Tóth (2000)](/sources/toth-2000.md)

* **Non-conservative — with consequences.** By the Lax–Wendroff theorem only
  conservative schemes are guaranteed correct jump conditions; Tóth's rotated
  shock-tube test demonstrates the failure concretely: across strong
  discontinuities the source terms produce **incorrect jumps that do not
  converge away with resolution**, even though the solution appears to
  converge normally.
* **Grid-agnostic and simple:** no staggering, no elliptic solve; usable on
  any grid type; requires only source terms and a Riemann-solver
  modification of the base scheme.
* **Usually adequate:** in most of the ten test problems it "works
  correctly" with small divergence errors and competitive accuracy — the
  failure mode is occasional, not generic.
* Initial/boundary data must satisfy the constraint to second-order accuracy
  (contrast the roundoff-exact compatibility CT requires:
  [exact discrete divergence](/properties/exact-discrete-divergence.md)).

**Powell's own rotated shock tube: a qualification.** The 1994 report
runs a 45°-rotated Brio–Wu tube with the first-order scheme on 600 and
1200 cells ([rotated shock tube](/benchmarks/rotated-shock-tube.md)).
Rotated and unrotated results are "nearly indistinguishable for all but the
normal component of velocity", and the normal-field errors, "on the order
of a few percent … on the coarse grid", "are reduced as the grid is
refined" (§3, Figs. 5, 8). This does not contradict Tóth's wrong-jump
result. The quantities differ: Powell measures the amplitude of
normal-field spikes at two resolutions, Tóth the post-shock states. So do
the schemes (first order against Tóth's second-order base scheme) and the
evidence (two grids, no convergence study of the plateau values). Powell's
visible offset of the normal velocity in the post-shock plateau (Fig. 5) is
the kind of error Tóth reports, and it was plotted on the fine grid only.

**An untested assessment.** Ryu, Miniati, Jones & Frank judge that the
source-term method "works well for some problems with open boundaries but
not for others, including those with periodic boundaries"; they give no
test ([Ryu et al. (1998)](/sources/ryu-1998.md) §1).

**Positivity, a second argument for the source term** (alongside Derigs et al.'s thermodynamic one).
[Wu & Shu (2018)](/sources/wu-shu-2018.md) prove that LF-type DG schemes for the
symmetrizable form are positivity-preserving at any order. The schemes
discretize the source term as a penalty, from $D_h^{\mathrm{c}}$ at first order
and from normal-field jumps at faces at high order, and use a locally
divergence-free basis. The proof needs no discrete divergence-free
condition. The conservative form provably needs one
([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).
This weighs against Tóth's wrong-jump result rather than closing it:
Wu & Shu concede the loss of conservation, and they run no
jump-convergence test of the kind Tóth used.
At the PDE level, smooth solutions of the symmetrizable system provably
keep density and pressure positive for any $\nabla\cdot B$. The result
extends to HLL fluxes on general meshes
([Wu & Shu (2019)](/sources/wu-shu-2019.md)).

The conservation trade-off is stated openly in the primary source: local
conservation errors are accepted in exchange for symmetrizability. Tóth's
rotated shock-tube result is the concrete realization of the risk that trade
admits — the two sources agree on the mechanism and differ in emphasis on
how often it bites.

**Low dissipation, measured in turbulence (preprint).** In driven
subsonic turbulence, Powell runs give the fastest kinematic dynamo at fixed
resolution: about 3 times Dedner on the same moving-mesh hydrodynamics,
2 times Dedner in a DG code, and up to 3–4 times a second-order CT code.
Arepo-Powell at $128^3$ matches Ramses-CT at $256^3$ in its kinematic
magnetic spectrum. On Arepo's moving Voronoi mesh the divergence arises
mainly from the continual change of the gradient discretization, and the
source terms remove most of it. The DG variant pairs a locally
divergence-free basis with a face Powell term, the same structure as
Wu & Shu's positive DG. Total momentum is no longer conserved to machine
precision ([Pakmor et al. (2026)](/sources/pakmor-2026.md)).
*Compiler reading:* the flow is subsonic, so Tóth's wrong-jump failure is
not exercised by this test.

**The eigensystem without the source terms.** [Jiang & Wu (1999)](/sources/jiang-1999.md) use Powell's $8\times8$
eigensystem only to decompose the flux for characteristic WENO
reconstruction; they add no source terms. Its effect is a nonzero
dissipative flux in the normal-field equation, which the $7\times7$
system leaves at zero. Without divergence correction this delays the
Orszag–Tang failure from $t \approx 2.5$ to $t \approx 3.9$; the authors
report that a fourth-order diffusion added to that equation does the same.
Neither replaces the projection they use.
*Compiler reading:* this isolates the dissipation carried by the eighth
characteristic field from the source terms that define the formulation.
Only the first is present here.

**The seven-wave system it augments.**
[Brio & Wu (1988)](/sources/brio-wu-1988.md) built their Roe-type scheme
on the 1D system with the normal field held constant: seven equations and
a $7\times7$ Jacobian with no normal-field row (§IV). That system is not
strictly hyperbolic. Up to five of its seven eigenvalues coincide, at zero
normal field or zero transverse field, and there the standard right
eigenvectors become ill defined and their matrix singular. Brio and Wu
renormalize them into "a set of right eigenvectors which is well defined
everywhere" (§IV.3, eqs. 39–46); this is the normalization
[Jiang & Wu (1999)](/sources/jiang-1999.md) use. The paper discusses no
zero eigenvalue and no divergence wave: in 1D the constraint is just a
constant normal field (§§II, IV).

**In a same-code comparison** ([Tomida, Sadanari, Takasao & Iwasaki (2026)](/sources/tomida-2026.md), Appendix A), Powell source terms in
Athena++, discretized with cell-centred differences, let the divergence
grow steadily on a KH test with a localized field without crashing. They
leave scaly, artificial field patterns that diffuse into the weakly
magnetized region, though without GLM's propagation. The authors note
that the method damps nothing and is not "cleaning".

[GLM cleaning](/methods/glm-divergence-cleaning.md) later kept the
advect-the-error philosophy while removing the trade: its source term sits
only in the unphysical $\psi$ equation, leaving the physical conservation
laws intact; in the Dedner et al. comparisons GLM is more robust than the
Powell source terms with significantly smaller divergence errors
([Dedner et al. (2002)](/sources/dedner-2002.md)).

A sharper attack targets the *motivation*:
[Balsara (2004)](/sources/balsara-2004.md) (his "Issue 3") notes the
eighth wave exists to handle the jump in the normal field component at
zone faces, which makes seven-wave Riemann solvers ill-defined — but
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
keeps that component $C^0$-continuous by construction, "thereby
eliminating the need for an eight-wave model" (with the absence of
physical magnetic monopoles invoked against monopole-introducing source
terms). The critique removes the premise, not the scheme: the eight-wave
formulation remains valid where cell-centered storage is a hard
requirement.

# Citations

1. [Powell et al. (1999)](/sources/powell-1999.md), §§2–3.
2. [Tóth (2000)](/sources/toth-2000.md), §§2–3, 6.3, 7.
3. [Dedner et al. (2002)](/sources/dedner-2002.md), §5.
4. [Balsara (2004)](/sources/balsara-2004.md), §1 (Issue 3).
5. [Derigs et al. (2018)](/sources/derigs-2018.md) — thermodynamic
   rederivation: allowing $\nabla\cdot\mathbf{B}\ne 0$ from first
   principles *produces* the non-conservative terms, recasting them as
   required physics wherever the constraint is not pointwise exact
   (the strongest published defense of the source-term family).
6. [Wu & Shu (2018)](/sources/wu-shu-2018.md), §§1, 3, 5.
7. [Wu & Shu (2019)](/sources/wu-shu-2019.md), §4, Proposition A.1.
8. [Pakmor et al. (2026)](/sources/pakmor-2026.md), §§2.1, 3, 6.2 (preprint).
9. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§2.3, 3.4.
10. [Tomida, Sadanari, Takasao & Iwasaki (2026)](/sources/tomida-2026.md), Appendix A.
11. [Brio & Wu (1988)](/sources/brio-wu-1988.md), §§II, IV.2–IV.3.
12. [Powell (1994)](/sources/powell-1994.md), §§1–4, eqs. 5, 8–17, Figs. 2–8.
13. [Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md), pp. 427–429.
14. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §1.
