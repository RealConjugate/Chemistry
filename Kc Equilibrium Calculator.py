# Kc Equilibrium Constant Calculator

def Menu():
    print("")
    print("Enter 1 to begin. Enter 2 to exit the program.")

    selection = input(">>> ")

    if selection == "1":
        UserEnter()
    elif selection == "2":
        exit
    else:
        print("Invalid input. Please try again.")
        Menu()



# User enters the compounds and coefficients

def UserEnter():
    print("")
    reactantNum =  0
    productNum = 0
    valid = False
    compoundLimit = 10 # max number of reactants OR products (not combined limit)

    # Enter number of reactants and products

    while valid == False:
        print("Enter the number of reactant compounds/elements in the equation.")
        reactantNum = input(">>> ")
        if reactantNum.isnumeric() and reactantNum[0] != "0": # if "int-able"
            if int(reactantNum) < compoundLimit:
                valid = True
                reactantNum = int(reactantNum)
            else:
                print("Too many reactants - must be at most " + str(compoundLimit) + ".")
        else:
            print("Invalid input. Please try again.")
    

    valid = False

    while valid == False:
        print("Enter the number of product compounds/elements in the equation.")
        productNum = input(">>> ")
        if productNum.isnumeric() and productNum[0] != "0":
            if int(productNum) < compoundLimit:
                valid = True
                productNum = int(productNum)
            else:
                print("Too many products - must be at most " + str(compoundLimit) + ".")
        else:
            print("Invalid input. Please try again.")


    # Enter each reactant and product

    print("")
    print("Enter the compounds/elements. Remember to include stoichiometric coefficients.")
    print("Coefficients must be integers. No spaces should be used. Example: \"2KMnO4\" or \"NH3\"")

    reactants = []
    products = []

    for i in range(1, reactantNum + 1):
        valid = False
        while valid == False:
            print("Enter reactant " + str(i) + ". Remember stoichiometry.")
            compound = input(">>> ")
            if compound != "":
                if compound.isnumeric() == False and not(" " in compound) and not("." in compound) and not(compound[0] == "0"): # validation
                    reactants.append(compound)
                    valid = True
                elif " " in compound or "." in compound:
                    print("Invalid input: cannot use spaces or decimal points.")
                elif compound.isnumeric() == True:
                    print("Invalid input: cannot be just a number.")
                elif compound[0] == "0":
                    print("Invalid input: cannot begin with 0.")
            else:
                print("Invalid input. Please try again.")

    print("")

    for i in range(1, productNum + 1):
        valid = False
        while valid == False:
            print("Enter product " + str(i) + ". Remember stoichiometry.")
            compound = input(">>> ")
            if compound != "":
                if compound.isnumeric() == False and not(" " in compound) and not("." in compound) and not(compound[0] == "0"):
                    products.append(compound)
                    valid = True
                elif " " in compound or "." in compound:
                    print("Invalid input: cannot use spaces or decimal points.")
                elif compound.isnumeric() == True:
                    print("Invalid input: cannot be just a number.")
                elif compound[0] == "0":
                    print("Invalid input: cannot begin with 0.")
            else:
                print("Invalid input. Please try again.")

    reactCoeff = SliceCoefficients(reactants)[0]
    reactForm = SliceCoefficients(reactants)[1]
    productCoeff = SliceCoefficients(products)[0]
    productForm = SliceCoefficients(products)[1]

    EnterConcentrations(reactCoeff, reactForm, productCoeff, productForm)
            


# Extracts the coefficients from user's chemical formulas

def SliceCoefficients(List):
    coefficientList = []
    formulaList = []
    
    for item in List:
        i = 0
        coefficient = "" # start as a string
        formula = "" # formula with coefficient removed

        if item[0].isnumeric() == False:
            coefficient = 1 # assume it's 1
            formula = item
        
        else:
            while item[i].isnumeric() == True:
                coefficient = coefficient + item[i]
                i = i + 1
            for j in range(i,len(item)):
                formula = formula + item[j]
        
            # UserEnter() already checked the item isn't just a number so it'll stop

        coefficientList.append(int(coefficient))
        formulaList.append(formula)
        
    return(coefficientList, formulaList)
        
    

# User enters concentrations

def EnterConcentrations(reactCoeff, reactForm, productCoeff, productForm):
    print("")
    print("You need to enter all the initial concentrations for either the reactants or products.")
    print("You also need to enter one equilibrium concentration from either reactants or products.")
    
    reactFormVar = "" # display reactants and products again
    for item in reactForm:
        reactFormVar = reactFormVar + item + " "
    print("Reactants are " + reactFormVar)
    productFormVar = ""
    for item in productForm:
        productFormVar = productFormVar + item + " "
    print("Products are " + productFormVar)

    # Select whether to enter initial conc of reactants or products

    valid = False
    while valid == False:
        print("Do you have initial concentrations of reactants or products?")
        selection = input(">>> ")
        if selection.lower() == "reactants" or selection.lower() == "reactant" or selection.lower() == "r":
            valid = True
            selection = "reactants"
        elif selection.lower() == "products" or selection.lower() == "product" or selection.lower() == "p":
            valid = True
            selection = "products"
        else:
            print("Invalid input. Please try again.")

    # Enter actual initial concentrations

    reactInitial = []
    productInitial = []

    if selection == "reactants":

        i = 1
        while i >= 1 and i <= len(productForm):
            productInitial.append(0.0) # no products initially
            i = i + 1
        
        for item in reactForm:
            valid = False
            while valid == False:
                print("Enter initial concentration of " + item + ".")
                conc = input(">>> ")
                try:
                    floatConc = (float(conc)) # convert to float
                    if floatConc <= 0:
                        print("Invalid input (negative or zero). Please try again.")
                    else:
                        valid = True
                        reactInitial.append(floatConc)
                except:
                    print("Invalid input. Please try again.")

    elif selection == "products":

        i = 1
        while i >= 1 and i <= len(reactForm):
            reactInitial.append(0.0) # no reactants initially
            i = i + 1
        
        for item in productForm:
            valid = False
            while valid == False:
                print("Enter initial concentration of " + item + ".")
                conc = input(">>> ")
                try:
                    floatConc = (float(conc)) # convert to float
                    if floatConc <= 0:
                        print("Invalid input (negative or zero). Please try again.")
                    else:
                        valid = True
                        productInitial.append(floatConc)
                except:
                    print("Invalid input. Please try again.")

    # Now user enters the single equilibrium concentration

    print("You now need to enter one equilibrium concentration.")
    valid = False
    while valid == False:
        print("Do you have the equilibrium concentration for a reactant or a product?")
        selection = input(">>> ")
        if selection.lower() == "reactants" or selection.lower() == "reactant" or selection.lower() == "r":
            selection = "reactants"
            valid = True
        elif selection.lower() == "products" or selection.lower() == "product" or selection.lower() == "p":
            selection = "products"
            valid = True
        else:
            print("Invalid input. Please try again.")
    
    valid = False

    if selection == "reactants":
        
        while valid == False: # this loop stops when the whole list is filled out correctly

            reactEq = []
            productEq = []
            i = 1
            while i >= 1 and i <= len(reactForm):
                reactEq.append("none")
                i = i + 1
            i = 1
            while i >= 1 and i <= len(productForm):
                productEq.append("none")
                i = i + 1
            
            invalidList = False

            i = 0
            foundConc = False
            eqIndex = 0
            
            while i < len(reactForm) and foundConc == False: # stop asking once they enter the first concentration
                endEntry = False
                
                while endEntry == False:
                    print("Enter the equilibrium concentration of " + reactForm[i] + " or type \"none\" if you don't have it.")
                    eqConc = input(">>> ")
                    if eqConc == "none" and i != len(reactForm)-1: # not the last
                        endEntry = True
                        reactEq[i] = eqConc # only put in the list once we've checked it's correct
                    elif eqConc == "none" and i == len(reactForm)-1: # the last
                        print("Invalid input: cannot give no concentration.")
                        invalidList = True
                        endEntry = True 
                    else:
                        try:
                            floatConc = float(eqConc)
                            if floatConc <= 0:
                                print("Invalid input (negative or zero). Please try again.")
                            else:
                                endEntry = True
                                reactEq[i] = floatConc
                                eqIndex = i # pass this index into CalculateKc
                                foundConc = True
                        except:
                            print("Invalid input. Please try again.")
                i = i + 1

            if invalidList == True:
                print("Invalid list. Please re-enter equilibrium concentration.")
            else:
                valid = True


    elif selection == "products":
        
        while valid == False:

            reactEq = []
            productEq = []
            i = 1
            while i >= 1 and i <= len(reactForm):
                reactEq.append("none")
                i = i + 1
            i = 1
            while i >= 1 and i <= len(productForm):
                productEq.append("none")
                i = i + 1
            
            invalidList = False

            i = 0
            foundConc = False
            eqIndex = 0
            
            while i < len(productForm) and foundConc == False:
                endEntry = False
                
                while endEntry == False:
                    print("Enter the equilibrium concentration of " + productForm[i] + " or type \"none\" if you don't have it.")
                    eqConc = input(">>> ")
                    if eqConc == "none" and i != len(productForm)-1: 
                        endEntry = True
                        productEq[i] = eqConc 
                    elif eqConc == "none" and i == len(productForm)-1: 
                        print("Invalid input: cannot give no concentration.")
                        print("")
                        invalidList = True
                        endEntry = True 
                    else:
                        try:
                            floatConc = float(eqConc)
                            if floatConc <= 0:
                                print("Invalid input (negative or zero). Please try again.")
                            else:
                                endEntry = True
                                productEq[i] = floatConc
                                eqIndex = i
                                foundConc = True
                        except:
                            print("Invalid input. Please try again.")
                i = i + 1

            if invalidList == True:
                print("Invalid list. Please re-enter equilibrium concentration.")
            else:
                valid = True


    CalculateKc(reactInitial, productInitial, reactEq, productEq, reactCoeff, productCoeff, eqIndex, selection)

    
# Actually calculate Kc (finally!) and units

def CalculateKc(reactInitial, productInitial, reactEq, productEq, reactCoeff, productCoeff, eqIndex, RorP):

    # RorP is the side of the equation with the known equilibrium concentration

    if RorP == "reactants":
        x = (reactEq[eqIndex] - reactInitial[eqIndex]) / reactCoeff[eqIndex] # x = the change (note sign)

        for i in range(0, len(reactEq)): # need an index for the for loop
            reactEq[i] = reactInitial[i] + (reactCoeff[i] * x) # add

        for i in range(0, len(productEq)):
            productEq[i] = productInitial[i] - (productCoeff[i] * x) # subtract
            
        
    elif RorP == "products":
        x = (productEq[eqIndex] - productInitial[eqIndex]) / productCoeff[eqIndex]

        for i in range(0, len(reactEq)):
            reactEq[i] = reactInitial[i] - (reactCoeff[i] * x)

        for i in range(0, len(productEq)):
            productEq[i] = productInitial[i] + (productCoeff[i] * x)

    reactPower = []
    productPower = []

    for i in range(0, len(reactEq)):
        reactPower.append(reactEq[i] ** (reactCoeff[i]))
    for i in range(0, len(productEq)):
        productPower.append(productEq[i] ** (productCoeff[i]))

    numerator = 1.0
    denominator = 1.0

    for item in reactPower:
        denominator = denominator * item
    for item in productPower:
        numerator = numerator * item

    Kc = str(round((numerator/denominator), 4)) # Kc calculated, rounded to 4dp

    # Calculate units

    reactSum = 0
    productSum = 0

    for item in reactCoeff:
        reactSum = reactSum + item
    for item in productCoeff:
        productSum = productSum + item

    M = productSum - reactSum

    if M == 0:
        units = "(no units)"
    elif M == 1:
        units = "mol dm^-3"
    else:
        units = "mol^" + str(M) + " dm^" + str(-3*M)

    print("Kc = " + Kc + " " + units)

    print("")
    Menu()
        


# Initialisation

print("----Kc Equilibrium Constant Calculator----")
print("")
print("This program calculates the Kc equilibrium constant for a chemical reaction.")
print("The initial concentrations of either the reactants or products are required.")
print("One equilibrium concentration of either a reactant or product is also required.")
print("This calculator does not check for stoichiometric errors.")

Menu()
