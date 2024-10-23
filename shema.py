import pydantic


class CreateAdvert(pydantic.BaseModel):
    title: str
    note: str
    owner_id: int


class CreateUser(pydantic.BaseModel):
    name: str
    email: str
    password: str

    @pydantic.validator('password')
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Minimal length of password is 8")
        return v