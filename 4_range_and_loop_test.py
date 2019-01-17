texts = ['mary', 'had', 'a', 'little', 'lamb']

# Normally better to use print(list(enumerate(texts))).
for t in range(len(texts)):
    print(t, texts[t])
    if t == len(texts) - 1:
        print('')

# Interesting results.
print(range(10))

# Demonstrates the 4 parameters of the range argument, start, end and step.
rangelist = [x for x in range(1, 3, 1)]
print(rangelist, '\n')

searchtext = ['a', 'litte']

# Changing the searchtext array gives insight as to how python iterates the search.
for t in range(len(texts)):
    for s in range(len(searchtext)):
        if searchtext[s] == texts[t]:
            print('mary\'s friend')
            # break breaks the innermost loop. In this case the outer loop still runs 5 times,
            # but break makes this loop only work once even if multiple searchtext are correct.
            break
    # This else is for the for loop and executes so long as break does not execute.
    else:
        print('checking for lambs...')
    if t < len(texts) - 1:
        # continue skips the code below it and starts with the next iteration.
        continue
    print('end of check\n')
