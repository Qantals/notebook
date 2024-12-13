# graphs and networks (L12, L13)

## graphs & networks
> directed graph = {nodes=n=4, edges=m=5}
- incidence matrices (关联矩阵,和常规定义多一个转置,见下) $A_{m\times n}$: column means nodes, row means edges, -1 means out, 1 means in.
    - $\vec{x}_{n\times 1}=(x_1,x_2,x_3,x_4)^T$ is potential at node (电势), $e$ is potential difference (电势差)
    - $e_{m\times 1}=Ax=(x_i-x_j,\dots)^T$
        - $\dim N(A)=1$: if $e=0\to x=(1,\dots ,1)^T$ is homogeneous solution.
        - $R(A)=n-1$: set one node as ground ($x_1=0$), other nodes (columns) are independent.
        - loop: dependent edges (rows) compose loop, independent ones compose tree.
- kirchhoff's current law: $f=A^Ty_{m\times 1}=0$ ($f$ is external current source)
    - for each row of $A^T$: same node iterates all edges, negitive sign means leaving out the node.
    - $y_{m\times 1}=Ce_{m\times 1}$ is current (Ohm's law, $C$ is conductance, scalar)
    - $N(A^T)$: all possible loops / meshes current for $f=0$.
        - $\dim N(A^T)=m-r=m-n+1$: # all smallest loops
        - basis of $N(A^T)$: current of the smallest loop (components of the current vector don't cross that loop is 0, others are 1 or -1 means right / reverse direction of settings in $A$. As a result you can see current of loop meets KCL).
- total equation: $A^TCAx=f$
- Eluer's formula (any graph has this property)
    - $\dim N(A^T)=m-r=m-n+1$
    - $\Leftrightarrow\#\text{loops}=\#\text{edges}-(\#\text{nodes}-1)$
    - $\Leftrightarrow\#\text{nodes}-\#\text{edges}+\#\text{loops}=1$
- tree: graph without loop (independent). Get it by choosing pivot columns from $A^T$.

## review / thinking (L13)
- $A^2=0$ but $A\ne 0$: $A=\begin{bmatrix}0 & 1 \\ 0 & 0\end{bmatrix}$
- $N(CD)=N(D)$ where $C$ is invertable.
    > proof: row operation doesn't change solution of $Ax=b$.
- for square matrix, row space may not equal to column space. e.g. $A=\begin{bmatrix} 0 & 1 \\ 0 & 0\end{bmatrix}$
- if $A,B$ are the same in four fundamental space, $A\ne kB$ is possible: $A,B$ are invertable.
