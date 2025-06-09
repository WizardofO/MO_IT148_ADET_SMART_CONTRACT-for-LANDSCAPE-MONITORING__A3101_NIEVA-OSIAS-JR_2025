# ----------------------------------------- MO-IT148_ADET Smart Landscape Monitoring with Payment System_NIEVA OSIAS JR-----------------------------------------
import pandas as pd                         # data handling and saving
import numpy as np                          # random number generation
from datetime import datetime, timedelta    # date time generation

num_records = 1000  # Number of records be generated

# Updated categories
vegetation_types = ["Native Grass", "Ornamental Shrubs", "Tropical Trees", "Ground Cover", "Succulents"]    # Vegetation types commonly found in the Philippines
project_statuses = ["Schematics Phase", "Design Devt. Phase", "Contract Document Phase", "Construction Phase", "Maintenance Phase"] # Project statuses commonly used in the Philippines
locations = {                                               # Locations in the Philippines with their coordinates
    "Quezon City": (14.6760, 121.0437),
    "Makati": (14.5547, 121.0244),
    "Taguig": (14.5176, 121.0509),
    "Cebu City": (10.3157, 123.8854),
    "Davao City": (7.1907, 125.4553),
    "Baguio": (16.4023, 120.5960),
    "Pasig": (14.5764, 121.0851),
    "Manila": (14.5995, 120.9842),
    "Parañaque": (14.4791, 121.0198),
    "Mandaluyong": (14.5794, 121.0359),
    "San Juan": (14.6042, 121.0292),
    "Las Piñas": (14.4443, 120.9930),
    "Caloocan": (14.6488, 120.9789),
    "Valenzuela": (14.7011, 120.9830),
    "Marikina": (14.6507, 121.1029),
    "Muntinlupa": (14.4081, 121.0415),
    "Navotas": (14.6667, 120.9414),
    "Antipolo": (14.6255, 121.1245),
    "Imus": (14.4297, 120.9367),
    "Dasmariñas": (14.3294, 120.9367),
    "Bacoor": (14.4600, 120.9617),
    "General Trias": (14.3869, 120.8811),
    "San Pedro": (14.3576, 121.0583),
    "Santa Rosa": (14.3122, 121.1114),
    "Biñan": (14.3424, 121.0803),
    "Calamba": (14.2116, 121.1650),
    "Batangas City": (13.7565, 121.0583),
    "Lipa": (13.9411, 121.1624),
    "Tarlac City": (15.4802, 120.5979),
    "Olongapo": (14.8371, 120.2820),
    "Angeles City": (15.1473, 120.5849),
    "San Fernando (Pampanga)": (15.0302, 120.6844),
    "Iloilo City": (10.7202, 122.5621),
    "Bacolod City": (10.6765, 122.9509),
    "Zamboanga City": (6.9214, 122.0790),
    "Butuan": (8.9475, 125.5406),
    "Cagayan de Oro": (8.4542, 124.6319),
    "Puerto Princesa": (9.7392, 118.7353),
    "Tagum": (7.4475, 125.8072),
    "Legazpi": (13.1391, 123.7438),
    "Naga City": (13.6218, 123.1948)
}
                                                                            # Project types commonly used in the Philippines        
project_types = ["Urban Park", "Rooftop Garden", "Public Plaza", "Residential Landscape", "Campus Landscape", "Commercial", "Institutional"]
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy"]        # Weather conditions commonly experienced in the Philippines
payment_statuses = ["Paid", "Pending", "Overdue"]                           # Payment statuses commonly used in the Philippines

# sample owners
provided_names = [
    "Albert Pablo", "Fergus Laurente", "Daniel Guzman", "Elton Rico", "Arvin dela Cruz", "Ernie Sotto",
    "Jacob Vasquez", "Jerome Gregorio", "Christian Guillermo", "Genkei Javier", "Christian Reyes",
    "Jaime Nicolas", "Ryan Fajardo", "Crisanto Pangilinan", "Nathan Malinao", "Xavier Andaya", "Calix Blanco",
    "Harlem de Los Santos", "Dranreb Manuel", "Wilfred dela Rosa", "Benjamin Alarcon", "Arellano Punzalan",
    "Melchor Catalan", "Jalen Conde", "Kylen Villareal", "Johnny Espino", "John Paul Cuizon", "Rodrigo Baguio",
    "Joshua Delos Reyes", "Alvin Narciso", "Ryan Musa", "Jonas Corpuz", "Danilo Prado", "John Carlo Pimentel",
    "John Mark Asuncion", "Juan Cruz", "Jaime Ballesteros", "Lancel Cano", "Calgary Molina", "Arvin Arcilla",
    "Aaron Benitez", "Ash Bondoc", "Cedric Fernando", "Fraley Manansala", "John Rey Castro", "Juan Tenorio",
    "Shawn Domingo", "James Samson", "Vince Perez", "Cyler Cordova"
]

filipino_first_names = [
    "Jose", "Maria", "Juan", "Ana", "Antonio", "Luz", "Pedro", "Carmen", "Ramon", "Teresa",
    "Carlos", "Rosa", "Andres", "Elena", "Miguel", "Isabel", "Ricardo", "Leticia", "Manuel", "Dolores",
    "Roberto", "Ligaya", "Eduardo", "Consuelo", "Fernando", "Virginia", "Jesus", "Estrella", "Jorge", "Adela"
]

filipino_last_names = [
    "Reyes", "Cruz", "Dela Cruz", "Santos", "Garcia", "Mendoza", "Torres", "Gonzales", "Ramos", "Lopez",
    "Rodriguez", "Morales", "Aquino", "Castro", "Villanueva", "Domingo", "Marquez", "Navarro", "Aguilar", "Salazar",
    "Delos Santos", "Silva", "Soriano", "Velasco", "Bautista", "Padilla", "Alvarez", "Ocampo", "Pascual", "Flores"
]
# sample designer
designer = [
    "Osias Landscape Design Studio","GreenScape Inc.", "Urban Eden Co.", "TropiLand Design", "EcoHabitat", "NatureScape PH",
    "VerdeWorks Studio", "Lush Living Landscapes", "BioVerdant Group", "ArborVista Design",
    "EcoTierra Solutions", "ZenCanopy Designs", "GreenForm Innovations", "TerraLeaf Collective",
    "UrbanCanopy Builders", "FloraFusion Co.", "BotaniCore Inc.", "Verdant Visions Ltd.",
    "MetroGreen Projects", "EcoVerde Philippines", "Leafline Studio"
]

# Generate synthetic data
data = []
for _ in range(num_records):
    location = np.random.choice(list(locations.keys()))
    lat, lon = locations[location]

    deposit = round(np.random.uniform(200_000, 5_000_000), 2)                       # Random deposit amount between 200,000 and 5,000,000 PHP
    withdraw = round(np.random.uniform(100_000, deposit), 2)                        # Random withdraw amount between 100,000 and deposit amount 
    balance = round(deposit - withdraw, 2)                                          # Balance is deposit minus withdraw

    project_record = {
        "timestamp": datetime.now() - timedelta(days=np.random.randint(0, 30)),     # Random timestamp within the last 30 days
        "project_id": f"PRJ{np.random.randint(1000, 9999)}",                        # Random project ID
        "location": location,                                                       # Random location from the list
        "latitude": round(lat + np.random.uniform(-0.01, 0.01), 6),                 # Random latitude variation based on Philippine Coordinates
        "longitude": round(lon + np.random.uniform(-0.01, 0.01), 6),                # Random longitude variation based on Philippine Coordinates
        "elevation_meters": round(np.random.uniform(5, 2000), 1),                   # Random elevation in meters
        "project_type": np.random.choice(project_types),                            # Random project type from the list
        # Smart Monitoring of Landscape
        "vegetation_type": np.random.choice(vegetation_types),                      # Random vegetation type from the list
        "density_of_vegetation": round(np.random.uniform(20.0, 95.0), 1),           # Random vegetation density percentage
        "soil_moisture": round(np.random.uniform(20.0, 80.0), 2),                   # Random soil moisture percentage
        "temperature_c": round(np.random.uniform(24.0, 35.0), 1),                   # Random temperature in Celsius
        "humidity_percent": round(np.random.uniform(50.0, 95.0), 1),                # Random humidity percentage
        "wind_speed_kph": round(np.random.uniform(0.0, 20.0), 1),                   # Random wind speed in kilometers per hour
        "sunlight_hours": round(np.random.uniform(4.0, 10.0), 1),                   # Random sunlight hours per day
        "weather_condition": np.random.choice(weather_conditions),                  # Random weather condition from the list
        # Project details-Designers and Budget Allocation
        "project_status": np.random.choice(project_statuses),                       # Random project status from the list
        "water_usage_liters": round(np.random.uniform(50.0, 300.0), 1),             # Random water usage in liters
        "maintenance_required": np.random.choice([True, False], p=[0.3, 0.7]),      # 30% chance of maintenance required
        "landscape_architect_id": str(np.random.randint(1, 10001)).zfill(4),        # Random landscape architect ID (4 digits)           
        "budget_allocated_php": np.random.randint(500_000, 5_000_000),              # Random budget allocated in PHP
        "contract_amount_php": np.random.randint(400_000, 6_000_000),               # Random contract amount in PHP
        "environmental_impact_assessment_score": round(np.random.uniform(1.0, 10.0), 1),    # Random environmental impact assessment score between 1 and 10
        # ALl about financial aspect of the project
        "payment_status": np.random.choice(payment_statuses),                       # Random payment status from the list
        "owner": np.random.choice(provided_names),                                  # Random owner from the provided names  
        "designer": np.random.choice(designer),                                     # Random designer from the list     
        "deposit_php": deposit,                                                     # Deposit amount in PHP              
        "withdraw_php": withdraw,                                                   # Withdraw amount in PHP
        "balance_checker_php": balance                                              # Balance amount in PHP
    }
    data.append(project_record)
    # INVETORY of DATA FIELDS 
    # TOTAL DATA INCLUDING TIMESTAMP =  28 Fields Records
    # LOCATION DATA = 6 Fields
    # SMART LANDSCAPE = 8 Fields
    # PROJECT DETAILS = 7 Fields
    # FINANCIAL ASPECT = 6 Fields
    # TIMESTAMP = 1 Field

# Save as DataFrame
df = pd.DataFrame(data)                                                 # Convert list of dictionaries to DataFrame
df.to_csv("landscape_project_with_payment.csv", index=False)            # Save DataFrame to CSV file without index
df.to_json("landscape_project_with_payment.json", orient="records")     # Save DataFrame to JSON file with records orientation

# Display sample
print(df.head())                                                                # Display first 5 records of the DataFrame
print("Dataset saved as 'landscape_project_with_payment.csv' and '.json'")      # Print confirmation message
