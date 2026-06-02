/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        if(!root) return true;

        return this.isBalanced(root.left) && this.isBalanced(root.right) && Math.abs(this.maxHeight(root.left) - this.maxHeight(root.right)) <= 1;
    }

    maxHeight(root) {
        if(!root) return 1;

        return 1 + Math.max(this.maxHeight(root.left), this.maxHeight(root.right))
    }
}

/*

find max height of left and right, see if they differ by 1+

*/