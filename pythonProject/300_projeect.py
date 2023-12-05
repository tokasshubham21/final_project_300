import mysql.connector
while True:
    a = input('enter g to login as a guest, a for admin, e for employee\n> ')
    if a in ['g','a','e']:
        break
    else:
        print('error')

if a == 'g':
    mydb = mysql.connector.connect(
        host="localhost",
        user="guest",
        password="",
        database="ARTMUSEUM"
    )
elif a == 'a':
    mydb = mysql.connector.connect(
        host="localhost",
        user="admins",
        password=input('enter the password> '),
        database="ARTMUSEUM"
    )
elif a == 'e':
    mydb = mysql.connector.connect(
        host="localhost",
        user="employee",
        password=input('enter the password> '),
        database="ARTMUSEUM"
    )

cursor = mydb.cursor()
if a == 'a':
    while True:
        print('enter your query, if want to exit enter quit')
        b = input('>')
        if b == 'quit':
            break
        else:
            try:
                cursor.execute(b)
                try:
                    for x in cursor:
                        print(x)
                except:
                    pass
            except:
                print('error! try again')

if a == 'g':
    print('\nWelcome to the Guest Interface. What would you like to do:')
    while True:
        print('1. Art Pieces')
        print('2. Artists')
        print('3. Exhibitions')
        print('4. Quit')

        guest_choice = input('Please enter your choice: ')
        while guest_choice not in ['1', '2', '3', '4']:
            guest_choice = input('\nInvalid input.\nPlease enter a valid choice: ')

        if guest_choice == '1':

            print('1. Paintings')
            print("2. Sculpture / Statues")
            print("3. Others")
            art_choice = input('Select one of the Above Types of Art:')

            if art_choice == '1':
                cursor.execute('SELECT * FROM painting')
                result = cursor.fetchall()
                if result:
                    print("Result:")
                    for row in result:
                        print(row)
                else:
                    print("Query executed successfully.")

            elif art_choice == '2':
                cursor.execute('SELECT * FROM STATUE;')
                result = cursor.fetchall()
                if result:
                    print("Result:")
                    for row in result:
                        print(row)
                else:
                    pass
                cursor.execute('SELECT * FROM SCULPTURE;')
                result = cursor.fetchall()
                if result:
                    print("Result:")
                    for row in result:
                        print(row)
                else:
                    pass
            elif art_choice == '3':
                cursor.execute('SELECT * FROM OTHER;')
                result = cursor.fetchall()
                if result:
                    print("Result:")
                    for row in result:
                        print(row)
                else:
                    print("Query executed successfully.")

            else:
                print('invalid input')
                continue

        elif guest_choice == '2':
            cursor.execute('SELECT * FROM artist')
            result = cursor.fetchall()
            if result:
                print("Result:")
                for row in result:
                    print(row)
            else:
                print("Query executed successfully.")

        elif guest_choice == '3':
            cursor.execute('SELECT * FROM exhibitions')
            result = cursor.fetchall()
            if result:
                print("Result:")
                for row in result:
                    print(row)
            else:
                print("Query executed successfully.")

        if guest_choice == '4':
            print('Thank you for using our database!')
            break

cursor.close()

if a == 'e':
    print('select your option\n1)')
