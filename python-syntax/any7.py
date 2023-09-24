def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    return any( num == 7 for num in nums )

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

