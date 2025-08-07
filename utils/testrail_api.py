import requests

# === CONFIGURATION ===
TESTRAIL_URL = "https://aksqatest.testrail.io/"
TESTRAIL_USER = "amankrsinha010@gmail.com"
TESTRAIL_API_KEY = "UGJdpebucEiyL6YI6dj.-NfaVzYEP6EjwkpjvX98v"
PROJECT_ID = 1

# === STATUS CODES ===
STATUS = {
    'passed': 1,
    'blocked': 2,
    'untested': 3,
    'retest': 4,
    'failed': 5
}
class Testrail_api:
    def send_post(self, uri, data):
        url = f"{TESTRAIL_URL}{uri}"
        response = requests.post(url, json=data, auth=(TESTRAIL_USER, TESTRAIL_API_KEY))
        response.raise_for_status()
        return response.json()

    def create_test_run(self, name="Automated Run", case_ids=None):
        uri = f"/index.php?/api/v2/add_run/{PROJECT_ID}"
        data = {
            "name": name,
            "include_all": False,
            "case_ids": case_ids or []
        }
        return self.send_post(uri, data)

    def add_result_for_case(self, run_id, case_id, status, comment=""):
        uri = f"/index.php?/api/v2/add_result_for_case/{run_id}/{case_id}"
        data = {
            "status_id": STATUS[status],
            "comment": comment
        }
        response = requests.post(f"{TESTRAIL_URL}{uri}", json=data, auth=(TESTRAIL_USER, TESTRAIL_API_KEY))
        response.raise_for_status()
        return response.json()


def close_test_run(self, run_id):
        uri = f"/index.php?/api/v2/close_run/{run_id}"
        return self.send_post(uri, {})
