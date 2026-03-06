import sys 

# --- PART A: Stack ADT ---
class StackADT:
    def __init__(self):
        self._items = []
        
    def push(self, x):
        self._items.append(x)
        
    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        return None    
    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        return None
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
# --- PART B: Factorial & Fibonacci ---
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0: return 1 #Base case
    return n * factorial(n-1)

naive_calls = 0
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1: return n
    return fib_naive(n-1) + fib_naive(n-2)

memo_calls = 0
memo = {}
def fib_memo(n):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# --- PART C: Tower of Hanoi ---
# Using StackADT to store and print moves
hanoi_stack = StackADT()

def hanoi(n, source, aux, dest):
    if n == 1:
        move = f"Move disk 1 from {source} to {dest}"
        hanoi_stack.push(move)
        print(move)
        return
    hanoi(n-1, source, aux, dest)
    move = f"Move disk {n} from {source} to {dest}"
    print(move)
    hanoi_stack.push(move)
    print(move)
    hanoi(n-1, aux, source, dest)
    
# --- PART D: Recursive Binary Search ---
def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)
    
#  ---Main Execution  for output.txt ---
def main():
    print("--- PART B: Factorial ---") 
    for n in [0, 1, 5, 10]:
        print(f"Factorial of ({n}): {factorial(n)}")  
        
    print("\n--- PART B: Fibonacci ---")
    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls, memo
        naive_calls, memo_calls, memo = 0, 0, {}
        ans_m = fib_memo(n)
        ans_n = fib_naive(n)
        print(f"n={n} | Result: {ans_m} | Naive Calls: {naive_calls} | Memo Calls: {memo_calls}")
        
    print("\n--- PART C: Tower of Hanoi (N=3) ---")    
    hanoi(3, "A", "B", "C")
    print("\n--- PART D: Recursive Binary Search ---")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for k in [7, 1, 13, 2]:
        print(f"Searching {k}: Index {binary_search(arr, k, 0, len(arr)-1)}")
        print(f"Searching empty[]: {binary_search([], 5, 0, -1)}")
        
if __name__ == "__main__":
    main()