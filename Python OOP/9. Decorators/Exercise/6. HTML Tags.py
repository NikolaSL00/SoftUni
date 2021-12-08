# Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with the given tag and return the new result. For more clarification, see the examples below

def tags(param):
    def decorator(func):
        tag_open = f'<{param}>'
        tag_close = f'</{param}>'

        def wrapper(*args):
            return f'{tag_open}{func(*args)}{tag_close}'

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))  # <p>Hello you!</p>


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))  # <h1>HELLO</h1>
