from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

page_bottom = 290
footer_pos = 265
line_distance = 10

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Set the lines
    line_pos = 21
    while line_pos <= page_bottom:
        pdf.line(10, line_pos, 200, line_pos)
        line_pos = line_pos + line_distance

    # Set the lines V2
    """
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    """

    # Set the footer

    pdf.ln(footer_pos)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Set the lines
        line_pos = 21
        while line_pos <= page_bottom:
            pdf.line(10, line_pos, 200, line_pos)
            line_pos = line_pos + line_distance

        # Set the lines V2
        """
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
        """

pdf.output("output.pdf")
