from lands import LandRetangle, LandSquare, Engineer


square: LandSquare = LandSquare(4)
retangle: LandRetangle = LandRetangle(3, 5)


# print(square.get_perimeter())
# print(square.get_area())
#
# print(retangle.get_perimeter())
# print(retangle.get_area())


engineer: Engineer = Engineer('Romeo')
land_square: str = engineer.measure_perimeter(square)
print(land_square)
land_square: str = engineer.measure_area(square)
print(land_square)
print()
engineer: Engineer = Engineer('Robert')
land_retangle: str = engineer.measure_perimeter(retangle)
print(land_retangle)
land_retangle: str = engineer.measure_area(retangle)
print(land_retangle)
