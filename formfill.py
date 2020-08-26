#%%
import requests
import datetime
import time
import sys
from numpy import random
from tqdm import tqdm

#%%

# return a choice with bias (example : [0.7, 0.3] or [.3,.6,.1])
def biased_chooser(array , prob = []):
    if len(prob) ==0:
        prob = [1/len(array) for _ in range(len(array))]
    
    return random.choice(array, p = prob)

#%%
# complete data for 1 entry
def data_gen(entry_list, answers_list, bias_list):
    assert len(answers_list) == len(bias_list) 
    assert len(bias_list) == len(entry_list)
    dic_val = {}
    for i in range(len(answers_list)):
        dic_val[entry_list[i]] = biased_chooser(answers_list[i], bias_list[i])
    return dic_val

#%% 
# send form
def postman(d):
    try:
        requests.post(url, data=d)
        print("Form Submitted.")
        time.sleep(10)
    except:
        print("Error Occured!")

#%%
#---------------------------------------
# ONLY MODIFY THIS IF YOU HAVE TEXT DATA
url = "https://docs.google.com/forms/d/e/1FAIpQLSeVAJqy8_PKCEK5uJn9k6Q_kx4Po1l8eG0k0d7XQHXQITCm3g/formResponse"

# note that this should be in order
entry_list = ["entry.154977165", "entry.1182441448", "entry.982253689", "entry.2123126992", "entry.760764552", "entry.23448803", "entry.45472707", "entry.913231705", "entry.1868157411", "entry.681148698"]
#%%
# list of list with possible options
answers = [
    ["safety", "comfort", "security", "ease", "speed","reliability"],
    ["yes", "no", "sometimes"],
    ["yes", "no"],
    ["yes", "no"],
    ["home","car","airport", "dont know", "faster booking"],
    ["yes", "no"],
    ["online", "offline"],
    ["see data", "fast", "yearly report","UI","speed","looks","lag","reliable","ease"],
    ["yes","no","maybe"],
    ["yes","no","maybe"],
]

# write down the probability of the answers you want. If none, leave it blank

prob_list = [
    [],
    [.7,.2,.1],
    [.7,.3],
    [.7,.3],
    [],
    [.7,.3],
    [.7,.3],
    [],
    [.6,.2,.2],
    [.6,.2,.2]
]

# no of times you want to submit the form
spam_times = 25
#---------------------------------------
#%%
for i in tqdm(range(spam_times)):
    postman(data_gen(entry_list, answers, prob_list))

