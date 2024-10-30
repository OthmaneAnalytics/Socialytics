def doc_format_checker_and_converter(conversion_function, valid_formats):
    def conversion_fct(filename, content):
        if filename.split(".")[-1] in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("Invalid file format")
    return conversion_fct




def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

def word_count_aggregator():
    count = 0
    def fct(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return fct

def new_collection(initial_docs):
    enclosed_docs = initial_docs.copy()
    def increase_list(string):
        enclosed_docs.append(string)
        return enclosed_docs
    return increase_list
    
