from abc import ABC, abstractmethod

class CompanyProvider(ABC):

    @abstractmethod
    async def get_company(self, ticker: str):
        raise NotImplementedError