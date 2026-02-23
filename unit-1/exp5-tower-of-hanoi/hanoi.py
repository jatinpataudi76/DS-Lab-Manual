count = 0

def hanoi(n, src, aux, dst):
    global count

    if n == 1:
        count += 1
        print("Move disk 1 from", src, "to", dst)
        return

    hanoi(n-1, src, dst, aux)
    count += 1
    print("Move disk", n, "from", src, "to", dst)
    hanoi(n-1, aux, src, dst)


print("Moves for n = 3")
hanoi(3, 'A', 'B', 'C')
print("Total moves =", count)

# Complexity : O(2^n)