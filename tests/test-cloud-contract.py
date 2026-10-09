"""Read-only regression for the shipped governance model, not provider evidence."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CloudContract(unittest.TestCase):
    def test_catalogue_identity_and_groups(self):
        data = json.loads((ROOT / "templates/c3a-criteria-catalog.json").read_text())
        self.assertEqual((data["catalogue"], data["version"]), ("BSI C3A", "1.0"))
        self.assertEqual([d["id"] for d in data["domains"]],
                         [f"SOV-{i}" for i in range(1, 7)])
        self.assertEqual(data["sourceSha256"],
                         "d985b4e7a9969aefda5882a02eeaf4fd97636b2a3ae30f868b25c01a5dcffe2d")
        expected = [f"SOV-{domain}-{number:02}" for domain, count in
                    enumerate([4, 3, 5, 10, 5, 3], 1) for number in range(1, count + 1)]
        groups = data["groups"]
        self.assertEqual([g["id"] for g in groups], expected)
        self.assertEqual(len(set(expected)), 30)
        for group in groups:
            self.assertTrue(group["name"])
            self.assertIn(group["page"], range(7, 17))
            identifiers = group["criteria"] + group["additional"] + group["information"]
            self.assertEqual(len(identifiers), len(set(identifiers)))
        by_id = {g["id"]: g for g in groups}
        self.assertEqual(by_id["SOV-3-01"]["criteria"], ["C1", "C2", "C3", "C4", "C5"])
        self.assertEqual(by_id["SOV-3-03"]["additional"], ["AC1", "AC2", "AC3"])
        self.assertEqual(by_id["SOV-4-01"]["additional"], ["C3"])
        self.assertEqual(by_id["SOV-4-04"]["criteria"], ["C1", "C2"])
        self.assertEqual(by_id["SOV-4-09"]["name"], "Disconnect")
        self.assertEqual(by_id["SOV-4-10"]["name"], "Reconnect")

    def test_all_groups_default_open_and_evidence_boundaries(self):
        content = (ROOT / "templates/cloud-autonomy-applicability-template.md").read_text()
        rows = re.findall(r"^\| (SOV-\d-\d{2}) \| Open \| \| \| Open \| \|$", content, re.M)
        catalogue = json.loads((ROOT / "templates/c3a-criteria-catalog.json").read_text())
        self.assertEqual(rows, [g["id"] for g in catalogue["groups"]])
        for phrase in ["Evidence origin:", "Selected variant(s)", "Customer-side",
                       "follow-up owner", "not an independently satisfied control",
                       "does not", "Type 1 / Type 2 / Unknown / N/A"]:
            self.assertIn(phrase, content)
        for heading in ["Cloud-Service Selection", "Provider Dependencies",
                        "Audit and Assurance Evidence", "Autonomy and Lock-In Risks",
                        "Exit and Portability"]:
            self.assertIn("## " + heading, content)

    def test_c5_report_semantics(self):
        content = (ROOT / "templates/cloud-compliance-assurance-template.md").read_text()
        for phrase in ["Type 1 / Type 2 / Unknown / N/A", "Report date:",
                       "Audit period start", "Audit period end",
                       "Operating effectiveness assessed over a period (Type 2 only)", "Customer-side",
                       "Exceptions", "Report / evidence", "Unknown"]:
            self.assertIn(phrase, content)
        self.assertIn("never Yes based on that", content)

    def test_regulatory_architecture_boundaries(self):
        for filename in ["constitution", "spec", "plan", "tasks", "agent-file"]:
            content = (ROOT / f"templates/{filename}-addendum.md").read_text()
            for phrase in ["Security evidence owns", "GDPR", "AI Act", "CRA",
                           "NIS2", "DORA", "not blanket regulatory exemptions",
                           "equivalent project-owned records", "tested recovery"]:
                self.assertIn(phrase, content)
        for filename in ["adr", "arc42-security", "threat-model"]:
            content = (ROOT / f"templates/{filename}-template.md").read_text()
            self.assertIn("Retention / deletion / defaults", content)
            self.assertIn("Legal Open finding", content)

    def test_manifest_and_wrappers(self):
        manifest = (ROOT / "preset.yml").read_text()
        self.assertIn('version: "0.6.2"', manifest)
        self.assertIn('name: "c3a-criteria-catalog"', manifest)
        files = re.findall(r'^\s+file: "([^"]+)"', manifest, re.M)
        self.assertEqual(len(files), 18)
        for filename in files:
            self.assertTrue((ROOT / filename).is_file(), filename)
        for filename in ["commands/speckit.specify.md", "commands/speckit.plan.md",
                         "commands/speckit.tasks.md"]:
            self.assertEqual((ROOT / filename).read_text().count("{CORE_TEMPLATE}"), 1)
        for filename in ["constitution", "spec", "plan", "tasks", "agent-file"]:
            content = (ROOT / f"templates/{filename}-addendum.md").read_text()
            for phrase in ["c3a-criteria-catalog", "Type 1", "Type 2", "Unknown",
                           "historical records"]:
                self.assertIn(phrase, content)

    def test_exact_release_installation_command(self):
        manifest = (ROOT / "preset.yml").read_text()
        version = re.search(r'^\s+version: "([^"]+)"', manifest, re.M).group(1)
        description = re.search(r'^\s+description: "([^"]+)"', manifest, re.M).group(1)
        self.assertLess(len(description), 200)
        archive = ("https://github.com/hindermath/spec-kit-preset-architecture-governance/"
                   f"archive/refs/tags/v{version}.zip")
        command = f"specify preset add --from {archive} --priority 20"
        # DE: Keine Zeilenfortsetzung: der Community-Validator liest einzelne Zeilen.
        # EN: No continuation: the community verifier parses individual command lines.
        pattern = re.compile(r"^" + re.escape(command) + r"\r?$", re.M)
        self.assertRegex((ROOT / "README.md").read_text(), pattern)
        for ending in ["\n", "\r\n"]:
            with self.subTest(ending=repr(ending)):
                self.assertRegex(command + ending, pattern)
        invalid_commands = [
            "specify preset add " + chr(92) + "\n  --from " + archive + " --priority 20",
            command.replace(f"v{version}.zip", "v0.6.0.zip"),
            command.replace("--priority 20", "--priority 10"),
        ]
        for invalid in invalid_commands:
            with self.subTest(invalid=invalid):
                self.assertNotRegex(invalid, pattern)


if __name__ == "__main__":
    unittest.main()
