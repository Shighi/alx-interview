# 0x04. UTF-8 Validation

## Overview
This project implements a solution to validate whether a given data set represents a valid UTF-8 encoding. It uses Python's bitwise operations to analyze the byte patterns according to UTF-8 encoding rules.

## Background

### UTF-8 Encoding Rules
UTF-8 is a variable-width character encoding that can represent every character in the Unicode standard. It uses between 1 and 4 bytes to encode characters, with the following patterns:

1. **1-byte character**: `0xxxxxxx` (ASCII characters use this format)
2. **2-byte character**: First byte: `110xxxxx`, Second byte: `10xxxxxx`
3. **3-byte character**: First byte: `1110xxxx`, Continuation bytes: `10xxxxxx`
4. **4-byte character**: First byte: `11110xxx`, Continuation bytes: `10xxxxxx`

For multi-byte characters, all continuation bytes must follow the pattern `10xxxxxx`.

## Requirements

### General
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Code should use the `PEP 8` style (version 1.7.x)
- All files must be executable

## Challenge Description

Write a method that determines if a given data set represents a valid UTF-8 encoding:
- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Implementation Approach

The solution follows these steps:
1. Process each byte in the data set one by one
2. Consider only the 8 least significant bits of each integer
3. For each byte, determine if it's a start of a new character or a continuation byte
4. Track how many continuation bytes to expect based on the pattern of the starting byte
5. Verify that continuation bytes follow the correct pattern (`10xxxxxx`)
6. Ensure all expected bytes are present for each character

The implementation uses bitwise operations to efficiently check byte patterns:
- Using masks and shifts to check specific bit patterns
- Bitwise AND to isolate specific bits
- Bit shifting to check multi-bit patterns

## File Descriptions

- **0-validate_utf8.py**: Contains the implementation of the `validUTF8` function

## Usage Example

```python
#!/usr/bin/python3
validUTF8 = __import__('0-validate_utf8').validUTF8

# Test cases
data = [65]  # ASCII 'A'
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]  # "Python is cool!"
print(validUTF8(data))  # True

data = [229, 65, 127, 256]  # Invalid UTF-8 sequence
print(validUTF8(data))  # False
```

## Key Concepts Used

1. **Bitwise Operations**: 
   - AND (`&`) to isolate specific bits
   - Left shift (`<<`) to create masks
   - Right shift (`>>`) to check bit patterns

2. **UTF-8 Encoding Knowledge**:
   - Understanding the specific bit patterns for 1, 2, 3, and 4-byte characters
   - Recognizing valid continuation bytes

3. **Byte-Level Data Handling**:
   - Working with the 8 least significant bits of integers
   - Tracking byte sequences across multiple integers

## Author
SHIGHI
