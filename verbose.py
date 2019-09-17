def Login(a):
    return [a[0]+" to the fiori launch pad as "+ a[1] +" and password "+a[2],"The SAP Fiori LaunchPad Displays"]


def Enter(a):
    return [a[0] +" value " + a[2] + " in " + a[1] + " field", a[1] +" value is entered"]


def Click(a):
    return [a[0] + " on the " + a[2] +" button", a[2] +" button is clicked. Please save required values."]

def Navigate(a):
    return [a[0] + " to " + a[1], "App home screen is displayed"]
def Save(a):
    return [a[0] + " Value of " + a[1] +" for further use", "Required values are noted"]

def verbose(argument):
    if(argument is not None):
        switcher = {
            "Login": Login,
            "Enter": Enter,
            "Click": Click,
            "Navigate": Navigate,
            "Save": Save,
        }
        # Get the function from switcher dictionary
        print(argument)
        a=argument.split("  ")
        print(a)
        func = switcher.get(a[0], lambda: "Invalid month")
        # Execute the function
        b=(func(a))
        print(b)
        return b
# triplets="""Login  PROJ_MANAGE_COMM  Welcome1!
# Enter  Project ID  1234
# Enter  Project Name  TestProject
# Enter  Description  Lol
# Click  button  Save """
# #print(triplets)
# for line in triplets.split("\n"):
#     verbose(line)