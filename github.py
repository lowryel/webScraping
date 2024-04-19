# We just scraped a CSRF-authenticated website
import os
import requests
from bs4 import BeautifulSoup as bs
username="lowryel"
password = os.environ("HUB_PASS")
login_url = '' #"https://github.com/session" # login session url for authenticating the endpoints
repo_url = '' #"https://github.com/" + username + "/?tab=repositories"

with requests.session() as s:
    req = s.get(login_url).text
    html = bs(req, "html.parser")
    token = html.find("input", {"name": "authenticity_token"}).attrs["value"]
    time = html.find("input", {"name": "timestamp"}).attrs["value"]
    timestampSecret = html.find("input", {"name": "timestamp_secret"}).attrs["value"]
    payload = {
        "authenticity_token":token, 
        "login":username, 
        "password":password, 
        "timestamp":time, 
        "timestamp_secret":timestampSecret,
    }
    res = s.post(login_url, data=payload)
    r = s.get(repo_url)

    soup = bs(r.content, "html.parser")
    username = soup.find("h1", class_="vcard-names")
    print("Github Username: ", username.getText().strip())

    repos = soup.find_all("h3", class_="wb-break-all")
    for repo in repos:
        repoName = repo.find("a").getText()
        print(f"Repository Name: {repoName}")
