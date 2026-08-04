def recommend_crop(soil, season):

    soil = soil.lower()
    season = season.lower()

    crop_data = {

        ("loamy","kharif"): ["Rice","Maize","Cotton"],
        ("loamy","rabi"): ["Wheat","Barley","Mustard"],
        ("loamy","summer"): ["Vegetables","Sunflower","Groundnut"],

        ("sandy","summer"): ["Watermelon","Cucumber","Groundnut"],
        ("sandy","rabi"): ["Carrot","Potato","Onion"],

        ("clay","kharif"): ["Rice","Soybean","Jute"],
        ("clay","winter"): ["Cabbage","Broccoli","Peas"],

        ("black","kharif"): ["Cotton","Soybean","Sorghum"],
        ("black","rabi"): ["Wheat","Sunflower","Gram"],

        ("red","kharif"): ["Groundnut","Millets","Pulses"],
        ("red","rabi"): ["Wheat","Mustard","Gram"],

        ("alluvial","kharif"): ["Rice","Sugarcane","Maize"],
        ("alluvial","zaid"): ["Watermelon","Muskmelon","Vegetables"],

        ("laterite","monsoon"): ["Tea","Coffee","Rubber"],
        ("laterite","kharif"): ["Cashew","Coconut","Millets"]
    }

    result = crop_data.get((soil,season))

    if result:
        return ", ".join(result)
    else:
        return "No specific crop recommendation found."