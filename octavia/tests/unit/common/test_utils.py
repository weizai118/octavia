# Copyright 2014,  Doug Wiegley,  A10 Networks.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import octavia.common.utils as utils
import octavia.tests.unit.base as base


class TestConfig(base.TestCase):

    def test_get_hostname(self):
        self.assertNotEqual(utils.get_hostname(), '')

    def test_is_ipv6(self):
        self.assertFalse(utils.is_ipv6('192.0.2.10'))
        self.assertFalse(utils.is_ipv6('169.254.0.10'))
        self.assertFalse(utils.is_ipv6('0.0.0.0'))
        self.assertTrue(utils.is_ipv6('::'))
        self.assertTrue(utils.is_ipv6('2001:db8::1'))
        self.assertTrue(utils.is_ipv6('fe80::225:90ff:fefb:53ad'))

    def test_is_ipv6_lla(self):
        self.assertFalse(utils.is_ipv6_lla('192.0.2.10'))
        self.assertFalse(utils.is_ipv6_lla('169.254.0.10'))
        self.assertFalse(utils.is_ipv6_lla('0.0.0.0'))
        self.assertFalse(utils.is_ipv6_lla('::'))
        self.assertFalse(utils.is_ipv6_lla('2001:db8::1'))
        self.assertTrue(utils.is_ipv6_lla('fe80::225:90ff:fefb:53ad'))
