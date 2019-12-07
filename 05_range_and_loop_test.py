texts = ['mary', 'had', 'a', 'little', 'lamb']

# The reason this doesn't work is because the current element in a loop cannot
# overwrite itself. To overwrite the current element use list[index] of the
# element.
for t in texts:
    t = t.upper()
print(texts)
print()

# May be better to use print(list(enumerate(texts))).
# Demonstrates writing over current element using lsit index.
for t in range(len(texts)):
    texts[t] = texts[t].upper()
    print(t, texts[t])
    texts[t] = texts[t].lower()
print()

# Interesting results.
print(range(10))

# Demonstrates the 4 parameters of the range argument, start, end and step.
rangelist = range(1, 3, 1)
print(rangelist)
print()

searchtext = ['a', 'litte']

# Changing the searchtext array gives insight as to how python iterates the
# search.
for t in range(len(texts)):
    for s in range(len(searchtext)):
        if searchtext[s] == texts[t]:
            print('mary\'s friend')
            # break breaks the innermost loop. In this case the outer loop
            # still runs 5 times,
            # but break makes this loop only work once even if multiple
            # searchtext are correct.
            break
    # This else is for the for loop and executes so long as break does not
    # execute.
    else:
        print('checking for lambs...')
    if t < len(texts) - 1:
        # continue skips the code below it and starts with the next iteration.
        continue
    print('end of check')
    print()

# Demonstrates while loops.
i = 3
while i >= 0:
    print(i)
    i -= 1
