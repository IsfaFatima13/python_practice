def function():
    print("hello")
#function call
function()

def function(name,end):
    print("hello "+name + end)
    
#function call
function("isfa", " ok")

def function(name,end):
    print("hello "+name + end)
    return "done"
#function call
a=function("isfa", " ok")
print(a)