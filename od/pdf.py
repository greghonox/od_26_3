from reportlab.pdfgen import canvas
from reportlab.lib.colors import white,red,green,blue,gray,black

arquivo = 'Teste.pdf'
pdf = canvas.Canvas(arquivo)

#desenha uma bola no ponto inicial
pdf.setFillColor(black)
#canto inferior esquerdo
pdf.circle(0,0,10,fill=1)
#canto inferior direito
pdf.circle(595.21,0,10,fill=1)
#canto superior esquerdo
pdf.circle(0,841.49,10,fill=1)
#canto superior direito
pdf.circle(595.21,841.49,10,fill=1)

##### POSICIONAMENTO
x = 595.21   #LARGURA, largura  maxima é 595.21
y = 841.49  #ALTURA , altura maxima é 841.49
largura = 80 #largura
altura = 80 #altura
pdf.setFillColor(red)
pdf.rect(x-largura-10,y-altura,largura,altura,fill=1)
#A OPÇÃO FILL SIGNIFICA FUNDO

pdf.setFillColor(green) 
pdf.rect(80,80,largura,altura)

#Escreve na tela entre os dois quadrados.
pdf.setFillColor(blue)
pdf.drawString(100,750,"VAMOS TESTAR!!!")

#desenhando uma linha no texto acima
pdf.setFillColor(blue)
pdf.line(0,750,585,750)
#largura,altura,largura_tamanho,largura_altura

#escreve na tela dentro do quadrado vermelho
pdf.setFillColor(white)
pdf.drawString(x-80,y-80,"PYTHON")

#desenha circulo com fundo no meio.altura
pdf.setFillColor(gray)
pdf.circle(x/2,y/2,altura,fill=1)

#desenha um png
pdf.drawImage("img/logo.png",x/2,(y/2)+100,altura,largura)

pdf.showPage()
pdf.save()



