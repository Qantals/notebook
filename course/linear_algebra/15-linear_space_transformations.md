# linear space and linear transformations (L5, L11, L31, L32)

## linear space
- linear space: $(V,P,+,\cdot)$: V set using $P$ number field is closure (still in $V$) to linear operation $(+,\cdot)$
    - meet 8 rules (addition: associate law 结合律, commutative law 交换律, add to 0, add negative self. scalar multiplication: times 1, associate law, distributive law - element / scalar)
    - $\vec{0}$: $\forall \vec{a}\in V,0\vec{a}=0\in V\to \vec{0}\in$ any space.
- subspace: $W\subset V$ is linear space $\Leftrightarrow$ closure to $(+,\cdot)$
    - trival subspace: $V_1=V,V_2=\{\vec{0}\}$
    - nontrival subspace: others
    - span subspace: $\forall \alpha _i\in V,L(\alpha _1,\dots, \alpha _r)$ is linear combination of $\alpha _i$
    - $\dim W\le \dim V$
        - $\dim W=\dim V\Rightarrow W=V$
- set operation
    - $P,L,\{\vec{0}\}\subset V=\mathbb{R^3}$, $P$ is plane across origin, $L$ is line across origin.
    - union: not a space. example: $P\cup L\ (L\subsetneq P)$
    - addition: is a space. example: $P+L=V\ (L\subsetneq P)$
    - intersection: is a space. example: $P\cap L=\{\vec{0}\}\ (L\subsetneq P)$

## change of basis
- basis: independent $\# n$ vectors, $\forall \# (n+1)$ are depedendent
    - dimension: $\dim V=n$
    - any $\# n$ independent vectors $\in V,\dim V=n$ is a set of basis
    - basis of subspace can be add to basis of whole space with $\# n-m,\dim V=n,\dim W=m,W\subset V$
- coordinate: $\alpha =a_1\alpha _1+\dots +a_n\alpha _n\to (a_1,\dots ,a_n)$
    - vector calculation is one-to-one corresponds to coordinate calculation: isomorphic 同构
- change of basis
    - $\alpha _{n\times n}=(\alpha _1,\dots ,\alpha _n),\alpha '_{n\times n}=(\alpha '_1,\dots ,\alpha '_n)$ are different basis, $\alpha _i$ is column vector.
    - formula: $\alpha '=\alpha S(\alpha '_j=\sum _iS_{ij}\alpha _i)\to S_{n\times n}$ is transition matrix
    - $S$ is invertable (proof: $\dim C(S^T)=R(S)=n$, need new basis is independent)
    - transitivity: $\alpha '=\alpha A,\alpha ''=\alpha 'B\Rightarrow \alpha ''=\alpha AB$
    - affine coordinate system $Ox'y'$: relative to orthogonal coordinate system, it can have non-orthonormal basis
- change of coordinates
    - $\forall v\in V\to v=\alpha x=\alpha 'x'=\alpha Sx'$ ($x$ is coordinate)
    - $\Rightarrow x=Sx',x'=S^{-1}x$

## Euclidean space 欧氏空间
- euclidean space: numerical field $P=\mathbb{R}$ defined inner product
- inner product
    - condition: symmetry, additivity and non-negative for modulus
    - modulus: $\| a\|=\sqrt{(a,a)}$
    - $(a,b)=a^TA_{n\times n}b$ is also inner product in $\mathbb{R^n}$ meet condition above
    - function inner product: $(f(x),g(x))=\int ^b_af(x)g(x)\mathrm{d}x$ meet condition above
    - meet Cauchy-Schwarz inequality and triangle inequality
        - can prove $(\int _a^bf(x)g(x)\mathrm{d}x)^2\le \int_a^bf^2(x)\mathrm{d}x\int_a^bg^2(x)\mathrm{d}x\Leftrightarrow (f(x),g(x))^2\le (f(x),f(x))(g(x),g(x))$

## linear space example
- matrix space
    - subspace $M_{3\times 3}$, $\dim M=9$
    - upper triangles, $\dim U=6$
    - symmetric matrices, $\dim S=6$
        - $S\cap U$: diagonal matrices, $\dim D=3$
        - $S+U=M$: linear combination of any $S$ and $U$
        - $\dim (S+U)+\dim (S\cap U)=\dim S+\dim U$
- rank X matrices
    - construction: $\mathrm{rank}=4$ matrix is linear combination of some $\mathrm{rank}=1$ matrices.
    - same rank matrices:
        - suppose $M$ is rank 4 metrices of all $5\times 17$ metrices
        - $\Rightarrow M$ is not a subset (not closure): $R(A+B)\le R(A)+R(B)$
- special vectors
    - suppose $S=\{\vec{v}_{4\times 1}|v_1+v_2+v_3+v_4=0\}$, is $S$ a space?
    - $A_{1\times 4}=[1\ 1\ 1\ 1]\to S=N(A)$
    - $R(A)=1,\dim N(A)=n-r=3$
    - $C(A)=\mathbb{R^1},N(A^T)=\vec{0}, \dim N(A^T)=m-r=0$

## linear transformation
- linear transformation: $T:V\to V\in \mathrm{R^n}$
    - linearity: $T(v+w)=T(v)+T(w),\ T(cv)=cT(v)$
        - $\Rightarrow T(cv+dw)=cT(v)+dT(w)$
        - check: $T(0)=0$
        > example: projection, rotation, derivation  
        > bad example: shift whole plane by $v_0:T(\vec{a})=T((a_1,a_2)^T)=(a_1+v_1,a_2+v_2)^T$ (for honogeneity issue)  
    - rotation matrix: $A=\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$, $y=Ax$ rotate vector $x$ to $y$ rotate counterclockwise $\theta$.
- types
    - scalar multiplication transformation: $T(a)=ka$
    - zero transformation: $T(a)=0a=0$
    - identity transformation: $T(a)=1a=a$
- invertable transformation: one-to-one mapping in $V$, vice versa
- operation
    - addition: $(T_1+T_2)a=T_1(a)+T_2(a)=a(A+B)$
    - scalar multiplication: $(kT_1)a=kT_1(a)=kaA$
    - multiplication: $(T_1T_2)a=T_1(T_2(a))=aAB\ne T_2(T_1(a))=aBA$
    - meet 8 rules like linear space
    - like operation of matrices: relationship with matrices!
- w.r.t. matrices
    - basis $\alpha _{n\times n}=(\alpha _1,\dots ,\alpha _n)$, $\alpha _{i-n\times 1}$
    - formula: $T(\alpha)_{n\times n}=(T(\alpha _1),\dots ,T(\alpha _n))=\alpha A$
    - explain: $T(\alpha _j)_{n\times 1}=\sum _ia_{ij}\alpha _i$ each column of $A$ is response to one original basis
    - coordinate: $v_{\mathrm{out}}=T(\alpha c_{\mathrm{in}})=T(\alpha)c_{\mathrm{in}}=\alpha Ac_{\mathrm{in}}=\alpha c_{\mathrm{out}}\Rightarrow c_{\mathrm{out}}=Ac_{\mathrm{in}}$
    - $T_1$ is invertable $\Leftrightarrow A$ is invertable
    - uniqueness: linear transformation has unique corresponding matrix under one basis
        > illustration: $T(\alpha _j)$ has coordinate column vector $a_j$ under basis $\alpha =(\alpha _1,\dots ,\alpha _n)$
- under different basis
    - $\beta =\alpha P\to T(\beta)=T(\alpha P)=T(\alpha)P$ transition matrix is same for **linear** transformation
    - $\beta =\alpha P$ is change of basis, $T:\alpha \to A,T:\beta \to B\Rightarrow B=P^{-1}AP$ is similar, and transition matrix $P$ is just invertable matrix in similarity.
        > proof: $\beta =\alpha S\to T(\beta)=\beta B=\alpha PB=T(\alpha)P=\alpha AP\Rightarrow PB=AP\to B=P^{-1}AP$
- example: 2-D projection
    - basis is eigenvectors
        - projection matrix is symmetric $\to$ eigenvectors are orthogonal and eigenvalues are 1 or 0 $\to$ corresponding transformation for orthogonal basis is 1 or 0 $\to$ special transformation matrix is diagonal and relative to eigenvalues.
        - projection matrix is symmetric $P=Q\Lambda Q^T,Pq_1=q_1\to \lambda _1=1$ projects to $q_1$
        - $T(Vc)=c_1v_1+c_20\to A=\Lambda =\begin{bmatrix}1 & 0 \\ 0 & 0\end{bmatrix},T:A(c_1,c_2)^T=(c_1,0)^T$
    - basis is standard: project onto $45^{\circ}$ line: $A=P=\frac{aa^T}{a^Ta}=\begin{bmatrix}1/2 & 1/2 \\ 1/2 & 1/2 \end{bmatrix}, a=(1,1)^T$ for $45^{\circ}$ (back to rectangular coordinate case)
- affine transformation: $T(x_{n\times 1})_{n\times 1}=L(x)+b_{n\times 1},L(x)$ is linear transformation

## linear mapping
- linear mapping: $T:V\in \mathbb{R^n}\to W\in \mathbb{R^m}$
    - linearity: the same as linear transformation
        > example: matrix multiplication $A$: $T_{2\times 1}(v)=A_{2\times 3}v_{3\times 1}$, $T:\mathbb{R^3}\to \mathbb{R^2}$  
        > bad example: $T(v)=\| v \|$ so $T:\mathbb{R^3}\to \mathbb{R^1}$ ($c=-1$ issue)  
- matrices
    - $V_{n\times n}=(v_1,\dots, v_n)$ is input basis, $W_{m\times m}=(w_1,\dots ,w_m)$ is output basis
    - columns of $A$ is response to each input basis $\in V$. i.e. $v_j\to a_{ij}w_i$
        - formula: $T(V)_{m\times n}=(T(v_1),\dots ,T(v_n))=W_{m\times m}A_{m\times n}$
        - coordinate: $w_{m\times 1}=T(v)_{m\times 1}=T(Vc_{\mathrm{in}})=Wc_{\mathrm{out}-m\times 1}=WAc_{\mathrm{in}-n\times 1}=c_{\mathrm{in}-1}\sum _ia_{i1}w_1+\dots +c_{\mathrm{in}-n}\sum _ia_{im}w_m$
- example: first derivate
    - input $V_{3\times 1}=(1,x,x^2)^T$, output $W_{3\times 1}=(1,x)^T$
    - $c_2+2c_3x=T(c_1+c_2x+c_3x^2)\to Ac_{in}=c_{out}:\begin{bmatrix}0 & 1 & 0 \\ 0 & 0 & 2\end{bmatrix}\begin{bmatrix}c_1 \\ c_2 \\ c_3 \end{bmatrix}=\begin{bmatrix}c_2 \\ 2c_3\end{bmatrix}$

## application: compression of images
- image: $A_{512\times 512}\to x\in \mathbb{R^{512\times 512}}$ one vector represents whole image
- standard basis $(0,0,0,1,0,0)^T$
- better basis
    - low frequency signal $(1,1,1,1,1,1)^T$, pure black image
    - high frequency signal $(1,-1,1,-1,1,-1)^T$, chessboard image
    - $(1,1,1,-1,-1,-1)^T$, half light half dark image
- Fourier basis: divide into $8\times 8$ blocks in the image
    - columns of Fourier matrix $(1,1,\dots)^T,(1,w,w^2,w^3,\dots)^T,\dots$
    - each block: 64 cofficients, 64 basis for 64 pixels $\to x\in \mathbb{R^{64}}$.
- lossy compression
    - set threshold to remove coefficients with many zeros (normal case throw high frequency because things changes smoothly)
    - $\hat{x}=\sum _{i<64}\hat{c_i}v_i$
- wavelets 小波 for $\mathbb{R^8}$
    - $w_1=(1,1,1,1,1,1,1,1)^T,w_2=(1,1,1,1,-1,-1,-1,-1)^T$
    - $(1,1,-1,-1,0,0,0,0)^T,(0,0,0,0,1,1,-1,-1)^T$
    - $(1,-1,0,0,0,0,0,0)^T,(0,0,1,-1,0,0,0,0)^T$
    - $(0,0,0,0,1,-1,0,0)^T,(0,0,0,0,0,0,1,-1)^T$
    - $p_{8\times 1}=c_1w_1+\dots +c_8w_8=Wc\to c=W^{-1}p=W^Tp$ orthogonal
- good basis
    - computes fast (FFT,FWT)
    - good compression, few is enough
- eigenvectors as basis is good $\to A=\Lambda$
