import re, ast, csv, sys, os, glob
import pandas as pd

mos = "MOS"
jitter = "Jitter"

pattern_mean_mos = '"meanMOS":[0-5].[0-9]{0,15}'
pattern_jitter = '"googJitterBufferMsAudio":[0-9]{0,3}'
pattern_packets_sent_audio = '"packetsAudioSent":[0-9]{0,20}'
pattern_packets_received_audio = '"packetsAudioReceived":[0-9]{0,20}'
pattern_timestamp = "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} INFO \[videoService\] on webrtcSessionStatsSimplyfied for session"

result_mean_mos = []
result_jitter = []
result_mos_packets_lost_audio = []
result_timestamps = []
result_packets_sent_audio = []
result_packets_received_audio = []

csv_columns = ['timestamp','meanMOS','googJitterBufferMsAudio','packetsAudioLoss (in %)']
csv_file = "stats.csv"
stats_list = []



        
# Get the latest created filename into a directory
def get_latest_filename():
    path_to_watch = r"C:\Users\10150573\Downloads\*"
    list_of_files = glob.glob(path_to_watch) 
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file

# Create a csv file which contains stats dictionnary
"""
def create_csv_file(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
"""   
   
# Create a list which contains the <pattern> values
def create_stats_values_list(occ, isTimestamp):
    result = []
    for res in occ:
        if isTimestamp == True:
            line = ""
            i = 0
            for string in res:
                if i < 23:
                    line += string
                else:
                    break
                i += 1
            result.append(line)
        else:
            line = res.replace(':', ',')
            res = ast.literal_eval(line)
            result.append(res[1])
    return result

# Create a list which contains the packetLost calculated values
def calculate_packets_loss(list_sent, list_received):
    result = []
    for i in range(len(list_sent)):
        if list_sent[i] > list_received[i]:
            diff = (1 - (list_received[i] / list_sent[i])) * 100
        else:
            diff = float(0)
        result.append(round(diff, 2))
    return result


logname = get_latest_filename()


if __name__ == '__main__':        
    # Open the log file
    with open(logname, "r") as f:
        content = f.read()
        if (mos in content) and (jitter in content):
            print("mos and jitter in content")
            print("Creation of a csv file in progress...")
            mean_mos_occ = re.findall(pattern_mean_mos, content)
            jitter_occ = re.findall(pattern_jitter, content)
            packets_sent_audio_occ = re.findall(pattern_packets_sent_audio, content)
            packets_received_audio_occ = re.findall(pattern_packets_received_audio, content)
            timestamps_occ = re.findall(pattern_timestamp, content)
            
            # Create a list which contains the meanMos values
            result_mean_mos = create_stats_values_list(mean_mos_occ, False)

            # Create a list which contains the jitter values
            result_jitter = create_stats_values_list(jitter_occ, False)

            # Create a list which contains the packetsAudioSent values
            result_packets_sent_audio = create_stats_values_list(packets_sent_audio_occ, False)
            
            # Create a list which contains the packetsAudioReceived values
            result_packets_received_audio = create_stats_values_list(packets_received_audio_occ, False)
            
            # Create a list which contains the timestamps values
            result_timestamps = create_stats_values_list(timestamps_occ, True)
            
            # Create a list which contains the packetLost calculated values
            result_packets_audio_lost = calculate_packets_loss(result_packets_sent_audio, result_packets_received_audio)

            # Create a dictionnary list which contains both lists
            for i in range(len(result_mean_mos)):
                new_tuple = []
                single_tuple = ("timestamp", result_timestamps[i])
                new_tuple.append(single_tuple)
                single_tuple = ("meanMOS", result_mean_mos[i])
                new_tuple.append(single_tuple)
                single_tuple = ("googJitterBufferMsAudio", result_jitter[i])
                new_tuple.append(single_tuple)
                single_tuple = ("packetsAudioLoss (in %)", result_packets_audio_lost[i])
                new_tuple.append(single_tuple)
                new_tuple = dict(new_tuple)
                stats_list.append(new_tuple)
            
            df = pd.DataFrame(stats_list)
            print(df)
            # Create a csv file which contains stats dictionnary
            #create_csv_file(csv_file, csv_columns, stats_list)
        else:
            print("mos is not in content")
            print("Any csv file was created!")
        print("--> END OF PROGRAM...")
        f.close()