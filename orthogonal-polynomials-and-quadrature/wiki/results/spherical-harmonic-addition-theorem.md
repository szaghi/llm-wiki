---
type: Result
title: "Spherical harmonic addition theorem"
description: "P_l(cos gamma) = 4 pi/(2l+1) sum_m Y_l^m(Omega) [Y_l^m(Omega')]^*, with gamma the angle between two directions; proved in Riley et al. from the closure relation and the rotation closure of each degree-l subspace; Arfken et al. defer it beyond the chapters read."
status: established
aliases: [addition theorem for spherical harmonics, Legendre addition theorem, Unsöld theorem]
tags: [spherical-harmonics, sphere, addition-theorem, multipole]
timestamp: 2026-10-14T00:00:00Z
---

# Spherical harmonic addition theorem

## Statement

For two directions $\Omega=(\theta,\phi)$ and $\Omega'=(\theta',\phi')$
separated by the angle $\gamma$,
$$\cos\gamma=\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi'),$$
$$P_\ell(\cos\gamma)=\frac{4\pi}{2\ell+1}\sum_{m=-\ell}^{\ell}Y_\ell^m(\theta,\phi)\,\big[Y_\ell^m(\theta',\phi')\big]^*$$
([Riley et al. (2006)](/sources/riley-2006.md), §18.3, eqs. 18.49–18.50,
p. 594, called there "the most important relationship obeyed by the
$Y_\ell^m$" after orthonormality). The theorem holds as written for the
[spherical harmonics](/definitions/spherical-harmonics.md) of either founding
source, since their $Y_\ell^m$ coincide; it involves only products
$Y_\ell^m(Y_\ell^m)^*$, which are unchanged by any $m$-dependent phase
(compiler's remark).

## Proof (Riley et al.)

1. **Closure.** Inserting the coefficients of the Laplace series into the
   series gives
   $\sum_{\ell m}Y_\ell^m(\Omega)\big(Y_\ell^m(\Omega')\big)^*=\delta(\Omega-\Omega')$,
   with $\int_{4\pi}\delta(\Omega)\,d\Omega=1$ (eq. 18.51, p. 594).
2. **Legendre expansion of the delta.** $\delta(\Omega-\Omega')$ depends only
   on $\gamma$, so $\delta=\sum_\ell b_\ell P_\ell(\cos\gamma)$; integrating
   over a full azimuth about $\Omega'$ turns the Legendre coefficient into a
   solid-angle integral and gives $b_\ell=(2\ell+1)/4\pi$ (eq. 18.52,
   p. 595). Hence
   $\sum_{\ell m}Y_\ell^m(\Omega)(Y_\ell^m(\Omega'))^*=\sum_\ell\frac{2\ell+1}{4\pi}P_\ell(\cos\gamma)$
   (eq. 18.53).
3. **Term-by-term equality in $\ell$.** A rigid rotation maps each
   $Y_\ell^m$ to a combination of the $Y_\ell^{m'}$ of the same $\ell$.
   Choosing the new polar axis along $\Omega'$,
   $P_\ell(\cos\gamma)=\sqrt{4\pi/(2\ell+1)}\,Y_\ell^0(\bar\Omega)$ is a
   combination of degree-$\ell$ harmonics of $\Omega$ only, so both sides of
   step 2 can be matched degree by degree (p. 595).

The argument in step 3 shows that each side is a degree-$\ell$ combination;
the proof then equates the two sums "term by term in $\ell$" by the
uniqueness of the expansion in the orthogonal $Y_\ell^m$, which Riley et al.
leave implicit (compiler's reading of p. 595).

## Arfken et al.

[Arfken et al. (2013)](/sources/arfken-2013.md) do not state the addition
theorem in the sections read. §15.5 establishes its ingredients, the
completeness of the Laplace series (eq. 15.144, p. 761) and the closure of
each fixed-$\ell$ space under rotation (eq. 15.147, p. 763), and defers
"formulas involving products of three spherical harmonics and the detailed
behavior … under coordinate rotations" to chapter 16 (p. 765), which this
bundle did not read. The theorem therefore rests on one founding source.

## Consequences

* **Sum rule.** At $\Omega=\Omega'$, $\gamma=0$ and $P_\ell(1)=1$ give
  $\sum_m|Y_\ell^m(\theta,\phi)|^2=(2\ell+1)/4\pi$, independent of
  direction. Riley et al. set this as Exercise 18.1 (pp. 640–641), verified
  for $\ell\le2$ and stated "true for any $\ell$", without linking it to the
  theorem (the link is the compiler's).
* **Multipole expansion in three dimensions.** Combined with the
  [Legendre expansion of the inverse distance](/results/legendre-expansion-of-inverse-distance.md),
  it separates $1/|\mathbf r-\mathbf r'|$ into products of functions of
  $\Omega$ and of $\Omega'$:
  $\frac1{|\mathbf r-\mathbf r'|}=\sum_{\ell,m}\frac{4\pi}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}Y_\ell^m(\Omega)\big(Y_\ell^m(\Omega')\big)^*$.
  Neither founding source writes this combined formula in the sections read;
  it is the compiler's substitution of one stated result into the other
  (hypothesis-grade as a citation, exact as algebra).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.3, eqs. 18.49–18.53, pp. 594–595; Exercise 18.1, pp. 640–641.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §15.5, eqs. 15.144, 15.147, pp. 761–765 (ingredients only).
