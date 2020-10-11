import random;
def Print(tictactoe):
    print(" ___________");
    for i in range(3):
        print("| "+tictactoe[i][0]+" | "+tictactoe[i][1]+" | "+tictactoe[i][2]+" |")
        print("|___|___|___|");
def ini(tictactoe):
    tictactoe=[[" "," "," "],[" "," "," "],[" "," "," "]];
def FillCompRand(tictactoe):
    count=0;
    while(True):
        x=random.randint(0,2);
        y=random.randint(0,2);
        if(tictactoe[x][y]==" "):
            tictactoe[x][y]="X";
            return;
        else:
            count=count+1;
            if(count==5):
                break;
    for i in range(3):
        for j in range(3):
            if(tictactoe==" "):
                tictactoe[i][j]="X";
                return;
def FillComp(tictactoe):
    print("Computer:");
    for i in range(3):
        for j in range(3):
            if(tictactoe[i][j]==" "):
                tictactoe[i][j]="X";
                iswin=checkWin(tictactoe);
                if(iswin=="Win"):
                    return;
                elif(iswin=="Draw"):
                    return;
                tictactoe[i][j]="O";
                iswin=checkWin(tictactoe);
                if(iswin=="Win"):
                    tictactoe[i][j]="X";
                    return;
                tictactoe=" ";
    for i in range(3):
        for j in range(3):
            if(tictactoe==" "):
                tictactoe[i][j]="X";
                return;
def FillYou(x,y,tictactoe):
    print("you:");
    tictactoe[x][y]="O";
    Print(tictactoe);
    return;
def checkWin(G):
    if(((G[0][0]=="X")and(G[0][1]=="X")and(G[0][2]=="X"))or
       ((G[1][0]=="X")and(G[1][1]=="X")and(G[1][2]=="X"))or
       ((G[2][0]=="X")and(G[2][1]=="X")and(G[2][2]=="X"))or
       ((G[0][0]=="X")and(G[1][1]=="X")and(G[2][2]=="X"))or
       ((G[2][0]=="X")and(G[1][1]=="X")and(G[0][2]=="X"))or
       ((G[0][0]=="O")and(G[0][1]=="O")and(G[0][2]=="O"))or
       ((G[1][0]=="O")and(G[1][1]=="O")and(G[1][2]=="O"))or
       ((G[2][0]=="O")and(G[2][1]=="O")and(G[2][2]=="O"))or
       ((G[0][0]=="O")and(G[1][1]=="O")and(G[2][2]=="O"))or
       ((G[2][0]=="O")and(G[1][1]=="O")and(G[0][2]=="O"))):
        return "Win";
    else:
        for i in range(3):
            for j in range(3):
                if(G[i][j]==" "):
                    return "Continue";
    return "Draw";
def Play():
    turn =True
    tictactoe=[[" "," "," "],[" "," "," "],[" "," "," "]];
    print("Game starts");
    Print(tictactoe);
    while(1):
        res=checkWin(tictactoe);
        if(res=="Win"):
            if(turn==True):
                print("I won the game!!!");
            else:
                print("You won the game!!!");
            return;
        if(res=="Draw"):
            print("Game is a Draw :( Lets try again!!!");
            return;
        if(turn==True):
            FillCompRand(tictactoe);
            turn=False;
        else:
            x=0
            y=0
            print("Do you want to quit:");
            quit=int(input());
            if(quit==1):
                return;
            while(1):
                print("chose slot: x,y");
                x=int(input());
                y=int(input());
                if((x>=0)and(x<=2)and(y<=2)and(y>=0)):
                    break;
                print("wrong input choose again!");
            FillYou(x,y,tictactoe);  
            turn=True;
Play()