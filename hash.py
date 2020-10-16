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
    current_array_list = self.array[array_index]

    if current_array_list is None:
        self.array[array_index] = LinkedList()
        self.array[array_index].insert_beginning([key, value])
        return
    if current_array_list.get_head_node().get_value()[0] == key:
        self.array[array_index].insert_beginning([key, value])
        return

    number_collisions = 1

    while(current_array_list.get_head_node().get_value()[0] != key):
        new_hash_code = self.hash(key, number_collisions)
        new_array_index = self.compressor(new_hash_code)
        current_array_list = self.array[new_array_index]

        if current_array_list is None:
            self.array[new_array_index] = LinkedList()
            self.array[new_array_index].insert_beginning([key, value])
            return

        if current_array_list.get_head_node().get_value()[0] == key:
            self.array[new_array_index].insert_beginning([key, value])
            return

        number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    link_list = self.array[array_index]
    possible_return_node = link_list.get_head_node()
    retrieved_episodes = []

    if possible_return_node is None:
        return None

    elif possible_return_node.get_value()[0] == key:
        while possible_return_node.get_next_node() != None:
            retrieved_episodes.append(possible_return_node.get_value()[1])
            possible_return_node = possible_return_node.get_next_node()
        return retrieved_episodes

    else:
        retrieval_collisions = 1
        while (possible_return_node.get_value()[0] != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_linklist = self.array[retrieving_array_index]

            if possible_linklist == None:
                return None

            if possible_linklist.get_head_node().get_value()[0] == key:
                possible_return_node = possible_linklist.get_head_node()
                while possible_return_node.get_next_node() != None:
                    retrieved_episodes.append(possible_return_node.get_value()[1])
                    possible_return_node = possible_return_node.get_next_node()
                return retrieved_episodes

            retrieval_collisions += 1

    return
