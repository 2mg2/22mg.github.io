s = input("enter size in S M L:\n")
p = input("extra peproni y or n:\n")
c = input("extra chesse y or n:\n")
if s == "s":
  b = 15
  if p == "y":
    b += 2
    if c == "y":
      b += 1
      print(f"bill is {b}")
    else:
      print(f"bill is {b}")
  else:
    if c == "y":
      b += 1
      print(f"bill is {b}")
    else:
      print(f"bill is {b}")
elif s == "m":
  b = 20
  if p == "y":
    b += 3
    if c == "y":
      b += 1
      print(f"bill is {b}")
    else:
      print(f"bill is {b}")
  else:
    if c == "y":
      b += 1
      print(f"bill is {b}")
    else:
      print(f"bill is {b}")
elif s == "l":
  b = 25
  if p == "y":
    b += 2
    if c == "y":
      b += 1
      print(f"bill is {b}")
    else:
      print(f"bill is {b}")
  else:
    if c == "y":
      b += 1
      print(f"bill is {b}")
    else:
      print(f"bill is {b}")
