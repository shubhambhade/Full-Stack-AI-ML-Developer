from typing import final

class Parent:
    @final
    def do_not_override(self):
        print("Don't override this")

p = Parent()
p.do_not_override()