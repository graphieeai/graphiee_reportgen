from fpdf import FPDF, XPos
import datetime

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", 1, 0, "C")
        # Performing a line break:
        self.ln(20)

pdf = FPDF()

########################################
# Front Page: first page the Risk Report
########################################
pdf.add_page()
pdf.set_font("Arial", size = 25)
pdf.cell(200, 10, txt = "MODEL RISK MANAGEMENT DOCUMENT", new_x=XPos.CENTER, align = 'C')

pdf.set_font("Arial", size = 20)
pdf.set_x(20)
pdf.cell(200, 10, txt = "Credit Line Decrease Model: Version")

pdf.set_x(30)
pdf.cell(200, 10, txt="Model Group: Customer Valuation Model", align = 'C')

x = datetime.datetime.now()

pdf.set_font("Arial", size = 15)

pdf.set_x(40)
developer_name = ""
dev_info=f'Developer: {developer_name}'
pdf.cell(200, 10, txt=dev_info, align = 'C')


pdf.set_x(50)
reviewer = ""
reviewer_name = f'Reviewer: {reviewer}'
pdf.cell(200, 10, txt=reviewer_name, align = 'C')


pdf.set_x(60)
date_reviewed=f'Date Reviewed: {x.strftime("%A")}, {x.day} / {x.month} / {x.year}'
pdf.cell(200, 10, txt=date_reviewed, align = 'C')

###############################
# Page 2: Document History Logs
###############################

pdf.add_page()
pdf.set_font("Arial", 'B', size = 15)
pdf.cell(100, 10, txt="Document Version Control", align = 'L')

pdf.set_x(20)
pdf.cell(200, 10, txt="Indicate Document version number and track documentation changes.", align = 'L')


############################
# Generate PDF: final output
############################

pdf.output("build/test_3.pdf")
