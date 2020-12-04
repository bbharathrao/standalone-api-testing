import requests

def test_github_api():
    """
    Asserts current_user_url is a key in the base Github API GET result JSON
    """
    json = requests.get('https://api.github.com/').json()
    assert('current_user_url' in json.keys())

