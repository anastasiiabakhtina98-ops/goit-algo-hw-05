import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    upper_bound = arr[left] if left < len(arr) else None
    return (iterations, upper_bound)

# Generate test array
def generate_sorted_float_array(size=20, min_val=0.0, max_val=100.0):
    arr = [random.uniform(min_val, max_val) for _ in range(size)]
    arr.sort()
    return arr

if __name__ == "__main__":
    test_array = generate_sorted_float_array(20, 0.0, 100.0)
    print("Sorted array:", [f"{x:.2f}" for x in test_array])
    print()
    
    for target in test_array:
        iterations, upper_bound = binary_search(test_array, target)
        print(f"Looking for {target:.2f}:")
        print(f"  Iterations: {iterations}")
        print(f"  Upper limit: {upper_bound:.2f}")
        print()
