# Dynamic Report Generator

def format_report(style):
    """Decorator to apply formatting style to report output."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            report = func(*args, **kwargs)
            if style == "uppercase":
                return report.upper()
            elif style == "lowercase":
                return report.lower()
            elif style == "stars":
                return f"*** {report} ***"
            else:
                return report
        return wrapper
    return decorator


class Report:
    reports_created = 0   # Class-level counter

    def __init__(self, title, content):
        self.title = title
        self.content = content
        Report.reports_created += 1

    def __str__(self):
        # Magic method for custom string representation
        return f"Report: {self.title}\nContent: {self.content}"

    @classmethod
    def total_reports(cls):
        return f"Total reports generated: {cls.reports_created}"

    @format_report("stars")
    def generate(self):
        return f"{self.title}\n{self.content}"


class ReportGenerator:
    def __init__(self):
        self.templates = []

    def add_template(self, report):
        self.templates.append(report)

    def show_all(self):
        for r in self.templates:
            print(r.generate())


# Example usage
if __name__ == "__main__":
    # Create reports
    r1 = Report("Sales Report", "Revenue increased by 15% this quarter.")
    r2 = Report("HR Report", "Employee satisfaction survey shows 80% positive feedback.")

    # Add to generator
    generator = ReportGenerator()
    generator.add_template(r1)
    generator.add_template(r2)

    # Display reports
    generator.show_all()

    # Show total reports created
    print(Report.total_reports())
