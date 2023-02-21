1. We need to iterate over each cell of the matrix and determine the distance to the nearest 0. This means that we need to start with a nested loop to iterate over each row and column of the matrix.

2. We can use breadth-first search (BFS) to determine the distance to the nearest 0. To do this, we start with all the 0s in the matrix and add them to a queue. Then, we start a BFS from each 0 and mark the distance of each cell as we visit it. We continue the BFS until we've visited all cells.

3. We need to keep track of the distance of each cell from the nearest 0. One way to do this is to create a new matrix of the same size as the input matrix and initialize each cell to -1. As we perform BFS from each 0, we update the corresponding cell in the new matrix with the distance.

4. Once we've finished BFS from all 0s, the new matrix will contain the distances of each cell to the nearest 0.

5. Finally, we return the new matrix.
