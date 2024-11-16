# orthogonality and projection (L14 ~ L17)

## inner product
- inner product: $(x,y)=x ^Ty$
    - non-negative for modulus $(x,x)\ge 0$ if and only $x=0$ meets equal sign.
    - symmetry: $(x,y)=(y,x)$
    - linearity: $(x+y,z)=(x,z)+(y,z)$ and $(k\vec{x},\vec{y})=k(x,y)$
- modulus: $(x,x)=\left \| x \right \|^2$
    - non-negative: $\left \| x \right \| \ge 0$ if and only $x=0$ meets equal sign.
    - homogeneity: $\left \| kx \right \| =|k|\left \| x \right \|$
        > proof: $(kx,kx)=k^2(x,x)\to \left \| kx \right \|=\sqrt{k^2} \left \| x \right \|\ge 0$
    - triangle inequality: $\left \| x+y \right \| \le \left \| x \right \| + \left \| y \right \|$ (the same as Cauchy-Schwarz meets equal sign when $x,y$ is dependent)
        > proof: $\left \| x+y \right \|^2=(x+y,x+y)=(x,x)+(y,y)+2(x,y)$ and $2(x,y)\le 2\sqrt{(x,x)(y,y)}$ from Cauchy-Schwarz inequality $\to \left \| x+y \right \|^2 \le \left \| x \right \|^2+ \left \| y \right \|^2 +2\left \| x \right \| \left \| y \right \| =(\left \| x \right \| +\left \| y \right \|)^2$
- Cauchy-Schwarz inequality
    - in essence is about angle between vectors.
    - $(x,y)^2\le \left \| x \right \|^2 \left \| y \right \|^2=(x,x)(y,y)$ if and only $x=ky$ linear dependent meets equal sign.
    > proof:
    > 1. $x,y$ is independent $\to \forall t:tx+y\ne 0\to (tx+y,tx+y)=(x,x)t^2+2(x,y)t+(y,y)>0\to \Delta =4(x,y)^2-4(x,x)(y,y)\le 0$
    > 2. $x,y$ is dependent: $x,y$ has 0 must right; otherwise $\to \forall k:y=kx\ne 0\to (x,y)^2=(x,kx)^2=k^2(x,x)^2=(x,x)(kx,kx)=(x,x)(y,y)$ meets equal sign.

## orthogonality / perpendicularity
- orthogonal vectors: $(x,y)=0\Leftrightarrow \left \| x \right \| ^2+\left \| y\right \| ^2=\left \| x+y \right \| ^2$
    - $\vec{0}\perp \forall \vec{a}\in \mathbb{R^n}$
        > proof: use linearity of inner product
    - $\Rightarrow$ independence (see Cauchy-Schwarz equality condition)
        > proof: $Ax=0,A=(a_1,\dots ,a_n),(a_1,Ax)=\sum (a_1,x_1a_1)+\dots +(a_1,x_na_n)=(a_1,x_1a_1)+0+\dots +0=x_1\left \| a_1 \right \|^2=a_1^TAx=a_1^T0=0\to x_1=0$, similarly, $(a_i,Ax)=0\to x_i=0\dots (A^TAx=\vec{0})\to x=0$ only has zero solution.
    - easily computational cofficients: $Ax=b$, get cofficients of $b$ is $x_i=\frac{a_i^Tb}{\left \| a_i \right \|}$ i.e. inner product $\Leftrightarrow$ projection.
        > proof: $A^TAx=A^Tb=\Lambda x$ where $\Lambda=\text{diag}(\left \| a_1 \right \| ,\dots ,\left \| a_n \right \|)$, so for each row $\left \| a_i \right \| x_i=a_i^Tb$ only need one inner product.
- orthogonal subspace: $S\perp T$ is every vector in $S\perp $ every vectors in $T$
    - $S\cap T=$ line: not orthogonal, becasue $\exists $ vectors in this line in both $S,T$.
    - orthogonal vector set: $S=(s_1,\dots ,s_s),T=(t_1,\dots ,t_t)\to S^TT=0$
    - $\perp$ vector set to span space: if $S^TT=0\to S\perp T$
        > proof: $(t_i,Sx)=\sum _j(t_i,x_js_j)=0$, $\perp$ vector set / basis $\to \perp$ span space.
- four subspaces
    - $C(A^T)\perp N(A)$ in $\mathbb{R^n}$
    - $C(A)\perp N(A^T)$ in $\mathbb{R^m}$
    > proof: $Ax=0$, every row in $A$ inner product $x=0$; the same as $A^Ty=0$.

## least squares
- $Ax=b$ when $m>n$ (measuring) may not have a solution, but **normal equation** $A^TA\hat{x}=A^Tb$ have.
- solve $Ax=b\to \min \left \| Ax-b\right \|^2 =\left \| e\right \|^2$ where $e$ is residual.
    - normal equation can be got from $\frac{\mathrm{d}\left \| e \right \|^2}{\mathrm{d} x}=0$ using quadric form.
- $(A^TA)_{n\times n}$
    - $A^TA=(A^TA)^T$
    - $N(A^TA)=N(A)$
        > proof: $Ax=0\to A^TAx=A^T0=0, A^TAx=0\to x^TA^TAx=0=(Ax)^TAx=\left \| Ax \right \|^2\to Ax=0$
    - $R(A^TA)=R(A)$
        > proof: from 1: $\dim N(A)=\dim N(A^TA)\to n-R(A)=n-R(A^TA)$
    - $R(A)=n\to A^TA$ is invertable
    - $A^TA$ is positive semidefinite matrix
        > proof: $x^TA^TAx=(Ax)^TAx=\left \| Ax \right \|\ge 0$

## orthogonal projection
- one dimension (vector): project $\vec{b}$ to line $\vec{a}$
    - projection vector: $\vec{p}=x\vec{a}$
    - projcetion direction: $\vec{e}=(\vec{b}-\vec{p})\perp \vec{a}$
    - cofficient $x$: $a^T(b-xa)=0\to x=\frac{a^Tb}{a^Ta}$
    - projection matrix: $p=a\frac{a^Tb}{a^Ta}=Pb\to P=\frac{aa^T}{a^Ta}$ is matrix.
- two dimension (matrix): project $b$ to plane $C(A)$
    - projection vector $p=A\hat{x}$
    - projection direction: $e=b-A\hat{x}\perp C(A)$
    - cofficient $\hat{x}$: $a_1^Te=0,a_2^Te=0\to A^T(b-A\hat{x})\to A^Tb=A^TA\hat{x}\to \hat{x}=(A^TA)^{-1}A^Tb$
        > note: $e\perp C(A)\Leftrightarrow A^TAx=A^Tb$ is least squares
    - projection matrix: $p=A\hat{x}=A(A^TA)^{-1}A^Tb=Pb$
- properities of projection matrix
    - $A$ is square matrix $\Rightarrow A$ is invertable (because $A$ is composed of basis) $\Rightarrow P_{m\times m}=I$
    - $P^T=P$
    - $P^2=P$
    - $b\in C(A)\Rightarrow Pb=b$
        > proof: substitude $b$ with $Ax=b$ in expression of $Pb$
    - $b\perp C(A)\Rightarrow Pb=0$ ($b\in N(A^T)$)
        > proof: substitude $b$ with $A^Tb=0$ in expression of $Pb$
    - $C(P)=C(A)\to R(P)=R(A)$
        > proof: $PA=A$
- least squares: $Ax=b\to A\hat{x}=p$ instead, project $b$ to $p\in C(A),e=(b-p)\perp C(A)$ orthogonality results in smallest $\left \| e \right \|$.
- another projection matrix $(I-P)$
    - $e=b-p=b-Pb=(I-P)b$, project $b$ to $e$
    - $C(I-P)\perp C(P)$
        > proof: $(I-P)^TP=0$

## orthonormal matrices
- orthonormal: like $A=I$ columns are independent, perpendicular and unit vectors.
    - $Q=[q_1,\dots ,q_n],Q^TQ=I$
    - **but $Q$ is square matrix** $\Rightarrow Q^T=Q^{-1}\Rightarrow QQ^T=I\to$ rows are independent, perpendicular and unit vectors.
    - $\det Q=\pm 1$
        > proof: $\det Q^TQ=\det Q^T \det Q=(\det Q)^2=\det I=1$
    - $A^TA=B^TB=I\Rightarrow (AB)^T(AB)=I$
        > proof: $(AB)^T(AB)=B^T(A^TA)B=B^TB=I$
- projection matrix
    - $P=Q(Q^TQ)^{-1}Q^T=QQ^T$, $Q$ is square $\Rightarrow P=I$.
    - $P^2=P=(QQ^T)(QQ^T)=Q(Q^TQ)Q^T=QQ^T$
- normal equation: $Q^TQ\hat{x}=Q^Tb\to \hat{x}=Q^Tb\to \hat{x_i}=q_i^Tb$ is easy to compute.
- hadamard matrix: a square matrix whose elements are +1 or -1, and $HH^T=mI$ where $m$ is dimension.
- Gram-Schmidt: get orthonormal columns $Q$ by doing projection.
    - doing normalization at final step
    - $a_1,a_2$ are independent vectors, project $a_2$ to $b_2$ so that $b_2 \perp b_1$.
    - $b_1=a_1,b_2=a_2-\frac{b_1^Ta_2}{b_1^Tb_1}b_1,q_1=\frac{b_1}{\left \| b_1 \right \|},q_2=\frac{b_2}{\left \| b_2 \right \|}$
        > proof: $b_1^Tb_2 =b_1 ^Ta_2-b_1 ^Ta_2=0$
    - $b_3 =a_3-\frac{b_1 ^Ta_3}{b_1 ^Tb_1}b_1-\frac{b_2 ^Ta_3}{b_2 ^Tb_2 }b_2, q_3=\frac{b_3}{\left \| b_3 \right \|}$
- decomposition $A=QR$: $Q^TA=Q^TQR=R=\begin{bmatrix} a_1^Tq_1 & a_2^Tq_1 \\ a_1^Tq_2 & a_2^Tq_2 \end{bmatrix}$.
    - $a_i^Tq_j=0(i<j)$
    - $R$ is easy to compute due to conclusion $x_i=q_i^Ta_j$ above.
