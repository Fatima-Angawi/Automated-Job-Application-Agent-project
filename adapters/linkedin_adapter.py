"""LinkedIn adapter stub (starter)."""
from typing import List
from core.adapters.base_adapter import BaseAdapter
from core.models import JobPosting

class LinkedInAdapter(BaseAdapter):
    """Adapter for LinkedIn. Implement actual scraping/login logic here."""

    def __init__(self, session=None):
        self.session = session

    def search_jobs(self, query: str, location: str = None, limit: int = 10) -> List[JobPosting]:
        # TODO: implement LinkedIn search scraping or API calls
        raise NotImplementedError("LinkedInAdapter.search_jobs not implemented")

    def get_job_details(self, url: str) -> JobPosting:
        # TODO: fetch job details
        raise NotImplementedError("LinkedInAdapter.get_job_details not implemented")

    def apply_to_job(self, job: JobPosting, applicant_data: dict) -> bool:
        # TODO: implement apply flow (if possible / permitted)
        raise NotImplementedError("LinkedInAdapter.apply_to_job not implemented")
