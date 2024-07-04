from schwarzer_strahler import SchwarzerStrahler
import sys

schwarzer_strahler = SchwarzerStrahler()
schwarzer_strahler.init()

# first parameter is the file name
schwarzer_strahler.run(sys.argv[1])
