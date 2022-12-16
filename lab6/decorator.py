

def decorate(funct):
    def mirror():
        print(321)
        funct()
    return mirror


@decorate
def test():
    print(123)


test()
