# [2015-11-23] Challenge # 242 [easy] Funny plant
# @ author Brian McEntee

challenge_inputs = []
input_line = raw_input()

while input_line :
    challenge_inputs.append([int(s) for s in input_line.split()])
    input_line = raw_input()

print challenge_inputs

NUM_PEOPLE = 0
NUM_START = 1
for challenge in challenge_inputs :
    people_to_feed = challenge[NUM_PEOPLE]
    starting_plants = challenge[NUM_START]

    harvest = [0 for i in range(starting_plants)]
    num_weeks = 1
    while total_fruit < people_to_feed :
        total_fruit = 0
        # increment num fruit on ea. plant
        harvest = [ i+1 for i in harvest]
        # count num fruit we currently have
        for i in harvest :
            total_fruit += i
        # plant new plants  
        for i in range(total_fruit) :
            harvest.append(0)
        num_weeks += 1

    print num_weeks 