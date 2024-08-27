from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str

class UserPost(UserPostIn):
    id: int

    class Config:
        from_attributes = True

class CommentIn(BaseModel):
    post_id: int
    body: str

class Comment(CommentIn):
    id: int

    class Config:
        from_attributes = True

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]