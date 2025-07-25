"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequentMinHeap(self, nums: list[int], k: int) -> list[int]:
        
        return [0]
    
    # O(n) time O(n) space
    def topKFrequentBucketSort(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums :
            count[num] = count.get(num, 0) + 1

        for pair in count.items():
            num = pair[0]
            cnt = pair[1]
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
"""
Array
Hash Table
Divide and Conquer
Sorting
Heap (Priority Queue)
Bucket Sort
Counting
Quickselect
I. MinHeap
II. (modified) Bucket Sort
"""

sol = Solution()

test_cases = [
    {
        "nums": [1, 1, 1, 2, 2, 3],
        "k": 2,
        "expected": [[1, 2], [2, 1]]
    },
    {
        "nums": [1],
        "k": 1,
        "expected": [[1]]
    },
    {
        "nums": [4, 4, 1, 1, 2, 2, 3],
        "k": 3,
        "expected": [[1, 2, 4], [4, 1, 2], [2, 4, 1], [2, 1, 4], [1, 4, 2], [4, 2, 1]]
    },
    {
        "nums": [5, 2, 5, 3, 5, 3, 1, 1, 3],
        "k": 2,
        "expected": [[3, 5], [5, 3]]
    }
]

for i, case in enumerate(test_cases):
    nums = case["nums"]
    k = case["k"]
    expected = case["expected"]

    print(f"\nRunning test case {i + 1}: nums={nums}, k={k}")

    try:
        result_bucket = sol.topKFrequentBucketSort(nums, k)
        assert result_bucket in expected
        print(f"  ✅ BucketSort passed: {result_bucket}")
    except AssertionError:
        print(f"  ❌ BucketSort failed: got {result_bucket}, expected one of {expected}")
    except Exception as e:
        print(f"  💥 BucketSort error: {e}")

    try:
        result_heap = sol.topKFrequentMinHeap(nums, k)
        assert result_heap in expected
        print(f"  ✅ MinHeap passed: {result_heap}")
    except AssertionError:
        print(f"  ❌ MinHeap failed: got {result_heap}, expected one of {expected}")
    except Exception as e:
        print(f"  💥 MinHeap error: {e}")

print("\nTesting complete.")