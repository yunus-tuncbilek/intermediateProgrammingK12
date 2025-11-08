numtrials = int(input())
cars = []
car = []
for i in range(numtrials):
    numcars = int(input())
    for i in range(numcars):
        c = int(input())
        car.append(c)
    cars.append(car)
    car = []

# numtrials = 2
# numcars = 4
# cars = [[2,3,1,4], [4,1,3,2]]
# car = []   

# trial = [2,3,1,4]
# order = trial.copy()
# order.sort()
# print(order, trial)

def recipe(trial):
    branch = []
    # order = trial.copy()
    # order.sort()
    # print(order,trial)
    for i in range(len(trial)):
        # print(i+1, trial, branch)
        if trial and (i+1) == trial[-1]:
            trial.pop()
        else:
            if not branch or (i+1) != branch[-1]:
                while trial and trial[-1] != i+1: # changed this from checking if i+1 in trial to if the last one is i+1 to fix TLE
                    branch.append(trial[-1])
                    trial.pop()
                # branch.pop()
                if trial: # end of trial must be i + 1
                    trial.pop()
                else:
                    return 'N'
            else:
                if (i+1) == branch[-1]:
                    branch.pop()
                else:
                    return 'N'
                
    return 'Y'
                


        
# print(cars)

for i in range(numtrials):
    # print(cars[i])
    print(recipe(cars[i]))  

