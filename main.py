class Node:
    def __init__(self, word, synonyms):
        self.word = word
        self.synonyms = synonyms  # List of synonyms for the word
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, word, synonyms):
        new_node = Node(word, synonyms)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def find_synonyms(self, word):
        current = self.head
        while current:
            # Check if the word matches the main word or any of its synonyms
            if current.word == word or word in current.synonyms:
                # Combine the main word and all synonyms, excluding the entered word itself
                all_related_words = [current.word] + current.synonyms
                all_related_words.remove(word)  # Exclude the entered word
                return all_related_words
            current = current.next
        return None

    def display(self):
        current = self.head
        while current:
            print(f"Word: {current.word}, Synonyms: {', '.join(current.synonyms)}")
            current = current.next


def load_words_from_file(file_path):
    linked_list = DoublyLinkedList()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            word = parts[0]
            synonyms = parts[1:]
            linked_list.append(word, synonyms)

    return linked_list


# Main function to run the program
if __name__ == "__main__":
    file_path = 'hindi_words.txt'  # Replace with your file path
    linked_list = load_words_from_file(file_path)

    # Display the list (Optional)
    # print("Words and their synonyms:")
    # linked_list.display()

    # Search for synonyms of a word
    search_word = input("Enter a word to find its synonyms: ")
    synonyms = linked_list.find_synonyms(search_word)

    if synonyms:
        print(f"Synonyms for '{search_word}': {', '.join(synonyms)}")
    else:
        print(f"No synonyms found for the word '{search_word}'")

