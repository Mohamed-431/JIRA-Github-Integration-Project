# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    github_data = request.json
    
    if 'comment' in github_data:
        comment_body = github_data.get('comment', {}).get('body', '').strip()
        
        if comment_body != '/jira':
            print(f"Ignoring comment: {comment_body}")
            return json.dumps({"message": "Comment is not /jira, ignoring"}), 200
    
    issue_title = github_data.get('issue', {}).get('title', 'No title provided')
    issue_body = github_data.get('issue', {}).get('body', 'No description provided')
    issue_url = github_data.get('issue', {}).get('html_url', '')
    
    print(f"=== Creating Jira Ticket ===")
    print(f"Title: {issue_title}")
    print(f"Body: {issue_body}")
    print(f"URL: {issue_url}")
    
    url = "https://mohamedo431.atlassian.net/rest/api/3/issue"
    API_TOKEN = ""
    
    auth = HTTPBasicAuth("mohamed.o431@outlook.com", API_TOKEN)
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": f"{issue_body}\n\nGitHub Issue: {issue_url}",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "project": {
                "key": "SCRUM"
            },
            "issuetype": {
                "id": "10004"
            },
            "summary": issue_title,
        },
        "update": {}
    })
    
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    
    print(f"=== Jira Response ===")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
