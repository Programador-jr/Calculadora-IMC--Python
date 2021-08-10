from colorama import Fore
import colorama
colorama.init()

print(Fore.GREEN + "«««««««««««««««««««««««««««««")
print(Fore.WHITE + "\n       Calculadora IMC \n")
print(Fore.GREEN +"»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")

weight = float(input(Fore.RED + "\nPor favor insira o seu peso ( kg ) : "))
height = float(input("\nPor favor, indique a sua altura ( ex: 1.60) : "  + Fore.MAGENTA))

IMC = weight / (height * height)
print("\nSeu imc é : " , round(IMC,2))

print("\nNOTA : \n")

if IMC < 18.5:
  print("Você está abaixo do peso. \n")
  print("qui estão algumas recomendações alimentares para ganhar peso:\n")
  print("1. Smoothies de proteína caseiros\n2. Leite\n3. Arroz\n4. Nozes e manteigas de nozes\n5. Carnes vermelhas\n6. Batatas e amidos\n7. Salmão e peixes oleosos\n8. Suplementos de proteína")

elif IMC < 25:
  print("Seu peso esta normal. \n")
  print("Continue comendo alimentos saudáveis!")

elif IMC < 30:
  print("Você está acima do peso. \n")
  print("Aqui estão algumas recomendações alimentares para perder peso :\n")
  print("1. Ovos inteiros\n2. Folhas verdes\n3. Salmão\n4. Vegetais crucíferos\n5. Carne magra e peito de frango\n6. Batatas cozidas\n7. Atum\n8. Feijão e Legumes")

else :
  print("Você está obeso. \n")
  print("Aqui estão algumas recomendações alimentares para perder peso:\n")
  print("1. Feijão e Legumes\n2. Sopas\n3. Queijo tipo cottage\n4. Abacate\n5. Vinagre de maçã\n6. Nozes\n7. Grãos integrais\n8. Pimenta")

print("\nOK te vejo mais tarde! :) ")