import sys
# call with this argument python3 CommandLineArgs.py ax bx cdd
args = sys.argv
textMessage = input("Imput some text: ")
for item in args:
    print(item, textMessage)
