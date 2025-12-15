"""Indeed adapter placeholder (implement later)."""
from core.adapters.base_adapter import BaseAdapter
from core.models import JobPosting

class IndeedAdapter(BaseAdapter):
    def search_jobs(self, query: str, location: str = None, limit: int = 10):
        raise NotImplementedError()

    def get_job_details(self, url: str):
        raise NotImplementedError()

    def apply_to_job(self, job: JobPosting, applicant_data: dict) -> bool:
        raise NotImplementedError()
