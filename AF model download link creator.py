#!/usr/bin/env python
# coding: utf-8

# The following code creates guessed download links for AF models corresponding to 85 UP accession codes, which I had dowloaded as a list from the Blast results:
# TR:A0A448ZPF4
# TR:B8C250
# TR:K0RA12
# ... etc
# I replaced TR: with empty strings and cut the list at the acc code I had deemed as the last one qualifying when studying the results in the web page then saved as uniprot-euk-acc-list-85.txt which is in the sequences etc folder 

# In[9]:


with open("uniprot-euk-acc-list-85.txt") as up_accs:
    for uniprot_id in up_accs:
        print (f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id.strip()}-F1-model_v4.pdb")



# After clicking the results there were 83 succesful downloads and two fails:
# AF-A0A8J2WXS8-F1-model_v4.pdb
# AF-A0A812X8B1-F1-model_v4.pdb
# 
# Those two UP entries do not contains cross-references to any AF models and the download attempt gets a reply from alphafold: The specified key does not exist.
# 
# I placed the downloaded models into the structures etc folder
# 
