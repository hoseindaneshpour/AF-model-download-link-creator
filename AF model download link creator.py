#!/usr/bin/env python
# coding: utf-8


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
