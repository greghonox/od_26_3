from reportlab.pdfgen import canvas
from reportlab.lib.colors import black,red,grey
import sql

arquivo = "Usuario.pdf"
pdf = canvas.Canvas(arquivo)

##### POSICIONAMENTO
x = 595.21   #LARGURA, largura  maxima é 595.21
y = 841.49  #ALTURA , altura maxima é 841.49
def corpo():
    #bordas
    pdf.setFillColor(black)
    #esquerda para direita
    pdf.rect(0,0,y,5,fill=1)
    #esquerda para cima
    pdf.rect(0,0,5,y,fill=1)
    #esquerda em cima para direita
    pdf.rect(0,y-5,y,5,fill=1)
    #direita para baixo
    pdf.rect(x-5,0,x,y,fill=1)
    #desenha a linha horizontal no inicio
    pdf.rect(0,y-50,y,1,fill=1)

    #fonte e tamanho
    pdf.setFont("Times-Roman",20)
    pdf.drawString(x/2-120,y-35,"RELATÓRIO USUÁRIOS")

    #desenha a linha horizontal no inicio
    pdf.rect(0,50,y,1,fill=1)
    #assinatura
    pdf.setFont("Times-Roman",20)
    pdf.drawString(x/2-75,21,"R. Dezesseis nºX")
    pdf.drawString(x/2-99,6,"Jd Colinas,Monte Mor-SP")



    #logo
    pdf.drawImage("img/logo.jpg",x-190,y-40,180,30)

def gerar():
    pdf.showPage()
    pdf.save()
    print("Criado {} com sucesso!".format(arquivo))

def pegar_usuairo():
        resultado = sql.pegar_usuario()
        pdf.setFillColor(grey)

        posicao = 110
        for dados_linha  in enumerate(resultado): 
            pdf.setFillColor(grey)           
            #print(dados_linha[1][0],dados_linha[1][1],dados_linha[1][2])   
            pdf.rect(6,y-posicao,x-11,30,fill=1)
            pdf.setFillColor(black)
            pdf.drawString(9,y-posicao+2," CODIGO:{}         NOME:{}             SENHA:{} ".format(dados_linha[1][0],dados_linha[1][1],dados_linha[1][2]))
            posicao += 50 

corpo()
pegar_usuairo()
gerar()