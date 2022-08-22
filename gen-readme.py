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

    md = open(readme_path, 'w')

    md.write(
        '<img src="https://s2.loli.net/2022/07/04/rD5a9fk21iVJ7KG.jpg" alt="drawing" width="450"/>\n\n')  # header image
    md.write('# rosalind-python\n\n')  # repo title
    md.write('Solution in Python for problems in [ROSALIND](https://rosalind.info/)\n\n')  # description

    basedir = './'
    dirnames = ['bioinfomatics-stronghold', 'bioinfomatics-armory', 'bioinfomatics-textbook-track',
                'algorithmic-heights']
    locnames = ['Bioinfomatics Stronghold', 'Bioinfomatics Armory', 'Bioinfomatics Textbook Track',
                'Algorithmic Heights']

    for i, dirname in enumerate(dirnames):
        md.write(f'\n## {locnames[i]}\n\n')  # Category Title
        md.write('\n| No. | Title | URL | Script |\n| :----- | :----- | :---- | :---- |\n')  # table header
        dirpath = os.path.join(basedir, dirname)
        pyfiles = []
        for name in os.listdir(dirpath):
            if not fnmatch(name, "*.*.py"): continue
            pyfiles.append(name)
        logging.info(f"Get {len(pyfiles)} solution script file(s) in {dirpath}")
        for i, name in enumerate(sorted(pyfiles)):
            index_prefix = f"[{i + 1}/{len(pyfiles)}]"
            filepath = os.path.join(dirpath, name)
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
