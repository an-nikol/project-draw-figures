# creating global variables that will be later defined
global FIGURE, DIRECTION, NUMBER_OF_ROWS, COLUMNS_RECT

while True:
    # display a menu to the user with options until the user decides to quit

    print()
    print('Pattern Drawing Program')
    print()
    print('Menu: ')
    print('1. Draw a Triangle')
    print('2. Draw a Rectangle')
    print('3. Draw a Pyramid')
    print('4. Quit')
    print()

    # take user input of the type of figure
    FIGURE = int(input('Enter your choice (1/2/3/4): '))

    # check the type of figure
    if 1 <= FIGURE <= 3:
        if FIGURE == 1:
            NUMBER_OF_ROWS = int(input(f'Enter the number of rows for the triangle: '))
            DIRECTION = input("Enter 'u' for upward or 'd' for downward: ")
        elif FIGURE == 2:
            NUMBER_OF_ROWS = int(input(f'Enter the number of rows for the rectangle: '))
            COLUMNS_RECT = int (input("Enter the number of columns for the rectangle: "))
        elif FIGURE == 3:
            NUMBER_OF_ROWS = int(input(f'Enter the number of rows for the pyramid: '))

    # exit the program if the user wants to quit
    elif FIGURE == 4:
        print('Goodbye!')
        break

    # generate figures

    if FIGURE == 1:
        # create figure for upward triangle
        if DIRECTION == 'u':
            for rows in range(NUMBER_OF_ROWS + 1):
                for cols in range(rows):
                    print('*', end='')
                print()
        # create figure for downward triangle
        elif DIRECTION == 'd':
            for rows in range(NUMBER_OF_ROWS + 1):
                for cols in range(NUMBER_OF_ROWS - rows):
                    print('*', end='')
                print()

    # create a rectangle
    elif FIGURE == 2:
        for rows in range(NUMBER_OF_ROWS):
            for cols in range(COLUMNS_RECT):
                print('*', end='')
            print()

    # create a pyramid
    elif FIGURE == 3:
        stars = 0
        # print the spaces
        for rows in range(1, NUMBER_OF_ROWS + 1):
            for cols in range(1, (NUMBER_OF_ROWS - rows) + 1):
                print(end=' ')
            # print the stars
            while stars != (2 * rows - 1):
                print('*', end= '')
                stars += 1

            stars = 0
            print()