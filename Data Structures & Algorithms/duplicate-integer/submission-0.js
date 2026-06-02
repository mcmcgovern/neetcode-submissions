class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = new Set();

        nums.forEach((num) => seen.add(num));

        return nums.length !== seen.size;
    }
}
