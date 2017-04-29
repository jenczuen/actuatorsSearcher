from django.test import TestCase
from searchingEngine.models import MotionProfileType


class MotionProfileTypeTests(TestCase):

    def test_creating_from_string(self):
        object_under_test = MotionProfileType["total_and_acc_time"]
        self.assertIs(object_under_test, MotionProfileType.total_and_acc_time)

        object_under_test = MotionProfileType["acc_and_speed"]
        self.assertIs(object_under_test, MotionProfileType.acc_and_speed)

        object_under_test = MotionProfileType["total_time"]
        self.assertIs(object_under_test, MotionProfileType.total_time)
