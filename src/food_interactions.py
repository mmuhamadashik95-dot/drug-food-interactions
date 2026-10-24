"""drug-food-interactions: check a medicine against well-known food-interaction
EXAMPLES. The dataset is EXAMPLE/demo data only, not a clinical database.
Educational/demo only — not medical advice.
"""
import sys

# medicine (lowercase, aliases included) -> list of (food, severity, explanation)
DATA = {
    "simvastatin": [("Grapefruit / grapefruit juice", "major",
        "Grapefruit blocks CYP3A4, raising statin blood levels and muscle-injury risk.")],
    "atorvastatin": [("Grapefruit (large amounts)", "moderate",
        "Large amounts of grapefruit can raise atorvastatin levels.")],
    "warfarin": [("Leafy green vegetables (vitamin K)", "moderate",
        "Sudden big changes in vitamin K intake can shift warfarin effect; keep intake steady."),
        ("Alcohol", "major", "Alcohol increases bleeding risk with warfarin.")],
    "tetracycline": [("Milk / dairy / calcium-rich foods", "major",
        "Calcium binds tetracyclines and sharply reduces absorption; separate by hours.")],
    "doxycycline": [("Milk / dairy / calcium-rich foods", "moderate",
        "Dairy can reduce doxycycline absorption; check product guidance.")],
    "ciprofloxacin": [("Milk / dairy / calcium / antacids", "major",
        "Calcium and antacids bind ciprofloxacin and cut absorption.")],
    "metronidazole": [("Alcohol", "major",
        "Alcohol with metronidazole can cause nausea, flushing and cramps; avoid during treatment.")],
    "levothyroxine": [("Soy products / high-fibre foods / coffee (close to dose)", "moderate",
        "Food and coffee near the dose can reduce levothyroxine absorption; take on an empty stomach.")],
    "iron": [("Tea / coffee / dairy (close to dose)", "moderate",
        "Tea, coffee and dairy reduce iron absorption; vitamin C can improve it.")],
    "theophylline": [("Caffeine (large amounts)", "moderate",
        "Large caffeine intake can add to theophylline side effects like jitteriness.")],
}
ALIASES = {"coumadin": "warfarin", "zocor": "simvastatin", "lipitor": "atorvastatin",
           "flagyl": "metronidazole", "cipro": "ciprofloxacin", "ferrous sulfate": "iron"}

def normalize(name):
    n = name.strip().lower()
    return ALIASES.get(n, n)

def check(medicine):
    """Return list of (food, severity, explanation) for a medicine, or []."""
    return DATA.get(normalize(medicine), [])

def check_list(medicines):
    return {m: check(m) for m in medicines}

def main(argv):
    if len(argv) < 2:
        print("Usage: food_interactions.py <medicine> [medicine ...]"); return 1
    for med in argv[1:]:
        hits = check(med)
        if not hits:
            print(f"{med}: no EXAMPLE food interactions in this demo dataset (does NOT mean safe).")
        for food, sev, why in hits:
            print(f"[{sev.upper()}] {med} + {food}: {why}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
