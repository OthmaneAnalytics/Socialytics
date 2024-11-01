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

def converted_font_size(font_size):
    def font_for_type(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")
    return font_for_type    

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            num = 0
            for word in doc.split():
                if sequence in word:
                    num += 1
            return num
        return with_length
    return with_char

def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper


# don't touch above this line

@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

def args_logger(*args, **kwargs):
    for index in range(len(args)):
        print(f"# {index}. {args[index]}")
    for key in sorted(kwargs.keys()):
        print(f"# * {key}: {kwargs[key]}")

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        lst = list(map(convert_md_to_txt, args))
        dct = dict(map(lambda x: (x[0],convert_md_to_txt(x[1])), kwargs.items()))
        return func(*lst, **dct)


    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""  First: {first_doc}
  Second: {second_doc}"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""  Title: {title}
  Body: {body}
  Conclusion: {conclusion}"""
