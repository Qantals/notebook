# eigenvalue and eigenvector

## eigenvalues, eigenvectors
- $A_{n\times n}x\parallel x:Ax=\lambda x$, get all $\lambda (x\ne 0)$
- special eigenvalues
    - upper triangle matrix: $\lambda _U=\text{diag}(U)$ (proof: use eigenvalue equation)
    - $A$ is singular $\Leftrightarrow \lambda _i=0$ is one eigen value; $A$ is invertable $\Leftrightarrow \lambda _A\ne 0$
        > proof: $Ax=0=0x,x\ne 0, \det A=\prod \lambda _i$
    - $A^2=A\Rightarrow \lambda _A=0,1$
        > proof: $Ax=\lambda x=A^2x=A(\lambda x)=\lambda Ax=\lambda ^2x\to \lambda ^2-\lambda =0$
    - projection matrix: $Px=x\to \lambda =1;Px=0\to \lambda =0$
    - permutation matrix: $A=\begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix},x=\begin{bmatrix} 1 \\ 1\end{bmatrix}\to \lambda =1;x=\begin{bmatrix}-1 \\ 1\end{bmatrix}\to \lambda =-1$.
        > generalization: $A_1=\begin{bmatrix} a & s-a \\ b & s-b\end{bmatrix},x_1=\begin{bmatrix} 1 \\ 1\end{bmatrix},\to Ax_1=sx_1$ row sum is equal $\to$ row sum is one eigen value;  
        > $A_2=\begin{bmatrix} a & a-d \\ b & b-d \end{bmatrix},x_2=\begin{bmatrix} 1 \\ -1 \end{bmatrix}\to A_2x_2=dx_2$ row difference is equal $\to$ row difference is one eigen value
- eigenvalue equation
    - $Ax=\lambda x\to (\lambda I-A)x=0(x\ne 0)\to \det (\lambda I-A)=0$ get all $\lambda$
    - $x_i\in V_{\lambda _i}=N(\lambda _iI-A)$
        > proof: $Ax=\lambda x\to A(kx)=kAx=(k\lambda )x$  
        > $Ax_1=\lambda x_1,Ax_2=\lambda x_2\to A(x_1+x_2)=\lambda x_1+\lambda x_2=\lambda (x_1+x_2)$ including $x=0$
    - algebratic multiplicity $k_i$: $(\lambda -\lambda _i)^{k_i}=0$
    - geometry multiplicity = #eigenvectors $=\dim N(\lambda _iI-A)$
- eigenvalue polynomial $f_A(\lambda )$
    - $A_{n\times n}$ has $n$ eigen values (allow repetition: degenerate matrix)
    - forms
        - factorization: $f_A(\lambda )=a_n(\lambda -\lambda _1)\dots (\lambda -\lambda _n)=a_n(\lambda -\lambda _1)^{k_1}\dots (\lambda -\lambda _r)^{k_r}$
        - expansion: $f_A(\lambda )=a_n\lambda ^n+a_{n-1}\lambda ^{n-1}+\dots +a_1\lambda +a_0$
        - determinants: $f_A(\lambda )=\det (\lambda I-A)$
    - Vieta theorem
        > check expansion of factorization: use **binomial theorem**  
        > check expansion of determinants: use big formula
        > 1. one term has all diagonal elements except for one factor, but that line only has diagonal element to choose, so this term has all diagonal elements.
        > 2. some terms have all diagonal elements except for two factors, so this time they has two element that is not diagonal element to choose. (so $\lambda ^{n-1}$ **must exist** in all diagonal elements term)
        > 3. for the term has all diagonal elements, every factor of product is $(\lambda -a_{ii})$, so use **binomial theorem** to expand.
        - $a_n=1$
        - $a_{n-1}=-\sum _{i=1}^n a_{ii}=-\text{tr}(A)=-a_n\sum _{i=1}^n\lambda _i$
        - $a_0=f_A(0)=\det (-A)=(-1)^n\det A=(-1)^na_n\prod _{i=1}^n\lambda _i$
- relation between eigen and matrix: not like linear function (unless $B$ is multiple of identity matrix).
    - if $Ax=\lambda x,By=\alpha y\to (A+B)x=(\lambda +\alpha)x$ is wrong: $x,y$ these eigenvectors are different.
- rotation matrix: $Q=\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$, orthogonal matrix.
    - complex eigenvalues are conjugate
    - symmetric / close symmetric matrix has real eigenvalues; $Q^T=-Q$: anti-symmetric, has pure imaginary eigenvalues.
    - real symmetric matrix has orthogonal eigenvectors with different eigenvalues.

## diagonalize
- diagonalize
    - eigenvectors: $S=(x_1,\dots ,x_n)$ where $S$ is **independent**
    - diagonal eigenvalues matrix: $AS=[\lambda_1x_1\ \dots \lambda_nx_n]=S\Lambda$, $\Lambda _{n\times n}=\mathrm{diag}(\lambda _1,\dots ,\lambda _n)$
    - similarity: $A\sim \Lambda: S^{-1}AS=\Lambda$, $A=S\Lambda S^{-1}\to \lambda _A=\mathrm{diag}(\Lambda)$
- independence
    1. different eigenvalues corresponding to eigenvectors are independent.
        > proof: use mathematical induction, for $A, \Lambda _{s\times s}=\mathrm{diag}(\lambda _1,\dots ,\lambda _s)$ has different eigenvalues, $X_{n\times s}=(x_1,\dots ,x_s)$ are their one eigenvector, $k_{s\times 1}=(k_1,\dots ,k_s)^T, Xk=0=AXk=X\Lambda k=\lambda _sXk\to X(\Lambda -\lambda _sI)k=0$, from induction: $R(X_{n\times (s-1)})=s-1\to k=(0,\dots ,0,k_s)\to k_sx_s=0, x_s\ne 0\to k_s=0\to k=0\to R(X_{n\times s})=s$
    2. $\Rightarrow$ different eigenvalues corresponding to basis set are independent.
- requirement
    1. diagonalized $\Leftrightarrow A$ has $n$ independent eigenvectors. (proof: $S$ is independent)
    2. diagonalized $\Leftarrow A$ has $n$ different eigenvalues. (proof: see independence illustration 1)
    3. diagonalized $\Leftrightarrow$ for all eigenvalues: algebratic multiplicity = geometry multiplicity. (proof: see independence illustration 2)
- order: $x_i$ should match $\lambda _i$, preserve order in $\Lambda ,S$
- unique
    - $S$ is not unique due to eigenvectors is chosen in space.
    - regardless order, $\Lambda$ is unique.
- If eigenvalues are different, $A$ has $n$ independent eigenvectors(diagonalizable). Otherwise it may (not) has $n$ independent eigenvectors.

## real symmetric matrix case
- modulus of complex vector: $(x,\bar{x})=\bar{x}^Tx=\bar{x_1}x_1+\dots=\sum |x_n|^2=\left \| x \right \|^2$
- real symmetric matrix $A^T=A,\bar{A}=A$
    - can be diagonalized (spectral theorem)
- eigenvalues are real
    > proof: $Ax=\lambda x\mathrm{\ (a)}\to \text{(conjugate)} A\bar{x}=\bar{\lambda}\bar{x}(A=\bar{A})\mathrm{\ (b)}\to \text{(transpose)} \bar{x}^TA=\bar{\lambda}\bar{x}^T\mathrm{\ (c)}$;  
    > (a) left multiply $\bar{x}^T:\bar{x}^TAx=\lambda\bar{x}^Tx$  
    > (c) right multiply $x:\bar{x}^TAx=\bar{\lambda}\bar{x}^Tx$  
    > $\to \lambda=\bar{\lambda}$
- different eigenvalues corresponding to eigenvectors are orthogonal
    > proof: suppose $Ax_1=\lambda _1x_1,Ax_2=\lambda _2x_2\to$ transpose: $x_1^TA=\lambda _1x_1^T\to$ right multiply $x_2:x_1^T(Ax_2)=\lambda _1x_1^Tx_2=x_1^T\lambda _2x_2\to (\lambda _1-\lambda _2)x_1^Tx_2=0, \lambda _1\ne \lambda _2\to x_1\perp x_2$
    - $A=Q\Lambda Q^{-1}=Q\Lambda Q^T=A^T$ ($Q$ has done normalization)
    - spectral theorem: every symmetric matrix is a combination of orthogonal projection matrices (relative to oblique projection).
        - $A=\lambda _1q_1q_1^T+\dots +\lambda _nq_nq_n^T$
        - $P=\frac{qq^T}{q^Tq}=qq^T, P^T=P,P^n=P$
- ** #signs of pivots (through elimination) are the same as #signs of eigenvalues (to judge stability of power)

## power
- $A^i\to \lambda _{A^i}=\lambda _A^i$ eigenvalues power likewise
    > proof: $A^ix=\lambda A^{i-1}x=\lambda ^ix$
- $x_{A^i}=x_{A}$ eigenvectors hold stable
    > proof: $A^2=S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2S^{-1}\to A^k=S\Lambda ^kS^{-1}$
- matrix power trend: $\lim _{k\to \infty}A^k\to 0$ if all $|\lambda _i|<1$
- difference equation: $u_{k+1}=Au_{k}$ so $u_{k}=Au_0$, where $u_0=c_1x_1+\dots +c_nx_n=Sc$ ($c$ is column vector like $x$), $A^nu_0=c_1\lambda ^nx_1+\dots =\Lambda ^nSc$
    - Fibonacci: $A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix},u_k=\begin{bmatrix}F_{k+1} \\ F_k \end{bmatrix}$.
    - get eigenvalues then eigenvectors of $A$ (growth speed), the bigger eigenvalue determines the growth(in polynominal this is main term)
    - $u_0$ is composed of basis of eigenvectors($c_n$ needed be calculated additionally)
    - $F_k=u_{k2}$