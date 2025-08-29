functionCalls=0

def f(x):
    global functionCalls 
    functionCalls+=1
    return x -1

def g(x):
    global functionCalls 
    functionCalls+=1
    return (x+1)*2

def h(x, y):
    global functionCalls 
    functionCalls+=1
    return int(str(x)+str(y))

#result = h(f(f(f(f(f(f(g(g(5)))))))),f(g(g(5))))


result = f(g(h(g(f(5)),g(5))))


print(result)
print("Function Calls: " + str(functionCalls))


