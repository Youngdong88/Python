def sum(a, b):
     return a + b

def safe_sum(a, b):
     if type(a) != type(b):
          print("더할 수 없습니다.")
          return
     else:
          result = sum(a, b)
     return result

########################################

def sum(a, b):
     return a + b

def safe_sum(a, b):
     if type(a) != type(b):
          print("더할 수 없습니다.")
          return
     else:
          result = sum(a, b)
     return result

print(safe_sum('a', 1))
print(safe_sum(1, 4))
print(sum(10, 10.4))

### if __name__ == "__main__":

def sum(a, b):
     return a + b

def safe_sum(a, b):
     if type(a) != type(b):
          print("더할 수 없습니다.")
          return
     else:
          result = sum(a, b)
     return result

if __name__ == "__main__":
     print(safe_sum('a', 1))
     print(safe_sum(1, 4))
     print(sum(10, 10.4))

########################################

PI = 3.141592

class Math:
     def solv(self, r):
          return PI * (r ** 2)

def sum(a, b):
     return a + b

if __name__ == "__main__":
     print(PI)
     a = Math()
     print(a.solv(2))
     print(sum(PI, 4.4))

