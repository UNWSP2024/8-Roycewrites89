# Royce Daniel 3/20/2026 "The Hammer"
def main():
    result = ''

    userinput = input('Enter a string: ')

    result = result + userinput[0]

    for i in range(1, len(userinput)):
        char = userinput[i]

        if char.isupper():
            char = char.lower()
            result = result + ' '

        result = result + char

    print(result)


main()