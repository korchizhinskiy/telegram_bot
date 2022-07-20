from typing import Union
from aiogram.types import Message

from aiogram.dispatcher.filters import BaseFilter



class Role_Filter(BaseFilter):
    """Filter for role of users."""
    user_role: Union[object, list]


    async def __call__(self, message, role) -> bool:
        if isinstance(self.user_role, object):
            return role == self.user_role
        else:
            return role in self.user_role
