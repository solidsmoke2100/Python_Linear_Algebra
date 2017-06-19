import math, random

class Vector(object):
  def __init__(self, *args, fill=0):
    if len(args) == 0:
      raise ValueError("Empty vectors aren't allowed")
    if len(args) == 1:                                                # If only one argument was passed in...
      if type(args[0]) == type(1):                                    #   if the argument is an integer...
        if args[0] == 0:
          raise ValueError("Empty vectors aren't allowed")
        self.__vals = [fill] * args[0]                                #     fill self.__vals with value of fill
        self.__dim = args[0]                                          #     store dimensions of vector
      elif type(args[0]) == type([]) or type(args[0]) == type(()):    #   if the argument is a list or tuple...
        self.__vals = [i for i in args[0]]                            #     populate self.__vals with provided list
        self.__dim = len(args[0])                                     #     store dimensions of vector
      elif type(args[0]) == type(self):                               #   if the argument is another vector...
        self.__vals = [i for i in args[0]]                            #     copy elements from vector into new vector
        self.__dim = len(args[0])                                     #     store dimensions of vector
      else:                                                           #   if we don't recognize the type...
        raise TypeError('Cannot construct vector from given object')  #     TODO: what type of error message would be most helpful?
    else:                                                             # If multiple arguments passed in...
      self.__vals = [i for i in args]                                 #   fill self.__vals with arguments
      self.__dim = len(args)                                          #   store dimensions of vector
  
  def __str__(self):
    result = '<'
    for i in self.__vals:
      result += i.__repr__() + ', '
    return result[:-2] + '>'

  def __repr__(self):
    return str(self)

  def __iter__(self):
    self.__idx = -1
    return self

  def __next__(self):
    if self.__idx >= (self.__dim - 1):
      raise StopIteration
    self.__idx += 1
    return self.__vals[self.__idx]

  def __getitem__(self, idx):
    return self.__vals[idx]

  def __setitem__(self, idx, val):
    self.__vals[idx] = val
  
  def __len__(self):
    return self.__dim

  def __add__(self, other):
    if type(other) != type(self):
      raise TypeError('Cannot add vector to non-vector')
    if len(self) != len(other):
      raise ValueError('Cannot add vectors with different dimension')
    return Vector( [a + b for a, b in zip(self.to_list(), other.to_list())] )

  def __sub__(self, other):
    if type(other) != type(self):
      raise TypeError('Cannot subtract non-vector from vector')
    if len(self) != len(other):
      raise ValueError('Cannot subtract vectors with different dimensions')
    return Vector( [a - b for a, b in zip(self.to_list(), other.to_list())] )

  def __mul__(self, other):
    if type(other) == type(self):
      return self.inner_prod(other)
    elif type(other) == type(1) or type(other) == type(1.0):
      return Vector( [other * i for i in self.__vals] )
    else:
      raise TypeError('Multiplication not defined between vector and non-vector')

  def __rmul__(self, other):
    if type(other) == type(self):
      return other.inner_prod(self)
    elif type(other) == type(1) or type(other) == type(1.0):
      return Vector( [other * i for i in self.__vals] )
    else:
      raise TypeError('Multiplication not defined between vector and non-vector')

  def inner_prod(self, other):
    """Function to calculate the inner (dot) product of two vectors"""
    if type(other) != type(self):
      raise TypeError('Inner product not defined between vector and non-vector')
    return sum([a*b for a,b in zip(self.to_list(), other.to_list())])

  def to_list(self):
    """Function to convert vector to python list"""
    return [i for i in self.__vals]

if __name__ == '__main__':
  u = Vector(1,2,3,4,5)
  v = Vector( [random.randint(1, 10) for i in range(5)] )

  print(u, v)
  print(u[0], v[0:-1])
  print(u + v)
  print(u - v)
  print(u * v)
  print(2 * v)
  print(v * 2)
  print(u.to_list())
  u[0] = 'hello'
  print(u)