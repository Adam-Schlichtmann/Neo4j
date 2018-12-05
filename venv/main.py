from neo4j.v1 import GraphDatabase


def makeEight(s):
    x = '0'
    s = s[2:]
    while len(s) < 8:
        s = x + s
    return s


def binaryStringToIntStr(s):
    result = ''
    for i in range(len(s)):
        digit = ord(s[len(s) - 1 - i])
        digitSTR = makeEight(bin(digit))
        result = digitSTR + result
    return result


class Connector(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def createNodes(self):
        id = 0
        with open("properties.db", "rb") as f:
            while True:
                binary = f.read(56)
                if not binary:
                    break
                line = binaryStringToIntStr(binary)

                parent_id = int(line[:64], 2)
                variable = int(line[64:96], 2)
                value = int(line[96:128], 2)
                dont_care = int(line[128:136], 2)
                prop_address = int(line[136:200], 2)
                time_buff1 = int(line[200:248], 2)
                time_buff2 = int(line[248:296], 2)
                time_buff3 = int(line[296:344], 2)
                time_buff4 = int(line[344:392], 2)
                time_buff5 = int(line[392:440], 2)

                with self._driver.session() as session:
                    session.run("CREATE (:Node {id: $id, parent_id: $parent_id, variable: $variable, value: $value, dont_care: $dont_care, prop_address: $prop_address, time_buff1: $time_buff1, time_buff2: $time_buff2, time_buff3: $time_buff3, time_buff4: $time_buff4, time_buff5: $time_buff5}) ",
                                id=id, parent_id=parent_id, variable=variable, value=value, dont_care=dont_care, prop_address=prop_address, time_buff1=time_buff1, time_buff2=time_buff2, time_buff3=time_buff3, time_buff4=time_buff4, time_buff5=time_buff5)
                id += 1

    def createRelationshipNodes(self):
        id = 0
        with open("child.db", "rb") as f:
            while True:
                binary = f.read(16)
                if not binary:
                    break
                line = binaryStringToIntStr(binary)

                parent_id = int(line[:64], 2)
                next_relationship = int(line[64:], 2)
                child_id = id + 1

                with self._driver.session() as session:
                    session.run("CREATE (:Relationship {parent_id: $parent_id, next_relationship: $next_relationship, child_id: $child_id}) ",
                                parent_id=parent_id, next_relationship=next_relationship, child_id=child_id)
                id += 1

    def makeRelationships(self):
        with self._driver.session() as session:
            session.run("Match (n:Node),(r:Relationship),(m:Node) "
                        "Where n.id = r.parent_id and m.id = r.child_id "
                        "Create (n)-[:Parent]->(m) "
                        )


def main():
    connection = Connector('bolt://localhost:7687', 'neo4j', 'password')
    connection.createNodes()
    connection.createRelationshipNodes()
    connection.makeRelationships()
    connection.makeRelationships2()
    connection.close()


if __name__ == '__main__':
    main()