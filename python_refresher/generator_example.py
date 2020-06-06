# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
print('\n')
do_something = 4
do_something += 3
print(do_something)
print('\n')

# Now go back to generating more even numbers.
for i in range(20):
    print(next(my_gen))
