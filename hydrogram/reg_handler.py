from hydrogram import Client, filters
import functools



def reg_handler(func):
    """Decorator to register a function as a Pyrogram event handler."""
    @functools.wraps(func)
    async def wrapper(self, client, message):
        return await func(self, client, message)

    # Store the function in a dictionary for later registration
    if not hasattr(Client, "_handlers"):
        Client._handlers = []
    Client._handlers.append(wrapper)
    
    return wrapper
