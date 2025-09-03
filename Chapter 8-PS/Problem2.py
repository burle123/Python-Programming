#Convert farhenite to celcius

def f_t_c(f):
    return 5*(f-32)/9


f=int(input("Enter temperature in f :"))
c=f_t_c(f)
print(f"{round(c,2)}°C")