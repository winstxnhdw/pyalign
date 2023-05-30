from numpy import array, vectorize
from numpy.core.defchararray import str_len
from pyscript import Element


def align():
    """
    Summary
    -------
    aligns the text in the input field by the character specified in the single-char-field
    """
    align_character: str | None = Element('single-char-field').value
    input_text: str | None = Element('text-field').value

    if not align_character or not input_text:
        print('Please fill in all fields!')
        return

    input_matrix = array([line.split(align_character) for line in input_text.split('\n')])  # type: ignore
    length_of_columns = str_len(input_matrix.T).max(axis=1)
    formatter = vectorize(lambda cell, length: f'{cell:{length}}')
    formatted_matrix = formatter(input_matrix, length_of_columns)
    Element('output-field').write('\n'.join(align_character.join(row) for row in formatted_matrix))
