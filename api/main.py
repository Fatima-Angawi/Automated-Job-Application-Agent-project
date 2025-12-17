from core.models import JobSearchQuery
from adapters.serpApi_adapter import SerpApiGoogleJobsAdapter
from manager.scraping_manager import ScrapingManager

query = JobSearchQuery(
    keywords="Data Engineer",
    city="Austin, Texas"
)

adapter = SerpApiGoogleJobsAdapter()
manager = ScrapingManager([adapter])

jobs = manager.search_jobs(query)

print(f"Found {len(jobs)} jobs")

