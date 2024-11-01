from typing import Any

from numpy import array, vectorize
from numpy.char import str_len

try:
    from js import alert
    from pyscript import document

except ImportError:
    alert = print
    document: Any


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
    return f"{cell:{length}}"


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

    input_matrix = array([line.split(align_character) for line in input_text.split("\n")])
    min_column_width: int = str_len(input_matrix.T).max(axis=1)
    formatter = vectorize(pad_cell)
    formatted_matrix: list[list[str]] = formatter(input_matrix, min_column_width)

    return "\n".join(align_character.join(row) for row in formatted_matrix)


def submit(_) -> None:
    """
    Summary
    -------
    aligns the text in the input field by the character specified in the `single-char-field`
    """
    align_character = document.getElementById("single-char-field").value
    input_text = document.getElementById("text-field").value

    if not align_character or not input_text:
        alert("Please fill in all fields!")
        return

    document.getElementById("output-field").value = align(align_character, input_text)
