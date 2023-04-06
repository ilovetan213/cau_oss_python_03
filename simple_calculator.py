def arithmetic_ops(op):
    a,b = map(int,input('숫자 두개를 입력해 주세요.').split())
    return a, b, op(a,b)

def plus():
  a,b = map(int,input('숫자 두개를 입력해 주세요.').split())
  c = a+b
  print(c)

def minus():
  a,b = map(int,input('숫자 두개를 입력해 주세요.').split())
  c = a-b
  print(c)

while True:
    op = input("input operation:")

    if op == '+':
      plus()
    elif op == '-':
      minus()
    elif op == "*":
       a, b, ret = arithmetic_ops(lambda x,y:x*y)
       print(ret)
    elif op == "/":
       a, b, ret = arithmetic_ops(lambda x,y:x/y)
       print(ret)
    elif op == "%":
       a, b, ret = arithmetic_ops(lambda x,y:x%y)     
       print(ret)
    elif op == 'end':
      break
    else:
      print("Invalid operation")
      continue
    
print("Exit program")