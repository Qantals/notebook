# examples (L23 ~ L25)

## power / recurrence
- power
    - $A^i\to \lambda _{A^i}=\lambda _A^i$ eigenvalues power likewise
        > proof: $A^ix=\lambda A^{i-1}x=\lambda ^ix$
    - $x_{A^i}=x_{A}$ eigenvectors hold stable
        > proof: $A^2=S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2S^{-1}\to A^k=S\Lambda ^kS^{-1}$
- recurrence - population example
    - $x=(x_1,\dots ,x_n)$ means original population.
    - $A_{n\times n},a_{ij}$ means percentage of $j$ population move to $i$, $a_{ii}$ means percentage of $i$ population stays there $\to \sum _ia_{ij}=1$
    - $x_1=Ax_0\to x_n=A^nx_0$
    - stable solution
        1. check $\lim _{n\to \infty}x_n=S\Lambda ^nS^{-1}x_0$
        2. already known it's stable: $\lim _{n\to \infty}x_n=x_{n-1}=x^*\to Ax^*=x^*,\lambda _1=1$ and compute eigenvector $s_1\to x^*=ks_1$, constraint: scalars in $x:\sum _ix_i=\sum _ix^*_i$
- recurrence - Fibonacci example
    - $u_{k+1}=A_{n\times n}u_k,u_k=A^ku_0$ where $u_i$ is column vector.
    - suppose $u_0=c_1x_1+\dots +c_nx_n=Sc\to c=S^{-1}u_0$, where $x_i$ is eigenvector, $u_0$ is given.
    - $u_k=A^ku_0=S\Lambda ^kS^{-1}Sc=S\Lambda ^kc=c_1\lambda _1^kx_1+\dots +c_n\lambda _n^kx_n$
    - Fibonacci: $F_{k+1}=F_{k}+F_{k-1}\to A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix},u_k=(F_{k+1},F_k)^T, u_0=(1,0)^T$. computation is quick through eigenvectors.
    - $F_{100}=u_{100_2}=c_1\lambda _1^{100}x_1+c_2\lambda _2^{100}x_2$
    - approximate: $\lambda _2=\frac{1-\sqrt{5}}{2}\approx-0.618,\lambda _1=\frac{1+\sqrt{5}}{2}\approx 1.618>1,x_1=(\lambda _1,1)^T,c_1=\frac{1}{\sqrt{5}}\to u_{100}\approx \frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2})^{100}\to \frac{F_{k+1}}{F_k}\approx \lambda _1\approx \frac{1+\sqrt{5}}{2}$ is golden mean.
- stability / trend: depends on main term
    - for $\lambda \in \mathbb{C}$, transform to argument form $\to$ power of $\lambda$ depends on modulus.
    - $\lim _{k\to \infty}A^k\to 0$ if all $|\lambda _i|<1$
    - for $\exists |\lambda _i|>1$: bigger eigenvalue determines the growth

## differential equations
- preliminary
    - linear differential equation: $a_n(x)y^{(n)}+\dots +a_1(x)y'+a_0y=f(x)$, homogeneous means $f(x)=0$
    - linear constant coefficients differential equation: $a_ny^{(n)}+\dots +a_1y'+a_0y=f(x)$
    - linear differential equation solution has linearity: additivity and homogeneity, complete solution = particular + homogeneous general.
- ordinary differential equation solution: $\frac{\mathrm{d}u}{\mathrm{d}t}=\lambda u\to u(t)=Ce^{\lambda t}=u(0)e^{\lambda t}$ where $u$ is scalar variable.
- linear constant coefficients homogeneous differential equations system
    - $\frac{\mathrm{d}u}{\mathrm{d}t}=A_{n\times n}u_{n\times 1}\to$ one possible solution $u(t)=e^{\lambda _it}x_{i(n\times 1)}$ where $x_i$ is eigenvector of $\lambda _i$
    - complete solution: $u(t)=c_1e^{\lambda _1t}x_1+\dots +c_ne^{\lambda _nt}x_n$
        - condition: all $\lambda$ are **different**.
    - compute $c_{n\times 1}:u(0)=c_1x_1+\dots +c_nx_n=Sc,c_{n\times 1}=(c_1,\dots ,c_n)^T=S^{-1}u(0)$ where $c_i$ is scalar.
- stability: trend concerning $\lim t\to \infty$
    - $\lambda =a+bi\in \mathbb{C},e^{\lambda t}=e^{at+ibt}=e^{at}(\cos bt+i\sin bt)\to \mathrm{Re}\{\lambda \}=a$ depends modulus, $\mathrm{Im}\{\lambda \}=b$ depends argument.
    - steady state / neutral: some $\mathrm{Re}\{\lambda \}=0$, others $\mathrm{Re}\{\lambda \}<0$
    - blow up / unstable: $\exists \mathrm{Re}\{\lambda \}>0$
    - decay / stable: $\forall \mathrm{Re}\{\lambda \}<0$
        - for $A_{2\times 2}$, stable: $\mathrm{tr}(A)<0, \det A >0$ using Vieta theorem.
- 2nd order equation transform to 2x2 system
    - $y''+by'+ky=0\to u=\begin{bmatrix}y' \\ y\end{bmatrix},u'=\begin{bmatrix}y'' \\ y'\end{bmatrix},A=\begin{bmatrix} -b & -k \\ 1 & 0\end{bmatrix}\to u'=Au$, where $A$ is companion matrix
    - eigenvalue equation $\lambda ^2+b\lambda +k=0$ is the same as solution to 2nd differential equation.
    - solution: $u(t)=(y',y)^T=c_1e^{\lambda _1t}(\lambda _1,1)^T+c_2e^{\lambda _2t}(\lambda _2,1)^T$
    - higher order: $A=\begin{bmatrix}a & b & c & d & e \\ && I_{4\times 5} &&\end{bmatrix},u=(y^{(4)};\dots y^{(0)})^T$
- difference equations
- decoupling (about original equations system, so no need to compute multi-functions): $\frac{du}{dt}=Au$, set $u=Sv$, so $S\frac{dv}{dt}=ASv\to \frac{dv}{dt}=S^{-1}ASv=\Lambda v$. (because $S\Lambda S^{-1}=A$ , see below to meet the "coincidence")
    - $v(t)=e^{\Lambda t}v(0)\to u(t)=Se^{\Lambda t}S^{-1}u(0)=e^{At}u(0)$
    - $e^{At}=I+At+\frac{(At)^2}{2}+\dots=SS^{-1}+S\Lambda S^{-1}t+\dots =Se^{\Lambda t}S^{-1}$ (Taylor series)(condition: can be diagonalized)
    - note:
        - $e^{\Lambda t}=$ diagonal matrix with $e^{\lambda t}$ elements. But $e^{At}$ can not be seen in this way, because it is made artificially.
        - $u(t)=Se^{\Lambda t}S^{-1}u(0)=Se^{\Lambda t}C=C_ne^{\lambda _n}x_n$


