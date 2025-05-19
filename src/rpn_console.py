from rpn import RPN as calc

greeting = "Welcome to the RPN calculator!"
prompt = "Enter a number or an operator (+, -, *, /, %, p, c (clear), q (quit)): "

while True:
    try:
        entry = input(prompt) 
        if entry.lower() == "q":
            print("Goodbye!")
            break
        elif entry.lower() == "c":
            calc.enter(calc,entry)
        else:
            result = calc.enter(calc,entry)
            print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")       
