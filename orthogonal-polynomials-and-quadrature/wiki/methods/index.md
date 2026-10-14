# Methods

Algorithms and schemes.

* [Gaussian quadrature](/methods/gaussian-quadrature.md) — Quadrature with nodes at the zeros of the degree-n polynomial orthogonal for the weight omega and weights chosen accordingly, integrating omega times polynomials of degree up to 2n-1 exactly; the general idea and the Legendre, Chebyshev, Laguerre and Hermite rules as Riley et al. present them, with what the founding sources prove and what they only assert.
* [Gauss–Chebyshev quadrature](/methods/gauss-chebyshev-quadrature.md) — Gaussian rules for the weights (1-x^2)^{-1/2} and (1-x^2)^{1/2} on [-1,1], with closed-form nodes cos((j-1/2)pi/n), cos(j pi/(n+1)) and weights pi/n, pi/(n+1) sin^2(j pi/(n+1)); the endpoint singularity is absorbed by the weight.
* [Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md) — The n-point Gaussian rule for unit weight on [-1,1]: nodes at the zeros of P_n, weights 2/((1-x_j^2)P_n'(x_j)^2), stated exact for polynomials of degree up to 2n-1; derivation through the Lagrange interpolant, the affine map from [a,b], tabulated nodes and weights, and Riley's worked comparison with the trapezium and Simpson rules.
* [Trapezium and Simpson rules](/methods/trapezium-and-simpson-rules.md) — The equally spaced composite rules that approximate f by straight lines or parabolas on strips of width h: trapezium error about (b-a)h^2<f''>/12, exact for linear f; Simpson error about (b-a)h^4<f''''>/180, using an even number of strips; derived by Taylor expansion about strip midpoints.
