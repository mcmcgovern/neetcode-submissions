/**
 * // Definition for a Node.
 * function Node(val) {
 *    this.val = val;
 *    this.left = null;
 *    this.right = null;
 *    this.parent = null;
 * }
 */
class Solution {
    /**
     * @param {Node} p
     * @param {Node} q
     * @return {Node} 
     * 3-5, 5-12-1, 1-3, 3-5, 5-12-1, 3-5
     * 12-1, 1-3, 3-5, 5-12-1, 1-3, 3-5
     */
    lowestCommonAncestor(p, q) {
        const phead = p;
        const qhead = q;
        while (p !== q) {
            if (p.parent === null) {
                p = qhead;
            } else {
                p = p.parent;
            }
            if (q.parent === null) {
                q = phead;
            } else {
                q = q.parent;
            }
            
        }
        return p; // both nodes now point at LCA
    }
}
