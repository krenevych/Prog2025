x = float(input("x = ? (float) "))

# if x >= 0:
#     abs_x = x
# else:
#     abs_x = -x

abs_x = x if x >= 0 else -x


print(abs_x)