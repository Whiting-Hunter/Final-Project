import random
#Game Paramaters
#Time is in seconds
GameTime=30
num_Runs= 10000
#Player percentages(can be changed per player)
TwoPointChance=.5
ThreePointChance=.3
TwoPointSuccess=.5
ThreePointSuccess=.35
FoulChance=.1
FTSuccces=.75
#Time for events
TimePerPossesion= 24
TimePerFoul=10
TimePerFT=15

def Game_simulation():
    Time_Left=GameTime
    #Teams score
    ATeam=0
    Bteam=0
    possesion="A"
    while Time_Left>0:
        if random.random() < FoulChance:
            SuccesfulFT=sum(random.random()<FTSuccces for _ in range(2))
            if possesion=="A":
                ATeam+=2
            else:
                Bteam+=SuccesfulFT
            Time_Left=Time_Left-TimePerFoul
            Time_Left= Time_Left-TimePerFT
        else:
            if random.random() < ThreePointChance:
                if random.random()< ThreePointSuccess:
                    if possesion=="A":
                        ATeam+=3
                else:
                    Bteam+=3
            else:
                if random.random() < TwoPointSuccess:
                    if possesion=="A":
                        ATeam+=2
                    else:
                        Bteam+=2
            Time_Left = Time_Left-TimePerPossesion
        if possesion=="A":
            possesion="B"
        else:
            possesion="A"
    return ATeam,Bteam
#Simulation Tracker
ATeamWins=0
BTeamWins=0
Draws=0
Points=0
#Run simulation(s)
for _ in range(num_Runs):
    ATeam,Bteam= Game_simulation()
    if ATeam>Bteam:
        ATeamWins+=1
    elif Bteam>ATeam:
        BTeamWins+=1
    else:
        Draws+=1 
    Points+=ATeam+Bteam
    #Print Statement
print(f"After {num_Runs} simulations:")
print(f"Team A wins: {ATeamWins} ({ATeamWins / num_Runs:.2%})")
print(f"Team B wins: {BTeamWins} ({BTeamWins / num_Runs:.2%}) ")
print(f"Draws: {Draws} ({Draws / num_Runs:.2%})")
print(f"Average Score={Points/num_Runs:.2}")





