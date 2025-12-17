class ScrapingManager:
    def __init__(self, adapters):
        self.adapters = adapters

    def search_jobs(self, query):
        all_jobs = []

        for adapter in self.adapters:
            try:
                jobs = adapter.search(query)
                all_jobs.extend(jobs)
            except Exception as e:
                print(f"Error with {adapter.source_name}: {e}")

        return all_jobs

