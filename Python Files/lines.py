lines = int(input())
oke = 1
if lines > 5000:
    print("no.")
    import time
    time.sleep(2)
    exit;
else:
    
    while oke <= lines:
        print("|")
        oke = oke + 1
    print("there ya go... that's", lines, "lines")
    import time
    time.sleep(4)
