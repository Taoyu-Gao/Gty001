a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
# Compare d and e
print("Change 2004-2014:", d)
print("Change 2014-2024:", e)
print(d>=e)
if d > e:
    print("d is larger than e")
    # Answer: Population growth is decelerating (slowing down)
else:
    print("e is larger than d")
    # Answer: Population growth is accelerating (speeding up)
# 4.2 Booleans
X = True
Y = False
# W represents 'X or Y'
W = X or Y
# Truth table for 'X or Y':
# When X=True, Y=True  -> W = True or True = True
# When X=True, Y=False -> W = True or False = True
# When X=False, Y=True -> W = False or True = True
# When X=False, Y=False -> W = False or False = False
# Summary: W is False only when both X and Y are False
print("\nBoolean tests:")
print("X=True, Y=False -> W =", W)
X = True
Y = True
print("X=True, Y=True -> W =", X or Y)
X = False
Y = True
print("X=False, Y=True -> W =", X or Y)
X = False
Y = False
print("X=False, Y=False -> W =", X or Y)
