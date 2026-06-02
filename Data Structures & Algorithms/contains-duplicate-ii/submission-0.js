class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums, k) {
        if(nums === undefined || nums.length < 2) return false;

        let window = new Set();
        let L = 0;

        for (let R = 0; R < nums.length; R++) {

            // if our window size is too big, remove the left element and advance boundary
            if(R - L > k) {
                window.delete(nums[L]);
                L++;
            }

            // if we have already seen the current value we are looking at, it is a duplicate within window range
            if(window.has(nums[R])) return true;

            window.add(nums[R]);
        }

        return false;
    }
}

/*
it sounds like not only are we considering if the input array has duplicates
but also we are evaluating the distance between the duplicates

so if the matching numbers exist, they must also be relatively close together
at least enough so that the distance is less than or equal to the target k value

naiively we can do a double for loop to check every pair and check the indices
the best solution should involve a sliding window where the window can be no larger than k


*/