class SerpApiGoogleJobsAdapter(JobSearchAdapter):
    source_name = "serpapi_google_jobs"
  
    def search(self, query):
        params = {
               "q": query.keywords,
               "location": query.city,
               "hl": "en",
               "gl": "us",
               "google_domain": "google.com",
               "api_key": "secret_api_key"
            }
        search = GoogleSearch(params)
        results = search.get_dict()
        jobs_results = results.get("jobs_results", [])
        # TODO: حوّلي JobSearchQuery إلى API params
        # TODO: اعملي client.search

        normalized_jobs = []

        for job in jobs_results:
            # مؤقتًا: رجّعي الداتا كما هي
            # لاحقًا: تحولينها لـ NormalizedJob
            normalized_jobs.append(job)

        return normalized_jobs
    

        # TODO: استخرجي jobs_results
        # TODO: حوّلي كل job إلى NormalizedJob

     def capabilities(self):
        # TODO: رجعي dictionary تحدد الخصائص المدعومة
