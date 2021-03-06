
import smart_imports

smart_imports.all()


D = pagination.Paginator.DELTA


class PaginatorTests(testcase.TestCase):

    def setUp(self):
        super(PaginatorTests, self).setUp()

    def create_paginator(self, total_pages, current_page):
        return pagination.Paginator(current_page_number=current_page,
                                    records_number=total_pages * 3,
                                    records_on_page=3,
                                    url_builder=None)

    def test_structure__one_page(self):
        paginator = self.create_paginator(1, 1)
        self.assertEqual(paginator.pages_numbers, [0])

    def test_structure__little_pages(self):
        paginator = self.create_paginator(4 * D, D * 2)
        self.assertEqual(paginator.pages_numbers, list(range(0, 4 * D)))

    def test_structure__left_hole(self):
        missed = 3
        paginator = self.create_paginator(4 * D + missed, 2 * D + missed)
        self.assertEqual(paginator.pages_numbers, list(range(0, D + 1)) + [None] + list(range(D + missed, 4 * D + missed)))

    def test_structure__right_hole(self):
        missed = 3
        paginator = self.create_paginator(4 * D + missed, 2 * D)
        self.assertEqual(paginator.pages_numbers, list(range(0, 3 * D + 1)) + [None] + list(range(3 * D + missed - 1, 4 * D + missed)))

    def test_structure__two_holes(self):
        missed = 3
        paginator = self.create_paginator(4 * D + 2 * missed, 2 * D + missed)
        self.assertEqual(paginator.pages_numbers,
                         list(range(0, D + 1)) + [None] + list(range(D + missed, D + missed + 2 * D + 1)) + [None] + list(range(3 * D + 2 * missed - 1, 4 * D + 2 * missed)))

    def test_wrong_page_number__good_number(self):
        paginator = self.create_paginator(10, 5)
        self.assertFalse(paginator.wrong_page_number)

    def test_wrong_page_number__less_then_0(self):
        paginator = self.create_paginator(10, -1)
        self.assertTrue(paginator.wrong_page_number)

    def test_wrong_page_number__greater_then_maximum(self):
        paginator = self.create_paginator(10, 11)
        self.assertTrue(paginator.wrong_page_number)
