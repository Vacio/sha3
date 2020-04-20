# constants
num_rounds = 24
rate = 1088
capacity = 512
block_size = rate + capacity # bits


def sha3(plaintext):
  num_block_iterations = get_block_iterations(plaintext)
  for iteration in range(num_block_iterations):
    x = preprocessing(plaintext, iteration)
    y = inner_keccak(x)
  print(y)

def get_block_iterations(plaintext):
  pass

def preprocessing(plaintext, iteration):
  pass

def inner_keccak(x):
  return squeezing(absorbing(x))

def absorbing(b):
  pass

def squeezing():
  pass

def f_function(b):
  for round in range(num_rounds):
    theta(rho(pi(chi(iota(b)))))

def theta(b):
  pass 

def rho(b):
  pass

def pi(b):
  pass

def chi(b):
  pass 

def iota(b):
  pass


if __name__ == "__main__":
  # sha3("tacos") # not ready yet!

  # test against this:
  import hashlib
  plaintext = input("Enter plaintext: ")
  s = hashlib.sha3_256(plaintext.encode())
  print(s.hexdigest())
