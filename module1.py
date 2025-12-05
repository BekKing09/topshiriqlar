# 1. factorial(n) - bitta butun sonni qabul qilib, uning factorialini qaytaradi.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# natija = factorial(5)
# print(natija)




def fibonachi(n):
    if n <= 0:
        return "Iltimos musbat butun son kiriting."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)  
   
    
   

natija = fibonachi(5)
print(natija)





# def upper_matn(matn):
#     return matn.upper
# natija = upper_matn()
# print(natija)
