from pyats import aetest

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def mark_loop(self):
        aetest.loop.mark(SimpleTest, number=[1, 2, 3])

class SimpleTest(aetest.Testcase):
    @aetest.test
    def print_number(self, number):
        print(f"Number {number} processed")

if __name__ == '__main__':
    aetest.main()
