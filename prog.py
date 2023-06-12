import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)


parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print(args.square**2)