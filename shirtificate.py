from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P",unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica",style="",size=48)
    pdf.set_y(30)
    pdf.cell(w=0,text="CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png",x=10,y=70,w=190)
    pdf.set_y(132)
    pdf.set_font_size(24)
    pdf.set_text_color(255,255,255)
    pdf.cell(w=0,text=f"{input("Name: ")} took CS50", align= "C")
    pdf.output("shitificate.pdf")


if __name__=="__main__":
    main()