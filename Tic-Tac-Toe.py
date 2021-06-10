l = [[" "," "," "],[" "," "," "],[" "," "," "]]


f = [1,2,3,4,5,6,7,8,9]


def selectPlayer(p1,p2):
    
    ch = ""
    
    while ch not in ["X","O"]:
        ch = input("Player 1 : Do you need X or O? ")
        
        if ch == "X":
            p1= "X"
            p2= "O"
            
        else:
            p1 = "O"
            p2 = "X"
    
    return [p1,p2]



def validate(ch):
    
    if ch in f:
        f.remove(ch)
        return True
    else:
        return False
    
    

def insert(p,ch):
    
    if ch == 1:
        l[0][0] = p
    elif ch == 2:
        l[0][1] = p
    elif ch == 3:
        l[0][2] = p 
    elif ch == 4:
        l[1][0] = p 
    elif ch == 5:
        l[1][1] = p 
    elif ch == 6:
        l[1][2] = p 
    elif ch == 7:
        l[2][0] = p 
    elif ch == 8:
        l[2][1] = p 
    else:
        l[2][2] = p
        



def f_validate():
    
    flag = 0
    
    if l[0][0]==l[0][1]==l[0][2]=="X":
        print("Player X won the game")
        flag=1
    elif l[1][0]==l[1][1]==l[1][2]=="X":
        print("Player X won the game")
        flag=1
    elif l[2][0]==l[2][1]==l[2][2]=="X":
        print("Player X won the game")
        flag=1
    elif l[0][0]==l[1][0]==l[2][0]=="X":
        print("Player X won the game")
        flag=1
    elif l[0][1]==l[1][1]==l[2][1]=="X":
        print("Player X won the game")
        flag=1
    elif l[0][2]==l[1][2]==l[2][2]=="X":
        print("Player X won the game")
        flag=1
    elif l[0][0]==l[1][1]==l[2][2]=="X":
        print("Player X won the game")
        flag=1 
    elif l[0][2]==l[1][1]==l[2][0]=="X":
        print("Player X won the game")
        flag=1
        
        
        
        
    elif l[0][0]==l[0][1]==l[0][2]=="O":
        print("Player O won the game")
        flag=1
    elif l[1][0]==l[1][1]==l[1][2]=="O":
        print("Player O won the game")
        flag=1
    elif l[2][0]==l[2][1]==l[2][2]=="O":
        print("Player O won the game")
        flag=1
    elif l[0][0]==l[1][0]==l[2][0]=="O":
        print("Player O won the game")
        flag=1
    elif l[0][1]==l[1][1]==l[2][1]=="O":
        print("Player O won the game")
        flag=1
    elif l[0][2]==l[1][2]==l[2][2]=="O":
        print("Player O won the game")
        flag=1
    elif l[0][0]==l[1][1]==l[2][2]=="O":
        print("Player O won the game")
        flag=1 
    elif l[0][2]==l[1][1]==l[2][0]=="O":
        print("Player O won the game")
        flag=1
    
    
    if flag == 1:
        return True
    
    else:
        return False
    
    
    

def selectPos(p):
    
    
    
    ch = ""
    
    
   
    
    
    while ch not in range(1,10):
        print("Enter the choice between 1 to 9")
        ch = int(input())
        
        while validate(ch)!= True:
            ch = int(input("The position is cooupied:Kindly select other"))
        
        insert(p,ch)
      
        """
        ans = f_validate()
        if f_validate == "True":
            break
        else:
            pass
        """
    print(l[0])
    print(l[1])
    print(l[2])
    
        
    


def main():
    
    
    print("Welcome to Game")
    
    
    p1 = ""
    p2 = ""
    
    x = selectPlayer(p1,p2)
    
    
    
    p1 = x[0]
    p2 = x[1]
    
    
    print(l[0])
    print(l[1])
    print(l[2])
    
    
    
    while f_validate()!=True:
        if f_validate()== True:
            break
        else:
            selectPos(p1)
            if f_validate()==True:
                break
            else:
                selectPos(p2)
    
    
   
    for i in range(0,3):
        for j in range(0,3):
            l[i][j] = " "
           
    for i in range(1,10):
        f.append(i)
    
    p = input("Do you want to continue(Yes,No)?")
    
    if p == "Yes":
        
        main()
    else:
        pass
    
    

main()




