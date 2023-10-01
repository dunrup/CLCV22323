    Based on today’s reading, what’s the difference a variable, a parameter, and an argument.

A **variable** is a name that refers to a value. 
Assignment statements create a new variable and give it a value. 
The variable's name is to the left of the '=' sign.
For example, below I create the variable "example" and assign it the string value "example string value."

      example = "example string value"

A **parameter** is a specific type of variable that is defined with a function.
Arguments are assigned to parameters.
Parameters (like variables) are locally defined.
For example, below I create a function "fun," with the parameters "wee" and "woo".

      def fun(wee, woo):
        goodtime = wee + woo
        print(goodtime)

Calling _fun_ will now print the two arguments that go in, 
so calling fun('yipee', 'yahoo') would print

      yipeeyahoo


  An **argument** in the function's input. 
  Above, 'yipee' and 'yahoo' were the arguments in the function 'fun'
