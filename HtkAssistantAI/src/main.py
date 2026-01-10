from application.htkai import htk
from tools.commandline.htk_args import HtkArgs

if __name__ == "__main__":
   htkargs = HtkArgs()
   htkargs.exec(onInitCallback=htk.main)