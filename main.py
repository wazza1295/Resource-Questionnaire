#Initilaize Values
hasID = 0
incomeLvl = 0
hasTaxes = 0


#user speaks English
def english_lang():
    print("Do you currently reside in Miami-Dade county?")
    inMiami = int(input("\n [1] Yes\n [2] No"))
    # In Miami Branch
    if inMiami == 1:
        print("do you currently have a form of Identification, such as State ID or a Driver's License?")
        global hasID
        hasID = int(input("\n [1] Yes\n [2] No"))
        if hasID == 1:
            print ("Next Question")
        else:
            hasID == 2 
    #employment Status
    print("What is your employment status?")
    global hasJob
    hasJob = int(input("\n [1] employed \n [2] unemployed "))
    #does have a job
    if hasJob == 1:
        incomeLvl = int(input("what is your income? "))
        #insert a branch for example if have a branch for under 10,000
        if incomeLvl > 13590:
            print("Eligible for Premium Tax Credit\n")
    # Immigration Status        
    print("Next question\n What is your immigration Status?\n")
    isCitizen = int(input("[1] I am a US citizen [2] I am a Resident card holder or other\n "))
    if isCitizen == 1:
        print("Do you need help paying taxes?\n ")
    hasTaxes = int(input("[1] Yes [2] No"))
    if hasTaxes == 1:
        print("")


    #not in miami Branch
    if inMiami == 2:
        print("Sorry this program does not support your area, please find your local municipal building and reach out for assistance")
        return
        

#user speaks Spanish
def spanish_lang():
    print("¿Usted reside actualmente en el condado de Miami-Dade?")
    inMiami = int(input("\n [1] Si\n [2] No \n "))
    # In Miami Branch
    print("¿Usted tiene actualmente algún tipo de identificación, como un ID estatal o una licencia de conducir?")
    hasID = int(input("\n [1] Si\n [2] No \n "))
    if hasID == 1:
        print ("Usted tiene un ID \n")
    else:
        hasID == 2
        pass 
    #employment Status
    print("¿Cuál es su situación laboral?")
    global hasJob
    hasJob = int(input("\n [1] Empleado \n [2] Desempleado "))
    #does have a job
    if hasJob == 1:
        incomeLvl = int(input("¿Cuál es su ingreso? "))
        #insert a branch for example if have a branch for under 10,000
        if incomeLvl > 13590:
            print("Usted es elegible para Premium Tax Credit\n")
    # Immigration Status        
    print("Siguiente pregunta \n ¿Cuál es su estatus migratorio?\n")
    isCitizen = int(input("[1] Soy un ciudadano [2] Soy titular de una tarjeta de residencia u otro\n "))
    if isCitizen == 1:
        print("Do you need help paying taxes?\n ")
    hasTaxes = int(input("[1] Yes [2] No"))
    if hasTaxes == 1:
        print("")

#Language menu
def menu_lang():
    print("Hello, welcome to the questionaire! Please select your language.")
    print("[1] English")
    print("[2] Spanish")
    print("[0] Exit")
    
lang = int(input("\nWhat language do you speak? \nEnter 1 or 2:\n [1] English\n [2] Spanish\n\n 1"))
while lang != 0:
    if lang == 1:
        english_lang()
        break
    elif lang == 2:
        spanish_lang()
        break
    else:
        print("invalid response, please enter 1 or 2")

#Result
if hasID == 2:
    print("\nIf you need help getting an ID, please go to this link\n https://www.flhsmv.gov/locations/miami-dade/")
if hasJob == 2:
    print ("\nIf you need help with employment, please go to this link\n https://www.miamidade.gov/global/humanresources/jobs/home.page\n")
if incomeLvl < 13590:
    print("\nYou are not eligible for premium tax credit, Please go to this link for marketplace insurance options\n https://localhelp.healthcare.gov/\n")
if hasTaxes == 1:
    print("\nFor help with filing taxes, please go to this link\n https://apps.irs.gov/app/freeFile/browse-all-offers/\n")