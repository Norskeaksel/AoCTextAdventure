def math_mode():
    print("Entering math mode. To escape, enter an invalid expression.")
    while True:
        expression = input(": ")
        try:
            answer = eval(expression)
            print(expression, "=", answer)
        except (NameError, SyntaxError):
            print(f"{expression} is an invalid expression. Exiting math mode")
            break
