#CONVERTER
#_____________

import os

while True:
    input("press enter to continue")
    os.system("cls" if os.name=="nt" else "clear")
    print("enter \"m\" for mass conversion")
    print("enter \"l\" for length conversion")
    print("enter \"t\" for temperature conversion")
    print("enter \"q\" to exit")
    type=input("type of conversion: ")
    
# MASS CONVERSION   
    
    if type.lower()=="m":
        print("enter \"0\" for lbs to kg")
        print("enter \"1\" for kg to lbs")
        print("enter \"2\" for grain to mg&g")
        
        type_m=input("choose type: ")
        
        if type_m=="0":
            # 1 pound (lb) = 0.45359237 kilograms (kg)
            # international avoirdupois pound [1]
            mass_lb=float(input("enter a measurement in lbs: "))
            mass_kg=mass_lb*0.45359237
            print(f"the measurement in kg = {mass_kg}")
            
        elif type_m=="1":
            mass_kg=float(input("enter a measurement in kg: "))
            mass_lb=mass_kg/0.45359237
            print(f"the measurement in lbs = {mass_lb}")
            
        elif type_m=="2":
            # 1 grain (gr) = 64.79891
            #the international yard and pound agreement of 1959 [2]
            mass_gr=float(input("enter a measurement in grains: "))
            mass_mg=mass_gr*64.79891
            mass_g=mass_mg/1000
            print(f"the measurement in mg = {mass_mg}")
            print(f"the measurement in g = {mass_g}")
            
        else:
            print("error, please enter one of the given values")

# LENGTH CONVERSION    
            
    elif type.lower()=="l":
        print("enter \"0\" for inch to cm&mm")
        print("enter \"1\" for cm\mm to inch")
        print("enter \"2\" for mile to km")
        print("enter \"3\" for km to mile")
        print("enter \"4\" for yard to m")
        print("enter \"5\" for m to yard")
        
        type_l=input("choose type: ")

        if type_l=="0":
            # 1 inch = 25.4 mm
            # British Standards Institution defined in 1930 [3]
            # American Standards Association (now ANSI) defined in 1933 [1]
            # National Advisory Committee for Aeronautics (now NASA) defined in 1952 [1]
            len_in=float(input("enter measurement in inch: "))
            len_cm=len_in*2.54
            len_mm=len_cm*10
            print(f"the measurement in cm = {len_cm}")
            print(f"the measurement in mm = {len_mm}") 
     
        elif type_l=="1":
            type_l2=input("input in mm or cm? ")
    
            if type_l2.lower()=="mm":
                len_mm=float(input("enter a measurement in mm: "))
                len_in=len_mm/25.4
                print(f"the measurement in inch = {len_in}")
        
            elif type_l2.lower()=="cm":
                len_cm=float(input("enter a measurement in cm: "))
                len_in=len_cm/2.54
                print(f"the measurement in inch = {len_in}")
                
        elif type_l=="2":
            # 1 mile = 1.609344 km
            # the international yard and pound agreement of 1959 [4]
            len_mi=float(input("enter measurement in mile: "))
            len_km=len_mi*1.609344
            print(f"the measurement in km = {len_km}")
            
        elif type_l=="3":
            len_km=float(input("enter measurement in km: "))
            len_mi=len_km/1.609344
            print(f"the measurement in mile = {len_mi}")
          
        elif type_l=="4":
            # 1 yard = 0.9144 m
            # the international yard and pound agreement of 1959 [3]
            len_yd=float(input("enter measurement in yard: "))
            len_m=len_yd*0.9144
            print(f"the measurement in m = {len_m}")
            
        elif type_l=="5":
            len_m=float(input("enter a measurement in m: "))
            len_yd=len_m/0.9144
            print(f"the measurement in yards = {len_yd}")
            
        else:
            print("error, please enter one of the given values")
            
# TEMPERATURE CONVERSION

    elif type.lower()=="t":
        print("enter \"0\" for °f to °c")
        print("enter \"1\" for °c to °f")
        
        type_t=input("choose type: ")
        
        if type_t=="0":
            temp_f=float(input("enter a measurement in °f: "))
            temp_c=((temp_f-32)*(5/9))
            print(f"the measurement in °c = {temp_c}")
            
        elif type_t=="1":
            temp_c=float(input("enter a measurement in °c: "))
            temp_f=((temp_c*(9/5))+32)
            print(f"the measurement in °f = {temp_f}")
                    
    elif type.lower()=="q":
        break
            
    else:
        print("error, please enter one of the given values")
        
        
# SOURCES

# [1]: Refinement of Values for the Yard and the Pound – US Metric Association https://share.google/BBNaJDIeV7pacZcSg

# [2]: https://en.wikipedia.org/wiki/Grain_%28unit%29#%3A%7E%3Atext%3DA_grain_is_a_unit%2Cto_have_been_ritualistic_formulas.?wprov=sfla1

# [3]: https://en.wikipedia.org/wiki/International_yard_and_pound?wprov=sfla1

# [4]: https://en.wikipedia.org/wiki/Mile#%3A%7E%3Atext%3DThe_statute_mile_was_standardised_as_a%2Cthe_mile_exactly_1609.344_metres_%281.609344_kilometres%29.?wprov=sfla1