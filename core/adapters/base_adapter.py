from abc import ABC, abstractmethod

class JobSearchAdapter(ABC):

  source_name = ""

  def search(self, q):
    pass

  def capabilities(self):
    pass
