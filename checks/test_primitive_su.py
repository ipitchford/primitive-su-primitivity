#!/usr/bin/env python3
"""Regression tests for the revised primitive SU computational evidence."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
sys.path.insert(0, str(CODE))


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pilot = load_module(CODE / "primitive_su_pilot.py", "tested_primitive_su_pilot")
formula = load_module(CODE / "primitive_su_formula.py", "tested_primitive_su_formula")
verifier = load_module(Path(__file__).with_name("independent_verifier.py"), "independent_verifier")


class PrimitiveSUContractTests(unittest.TestCase):
    def test_even_positive_input_contract(self) -> None:
        for function in (pilot.count, formula.ranks):
            for value in (0, -2, 1, 3):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)
            for value in (True, 2.0, "4", None):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value)

    def test_auxiliary_input_contracts(self) -> None:
        with self.assertRaises(ValueError):
            formula.charge_count(0, 0)
        with self.assertRaises(TypeError):
            formula.charge_count(4, True)
        with self.assertRaises(TypeError):
            formula.divisors(False)

    def test_N2_boundary_requires_the_pair_obstruction(self) -> None:
        result = pilot.count(2)
        self.assertEqual(result["ranks"], [2, 1])
        self.assertGreater(result["ranks"][0], result["ranks"][1])
        self.assertFalse(
            result["parent_pair_witnesses"][0][
                "one_step_rotation_has_distinct_even_orbit"
            ]
        )

    def test_diagnostic_name_matches_established_scope(self) -> None:
        payload = pilot.evidence_payload()
        encoded = json.dumps(payload)
        self.assertNotIn('"electron_fixed"', encoded)
        for row in payload["results"]:
            self.assertIn(verifier.INVARIANT_FIELD, row)

    def test_committed_evidence_is_fresh(self) -> None:
        pilot_evidence = json.loads((ROOT / "evidence/pilot.json").read_text(encoding="utf-8"))
        formula_evidence = json.loads((ROOT / "evidence/formula.json").read_text(encoding="utf-8"))
        self.assertEqual(pilot_evidence, pilot.evidence_payload())
        self.assertEqual(formula_evidence, formula.evidence_payload())


class PrimitiveSUIndependentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.receipt = verifier.verify(ROOT)

    def test_independent_scope_and_result(self) -> None:
        self.assertEqual(self.receipt["status"], "passed")
        self.assertEqual(self.receipt["scope"]["DP_charge_cells"], 5050)
        self.assertEqual(self.receipt["scope"]["rank_comparisons_even_N"], [2, 100])
        self.assertEqual(
            self.receipt["scope"]["quantitative_gap_comparisons_even_N"], [4, 100]
        )
        self.assertEqual(self.receipt["direct_ranks"]["2"], [2, 1])
        self.assertEqual(
            self.receipt["quantitative_gap_equality_witness"],
            {"N": 4, "q": 2, "gap": 2},
        )

    def test_semantic_negative_controls_are_live(self) -> None:
        controls = self.receipt["negative_controls"]
        self.assertEqual(len(controls), 5)
        self.assertTrue(all(item["detected"] for item in controls))
        self.assertEqual(
            {item["id"] for item in controls},
            {
                "corrupted-charge-cell",
                "wrong-rotation-group",
                "legacy-fixed-object-field",
                "quantitative-gap-corruption",
                "rank-only-N2-inference",
            },
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
