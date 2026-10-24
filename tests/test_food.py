import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from food_interactions import check, normalize

class TestFood(unittest.TestCase):
    def test_grapefruit_statin(self):
        hits = check("simvastatin")
        self.assertTrue(any("Grapefruit" in f for f, _, _ in hits))
    def test_alias(self):
        self.assertEqual(normalize("Coumadin"), "warfarin")
        self.assertTrue(len(check("Coumadin")) >= 1)
    def test_case_insensitive(self):
        self.assertEqual(check("WARFARIN"), check("warfarin"))
    def test_unknown_empty(self):
        self.assertEqual(check("unknown-drug-xyz"), [])
    def test_severity_values(self):
        for _, sev, _ in check("metronidazole"):
            self.assertIn(sev, ("major", "moderate", "minor"))

if __name__ == "__main__":
    unittest.main()
