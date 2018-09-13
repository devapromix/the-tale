
import time

from tt_protocol.protocol import events_log_pb2


def from_event(event):
    return events_log_pb2.Event(id=event.id,
                                data=event.data,
                                tags=tuple(event.tags),
                                turn=event.created_at_turn,
                                time=time.mktime(impact.time.timetuple())+event.time.microsecond / 1000000)
