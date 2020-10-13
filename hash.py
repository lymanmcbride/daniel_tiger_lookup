from linked_list import Node, LinkedList
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    if current_array_value is None:
        self.array[array_index] = LinkedList()
    self.array[array_index].insert_beginning([key, value])
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    link_list = self.array[array_index]
    return_node = link_list.get_head_node()
    retrieved_episodes = []

    while return_node.get_next_node() != None:
        retrieved_episodes.append(return_node.get_value()[1])
        return_node = return_node.get_next_node()
    return retrieved_episodes
