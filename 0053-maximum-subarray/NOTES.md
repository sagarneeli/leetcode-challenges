We can use Kadane's algorithm to find the maximum subarray sum.
​
The constraint being, we want the subarray to always be largest hence whenever we encounter a negative sum we reset to zero
​
Time Complexity
Since we do a one pass over the entire array - O(N), where N being the number of elements in the array
​
Space Complexity
O(1), since we don't use any additional space apart from the input array.
​