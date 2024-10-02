from _typeshed import Incomplete

class Organization:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        links: Incomplete | None = None,
        id: str | None = None,
        name: Incomplete | None = None,
        default_storage_type: str | None = None,
        description: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        status: str = "active",
    ) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, id: str) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    default_storage_type: str | None
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def created_at(self): ...
    @created_at.setter
    def created_at(self, created_at) -> None: ...
    @property
    def updated_at(self): ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
