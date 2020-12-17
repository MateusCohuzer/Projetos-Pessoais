P = float(input('Me diga seu peso: '))
A = float(input('Agora, me diga a sua altura: '))
IMC = P / A ** 2
if IMC <= 18.4:
    print('Você esta muitissimo abaixo do seu peso, seu IMC é {}'.format(IMC))
elif IMC >= 18.5 and IMC <= 24.9:
    print('Você esta no seu peso ideal, parabéns! Seu IMC é {}'.format(IMC))
elif IMC >= 25 and IMC <= 29.9:
    print('Você esta com sobrepeso, cuidado! Seu IMC é {}'.format(IMC))
elif IMC >=30 and IMC <= 34.9:
    print('Você esta com Obesidade I, cuidado, seu IMC é {}'.format(IMC))
elif IMC >= 35 and IMC <= 39.9:
    print('Você esta com Obesidade II, muito cuidado, seu IMC é {}'.format(IMC))
else:
    print('Você esta com Obesidade III, vai no médico, seu IMC é {}'.format(IMC))
