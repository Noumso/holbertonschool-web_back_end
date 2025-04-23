#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.2) == 1.11 + 2.22 )
print(add.__annotations__)
print("add(1.11, 2.2) returns", add(1.11, 2.2))
print(add(1, 2) == 1 + 2)