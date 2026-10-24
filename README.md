# drug-food-interactions

Check a medicine against a built-in dataset of well-known **food-interaction
examples** — grapefruit + statins, dairy + tetracyclines, leafy greens +
warfarin, alcohol + metronidazole, and more.

> ⚠️ Educational/demo only — not medical advice. Always consult your pharmacist or doctor.

> The dataset is EXAMPLE/demo data only — it is not a clinical database and
> "no interaction found" does **not** mean a combination is safe.

## Usage

```bash
python src/food_interactions.py warfarin simvastatin metronidazole
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Author

M.Muhamad Ashik — Founder @ Prescripsy · Contact: prescripsy@prescripsy.space
