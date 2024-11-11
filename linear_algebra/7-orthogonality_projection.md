# orthogonality and projection (L14 ~ L17)

## orthogonality / perpendicularity
- orthogonal vectors: $x^Ty=0\Leftrightarrow \left \| x \right \| ^2+\left \| y\right \| ^2=\left \| x+y\right \| ^2\Leftrightarrow x^Tx+y^Ty=(x+y)^T(x+y)=x^Tx+y^Ty+x^Ty+y^Tx\Leftrightarrow x^Ty=0$ ($x^Ty=y^Tx$)
- $\vec{0}\perp \forall \vec{a}\in \mathbb{R^n}$
- orthogonal subspace: $S\perp T$ is every vector in $S\perp $ every vectors in $T$
    - $S\cap T=$ line: not orthogonal, becasue $\exists $ vectors in this line in both $S,T$.
- four subspaces
    - $C(A^T)\perp N(A)$ in $\mathbb{R^n}$
    - $C(A)\perp N(A^T)$ in $\mathbb{R^m}$
    > proof: $Ax=0$, every row in $A$ inner dot $x=0$; the same as $A^Ty=0$.

## least squares
- $Ax=b$ when $m>n$ (measuring) may not have a solution, but **normal equation** $A^TA\hat{x}=A^Tb$ have.
- solve $Ax=b\to \min \left \| Ax-b\right \|^2 =\left \| e\right \|^2$ where $e$ is residual.
    - normal equation can be got from $\frac{\mathrm{d}\left \| e \right \|^2}{\mathrm{d} x}=0$ using quadric form.
- $(A^TA)_{n\times n}$
    - $A^TA=(A^TA)^T$
    - $N(A^TA)=N(A)$
        > proof: $Ax=0\to A^TAx=A^T0=0, A^TAx=0\to x^TA^TAx=0=(Ax)^TAx=\left \| Ax \right \|^2\to Ax=0$
    - $rank(A^TA)=rank(A)$
        > proof: from 1: $\dim N(A)=\dim N(A^TA)\to n-rank(A)=n-rank(A^TA)$
    - $rank(A)=n\to A^TA$ is invertable
    - $A^TA$ is positive semidefinite matrix
        > proof: $x^TA^TAx=(Ax)^TAx=\left \| Ax \right \|\ge 0$

## projection
- one dimension (vector): project $\vec{b}$ to line $\vec{a}$
    - projection vector: $\vec{p}=x\vec{a}$
    - projcetion direction: $\vec{e}=(\vec{b}-\vec{p})\perp \vec{a}$
    - cofficient $x$: $a^T(b-xa)=0\to x=\frac{a^Tb}{a^Ta}$
    - projection matrix: $p=a\frac{a^Tb}{a^Ta}=Pb\to P=\frac{aa^T}{a^Ta}$ is matrix.
- properties of projection matrix:
    - $C(P)$ is a line through $a$, $rank(P)=1$.
    - $P^T=P$ ($aa^T$ is symmetric), $P^2=P$
- two dimension (matrix): project $b$ to plane $C(A)$
    - projection vector $p=A\hat{x}$
    - projection direction: $e=b-A\hat{x}\perp C(A)$
    - cofficient $\hat{x}$: $a_1^Te=0,a_2^Te=0\to A^T(b-A\hat{x})\to A^Tb=A^TA\hat{x}\to \hat{x}=(A^TA)^{-1}A^Tb$
        > note: $e\perp C(A)\Leftrightarrow A^TAx=A^Tb$ is least squares
    - projection matrix: $p=A\hat{x}=A(A^TA)^{-1}A^Tb=Pb$
- properities of projection matrix
    - $P_{m\times m}=I$ if $A$ is invertable (if $A$ is square matrix, $A$ is invertable from definition)
    - $P^T=P$
    - $P^2=P$
    - $b\in C(A)\Rightarrow Pb=b$
        > proof: substitude $b$ with $Ax=b$ in expression of $Pb$
    - $b\perp C(A)\Rightarrow Pb=0$ ($b\in N(A^T)$)
        > proof: substitude $b$ with $A^Tb=0$ in expression of $Pb$
    - $C(P)=C(A)$, so $rank(P)=rank(A)$
        > proof: $PA=A$
- least squares: $Ax=b\to A\hat{x}=p$ instead, project $b$ to $p\in C(A),e=(b-p)\perp C(A)$ orthogonality results in smallest $\left \| e \right \|$.
- another projection matrix $(I-P)$
    - $e=b-p=b-Pb=(I-P)b$, project $b$ to $e$
    - $C(I-P)\perp C(P)$
        > proof: $(I-P)^TP=0$
