#Initilaize Values
hasID = 0
hasJob = 0
incomeLvl = 0
isCitizen = 0
hasTaxes = 0
tieneID = 0
tieneTrabajo = 0
nvlIngreso = 0
esCiudadano = 0
tieneImpuestos = 0
inMiami = 0
enMiami = 0


#user speaks English
def english_lang():
    print("\nDo you currently reside in Miami-Dade county?")
    global inMiami
    inMiami = int(input("[1] Yes\n[2] No \n"))
    # In Miami Branch
    if inMiami == 1:
        print("\nDo you currently have a form of Identification, such as State ID or a Driver's License?")
        global hasID
        hasID = int(input("[1] Yes\n[2] No \n"))
        #employment Status
        print("\nNext question:\nWhat is your employment status?")
        global hasJob
        hasJob = int(input("[1] Employed \n[2] Unemployed \n"))
        #does have a job
        if hasJob == 1:
            global incomeLvl
            incomeLvl = int(input("\nWhat is your income?\n"))
            #insert a branch for example if have a branch for under 10,000
            if incomeLvl > 13590:
                print("Eligible for Premium Tax Credit\n")
        # Immigration Status        
        print("\nFinal question:\nWhat is your immigration Status?")
        global isCitizen
        isCitizen = int(input("[1] I am a US citizen \n[2] I am a Resident card holder or other\n "))
        if isCitizen == 1:
            print("\nDo you need help paying taxes?")
            global hasTaxes
            hasTaxes = int(input("[1] Yes \n[2] No\n"))
            if hasTaxes == 1:
                print("")

    #not in miami Branch
    else:
        print("We are very sorry, but this program does not support your area. Please find your local municipal building and reach out for assistance")
        return
        

#user speaks Spanish
def spanish_lang():
    print("\n¿Usted reside actualmente en el condado de Miami-Dade?")
    global enMiami
    enMiami = int(input("[1] Si\n[2] No \n "))
    # In Miami Branch
    if enMiami == 1:
        print("\n¿Usted tiene actualmente algún tipo de identificación, como un ID estatal o una licencia de conducir?")
        global tieneID
        tieneID = int(input("[1] Si\n[2] No \n "))
        if tieneID == 1:
            print ("Usted tiene un ID")
        else:
            tieneID == 2
            pass 
        #employment Status
        print("\nSiguiente pregunta:\n¿Cuál es su situación laboral?")
        global tieneTrabajo
        tieneTrabajo = int(input("[1] Empleado \n[2] Desempleado \n"))
        #does have a job
        if tieneTrabajo == 1:
            global nvlIngreso
            nvlIngreso = int(input("\n¿Cuál es su ingreso? \n"))
            #insert a branch for example if have a branch for under 10,000
            if nvlIngreso > 13590:
                print("Usted es elegible para Premium Tax Credit\n")
        # Immigration Status        
        print("\nÚltima pregunta: \n¿Cuál es su estatus migratorio?")
        global esCiudadano
        esCiudadano = int(input("[1] Soy un ciudadano \n[2] Soy titular de una tarjeta de residencia u otro\n "))
        if esCiudadano == 1:
            print("\n¿Necesita ayuda para pagar impuestos? ")
            global tieneImpuestos
            tieneImpuestos = int(input("[1] Si \n[2] No\n"))
            if tieneImpuestos == 1:
                print("")

    else:
        print("Lo sentimos mucho, pero este programa no es compatible con su área. Encuentre el edificio municipal de su localidad y solicite ayuda.")
        return

#Language menu
def menu_lang():
    print("Hello, welcome to the questionaire! Please select your language.")
    print("[1] English")
    print("[2] Spanish")
    print("[0] Exit")
    
lang = int(input("\nWhat language do you speak? \nEnter 1 or 2:\n[1] English\n[2] Spanish\n"))
while lang != 0:
    if lang == 1:
        english_lang()
        break
    elif lang == 2:
        spanish_lang()
        break
    else:
        print("invalid response, please enter 1 or 2")

#Result in english
if lang == 1 and inMiami == 1:
    if (hasID == 1 and hasJob == 1 and incomeLvl > 13590 and hasTaxes == 2):
        print("Congratulations! Your current situation lacks any critical issues.")
    else:
        print("Based on your responses, here are the resources:")
        if hasID == 2:
            print("\nIf you need help getting an ID, please go to this link\nhttps://www.flhsmv.gov/locations/miami-dade/")
        if hasJob == 2:
            print ("\nIf you need help with employment, please go to this link\nhttps://www.miamidade.gov/global/humanresources/jobs/home.page\n")
        if incomeLvl < 13590 and (inMiami == 1 or enMiami == 1) and (hasJob == 1 or tieneTrabajo == 1):
            print("\nYou are not eligible for Premium Tax Credit, please go to this link for marketplace insurance options\nhttps://localhelp.healthcare.gov/\n")
        if hasTaxes == 1:
            print("\nFor help with filing taxes, please go to this link\nhttps://apps.irs.gov/app/freeFile/browse-all-offers/\n")

#results in spanish
if lang == 2 and enMiami == 1:
    if (tieneID == 1 and tieneTrabajo == 1 and nvlIngreso > 13590 and tieneImpuestos == 2):
        print("¡Felicidades! Su situación actual carece de problemas críticos.")
    else:
        print("Basado en sus respuestas, aquí están los recursos:")
        if tieneID == 2:
            print("\nSi necesita ayuda para obtener una identificación, por favor vaya a este enlace\nhttps://www.flhsmv.gov/locations/miami-dade/")
        if tieneTrabajo == 2:
            print ("\nSi necesita ayuda consiguiendo trabajo, por favor vaya a este enlace\nhttps://www.miamidade.gov/global/humanresources/jobs/home.page\n")
        if nvlIngreso < 13590 and (enMiami == 1 or inMiami == 1) and (tieneTrabajo == 1 or hasJob == 1):
            print("\nUsted no es elegible para Premium Tax Credit, por favor vata a este enlace para conocer las opciones de seguro en el mercado\nhttps://localhelp.healthcare.gov/\n")
        if tieneImpuestos == 1:
            print("\nPara obtener ayuda con la declaración de impuestos, por favor vaya a este enlace\nhttps://apps.irs.gov/app/freeFile/browse-all-offers/\n")