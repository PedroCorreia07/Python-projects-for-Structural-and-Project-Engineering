def calculate_number_of_beams(n_type_bays, n_bays,n_deeps):
    n_type_beams=int(input("Insert the number of beam TYPES per bay:"))
    beams_per_bay=[] #create a list to store the number of beams per bay for each type
    if n_type_beams==1:
        levels=int(input("Insert the number of levels of beams:"))
        n_beams_bay=levels*2
        beams_per_bay.append(n_beams_bay)
        total_beams=n_beams_bay*n_bays*n_deeps
        print(f"The number of beams per bay is: {sum(beams_per_bay)}")
        print(f"The total number of beams is: {total_beams}")
    else:
        for i in range(1,n_type_beams+1):
            levels_type_i=int(input(f"Insert the number of levels of type {i} beams:"))
            beams_per_bay.append(levels_type_i * 2)
            for i, beams in enumerate(beams_per_bay, start=1):
                print(f"The number of beams of type {i} per bay is: {beams}")
                total_beams=beams*n_bays*n_deeps
                print(f"The total number of beams of type {i} is: {total_beams}")


def calculate_number_of_frames_and_footplates(n_bays):
    total_frames=(n_bays+1)*n_deeps
    total_footplates=total_frames*2
    total_anch=total_footplates*2
    total_nusl=total_anch
    print(f"The total number of frames is: {total_frames}")
    print(f"The total number of footplates is: {total_footplates}")
    print(f"The total number of anchors is: {total_anch}")
    print(f"The total number of nuts (NUSL) is: {total_nusl}")

def bracing_calculation(n_bracing_towers):
    n_bracing_levels=int(input("Insert the number of bracing levels: "))
    n_single_racks=int(input("Insert the number of single racks: "))
    n_double_racks=int(input("Insert the number of double racks: "))

    def calculate_connectors_per_level(levels):
        sr_connectors = 0
        dr_connectors = 0
        for i in range(1, n_bracing_levels + 1):
            if i % 2 == True:
                sr_connectors += 1
                dr_connectors +=1
            else:
                sr_connectors += 3
                dr_connectors +=2

        return sr_connectors,dr_connectors

    total_sr_connectors, total_dr_connectors = calculate_connectors_per_level(n_bracing_levels)
    total_sr_connectors *= n_bracing_towers * n_single_racks
    total_dr_connectors *= n_bracing_towers * n_double_racks
    print(f"The total number of single rack connectors is: {total_sr_connectors}")
    print(f"The total number of double rack connectors is: {total_dr_connectors}")

    def calculate_horizontal_bracing(levels):
        n_double_deep_racks=int(input("Insert the number of double deep racks: "))
        n_single_deep_racks=int(input("Insert the number of single deep racks: "))
        n_levels_hb=int(input("Insert the number of levels for horizontal bracing: "))

        if n_double_deep_racks>0:
            total_double_deep_horizontal_bracings=n_levels_hb*n_bracing_towers*n_double_deep_racks
            total_dd_prcg_25 = 2 * total_double_deep_horizontal_bracings
            total_dd_pnhbs_70 = total_dd_prcg_25
            total_dd_pndbs_74 = total_dd_pnhbs_70
            total_dd_bru_53_type1 = total_double_deep_horizontal_bracings
            total_dd_bru_53_type2 = total_double_deep_horizontal_bracings
            total_dd_pnhbcl = total_double_deep_horizontal_bracings
            total_dd_pnhbcr = total_double_deep_horizontal_bracings
            total_dd_boft_10_25 = 4 * total_double_deep_horizontal_bracings
            total_dd_nuwl_10 = 4 * total_double_deep_horizontal_bracings
            print(f"For the double deep racks, the total number of PRCG 25 is: {total_dd_prcg_25}")
            print(f"For the double deep racks, the total number of PNHBS 70 is: {total_dd_pnhbs_70}")
            print(f"For the double deep racks, the total number of PNHBS 74 is: {total_dd_pndbs_74}")
            print(f"For the double deep racks, the total number of BRU 23 of type 1 is: {total_dd_bru_53_type1}")
            print(f"For the double deep racks, the total number of BRU 23 of type 2 is: {total_dd_bru_53_type2}")
            print(f"For the double deep racks, the total number of PNHBCL is: {total_dd_pnhbcl}")
            print(f"For the double deep racks, the total number of PNHBCR is: {total_dd_pnhbcr}")
            print(f"For the double deep racks, the total number of BOFT 10x25 is: {total_dd_boft_10_25}")
            print(f"For the double deep racks, the total number of NUWL 10 is: {total_dd_nuwl_10}")

        else:
            total_double_deep_horizontal_bracings=0
        if n_single_deep_racks>0:
            total_single_deep_horizontal_bracings=n_levels_hb*n_bracing_towers*n_single_deep_racks
            total_sd_prcg_25 = 4 * total_single_deep_horizontal_bracings
            total_sd_pnhbs_70 = 2* total_single_deep_horizontal_bracings
            print(f"For the single deep racks, the total number of PRCG 25 is: {total_sd_prcg_25}")
            print(f"For the single deep racks, the total number of PNHBS 70 is: {total_sd_pnhbs_70}")
        else:
            total_single_deep_horizontal_bracings=0

    total_horizontal_bracing =calculate_horizontal_bracing(n_bracing_towers)

n_bays=int(input("Insert the number of bays: "))
n_deeps=int(input("Insert the number of deeps: "))
n_bracing_towers=int(input("Insert the number of bracing tower: "))

calculate_number_of_beams(1, n_bays,n_deeps)
calculate_number_of_frames_and_footplates(n_bays)
bracing_calculation(n_bracing_towers)