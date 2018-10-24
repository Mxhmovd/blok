from argparse import ArgumentParser
from src import websiteBlocker as wb

parser = ArgumentParser(prog="blok")

parser.add_argument("-min", "--minute", type=int)
parser.add_argument("-sites", "--websites", type=str)
parser.add_argument("--sys", type=str)

args = parser.parse_args()

block = wb.websiteBlock(args.minute, args.websites, args.sys)
block.start()
block.revert()
