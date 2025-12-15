"""Small example showing how to wire the manager and adapters (placeholders)."""
from manager.scraping_manager import ScrapingManager
from adapters.linkedin_adapter import LinkedInAdapter


def main():
    manager = ScrapingManager()
    # register a LinkedIn adapter (stub)
    manager.register_adapter(LinkedInAdapter())

    results = manager.search(q := "software engineer", location="Remote")
    print("Search query:", q)
    print("Results:", results)


if __name__ == "__main__":
    main()
