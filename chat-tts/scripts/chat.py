import os, sys

sys.path.append(os.getcwd())

import ChatTTS
import numpy as np
import wave
import torch 

def init(seed=2):
    chat = ChatTTS.Chat()
    chat.load_models(source='local',
                    local_path='/root/autodl-tmp/models/ChatTTS',
                    compile=False)
    
    torch.manual_seed(seed)
    rand_spk = chat.sample_random_speaker()

    params_infer_code = {
        'spk_emb': rand_spk, # add sampled speaker 
        'temperature': .3, # using custom temperature
        'top_P': 0.7, # top P decode
        'top_K': 20, # top K decode
    }   
     
    # use oral_(0-9), laugh_(0-2), break_(0-7) 
    # to generate special token in text to synthesize.
    params_refine_text = {
        'prompt': '[oral_7][laugh_1][break_3]'
    } 
    return chat, params_infer_code, params_refine_text


def save_wav(wav_data, output_path):

    audio_data = np.array(wav_data, dtype=np.float32)

    # 正常化音频数据到 -1.0 到 1.0 之间
    audio_data = audio_data / np.max(np.abs(audio_data))

    # 转换为 16 位整数格式
    audio_data_int16 = (audio_data * 32767).astype(np.int16)

    # 写入 WAV 文件
    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(1)  # 单声道
        wf.setsampwidth(2)  # 16 位
        wf.setframerate(24000)  # 采样率
        wf.writeframes(audio_data_int16.tobytes())

    print(f"Audio saved to {output_path}")


    
if __name__ == '__main__':
    text = '上一期我们的视频讲的是拉码C加加这个内容其实有一点难度所以今天我们来讲一个更有意思的内容就是关于语音生成相关的听到这里你又没发现声音有一点不一样呢'
    seed = 3
    chat, params_infer_code, params_refine_text = init()
    
    wav = chat.infer(
            text,
            skip_refine_text=False,
            params_refine_text=params_refine_text,
            params_infer_code=params_infer_code
        )
    save_wav(wav, 'outputs/sample2.wav')