/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    function reverse(nums,left,right){
        while (left<=right){
            let temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++
            right--
        }
    }
    k%=nums.length
    reverse(nums,0,nums.length-1)
    reverse(nums,0,k-1)
    reverse(nums,k,nums.length-1) 
};