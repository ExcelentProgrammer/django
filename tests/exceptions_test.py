from unittest import TestCase

import pytest

from core.exceptions import BreakException


class ExceptionTest(TestCase):

    def test_break_exception(self):
        with pytest.raises(BreakException) as e:
            raise BreakException("test message", data=[1, 2, 3])
        self.assertEqual(e.value.args[0], "test message")
