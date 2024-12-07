# linear transformations (L31~L32)

## linear transformation
- linearity: $T(v+w)=T(v)+T(w), T(cv)=cT(v)\to T(cv+dw)=cT(v)+dT(w)$
    - check: $T(0)=0$
    - example 1: projection $T:\mathbb{R^2}\to \mathbb{R^2}$ a mapping
    - bad example 1: shift whole plane by $v_0$ ($c=2$)
    - bad example 2: $T(v)=\| v \|$ so $T:\mathbb{R^3}\to \mathbb{R^1}$ ($c=-1$)
    - example 2: rotation by $45^{\circ}$
    - example 3: matrix multiplication $A$: $T_{2\times 1}(v)=A_{2\times 3}v_{3\times 1}$, $T:\mathbb{R^3}\to \mathbb{R^2}$
- transformation $\Leftrightarrow$ matrices
    - $T:V\in \mathbb{R^n}\to W\in \mathbb{R^m}$
    - $V=(v_1,\dots, v_n)$ is orthogonal input basis, $\forall v=Vc_{\mathrm{in}},c_{n\times 1}=(c_1,\dots ,c_n)$ is coordinates.
    - $W=(w_1,\dots ,w_m)$ is output basis, $\forall w=Wc_{\mathrm{out}},c_{m\times 1}$
    - rows of $A$ corresponds output basis $W$, columns of $A$ corresponds input basis $V$. i.e. $a_{ij}$ means response $v_j\to w_i$
        - $w=T(v)=c_{1-\mathrm{in}}T(v_1)+\dots +c_nT(v_n)$
        - i-th column of $A$ is $T(v_i)=a_{1i}w_1+\dots +a_{mi}w_m\to (a_{1i},\dots ,a_{mi})=c_{\mathrm{out}}$
        - $\Rightarrow w=T(v)=c_1\sum _ia_{i1}w_1+\dots +c_n\sum _ia_{im}w_m\Rightarrow T:A_{m\times n}c_{\mathrm{in}}=c_{\mathrm{out}}$
    - inverse of linear transformation is $A^{-1}$ ($Av=w\to v=A^{-1}w$)
- example: 2-D projection
    - basis is eigenvectors
        - projection matrix is symmetric $\to$ eigenvectors are orthogonal and eigenvalues are 1 or 0 $\to$ corresponding transformation for orthogonal basis is 1 or 0 $\to$ special transformation matrix is diagonal and relative to eigenvalues.
        - projection matrix is symmetric $P=Q\Lambda Q^T,Pq_1=q_1\to \lambda _1=1$ projects to $q_1$
        - $m=n=2,V=W=Q$
        - $T(Vc)=c_1v_1+c_20\to A=\Lambda =\begin{bmatrix}1 & 0 \\ 0 & 0\end{bmatrix},T:A(c_1,c_2)^T=(c_1,0)^T$
    - basis is standard: project onto $45^{\circ}$ line: $V=W=I_{2\times 2},A=P=\frac{aa^T}{a^Ta}=\begin{bmatrix}1/2 & 1/2 \\ 1/2 & 1/2 \end{bmatrix}, a=(1,1)^T$ for $45^{\circ}$ (back to rectangular coordinate case)
- example: first derivate
    - input $V_{3\times 1}=(1,x,x^2)^T$, output $W_{3\times 1}=(1,x)^T$
    - $c_2+2c_3x=T(c_1+c_2x+c_3x^2)\to Ac_{in}=c_{out}:\begin{bmatrix}0 & 1 & 0 \\ 0 & 0 & 2\end{bmatrix}\begin{bmatrix}c_1 \\ c_2 \\ c_3 \end{bmatrix}=\begin{bmatrix}c_2 \\ 2c_3\end{bmatrix}$

## compression of images
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

## change of basis
- $T:V\in \mathbb{R^n}\to V\in \mathbb{R^n}$
- change of basis: $\alpha=(\alpha _1,\dots ,\alpha _n),\beta =(\beta _1,\dots ,\beta _n)\in V\in \mathbb{R^n}$ are different basis, $\beta =\alpha S(\beta _j=\sum _iS_{ij}\alpha _i)\to S_{n\times n}$ is transition matrix
- change of coordinates: $\forall v\in V\to v=\alpha x=\beta y=\alpha Sy$ ($x_{n\times 1},y_{n\times 1}$ are coordinates) $\to x=Sy$
- similarity $A\sim B\Leftrightarrow$ same eigenvalues $\to$ same linear transformation under different basis
    > proof: $A$ is transformation matrix corresponding $T$ with basis $\alpha$, $B$ is with $\beta$  
    > $\therefore$ see from basis $\alpha: u=Ax=SBy=SBS^{-1}(Sy)=(SBS^{-1})x\to A=SBS^{-1}$ is similar
    - $Ax=SBy\Leftarrow R=S\to u=Ax=Sv=S(By)$ see below
- expansion to $m\ne n$
    - $T:V\in \mathbb{R^n}\to W\in \mathbb{R^m}$
    - $V\in \mathbb{R^n}:\alpha \to \beta:\beta =\alpha S_{n\times n},x=Sy$
    - $W\in \mathbb{R^m}:\gamma \to \delta:\gamma =\delta R_{m\times m},u=Rv$
    - $w=T(v)=\gamma u=\delta v$
    - $u=Ax,v=By=BS^{-1}Sy=BS^{-1}x=R^{-1}u=R^{-1}Ax\to R^{-1}A=BS^{-1},B=R^{-1}AS$

