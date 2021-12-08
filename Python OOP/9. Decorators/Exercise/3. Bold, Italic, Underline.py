# Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.
import functools


def make_underline(func):
    open_u_tag = '<u>'
    close_u_tag = '</u>'

    @functools.wraps(func)
    def wrapper(*args):
        return f'{open_u_tag}{func(*args)}{close_u_tag}'

    return wrapper


def make_italic(func):
    open_i_tag = '<i>'
    close_i_tag = '</i>'

    @functools.wraps(func)
    def wrapper(*args):
        return f'{open_i_tag}{func(*args)}{close_i_tag}'

    return wrapper


def make_bold(func):
    open_b_tag = '<b>'
    close_b_tag = '</b>'

    @functools.wraps(func)
    def wrapper(*args):
        return f'{open_b_tag}{func(*args)}{close_b_tag}'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


# <b><i><u>Hello, Peter</u></i></b>


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
# <b><i><u>Hello, Peter, George</u></i></b>
