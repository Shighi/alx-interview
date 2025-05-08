#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""
import sys
import re


def print_stats(total_size, status_codes):
    """
    Print statistics:
    - Total file size
    - Number of lines by status code in ascending order
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """
    Main function to read stdin line by line and compute metrics.
    """
    # Initialize variables
    total_size = 0
    line_count = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    # Pattern to match the expected line format
    pattern = r'^\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    regex = re.compile(pattern)
    
    try:
        for line in sys.stdin:
            line = line.strip()
            
            # Attempt to match the line with the expected format
            match = regex.match(line)
            
            # If the format is valid, update metrics
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))
                
                # Update total file size
                total_size += file_size
                
                # Update status code count if it's one we're tracking
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                # Increment line count
                line_count += 1
                
                # Print statistics after every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
            
    except KeyboardInterrupt:
        # Handle CTRL+C interruption
        pass
    finally:
        # Print final statistics
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
