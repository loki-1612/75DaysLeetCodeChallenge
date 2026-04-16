public class Solution {
    public int Fib(int n) {
        if (n==0)
        {
            return 0;
        }
        if (n==1)
        {
            return 1;
        }
        int result = 0;
        int prev = 0;
        int curr = 1;
        for (int i=2; i<=n; i++)
        {
            result = curr + prev;
            prev = curr;
            curr = result;
        }
        return result;
    }
}