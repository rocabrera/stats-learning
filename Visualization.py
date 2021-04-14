from IPython.core.display import display, HTML

def display_side_by_side(dfs:list, captions:list,space:tuple):
    """Display tables side by side to save vertical space
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table captions
    """
    init_spacing, final_spacing = space
    output = "\xa0"*init_spacing
    combined = dict(zip(captions, dfs))
    for caption, df in combined.items():
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += "\xa0"*final_spacing
    display(HTML(output))