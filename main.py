# coding: utf8
import argparse
from xmlConterter import Converter
from os import path, listdir


def build_json_name(file_name):
  '''
  Принимает название файла
  :param file_name:
  :return:
  '''


if __name__ == "__main__":
  parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                   description="Анализ xsd файла с закупок")
  parser.add_argument('-i', metavar="input-dir", action='store', default="", help="Путь к каталогу с xsd")
  parser.add_argument('-t', metavar="type", action='store', default="", help="Расширение выходного файла")

  args = parser.parse_args()

  if path.isdir(args.i):
    for file in [f for f in listdir(args.i) if path.isfile(path.join(args.i, f))]:
      i = 0
      conv = Converter.Converter(path.join(args.i, file),
                                 path.join(args.i, "{0}.{1}".format(path.splitext(file)[0], args.t)))
      conv.xml_to_json()