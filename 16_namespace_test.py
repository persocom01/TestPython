# Demonstrates assign of variables to 3 different namespace levels: local,
# nonlocal and global.


def scope_test():

    # Local assignments do not affect anything outside the function they are
    # defined.
    def do_local():
        spam = "local spam"

    # nonlocal goes one level higher to the parent function.
    # nonlocal closure functions are an alternative to recursive functions.
    # They also tend to be faster. Details here:
    # https://towardsdatascience.com/dont-use-recursion-in-python-any-more-918aad95094c
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    # global leaves the function altogether and occupies a namespace in the
    # module.
    def do_global():
        global spam
        spam = "global spam"

    spam = "spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
