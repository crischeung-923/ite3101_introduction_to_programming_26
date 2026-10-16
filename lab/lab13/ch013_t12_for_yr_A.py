phrase = "A bird in the hand..."

# Add your for loop


# Don't delete this print statement!
print()
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == "A" or char == "a":       # <-- 缩进 1 次 (4个空格)
        print('X', end=', ')             # <-- 缩进 2 次 (8个空格)
    else:                                # <-- 缩进 1 次，与 if 对齐
        print(char, end=" ")             # <-- 缩进 2 次，与上面 print 对齐

# Don't delete this print statement!
print()