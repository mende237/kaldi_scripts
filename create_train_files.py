import os
from pathlib import Path
import sys


error = 0
argv_len = len(sys.argv)
if argv_len < 7 or argv_len > 7:
    error = 1

if error == 1:
    print("syntaxe -> python create_file.py locutor_path_data kaldi_text_path kaldi_segment_path kaldi_wav_scp_path file_descriptor")
    exit(1)


path_input = sys.argv[1]

kaldi_text_path = sys.argv[2]

kaldi_segment_path = sys.argv[3]

kaldi_wav_scp_path = sys.argv[4]

kaldi_utt2spk_path = sys.argv[5]

option = sys.argv[6]



parent_path = Path(path_input).absolute()
tab_path = parent_path.parts
speaker_ID = tab_path[len(tab_path) - 1]

kaldi_text_file = open(kaldi_text_path , option)
kaldi_segment_file = open(kaldi_segment_path , option)
kaldi_wav_scp_file = open(kaldi_wav_scp_path , option)
kaldi_utt2spk_file = open(kaldi_utt2spk_path , option)
print(f"****************** BEGIN speaker {speaker_ID}***************")
                                                      
for (root,dirs,file) in os.walk(path_input):
    for file_name in file:
        tab = file_name.split(".")
        try:
            if tab[1] == "TXT":
                utterance_ID = speaker_ID + "_" + tab[0]
                file_ID = utterance_ID + "_FILE"
                with open(path_input + "/" + file_name) as file_data:
                    lines = file_data.readlines()
                    word_tab = lines[0].split(" ")
                    start_time = int(word_tab[0])
                    end_time = int(word_tab[1])
                    utterance = utterance_ID
                    for i in range(2,len(word_tab)):
                        utterance += " " + word_tab[i]  

                    kaldi_text_file.write(utterance)
                    segment = utterance_ID + " " + file_ID + " " + str(start_time) + " " + str(end_time)
                    kaldi_segment_file.write(segment +"\n")
                    kaldi_utt2spk_file.write(utterance_ID + " " + speaker_ID + "\n")
            elif tab[1] == "WAV":
                utterance_ID = speaker_ID + "_" + tab[0]
                file_ID = utterance_ID + "_FILE"
                wav_path = parent_path.__str__() + "/" + tab[0] + "." + tab[1].lower()
                kaldi_wav_scp_file.write(file_ID + " " + wav_path + "\n")
        except IndexError:
            print("file without extension  " + file_name)



kaldi_text_file.close()
kaldi_segment_file.close()
kaldi_wav_scp_file.close()
kaldi_utt2spk_file.close()

print(f"****************** END ******************************")
