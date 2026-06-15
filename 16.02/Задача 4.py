class Report:
    def render(self, data) -> str:
        return (self._format_header() +
                self._format_body(data) +
                self._format_footer())

    def _format_header(self) -> str:
        return ""

    def _format_body(self, data) -> str:
        return "\n".join(str(item) for item in data)

    def _format_footer(self) -> str:
        return ""


class HtmlReport(Report):
    def _format_header(self) -> str:
        return "<html><h1>Report</h1>"

    def _format_body(self, data) -> str:
        items = "".join(f"<li>{item}</li>" for item in data)
        return f"<ul>{items}</ul>"

    def _format_footer(self) -> str:
        return "<p>End</p></html>"


if __name__ == "__main__":
    r = HtmlReport()
    print(r.render(["A", "B"]))