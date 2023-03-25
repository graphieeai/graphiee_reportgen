from fpdf import FPDF
import plotly.express as px
import plotly
import os


df = px.data.iris()
pltx = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
plotly.io.write_image(pltx,file='pltx.png',format='png',width=700, height=450)
pltx=(os.getcwd()+'/'+"pltx.png")

class PDF(FPDF):
    def lines(self):
            self.rect(5.0, 5.0, 200.0,287.0)
            self.rect(8.0, 8.0, 194.0,282.0)

    def charts(self):
            self.set_xy(40.0,25.0)
            self.image(pltx,  link='', type='', w=700/5, h=450/5)

    def texts(self,name):
            with open(name,'rb') as xy:
                txt=xy.read().decode('latin-1')
            self.set_xy(10.0,80.0)    
            self.set_text_color(76.0, 32.0, 250.0)
            self.set_font('Arial', '', 12)
            self.multi_cell(0,10,txt)



pdf = PDF(orientation='L', unit='mm', format='A4')

pdf.add_page()
pdf.output('test.pdf','F')
pdf.set_author('Sample Author')