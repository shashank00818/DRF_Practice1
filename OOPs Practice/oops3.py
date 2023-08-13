def decorated_docstring(function):
    function.__doc__ += '\n Hi George, I''m a simple Decorator.'
    return function


def my_function(string1):
    """Return the string."""
    return string1


def main():
    myFunc = decorated_docstring(my_function)
    myFunc('Hai')
    help(myFunc)


if __name__ == "__main__":
    main()