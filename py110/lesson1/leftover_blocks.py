def leftover_blocks(total_blocks):
    layer = 0
    sum = 0
    for blocks in range(total_blocks + 1):
        if blocks - sum == layer ** 2:
            layer += 1
            sum = blocks

    return total_blocks - sum


print(leftover_blocks(0) == 0)
print(leftover_blocks(1) == 0)
print(leftover_blocks(2) == 1)
print(leftover_blocks(4) == 3)
print(leftover_blocks(5) == 0)
print(leftover_blocks(6) == 1)
print(leftover_blocks(14) == 0)
