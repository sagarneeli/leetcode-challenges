We can use Kadane's algorithm to find the maximum subarray sum.
​
Kadane's algorithm runs one for loop over the array and at the beginning of each iteration, if the current sum is negative, it will reset the current sum to zero. This way, we ensure a one-pass and solve the problem in linear time.
​
Time Complexity
Since we do a one pass over the entire array - O(N), where N being the number of elements in the array
​
Space Complexity
O(1), since we don't use any additional space apart from the input array.
​