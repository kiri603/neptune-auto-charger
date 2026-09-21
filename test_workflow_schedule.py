import unittest
from pathlib import Path


class WorkflowScheduleTest(unittest.TestCase):
    def test_workflow_contains_five_independent_schedule_entries(self):
        workflow = Path(__file__).parent / ".github" / "workflows" / "auto-charge.yml"
        content = workflow.read_text(encoding="utf-8")

        expected_crons = {
            "47 19 * * *",
            "17 20 * * *",
            "47 20 * * *",
            "17 21 * * *",
            "7 22 * * *",
        }

        self.assertEqual(content.count("    - cron:"), 5)
        for cron in expected_crons:
            self.assertIn(f"    - cron: '{cron}'", content)

        self.assertNotIn("concurrency:", content)


if __name__ == "__main__":
    unittest.main()
