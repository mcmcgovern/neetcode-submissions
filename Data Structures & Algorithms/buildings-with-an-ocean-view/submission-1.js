class Solution {
    /**
     * @param {number[]} heights
     * @return {number[]}
     */
    findBuildings(heights) {
        const result = [];
        const stack = [];
        for (let i = heights.length - 1; i >= 0; i--) {
            if (stack.length === 0) {
                stack.push([heights[i], i]);
            } else {
                const prevBuilding = stack.pop();
                if (heights[i] > prevBuilding[0]) {
                    stack.push([heights[i], i]);
                    result.push(prevBuilding[1]); // add index to the 
                } else {
                    stack.push(prevBuilding);
                }
            }
        }
        if (stack.length !== 0) result.push(stack.pop()[1]);
        // return result;
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
