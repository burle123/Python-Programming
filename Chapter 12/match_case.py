def status(code):
    match code:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(status(400))
print(status(404))
print(status(418))
print(status(500))        

