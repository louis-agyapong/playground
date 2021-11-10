def square(x):
    return x * x


def cube(x):
    return x * x * x


# f = square
# print(square)
# print(f(5))


def my_map(func, arg_list: list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# squares = my_map(square, [1, 2, 3, 4, 5])

# cubes = my_map(cube, [1, 2, 3, 4, 5])
# print(squares)
# print(cubes)


def logger(msg):
    def log_message():
        print("Log:", msg)

    return log_message


log_hi = logger("Hi!")
log_hi()


def html_tag(tag: str):
    def wrap_text(msg: str):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Test Headline")
print_h1("Another Headline")
