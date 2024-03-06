def main():
    def latex_to_ti_nspire(latex_str):
        latex_str = r"{}".format(latex_str)
        if latex_str[0] == "s":
            solve = True
            latex_str = latex_str[1:]
        else: solve = False
        ti_format = latex_str.replace("{,}", ".")  # Replace "{,}" with "."
        ti_format = ti_format.replace("\\cdot", "*")  # Replace "\cdot" with "*"
        ti_format = ti_format.replace("\\ ", "")  # Remove any spaces
        ti_format = ti_format.replace("\\cos", "cos")  # Replace "\cos" with "cos"
        ti_format = ti_format.replace("\\sin", "sin")  # Replace "\sin" with "sin"
        ti_format = ti_format.replace("\\tan", "tan")  # Replace "\tan" with "tan"
        ti_format = ti_format.replace("\\alpha", "α") # Replace "\alpha" with "α"
        ti_format = ti_format.replace("\\beta", "β") # Replace "\beta" with "β"
        ti_format = ti_format.replace("\\gamma", "γ") # Replace "\gamma" with "γ"
        ti_format = ti_format.replace("\\delta", "δ") # Replace "\delta" with "δ"
        ti_format = ti_format.replace("\\theta", "θ") # Replace "\theta" with "θ"
        ti_format = ti_format.replace("\\pi", "π") # Replace "\pi" with "π"
        ti_format = ti_format.replace("\\deg", "°")  # Replace "\deg" with "°"
        ti_format = ti_format.replace("\\left(", "(") # Replace "\left(" with "("
        ti_format = ti_format.replace("\\right)", ")") # Replace "\right)" with ")"
        ti_format = ti_format.replace("\\sqrt{", "√(") # Replace "\sqrt" with "√"
        print(ti_format)
        ti_format = ti_format.replace("\\frac{", "(").replace("}{", ")/(").replace("}", ")") # Replace "\frac{}{}" with "()/()"

        # Handle exponentiation
        index = 0
        while "^" in ti_format[index:]:
            index = ti_format.index("^", index)
            ti_format = ti_format[:index] + ti_format[index:].replace("^", "^(", 1)  # Replace '^' with '^(' once
            index += 2  # Move the index forward to avoid infinite loop
            end_bracket_index = index
            while end_bracket_index < len(ti_format) and (ti_format[end_bracket_index].isdigit() or ti_format[end_bracket_index] == '.'):
                end_bracket_index += 1
            ti_format = ti_format[:end_bracket_index] + ")" + ti_format[end_bracket_index:]

    
        if solve == True:
            ti_format = "solve(" + ti_format + ")"
        
    
        return ti_format

    ti_nspire_str = latex_to_ti_nspire(input("LaTeX: "))
    print(ti_nspire_str)
if __name__ == "__main__":
    main()