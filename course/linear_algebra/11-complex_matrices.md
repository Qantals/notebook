# complex matrices (L27)

## complex number review
- $z=a+bi$
- modulus - the same as complex vector
    - $z\bar{z}=|z|^2=a^2+b^2$
    - $z\bar{z}=1\Leftrightarrow |z|=1\Leftrightarrow \bar{z}=\frac{1}{z}$
    - $||z_1|-|z_2||\le |z_1\pm z_2|\le |z_1|+|z_2|$ (triangle inequality)
    - $|z_1z_2|=|z_1||z_2|$
        > proof: $|z_1z_2|^2=(z_1z_2)(\overline{z_1z_2})=z_1z_2\bar{z_1}\bar{z_2}=|z_1|^2|z_2|^2$
- conjugate
    - $\overline{(z_1\pm z_2)}=\bar{z_1}\pm \bar{z_2}$
    - $\overline{z_1z_2}=\bar{z_1}\bar{z_2}$
        > proof: $\overline{a_1a_2-b_1b_2+i(a_1b_2+a_2b_1)}=(a_1-ib_1)(a_2-ib_2)$
    - $\mathrm{Re}(z)=\frac{z+\bar{z}}{2},\mathrm{Im}(z)=\frac{z-\bar{z}}{2i}$
- argument form: easily compute $z_1z_2$
    - complex numbers multiplication is scale and rotation transformation originally.
    - exponent benefit: $f(z)=e^a(\cos b+i\sin b)\to f(z_1+z_2)=f(z_1)f(z_2)$ (side: logarithm has $f(x_1)+f(x_2)=f(x_1x_2)$)
    - Euler's formula: Taylor expansion of exponent with imaginary number and trigonometric functions. Taylor expansion of $\sin ,\cos$ have even or odd terms dividely and swaps signs every other term, meet the need of Taylor expansion of imaginary exponent of natural constant which swaps signs due to power of imaginary unit.
    - result: expand trigonometric functions and exponential functions to complex field.
    - give me vector $z=a+bi\to$ polar coordinate expression $z=r(\cos \theta +i\sin \theta)\to$ complex exponent expression $z=re^{i\theta}$
    - $e^{i\theta}=\overline{e^{-i\theta}}$
    - $\cos \theta=\frac{e^{i\theta}+e^{-i\theta}}{2}, \sin \theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}$

## complex matrix
- $z=(z_1,\dots ,z_n)^T\in \mathbb{C^n}$
- modulus: $(z,z)=\bar{z}^Tz=z^Hz= \| z \|^2=\sum _i|z_i|^2$ so it is non-negative
- inner product: $(x,y)=x^Hy=\overline{y^Hx}=\overline{(y,x)}$
    > another proof: $(\bar{x}y)(x\bar{y})=x\bar{x}y\bar{y}=|x|^2|y|^2,a\bar{a}=|a|^2\to \bar{x}y=\overline{x\bar{y}}$
- complex symmetric (Hermitian matrix): $\bar{A}^T=A\to A^H=A$.
    - quadratic form is real (and Hermitian)
        > proof: $(x^HAx)^H=x^HA^Hx=x^HAx$
    - eigenvalues are real
        > proof: $Ax=\lambda x\to \lambda x^Hx=x^HAx$ is real (from above), $x^Hx=\| x\|^2$ is real $\to \lambda$ is real.
    - eigenvectors of different eigenvalues are orthogonal
        > proof: $Ax_1=\lambda _1x_1,Ax_2=\lambda _2x_2\to (Ax_1)^Hx_2=\lambda _1x_1^Hx_2=x_1^HAx_2=x_1^H\lambda _2x_2\to (\lambda _1-\lambda _2)x_1^Hx_2=0\to x_1^Hx_2=0$ ($\bar{\lambda }_1=\lambda _1,A^H=A$)
    - $\Rightarrow$ can be diagonalized $A=Q\Lambda Q^{-1}=Q\Lambda Q^H=\sum _i^n\lambda _iq_iq_i^H$ 
- orthonormal: $(q_i,q_j)=q^H_iq_j= \begin{cases} 0(i\ne j) \\ 1(i=j) \end{cases}\to Q^HQ=I\to $ unitary matrix $Q$ 酉矩阵
    - properties: multiplication $Q_1Q_2,Q^{-1}$ is unitary matrix

## FFT example
- unit root (in unit circle)
    - $w_n=e^{i\frac{2\pi}{n}}\to x^n=1$ has $n$ solutions $\{x=w_n^k=e^{\frac{2k\pi i}{n}}|k=0,1,\dots ,n-1\}$
    - understanding: power of a unit complex number is rotate counter clockwise
    - properties: $w_n^n=1,w_n^k=w_{2n}^{2k},w_{2n}^{k+n}=-w_{2n}^k$
    - primitive unit root: $\{w_n^k|0\le k<n,\gcd (n,k)=1\},\mathrm{card}=\phi (n)$
        - any primitive unit root can generate all unit root by powering
        > illustration: $\phi (n)$ is Euler's totient function, indicate #$< n$ numbers coprime with $n$  
        > Eular's theorem: $\gcd (a,m)=1\to a^{\phi (m)}\equiv 1 \pmod{m}$
- Fourier matrix
    - $F_n=\begin{bmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & w & w^2 & \cdots & w^{n-1} \\ 1 & w^2 & w^4 & \cdots & w^{2(n-1)} \\ \vdots & \vdots & \vdots & \ddots & \vdots\\  1 & w^{n-1} & w^{2(n-1)} & \cdots & w^{(n-1)^2} \end{bmatrix}\in \mathbb{C^{n\times n}}$
    - $(F_n)_{ij}=w^{ij}(i,j=\mathbf{0},\dots ,n-1),w=e^{\frac{2\pi}{n}}$ is one primitive unit root.
    - unitary: $F_4^HF_4=4I\to (\frac{1}{\sqrt{n}}F_n)^H(\frac{1}{\sqrt{n}}F_n)=I$
- FFT
    - normal $F_{n}$ cost $f(n)=n^2$ operations
    - FFT cost $f_F(n)=2f_F(n/2)+n/2=\frac{1}{2}n\log_{2}{n}$
    - $F_{n}=\begin{bmatrix}I_{(n/2)\times (n/2)} & D \\ I & -D\end{bmatrix}\begin{bmatrix}F_{n/2} & 0 \\ 0 & F_{n/2}\end{bmatrix}P_{n\times n}$
        - $P_{n\times n}$ is column permutation matrix, rearrange even columns ahead of odd ones $(x_0,x_1,\dots ,x_n)P=(x_0,x_2,\dots ,x_1,x_3,\dots )$
        - $D_{(n/2)\times (n/2)}=\mathrm{diag}(1,w,w^2,\dots ,w^{n-1})$ cost $n/2$ multiplication.
