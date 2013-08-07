# coding: utf-8

from django.core.urlresolvers import reverse

from dext.utils.testcase import TestCase as DextTestCase, TransactionTestCase as DextTransactionTestCase
from dext.settings import settings

from game.persons.storage import persons_storage
from game.mobs.storage import mobs_storage
from game.artifacts.storage import artifacts_storage
from game.map.storage import map_info_storage
from game.map.places.storage import places_storage, buildings_storage, resource_exchange_storage
from game.map.roads.storage import roads_storage, waymarks_storage


def setUp(self):
    settings.refresh(force=True)

    places_storage.clear()
    buildings_storage.clear()
    persons_storage.clear()
    waymarks_storage.clear()
    roads_storage.clear()
    mobs_storage.clear()
    artifacts_storage.clear()
    map_info_storage.clear()
    resource_exchange_storage.clear()

    places_storage._setup_version()
    buildings_storage._setup_version()
    persons_storage._setup_version()
    waymarks_storage._setup_version()
    roads_storage._setup_version()
    mobs_storage._setup_version()
    artifacts_storage._setup_version()
    map_info_storage._setup_version()
    resource_exchange_storage._setup_version()


class TestCaseMixin(object):

    def request_login(self, email, password='111111'):
        response = self.client.post(reverse('accounts:auth:login'), {'email': email, 'password': password})
        self.check_ajax_ok(response)

    def request_logout(self):
        response = self.client.post(reverse('accounts:auth:logout'))
        self.check_ajax_ok(response)


class TestCase(DextTestCase, TestCaseMixin):
    def setUp(self):
        super(TestCase, self).setUp()
        setUp(self)

class TransactionTestCase(DextTransactionTestCase, TestCaseMixin):
    def setUp(self):
        super(TransactionTestCase, self).setUp()
        setUp(self)
