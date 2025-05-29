weather = input("How's the weather today? sunny/rainy/cold ")

if weather == "sunny":
    print("Wear a tshirt and some sunglasses")
elif weather == "rainy":
    print("Dont forget your umbrella and raincoat")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print(f"Sorry i dont have recommendations to this weather {weather}")
    