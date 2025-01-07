from app.repositories.unit_repository import UnitRepository

class UnitService:
    def __init__(self, repository: UnitRepository):
        self.repository = repository

    def create_unit(self, name: str):
        if self.repository.get_unit_by_name(name):
            raise ValueError(f"Unit with name {name} already exists.")
        return self.repository.create_unit(name)
