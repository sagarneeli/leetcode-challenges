Complexity Analysis
Let n be the length of cookies.
​
Time complexity: O(k + n)
- The algorithm attempts to distribute each of the `n` cookies to each of the `k` children, resulting in at most
​
Space complexity: O(k+n)
​
The array distribute represents the status of `k` children, thus taking up O(k) space.
The space complexity of a recursive call depends on the maximum depth of the recursive call stack, which is at most `n`. As each recursive call increments i by 1. Therefore, at most `n` levels of recursion will be created, and each level consumes a constant amount of space.
(