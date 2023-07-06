def calculate_ipe_hea_heb_profile_properties(h, b, w_t,f_t):
  
    Iy = (b*h**3-(b-w_t)*(h-2*f_t)**3)/12
    W = Iy / (h / 2)
    print(f"The value of Iy is {Iy} mm4")
    print(f"The value of W is {W} mm3")
    return Iy, W

def analyze_ipe_hea_heb_profile_beam(max_moment):
 
    h = profile_height
    b = profile_width 
    w_t = profile_w_t 
    f_t = profile_f_t 
 
    Iy, W = calculate_ipe_hea_heb_profile_properties(h, b, w_t, f_t)
  
    M_Rd = (W * f_y) / 1.1 

    if max_moment <= M_Rd:
        print("The IPE beam can withstand the maximum bending moment.")
    else:
        print("The IPE beam cannot withstand the maximum bending moment.")


profile_height=float(input("Insert profile height (mm):"))
profile_width=float(input("Insert profile width (mm):"))
profile_w_t=float(input("Insert profile web thickness (mm):"))
profile_f_t=float(input("Insert profile flange thickness (mm):"))
M_Ed=float(input("Insert the Maximum applied moment in kNm: "))
f_y=float(input("Insert the yield strength of the profile in MPa:"))

analyze_ipe_hea_heb_profile_beam(M_Ed)

