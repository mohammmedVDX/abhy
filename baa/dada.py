import subprocess

def print_bomb():
    print("     ___________")
    print("    '._==_==_=_. '")
    print("    .-\\:      /-. ")
    print("   | (|:.     |) |")
    print("    '-|:.     |-'")
    print("      \\::.    /")
    print("       '::. .'")
    print("         ) (")
    print("       _.' '._")
    print("      `\"\"\"\"\"\"`")

def main():
    print_bomb()
    choice = input("Do you want to open the Bomb (y/n): ")
    if choice.lower() == 'n':
        print("Please delete it or don't say that again.")
    elif choice.lower() == 'y':
        try:
            subprocess.call(['start', 'C:\\Users\\m8398\\Desktop\\baa\\baba.bat'], shell=True)
        except FileNotFoundError:
            print("Error: File not found.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
