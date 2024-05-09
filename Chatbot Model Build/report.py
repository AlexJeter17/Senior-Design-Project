class Report:
    def __init__(self, report_id, name, requester):
        self.report_id = report_id
        self.name = name
        self.requester = requester
        self.files = []

    def add_file(self, file_path):
        self.files.append(file_path)

    def generate_report(self):
        print(f"Generating report '{self.name}' for {self.requester}.")
        for file in self.files:
            print(f"Including file: {file}")
        # Creat logic and flow of reports, will have a static format that the BOT has to follow no matter what.
        return f"Report: {self.name}, Files: {self.files}"

    def save_report(self, filename="report.txt"):
        with open(filename, "w") as file:
            report_content = self.generate_report()
            file.write(report_content)
        print(f"Report saved as {filename}.")
