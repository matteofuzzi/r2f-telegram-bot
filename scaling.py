# scaling.py
def get_scaling_for_movement(query):
    query = query.lower().strip()
    scaling_dict = {
        "hspu": "HSPU: Elevated HSPU (Use a riser that allows +/- 5 Reps UB) > Box Pike Push-ups",
        "strict hspu": "Strict HSPU: Elevated Strict HSPU (Use a riser that allows +/- 5 Reps UB) > Box Pike Push-ups",
        "c2w hspu": "C2W HSPU: Elevated C2W HSPU (Use a riser that allows +/- 5 Reps UB) > Box Pike Push-ups",
        "wall walk": "Wall Walk: Half Wall Walks > Box Walk",
        "ww+c2w": "WW+C2W: Box Walk + Box Pike Push-ups",
        "hsw": "HSW (25ft = 7.62m): 30\" Walk to Wall Drill > 10 Wall Facing Plate Shoulder Taps > 2 Wall Walk",
        "freestanding hspu": "Freestanding HSPU > Freestanding Negative HSPU",
        "freestanding handstand hold": "Freestanding Handstand Hold > Single Leg Lift > Chest to Box > Stacked Plates",
        "bbgo": "Burpee Box Get Overs @120/100cm > BBJO 75/60cm > BBJO 60/50cm",
        "bmu": "BMU: Banded BMU (Use a Band that allows +/- 5 Reps UB) > Strict C2B > Strict Pull-ups",
        "rmu": "RMU: Low Ring Banded Muscle ups + Strict/Jump Dip (Use a band that allows +/- 5 Reps UB)",
        "strict rmu": "Strict RMU: Seated Banded Strict RMU",
        "push-up": "Push-ups: Knee Push-ups > Box Push-ups",
        "ring dips": "Ring Dips: Banded Ring Dips (Use a band that allows +/- 5 Reps UB)",
        "pull-ups": "Pull-ups: Banded Strict Pull-up (Use a Band that allows +/- 5 Reps UB)",
        "strict pull-ups": "Strict Pull-ups: Banded Strict Pull-up (Usare una band che permetta +/- 5 Reps UB)",
        "c2b": "C2B: Pull-ups > Banded Strict Pull-up (Use a band that allows +/- 5 Reps UB)",
        "ttb": "TTB: Knee to Chest & Kick > One Leg TTB > Knee to Chests > Supinated TTB",
        "ttr": "TTR: Knee to Chest & Kick > One Leg TTR > Knee to Chests",
        "pull-overs": "Pull-Overs: Box Pullovers",
        "ghd": "GHD Sit-ups: GHD to Parallel > AB Mat Sit-ups",
        "v-ups": "V-ups Sit-ups: Tuck-ups",
        "rope climb legless": "Rope Climb Legless: 1 Half Rope Climb Legless > 1 Rope Climb > 1 Half Rope Climb > 2 Laying to Stand Rope Climbs",
        "rope climb": "Rope Climb: 1 Half Rope Climb > 2 Laying to Stand Rope Climbs",
        "pegboard": "Pegboard: Half Pegboard",
        "pistols": "Pistols: Assisted Pistols > Skater Squats > Reverse Lunges",
        "du": "DU: Same Number Single Unders",
        "suco": "SUCO: Double Unders > Single Unders",
        "duco": "DUCO > 2x SUCO > 1x Double Unders > 2x Single Unders",
        "heavy rope du": "Heavy Rope DU  > DU > Heavy Rope SU > SU (Same numbers)"
    }

    for key in scaling_dict:
        if key in query:
            return scaling_dict[key]
    return None
