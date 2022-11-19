# Steve Harris
# 2022-11-18
# Export Zotero publications using the Better BibTex plugin to CSL YAML format
# Then prepare a YAML file that can be used as a custom listing in Quarto
# https://www.zotero.org
# https://retorque.re/zotero-better-bibtex/
# https://quarto.org/docs/websites/website-listings-custom.html

# Development
# ```sh
# pyenv install 3.11.0
# pyenv virtualenv 3.11.0 uclhal
# pyenv activate uclhal

# now create a .pyenv-version file in this directory so that the build system
# activates the correct virtualenv it should contain one line

# 3.11.0/envs/uclhal

# ```

# Add the following to the Zotero BetterBibtex Export postscript
# if (Translator.BetterCSL) {
#     csl.keyword = zotero.tags
# }


# Example

import yaml
from typing import List, Dict

# User the Zotero Better CSL YAML format
PUBLICATIONS_YAML_INPUT = "uclhal_publications_zotero_better_csl.yaml"
PUBLICATIONS_YAML_OUTPUT = "uclhal_quarto_listing.yaml"


class ZoteroRef:

    def __init__(self, ref):
        self.cite_key = ref.get('id', '')
        self.journal = ref.get('container-title', '')
        self.title = ref.get('title', '')
        self.url = ref.get('URL', '')
        self.doi = ref.get('DOI', '')
        self.abstract = ref.get('abstract', '')

        self.year = ref.get('issued')[0]['year']

        def _author_list(lofd: List[Dict]) -> str:
            "Unpack and format author list"
            author_list = []
            for d in lofd:
                first_name = d.get('given', '')
                first_initial = first_name[0] if first_name else ''
                last_name = d.get('family', '')
                author = ' '.join([last_name, first_initial])
                author_list.append(author)
            return ', '.join(author_list)

        self.authors = _author_list(ref['author'])
        self.tags = [t.get('tag') for t in ref.get('keyword', []) ]

    def __repr__(self):
        return f"{self.cite_key}"

    def listing_item(self):
        "Return a Python dictionary to be written as YAML"

        litem = {}
        litem['cite_key'] = self.cite_key
        litem['authors'] = self.authors
        litem['title'] = self.title
        litem['journal'] = self.journal
        litem['year'] = self.year
        litem['doi'] = self.doi
        litem['url'] = self.url
        litem['url4title'] = f"http://doi.org/{self.doi}" if self.doi else self.url
        litem['categories'] = self.tags
        litem['favourite'] = True if 'recommended' in self.tags else False
        litem['abstract'] = self.abstract if 'recommended' in self.tags else ''
        return litem


with open(PUBLICATIONS_YAML_INPUT, "r") as fr:
    fr_txt = yaml.safe_load(fr)
    zotero_refs = fr_txt['references']

refs = []
for zref in zotero_refs:
    ref = ZoteroRef(zref)
    refs.append(ref)

with open(PUBLICATIONS_YAML_OUTPUT, "w") as fw:
    listing = [i.listing_item() for i in refs]
    print(listing)
    yaml.dump(listing, fw, sort_keys=False)


print(refs[0])
print(refs[0].listing_item)
