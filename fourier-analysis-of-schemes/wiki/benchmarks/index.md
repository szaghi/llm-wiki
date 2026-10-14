# Benchmarks

Standard test problems.

* [Exponential-decay test equation](/benchmarks/exponential-decay-test-equation.md) — The initial-value problem dy/dt = -y, y(0) = 1, with exact solution exp(-t), used to compare forward Euler at several steps and Milne's two-step method against the exact values and to exhibit oscillation, divergence and parasitic growth of difference schemes.
* [Sawtooth wave](/benchmarks/sawtooth-wave.md) — The odd, period-L function equal to x on -L/2 < x < L/2, with a jump of size L at the period ends; its sine coefficients alternate in sign and decay only as 1/m, and it tests convergence to the mean at a jump, the persistent overshoot, failed term-by-term differentiation and successful term-by-term integration.
* [Square wave](/benchmarks/square-wave.md) — The odd, period-T function equal to -1 on the first half-period and +1 on the second; its Fourier series contains only odd sine harmonics with amplitudes 4/(pi m), and it serves as the test function for convergence at a jump (to 0), the Gibbs overshoot (quantified on it as about 18% of the half-jump), and Parseval's power partition.
