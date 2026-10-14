---
type: Source
title: "Riley, Hobson & Bence (2006) — Mathematical Methods for Physics and Engineering, 3rd ed. (Chs. 10, 11, 26)"
description: "Textbook of applied mathematics; this bundle reads its vector calculus (Ch. 10), line, surface and volume integrals with the divergence, Stokes and Green theorems (Ch. 11) and tensors from Cartesian to general curvilinear coordinates with metric, Christoffel symbols and covariant derivative (Ch. 26)."
resource: "doi:10.1017/CBO9780511810763"
source_kind: book
authors: [Riley K.F., Hobson M.P., Bence S.J.]
year: 2006
venue: "Cambridge University Press (3rd ed.)"
local_file: "/home/stefano/papers/mosaic/curvilinear-metric-discretization/2006-CUP-Riley-101017CBO9780511810763.pdf"
tags: [textbook, vector-calculus, integral-theorems, tensor-calculus, curvilinear-coordinates, metric]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

Riley, Hobson and Bence's *Mathematical Methods for Physics and Engineering*
(3rd ed., Cambridge University Press, 2006; hardback ISBN 978-0-521-86153-3,
paperback 978-0-521-67971-8; DOI verified on Crossref as a monograph,
edition 3) is a graduate-entry textbook that presents each topic as a
qualitative introduction, a formal development that "deliberately avoided
strictly mathematical questions such as the existence of limits", and worked
examples (preface to the first edition, p. xxv). Proofs are therefore
heuristic in places, and several results are stated with "it may be shown".

**Scoped read.** This bundle read the preface (third, second and first
editions), the contents, and Chapters 10 (*Vector calculus*, pp. 334–376),
11 (*Line, surface and volume integrals*, pp. 377–414) and 26 (*Tensors*,
pp. 927–983), including their exercises and hints. All other chapters were
not read here; the same book founds other bundles that read other chapters.
PDF page = printed page + 30. The text layer is a scanned print with
garbled equations; every equation used on a concept page was checked
against the text and, where ambiguous, against a rendered page image
(pp. 366, 368, 955, 962, 964, 966, 967, 973, 974). No range was illegible.

The three chapters build one line: Cartesian vector operators (Ch. 10) →
their orthogonal-curvilinear forms through scale factors (§§10.9–10.10) →
coordinate-free integral definitions and the integral theorems (Ch. 11) →
Cartesian tensors and, from §26.14, general tensors in arbitrary curvilinear
coordinates with the metric tensor, Christoffel symbols, covariant
derivative and the tensor forms of grad, div, curl and Laplacian valid for
non-orthogonal systems (§26.20). The book covers the continuum only:
discretization of metrics, grids and conservation laws in moving
coordinates are outside it.

# Key claims

1. **Curvilinear coordinates and scale factors** (§10.10, pp. 364–366):
   one-to-one differentiable mapping, coordinate surfaces and curves,
   orthogonality; $h_i=\lvert\partial\mathbf x/\partial\xi^i\rvert$,
   $(ds)^2=\sum h_i^2(d\xi^i)^2$ and $dV=h_1h_2h_3\,d\xi^1d\xi^2d\xi^3$ for
   orthogonal systems (eq. (10.58)). → [curvilinear coordinates](/definitions/curvilinear-coordinates.md),
   [scale factors](/definitions/scale-factors.md).
2. **Two reciprocal bases** $\mathbf a_i=\partial\mathbf x/\partial\xi^i$ and
   $\mathbf a^i=\nabla\xi^i$, $\mathbf a_i\cdot\mathbf a^j=\delta^j_i$
   (pp. 366–367; eq. (26.54)); contravariant and covariant components
   (p. 366, §26.14); $\mathbf a^i=\mathbf a_j\times\mathbf a_k/[\mathbf a_i\cdot(\mathbf a_j\times\mathbf a_k)]$
   (p. 959). → [bases](/definitions/covariant-and-contravariant-bases.md).
3. **Orthogonal-coordinate operators** (eqs. (10.60)–(10.62), Table 10.4,
   pp. 367–369), with cylindrical and spherical tables 10.2–10.3; proofs of
   div and curl through $\nabla\cdot(\nabla\xi^2\times\nabla\xi^3)=0$ and
   $\nabla\times\nabla\xi^1=\mathbf 0$. → [gradient](/definitions/gradient.md),
   [divergence](/definitions/divergence.md), [curl](/definitions/curl.md),
   [Laplacian](/definitions/laplacian.md).
4. **Vector identities** (Table 10.1; eqs. (10.37)–(10.43), pp. 354–357),
   stated to be coordinate-independent; the vector Laplacian splits by
   components only in Cartesians (p. 357). → [vector operator identities](/results/vector-operator-identities.md).
5. **Line and surface integrals; vector area** (§§11.1, 11.5, pp. 377–396):
   orientation conventions, $d\mathbf S=\hat{\mathbf n}\,dS$, parametric
   surface element (eqs. (10.22)–(10.24)); $\oint_Sd\mathbf S=\mathbf 0$ for a
   closed surface, $\mathbf S=\frac12\oint_C\mathbf x\times d\mathbf x$,
   $V=\frac13\oint_S\mathbf x\cdot d\mathbf S$ (pp. 393–397).
   → [vector area element](/definitions/vector-area-element.md),
   [closed-surface vector area](/results/closed-surface-vector-area.md).
6. **Connectivity and conservative fields** (§§11.2, 11.4, pp. 383–389):
   four equivalent conditions in a simply connected region; multivalued
   potentials in multiply connected ones (§11.9.2). → [conservative vector field](/definitions/conservative-vector-field.md).
7. **Green's theorem in the plane** (eq. (11.4), pp. 384–386).
   → [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md).
8. **Integral definitions of grad, div, curl** (eqs. (11.14)–(11.17),
   p. 398), shown consistent in Cartesians (grad) and orthogonal coordinates
   (div, curl) only. → [integral definitions](/results/integral-definitions-of-grad-div-curl.md).
9. **Divergence theorem** (eq. (11.18), p. 401) by summing the integral
   definition over a partition; corollaries (11.21)–(11.22); continuity
   equation (§11.8.3); tensor form (§26.13, stated without rigorous proof).
   → [divergence theorem](/results/divergence-theorem.md); Green's first
   and second theorems (eqs. (11.19)–(11.20)) → [Green's identities](/results/greens-identities.md).
10. **Stokes' theorem** (eq. (11.23), p. 406), corollaries (11.24)–(11.25),
    tensor form (p. 955). → [Stokes' theorem](/results/stokes-theorem.md).
11. **Cartesian tensors** (§§26.3–26.12): rotation law, algebra, contraction,
    quotient law (proved for $M=N=2$), $\delta_{ij}$ and $\varepsilon_{ijk}$,
    the $\varepsilon$–$\delta$ identity (26.30), isotropic tensors,
    pseudotensors, duals; physical examples (inertia, conductivity,
    elasticity). → [Cartesian tensor](/definitions/cartesian-tensor.md),
    [quotient law](/results/quotient-law.md),
    [Levi-Civita symbol](/definitions/levi-civita-symbol.md).
12. **Metric tensor** (§26.15, eqs. (26.56)–(26.65)): $g_{ij}=\mathbf a_i\cdot\mathbf a_j$,
    $(ds)^2=g_{ij}d\xi^id\xi^j$, $dV=\sqrt g\,d\xi^1d\xi^2d\xi^3$,
    $[g^{ij}]=[g_{ij}]^{-1}$, raising and lowering, $\lvert\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)\rvert=\sqrt g$
    ("it may be shown"). → [metric tensor](/definitions/metric-tensor.md),
    [Jacobian](/definitions/jacobian.md).
13. **General tensors** (§26.16, eq. (26.71)): contravariant and covariant
    transformation laws as definitions; $g_{ij}$ is a tensor; partial
    derivatives of components are not (eq. (26.84)). → [general tensor](/definitions/general-tensor.md).
14. **Relative tensors** (§26.17, eq. (26.74)): weight $w$ with the factor
    $\lvert\partial\xi/\partial\bar\xi\rvert^w$; $g$ has weight 2,
    $\varepsilon_{ijk}$ weight $-1$, $\varepsilon^{ijk}$ weight $+1$; the
    source flags that both $\lvert\partial\bar\xi/\partial\xi\rvert$ and its
    reciprocal are called "the Jacobian". → [relative tensor](/definitions/relative-tensor.md).
15. **Christoffel symbols** (§26.18, eqs. (26.75)–(26.83)): definition,
    symmetry, non-tensor transformation (26.78), metric formula (26.82),
    cylindrical values. → [Christoffel symbols](/definitions/christoffel-symbols.md).
16. **Covariant derivative** (§26.19, eqs. (26.85)–(26.90)) and absolute
    derivative, geodesics (§§26.21–26.22); $g_{ij;k}=0$ and vanishing
    Riemann tensor in Euclidean space as exercises (26.27, 26.29).
    → [covariant derivative](/definitions/covariant-derivative.md).
17. **Vector operators in tensor form** (§26.20, eqs. (26.91)–(26.98),
    pp. 971–975): $\nabla\phi=\partial_i\phi\,\mathbf a^i$;
    $\nabla\cdot\mathbf v=(1/\sqrt g)\partial_j(\sqrt g\,v^j)$ via
    $\Gamma^i_{ki}=\partial_k\sqrt g/\sqrt g$;
    $\nabla^2\phi=(1/\sqrt g)\partial_j(\sqrt g\,g^{jk}\partial_k\phi)$;
    $(\nabla\times\mathbf v)^i=(1/\sqrt g)\varepsilon^{ijk}\partial_jv_k$;
    valid for non-orthogonal systems.

Not compiled into pages (kept here only): space curves and the
Frenet–Serret formulae (§10.3, eq. (10.16)); the physical applications of
§26.12 (inertia tensor, conductivity, Hooke's law with the Lamé constants);
solid angle (eq. (11.11)).

# Notation map

| Riley et al. | Registry | Note |
|---|---|---|
| $u_1,u_2,u_3$ (Ch. 10), $u^1,u^2,u^3$ (Ch. 26) | $\xi^1,\xi^2,\xi^3$ | curvilinear coordinates |
| $u'^i$ | $\bar\xi^i$ | second general system |
| $x,y,z$; $x_i$ | $x^i$ ($x_i$ allowed in Cartesian-tensor pages) | |
| $\mathbf r$ | $\mathbf x$ | position vector; $r=\lvert\mathbf x\rvert$ kept |
| $\mathbf i,\mathbf j,\mathbf k$; $\mathbf e_i$ (Cartesian, §§26.2–26.13) | $\mathbf e_k$ | |
| $\mathbf e_i=\partial\mathbf r/\partial u_i$ | $\mathbf a_i$ | covariant base vectors |
| $\boldsymbol\epsilon_i=\nabla u_i$ (Ch. 10, §26.14), $\mathbf e^i$ (from §26.14) | $\mathbf a^i$ | contravariant base vectors |
| $\hat{\mathbf e}_i$ | $\hat{\mathbf a}_i$ | unit tangent basis |
| $\hat{\boldsymbol\epsilon}_i$ | $\hat{\mathbf a}^i$ | unit normal basis |
| $\alpha_i$, $\beta_i$ (§10.10) | $v^i$, $v_i$ | contravariant, covariant components |
| $a_i$, $A_i$ on unit bases (§10.10); $\hat v^i$ (§26.20) | $\hat v_i$ | physical components |
| $\mathbf a$ (vector field) | $\mathbf v$ | |
| $\Phi$ (scalar field, Tables 10.2–10.4) | $\phi$ | |
| $(\rho,\phi,z)$ cylindrical | $(R,\varphi,z)$ | $\rho$ reserved for density |
| $(r,\theta,\phi)$ spherical | $(r,\theta,\varphi)$ | |
| $\hat{\mathbf e}_\rho,\hat{\mathbf e}_\phi,\dots$ | $\hat{\mathbf a}_R,\hat{\mathbf a}_\varphi,\dots$ | |
| $\epsilon_{ijk}$ | $\varepsilon_{ijk}$ | |
| $J=\lvert\partial u'/\partial u\rvert$ (§26.17) | $\lvert\partial\bar\xi/\partial\xi\rvert$, written in full | the registry's $J$ is $\det[\partial x^i/\partial\xi^j]$ only |
| $\mathsf G=[g_{ij}]$, $\hat{\mathsf G}=[g^{ij}]$, $\mathsf U$ | $G$, $[g^{ij}]$, $U$ | |
| $\mathbf v$ (fluid velocity, §11.8.3) | $\mathbf u$ | |
| $\hat{\mathbf n}$, $d\mathbf S$, $dS$, $V$, $S$, $C$, $\delta_{ij}$, $g_{ij}$, $g$, $\Gamma^k_{ij}$, $v^i{}_{;j}$, $h_i$ | same | |
| primes on rotated Cartesian frames ($x'_i=L_{ij}x_j$) | same, on Cartesian-tensor pages only | |

# Pages created

* Created [Notation registry](/notation.md)
* Created [General curvilinear coordinates](/definitions/curvilinear-coordinates.md)
* Created [Scale factors](/definitions/scale-factors.md)
* Created [Covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md)
* Created [Metric tensor](/definitions/metric-tensor.md)
* Created [Jacobian of the coordinate mapping](/definitions/jacobian.md)
* Created [Christoffel symbols](/definitions/christoffel-symbols.md)
* Created [Cartesian tensor](/definitions/cartesian-tensor.md)
* Created [General tensor](/definitions/general-tensor.md)
* Created [Relative tensor](/definitions/relative-tensor.md)
* Created [Levi-Civita symbol](/definitions/levi-civita-symbol.md)
* Created [Conservative vector field](/definitions/conservative-vector-field.md)
* Created [Vector area element](/definitions/vector-area-element.md)
* Created [Gradient](/definitions/gradient.md)
* Created [Divergence](/definitions/divergence.md)
* Created [Curl](/definitions/curl.md)
* Created [Laplacian](/definitions/laplacian.md)
* Created [Covariant derivative](/definitions/covariant-derivative.md)
* Created [Divergence theorem](/results/divergence-theorem.md)
* Created [Green's identities](/results/greens-identities.md)
* Created [Stokes' theorem](/results/stokes-theorem.md)
* Created [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md)
* Created [Integral definitions of grad, div and curl](/results/integral-definitions-of-grad-div-curl.md)
* Created [Vector area of a closed surface](/results/closed-surface-vector-area.md)
* Created [Vector operator identities](/results/vector-operator-identities.md)
* Created [Quotient law](/results/quotient-law.md)
* Cited on [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md) (added with arfken-2013)

# Citations

The chapters read cite three works, all in the opening footnote of Ch. 26
(p. 927) as textbooks on tensor calculus in general spaces and relativity:
D'Inverno (1992), Foster & Nightingale (2006), Schutz (1985); recorded in
the [bibliography](/bibliography.md). Chapters 10 and 11 cite no external
work. The preface mentions the companion *Student Solutions Manual*
(Cambridge University Press, 2006), not recorded as a citation of the
chapters read.
