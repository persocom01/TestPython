# Demonstrates printing of information in embedded lists or dictionaries.
# Also demonstrates reversed function to reverse the order.
months_2018 = [[2018, 'January'], [2018, 'Febuary'], [2018, 'March'], ]
for x, y in reversed(months_2018):
    print(y, x)

# Trying x, y, z here will not work.
for y, x in enumerate(months_2018):
    print(y, x)

# Demonstrate typical use of enumerate, in this case starting from 1 instead of 0.
numbered = dict(enumerate(months_2018, 1))
print(numbered)

# Demonstrates use zip function to link two lists together.
questions = ['age', 'sex']
answers = [9, 'M']
for x, y in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(x, y))

# Demonstrates use zip function combine and unpack two lists.
# Repeat of technique covered in 9_list_comprehension.py
q_and_a = list(zip(questions, answers))
print(q_and_a)

questions, answers = zip(*q_and_a)
print(questions)
print(answers)
