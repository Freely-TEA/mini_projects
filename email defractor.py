def email_defractor():
    email = input("Insert curent E-Mail or press enter to quit: ")
    while True:

        if not email:   # quit   
            quit()

        lenght = len(email) 
        
        # test validation to defraction
        for i in range(lenght): 

            if email[i] == "@":

                arr = email.split('@') # spliting email

                # print difractors output
                print("User name: ", arr[0]) 
                print("Domen name: ", arr[1])

                # restart email defractor
                email_defractor() 
        
        email = input("Not correct input. Please reinput email or press inter to quit: ")

email_defractor()