from fpdf import FPDF

def create_pdf(password, score, strength):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=14
    )

    pdf.cell(
        200,
        10,
        txt="PassGuard AI Report",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Password: {password}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Score: {score}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Strength: {strength}",
        ln=True
    )

    pdf.output("report.pdf")