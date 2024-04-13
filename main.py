from functools import reduce


def factorial(n):
    fac = lambda n: n * factorial(n - 1) if n > 1 else 1
    return fac(n)


def ShortConcat(strings):
    concatenate = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)
    return concatenate(strings)


def cumulative_sum_of_squares(list_of_lists):
    return list(
        map(
            lambda sublist: (
                lambda even_numbers: (
                    lambda squares: sum(squares)  # Correct usage of sum here
                )(list(map(lambda x: x ** 2, even_numbers)))
            )(list(filter(lambda x: x % 2 == 0, sublist))),
            list_of_lists
        )
    )


def count_palindromes(list_of_lists):
    return list(map(lambda sublist: len(list(filter(lambda x: x == x[::-1], sublist))), list_of_lists))


def main():
    # Q9
    print(factorial(6))

    # Q10
    strings = ['Hello', 'world', 'this', 'is', 'a', 'test']
    result = ShortConcat(strings)
    print(result)

    # Q11
    test_data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = cumulative_sum_of_squares(test_data)
    print(result)

    # Q12
    nums = [1, 2, 3, 4, 5, 6]
    sum_squared = reduce(lambda acc, x: acc + x, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
    print(sum_squared)

    # Q13
    test_data = [['abc', 'madam', '12321'], ['racecar', 'hello'],
                 ['it', 'aba', 'car', 'or', 'dad', 'cat']]
    result = count_palindromes(test_data)
    print(result)

    # Q14
'''
The term "lazy evaluation," also known as "deferred execution,"
refers to a programming strategy where the evaluation of an expression is delayed until its value is actually needed. 
This contrasts with "eager evaluation," where expressions are evaluated as soon as they are bound to a variable. 
In the context of the Python program in the question,
lazy evaluation can be observed with the use of Python's generators and list comprehensions.

Explanation of the Program:
The program defines two functions, generate_values() and square(x).
Let’s break down how each part of the program illustrates lazy vs. eager evaluation:
1. Eager Evaluation:
print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)
generate_values() is a generator function that yields values one at a time. 
When called with list(generate_values()), it immediately generates all its values. 
The list() function forces the generator to execute eagerly, producing all its values at once. 
This is evidenced by the immediate printing of "Generating values..." followed by the generation of all values.
[square(x) for x in values]: 
This list comprehension then takes the eagerly evaluated list of values and applies the square function to each element. 
The squaring of each number is also done eagerly; each number is processed in sequence,
and "Squaring x" is printed for each element before moving to the next.
2. Lazy Evaluation:
print('/nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)
[square(x) for x in generate_values()]: In this list comprehension, generate_values() is used directly. 
Unlike the eager version, there is no intermediate conversion to a list.
This means the values are generated one at a time, on demand.
Each value from the generator is produced only when the next iteration of the list comprehension occurs.
Each number is yielded from the generator, immediately squared (as indicated by the "Squaring x" print),
and then the next number is processed.
The process is lazy because the generation and squaring of each number,
are deferred until it's actually needed for the next step of the list comprehension. 
The generator does not generate the next value until the current one has been processed and squared.
       
 '''


if __name__ == "__main__":
    main()
