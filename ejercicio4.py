def EvaluacionPolinomio(n,x):
  grado = int(n)
  var = float(x)
  EvaluacionPolinomio = grado*var+grado-1
  for i in range(grado-1,0,-1):
    EvaluacionPolinomio = EvaluacionPolinomio*var+i-1
  return EvaluacionPolinomio


a = input("ingrese el grado ")
b = input("ingrese el valor en el que va a evaluar el polinomio ")
print(f"la variable ({b}), evaluada en el polinomio es igual a {EvaluacionPolinomio(a,b)}")