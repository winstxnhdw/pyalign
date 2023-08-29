from typing import TYPE_CHECKING

from numpy import array, vectorize
from numpy.core.defchararray import str_len

if TYPE_CHECKING:
    from js import alert
    from pyscript import Element


def pad_cell(cell: str, length: int) -> str:
    """
    Summary
    -------
    applies padding to a cell

    Parameters
    ----------
    cell (str) : the cell to pad
    length (int) : the length to pad the cell to

    Returns
    -------
    padded_cell (str) : the padded cell
    """
    return f'{cell:{length}}'


def align(align_character: str, input_text: str) -> str:
    """
    Summary
    -------
    aligns a text given a character to align by

    Parameters
    ----------
    align_character (str) : the character to align the text by
    input_text (str) : the text to align

    Returns
    -------
    aligned_text (str) : the aligned text
    """
    input_text = input_text.strip()
    align_character = align_character.strip()

    input_matrix = array([line.split(align_character) for line in input_text.split('\n')])
    min_column_width: int = str_len(input_matrix.T).max(axis=1)
    formatter = vectorize(pad_cell)
    formatted_matrix: list[list[str]] = formatter(input_matrix, min_column_width)

    return '\n'.join(align_character.join(row) for row in formatted_matrix)


def submit():
    """
    Summary
    -------
    aligns the text in the input field by the character specified in the `single-char-field`
    """
    align_character = Element('single-char-field').value
    input_text = Element('text-field').value

    if not align_character or not input_text:
        alert('Please fill in all fields!')
        return

    Element('output-field').write(align(align_character, input_text))
