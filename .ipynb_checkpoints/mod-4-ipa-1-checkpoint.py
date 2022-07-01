'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    fromFollowing = social_graph[from_member]["following"]
    toFollowing = social_graph[to_member]["following"]
    
    if from_member in toFollowing and to_member in fromFollowing:
        return "friends"
    elif from_member in toFollowing:
        return "followed by"
    elif to_member in fromFollowing:
        return "follower"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    win = "NO WINNER"
    
    #define win-checker function
    def checkMatch(line):
        setCheck = set()
        for value in line:
            setCheck.add(value)
        if len(setCheck) == 1:
            winLine = list(setCheck)
            if winLine[0] != "":
                return(str(winLine[0]))

    #check for horizontal wins
    for row in board:
        if checkMatch(row) != None:
            win = checkMatch(row)
            
    #check for vertical rows
    for column in list(zip(*board)):
        if checkMatch(column) != None:
            win = checkMatch(column)
            
    #check up-down diagonal
    upDown = list()
    for x in range(len(board)):
        upDown.append(board[x][x])
    if checkMatch(upDown) != None:
            win = checkMatch(upDown)
            
    #check down-up diagonal
    downUp = list()
    for x in range(len(board)):
        downUp.append(board[len(board)-1-x][x])
    if checkMatch(downUp) != None:
            win = checkMatch(downUp)
    
    return win

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    route = (first_stop, second_stop)
    time = 0
    
    #Deal with the obvious cases
    if route in list(route_map.keys()):
        return route_map[route]["travel_time_mins"]
    elif first_stop == second_stop:
        for stopTimes in list(route_map.values()):
            time += stopTimes["travel_time_mins"]
        return time
    
    #Else, Create a map of the routes
    routeMap = list()
    for leg in list(route_map):
        routeMap.append(leg[0])
        
    #Find stops in the list
    fromStop = routeMap.index(first_stop)
    toStop = routeMap.index(second_stop)
    
    #simulate bus ride
    currentStop = fromStop
    listOfStopIndexes = [fromStop]
    while currentStop != toStop:
        currentStop += 1
        if currentStop > len(route_map)-1:
            currentStop = 0
        listOfStopIndexes.append(currentStop)
    listOfStopIndexes.pop()
    
    #Get Stops
    stopsNeeded = list()
    stopsInAList = list(route_map)
    for stop in listOfStopIndexes:
        stopsNeeded.append(stopsInAList[stop])
    
    #Return time spent on those stops
    for stop in stopsNeeded:
        time += route_map[stop]["travel_time_mins"]
        
    return(time)