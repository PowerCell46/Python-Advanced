from sty import fg, bg, ef, rs, RgbFg


def print_highlighted_text_with_a_color(text, color_value):
    bold_text = (ef.bold + text + rs.bold_dim)
    print(f'{fg(color_value) +bold_text}\n{fg(40)+ "This file was made by Peter Gerdzhikov"}')
    
