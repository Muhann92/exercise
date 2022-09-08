import math
import argparse

parser = argparse.ArgumentParser ( description = ' Calculate volume of a Cylinder ' )
parser.add_argument ( '--radius', '-r ' , type = int , help = ' Radius of Cylinder ' )
parser.add_argument ( '--height', '-H' , type = int , help = ' Height of Cylinder ' )
args = parser.parse_args ( )

def cylinder_volume ( radius , height ) :
    vol = ( math.pi ) * ( radius ** 2 ) * ( height )
    return vol

print (cylinder_volume ( args.radius , args.height ))
