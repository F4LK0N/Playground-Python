# PYTHON

## RUN
```shell
python
clear; ./main.py
```

## COMMENTS
```python
#This is a comment

"""
This is a multiline comment.
Actually this is a literal string,
that will be ignored by the compiler.
"""
```

## VARIABLES
```python
x = 5
y = "Hello, World!"
```

### Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
Rules for Python variables:
- A variable name must start with a letter or the underscore character;
- A variable name cannot start with a number;
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ );
- Variable names are case-sensitive (age, Age and AGE are three different variables);
- A variable name cannot be any of the Python keywords.

### Python Keywords
```python
and as assert break class continue def del elif else except False finally for from global if import in is lambda None nonlocal not or pass raise return True try while with yield
```

## DATATYPES
```python
x = "Hello World"	# str
x = 20	# int
x = 20.5	# float
x = 1j	# complex
x = ["apple", "banana", "cherry"]	# list
x = ("apple", "banana", "cherry")	# tuple
x = range(6)	# range
x = {"name" : "John", "age" : 36}	# dict
x = {"apple", "banana", "cherry"}	# set
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = True	# bool
x = b"Hello"	# bytes
x = bytearray(5)	# bytearray
x = memoryview(bytes(5))	# memoryview
x = None	# NoneType
```

## CASTING
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

## STRINGS

### Escape
```python
"\'"	Single Quote
"\\"	Backslash
"\n"	New Line
"\r"	Carriage Return
"\t"	Tab
"\b"	Backspace
"\f"	Form Feed
"\ooo"	Octal value
"\xhh"	Hex value
```

## ARRAYS

### Methods
```python
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
```

## OPERATORS

### Arithmetic
```python
Operator    Name                Example
+	        Addition	        x + y
-	        Subtraction	        x - y
*	        Multiplication      x * y
/	        Division            x / y
%	        Modulus             x % y
**	        Exponentiation      x ** y
//	        Floor division      x // y
```

### Assignment
```python
Operator    Example         Same As
=	        x = 5	        x = 5
+=	        x += 3	        x = x + 3
-=	        x -= 3	        x = x - 3
*=	        x *= 3	        x = x * 3
/=	        x /= 3	        x = x / 3
%=	        x %= 3	        x = x % 3
//=	        x //= 3	        x = x // 3
**=	        x **= 3	        x = x ** 3
&=	        x &= 3	        x = x & 3
|=	        x |= 3	        x = x | 3
^=	        x ^= 3	        x = x ^ 3
>>=	        x >>= 3	        x = x >> 3
<<=	        x <<= 3	        x = x << 3
:=	        print(x := 3)	x = 3
                            print(x)
```

### Comparison
```python
Operator    Name                        Example
==	        Equal	                    x == y
!=	        Not equal	                x != y
>	        Greater than	            x > y
<	        Less than	                x < y
>=	        Greater than or equal to	x >= y
<=	        Less than or equal to	    x <= y
```

### Logical
```python
Operator    Description                                                 Example
and 	    Returns True if both statements are true	                x < 5 and  x < 10
or	        Returns True if one of the statements is true	            x < 5 or x < 4
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
```

### Identity
```python
Operator    Description                                                 Example
is 	        Returns True if both variables are the same object	        x is y
is not	    Returns True if both variables are not the same object	    x is not y
```

### Membership
```python
Operator	Description	                                                                        Example
in 	        Returns True if a sequence with the specified value is present in the object	    x in y
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

```

### Bitwise
```python
Operator	Name	                Description	                                                                                                Example
& 	        AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y
|	        OR	                    Sets each bit to 1 if one of two bits is 1	                                                                x | y
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y
~	        NOT	                    Inverts all the bits	                                                                                    ~x
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
```

### Precedence
```python
()
**
+x  -x  ~x
*  /  //  %
+  -
<<  >>
&
^
|
==  !=  >  >=  <  <=  is  is not  in  not in
not
and
or
```
