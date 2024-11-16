# eigenvalue and eigenvector

## eigenvalues, eigenvectors
- $Ax\parallel x:Ax=\lambda x$, get all $\lambda (x\ne 0)$
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
- $S=[x_1,\dots ,x_n]$ where $S$ is **independent**
- $AS=[\lambda_1x_1\ \dots \lambda_nx_n]=S\Lambda$, $\Lambda _{n\times n}=\mathrm{diag}(\lambda _1,\dots ,\lambda _n)$
- $A\sim \Lambda: S^{-1}AS=\Lambda$, $A=S\Lambda S^{-1}\to \lambda _A=\mathrm{diag}(\Lambda)$
- If eigenvalues are different, $A$ has $n$ independent eigenvectors(diagonalizable). Otherwise it may (not) has $n$ independent eigenvectors.

## power
- $A^2\to \lambda _{A^2}=\lambda _A^2$
    > proof: $A^2x=\lambda Ax=\lambda ^2x$
- $x_{A^i}=x_{A}$ eigenvectors hold stable
    > proof: $A^2=S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2S^{-1}\to A^k=S\Lambda ^kS^{-1}$
- matrix power trend: $\lim _{k\to \infty}A^k\to 0$ if all $|\lambda _i|<1$

- difference equation: $u_{k+1}=Au_{k}$ so $u_{k}=Au_0$, where $u_0=c_1x_1+\dots +c_nx_n=Sc$ ($c$ is column vector like $x$), $A^nu_0=c_1\lambda ^nx_1+\dots =\Lambda ^nSc$
    - Fibonacci: $A=\begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix},u_k=\begin{bmatrix}F_{k+1} \\ F_k \end{bmatrix}$.
    - get eigenvalues then eigenvectors of $A$ (growth speed), the bigger eigenvalue determines the growth(in polynominal this is main term)
    - $u_0$ is composed of basis of eigenvectors($c_n$ needed be calculated additionally)
    - $F_k=u_{k2}$