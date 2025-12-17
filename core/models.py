class JobSearchQuery:
    def __init__(
        self,
        keywords,
        city,
        experience=None,
        major=None,
        education=None,
        remote=None
    ):
        self.keywords = keywords
        self.city = city
        self.experience = experience
        self.major = major
        self.education = education
        self.remote = remote


class NormalizedJob:
    def __init__(
        self,
        title,
        company_name,
        location,
        description,
        url,
        source
    ):
        self.title = title
        self.company_name = company_name
        self.location = location
        self.description = description
        self.url = url
        self.source = source

