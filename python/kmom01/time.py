seconds = int(input("Enter number of seconds:"))

hours = seconds // (60*60)

seconds_left = seconds % (60*60)

print(f"{seconds} seconds is {hours} hours and {seconds_left} seconds.")