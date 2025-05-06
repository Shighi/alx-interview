# 0x03. Log Parsing

## Overview
This project involves creating a script to parse logs from stdin, compute metrics, and print statistics. The script reads input line by line, extracts file sizes and HTTP status codes, and displays aggregated statistics periodically or when interrupted.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable
- The length of files will be tested using wc

## Task: Log Parsing

Write a script that reads stdin line by line and computes metrics:

### Input Format
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
If the format is not as specified, the line must be skipped.

### Output Requirements
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

1. Total file size: `File size: <total size>`
   - Where `<total size>` is the sum of all previous `<file size>`

2. Number of lines by status code:
   - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
   - If a status code doesn't appear or is not an integer, don't print anything for this status code
   - Format: `<status code>: <number>`
   - Status codes should be printed in ascending order

### Example

```bash
$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

### Implementation Notes

- Use proper signal handling to catch keyboard interruptions (CTRL + C)
- Parse log lines using appropriate string manipulation or regular expressions
- Keep track of the total file size and counts of different status codes
- Output the required statistics at regular intervals and when interrupted
- Handle invalid input formats gracefully by skipping malformed lines

## Testing
A generator script (`0-generator.py`) is provided to simulate log input. Run it and pipe the output to your script:

```bash
$ ./0-generator.py | ./0-stats.py
```

## Files
- `0-stats.py`: The main script for parsing logs and computing metrics

## Author
- Shighi
