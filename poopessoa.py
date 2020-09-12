# Testando a biblioteca de datas o pendulum
import pendulum

p = pendulum.parse('2020-09-09T07:00:00Z/2021-09-09T07:00:00Z')
a = p.in_days()
print(f'{p} e {a}')
