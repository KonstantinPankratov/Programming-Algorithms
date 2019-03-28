from collections import deque

'''
Create a list of your friends and their friends
List["Name"] = [Profession, [Friend list]]
'''

friends = dict()
friends["me"]     = ["Developer", ["Alice", "Oliver", "Claire"]]
friends["Oliver"] = ["Lawyer", ["George", "Jane"]]
friends["Alice"]  = ["Florist", ["Jane"]]
friends["Claire"] = ["Scientist", ["Harry", "Jack"]]
friends["George"] = ["Police officer", []]
friends["Jane"]   = ["Engineer", []]
friends["Harry"]  = ["Manager", []]
friends["Jack"]   = ["Teacher", []]

search_queue = deque()  # Create a queue
search_queue += friends["me"][1]  # Set a starting point to the queue


def search(queue):
    searched = []  # An already handled persons to avoid reiteration
    while queue:
        person = queue.popleft()  # Get a first person from the hast table
        if person not in searched:
            if is_manager(person):
                print(person + " is a manager!")
                return True
            else:
                searched.append(person)
                queue += friends[person][1]
    print("There is no manager in your friends list or lists of your friends!")
    return False


def is_manager(person):
    if friends[person][0] == "Manager":
        return True


search(search_queue)
