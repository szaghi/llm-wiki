---
type: Property
title: "Symplecticity and quadratic-invariant preservation"
description: "A method is symplectic when its one-step map is a symplectic transformation for every Hamiltonian system; splittings into exactly solvable Hamiltonian parts and Gauss–Legendre methods have it, it yields near-conservation of energy over exponentially long times through a modified Hamiltonian, and it is linked to the exact preservation of quadratic and linear invariants."
status: established
aliases: [symplectic integrator, symplectic method, quadratic invariants, linear invariants, geometric integration]
tags: [geometric-integration, structure-preserving, splitting, runge-kutta]
timestamp: 2026-10-20T06:18:00Z
---

# Symplecticity and quadratic-invariant preservation

The exact flow $\varphi_h$ of a Hamiltonian system is a symplectic map. A
one-step method $\psi_h$ is **symplectic** when $\psi_h$ is a symplectic map
for every Hamiltonian system and every $h$ *(definition supplied by the compiler;
the sources use the term without stating it)*. The property matters through
[backward error analysis](/methods/backward-error-analysis.md): the modified
vector field of a symplectic method is Hamiltonian, so the method has a
**modified Hamiltonian** $\tilde H$ and conserves $H$ up to $O(h^p)$ over
exponentially long times ([Blanes et al. (2024)](/sources/blanes-2024.md),
§4.4; [Farrell et al. (2021)](/sources/farrell-2021.md), §2.1).

## Which methods are symplectic

* **Splitting into Hamiltonian parts.** If $H=H^{[1]}+H^{[2]}$ and each part
  has an exactly computable flow, every composition of those flows is
  symplectic, because each flow is (Blanes et al. (2024), §1, §4.4). For
  separable $H=T(p)+V(q)$ this gives the symplectic Euler methods (Lie–Trotter,
  Eqs. (1.29)–(1.30)) and Störmer–Verlet (Strang, Algs. 1.3–1.4); see
  [operator splitting](/methods/operator-splitting.md) and
  [composition methods](/methods/composition-methods.md).
* **Gauss–Legendre RK methods** are symplectic and preserve quadratic
  invariants (Farrell et al. (2021), §3.2, §4.4.2, as recalled). Implicit
  midpoint is the one-stage case.
* **Symplectic DIRKs.** Farrell et al. (2021, Eq. (37)) use the two-stage DIRK
  $c=(\tfrac14,\tfrac34)$, $A=\begin{pmatrix}1/4&0\\1/2&1/4\end{pmatrix}$,
  $b=(\tfrac12,\tfrac12)$ (attributed to Qin and Zhang), second order,
  A-stable and symplectic. It is two implicit-midpoint half-steps in
  succession, with step $h/2$ each *(compiler check, not in the source)*.
  [Southworth et al. (2022)](/sources/southworth-2022.md) (§2.1) state that
  symplectic DIRKs are limited to order 4 and that the known ones above order
  2 have negative diagonal entries, and that neither linear multistep methods
  nor explicit RK methods can be symplectic in general for non-separable
  problems.
* **Multirate implicit midpoint.** The coupled ($m$ odd) and decoupled ($m$
  even) multirate implicit midpoint methods keep the algebraic stability,
  symmetry and symplecticity of implicit midpoint
  ([Roberts et al. (2021)](/sources/roberts-2021.md), §5.2).

Symmetry is related but distinct: a method is time-symmetric when
$\psi_h=\psi_h^*=\psi_{-h}^{-1}$; symmetric methods have even order and
modified equations in even powers of $h$ (Blanes et al. (2024), §2.1.1).
The "adjoint" and "time symmetry" of discrete adjoint computations are
different notions: there the adjoint is the transpose of the linearized time
stepping, and time symmetry means that the backward adjoint recurrence retraces
the forward solution, which relaxation methods achieve exactly on
skew-symmetric linear problems ([Bencomo & Chan (2023)](/sources/bencomo-2023.md),
§2.2.2, who flag the distinction; see
[discrete adjoints](/methods/discrete-adjoint-runge-kutta.md)).
Störmer–Verlet is both; its modified equation, computed through $h^7$ as an
additive RK method, has no odd powers of $h$
([Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md), §3.1.2).

## Invariants

* **Quadratic invariants.** Gauss–Legendre methods preserve them; cubic
  invariants require "very strong conditions" (Farrell et al. (2021), §4.4.2,
  citing Iserles–Zanna). On the BBM solitary wave the linear and quadratic
  invariants were conserved to $O(10^{-15})$ by one- and two-stage
  Gauss–Legendre, while the cubic invariant drifted to $0.9948969$ and
  $0.9999990$ of its initial value at $T=18$ (Table 2). On the mixed wave
  equation, whose energy is a quadratic invariant, Gauss–Legendre(1) and (2)
  gave $E(10)/E(0)=1$ for $h=0.1,0.5,1.0$, whereas two-stage Radau IIA gave
  $0.900$, $7.1\times10^{-4}$, $3.8\times10^{-7}$ and two-stage Lobatto IIIC
  $0.379$, $9.8\times10^{-18}$, $1.2\times10^{-20}$; the symplectic DIRK
  above matched Gauss–Legendre (Table 1, §4.3).
* **Störmer–Verlet** preserves all linear first integrals and the quadratic
  ones of the form $p^\top Cq$ (Blanes et al. (2024), §1).
* **Linear invariants under GARK.** A general GARK method does not preserve a
  linear invariant $\zeta^\top y$ of $f^{\{\mathrm f\}}+f^{\{\mathrm s\}}$; it
  does if each partition conserves it separately, or if the fast and slow
  coupling rows and weights coincide, in which case the method is a
  partitioned RK method (Roberts et al. (2021), App. C, Eq. (C.3); page-local
  vector $\zeta$).

* **Which Runge–Kutta methods.** Only symplectic Runge–Kutta methods preserve
  all quadratic invariants, and such methods "must be fully implicit" (but see
  Qualifications); no Runge–Kutta method
  preserves all polynomial invariants of degree $\ge3$
  ([Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md), §1, as recalled from
  Hairer–Lubich–Wanner). For Runge–Kutta methods symplecticity is equivalent to
  the preservation of quadratic invariants
  ([de León et al. (2025)](/sources/deleon-2025.md), §1.1). Explicit
  methods can be made to conserve one or several chosen invariants by
  [relaxation](/methods/relaxation-runge-kutta.md); see
  [entropy stability](/properties/entropy-stability.md).

## Pseudo-symplectic methods

A **pseudo-symplectic** method of order $(p,q)$, after Aubry & Chartier
(1998), is an explicit method of classical order $p$ that satisfies the
symplecticity conditions up to order $q>p$, so that its symplecticity (and
quadratic-invariant) defect is $O(h^{q+1})$ per step (de León et al.
(2025), §1.1). The cumulative numbers of pseudo-symplecticity conditions
through orders 1–6 are 1, 2, 3, 6, 12, 28 (Table 4). de León et al.
define the energy analogue,
[pseudo-energy-preserving methods](/methods/pseudo-energy-preserving-runge-kutta.md),
which need fewer conditions from order 5 on (10 and 21), and compare the two:
they behave alike on most tests, while the PEP methods conserve energy markedly
better on Hénon–Heiles (§4.1.3, Fig. 2). Their Remark 1 notes that the usual
necessity argument for symplecticity conditions relies on the independence of
elementary differentials, which is questionable on Hamiltonian systems
(as recalled).

## Energy preservation without symplecticity

Energy-preserving methods are a different class. No Runge–Kutta method is
energy preserving for every Hamiltonian system (Celledoni et al. 2009, as
recalled by de León et al. (2025), §1). The average vector field
method is a B-series method that preserves energy for Hamiltonian systems with
constant structure matrix; its modified equation to $h^4$ shows the
preservation term by term (Ketcheson & Ranocha (2023), §3.2). Explicit
midpoint conserves $\lVert y\rVert^2$ exactly on one nonlinear oscillator, and
the modifying integrator that raises its order loses the Hamiltonian structure
from $h^5$, after which its error grows faster than the plain method's
(§2.6.2). Projection or modification for accuracy can thus cost the
long-time behaviour that the structure provides.

## Long-time behaviour

For an order-$p$ symplectic splitting on a compact energy set,
$H(y_n)=H(y_0)+O(h^p)$ for $nh\le e^{h_0/(2h)}$; on integrable systems the
global error grows at most linearly in $t$, against an $O(th^p)$ energy drift
and quadratic error growth for non-symplectic methods (Blanes et al. (2024),
§4.4, Eq. (4.16), as recalled from Hairer–Lubich–Wanner, Moan, Calvo–Hairer).
Variable step sizes destroy this, because the modified equation depends on
$h$; time transformations are the remedy (§4.4, §9.10). Symplectic splittings
are the method of choice in molecular dynamics and Hamiltonian Monte Carlo,
where Störmer–Verlet and three-stage splittings tuned to minimize the energy
error at large $h$ are used (§9, §9.6).

For the wave equation the property is visible directly: Gauss–Legendre is
preferred because the damping of Radau IIA and Lobatto IIIC destroys the
energy (Farrell et al. (2021), §2.1, §4.3).

## Complex and linear-system variants

* For $iu'=Hu$ written as $q'=Hp$, $p'=-Hq$, splitting methods are not
  unitary but are conjugate to unitary maps for small $h$ (Blanes et al.
  (2024), §3.4).
* Symmetric-conjugate complex compositions satisfy $\bar\psi_h=\psi_h^{-1}$
  on problems reversible under conjugation and nearly preserve norm and
  energy; palindromic complex methods do not (§7.2, Fig. 7.1). Taking the
  real part of a complex method keeps time-symmetry and symplecticity only up
  to a finite order ($4k-1$, $4k+3$ or $4k+1$ depending on the class, §7.3).
  See [complex-coefficient splitting](/methods/complex-coefficient-splitting.md).

## Invariants built into a learned model

[Müller (2023)](/sources/muller-2023.md) builds conservation into the model instead of the
integrator: a neural-network Lagrangian made exactly invariant under rotations and translations
has, by Noether's theorem, exactly conserved momenta, and the learned equations are then advanced
by non-symplectic RK4 (§2, §3; see [learned time integrators](/methods/learned-time-integrators.md)).
The conservation is exact for the continuous learned dynamics only; the author writes that the
drift of the learned momenta "would be zero in exact arithmetic and for an exact time integrator"
and attributes the measured drift, about $10^{-5}$, to single-precision rounding without a
step-size study (§3.1.2). Since the learned momenta are nonlinear functions of the state, RK4
does not preserve them in general *(compiler remark, not in the source)*. Müller compares the
exactly conserved learned momentum, and the resulting near-conservation of the true momentum,
to the modified Hamiltonian of a symplectic method (§2.3.1, §3.1.1). The comparison is an
analogy only: the modified Hamiltonian is an invariant of the modified equation of the discrete
map, the learned momentum an invariant of a different continuous model. He also recalls that
Hamiltonian neural networks were first integrated with non-symplectic RK4 and that later
symplectic recurrent networks with Störmer–Verlet were argued to perform better (§1.1.1).

## Parallel-in-time iterations

A [Parareal](/methods/parareal.md) iterate
$U^{(k+1)}_{j+1}=\mathcal G(U^{(k+1)}_j)+\mathcal F(U^{(k)}_j)-\mathcal G(U^{(k)}_j)$ is a linear
combination of propagator values, not a composition of maps, so it does not inherit the
symplecticity of its propagators; only the converged solution, the serial fine solution, does
*(compiler remark, not in the source)*.
[Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) (Remark 5.4) state the
consequence for their particle-in-Fourier Vlasov–Poisson scheme, which conserves charge,
momentum and (before time discretization) energy: the converged Parareal solution keeps these
properties only if the Parareal tolerance is near machine precision, and a lenient tolerance
loses them; symmetric Parareal variants are left to future work. Their measurements agree
(App. A.2, Figs. 8–9):

* the energy error of Parareal iterates with a particle-in-cell coarse propagator is orders of
  magnitude above that of serial stepping and grows in early iterations, matching serial
  stepping only near convergence;
* the momentum error stays near machine precision in every iteration, independently of the
  nonuniform-FFT tolerance;
* charge conservation depends on the fine propagator's FFT tolerance.

The momentum result fits a general fact: if both propagators preserve a linear invariant
$w^\top y$, so does every Parareal iterate, because the coefficients $1,1,-1$ of the update sum to
one, so $w^\top U^{(k+1)}_{j+1}=w^\top U^{(k+1)}_j$ *(compiler check, not in the source)*. Quadratic
invariants and energy have no such property. The authors therefore choose the Parareal tolerance
so that energy and charge errors match those of serial stepping (App. A.2–A.3).

## Qualifications

* Southworth et al. (2022, §2.1) cite the order-4 limit for symplectic DIRKs
  without stating its hypotheses. Symmetric compositions of implicit midpoint
  with real weights (the triple jump of Blanes et al. (2024), §2.1.1) are
  symplectic DIRKs of any even order, with a negative weight and hence a
  negative diagonal entry *(compiler check, not in the sources)*; the
  order-4 statement presumably carries extra conditions such as positive
  diagonal entries. Not recorded as a contradiction because neither source
  states the opposite claim.
* Biswas & Ketcheson (2023, §1) write that symplectic Runge–Kutta methods
  "must be fully implicit". The symplectic DIRKs above (Farrell et al. (2021),
  Eq. (37); Southworth et al. (2022), §2.1) are diagonally implicit, so the
  defensible statement is "implicit", not "fully implicit". Loose wording in
  an introduction recalling Hairer–Lubich–Wanner, not a contested result, so
  not a contradiction.
* The long-time results assume a constant step and a compact level set; they
  are statements about the method on Hamiltonian ODEs, not about
  semi-discretized PDEs in general.
* Muralikrishnan & Speck (2025, Remark 5.4) call particle-in-Fourier "structure preserving" in
  the sense of semi-discrete conservation of charge, momentum and energy; their velocity Verlet
  time integrator does not conserve energy exactly, its energy error decreasing like $O(h^2)$
  (App. A).

# Citations

- [Blanes et al. (2024)](/sources/blanes-2024.md) — §1 (Störmer–Verlet invariants), Eqs. (1.29)–(1.30), §2.1.1 (symmetric methods), §3.4, §4.4 (modified Hamiltonian, Eq. (4.16)), §7.2–7.3, §9, §9.6, §9.10.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.1, §3.2, Eq. (37), §4.3 and Table 1 (wave energy), §4.4.2 and Table 2 (BBM invariants).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1 (symplectic DIRK and LMM limits).
- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §2.6.2, §3.1.2, §3.2 (Störmer–Verlet modified equation, AVF, explicit midpoint).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §5.2 (multirate implicit midpoint), App. C (linear invariants).
- [de León et al. (2025)](/sources/deleon-2025.md) — §1, §1.1 (pseudo-symplectic methods), Remark 1, Table 4, §4.1.3 (Fig. 2).
- [Bencomo & Chan (2023)](/sources/bencomo-2023.md) — §2.2.2 (discrete-adjoint time symmetry versus geometric adjoints).
- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §1 (quadratic and polynomial invariants of RK methods).
- [Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) — arXiv v2: Remark 5.4, App. A, A.2–A.3 (Figs. 8–9).
- [Müller (2023)](/sources/muller-2023.md) — §1.1.1, §2.1–2.3 (Noether invariants of learned Lagrangians), §3.1.1–3.1.2.
