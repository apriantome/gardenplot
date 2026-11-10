# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: GardenPlot
def score_planting(planting, beds):
    score = 0
    bed = beds.get(planting['bed'])
    if bed:
        if planting['days_to_harvest'] <= bed['size']:
            score += 2
        if planting['watering_frequency'] <= bed['water_capacity']:
            score += 2
    if planting['expected_yield'] > 0:
        score += 1
    if planting['difficulty'] == 'easy':
        score += 1
    return score

def recommend_plantings(plantis, beds):
    recommendations = []
    for planting in plantings:
        score = score_planting(planting, beds)
        recommendations.append((score, planting))
    recommendations.sort(reverse=True)
    return recommendations[:5]
