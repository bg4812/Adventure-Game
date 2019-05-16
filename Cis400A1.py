def askStats(fighter):    # asks user if they want to see there fighter's stats
       ans=input('Would you like to see the stats of '+str(fighter.name)+'?(y or n)')
       if ans == 'y' or ans=='Y':
           fighter.showStats()
       elif ans== 'N' or ans =='n':
           ans2=input('Are you sure you do not want to see your Fighters stats? ')
           if ans2 == 'y' or ans2 == 'Y':
               print()
           elif ans == 'N' or ans == 'n':
               askStats(fighter)
       else:
           print("invaild input ")
           askStats(fighter)
def battle(yourfighter,opponent):  #loop as long as your health and opponent health not 0
    print('A battle has started between '+ yourfighter.name+'and '+opponent.name)
    battleCounter=0
    while(yourfighter.currHealth>0 and opponent.currHealth>0):
        battleCounter= battleCounter+1
        print(str(yourfighter.name) + ' health : '+ str(yourfighter.currHealth))
        print(str(opponent.name) +' health : '+str(opponent.currHealth))
        yourfighter.showAttackList()
        
        ans=input('Pick an attack' )
        if ans == 'n'or ans == 'N':
            yourfighter.attack(opponent)
            
        elif ans == 'm' or ans == 'M':
            yourfighter.Magicattack(opponent)
            
        elif ans == 's' or ans == 'S':
            yourfighter.SignatureAttack(opponent)
            
        else:
            break
        if opponent.currHealth>0:
            
            if battleCounter%2 == 0:
                opponent.SignatureAttack(yourfighter)
                                         
            elif opponent.magicalPower< opponent.physicalPower:
                opponent.attack(yourfighter)
        
            elif opponent.magicalPower>opponent.physicalPower:
                opponent.Magicattack(yourfighter)
            
            else:
                opponent.attack(yourfighter)
            
            
                  
        if yourfighter.currHealth<=0:
            print(str(yourfighter.name) +' has lost')
            yourfighter.battleLog(opponent,"LOSS")
        
        if opponent.currHealth<=0:
            print(str(yourfighter.name) +' has won')
            yourfighter.battleLog(opponent,"WIN")
            
        
''' store the Winner and loser of the battle in a dictionary and return them'''


def askBattle(fighter,opponent): #asks if you would like to fight
    ans=input('Would you like to battle the fighter named '+opponent.name+'?(y or n)')
    if ans == 'y' or ans=='Y':
            battle(fighter,opponent)
    elif ans== 'N' or ans =='n':
           ans2=input('Are you sure you do not want to battle'+ opponent.name+'?')
           if ans2 == 'y' or ans2 == 'Y':
               print('')
           elif ans == 'N' or ans == 'n':
               askBattle(fighter,opponent)
    else:
        print("invaild input ")
        askBattle(fighter,opponent)
        
def askLog(fighter): # ask to see all the opponents you have faught
    ans=input('Would you like to see your BattleLog ?')
    if ans == 'y' or ans=='Y':
            print(fighter.Log)
    elif ans== 'N' or ans =='n':
           ans2=input('Are you sure you do not want to see your BattleLog?')
           if ans2 == 'y' or ans2 == 'Y':
               print('')
           elif ans == 'N' or ans == 'n':
               askLog(fighter)
    else:
        print("invaild input ")
        askLog(fighter)
    
        
    
class Fighter:
    #fighter stats
    physicalPower=0   
    magicalPower=0 
    physicalDefense=0
    magicalDefense=0
    currHealth=1
    TotalHealth=1
    attackList=["normal attack","Magical attack","Signature attack","Withdraw"]  #a list that names your attacks that you can use
    fightersFaught=[]
    Log={}          # a log of all of your fights and the results
    powerLevel=0  #total power


    def __init__(self,name):  # creates a standard fighter 
        self.name=name
        self.physicalPower = 500
        self.magicalPower = 500
        self.physicalDefense=500
        self.magicalDefense=500
        self.currHealth=500
        self.TotalHealth=500
        self.powerLevel= self.physicalPower+self.magicalPower
        print(self.name+' was created')

    def showStats(self): #shows the stats for your fighter
        print(self.name+" Stats: ")
        print('Health ='+ str(self.currHealth)+'/'+str(self.TotalHealth))
        print('Magical power = '+ str(self.magicalPower))
        print('Physical power = ' + str(self.physicalPower))
        print("Power level = " + str(self.powerLevel))

    def attack(self,opponent): #attacks using physcial power
        try:
            attackPower=self.physicalPower-(opponent.physicalDefense)*.75 # create algorithim for how much attacks will take
        except ArithmeticError:
            print('ERROR: attackpower calculation')
        if attackPower<0:
            attackPower=0
        opponent.currHealth=opponent.currHealth-attackPower
        print(self.name +' has attacked '+ opponent.name+' with a normal attack dealing '+str(attackPower)+' damage')
    
    def Magicattack(self,opponent): #attacks using magical power
        try:
            attackPower=self.magicalPower-(opponent.magicalDefense)*.75 # create algorithim for how much attacks will take
        except ArithmeticError:
            print('ERROR: attackpower calculation')
        if attackPower<0:
            attackPower=0
        opponent.currHealth=opponent.currHealth-attackPower
        print(self.name +' has attacked '+ opponent.name+' with a magical attack dealing '+str(attackPower)+' damage')
        
    def SignatureAttack(self,opponent): #signiture attack varies on race
        try:
            attackPower=self.magicalPower+self.physicalPower-(opponent.physicalDefense*.75)-(opponent.magicalDefense*.75)
        except ArithmeticError:
            print('ERROR: attackpower calculation')
        if attackPower<0:
            attackPower=0
        opponent.currHealth=opponent.currHealth-attackPower
        print(self.name +' has attacked '+ opponent.name+' with their signatur move dealing '+str(attackPower)+' damage')
        
    def battleLog(self,fighter,result):  #logs all the opponents that your fighter has faced and whether they won or not
        #put the fighter in a dictionary 
        #the dictionary index should have the opponent : WIN/LOSE
        #fightersFaught.append(fighter.name)
        self.Log[fighter.name]=result
    def showAttackList(self):  #shows all available attacks
        print(self.name+" attacks:")
        for item in self.attackList:
            print(item+"     ",end="")
        
    def seeWins(self): # returns a list of only the oppponets your fighter has won
        winnersList=[item for item in self.Log if self.Log[item]=='WIN']
        winnersDict={k: v for k, v in self.Log.items() if v =='WIN'}
    
        return winnersList,winnersDict
    def boost(self,mA,fA,mD,fD,HP): #increases a fighters stats
        self.magicalPower=mA
        self.physicalPower=fA
        self.magicalDefense=mD
        self.physicalDefense=fD
        self.TotalHealth=HP
        self.powerLevel=mA+fA
    
        
    
        #the list will be turn in to a dictionary using dictionary comprehension

"""class Mage(Fighter):

    def __init__(self,name):
        Fighter.__init__(self,name)
        self.name=name
        super().magicalPower=10000

    def signature_move(self):   #
        print(self.name+"used signature move")"""
class Demon(Fighter):  # strong physical and magical 
    
    def SignatureAttack(self,opponent): #signiture attack varies on race
        try:
            attackPower=(self.magicalPower*2)+(self.physicalPower*2)-(opponent.physicalDefense*.75)-(opponent.magicalDefense*.75)
        except ArithmeticError:
            print('ERROR: attackpower calculation')
        opponent.currHealth=opponent.currHealth-attackPower
        print(self.name +' has attacked '+ opponent.name+' with their signature move dealing '+str(attackPower)+' damage')

class Giant(Fighter):    #strong physical weak magical
    
    def __init__(self,name,level):
        self.name=name
        self.physicalPower = 1000*level
        self.magicalPower = 250 *level
        self.physicalDefense=1000*level
        self.magicalDefense=250*level
        self.currHealth=1000*level
        self.TotalHealth=1000*level
        self.powerLevel= self.physicalPower+self.magicalPower
        print(self.name+' has appeared')
    
    def SignatureAttack(self,opponent): #signature attack varies on race
        try:
            attackPower=(self.physicalPower*2.25)-(opponent.physicalDefense*.75)
        except ArithmeticError:
            print('ERROR: attackpower calculation')
        opponent.currHealth=opponent.currHealth-attackPower
        print(self.name +' has attacked '+ opponent.name+' with their signature move dealing '+str(attackPower)+' damage')

class Fairy(Fighter):       #weak phyical high magical
    
    def __init__(self,name,level):
        self.name=name
        self.physicalPower = 250*level
        self.magicalPower = 1000 *level
        self.physicalDefense=250*level
        self.magicalDefense=1000*level
        self.currHealth=500*level
        self.TotalHealth=500*level
        self.powerLevel= self.physicalPower+self.magicalPower
        print(self.name+' has appeared')
        
    def SignatureAttack(self,opponent): #signiture attack varies on race
        try:
            attackPower=(self.magicalPower*2.25)-(opponent.magicalDefense*.75)
        except ArithmeticError:
            print('ERROR: attackpower calculation')
        opponent.currHealth=opponent.currHealth-attackPower
        print(self.name +' has attacked '+ opponent.name+' with their signature move dealing '+str(attackPower)+' damage')


if __name__=="__main__":
    print('When faced with a decision enter the first letter of whatever you decide')
    name1=input('Name your fighter ')
    F1 = Fighter(name1)
    askStats(F1)
    CPU= Fighter("goblin")
    print('A goblin has appeared')
    askStats(CPU)
    print('The goblin has attacked')
    battle(F1,CPU)
    askLog(F1)
    List,Dict=(F1.seeWins())
    print('bg currently has '+str(F1.currHealth)+' health remaining')
    print('There is a sign?!!')
    print('It reads: Go left to the Giants nation or right for the fairy kingdom')
    ans=input('Would you like to go left or right?')
    if ans =="R" or ans=='r':
        fairy1= Fairy("fairy kid",1)
        print(fairy1.name+': Who are you?')
        print(fairy1.name+': You are here for the sacred tree arent you?!')
        askStats(fairy1)
        battle(F1,fairy1)
        askLog(F1)
        print(fairy1.name+': HAHA!!')
        print(fairy1.name+': You could even survive on attack and you think you can achieve imortality ')
        print(fairy1.name+': The scared tree is heavily guarded!! Your too weak to ever make it there')
        F1.currHealth=1
        print('bg currently has '+str(F1.currHealth)+' health remaining')
        print('bg: I guess I should have turned left after all')
        print(F1.name+': I hope the giants are nicer than the fairies')
    else:
        print(F1.name+': ON TO GIANTS NATION!!')
    G = Giant('Giant Solider',2)
    askStats(G)
    print(F1.name+": This guy is Strong!?")
    ans2=input(G.name+': You look hurt do you need help?')
    print('Let me take you back to our village')
    print('...................................')
    print(F1.name+': Where am I?')
    print('You are in our hospital')
    F1.boost(1000,1000,1000,1000,1000)
    F1.currHealth=F1.TotalHealth
    print(F1.name+': I feel stronger')
    askStats(F1)
    print('We did some procedures and have you better than ever') 
    print('Would you like to test your new strength?')
    askBattle(F1,G)
    print('The fairies did this to you?')
    print('They are always on guard for visitors because they are protecting a tree that grants imortality')
    
        
