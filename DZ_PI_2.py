from DZ_PI_1 import Stack

def check_balance(example_string):
    stack = Stack()
    pairs = [(')','('), ('}','{'), (']','[')]
    identical_brackets = dict(pairs)
    for bracket in example_string:
        if bracket in '({[':
            stack.push(bracket)
        elif bracket in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != identical_brackets[bracket]:
                return False
    return stack.is_empty()

def get_result(test_string):
    result = check_balance(test_string)
    return "Сбалансированно" if result else "Несбалансированно"

if __name__ == "__main__":
    example_strings = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]

    for string in example_strings:
        print(get_result(string))