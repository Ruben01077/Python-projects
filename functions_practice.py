def hello():
    print("Hello")


def pack(first_name, last_name, age):
    info = (first_name, last_name, age)    
    print(info)
    
pack("Ruben", "Melikyan", 25)



def eat_lunch(list):

    if len(list) == 0:
        print("My lunchbox is empty!")

    if len(list) == 1:
        print("First I eat", list[0])

    if len(list) > 1:
        print("First I eat", list[0])
        for i in list:
         print("Next I eat", i)


eat_lunch(["Apple", "Grape", "Banana"])
