def clean_dict(dict):
    emotion_list = ['happy', 'calm', 'sad', 'worried', 'frustrated', 'angry']
    return_dict = {}
    for emotion in emotion_list:
        return_dict[emotion] = dict[emotion]
    return return_dict