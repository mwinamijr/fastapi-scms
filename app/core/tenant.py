from contextvars import ContextVar

current_school_id = ContextVar("current_school_id", default=None)
current_user_id = ContextVar("current_user_id", default=None)


def set_tenant(school_id: str):
    current_school_id.set(school_id)


def get_tenant():
    return current_school_id.get()
