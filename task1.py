def Even(value):
  return str(value)[-1] in ['0','2','4','6','8']
# + Удобно если дается сразу строка или последняя цифра числа
# - таким образом нельзя проверить делимость на другие числа, т.к. остальные числа кроме 5 имеют дополнительные условия.
# - медленее работает, делаются дополнительные подготовительные действия. (скорость проверял с помощью следующего кода)

Результаты 

Приведённый код
>>>
finish
1.0959949493408203

Реализованный мною
>>>
finish
2.872758388519287
