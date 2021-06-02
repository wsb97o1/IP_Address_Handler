# IP Address handler

### Songbo Wu

## Approach/Design
I use a dictionary/hashtable to store all the ip addresses called as key and times of calling as value, and keep tracking these key value pairs while the `request_handled()` function is called. 
When we want the top 100 ip addresses, for each ip addresses in the dictionary, we keep a minimum heap and update each into the heap and then we get the top 100 ip addresses in heap. 
I put most of the operations in the function `top100()` and made `request_handled()` only takes constant time because in this system, `request_handled()` would be called way more than `top100()` and the overall performance would increase by doing so, but if the requirement emphasizes calling `top100()` any time during the stream of requests, then separate the operations into two functions might be a better idea. 
Lastly, for clear, I simply empty the dictionary for a new day.

## Runtime Complexity
The complexity for `request_handled()` is O(1), since it only involves two read/write operation for a dictionary and both of them takes O(1) of time. 
The complexity for `top100()` is O(nlog100). For each ip addresses, updating it into the minimum heap takes the time of layers of the heap, which is log100. And there are n ip addresses total, so it takes O(nlog100) time.
The complexity for `clear()` is O(1), since it just clear all the keys and values in the dictionary and the reset operation takes constant time.

## Other Approaches Considered
The method I considered is to find maximum among the ip addresses like in the bubble sort and do this 100 times to get top 100 ip addresses. However it takes O(n\*100) and since n is very large(20 million), this method is not going to meet the requirement.

## Testing
The file `test.py` contains a simple sample testing case for each functions to show they works, running it by using `pytest test.py`. Ideally, I would use a unit test along with a load test for testing this comprehensively. The unit testing is to test each functionality works, while the load test is to test the performance and the throughput under huge load.

## Future Improvement
If I have more time, I would add input check or handle exception for invalid ip address. 
Also I would try to improve or at least consider how to improve the memory space, since currently I have to store all ip addresses. Then for 20 million ip addresses, it would take many GBs to store it and that might be a problem. For the speed, I think the consideration of edge cases might speed up the performance. Introducing concurrency feature would also increase the performance facing the huge load while requiring extra effort on handling synchronization.