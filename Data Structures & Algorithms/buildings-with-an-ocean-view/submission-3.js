class Solution {
    /**
     * @param {number[]} heights
     * @return {number[]}
     */
    findBuildings(heights) {
        const n = heights.length;
        let maxRight = heights[n-1];
        const buildingsWithOV = [n-1];

        for (let i = n-2; i >= 0; i--) {
            if (heights[i] > maxRight) {
                maxRight = heights[i];
                buildingsWithOV.push(i);
            }
        }
        return buildingsWithOV.reverse();
    }
}
