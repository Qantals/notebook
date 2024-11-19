# examples (L23 ~ L25)

## power / recurrence
- power
    - $A^i\to \lambda _{A^i}=\lambda _A^i$ eigenvalues power likewise
        > proof: $A^ix=\lambda A^{i-1}x=\lambda ^ix$
    - $x_{A^i}=x_{A}$ eigenvectors hold stable
        > proof: $A^2=S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2S^{-1}\to A^k=S\Lambda ^kS^{-1}$
- recurrence / iteration
    - $u_{k+1}=A_{n\times n}u_k\to u_k=A^ku_0$ where $u_i$ is column vector.
    - suppose $u_0=c_1x_1+\dots +c_nx_n=Sc\to c=S^{-1}u_0$, where $x_i$ is eigenvector, $u_0$ is given.
    - $u_k=A^ku_0=S\Lambda ^kS^{-1}Sc=S\Lambda ^kc=c_1\lambda _1^kx_1+\dots +c_n\lambda _n^kx_n$, stability depends on $\lambda ^k$
- stability / trend: depends on main term
    - for $\lambda \in \mathbb{C}$, transform to argument form $\to$ power of $\lambda$ depends on modulus.
    - stable: $\lim _{k\to \infty}A^k\to 0$ if all $|\lambda _i|<1$
    - unstable: $\exists |\lambda _i|>1$: bigger eigenvalue determines the growth
- immigration example: seen Markov matrices.
- Fibonacci example
    - $F_{k+1}=F_{k}+F_{k-1}\to A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix},u_k=(F_{k+1},F_k)^T, u_0=(1,0)^T$. computation is quick through eigenvectors.
    - $F_{100}=u_{100_2}=c_1\lambda _1^{100}x_1+c_2\lambda _2^{100}x_2$
    - approximate: $\lambda _2=\frac{1-\sqrt{5}}{2}\approx-0.618,\lambda _1=\frac{1+\sqrt{5}}{2}\approx 1.618>1,x_1=(\lambda _1,1)^T,c_1=\frac{1}{\sqrt{5}}\to u_{100}\approx \frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2})^{100}\to \frac{F_{k+1}}{F_k}\approx \lambda _1\approx \frac{1+\sqrt{5}}{2}$ is golden mean.
- one-step 2nd order difference equations example
    - suppose system is steady as $t$ increases: $y''+y=0\to u=(y,y')^T=(\cos t,-\sin t)^T$ construct a circle
    - $U_n=(Y_n,Z_n)^T, Y_n$ is difference term of $y$ and $Z_n$ is difference of $y'$
    - forward form $\begin{bmatrix} Y_{n+1} \\ Z_{n+1}\end{bmatrix}=\begin{bmatrix} 1 & \Delta t \\ -\Delta t & 1\end{bmatrix}\begin{bmatrix} Y_n \\ Z_n\end{bmatrix} \to U_{n+1}=A_FU_n$ where $Z'=-Y=y''$
        - $Z_n=\frac{Y_{n+1}-Y_n}{\Delta t}, -Y_n=\frac{Z_{n+1}-Z_n}{\Delta t}\to \frac{Y_{n+1}-2Y_n+Y_{n-1}}{(\Delta t)^2}=-Y_{n-1}$
        - unstable: $\lambda =1\pm i\Delta t\to |\lambda |>1$ check the stability of $U$ rather than $y$
    - backward form $\begin{bmatrix} 1 & -\Delta t \\ \Delta t & 1\end{bmatrix}\begin{bmatrix} Y_{n+1} \\ Z_{n+1}\end{bmatrix}=\begin{bmatrix} Y_n \\ Z_n\end{bmatrix} \to A_F^TU_{n+1}=U_n$ where $A_B^{-1}=A_F^T$
        - $Z_{n+1}=\frac{Y_{n+1}-Y_n}{\Delta t}, -Y_{n+1}=\frac{Z_{n+1}-Z_n}{\Delta t}\to \frac{Y_{n+1}-2Y_n+Y_{n-1}}{(\Delta t)^2}=-Y_{n+1}$
        - too stable: $|\lambda |<1$ due to inverse
    - centered form (leapfrog method) $\begin{bmatrix} 1 & 0 \\ \Delta t & 1\end{bmatrix}\begin{bmatrix} Y_{n+1} \\ Z_{n+1}\end{bmatrix}=\begin{bmatrix} 1 & \Delta t \\ 0 & 1\end{bmatrix}\begin{bmatrix} Y_n \\ Z_n\end{bmatrix} \to U_{n+1}=A_CU_n\to \det A_C=1$
        - $Z_{n}=\frac{Y_{n+1}-Y_n}{\Delta t}, -Y_{n+1}=\frac{Z_{n+1}-Z_n}{\Delta t}\to \frac{Y_{n+1}-2Y_n+Y_{n-1}}{(\Delta t)^2}=-Y_n$
        - oscillate from circle but fit through some perioud for small $\Delta t$.
    - Trapezoidal $\begin{bmatrix} 1 & -\Delta t/2 \\ \Delta t/2 & 1\end{bmatrix}\begin{bmatrix} Y_{n+1} \\ Z_{n+1}\end{bmatrix}=\begin{bmatrix} 1 & \Delta t/2 \\ -\Delta t/2 & 1\end{bmatrix}\begin{bmatrix} Y_n \\ Z_n\end{bmatrix} \to U_{n+1}=A_TU_n$
        - $\frac{Z_{n+1}+Z_n}{2}=\frac{Y_{n+1}-Y_n}{\Delta t}, -\frac{Y_{n+1}+Y_n}{2}=\frac{Z_{n+1}-Z_n}{\Delta t}\to \frac{Y_{n+1}-2Y_n+Y_{n-1}}{(\Delta t)^2}=-\frac{Y_{n+1}+Y_{n-1}}{2}$
        - match perfectly

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
    - compute $c:u(0)=c_1x_1+\dots +c_nx_n=Sc_{n\times 1},c_{n\times 1}=S^{-1}u(0)$ where $c_i$ is scalar.
- decoupling
    - $\frac{du}{dt}=Au$, set $u=Sv\to S\frac{dv}{dt}=ASv\to \frac{dv}{dt}=S^{-1}ASv=\Lambda v$
    - $v(t)=e^{\Lambda t}v(0)\to u(t)=Se^{\Lambda t}S^{-1}u(0)=e^{At}u(0)=Se^{\Lambda t}c$ the same as above.
    - matrix exponential
        - generalize from infity series difinition: $e^{At}=I+At+\frac{1}{2}(At)^2+\dots=S(I+\Lambda t+\dots )S^{-1}=Se^{\Lambda t}S^{-1}$
        - $e^{\Lambda t}=\mathrm{diag}(e^{\lambda _1},\dots ,e^{\lambda _n})$ But $e^{At}$ can not be seen in this way, because it is made artificially.
        - $(e^{At})^{-1}=e^{-At}$ (proof: $e^{At}e^{-At}=I$)
        - $\lambda _{e^{At}}=e^{\lambda t}$
        - $A^T=-A\to (e^{At})^Te^{At}=I$ (proof: $(e^{At})^T=e^{-At}$ using definition expansion)
    - illustration for same eigenvalue results in $te^{\lambda t}:e^{At}=e^{It}e^{(A-I)t}=e^t(I+(A-I)t+0)$ due to $(A-I)^2=0$
- stability: trend concerning $\lim t\to \infty$
    - $\lambda =a+bi\in \mathbb{C},e^{\lambda t}=e^{at+ibt}=e^{at}(\cos bt+i\sin bt)\to \mathrm{Re}(\lambda )=a$ depends modulus, $\mathrm{Im}(\lambda )=b$ depends argument.
    - steady state / neutral: some $\mathrm{Re}(\lambda )=0$, others $\mathrm{Re}(\lambda )<0$
    - blow up / unstable: $\exists \mathrm{Re}(\lambda )>0$
    - decay / stable: $\forall \mathrm{Re}(\lambda )<0$
        - for $A_{2\times 2}$, stable: $\mathrm{tr}(A)<0, \det A >0$ using Vieta theorem.
- 2nd order equation transform to 2x2 system
    - $y''+by'+ky=0\to u=\begin{bmatrix}y' \\ y\end{bmatrix},u'=\begin{bmatrix}y'' \\ y'\end{bmatrix},A=\begin{bmatrix} -b & -k \\ 1 & 0\end{bmatrix}\to u'=Au$, where $A$ is companion matrix
    - eigenvalue equation $\lambda ^2+b\lambda +k=0$ is the same as solution to 2nd differential equation.
    - solution: $u(t)=(y',y)^T=c_1e^{\lambda _1t}(\lambda _1,1)^T+c_2e^{\lambda _2t}(\lambda _2,1)^T$
    - higher order: $A=\begin{bmatrix}a & b & c & d & e \\ && I_{4\times 5} &&\end{bmatrix},u=(y^{(4)};\dots y^{(0)})^T$

## Markov matrices
- $A_{n\times n}$ property:
    1. $a_{ij}\ge 0$
    2. column sum is 1
- power analysis:
    1. has eigenvalue $\lambda _1=1$
        > proof: $A-I$ all columns add to 0 $\to (1,1,1)\in N((A-I)^T)\to R(A-I)<n\to (A-I)x=0,x\ne 0\to Ax=x$  
        > or $\lambda _A=\lambda _{A^T}:A^Tx_1=x_1,x_1=(1,\dots ,1)^T$
    2. all other eigenvalue $|\lambda _i|<1$
        > proof: $A^Tx=\lambda x$, let $x_k=\max x_i\in x_{n\times 1}\to |\lambda||x_k|=|(A^Tx)_k|=|\sum _ja_{jk}v_j|\le \sum _ja_{jk}|v_j|\le |v_k|\sum _ja_{jk}=|x_k|\to |\lambda|\le 1$
    3. from 1,2: $c_1\lambda _1x_1$ become the main term in $u_k=A^ku_0$, so $x_1$ determines the value of stable state
- application - immigration
    - $u_k=(u_{k1},\dots ,u_{kn})$ means original population at time $k$.
    - $A_{n\times n},a_{ij}$ means percentage of $j$ population move to $i$, $a_{ii}$ means percentage of $i$ population stays there $\to \sum _ia_{ij}=1$
    - stable solution: already known it's stable: $\lim _{k\to \infty}u_k=u_{k-1}=u^*\to Au^*=u^*,\lambda _1=1$ and compute eigenvector $x_1\to u^*=kx_1$, constraint: scalars in $x:\sum _iu_i=\sum _iu^*_i$

## Fourier series (orthogonal functional basis)
- $f(x)=a_0+a_1\cos x+b_1\sin x+a_2\cos 2x+\dots$
- $f(x)=f(x+2\pi)$: periodic function
- analogy:
    - $f(x)$ is linear combination of orthogonal basis $\cos kx$
    - function inner product: $f^Tg=\int _0^{2\pi} f(x)g(x)dx$
        - example: $\int _0^{2\pi}\sin x\cos x=0$
    - compute series coefficients: $\int _0^{2\pi}f(x)\cos x=a_1\pi$

## review (L25)
- main, upper and lower diagonal are 1 matrices $A_n$
    - $\det A_n=\det A_{n-1}-\det A_{n-2}$ (proof: expand with first row)
    - recurrence convergence: let $\det A_n=D_n,u_k=(D_n,D_{n-1})^T,A=\begin{bmatrix} 1 & -1 \\ 1 & 0\end{bmatrix}\to u_k=Au_{k-1},\mathrm{Re}(\lambda _A)=0\to$ neutral
- upper and lower diagonal increase matrices
    - $A_4=\begin{bmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 2 & 0\\ 0 & 2 & 0 & 3 \\ 0 & 0 & 3 & 0 \end{bmatrix}=A_4^T$
    - quick guess: projection matrix is $I$ because $A_4$ is invertable
    - guess odd order is singular, even order is invertable
        > judgement: has $\lambda =0 / \det A=0$
