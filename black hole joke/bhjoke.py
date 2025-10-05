print("⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠠⡏⠤⠀⠂⠂⣂⣵⣿⣿⣿⣿⣿⣿⣿⣶⣆⠂⠂⠈⠈⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⡿⠛⠉⠉⠉⠛⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣤⣀⡀⠀⢀")
print("⠀⠀⣀⠰⣀⢿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣰⣰⣶⣿⣿⣿⣿⣿⠿⠿⠁⠉⠁")
print("⠈⠀⠀⠀⠈⠉⠛⠛⠛⠛⣿⣿⡽⣏⠉⠉⠉⠉⠉⣽⣿⠉⠉⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣦⣄⣀⣠⣴⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

print("Are you beyond the event horizon? No worries! Use this code!")
n = input("What is your current Velocity in m/s? ")
try: 
    n = float(n)
    if n >= 299792458:
        m = input("Are you a massless object? Y/N: ")
        if m in ["Y", "y", "yes", "Yes"]:
            print("Wow? never thought a massless object such as yourself would be capable of using this code!")
        if m == "n" or "N" or "no" or "No":
            print("Stop trying to break the laws of physics!")
    if n < 299792458:
        print("I am sorry my friend. Not my fault though!")
except ValueError:
    print("Enter a valid valocity number!!!")
