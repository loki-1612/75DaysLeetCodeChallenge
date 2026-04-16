public class Solution {
    public int Fib(int n) {
        if (n<=1)
        {
            return n;
        }

        int prev = 0;
        int curr = 1;
        for (int i=2; i<=n; i++)
        {
            int result = curr + prev;
            prev = curr;
            curr = result;
        }
        return curr;
    }
}