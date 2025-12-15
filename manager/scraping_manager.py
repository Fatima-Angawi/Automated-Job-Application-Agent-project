"""ScrapingManager: orchestrates adapters to collect job postings."""
from typing import List
from core.models import JobPosting

class ScrapingManager:
    """Simple manager to register adapters and run searches across them."""

    def __init__(self):
        self.adapters = []

    def register_adapter(self, adapter):
        self.adapters.append(adapter)

    def search(self, query: str, location: str = None, limit_per_adapter: int = 10) -> List[JobPosting]:
        results: List[JobPosting] = []
        for adapter in self.adapters:
            try:
                hits = adapter.search_jobs(query=query, location=location, limit=limit_per_adapter)
                results.extend(hits)
            except Exception:
                # adapter failure should not break entire search
                continue
        return results
