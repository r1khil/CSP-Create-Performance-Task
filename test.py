playing = True

current_points= 0
current_lifes = 0


random_flag = "a"

answer = input("Answer")



def p_update(points):
  points = points + 1
  return points

def l_update(lifes):
  lifes = lifes - 1
  return lifes

def check_answer():
  if answer == random_flag:
    print("Correct!")
    print(p_update(current_points))
  else:
    print("Incorrect!")
    print(l_update(current_lifes))
    
def run():
  check_answer()
  
run()

random_flag = ("b")

answer = input("Answer")


run()