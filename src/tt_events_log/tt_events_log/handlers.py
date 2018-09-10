
from tt_web import handlers

from tt_protocol.protocol import events_log_pb2

from . import protobuf
from . import operations


@handlers.api(events_log_pb2.AddEventRequest)
async def add_event(message, **kwargs):
    await operations.add_events(tags=frozenset(message.tags),
                                data=message.data,
                                turn=message.turn)
    return events_log_pb2.AddEventResponse()


@handlers.api(events_log_pb2.GetEventsRequest)
async def get_events(message, **kwargs):
    tags = frozenset(message.tags)

    records_number = await operations.events_number(tags=tags)

    total_pages = records_number // message.records_on_page

    if total_pages * message.records_on_page < records_number:
        total_pages += 1

    if total_pages <= 0:
        total_pages = 1

    page = message.page if message.page <= total_pages else total_pages

    if page <= 0:
        page = 1

    events = await operations.get_events(tags=tags,
                                         page=page,
                                         records_on_page=message.records_on_page,
                                         sort_method=message.sort_method)

    return events_log_pb2.GetRecordsResponse(events=[protobuf.from_event(event) for event in events],
                                             page=page,
                                             total_pages=total_pages)


@handlers.api(events_log_pb2.DebugClearServiceRequest)
async def debug_clear_service(message, **kwargs):
    await operations.clean_database()
    return events_log_pb2.DebugClearServiceResponse()
