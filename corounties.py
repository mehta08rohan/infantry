# # def finder(x):
# #     while True:
# #         inputText = yield
# #         if x in inputText:
# #             print(inputText)
# #
# # a = finder('Rohan')
# # next(a)
# # a.send('Rohan is good boy')
# # a.close()
#
# # async def Hello():
# #     await print("Saket")
# #     print("Rohan")
# #
# # a = Hello()
# # print(a)
#
# def mul(num):
#     yield (i*2 for i in range(num))
# a =mul(10000000000)
# print(a)
#
# print(next(next(a)))
# print(next(a))
# # print(next(a))
# # print(next(a))


import time

def GeneratorFunction(max_val):
    for i in range(0,max_val):
        time.sleep(1)
        yield "String %d"%i

def SmallGenerator():
    yield GeneratorFunction(3) # <-- note the use of return instead of yield

a=GeneratorFunction(3)

print(next(a))
print(next(a))
print(next(a))

# for i in GeneratorFunction(10):
#     print(i)

# for i in range(10):
#     a = SmallGenerator()
#     for i in a:
#         # print(i)
#         print("****************")
#         print(next(i))
#         print(next(i))

# for s in SmallGenerator():
#     print (next(s))
#     print(next(s))
#     print(next(s))