from pyats import aetest

class CommonSetupSection(aetest.CommonSetup):

    @aetest.subsection
    def mark_tests(self):
        aetest.loop.mark(PingTest.ping, ip=['8.8.8.8', '1.1.1.1'])

class PingTest(aetest.Testcase):

    @aetest.test
    def ping(self, ip):
        print(f"Pinging {ip}...")

if __name__ == '__main__':
    aetest.main()
