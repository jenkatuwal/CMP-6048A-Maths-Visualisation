import re


class RendTranslate:

    def __init__(self, passed_string):
        # Raw input
        self.raw_string = passed_string

        # String for Renderer
        self.rend_string = ""

        self.num_to_rend()

    def num_to_rend(self):
        # If you were to separate using operators you could attempt the below
        # pattern = r'\*|\+|\-|\/'
        # digits = re.split(pattern, self.raw_string)

        # Current implementation of this code only works on whitespace
        digits = re.split(' ', self.raw_string)
        print(digits)
        new_string = ''

        # Attempting to implement parenthesis matching
        stack = []
        print("input", self.raw_string)
        for index, element in enumerate(digits):
            if '(' in element:
                digits[index] = str(element.split('(')[1])
                stack.append(element)
            if ')' in element:
                digits[index] = str(element.split(')')[0])
                stack.pop(0)
        for index, element in enumerate(digits):
            if '/' in element:
                digits.pop(index)
                string = '$frac' + '{' + digits.pop(index - 1) + '}' + '{' + digits.pop(index - 1) + '}'
                digits.insert(index - 1, string)
                print("digits:", digits)
        for i in digits:
            new_string += i
        print(stack)
        print("new string", new_string)

        # if (stack is not )
        # test print output
        # print('search string:', search_string)
        # return search_string

    def convert_to_proper_format(self):
        return f'{self.raw_string} >> placeholder string'

    def matching_parenthesis(self):
        stack = []


if __name__ == '__main__':
    # TURN INPUT: 1 / 2 or (1 / 2) -> ${\frac{1}{2}}$
    userinput = "(20 / 40) * 5 + 2"
    rendTrans = RendTranslate(userinput)
