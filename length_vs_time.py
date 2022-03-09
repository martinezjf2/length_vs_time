# Program to calculate Length of the wire

# Elmer Rosali Martinez

# 6/7/2021



weight = 454 * float(input("what is the weight in pounds: "))

#weight = input("what is the weight in pounds: ")

#weight_pounds = float(weight)

#weight_grams = 454*weight_pounds

density_list = ("Materials Density List ", "Aluminium: 2.74gm/cc ", "Brass8020: 8.49gm/cc", "Copper: 8.96gm/cc", "Gut: 1.27gm/cc", "KanthanID: 7.25gm/cc",

      "Monel400: 8.80gm/cc", "Nickel: 8.90", "Nylon: 1.06gm/cc", "Phosphor Bronze: 8.80", "PVDF: 1.70", "Silver: 10.50gm/cc",

      "SS430: 7.75gm/cc", "SS304: 8.03gm/cc", "Steel: 7.81gm/cc", "Titanium: 4.40gm/cc", "Tungsten: 19.20gm/cc", "Zyex: 1.30gm/cc" , "33%Al67%Cu: 6.89")

for lang in density_list:
      print(lang)
      
density = float(input("what is the density in gram/cm3: "))
wire_diameter = float(input("what is the diameter of the wire in inches: "))
RPM = float(input("what is the RPM: "))



wire_radius = (1/2) * wire_diameter

print("Radius of the wire: ", wire_radius)

wire_volume = weight/(density*2.54**3)

print("Volume of the wire: ", format(wire_volume, ".3f"), "inch3")

length = wire_volume/(3.14*wire_radius**2)

print("Wire length: ", format(length, ".3f"), "inches")



core_diameter = float(input("core diameter in inches: "))

wire_turn_length = (core_diameter+wire_diameter)*3.14

print("wire circumference: ", format(wire_turn_length, ".5f"))

total_time = (length/(RPM*wire_turn_length))/60

format_weight = format(weight/454, ".2f")

format_hours = format(total_time, ".2f")

print("Continuous Winder: ", format_weight, "pounds of", wire_diameter, "inch diameter of ", density, "density wire at", RPM,"RPM will last for",

      format_hours, "hours")



string_length = float(input("What is the wrap length of the string in inches: "))

number_of_loops = (string_length/wire_diameter)

print("Number of Loops: ", format(number_of_loops, ".2f"), "inches")

length_of_wire_per_one_string = number_of_loops * wire_turn_length

print("Length of wire per one string: ", format(length_of_wire_per_one_string, ".2f"), "inches")

number_of_string_per_spool = length/length_of_wire_per_one_string

print("Strings per Spool:", format(number_of_string_per_spool, ".1f"))



#Flat wire

wire_thickness = float(input("What is the thickness of the flat wire in inches: "))

wire_width = float(input("What is the width of the flat wire in inches: "))

flat_wire_length = weight/(wire_thickness*wire_width*density**3)

print("Length of the flat wire: ", format(flat_wire_length, ".2f"), "inches")











print(input("pause: "))

