class SerpApiGoogleJobsAdapter(JobSearchAdapter):
    source_name = "serpapi_google_jobs"
  
    def search(self, query):
        # TODO: حوّلي JobSearchQuery إلى API params
        # TODO: اعملي client.search
        # TODO: استخرجي jobs_results
        # TODO: حوّلي كل job إلى NormalizedJob

     def capabilities(self):
        # TODO: رجعي dictionary تحدد الخصائص المدعومة
