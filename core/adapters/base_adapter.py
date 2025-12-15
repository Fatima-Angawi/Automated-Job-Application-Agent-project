"""Abstract base adapter that all site-specific adapters should extend."""
from abc import ABC, abstractmethod
from typing import List
from core.models import JobPosting

class BaseAdapter(ABC):
    """Base interface for a job board adapter/scraper."""

    @abstractmethod
    def search_jobs(self, query: str, location: str = None, limit: int = 10) -> List[JobPosting]:
        """Search job postings and return a list of JobPosting objects."""
        raise NotImplementedError()

    @abstractmethod
    def get_job_details(self, url: str) -> JobPosting:
        """Fetch detailed job information for a single job posting."""
        raise NotImplementedError()

    @abstractmethod
    def apply_to_job(self, job: JobPosting, applicant_data: dict) -> bool:
        """Attempt to apply to a job using applicant data. Return True on success."""
        raise NotImplementedError()
