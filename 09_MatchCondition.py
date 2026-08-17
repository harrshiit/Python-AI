color=input("enter color:").lower()  # to not make  it case sensitive

match  color:
    case "green":
       print("go")
    case "red":
       print("stop")
    case  "yellow":
       print("look")
    case _:    # for  default case
        print("wrong color")