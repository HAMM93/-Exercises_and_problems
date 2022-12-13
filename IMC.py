
people = ((43, 1.09),
(48, 1.73),
(86, 1.82),
(77, 2.53),
(52, 1.36),
(69, 1.77),
(107, 1.72),
(88, 1.66),
(87, 1.68),
(101, 1.72),
(98, 1.87),
(114, 1.95),
(73, 2.07),
(46, 1.15),
(102, 2.92),
(84, 2.45),
(45, 1.63),
(77, 2.27),
(68, 1.39),
(95, 1.72),
(113, 2.01),
(76, 2.00),
(55, 1.70),
(45, 1.10),
(118, 2.32),
(99, 2.66),
(92, 1.60),
(73, 1.47),
(86, 1.67),
(109, 2.53),
(84, 2.76),
(55, 1.85),
(53, 1.43))

results = []

def calculoIMC(x,y):
    imc = (x/(y**2))
    if imc < 18.5:
        return "under"
    if 18.5 <= imc  and  imc < 25:
        return "normal"
    if 25 <= imc  and  imc < 30:
        return "over"
    if 30 <= imc :
        return "obese"

for person in people:
    imc = calculoIMC(person[0], person[1])
    results.append(imc)
    

print(results)
