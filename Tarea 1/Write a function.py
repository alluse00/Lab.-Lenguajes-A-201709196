def is_leap(n):
    leap = False
    
    # Write your logic here
    if  n % 400==0:
        return True
    if n % 100==0:
        return False
    if n % 4==0:
        return True
    return False

year = int(raw_input())