import urllib2

class NothingGetter():
    def __init__(self):
        self.divide_by_2 = False

    def get_next_nothing(self, current_nothing):
        response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + current_nothing)
        html = response.read()
        print(html)
        # Check for division by two statement
        if "Yes. Divide by two and keep going." in html:
            self.divide_by_2 = True
            print(str(int(current_nothing) / 2))
            return str(int(current_nothing) / 2)
        next_nothing = html.split(" ")[-1]
        print(next_nothing)
        return next_nothing

if __name__ == "__main__":
    ng = NothingGetter()
    current_nothing = "82682"
    for i in range(400):
        current_nothing = ng.get_next_nothing(current_nothing)

# PEAK