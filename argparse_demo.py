import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volue of a Cylinder')

# parser.add_argument('radius', type=int, help='Radius of Cylinder')  # positional arguments
# parser.add_argument('height', type=int, help='Height of Cylinder')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of Cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = math.pi * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f'Volume of a Cylinder with radious {args.radius} and height {args.height} is {volume}')
    else:
        print(f'Volume of Cylinder = {volume}')
