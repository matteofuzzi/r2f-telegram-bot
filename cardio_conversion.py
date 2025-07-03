# cardio_conversion.py

# Conversione da calorie a metri equivalenti (stima da R2F + CrossFit AP)
# Valori medi per 1:00 di lavoro a intensità sostenuta

calorie_to_meters = {
    "Row": 15,          # 15 cal ≈ 250m
    "SkiErg": 15,       # 15 cal ≈ 250m
    "BikeErg": 15,      # 15 cal ≈ 400m
    "Assault Bike": 15, # 15 cal ≈ 200m (stima potenza)
    "Echo Bike": 15,    # 15 cal ≈ 200m
    "Run": 100,         # 100m ≈ 15 cal equivalenti
}

# Conversione da tempo a calorie stimate
calorie_per_minute = {
    "Row": 15,
    "SkiErg": 15,
    "BikeErg": 15,
    "Assault Bike": 15,
    "Echo Bike": 15,
    "Run": 100  # 100m per 1:00 su media CF
}

# Conversione metri equivalenti per movimento
meters_equivalent = {
    "100m Run": {
        "Row": 60,
        "BikeErg": 160,
        "SkiErg": 60,
        "Echo Bike": 80,
        "Assault Bike": 80
    },
    "200m Run": {
        "Row": 120,
        "BikeErg": 320,
        "SkiErg": 120,
        "Echo Bike": 160,
        "Assault Bike": 160
    },
    "400m Run": {
        "Row": 250,
        "BikeErg": 600,
        "SkiErg": 250,
        "Echo Bike": 320,
        "Assault Bike": 320
    },
    "800m Run": {
        "Row": 500,
        "BikeErg": 1200,
        "SkiErg": 500,
        "Echo Bike": 640,
        "Assault Bike": 640
    },
    "1000m Row": {
        "Run": 800,
        "BikeErg": 2400,
        "SkiErg": 1000,
        "Echo Bike": 1300,
        "Assault Bike": 1300
    }
}

# Esempio di stime pacing (split, cal, metri) – semplificato
pace_split = {
    "Row": {
        "2:00/500m": 250,   # ≈ 15 cal/min
        "1:45/500m": 320,   # ≈ 18-20 cal/min
        "1:30/500m": 400    # ≈ 22-24 cal/min
    },
    "SkiErg": {
        "2:00/500m": 250,
        "1:45/500m": 320,
        "1:30/500m": 400
    },
    "BikeErg": {
        "2:00/1000m": 500,
        "1:45/1000m": 600,
        "1:30/1000m": 700
    },
    "Echo Bike": {
        "60 rpm": 12,
        "65 rpm": 14,
        "70 rpm": 16,
        "75 rpm": 18
    },
    "Assault Bike": {
        "55 rpm": 10,
        "60 rpm": 13,
        "65 rpm": 15,
        "70 rpm": 18
    }
}
