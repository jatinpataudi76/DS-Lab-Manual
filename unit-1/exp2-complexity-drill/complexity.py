# Single loop -> O(n)

n = 5
count = 0

for i in range(n):
    count += 1

print("Single loop count =", count)
print("Time complexity : O(n)")

# Nested loop -> O(n^2)

count = 0
for i in range(n):
    for j in range(n):
        count += 1

print("Nested loop count =", count)
print("Time complexity : O(n^2)")

# Halving loop -> O(log n)

count = 0
x = n

while x > 0:
    x = x // 2
    count += 1

print("Halving loop count =", count)
print("Time complexity : O(log n)")