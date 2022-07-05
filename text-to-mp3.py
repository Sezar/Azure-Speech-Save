import azure.cognitiveservices.speech as speechsdk 
from azure.cognitiveservices.speech import AudioDataStream


speech_config = speechsdk.SpeechConfig(subscription="<KEY>", region="<region>")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

audioPeople = ['0','en-US-BrandonNeural','en-US-ChristopherNeural','en-US-EricNeural','en-US-GuyNeural','en-US-JennyNeural','en-US-AshleyNeural','en-US-CoraNeural','en-US-ElizabethNeural']

def saveAudio(People,textFile,fileName):
    if People >0 and People <=3:
        text = ""
        with open(textFile, 'r', encoding='utf8') as texts:
            text = texts.read()
        speech_config.speech_synthesis_voice_name=audioPeople[People]
        speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz160KBitRateMonoMp3)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

        result = synthesizer.speak_text_async(text).get()
        stream = speechsdk.AudioDataStream(result)
        stream.save_to_wav_file(fileName+".mp3")

#People, Man: '1' '2' '3' '4' Women: '5' '6' '7' '8'

saveAudio(1,"text.txt","asdAudio") # args 1: People ^^, args 2: the file where the text are, args 3: the name of the file to be saved

