# libraries to import
from scipy.optimize import fsolve
import math
import numpy as np


# Start/stop angle
ss_angle = [0, 360]

# Number of steps
step_no = 360

# Input vector (degrees)
fi1 = [ss_angle[1]/step_no * x for x in range(step_no+1)]
#   print(fi1)
#   print(type(fi1))

# Converting input vector into radians
fi1 = [math.radians(x) for x in fi1]

print(fi1)



dobra teraz już w sumie niedaleko, trzeba tylko stworzyć funkcję która wyliczy nam wszystkie wartości
kontowe dla przedziału 0-360. Jak już to będziemy mieli to wystarczy je przeliczyć sinx+sinx, cosx+cosx i
będzie przemieszczenie.

Jak już to się stanie to trzeba po prostu wyplotować i zrobić porównanie z Siemens NX

Jak widzimy w NX kinematyka też jest liczona po kolei, więc wszystko powinno się zgadzać

Na koniec jakiś przykład w którym tak budujemy mechanizm ze nie wszytskie stany będą osiąganlne (np jedno ramię za krótkie). No i
zobaczymy co z tego wyniknie. Prawdopodobnie python bez problemu to wyliczy, natomiast NX się wywali. No i w sumie o to chodzi



