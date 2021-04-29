#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re, ast, csv, sys, os

mos = "MOS"
jitter = "Jitter"

pattern_mean_mos = '"meanMOS":[0-5].[0-9]{0,15}'
pattern_jitter = '"googJitterBufferMsAudio":[0-9]{0,3}'
pattern_mos_packets_lost_audio = '"mosPacketsLostAudio":[0-9]{0,20}'

result_mean_mos = []
result_jitter = []
result_mos_packets_lost_audio = []

csv_columns = ['meanMOS','googJitterBufferMsAudio','mosPacketsLostAudio']
csv_file = "stats.csv"
stats_list = []


# Create a csv file which contains stats dictionnary
def create_csv_file(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
        
# Create a list which contains the meanMos values
def create_stats_values_list(occ):
    result = []
    for res in occ:
        line = res.replace(':', ',')
        res = ast.literal_eval(line)
        result.append(res[1])
    return result


if __name__ == '__main__':   
    logname = input("log pathname : ")
    if os.path.isfile(logname):
        # Open the log file
        with open(logname, "rt") as f:
            content = f.read()
            if (mos in content) and (jitter in content):
                print("mos and jitter in content")
                mean_mos_occ = re.findall(pattern_mean_mos, content)
                jitter_occ = re.findall(pattern_jitter, content)
                mos_packets_lost_audio_occ = re.findall(pattern_mos_packets_lost_audio, content)

                # Create a list which contains the meanMos values
                result_mean_mos = create_stats_values_list(mean_mos_occ)

                # Create a list which contains the jitter values
                result_jitter = create_stats_values_list(jitter_occ)

                # Create a list which contains the mosPacketsLostAudio values
                result_mos_packets_lost_audio = create_stats_values_list(mos_packets_lost_audio_occ)

                # Create a dictionnary list which contains both lists
                for i in range(len(result_mean_mos)):
                    new_tuple = []
                    single_tuple = ("meanMOS", result_mean_mos[i])
                    new_tuple.append(single_tuple)
                    single_tuple = ("googJitterBufferMsAudio", result_jitter[i])
                    new_tuple.append(single_tuple)
                    single_tuple = ("mosPacketsLostAudio", result_mos_packets_lost_audio[i])
                    new_tuple.append(single_tuple)
                    new_tuple = dict(new_tuple)
                    stats_list.append(new_tuple)

                # Create a csv file which contains stats dictionnary
                create_csv_file(csv_file, csv_columns, stats_list)
            else:
                print("mos is not in content")
            f.close()

