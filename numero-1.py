import sys
import functools

arguments = sys.argv[1:]

sum = functools.reduce(
    lambda x, y: float(x) + float(y),
    arguments
)
average = sum / len(arguments)

print(f"Somme: {sum:.2f} \nMoyenne: {average:.2f}")