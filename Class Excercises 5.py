#Bronya McGrory
#22/09/2014
#Both a fridge and a lift have heights, widths and depths. Work out how much space is left in the lift once the fridge


fridgeheight= int (input("fridge height"))
fridgewidth= int (input("fridge width"))
fridgedepth= int (input("fridge depth"))

volume_of_fridge_answer= fridgeheight * fridgewidth * fridgedepth

print (volume_of_fridge_answer)


liftheight= int (input("lift height"))
liftwidth= int (input("lift width"))
liftdepth= int (input("lift depth"))

volume_of_lift_answer= liftheight * liftwidth * liftdepth

print (volume_of_lift_answer)

space_left= volume_of_fridge_answer-volume_of_lift_answer

print("the amount of space left in the lift is".format(space_left))
