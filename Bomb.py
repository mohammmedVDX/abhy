import subprocess
import os

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
        current_directory = os.path.dirname(os.path.realpath(__file__))
        try:
            subprocess.call(['start', os.path.join(current_directory, 'Bompe.py')], shell=True)
        except FileNotFoundError:
            print("Error: File not found.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()