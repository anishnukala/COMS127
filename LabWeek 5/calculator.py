import myShapes
import myPhysics
import myOhmsLaw
import myUsefulLifeCalcs

print("Choose an option:")
print("1. Calculate area of rectangle")
print("2. Calculate perimeter of rectangle")
print("3. Calculate area of circle")
print("4. Calculate circle of circumference")
print("5. Distance Speed Time")
print("6. Velocity Acceleration Time")
print("7. Calculate the Voltage")
print("8. Calculate the resistance")
print("9. Calculate the Current")
print("10. Body Mass Index")
print("11. Compound Amount")
print("12. Quit")

choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

def main():
    running = True

if choice == '1':
 base= float(input("please enter the base of Rectangle:"))
 height= float(input("please enter the height of Rectangle:"))
 area = base * height
 print(f"The area of Rectangle is {area} for base {base} and height {height}.")
 
elif choice == '2':
            side_length = float(input("Enter the side length of the cube: "))
            surface_area = myShapes.cubeSurface(side_length)
            print(f"The surface area of the cube is: {surface_area}")
elif choice == '3':
            radius = float(input("Enter the radius of the sphere: "))
            volume = myShapes.sphereVolume(radius)
            print(f"The volume of the sphere is: {volume}")
elif choice == '4':
            radius = float(input("Enter the radius of the sphere: "))
            surface_area = myShapes.sphereSurface(radius)
            print(f"The surface area of the sphere is: {surface_area}")
elif choice == '5':
            celsius = float(input("Enter the Celsius temperature: "))
            fahrenheit = myTemps.cth(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif choice == '6':
            celsius = float(input("Enter the Celsius temperature: "))
            kelvin = myTemps.ctk(celsius)
            print(f"{celsius}°C is equal to {kelvin}K.")
elif choice == '7':
            fahrenheit = float(input("Enter the Fahrenheit temperature: "))
            celsius = myTemps.ftc(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C.")
elif choice == '8':
            kelvin = float(input("Enter the Kelvin temperature: "))
            celsius = myTemps.ktc(kelvin)
            print(f"{kelvin}K is equal to {celsius}°C.")
elif choice == '9':
            kelvin = float(input("Enter the Kelvin temperature: "))
            fahrenheit = myTemps.ktf(kelvin)
            print(f"{kelvin}K is equal to {fahrenheit}°F.")
elif choice == '10':
            fahrenheit = float(input("Enter the Fahrenheit temperature: "))
            kelvin = myTemps.ftk(fahrenheit)
            print(f"{fahrenheit}°F is equal to {kelvin}K.")
            
elif choice == '11':
            fahrenheit = float(input("Enter the Fahrenheit temperature: "))
            kelvin = myTemps.ftk(fahrenheit)
            print(f"{fahrenheit}°F is equal to {kelvin}K.")
                        
elif choice == '12':
            print("Goodbye!")
            running = False  # Set running to False to exit the loop
else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7/8/9/10/11/12).")

if __name__ == "_main_":
    main()
