def display_main_menu():
    print("display_main_menu")
    print ("Enter some numbers separated by commas (e.g. 5, 67, 32")

def calc_average(temp):
    print("calc_average")
    avgtemp = sum(temp )/len(temp)
    print (avgtemp)
    return avgtemp
def get_user_input():
    global temp
    print("get_user_input")
    x = input()
    list1 = x.split(",")
    temp = list(map(float, list1))
    print (temp)

    return temp
def find_min_max(temp):
    print("find_min_max")
    print("Max " + str(max(temp)))
    print("Min " + str(min(temp)))

def sort_temperature():
    print(sort_temperature)

def calc_median_temperature():
    print("calc_median_temperature")

get_user_input()
calc_average(temp)
find_min_max(temp)