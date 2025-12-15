"""ApplicationAgent: orchestrates applying to a job posting."""
from core.models import JobPosting, Resume
from typing import Dict

class ApplicationAgent:
    def __init__(self, adapters=None):
        self.adapters = adapters or []

    def apply_to_job(self, job: JobPosting, resume: Resume, extra_data: Dict = None) -> bool:
        """Try applying to a job using registered adapters. Returns True if any adapter reports success."""
        success = False
        applicant = {
            "name": resume.name,
            "email": resume.email,
            "phone": resume.phone,
            "resume": resume,
        }
        if extra_data:
            applicant.update(extra_data)

        for adapter in self.adapters:
            try:
                if adapter.apply_to_job(job, applicant):
                    success = True
                    break
            except Exception:
                continue
        return success
