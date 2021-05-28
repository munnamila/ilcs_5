import argparse

parser = argparse.ArgumentParser(description = 'input a number')

parser.add_argument('integers', type = str, help = '传入数字')

args = parser.parse_args()

print(args.integers)