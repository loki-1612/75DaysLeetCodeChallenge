/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0;
    let minSoFar = prices[0]

    for (let i=1; i<prices.length; i++){
        minSoFar = Math.min(minSoFar,prices[i])
        maxProfit = Math.max(maxProfit,prices[i]-minSoFar)
    }
    return maxProfit
};