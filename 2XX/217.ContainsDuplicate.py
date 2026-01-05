# author : fakhripm

class SolutionSet:
    # Using Set
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
    # Time Complexity: O(n)
    # Space Complexity: O(n)


class SolutionSetOneLiner:
    # Set Conversion 
    # One-liner
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    # Time Complexity: O(n)
    # Space Complexity: O(n)


class SolutionSort:
    # Sorting Approach
    # Mutates the input list
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
    # Time Complexity: O(n log n)
    # Space Complexity: O(n) in phyton due to sort implementation, O(1) conceptually


class SolutionHashmap:
    # Hashmap Frequency Count
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_count = {}
        for num in nums:
            if num in num_count:
                return True
            num_count[num] = 1
        return False
    # Time Complexity: O(n)
    # Space Complexity: O(n)


class SolutionBruteForce:
    # Brute Force
    # Not efficient for large datasets
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)