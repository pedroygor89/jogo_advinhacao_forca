import forca
import adivinhacao

print("**********************")
print("Escolha seu Jogo:")
print("**********************")

print("Forca(1) Adivinhacao(2)")

jogo = int(input("Qual Jogo?"))

if (jogo == 1):
  print("Jogando Forca")
  forca.jogar()
      
elif(jogo == 2):
  print("Jogando advinhação")
  adivinhacao.jogar()