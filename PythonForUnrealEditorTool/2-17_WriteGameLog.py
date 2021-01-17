import unreal
import sys

file = open("C:\\Users\\tripp\\Desktop\\PythonPlayground_LOG.txt", "a+")

file.write(sys.argv[1])

file.close()