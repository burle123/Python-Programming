# def pure_chai(cups):
#     return cups * 10
# total_chai = 0


# #Not recommended
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups

def pour_chai(n):
    if n == 0:
        print("All Tea is poured")
    return pour_chai(n-1)

print(pour_chai(3))