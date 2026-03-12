/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let prefixSum = 0;
    let count = 0;
    let freq = {0:1}
    for (let i=0; i<nums.length; i++){
        prefixSum+=nums[i]
        let diff = prefixSum - k
        count += freq[diff] || 0
        freq[prefixSum] = (freq[prefixSum] || 0)+1
    }
    return count
    
};