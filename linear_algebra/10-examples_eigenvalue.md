# examples (L23 ~ L25)

## power
- $A^i\to \lambda _{A^i}=\lambda _A^i$ eigenvalues power likewise
    > proof: $A^ix=\lambda A^{i-1}x=\lambda ^ix$
- $x_{A^i}=x_{A}$ eigenvectors hold stable
    > proof: $A^2=S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2S^{-1}\to A^k=S\Lambda ^kS^{-1}$
- matrix power trend: $\lim _{k\to \infty}A^k\to 0$ if all $|\lambda _i|<1$
- population
    - $A_{m\times n}, X=(x_1,\dots ,x_n)$
    - $a_{ij}$ means percentage of $j$ population move to $i$, $a_{ii}$ means percentage of $i$ population stays there.
    - $\sum _ia_{ij}=1$
    - $X_1=AX_0,\dots ,X_n=A^nX_0$
    - stable solution
        1. check $\lim _{n\to \infty}X_n=P\Lambda ^nPX_0$
        2. $\lim _{n\to \infty}X_n=X_{n-1}=X^*\to AX^*=X^*,\lambda =1\to$ get basis of eigenvector $B \to X^*=Bk$, constraint: $\sum _ix_i=\sum _ix^*_i$
- difference equation: $u_{k+1}=Au_{k}$ so $u_{k}=Au_0$, where $u_0=c_1x_1+\dots +c_nx_n=Sc$ ($c$ is column vector like $x$), $A^nu_0=c_1\lambda ^nx_1+\dots =\Lambda ^nSc$
    - Fibonacci: $A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix},u_k=\begin{bmatrix}F_{k+1} \\ F_k \end{bmatrix}$.
    - get eigenvalues then eigenvectors of $A$ (growth speed), the bigger eigenvalue determines the growth(in polynominal this is main term)
    - $u_0$ is composed of basis of eigenvectors($c_n$ needed be calculated additionally)
    - $F_k=u_{k2}$

## differential equations
- two 1st differential equations system: $A$ is coefficient matrix, form: $\frac{du_1}{dt}=a_{11}u_1+a_{12}u_2$
    - solution: $u(t)=C_1e^{\lambda _1t}x_1+C_2e^{\lambda _2t}x_2$ ($x$ is eigenvectors, each elements in $x$ match different $u$)(illusition see below *decoupling* part)
    - stability ($u(t)\to 0$): $\mathbb{Re}\{\lambda \} <0$ (imaginary part has constant model 1, from Euler's rule)
    - steady state: $\lambda _1=0$, other $\mathbb{Re}\{\lambda \} <0$
    - blow up: any $\mathbb{Re}\{\lambda \} >0$
- decoupling (about original equations system, so no need to compute multi-functions): $\frac{du}{dt}=Au$, set $u=Sv$, so $S\frac{dv}{dt}=ASv\to \frac{dv}{dt}=S^{-1}ASv=\Lambda v$. (because $S\Lambda S^{-1}=A$ , see below to meet the "coincidence")
    - $v(t)=e^{\Lambda t}v(0)\to u(t)=Se^{\Lambda t}S^{-1}u(0)=e^{At}u(0)$
    - $e^{At}=I+At+\frac{(At)^2}{2}+\dots=SS^{-1}+S\Lambda S^{-1}t+\dots =Se^{\Lambda t}S^{-1}$ (Taylor series)(condition: can be diagonalized)
    - note:
        - $e^{\Lambda t}=$ diagonal matrix with $e^{\lambda t}$ elements. But $e^{At}$ can not be seen in this way, because it is made artificially.
        - $u(t)=Se^{\Lambda t}S^{-1}u(0)=Se^{\Lambda t}C=C_ne^{\lambda _n}x_n$
- one 2nd order equation: to $2\times 2$ 1st order system: $y''+by'+ky=0\to u=[y';y],u'=[y'';y']=[-b\ -k;1\ 0]u$
    - higher order: $u'=[a\ b\ c\ d\ e;I]u,u=[y^{(4)};\dots y^{(0)}]$

