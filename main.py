def brackets(b_str):
    if len(b_str) % 2:
        print('Несбалансированно')
    else:
        from stack import Stack
        my_brackets = Stack()
        for element in b_str:
            try:
                previos_element = my_brackets.peek()
            except KeyError:
                pass
            my_brackets.push(element)
            if (my_brackets.peek() == ']' and previos_element == '[') \
                    or (my_brackets.peek() == ')' and previos_element == '(') \
                    or (my_brackets.peek() == '}' and previos_element == '{'):
                my_brackets.pop()
                my_brackets.pop()
        if list(my_brackets.stack.values()) == []:
            print('Сбалансированно')
        else:
            print('Несбалансированно')
        return list(my_brackets.stack.values())


if __name__ == '__main__':

    our_brackets = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]
    for element in our_brackets:
        brackets(element)
