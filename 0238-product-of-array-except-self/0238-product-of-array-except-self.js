/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n=nums.length;
    let result = new Array(n).fill(0)
    if (n===0){
        return result
    }
    let leftProduct = new Array(n).fill(0)
    let rightProduct = new Array(n).fill(0)

    let product = 1;
    for (let i=0; i<n; i++){
        product*=nums[i];
        leftProduct[i] = product
    }

    product = 1;
    for (let i=n-1; i>=0; i--){
        product*=nums[i];
        rightProduct[i] = product
    }

    result[0] = rightProduct[1];
    result[n-1] = leftProduct[n-2];

    for (let i=1; i<n-1; i++){
        result[i] = leftProduct[i-1] * rightProduct[i+1]
    }
    return result
    
};