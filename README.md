# Linear-Algebra
# Chapter 1. Matrices & Gaussian Elimination

우리는 기하공간을 두 가지 관점으로 바라볼 수 있다.

1. 행 관점: 교점, 교선을 그래프로 표현
2. 열 관점: 벡터의 관점(화살표라 생각하면 직관적)

정리: 저차원에서는 행 관점이 더 편할 수 있지만, 고차원으로 갈수록 시각화가 어려워 열 관점을 채택한다.

## Gaussian Elimination

Reduce a system of equations (line up the variables, the equations 
are the rows), a matrix, or an augmented matrix by using elementary row operations.
Forward elimination (전진소거법)
1. Start with the first row.
2. Excluding all rows before the current row, in the leftmost nonzero column,
make the entry in the current row nonzero by switching rows as necessary. 
The pivot is the first nonzero in the current row, the row that does the elimination. 
3. Make all numbers below the pivot zero.
4. Move on to the next row, and repeat until only zero rows remain.
Backward-substitution (후방대입법)
5. Work upward, beginning with the last nonzero row, and add multiples of each row to the rows above to create zeros in the pivot column. When working with equations, 
this is essentially substituting the value of the variable into earlier equations.
6. Repeat for each preceding row except the first.

## LU 분해: 하삼각행렬과 상삼각행렬로 행렬 분해.
-왜 LU 분해일까? 
 -더 빠른 행렬계산을 하려고
BUT!! 모든 행렬이 LU분해 가능하지 않다. 따라서 치환행렬 P를 사용하여, LU 분해가능하게 한다.(PA=LU)
