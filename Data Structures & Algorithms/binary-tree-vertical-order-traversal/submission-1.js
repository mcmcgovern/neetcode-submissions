/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 * 
 * interface NodeMetadata {
 *      row: number;
 *      column: number;
 *      node: TreeNode
 * }
 */



class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    verticalOrder(root) {
        if (!root) return [];
        const colToNodeAndRow = new Map(); // key: column, value: [Node, Row]

        function levelOrderTraversal(root) {
            let [leftmostCol, rightmostCol] = [0,0];
            if (!root) return [leftmostCol, rightmostCol];
            const queue = [];
            let queueItem = {
                node: root,
                row: 0,
                col: 0
            }
            queue.push(queueItem);
            while (queue.length !== 0) {
                const { node: currentNode, row: currentRow, col: currentCol } = queue.shift();
                if (!currentNode) continue;

                if (currentNode.left) {
                    const nextNode = {
                        node: currentNode.left,
                        row: currentRow+1,
                        col: currentCol-1
                    }
                    queue.push(nextNode);
                    if (currentCol-1 < leftmostCol) leftmostCol = currentCol-1;
                }
                if (currentNode.right) {
                    const nextNode = {
                        node: currentNode.right,
                        row: currentRow+1,
                        col: currentCol+1
                    }
                    queue.push(nextNode);
                    if (currentCol+1 > rightmostCol) rightmostCol = currentCol+1;
                }

                if (colToNodeAndRow.has(currentCol)) {
                    const updated = colToNodeAndRow.get(currentCol);
                    updated.push({node: currentNode, row: currentRow});
                    colToNodeAndRow.set(currentCol, updated);
                } else {
                    colToNodeAndRow.set(currentCol, [{node: currentNode, row: currentRow}]);
                }

            }
            return [leftmostCol, rightmostCol];
        }

        const [leftmostCol, rightmostCol] = levelOrderTraversal(root);
        const result = [];
        for (let i = leftmostCol; i <= rightmostCol; i++) {
            const currentCol = colToNodeAndRow.get(i);
            const vals = currentCol.map((cell) => cell.node.val);
            // represents current array of [node:row] elements
            // colToNodeAndRow[i].sort(([a,b]))
            result.push(vals);
        }

        return result;
        
    }
}







