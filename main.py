import requests
from bs4 import BeautifulSoup

def scrapMe(url):
    res = requests.get(url)
    # res = requests.get(url, auth=("", ""))
    soup = BeautifulSoup(res.content, "html.parser")
    result = soup.find(id="ResultsContainer")
    job_elements = result.findAll("div", class_="card-content")
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        time_element = job_element.find("p", class_="is-small")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print(time_element.text.strip())
        print()

# if __name__ == "main":
url = "https://realpython.github.io/fake-jobs/"
print(scrapMe(url))
