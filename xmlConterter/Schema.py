from lxml import etree
from io import StringIO

SCHEMA_SPACE = "{http://www.w3.org/2001/XMLSchema}"


class Schema:
  def __init__(self, schemafile):
    self.root = etree.parse(schemafile)

  def findall(self, path):
    return self.root.findall(path.replace("xs:", SCHEMA_SPACE))

  def find(self, path):
    return self.root.find(path.replace("xs:", SCHEMA_SPACE))

  def names_of(self, nodes):
    return [node.get("name") for node in nodes]

  def print_Elements(self, nodes, path=''):
    res = []
    for node in nodes:
      res.append({'name': node.attrib['name'], "group": 1 if len(node.getchildren()) > 0 else 0,
                  "path": '.'.join(path, node.attrib['name'])})


  def get_comElemetns(self, t_name="xs:complexType"):
    return self.print_Element(self.findall(t_name))

  def get_simElemetns(self, t_name="xs:simpleType"):
    return self.print_Element(self.findall(t_name))

  def get_Types(self, t_name):
    return self.names_of(self.findall(t_name))

  def get_simpleTypes(self):
    return self.get_Types("xs:simpleType")

  def get_complexTypes(self):
    return self.get_Types("xs:complexType")

  def get_elements_of_attribute(self, attribute):
    return self.names_of(self.findall(".//xs:element/xs:complexType/xs:" + attribute + "/../.."))

  def get_element_attributes(self, name):

    node = self.find(".//xs:element[@name='" + name + "']")
    if node is None:
      node = self.find(".//xs:complexType[@name='" + name + "']")

    if node is None:
      return None
    else:
      return node.attrib


if __name__ == '__main__':
  with open("schema.txt") as f:
    schema = Schema(f)

    print schema.get_simpleTypes()
    print schema.get_complexTypes()
    print schema.get_elements_of_attribute("all")

    print schema.get_element_attributes("source")
    print schema.get_element_attributes("contact_id")
