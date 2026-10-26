
from html.parser import HTMLParser

class FormTest(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.form_found = False
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if "id" in attrs:
            self.ids.append(attrs["id"])

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True

with open("index.html", encoding="utf-8") as f:
    html = f.read()

test = FormTest()
test.feed(html)

assert test.form_found, "Form is missing"
for field in ["studentName", "rollNumber", "email", "course"]:
    assert field in test.ids, f"{field} is missing"

assert test.submit_found, "Submit button is missing"

print("PASS: Registration form and all required fields exist!")
