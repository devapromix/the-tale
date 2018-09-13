
from tt_web import exceptions


class EventsLogError(exceptions.BaseError):
    pass


class NoTagsForEvent(EventsLogError):
    MESSAGE = 'No tags for event {data} at turn {turn}'
