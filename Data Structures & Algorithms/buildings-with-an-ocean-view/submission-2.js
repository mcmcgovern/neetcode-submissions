class Solution {
    /**
     * @param {number[]} heights
     * @return {number[]}
     */
    findBuildings(heights) {
        const result = [];
        let rightMax = 0;
        for (let i = heights.length - 1; i >= 0; i--) {
            if (heights[i] > rightMax) {
                rightMax = heights[i];
                result.push(i);
            }
        }
        
        return result.sort((a,b) => a - b);
    }
}

// Input: heights = [4,2,3,2,1]
// 4: maxval, has ov
// 2: less than neighbor, does not have ov
// 3: 

// // overall notice that decreasing parts of an array have ov
// // notice that last index will always have an ov
// // could start from right, iterate backwards

// Output: [0,2,3,4]
