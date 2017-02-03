import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    assert len(alist)>0,"alist is null."
    assert sum(alist)>=0,"summation of alist is under 0. "
    return alist
    
    
    """
    print a generated list
    """
    
def printIt():
    print(generate_list())
    
def main():
    printIt()
    
    

    """
    If this script file is called, it will run main() directlt
    """
    
if __name__ == '__main__':
    print("Test printIt(): ")
    main()