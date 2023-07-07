#The following Python script is designed to verify if the backstops of a rack structure can withstand the weight of a pallet.
#This script utilizes a simplified calculation method based on the Finite Element Method (FEM) 9.842.

def calculate_hollow_section_moment_of_inertia(b_outer, h_outer, t):
  #t=thickness
    b_inner = b_outer - 2 * t
    h_inner = h_outer - 2 * t

    Ix_outer = (b_outer * h_outer**3) / 12
    Ix_inner = b_inner * h_inner**3 / 12
    Ix = Ix_outer - Ix_inner

    Iy_outer = (h_outer * b_outer**3) / 12
    Iy_inner = h_inner * b_inner**3 / 12
    Iy = Iy_outer - Iy_inner

    print(f"The Ix is: {Ix} mm4")
    print(f"The Iy is: {Iy} mm4")

    return Ix, Iy

def calculate_hollow_section_plastic_modulus(b_outer, h_outer, t):

    b_inner = b_outer - 2 * t
    h_inner = h_outer - 2 * t 

    W_pl_x_outer = (b_outer * h_outer**2) / 4
    W_pl_x_inner = b_inner * h_inner**2 / 4
    W_pl_x = W_pl_x_outer - W_pl_x_inner

    W_pl_y_outer = (h_outer * b_outer**2) / 4
    W_pl_y_inner = h_inner * b_inner**2 / 4
    W_pl_y = W_pl_y_outer - W_pl_y_inner

    print(f"The Wx is: {W_pl_x} mm3")
    print(f"The Wy is: {W_pl_y} mm3")

    return W_pl_x, W_pl_y

def calculate_max_applied_moment(l_backstop,Q_pallet):
    #Consider a simple supported beam with a point load at the middle
    #l_beam in mm
    #Qd=point_load/4 in kN

    Load_acidental_factor=1
    Qd=Q_pallet*0.0098*Load_acidental_factor/4
    M_Ed_max=(Qd*l_backstop*10**-3)/4

    print(f"The maximum applied moment is: {M_Ed_max} kNm")
    
    return M_Ed_max,Qd

def calculate_max_resist_moment(W_pl_x,fy):

    M_pl_Rd=(W_pl_x*fy*1.1)*10**-6

    print(f"The maximum resisting moment is: {M_pl_Rd} kNm")

    return M_pl_Rd

def calculate_max_deflection(Ix,Qd,l_backstop):
    #E of steel is normally considered 200 GPa

    E=200

    fmax=((Qd*(l_backstop*10**-3)**3)/(48*E*10**6*Ix*10**-12))*10**3

    print(f"The maximum deflection on the backstop is {fmax} mm")

    return fmax

b_outer=int(input("Insert b_outer (mm):"))
h_outer=int(input("Insert h_outer (mm):"))
t=float(input("Insert thickness (mm):"))
fy=int(input("Insert the steel yeld stress (MPa):"))
l_backstop=int(input("Insert the length of the backstop (mm):"))
Q_pallet=int(input("Insert the weight of the pallet (kg):"))

moment_of_inertia = calculate_hollow_section_moment_of_inertia(b_outer, h_outer, t)
section_modulus = calculate_hollow_section_plastic_modulus(b_outer, h_outer, t)
maximum_applied_moment=calculate_max_applied_moment(l_backstop,Q_pallet)
maximum_resisting_moment=calculate_max_resist_moment(section_modulus[0],fy)
maximum_deflection=calculate_max_deflection(moment_of_inertia[0],maximum_applied_moment[1],l_backstop)

if maximum_applied_moment[0]<=maximum_resisting_moment:
    print(f"{maximum_applied_moment[0]}<={maximum_resisting_moment} so, MEd<=MRd:: OK!")
else:
    print(f"{maximum_applied_moment[0]}>{maximum_resisting_moment} so, MEd>MRd:: KO!")

if maximum_deflection<=50:
    print(f"{maximum_deflection}<=50mm so, fmax<=50mm:: OK!")
else:
    print(f"{maximum_deflection}>50mm so, fmax>50mm:: KO!")