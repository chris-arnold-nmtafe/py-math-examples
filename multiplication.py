def addition_example():
    first_number = 5
    second_number = 5
    addition = first_number + second_number
    #We should see 10!
    print(addition)

#addition_example()

def multiplication_example():
    # we multiply numbers together
    number = 5
    add_result = number + number + number + number
    #We should see 20!
    multiply_result = number * 4
    print(add_result)
    print(multiply_result)
#multiplication_example()

def division_example():
    # we divide numbers
    
    # start with 4 * 5 = 20
    # division turns this upside-down:
    # 20 / 5 = 4; and
    # 20 / 4 = 5
    multiply_result=20
    number=5
    print(multiply_result / number)
#division_example()

def multiplication_list():
    numbers=[5,5,5,5,5,5]
    total = 0
    for num in numbers:
        total += num
    print(total)
multiplication_list()

def area_of_rectangle():
    length = 7
    height = 3
    area = length * height
    print(f"area of the rectangle is {area}")

def area_of_square():
    length = 7
    area = length * length
    print(f"area of the square is {area}")
    # 7 "to the power of" 2
    area = length ** 2
    #The answer should still be 49
    print(f"area of the square is {area}")
area_of_square()

def volume_of_cube():
    length = 7
    area = length * length * length
    print(f"volume of the cube is {area}")
    # 7 "to the power of" 3
    area = length ** 3
    print(f"volume of the cube is {area}")
volume_of_cube()