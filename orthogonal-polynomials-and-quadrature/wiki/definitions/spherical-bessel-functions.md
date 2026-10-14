---
type: Definition
title: "Spherical Bessel functions"
description: "The radial solutions j_l, y_l (and Hankel combinations h_l) of the Helmholtz equation in spherical coordinates, sqrt(pi/2x) times Bessel functions of order l+1/2; elementary closed forms, Rayleigh formulae, recurrences, small- and large-argument limits, orthogonality on [0,a] with weight r^2, and the modified functions i_l, k_l."
status: established
aliases: [spherical Neumann functions, spherical Hankel functions, Rayleigh formulae, modified spherical Bessel functions]
tags: [bessel, spherical-bessel, sphere, special-functions]
timestamp: 2026-10-14T00:00:00Z
---

# Spherical Bessel functions

## Definition

Separating the Helmholtz equation $(\nabla^2+k^2)u=0$ in spherical polar
coordinates gives the radial equation
$r^2R''+2rR'+[k^2r^2-\ell(\ell+1)]R=0$; with $R=r^{-1/2}S$ it becomes
Bessel's equation of order $\ell+\tfrac12$ in $x=kr$. The **spherical Bessel
functions** are
$$j_\ell(x)=\sqrt{\frac{\pi}{2x}}\,J_{\ell+1/2}(x),\qquad y_\ell(x)=\sqrt{\frac{\pi}{2x}}\,Y_{\ell+1/2}(x),\qquad h_\ell^{(1,2)}=j_\ell\pm iy_\ell$$
([Riley et al. (2006)](/sources/riley-2006.md), §18.6, eqs. 18.101–18.103,
pp. 614–615; [Arfken et al. (2013)](/sources/arfken-2013.md), §14.7,
eqs. 14.148–14.151, pp. 698–699). **Naming:** Riley et al. write $n_\ell$
for the second kind, Arfken et al. $y_n$; the definitions are identical and
the registry uses $y_\ell$. Since $Y_{\ell+1/2}=(-1)^{\ell+1}J_{-\ell-1/2}$
for integer $\ell$, $y_\ell=(-1)^{\ell+1}j_{-\ell-1}$ (Riley et al., p. 607;
Arfken et al., eq. 14.152, p. 699).

## Closed forms

$$j_0=\frac{\sin x}{x},\quad y_0=-\frac{\cos x}{x},\quad j_1=\frac{\sin x}{x^2}-\frac{\cos x}{x},\quad y_1=-\frac{\cos x}{x^2}-\frac{\sin x}{x},$$
$$j_2=\Big(\frac3{x^3}-\frac1x\Big)\sin x-\frac{3}{x^2}\cos x,\qquad h_0^{(1)}=-\frac{i}{x}e^{ix}$$
(Riley et al., eqs. 18.104–18.105, p. 615, and p. 616; Arfken et al.,
eqs. 14.157–14.168, pp. 701–702). All $j_\ell$, $y_\ell$ are elementary:
the **Rayleigh formulae**
$$j_\ell(x)=(-1)^\ell x^\ell\Big(\frac1x\frac{d}{dx}\Big)^{\ell}\frac{\sin x}{x},\qquad y_\ell(x)=-(-1)^\ell x^\ell\Big(\frac1x\frac{d}{dx}\Big)^{\ell}\frac{\cos x}{x}$$
(Riley et al., eq. 18.106, p. 616, written as one formula for
$f_\ell=j_\ell$ or $n_\ell$ in terms of $f_0$; Arfken et al., eqs.
14.173–14.176, p. 703, by induction). Arfken et al. also give
$h_\ell^{(1)}$ as a terminating sum, $(-i)^{\ell+1}\frac{e^{ix}}x\sum_{s=0}^\ell\frac{i^s(\ell+s)!}{s!(2x)^s(\ell-s)!}$,
from the terminating Hankel asymptotic series (eq. 14.162, p. 702).

## Recurrences and limits

For $f_\ell$ any of $j_\ell,y_\ell,h_\ell^{(1)},h_\ell^{(2)}$
([Arfken et al. (2013)](/sources/arfken-2013.md), eqs. 14.169–14.172,
p. 702; Riley et al. derive the third, eq. on p. 616):
$$f_{\ell-1}+f_{\ell+1}=\frac{2\ell+1}{x}f_\ell,\qquad \ell f_{\ell-1}-(\ell+1)f_{\ell+1}=(2\ell+1)f_\ell',\qquad \frac{d}{dx}\big[x^{-\ell}f_\ell\big]=-x^{-\ell}f_{\ell+1}.$$
Small $x$: $j_\ell\approx x^\ell/(2\ell+1)!!$, $y_\ell\approx-(2\ell-1)!!/x^{\ell+1}$;
large $x$: $j_\ell\sim\sin(x-\ell\pi/2)/x$, $y_\ell\sim-\cos(x-\ell\pi/2)/x$,
valid for $x\gg\ell(\ell+1)/2$ (Arfken et al., eqs. 14.177–14.182,
p. 703, with footnote 9 giving the sharper small-$x$ condition for $j_\ell$).
$j_\ell$, $y_\ell$ describe standing spherical waves and $h_\ell^{(1)}$
($h_\ell^{(2)}$) outgoing (incoming) waves for time dependence $e^{-i\omega t}$
(p. 703).

## Orthogonality and zeros

The positive zeros of $j_\ell$ are those of $J_{\ell+1/2}$, i.e.
$\alpha_{\ell+1/2,p}$, $p=1,2,\dots$ (Arfken et al. write $\alpha_{np}$).
With them,
$$\int_0^a j_\ell\Big(\alpha_{\ell+1/2,p}\frac ra\Big)j_\ell\Big(\alpha_{\ell+1/2,q}\frac ra\Big)r^2\,dr=\frac{a^3}{2}\big[j_{\ell+1}(\alpha_{\ell+1/2,p})\big]^2\delta_{pq}$$
([Arfken et al. (2013)](/sources/arfken-2013.md), eq. 14.183, p. 704), the
weight $r^2$ being uniform weight over the ball. Riley et al. state only that
the orthogonality "follow[s] directly" from that of $J_\nu$ (p. 616). Arfken
et al. tabulate the first five zeros of $j_0,\dots,j_5$ and of their
derivatives (Table 14.2, p. 704; the zeros of $j_0$ are $p\pi$) and add an
orthogonality in the index on the whole line,
$\int_{-\infty}^\infty j_mj_n\,dx=\frac{\pi}{2n+1}\delta_{mn}$, proof set as
exercises (eqs. 14.190–14.191, p. 706).

## Modified spherical Bessel functions

For the radial equation with $-k^2$, Arfken et al. define
$i_\ell=\sqrt{\pi/2x}\,I_{\ell+1/2}$ and $k_\ell=\sqrt{2/\pi x}\,K_{\ell+1/2}$,
noting the different prefactor of $k_\ell$; $i_0=\sinh x/x$,
$k_0=e^{-x}/x$, $i_\ell\sim e^x/2x$, $k_\ell\sim e^{-x}/x$
(eqs. 14.193–14.198, pp. 706–708). Riley et al. do not treat them.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.6, eqs. 18.101–18.106, pp. 614–616.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §14.7, eqs. 14.148–14.198, pp. 698–708; Table 14.2, p. 704.
