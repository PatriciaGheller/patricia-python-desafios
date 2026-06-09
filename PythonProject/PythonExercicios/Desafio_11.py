#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area= larg * alt
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f}m².'.format(larg, alt,area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))
