# main.py

import sys
from pkg.calculator import Calculator # type: ignore
from pkg.render import render # type: ignore


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: pythin main.py "<expression>"')
        print('Example: pythong main.py "3 + 5"')
        return
    
    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
