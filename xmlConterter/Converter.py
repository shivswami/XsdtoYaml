# coding: utf8
import json
try:
 import xml.etree.cElementTree as ET
except ImportError:
 import xml.etree.ElementTree as ET
from lxml import etree
from collections import defaultdict
import Schema

class Converter:
  '''
  Класс для перевода xml в разные форматы
  '''

  def __init__(self, input_file_name, output_file_name):
    self.input = input_file_name
    self.output = output_file_name

  def _xml_to_etree(self, xml_input):
    '''Converts xml to a lxml etree.'''

    f = open(xml_input, 'r')
    xml = f.read()
    f.close()
    return Schema.Schema(xml)

  def _etree_to_dict(self, tree):
    '''Converts an lxml etree into a dictionary.'''
    # {tree.tag: map(self._etree_to_dict, list(tree)) or tree.text}
    # d = {tree.tag: {} if tree.attrib else None}
    # children = list(tree)
    # if children:
    #   dd = defaultdict(list)
    #   for dc in map(self._etree_to_dict, children):
    #     for k, v in dc.items():
    #       dd[k].append(v)
    #   d = {tree.tag: {k: v[0] if len(v) == 1 else v
    #                for k, v in dd.items()}}
    # if tree.attrib:
    #   d[tree.tag].update((k, v)
    #                   for k, v in tree.attrib.items())
    # if tree.text:
    #   text = tree.text.strip()
    #   if children or tree.attrib:
    #     if text:
    #       d[tree.tag]['#text'] = text
    #   else:
    #     d[tree.tag] = text
    # return d
    print tree.get_complexTypes()

  def _dict_to_json(self, dictionary, json_output):
    '''Coverts a dictionary into a json file.'''
    f = open(json_output, 'w')
    f.write(json.dumps(dictionary, sort_keys=True, indent=4))
    f.close()

  def xml_to_json(self):
    '''Converts an xml file to json.'''
    self._dict_to_json(self._etree_to_dict(self._xml_to_etree(self.input)), self.output)
