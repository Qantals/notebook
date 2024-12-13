# determinants (L18 ~ L20)

## definition
- properities(1~3 are base):
    1. $\det I=1$
    2. exchange rows reverse the sign ($\det E_{ij}=-1$). So permutation $\det P=1/-1$ (divided to odd / even type)
    3. linearity (superposition principle) of row-wise
        - homogeneity: $\det E_{i}(c)=c$
        - additivity: $\det (A_{\text{row}-i}+B_{\text{row}-i})=\det A_{\text{row}-i} + \det B_{\text{row}-i}$ where $A$ and $B$ only has row $i$ is different.
    4. 2 equal rows lead to $\det =0$ (proof: from property 2)
    5. holds invarient when $E_{ij}(c)=1$ (proof: from property 4 and 3)
    6. row of zeros lead to $\det =0$ (proof: from property 3)
    7. $\det A = \det U=d_1d_2\dots d_n$ where $d_n$ are diagonals, $U$ is upper triangle matrix. (proof: from property 5 using Gauss-Jordan elimination $A\to U$ , then use property 1 and 3 extract $k$ from all rows)
    8. $\det A=0\Leftrightarrow$ A is singular (proof: elimination and row of zeros), $\det A\ne 0\Leftrightarrow$ A is invertable.
    9. $\det AB=(\det A)(\det B)$ (proof: if any one is singular, then through elimination $AB\to U$ contains row of zeros so $\det =0$; otherwise $A,B$ are split into product of elementary matrices, which has this property $\det E_1A=\det E_1 \det A$ known from property 2, 3, 5)
        - $\det A^{-1}=(\det A)^{-1}$
        - $\det A^2=(\det A)^2$
        - $\det 2A=2^{n}\det A$
    10. $\det A^T=\det A$ (proof: $A=LU$ to get triangle matrix, then use property 7 and 9. Or you can also use elementary matrices to do decomposition).
- calculation
    - pivot formula: split each row to #column determinants using additivity of property 3, leaving $\det \ne 0$ ones which have only one non-zero pivot in all rows and columns ($\det \ne 0$ ones like permutations of diagonal matrices, $\det =0$ ones has row / column of zeros).
    - big formula: $\det A=\sum_{n!\text{terms}}(-1)^{\text{inversion number}} a_{1\alpha}a_{2\beta}\dots$ where $\alpha ,\beta$ are permutations of $(1\dots n)$ means the column label where pivots stand in each row. We want to get diagonal matrix, whose permutation is just natural order $(1\dots n)$, to use property 7. The sign depends on exchange times of rows (inversion number).
        - illustration: split determinant to $n!$ terms using pivot formula (there are $n$ rows, each row has one column to choose, chosen column can not be chosen again).  
        - calculate inversion number:  iterate all numbers, and sum up all times that numbers before are bigger than this number. See insertion sort for principle reference.  
        - inversion number has same parity with exchange times in sorting.
            - inversion number is odd: odd permutation, otherwise even permutation.
            - exchange of two numbers change parity of permutation.
                > proof:  
                > 1. When exchange between two near numbers, the inversion number $\pm 1$ so it changes parity;  
                > 2. When exchange between two far numbers including $m$ numbers in the middle, it need $2m+1$ (this is odd so changes parity, otherwise holds parity) near number changes where $a\to b$ needs $m+1$ then $b\to a$ needs $m$, so inversion number changes parity.
- sub determinants
    - minor: choose #$i$ rows and #$j$ columns from $A$. 
    - principal minor: rows label is the same as columns label.
    - cofactors (代数余子式) of $a_{ij}\to C_{ij}=(-1)^{i+j} \det$ (n-1)-order matrix without row $i$ and col $j$.
- cofactor formula: along any row or any column (becasue $\det A=\det A^T$).
    - Laplace expansion: choose any $k$ rows, the determinant equals to all sub-matrices (square matrices) with these $k$ rows (amount is $C_n^k$) multiply their cofactors dividely (sign depends on summation of chosen sub-matrices' rows and columns).
    - This is convenient for block matrices computation: $A=\begin{bmatrix} B_{m\times m} & * \\ O & C_{n\times n}\end{bmatrix},\det A=\det B \det C$ where $A$ is not diagonal matrix but block matrix is.
- $A$ is invertable $\Leftrightarrow \det A \ne 0\Leftrightarrow \lambda _A\ne 0$ ($\prod \lambda \ne 0$)
    > proof: split $A$ with element matrices using Gauss-Jordan elimination and use property 9.

## calculation
- normal: use property 3 for Gauss elimination and property 7 multiply diagonal elements.
- common practice
    - tridiagonal matrix(三对角矩阵): diagonal and sub-diagonal has elements $d,u,l$, others are zero. $\det A_n=d\det A_{n-1}-ul\det A_{n-2}$ (proof: expand with row 1). Then use recurrence form with eigenvalue to solve.
    - Vandermonde determinant: $V_n=\begin{vmatrix}1 &\dots & 1 \\ x_1 & \dots & x_n \\ \dots \\ x_1^{n-1} & \dots & x_n^{n-1}\end{vmatrix}=\prod_{1\le j \le i \le n}(x_i-x_j)$
        > proof: subtract row $i-1$ times $x_1$ from row $i$ and $i$ starts from $n$ to 1, and get $V_n=(x_2-x_1)\dots (x_n-x_1)\det V_{n-1}$, using recursion.

## Cramer's rule
- inverse formula: $A^{-1}=\frac{1}{\det A}C^T$ where $C$ is cofactor matrix(conmosed of $C_{ij}$), but $C^T=A^*$ is adjugate matrix 伴随矩阵.
    > proof: $AC^T=AA^*=(\det A)I$ where transpose make it easy to compute matrix multiplication.  
    > Elements 1 mean computes $\det A$, and elements 0 mean computing determinants of singular matrix (proof: calculate determinant of matrix with same row is zero)
- $R(A^*)=\begin{cases} n & R(A)=n \\ 1 & R(A)=n-1 \\ 0 & R(A)<n-1\end{cases}$
    > proof:
    > 1. $R(A)=n,\det AA^*=\det A\det A^*=\det (\det A)I=(\det A)^n\ne 0,\det A\ne 0\to \det A^*\ne 0$
    > 2. $R(A)<n-1$, from definition $\det C_{ij}=0\to A^*=0$
    > 3. $R(A)=n-1,\det A=0\to AA^*=(\det A)I=0\to R(A)+R(A^*)=n-1+R(A^*)\le n\to R(A^*)\le 1$, but $R(A)=n-1\to \exists C_{ij}\ne 0\to R(A^*)>0\to R(A^*)=1$
- $Ax=b,x=A^{-1}b=\frac{1}{\det A}C^Tb\to x_j=\frac{\det B_j}{\det A}$
- $B_j=[b\text{(the j-th column)},\ A\text{(without j-th column)}]$
    > proof: expand $\det B_j$ with column $j$: row $j$ of $C^T$ means column $j$ of $C$, then replace $A_{\_ j}$ with $b$
- computation is very expensive.

## volume (geometry significance)
- outer product
    - $\| a\times b\|=\| a\| \| b\| \sin \langle a,b\rangle$
    - right-hand rule: $a\times b\perp a,b$
    - $a\times a=0,a\times 0=0$
    - $a\times b=-b\times a$ careful with order
    - $(\lambda a)\times (\mu b)=\lambda \mu (a\times b)$
    - $a\times (b+c)=a\times b+a\times c$
- outer product of basis
    - $i\times i=j\times j=k\times k=0$
    - $i\times j=k,\ j\times k=i,\ k\times i=j$
- outer product with basis
    - $a\times b=\begin{vmatrix}i & j & k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$
    - $S_{\triangle}=\frac{1}{2}\| a\| \| b\|\sin \theta=\frac{1}{2}\| a\times b\|$
    - $S_{\Box}=2S_{\triangle}=\| a\times b\|$
- mixed product
    - $(a\times b)\cdot c=(b\times c)\cdot a=(c\times a)\cdot b$
    - $(a\times b)\cdot (\lambda c_1+\mu c_2)=\lambda (a\times b)\cdot c_1+\mu (a\times b)\cdot c_2$
    - $[a\ b\ c]=0\Leftrightarrow a,b,c\ne 0$ on a common plane
- mixed product with basis
    - $(a\times b)\cdot c=[a\ b\ c]=\begin{vmatrix}a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}=\det A$
    - parallel hexahedron 平行六面体: $V=|\det A|=\| a\times b\| \| c\| |\cos \theta|=|(a\times b)\cdot c|$
    > computed by determinant: check  
    > determinant property 1: $A=Q\to \det Q=\pm 1$ (proof: $QQ^T=I\to \det QQ^T=(\det Q)^2=1$)  
    > property 2: exchange rows doesn't change volume.  
    > property 3a: $\lambda$ times of one row, the volume and determinant increase the same size $\lambda$.  
    > property 3b: parallelogram 平行四边形, 2-dim example:$(0,0),(x_1,y_1),(x_2,y_2),(x_1+x_2,y_1+y_2)\to S=\begin{vmatrix}x_1 & y_1 \\ x_2 & y_2\end{vmatrix}$.  
    > $\begin{vmatrix}x_1+x_3 & y_1+y_3 \\ x_2 & y_2\end{vmatrix}=\begin{vmatrix}x_1 & y_1 \\ x_2 & y_2\end{vmatrix}+\begin{vmatrix}x_3 & y_3 \\ x_2 & y_2\end{vmatrix}$ is additive (details are complex).
- triangle (with shift to origin): $(x_1,y_1),(x_2,y_2),(x_3,y_3)$. $A=\begin{bmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{bmatrix}\to S=\frac{1}{2}|\det A|$.
    - illustration: $S=\frac{1}{2}\begin{vmatrix}x_1 & y_1 & 1 \\ x_2-x_1 & y_2-y_1 & 0 \\ x_3-x_1 & y_3-y_1 & 0\end{vmatrix}=\frac{1}{2}\begin{vmatrix}x_2-x_1 & y_2-y_1 \\ x_3-x_1 & y_3-y_1\end{vmatrix}$.
