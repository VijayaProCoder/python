def f(list):
    word=" "
    double=list
    for i in range(len(list)):
        word=list[2*i]
        double.insert(2*i+1,len(word)*"*")
    return double
f(["hi","hello"])