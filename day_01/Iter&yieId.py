#!/usr/bin/python
if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5]
    it = iter(ls)
    print(next(it))
    print(next(it))
    for i in it:
        print(i)


    class MyNumber:
        def __iter__(self):
            self.a = 0
            return self

        def __next__(self):
            if self.a < 20:
                self.a += 1
                return self.a
            else:
                raise StopIteration


    myClass = MyNumber()
    myIter = iter(myClass)
    print(next(myIter))
    print(next(myIter))

    for x in myIter:
        print(x)
