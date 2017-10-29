# coding: utf8
import json
from lxml import etree
from collections import defaultdict
from xmlConterter import Schema

class Converter:
  '''
  Класс для перевода xml в разные форматы
  '''

  def __init__(self, input_file_name, output_file_name):
    self.input = input_file_name
    self.output = output_file_name

  def _etree_to_dict(self, tree):
    '''Converts an lxml etree into a dictionary.'''
    print tree.get_complexTypes()

  def _dict_to_json(self, dictionary, json_output):
    '''Coverts a dictionary into a json file.'''
    f = open(json_output, 'w')
    f.write(json.dumps(dictionary, sort_keys=True, indent=4))
    f.close()

  def xml_to_json(self):
    '''Converts an xml file to json.'''
    self._dict_to_json(self._etree_to_dict(Schema.Schema(self.input)), self.output)
