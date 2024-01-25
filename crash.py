# # Functions
# #its a rule for taking zero or more inputs and returning a corresponding output
# # block of code which only runs when its called
# # defined using the def keyword
#
# def my_name(lname, fname):
#     print(lname +" "+ fname)
#
# my_name("Kelvin", "Ekisa")
#
# def my_family(*names):
#     print("My beautiful wife is " + names[0])
# my_family("Mrs Ruth Mukiri", "Salem", "Jair", "Serena")
#
# def my_friends(friends):
#     for x in friends:
#         print(x)
#
# names =["John Pombe", "FAith orokpo", "Pius Mathew", "Jane karim", "Messi Lionel"]
# my_friends(names)
#
# def my_math(x):
#     return 5*x
#
# print(my_math(3))
# print(my_math(10))
# print(my_math(12))
#
# #the Pass Statement
# # python funvtions cannot be empty, for some reasons you can use the pass statement.
#
# def my_health():
#     pass

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("recursion Example results")
tri_recursion(8)
