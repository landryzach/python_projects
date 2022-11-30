print("Hello from inside a file!")

def hello():
    print("Welcome to my function!")

hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]

print(pack("clothes", "food", "equipment"))


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

eat_lunch([])
eat_lunch(["ice cream"])
eat_lunch(["chicken","pasta","bread","veggies"])