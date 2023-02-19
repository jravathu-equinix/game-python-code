members = ["a","b","c","d"]
timestamps = [11,1,1,2]

def solution(members,timestamps):

    dictionary = {}
    for i in range(len(members)):
        dictionary[i] = members[i]

    index = 0
    while(len(members) != 1):
        location = timestamps[index]%len(members)
        del members[location]
        l1 = members[0:location]
        l2 = members[location:]
        members = l2+l1
        index += 1
        if index == len(timestamps):
            index = 0

    print(members)
    
    winner = 0
    for key,val in dictionary.items():
        if val == members[0]:
            winner = key

    return winner

sol = solution(members,timestamps)
print(sol)
