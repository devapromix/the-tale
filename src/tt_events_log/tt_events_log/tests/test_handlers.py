
import time

from aiohttp import test_utils

from tt_protocol.protocol import events_log_pb2

from tt_web import postgresql as db

from .. import objects
from .. import protobuf
from .. import operations

from . import helpers


class AddEventTests(helpers.BaseTests):

    @test_utils.unittest_run_loop
    async def test_no_tags(self):

        request = await self.client.post('/add-event', data=events_log_pb2.AddEventRequest(tags=[],
                                                                                           data='{"a": "b"}',
                                                                                           turn=666,
                                                                                           time=time.time()).SerializeToString())
        await self.check_error(request, error='events_log.add_event.no_tags')

        result = await db.sql('SELECT * FROM events')
        self.assertFalse(result)

    @test_utils.unittest_run_loop
    async def test_success(self):
        request = await self.client.post('/add-event', data=events_log_pb2.AddEventRequest(tags=[1, 13, 666],
                                                                                           data='{"a": "b"}',
                                                                                           turn=666,
                                                                                           time=time.time()).SerializeToString())
        await self.check_success(request, events_log_pb2.AddEventResponse)

        events = await operations.get_events(tags=(1, 13), page=1, records_on_page=10)

        self.assertEqual(len(events), 1)

        self.assertEqual(events[0], objects.Event(id=events[0].id,
                                                  tags={1, 13, 666},
                                                  data={'a': 'b'},
                                                  created_at=events[0].created_at,
                                                  created_at_turn=666))
