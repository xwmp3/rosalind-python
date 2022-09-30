import os
import requests
import re
import logging
from fnmatch import fnmatch


def get_title(url: str):
    s = requests.session()
    content = s.get(url).text
    return re.findall('<title>(.*)</title>', content)[0]


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    readme_path = "./README.md"
    # logo_path = "./rosalind-logo.jpg"

    md = open(readme_path, 'w')

    # md.write(
    #     '<img src="{}" alt="drawing" width="450"/>\n\n'
    #     .format(logo_path)
    # )  # header image
    md.write('# rosalind-python\n\n')  # repo title
    md.write('Solution in Python for problems in [ROSALIND](https://rosalind.info/)\n\n')  # description

    basedir = './'
    dir_dict = {
        'bioinfomatics-stronghold': 'Bioinfomatics Stronghold',
        'bioinfomatics-armory': 'Bioinfomatics Armory',
        'bioinfomatics-textbook-track': 'Bioinfomatics Textbook Track',
        'algorithmic-heights': 'Algorithmic Heights'
    }

    for dirname in dir_dict.keys():
        md.write(f'\n## {dir_dict[dirname]}\n\n')  # Category Title
        md.write('\n| No. | Title | URL | Script |\n| :----- | :----- | :---- | :---- |\n')  # table header
        dirpath = os.path.join(basedir, dirname)
        # get pyfiles in dirpath
        pyfiles = []
        for name in os.listdir(dirpath):
            if not fnmatch(name, "*.*.py"):
                continue
            pyfiles.append(name)
        logging.info(f"Get {len(pyfiles)} solution script file(s) in {dirpath}")
        # get info of each problem
        for i, name in enumerate(sorted(pyfiles)):
            n_files = len(pyfiles)
            index_prefix = f"[{str(i + 1).zfill(len(str(n_files)))}/{n_files}]"
            filepath = f"{dirpath}/{name}"
            with open(filepath, 'r', encoding='utf-8') as pyfile:
                no = name.split('.')[0]
                url = pyfile.readline().replace('\n', '').strip().split()[1]
                logging.info(f"{index_prefix} Requesting URL: {url}")
                title = get_title(url).split('|')[1].strip()
                url_title = name.split('.')[1]
                logging.info(f"{index_prefix} Problem No.{no}")
                logging.info(f"{index_prefix} Problem Title: {title}")
                logging.info(f"{index_prefix} Problem URL: {url_title}: {url}")
                logging.info(f"{index_prefix} Problem Filename: {name}, Filepath: {filepath}")
                md.write(f"| {no} | {title} | [{url_title}]({url}) | [{name}]({filepath}) |\n")  # table content
    md.close()
