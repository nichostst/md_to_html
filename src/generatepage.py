from markdown_blocks import markdown_to_html_node
from inline_markdown import extract_title
import glob
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as s:
        source = s.read()

    with open(template_path, 'r') as s:
        template = s.read()
    
    source_html = markdown_to_html_node(source).to_html()
    title = extract_title(source)

    out = template.replace("{{ Title }}", title).replace("{{ Content }}", source_html)

    with open(dest_path, 'w') as o:
        o.write(out)

def write_file(fn, content):
    structure = fn.split('/')[:-1]
    for i in range(len(structure)):
        dirname = '/'.join(structure[:i+1])
        if not os.path.exists(dirname):
            os.mkdir(dirname)
    
    with open(fn, 'w') as o:
        o.write(content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath=''):
    if basepath == '':
        basepath = '/'
    mds = glob.glob(f'{dir_path_content}**/*.md', recursive=True)

    with open(template_path, 'r') as s:
        template = s.read()
    
    for md in mds:
        path = dest_dir_path + '/'.join(md.split('/')[1:])[:-3] + '.html'

        with open(md, 'r') as s:
            source = s.read()


        source_html = markdown_to_html_node(source).to_html()
        title = extract_title(source)

        out = template.replace("{{ Title }}", title).replace("{{ Content }}", source_html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
        write_file(path, out)
