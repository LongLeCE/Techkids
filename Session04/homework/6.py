class String:
    @staticmethod
    def get_string(s):
        return s

    @staticmethod
    def print_string(s):
        print(s.upper())


print(String().get_string("abc"))
String().print_string("abc")
