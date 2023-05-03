
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2")

if __name__ == "__main__":
    main()
def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print ("Weight = "+ str(weight))
    bmi = weight/(height*height)
    print (bmi)
    if bmi<18.5:
        print ("Under Weight")
    elif 18.5<=bmi<=25.0:
            print ("Normal Weight")
    elif bmi>25.0:
            print("Overweight")


calculate_bmi(weight=57,height=1.73)
