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

**A Godunov use before Powell.**
[Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md)
(received June 1992) build a Strang-split higher-order Godunov scheme on a
nonconservative system whose right-hand side "differs from the
conservation form of the equations by terms of the form
$\nabla\cdot\mathbf B(\ldots)$" (§2.1, eq. 1). Their momentum equation is
the conservative one with the term $\mathbf B\,(\nabla\cdot\mathbf B)$
removed, divided by $4\pi$ in their Gaussian units (compiler check,
symbolic): the Brackbill–Barnes form; induction stays conservative (eq. 1e). The energy equation is also
nonconservative, but as printed its difference from conservation form is
not a $\nabla\cdot\mathbf B$ term (reader's reading; see the Source page).
* **Motive: splitting.** The form minimizes the extent to which discrete
  terms in different sweep directions "would have to sum to zero due to
  the divergence-free constraint", and "reduces the effect of magnetic
  monopole forces" (citing Brackbill & Barnes). §4: it "appears to
  suppress the occurrence of monopole forces"; no measurement is given.
* **Sources in the sweeps.** Each 1D sweep holds the normal field
  constant, so the seven-wave Riemann problem applies, and the leftover
  normal-field derivative terms are treated "formally" as source terms
  (§2.1, eqs. 2–4). In primitive variables they reduce to the velocity
  times the normal-field derivative in the transverse-field equations
  only (eq. 15, p. 269).
* *Compiler reading:* those predictor terms are the 1D analogue of the
  induction row of Powell's source. Zachary et al. do not make this
  connection, and they add no eighth wave.

**Rejected by the Ryu codes.**
[Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §2.4 decline
the "modified form of the MHD equations originally suggested in Brackbill &
Barnes (1980)": it "is not suitable for our code and it does not remove
$\nabla\cdot B$ completely anyway". They keep the conservative seven-wave
TVD scheme, hold the parallel field component constant in each split sweep,
and [project](/methods/projection-method.md) after every step instead.

## The analytical mechanism

With the source terms,
$$\partial_t(\nabla\cdot\mathbf{B}) + \nabla\cdot(\mathbf{u}\,\nabla\cdot\mathbf{B}) = 0,$$
i.e. $\nabla\cdot\mathbf{B}/\rho$ is a passively convected scalar: clean
initial and boundary data stay clean along particle paths, to truncation
error. Divergence errors are not eliminated but *advected with the flow*,
preventing local accumulation. What the symmetrizable form buys: Galilean
invariance, an entropy conservation law, and no zero eigenvalue in the flux
Jacobian — none of which the unmodified conservative system has. Known
ambiguity, acknowledged by
[Powell et al. (1999)](/sources/powell-1999.md): isolated recirculating
regions cut off from boundaries. Discretely, the cell source uses the
face-integral divergence $D_h^{\mathrm f}$ (the sum over the cell's faces of
the normal field times the face area, divided by the cell volume) — evaluated as
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
the kind of error Tóth reports; Figs. 3–7 compare the fine-grid runs only
(§3), so its behaviour under refinement is not shown.

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

The conservation trade-off is stated openly by
[Powell et al. (1999)](/sources/powell-1999.md) (the 1994 report has no
symmetrizability argument; see above): local
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
[Orszag–Tang](/benchmarks/orszag-tang-vortex.md) failure from $t \approx 2.5$ to $t \approx 3.9$; the authors
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
everywhere" (§IV.3, eqs. 39–46), at the triple umbilic by assignment (see
the regularity paragraph below); this is the normalization
[Jiang & Wu (1999)](/sources/jiang-1999.md) use. The paper discusses no
zero eigenvalue and no divergence wave: in 1D the constraint is just a
constant normal field (§§II, IV).

**The normalization the eight-wave solver uses.**
[Roe & Balsara (1996)](/sources/roe-balsara-1996.md) rescale the fast and
slow eigenvectors of the same seven-wave system so that each right–left
pair has unit product, with two parameters whose squares sum to one
(eqs. 7–9). The slow parameter is Brio & Wu's; the fast one carries an
extra factor of the sound speed over the fast speed (p. 60). The
eigenvectors stay bounded in every degenerate case except vacuum, but at
the triple umbilic (fast, slow and Alfvén speeds equal) their limit depends
on the direction of approach (eq. 15). Near that point the Roe flux changes
only in proportion to the distance of the linearization state from it
(§4). [Powell (1994)](/sources/powell-1994.md) normalizes his
eigenvectors "as in Roe & Balsara"; the eighth eigenvector is his. Roe &
Balsara's §6 describes Powell's form as retaining the 1D eigenstructure
"with the addition of an eighth wave that convects div B as a passive
scalar", with no equation.

**A second source for the seven-wave system.**
[Ryu & Jones (1995)](/sources/ryu-jones-1995.md) build their Harten-TVD
code on the same system: seven conserved variables without the normal
field, seven eigenvalues, no divergence wave (§§2.1–2.2, eqs. 2.6,
2.10–2.16). They adopt the Brio–Wu renormalization and print in full what Brio &
Wu state more briefly; only the left eigenvectors are new:
* the unnormalized right eigenvectors are "not well defined with columns
  becoming singular" near zero normal field or zero transverse field
  (§2.2);
* the limits of the normalization factors, as in Brio & Wu (eqs. 45–46):
  both transverse direction factors equal $1/\sqrt2$ at zero transverse
  field, and both fast and slow factors equal 1 at the triple point
  (eqs. 2.37–2.38);
* the full left eigenvectors (eqs. 2.39–2.73), which Brio & Wu do not
  print (they solve a linear system for the wave strengths, eq. 47);
* "with the above normalization, some columns are not continuous": a sign
  factor of the transverse field fixes this, applied to the slow
  eigenvectors when the sound speed exceeds the normal Alfvén speed and to
  the fast ones otherwise (eq. 2.74), as Brio & Wu prescribe (p. 410).
[Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §2.2 use the
same eigenvectors without reprinting them.
[Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md)
§2.3.3 state for their own 1992 eigenvectors that "the degeneracy of the
eigenvalues does not also imply a deficiency in the eigenvectors. We
always have a set of complete, linearly independent eigenvectors", and
still detect near-degenerate pairs and add Rusanov dissipation where their
speed changes sign (eqs. 31–33).

**Regularity at the triple umbilic: defined by convention.** The sources
do not disagree about the eigenvectors at the triple umbilic (zero
transverse field, sound speed equal to the normal Alfvén speed); they
handle one indeterminacy by assignment.
* [Brio & Wu (1988)](/sources/brio-wu-1988.md) obtain "well defined
  everywhere" by definition: at that point they set both the fast and the
  slow normalization factor to 1 (eq. 46, p. 410). They concede that with
  this normalization some entries "are not continuous" as both transverse
  components approach zero, and add a sign factor of the transverse field
  for continuity (p. 410).
* [Roe & Balsara (1996)](/sources/roe-balsara-1996.md) show that the limit
  of their normalization parameters there depends on the direction of
  approach (eq. 15) and call it "the unavoidable indeterminacy near the
  magnetosonic (or triple umbilic) state" (abstract). They find Brio & Wu's
  expressions "well formed except close to the 'triple umbilic'", and
  credit those eigenvectors with demonstrating "that the MHD equations are
  always diagonalisable although not everywhere convex" (p. 57).
* [Ryu & Jones (1995)](/sources/ryu-jones-1995.md) make the same kind of
  assignment: both factors equal 1 at the triple point (eq. 2.38), with a
  sign factor for continuity (eq. 2.74).
* Roe & Balsara §4: the Roe-type flux changes only in proportion to the
  distance of the linearization state from the triple umbilic, although
  the individual wave strengths change by order one, and the same argument
  "provides a justification for assigning arbitrary values" to the
  transverse directions where the transverse field vanishes (p. 65).

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
11. [Brio & Wu (1988)](/sources/brio-wu-1988.md), §§II, IV.2–IV.3, eqs. 45–47, p. 410.
12. [Powell (1994)](/sources/powell-1994.md), §§1–4, eqs. 5, 8–17, Figs. 2–8.
13. [Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md), pp. 427–429.
14. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §1.
15. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §§2.1–2.3.3, 4, eqs. 1–4, 15, 31–33.
16. [Ryu & Jones (1995)](/sources/ryu-jones-1995.md), §§2.1–2.2, eqs. 2.6, 2.10–2.16, 2.21–2.74.
17. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §§2.2–2.4.
18. [Roe & Balsara (1996)](/sources/roe-balsara-1996.md), abstract, pp. 57, 60–61, 64–66, eqs. 7–9, 15, §§4, 6.
