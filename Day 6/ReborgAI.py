# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json

def turn_right():
    turn_left()
    turn_left()
    return find_way()

def find_way():
    while front_is_clear() == True and at_goal() != True :
        move()
    if at_goal ==True:
        return
        
    elif front_is_clear() != True:
        while wall_in_front()==True:
            turn_left()
            if front_is_clear() != True:
                turn_right()
            elif front_is_clear() == True:
                return find_way()
            
           

find_way()