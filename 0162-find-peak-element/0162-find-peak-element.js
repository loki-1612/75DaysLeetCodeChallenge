/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    if (nums.length === 0){
        return 0
    }
    let maxElement = nums[0]
    let maxIndex = 0

    for (let i=1; i<nums.length; i++){
        if (nums[i]>maxElement){
            maxElement = nums[i]
            maxIndex = i
        }
    }
    return maxIndex
    
};