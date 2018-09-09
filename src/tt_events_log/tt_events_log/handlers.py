
from tt_web import handlers

from tt_protocol.protocol import events_log_pb2

from . import protobuf
from . import operations


@handlers.api(events_log_pb2.AddEventsRequest)
async def add_events(message, **kwargs):
    await operations.add_events(events=[protobuf.to_event(event) for event in message.events])
    return events_log_pb2.AddEventsResponse()


@handlers.api(events_log_pb2.GetEventsRequest)
async def get_events(message, **kwargs):
    tags = await operations.get_tags_ids(tags=[protobuf.to_tag(tag) for tag in message.tags])

    events = await operations.get_events(tags=tags,
                                         page=message.page,
                                         records_on_page=message.records_on_page,
                                         sort_method=message.sort_method)

    return events_log_pb2.GetRecordsResponse(events=[protobuf.from_event(event) for event in events],
                                             page='xxxx')


@handlers.api(events_log_pb2.DebugClearServiceRequest)
async def debug_clear_service(message, **kwargs):
    await operations.clean_database()
    return events_log_pb2.DebugClearServiceResponse()
