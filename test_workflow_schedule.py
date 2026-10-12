import unittest
from pathlib import Path


class WorkflowScheduleTest(unittest.TestCase):
    def test_workflow_runs_every_half_hour_throughout_the_day(self):
        workflow = Path(__file__).parent / ".github" / "workflows" / "auto-charge.yml"
        content = workflow.read_text(encoding="utf-8")

        self.assertEqual(content.count("    - cron:"), 1)
        self.assertIn("    - cron: '0,30 * * * *'", content)

        self.assertNotIn("concurrency:", content)


if __name__ == "__main__":
    unittest.main()
