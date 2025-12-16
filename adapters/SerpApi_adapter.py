from serpapi import GoogleSearch
import requests
r = requests.get("https://serpapi.com/search.json?engine=google_jobs&q=barista+new+york&hl=en")


params = {
  "q": "Coffee",
  "location": "Austin, Texas, United States",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": "secret_api_key"
}

search = GoogleSearch(params)
results = search.get_dict()

class SerpApiGoogleJobsAdapter(JobSearchAdapter):
    source_name = "serpapi_google_jobs"
  
    def search(self, query):
        # TODO: حوّلي JobSearchQuery إلى API params
        # TODO: اعملي client.search
        # TODO: استخرجي jobs_results
        # TODO: حوّلي كل job إلى NormalizedJob
