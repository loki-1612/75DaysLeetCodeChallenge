/**
 * @param {number[]} nums
 * @return {number[]}
 */


var sortArray = function (nums) {

    function merge(nums, left, mid, right){
        let n1 = mid-left + 1;
        let n2 = right - mid;

        let l1 = nums.slice(left, left + n1)
        let l2 = nums.slice(mid + 1, mid + 1 + n2)

        let i = 0;
        let j = 0;
        let counter = left;

        while (i < n1 && j < n2) {
            if (l1[i] < l2[j]) {
                nums[counter] = l1[i]
                i++
            } else{
                nums[counter] = l2[j]
                j++
            }
            counter++
        }

        while (i < n1) {
            nums[counter] = l1[i]
            i++
            counter++
        }
        while (j < n2) {
            nums[counter] = l2[j]
            j++
            counter++
        }
    }

    function mergeSort(nums, left, right){
        if (left < right){
            let mid = Math.floor((left + right) / 2)
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)
        }
    }


    mergeSort(nums, 0, nums.length - 1)
    return nums;
};