import re
import unittest


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.validateIPv4Address(IP):
            return "IPv4"
        elif self.validateIPv6Address(IP):
            return "IPv6"
        else:
            return "Neither"

    def validateIPv4Address(self, IP: str) -> bool:
        pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
        match = re.match(pattern, IP)
        if match:
            g1 = match.group(1)
            g2 = match.group(2)
            g3 = match.group(3)
            g4 = match.group(4)

            groups = [g1, g2, g3, g4]
            for g in groups:
                if g != "0" and g.startswith("0"):
                    return False

                int_g = int(g)
                if int_g < 0 or int_g > 255:
                    return False

            return True
        else:
            return False

    def validateIPv6Address(self, IP: str) -> bool:
        pattern = r"^(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$"
        match = re.match(pattern, IP)
        if match:
            return True
        else:
            return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        IP = "172.16.254.1"
        # Output
        output = "IPv4"

        solution = Solution()
        self.assertEqual(solution.validIPAddress(IP), output)

    def test_example2(self):
        # Input
        IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
        # Output
        output = "IPv6"

        solution = Solution()
        self.assertEqual(solution.validIPAddress(IP), output)

    def test_example3(self):
        # Input
        IP = "256.256.256.256"
        # Output
        output = "Neither"

        solution = Solution()
        self.assertEqual(solution.validIPAddress(IP), output)


if __name__ == "__main__":
    unittest.main()
