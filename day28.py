#Day 28(f-strings)

'''before fstring this method was used'''
intro= "Hello my name is {} and I am from {}"
name="Abdullah"
country="Pakistan"
print(intro.format(name,country))

value=30.29876
string=f"The amount is: {value:.2f}" #used for rounding of to 2 digits after decimal
print(string)

intro= f"Hello my name is {{}} and I am from {{}}" #if you want curly braces in your string
print(intro)
