def auswertung(word, interpretation_list):
    #this function interpretes a given word and returns its boolean value and paranthesis depth
    #  if it is a valid expression. Else it raises an Exception
    # we first define the amount of sentence letters of form xi, i being any natural number in the word.
    T = True
    F = False

    if word == "":
        return (True, 0)

    def get_list_of_brackets(word):
        #this function returns a list of all brackets in the word in the order of appearance
        list_of_brackets = []
        bracket_set = ("(", ")", "[", "]")
        for character in word:
            if character in bracket_set:
                list_of_brackets.append(character)
            else:
                continue
        return list_of_brackets

    def depth_calculator(stack):
        #this function calculates the amount of opening brackets that are in a stack at
        # the same time (paranthesis depth). It requires the stack of the  function
        count = 0
        for element in stack:
            if element in ("(", "["):
                count += 1
        return count

    def get_last_opening_bracket_match(stack):
        #this function returns the bracket match index of the last opening bracket on the stack
        bracket_list = ["(", "["]
        try:
            return bracket_list.index(stack[-1])
        except IndexError:
            raise Exception("...")

    def check_correct_brackets_and_return_depth(word):
        opening_brackets_list = ["(", "["]
        closing_brackets_list = [")", "]"]
        depths = [0]
        stack = []
        bracket_match = 0
        #first, we need to get a list of all the brackets that appear in their respective orders.
        list_of_brackets = get_list_of_brackets(word)
        if len(list_of_brackets) == 0:
            return max(depths)
        elif len(list_of_brackets) == 1:
            raise Exception("..")
        # a word cannot have a closing bracket as first bracket, neither an opening bracket
        # as last bracket
        elif list_of_brackets[0] in closing_brackets_list:
            raise Exception("Unzulaessige Formel: Klammern passen nicht zusammen:")
        elif list_of_brackets[-1] in opening_brackets_list:
            raise Exception("Unzulaessige Formel: Klammern passen nicht zusammen:")
        else:
            for bracket in list_of_brackets:
                if bracket in opening_brackets_list:
                    stack.append(bracket)
                elif bracket in closing_brackets_list:
                    depths.append(depth_calculator(stack))
                    bracket_match = get_last_opening_bracket_match(stack)
                    if bracket != closing_brackets_list[bracket_match]:
                        raise Exception("Unzulaessige Formel: Klammern passen nicht zusammen: "
                        + bracket + " gefunden; " + closing_brackets_list[bracket_match] + " erwartet.")
                    else:
                        stack.pop()
            if len(stack) > 0:
                raise Exception("Unzulaessige Formel: Klammern passen nicht zusammen: ...")
            else:
                return max(depths)

    y = check_correct_brackets_and_return_depth(word)

    def split_across_delimeters(expression):
        #this function splits an expression across delimeters &", "|"
        output = []
        current_formula = ""
        for character in expression:
            if character == "&" or character == "|":
                output.append(current_formula)
                output.append(character)
                current_formula = ""
            else:
                current_formula = current_formula + character
        if len(current_formula) > 0:
            output.append(current_formula)
        return output

    def letter_interpreter(letter_formula):
        booldict = {"True": True, "False": False, "T": True, "F": False}
        #this function interpretes a sentence letter of form xi (i any natural number) and returns
        #the value of interpretation_list[i]
        if letter_formula in ("True", "False", "T", "F"):
            return booldict[letter_formula]
        index = ""
        for character in letter_formula:
            if character.isdigit():
                index += character
        if index == "":
            raise Exception("Unzulässiger Satzbuchstabenindex: ... ")
        index = int(index)
        try:
            return interpretation_list[index]
        except IndexError:
            raise Exception("Unzulaessiger Satzbuchstabenindex: ...")

    def formula_evaluator(formula):
        # print("this formula is passed")
        # print(formula)
        if formula in ("T", "F", "True", "False"):
            return formula
        elif formula == "":
            raise Exception("Unzulaessiger Satzbuchstabenindex: ...")
        elif formula.count("x") > 1:
            raise Exception("Unzulaessiger Satzbuchstabenindex: ...")
        elif formula[-1] == "!":
            raise Exception("Unzulaessiger Satzbuchstabenindex: ...")
        #now I should have a formula containing exclamation marks and at most
        # one sentence letter.
        if formula.count("!") == 0:
            return str(letter_interpreter(formula))
        # print("before")
        # print(formula)
        formula_list = formula.split("!")
        # print("after")
        # print(formula_list)
        output = not letter_interpreter(formula_list[-1])
        formula_list.remove("")
        #verification !!
        while "" in formula_list:
            output = not output
            formula_list.remove("")
        if output == T:
            return "T"
        elif output == F:
            return "F"

    def unparanthesized_expression_evaluator(expression):
        #first split the expression across delimeters "&", "|":
        #(TODO) rearrange list to respect order "and" before "or". EDIT: handled by order of while loops
        booldict = {"T": True, "F": False, "True": True, "False": False,
                    "or": lambda left, right: left or right,
                    "and": lambda left, right: left and right}

        expression_list = split_across_delimeters(expression)
        # print("this is expression list at beginning")
        # print(expression_list)
        if not expression_list:
            raise Exception("...")
        expression_list = ["and" if x == "&" else "or" if x == "|" else x for x in expression_list]
        if expression_list[0] in ("and", "or"):
            raise Exception("Unzulaessiger Satzbuchstabenindex: ... ")
        elif expression_list[-1] in ("and", "or"):
            raise Exception("Unzulaessiger Satzbuchstabenindex: ...")
        for formula in expression_list:
            if formula == "and" or formula == "or":
                continue
            else:
                #should give back "T" or "F"
                expression_list[expression_list.index(formula)] = formula_evaluator(formula)
         #   expression_list = rearrange_and_before_or(expression_list)
        # print(expression_list)
        # print("just printed expression list")
        expression_list = [booldict[formula] for formula in expression_list]

        if len(expression_list) == 1:
            return str(expression_list[0])

        # print("this is expression list after booldict")
        # print(expression_list)
        #start evalutation :
        while booldict["and"] in expression_list:
            # print("and op from this")
            # print(expression_list)
            index = expression_list.index(booldict["and"])
            left_index = index - 1
            right_index = index + 1
            expression_list[index] = expression_list[index](expression_list[left_index], expression_list[right_index])
            # print("does this work?")
            # print(expression_list)
            del expression_list[right_index]
            del expression_list[left_index]
            # print("and op to this")
            # print(expression_list)
        # print("this is expression_list after and")
        # print(expression_list)
        while booldict["or"] in expression_list:
            # print("or op from this")
            # print(expression_list)
            index = expression_list.index(booldict["or"])
            left_index = index - 1
            right_index = index + 1
            expression_list[index] = expression_list[index](expression_list[left_index], expression_list[right_index])
            del expression_list[right_index]
            del expression_list[left_index]
            # print("or op to this")
            # print(expression_list)

        # print("about to return this")
        # print(expression_list)
        return str(expression_list[0])

    # start interpretation
    stack = []
    unparanth_expr_of_curr_depth = ""
    allowed = ("|", "&", "(", "[", "]", ")", "!")
    current_index = -1
    for character in word:
        current_index += 1
        if character in ("(", "["):
            if current_index != 0:
                if word[current_index - 1] not in allowed:
                    raise Exception("...")
            stack.append(character)
            stack.append(unparanth_expr_of_curr_depth)
            unparanth_expr_of_curr_depth = ""
        elif character in (")", "]"):
            if current_index != (len(word) - 1) :
                if word[current_index + 1] not in allowed:
                    raise Exception("...")
            bool_interpretation = unparanthesized_expression_evaluator(unparanth_expr_of_curr_depth)
            unparanth_expr_of_curr_depth = stack[-1] + str(bool_interpretation)
            stack.pop()
            stack.pop()
        else:
            unparanth_expr_of_curr_depth += character

    # print("expression to be passed to eval")
    # print(unparanth_expr_of_curr_depth)
    # print(unparanthesized_expression_evaluator(unparanth_expr_of_curr_depth))
    booldictionary = {"T": True, "F": False, "True": True, "False": False}
    x = booldictionary[unparanthesized_expression_evaluator(unparanth_expr_of_curr_depth)]

    return (x, y)
