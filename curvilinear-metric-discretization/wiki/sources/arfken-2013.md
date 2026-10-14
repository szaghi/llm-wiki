---
type: Source
title: "Arfken, Weber & Harris (2013) — Mathematical Methods for Physicists, 7th ed. (Chs. 3, 4)"
description: "Textbook of mathematical physics; this bundle reads its vector analysis with orthogonal curvilinear coordinates, integral theorems and potential theory (Ch. 3) and its tensors in general coordinates, Jacobians and differential forms with the exterior derivative and Stokes' theorem for forms (Ch. 4)."
resource: "doi:10.1016/C2009-0-30629-7"
source_kind: book
authors: [Arfken G.B., Weber H.J., Harris F.E.]
year: 2013
venue: "Academic Press (7th ed.)"
local_file: "/home/stefano/papers/mosaic/curvilinear-metric-discretization/2013-AcademicPress-Arfken-101016C20090306297.pdf"
tags: [textbook, vector-calculus, integral-theorems, curvilinear-coordinates, tensor-calculus, metric, jacobian, differential-forms]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

Arfken, Weber and Harris's *Mathematical Methods for Physicists* (7th ed.,
Academic Press, an imprint of Elsevier, © 2013; ISBN 978-0-12-384654-9;
DOI 10.1016/C2009-0-30629-7, verified on Crossref) is a graduate textbook in
which "proofs are sketched for almost all the mathematical relations", and
"the mathematical proofs are not what a mathematician would consider
rigorous", while the reader "is warned of limitations that are likely to be
relevant" (preface, p. xi).

**Scoped read.** This bundle read the preface (pp. xi–xiii) and Chapters 3
(*Vector Analysis*, pp. 123–203) and 4 (*Tensors and Differential Forms*,
pp. 205–249), including their exercises and the chapter-end Additional
Readings. All other chapters were not read here; the same book is ingested by
other bundles for other chapters. The file is a calibre ebook conversion with
a good text layer; the PDF-to-printed page offset is +12 in Ch. 3 and +11 in
Ch. 4, and all locators below are **printed** pages read from the running
heads. Equations were taken from the text layer and checked against rendered
page images where it was ambiguous (pp. 165, 184, 191, 222, 225). No range
was illegible. Misprints found and checked on the page image: eq. (3.84)
repeats (3.83) instead of exchanging $u,v$ (p. 165); eq. (3.131) has
$(\partial y/\partial q_i)^2$ twice, the third term should be
$(\partial z/\partial q_i)^2$ (p. 184); eq. (3.154) prints
$d\tau=r^2\sin\theta\,d\rho\,d\theta\,d\varphi$ for $dr$ (p. 191); in
Example 4.7.2 (p. 247) "$dz\wedge dz\to d\sigma_y$" stands for
$dz\wedge dx$, and eq. (4.115) has $E_y\,dz\wedge dz$ for $E_y\,dz\wedge dx$.

Chapter 3 develops Cartesian vector algebra and rotations, the differential
operators with their flux and circulation interpretations, line, surface and
volume integrals, the Gauss, Green and Stokes theorems, potential theory with
the Helmholtz theorem, and the operators in **orthogonal** curvilinear
coordinates. Chapter 4 adds tensors under general coordinate changes, the
metric tensor, covariant and contravariant bases, Christoffel symbols and the
covariant derivative with the tensor forms of grad, div, Laplacian and curl
(§4.3), the Jacobian of a change of variables (§4.4), and differential forms:
exterior algebra, Hodge star, exterior derivative and Stokes' theorem for
forms (§§4.5–4.7). Like the founding source, it covers the continuum only:
grids, discretization and moving coordinates are outside it.

# Key claims

1. **Rotations and Cartesian tensors** (§§3.3–3.4, eqs. (3.26)–(3.37);
   §4.1, eqs. (4.1)–(4.17); §4.2): orthogonal transformation matrix with
   $\partial x_\nu/\partial x'_\mu=\partial x'_\mu/\partial x_\nu$ for
   Cartesian frames (eq. (3.34), p. 139); pseudovectors $\det(S)S\mathbf A$;
   isotropy of $\delta$ and $\varepsilon$; duals. → [Cartesian tensor](/definitions/cartesian-tensor.md),
   [relative tensor](/definitions/relative-tensor.md), [Levi-Civita symbol](/definitions/levi-civita-symbol.md).
2. **Gradient, divergence, curl, Laplacian** (§§3.5–3.6, eqs. (3.38)–(3.74),
   pp. 143–158): the gradient proved to be a vector; divergence as net
   outflow per unit volume with the continuity equation (eqs. (3.55)–(3.56));
   curl as circulation per unit area (eq. (3.60)); vector Laplacian defined
   by the double-curl identity (eq. (3.70)), componentwise only in
   Cartesians. → [gradient](/definitions/gradient.md),
   [divergence](/definitions/divergence.md), [curl](/definitions/curl.md),
   [Laplacian](/definitions/laplacian.md), [vector operator identities](/results/vector-operator-identities.md).
3. **Vector integration and integral theorems** (§§3.7–3.8, eqs. (3.75)–(3.95),
   pp. 159–170): orientation of $d\boldsymbol\sigma$; Gauss' theorem for a
   simply connected region (eq. (3.81)); Green's theorem (eqs. (3.85)–(3.86));
   Stokes' theorem (eq. (3.92)) and $\oint(\nabla\times\mathbf B)\cdot d\boldsymbol\sigma=0$
   over a closed surface (eq. (3.93)); the gradient and curl corollaries.
   → [vector area element](/definitions/vector-area-element.md),
   [divergence theorem](/results/divergence-theorem.md),
   [Green's identities](/results/greens-identities.md),
   [Stokes' theorem](/results/stokes-theorem.md),
   [vector area of a closed surface](/results/closed-surface-vector-area.md).
4. **Potential theory** (§3.9, pp. 170–182): equivalence of $\mathbf F=-\nabla\varphi$,
   path independence and zero curl in a simply connected region; explicit
   vector potential of a solenoidal field (eq. (3.102)); gauge freedom;
   $\nabla^2(1/r)=-4\pi\delta(\mathbf r)$ (eq. (3.120)); the uniqueness theorem
   and Helmholtz's theorem (eqs. (3.122)–(3.126)).
   → [conservative vector field](/definitions/conservative-vector-field.md),
   [Helmholtz theorem](/results/helmholtz-theorem.md).
5. **Orthogonal curvilinear coordinates** (§3.10, eqs. (3.127)–(3.160),
   pp. 182–203): $g_{ij}$ and scale factors, integrals, grad/div/Laplacian/curl
   derived from flux and circulation on curvilinear elements, cylindrical and
   spherical forms including the vector Laplacian components.
   → [curvilinear coordinates](/definitions/curvilinear-coordinates.md),
   [scale factors](/definitions/scale-factors.md),
   [integral definitions of grad, div and curl](/results/integral-definitions-of-grad-div-curl.md).
6. **General tensors and the quotient rule** (§4.1, eqs. (4.4)–(4.24)):
   contravariant, covariant and mixed laws; $\delta^k_l$ a mixed tensor in any
   dimension; contraction; direct product; inverse law; quotient rule proved
   for $K_i{}^jA_j=B_i$ in general coordinates, with the zero-right-hand-side
   pitfall. → [general tensor](/definitions/general-tensor.md),
   [quotient law](/results/quotient-law.md).
7. **Metric and bases in general coordinates** (§4.3, eqs. (4.37)–(4.50),
   pp. 218–221): $\boldsymbol\varepsilon_i=\partial\mathbf r/\partial q^i$,
   $g_{ij}=\boldsymbol\varepsilon_i\cdot\boldsymbol\varepsilon_j$, $g^{ij}$ as the
   inverse, $\boldsymbol\varepsilon^i=\nabla q^i$ with
   $\boldsymbol\varepsilon^i\cdot\boldsymbol\varepsilon_j=\delta^i_j$ and
   $g^{ij}=\boldsymbol\varepsilon^i\cdot\boldsymbol\varepsilon^j$; spherical
   metric. → [metric tensor](/definitions/metric-tensor.md),
   [covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md).
8. **Christoffel symbols and covariant derivative** (§4.3,
   eqs. (4.51)–(4.63), pp. 222–224), and the tensor forms of gradient,
   divergence $\frac{1}{\sqrt{\det g}}\partial_k(\sqrt{\det g}\,V^k)$,
   Laplacian and curl $V_{i;j}-V_{j;i}$ (eqs. (4.64)–(4.71), pp. 224–225).
   → [Christoffel symbols](/definitions/christoffel-symbols.md),
   [covariant derivative](/definitions/covariant-derivative.md),
   and the operator pages of claim 2.
9. **Jacobians** (§4.4, eqs. (4.72)–(4.76), pp. 227–231): $d\tau=J\,du_1du_2\cdots$
   with $J=\partial(x_1,x_2,\dots)/\partial(u_1,u_2,\dots)$ derived as a volume
   by row reduction; $J^{-1}=1/J$; triple-product form; sign tied to
   handedness. → [Jacobian](/definitions/jacobian.md).
10. **Differential forms** (§4.5, eqs. (4.77)–(4.84), pp. 232–238): $p$-forms,
    exterior algebra, Hodge star in Euclidean and Minkowski space, cross and
    triple products as $*(A\wedge B)$ and $*(A\wedge B\wedge C)$.
    → [differential form](/definitions/differential-form.md),
    [wedge product](/definitions/wedge-product.md),
    [Hodge star](/definitions/hodge-star.md).
11. **Exterior derivative** (§4.6, eqs. (4.85)–(4.99), pp. 238–243): axioms,
    $d(d\omega)=0$ (called Poincaré's lemma), grad/curl/div as $d$ on 0-, 1-,
    2-forms, $\nabla\times\nabla f=0$ and $\nabla\cdot\nabla\times\mathbf A=0$
    from $d^2=0$, Maxwell's equations as $dF=0$, $d(*F)=J$.
    → [exterior derivative](/definitions/exterior-derivative.md).
12. **Integrating forms; Stokes' theorem** (§4.7, eqs. (4.100)–(4.117),
    pp. 243–248): exact forms, oriented areas and the signed Jacobian
    (eqs. (4.103)–(4.105)), $\int_R d\omega=\int_{\partial R}\omega$ for a simply
    connected region (eq. (4.106)), with Green, Stokes and Gauss as cases.
    → [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md),
    [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md).

Not compiled into pages (kept here only): Euler angles and the rotation
matrix (eqs. (3.35)–(3.37)); rotations and reflections of spherical
components (eqs. (3.166)–(3.169)); spinors (one paragraph, p. 213);
electromagnetic applications (Maxwell's equations, gauge conditions, Gauss's
law, Oersted and Faraday laws) except as illustrations named on the pages
above; the Riemann tensor counting exercise 4.1.5 (four-dimensional).

## Comparison with the founding source

No contradiction with [Riley et al. (2006)](/sources/riley-2006.md) was
found in the chapters read. Every shared continuum claim agrees, including
the general-coordinate divergence and Laplacian, the Christoffel-symbol
formulas and the covariant derivative. Differences recorded as
**qualifications** (different hypotheses, scope or naming, not incompatible
claims):

* *Connectivity hypothesis of the integral theorems.* Arfken assumes a simply
  connected region for Gauss' theorem (p. 164) and for Stokes' theorem for
  forms (p. 245); Riley states the divergence and Stokes theorems for multiply
  connected surfaces too (pp. 401, 406). → [divergence theorem](/results/divergence-theorem.md),
  [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md),
  [Stokes' theorem](/results/stokes-theorem.md),
  [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md).
* *Smoothness of the second-order identities.* Arfken requires continuous
  second derivatives (pp. 154–155); Riley says "differentiable".
  → [vector operator identities](/results/vector-operator-identities.md).
* *Sign of the metric's diagonal elements.* Arfken's "may be of either sign"
  (p. 219) concerns pseudo-Riemannian metrics; in Euclidean space both books'
  definition gives $g_{ii}>0$. → [metric tensor](/definitions/metric-tensor.md).
* *Names.* Arfken's "Green's theorem" is Riley's Green's second theorem
  (→ [Green's identities](/results/greens-identities.md)); Arfken's "rank" is
  Riley's "order"; Arfken's Example 4.4.2 labels $\partial(r,\theta,\varphi)/\partial(x,y,z)$
  as $J$, reversing its own eq. (4.74) (→ [Jacobian](/definitions/jacobian.md));
  Arfken calls $d(d\omega)=0$ "Poincaré's lemma" (→ [exterior derivative](/definitions/exterior-derivative.md)).

# Notation map

| Arfken et al. | Registry | Note |
|---|---|---|
| $q_1,q_2,q_3$ (Ch. 3), $q^i$ (Ch. 4) | $\xi^1,\xi^2,\xi^3$ | curvilinear coordinates |
| $(x')^i$, $x'_i$ | $\bar\xi^i$ (general change), primed $x'_i$ on Cartesian-tensor pages | |
| $x,y,z$; $x_i$; $x^i$ | $x^i$ | Arfken moves to upper indices in Ch. 4 |
| $\mathbf r$, $r$ | $\mathbf x$, $r=\lvert\mathbf x\rvert$ | |
| $\hat{\mathbf r}$ | $\hat{\mathbf x}$ | radial unit vector |
| $\hat{\mathbf e}_x,\hat{\mathbf e}_y,\hat{\mathbf e}_z$; $\hat{\mathbf e}_i$ (Cartesian) | $\mathbf e_k$ | |
| $\hat{\mathbf e}_i$ (orthogonal curvilinear, Ch. 3) | $\hat{\mathbf a}_i$ | defined as unit normals to coordinate surfaces (p. 183) and as $h_i^{-1}\partial\mathbf r/\partial q_i$ (eq. (3.132)); equal in orthogonal systems |
| $\boldsymbol\varepsilon_i$ | $\mathbf a_i$ | covariant basis vectors (eq. (4.37)) |
| $\boldsymbol\varepsilon^i$ | $\mathbf a^i$ | contravariant basis vectors (eq. (4.44)) |
| $\varepsilon_{ijk}$ | $\varepsilon_{ijk}$ | same symbol as the basis vectors' $\boldsymbol\varepsilon$ in Arfken; bold vs. indexed distinguishes them |
| $S$, $s_{\mu\nu}$, $A$ (orthogonal transformation) | $L$, $L_{ij}$ | Cartesian-tensor pages only |
| $\mathbf A,\mathbf B,\mathbf V,\mathbf P$ (generic vectors) | $\mathbf v,\mathbf w,\mathbf b$ | |
| $\varphi$, $\psi$, $f$, $u$, $v$ (scalar fields) | $\phi,\psi$ | Arfken's $\varphi$ is a scalar potential in Ch. 3 and the azimuth in §3.10 |
| $V_i$, $V^i$ | $v_i$, $v^i$ | covariant, contravariant components |
| $V_i$ on $\hat{\mathbf e}_i$ (Ch. 3, orthogonal) | $\hat v_i$ | physical components; $\hat v_k=h_kv^k$ (p. 225) |
| $h_i$ | $h_i$ | scale factors |
| $g_{ij}$, $g^{ij}$ | $g_{ij}$, $g^{ij}$ | |
| $\det(g)$ | $g$ | $[\det(g)]^{1/2}\leftrightarrow\sqrt g$ |
| $\Gamma^\mu_{jk}$ with $\partial\boldsymbol\varepsilon_k/\partial q^j=\Gamma^\mu_{jk}\boldsymbol\varepsilon_\mu$ | $\Gamma^\mu_{kj}$ ($=\Gamma^\mu_{jk}$) | Arfken writes the differentiation index first in the lower pair; equal by symmetry |
| $[ij,k]=g_{mk}\Gamma^m_{ij}$ | $\Gamma_{kij}$ | Christoffel symbol of the first kind |
| $V^k{}_{;j}$, $V_{i;j}$ | $v^k{}_{;j}$, $v_{i;j}$ | |
| $J=\partial(x_1,x_2,\dots)/\partial(u_1,u_2,\dots)$ | $J=\det[\partial x^i/\partial\xi^j]$ | when $x$ Cartesian and $u=\xi$; Arfken's matrix (4.73) is the transpose, same determinant |
| $J^{-1}=\partial(u_1,\dots)/\partial(x_1,\dots)$ | $J^{-1}$ | Example 4.4.2 swaps the labels (see Jacobian page) |
| $d\boldsymbol\sigma$, $dA$, $\hat{\mathbf n}$ | $d\mathbf S$, $dS$, $\hat{\mathbf n}$ | |
| $d\tau$, $d^3r$ | $dV$ | |
| $d\lambda$ (Ex. 3.8.6–3.8.10) | $d\mathbf x$ | line element |
| $V$, $\partial V$; $S$, $\partial S$ | $V$, $S$; $S$, $C$ | $\partial$ = boundary, registered for forms |
| $R$, $\partial R$ (Stokes for forms) | $\Omega$, $\partial\Omega$ | |
| $(\rho,\varphi,z)$ cylindrical | $(R,\varphi,z)$ | $\rho$ reserved for density |
| $(r,\theta,\varphi)$ spherical | $(r,\theta,\varphi)$ | |
| $\rho$, $\mathbf v$ (fluid, §3.5) | $\rho$, $\mathbf u$ | |
| $\omega$, $\omega'$, $\omega_j$ (forms) | $\alpha,\beta,\gamma$ | |
| $\wedge$, $d$ | $\wedge$, $d$ | |
| $*$ (prefix Hodge operator) | $\star$ | |
| $d$ (space dimension, §4.1), $n$ (Stokes for forms) | $D$ | |
| $s$, $\mathbf c$ (source and circulation densities, Helmholtz) | $\nabla\cdot\mathbf v$, $\nabla\times\mathbf v$ written out | registry $\mathbf c$ is a constant vector |
| $\mathbf r_1$, $\mathbf r_2$, $\nabla_1$, $\nabla_2$, $r_{12}$ | $\mathbf x$, $\mathbf y$, $\nabla$, $\nabla_{\mathbf y}$, $\lvert\mathbf x-\mathbf y\rvert$ | |
| $\mathbf a$ (constant vector, eqs. (3.87)–(3.90)) | $\mathbf c$ | |
| rank | order | of a tensor |

# Pages touched

* Created [Differential form](/definitions/differential-form.md)
* Created [Wedge product](/definitions/wedge-product.md)
* Created [Hodge star operator](/definitions/hodge-star.md)
* Created [Exterior derivative](/definitions/exterior-derivative.md)
* Created [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md)
* Created [Helmholtz theorem](/results/helmholtz-theorem.md)
* Updated [Notation registry](/notation.md) — differential-forms section, $\mathbf y$, $\nabla_{\mathbf y}$, $x_0,y_0$
* Updated [General curvilinear coordinates](/definitions/curvilinear-coordinates.md)
* Updated [Scale factors](/definitions/scale-factors.md)
* Updated [Covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md)
* Updated [Metric tensor](/definitions/metric-tensor.md) — qualification on the sign of diagonal elements
* Updated [Jacobian of the coordinate mapping](/definitions/jacobian.md)
* Updated [Christoffel symbols](/definitions/christoffel-symbols.md)
* Updated [Covariant derivative](/definitions/covariant-derivative.md)
* Updated [General tensor](/definitions/general-tensor.md)
* Updated [Cartesian tensor](/definitions/cartesian-tensor.md)
* Updated [Relative tensor](/definitions/relative-tensor.md)
* Updated [Levi-Civita symbol](/definitions/levi-civita-symbol.md)
* Updated [Conservative vector field](/definitions/conservative-vector-field.md)
* Updated [Vector area element](/definitions/vector-area-element.md)
* Updated [Gradient](/definitions/gradient.md)
* Updated [Divergence](/definitions/divergence.md)
* Updated [Curl](/definitions/curl.md)
* Updated [Laplacian](/definitions/laplacian.md)
* Updated [Divergence theorem](/results/divergence-theorem.md) — qualification on connectivity
* Updated [Green's identities](/results/greens-identities.md) — naming
* Updated [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md)
* Updated [Stokes' theorem](/results/stokes-theorem.md)
* Updated [Integral definitions of grad, div and curl](/results/integral-definitions-of-grad-div-curl.md)
* Updated [Vector area of a closed surface](/results/closed-surface-vector-area.md)
* Updated [Vector operator identities](/results/vector-operator-identities.md) — qualification on smoothness
* Updated [Quotient law](/results/quotient-law.md)

# Citations

The reference list of the chapters read is their chapter-end **Additional
Readings**: ten works after Ch. 3 (p. 203) and fifteen after Ch. 4 (p. 249),
of which Margenau & Murphy (1956) and Morse & Feshbach (1953) appear in
both, so 23 distinct works. The Morse–Feshbach annotation, in both lists,
also cites "the second (1970) edition of Mathematical Methods for
Physicists", recorded as a separate entry; the text of §3.10 refers to "the
first two editions of this work" (p. 187) without bibliographic data for the
first, which is not recorded. All 24 are in the
[bibliography](/bibliography.md), with metadata as printed (no DOI is
printed; none was added).
