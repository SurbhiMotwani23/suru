import argparse
#Addition function
def add(a,b):
    val = a+b
    return val
 
#Subtraction function
def sub(a,b):
    val = a-b
    return val
 
#Division function
def div(a,b):
    val = a/b
    return val
 
#Multiplication function
def multi(a,b):
    val = a*b
    return val
 
#Main function
def Main():
    #reate the parser
    parser = argparse.ArgumentParser()
 
    group = parser.add_mutually_exclusive_group()
    ##adding the argument
    #help menu
    group.add_argument("-fa","--fadd",help="Performs addition",action="store_true")
    group.add_argument("-fs","--fsub",help="Performs subtraction",action="store_true")
    group.add_argument("-fd","--fdiv",help="Performs division",action="store_true")
    group.add_argument("-fm","--fmulti",help="Performs multiplication",action="store_true")
 
    parser.add_argument("num1",help="Number1 to calculate",type=int)
    parser.add_argument("num2",help="Number2 to calculate",type=int)
    #parse the argument
    args = parser.parse_args()
    #Optional arguments 
    if args.fadd:
        print("The addition result of {} and {} is {}".format(args.num1,args.num2,(add(args.num1,args.num2))))
    elif args.fsub:
        print("The subtraction result of {} and {} is {}".format(args.num1,args.num2,(sub(args.num1,args.num2))))
    elif args.fdiv:
        print("The division result of {} and {} is {}".format(args.num1,args.num2,(div(args.num1,args.num2))))
    elif args.fmulti:
        print("The multiplication result of {} and {} is {}".format(args.num1,args.num2,(multi(args.num1,args.num2))))
    else:
        print("Error:Requires an argument to perform an action")
 
     
if __name__ == '__main__':
    Main()