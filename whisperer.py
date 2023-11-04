# Prerequesites
# Setup git: https://git-scm.com/
# Install Visual Studio: https://aka.ms/vs/16/release/vc_redist.x64.exe
# Install whisper module: pip install git+https://github.com/openai/whisper.git 

import json
import whisper

for model_used in ["base", "small", "medium", "large"]:

    model = whisper.load_model(model_used) # tiny/base/small/medium/large: https://github.com/openai/whisper#available-models-and-languages

    file_path = "output.wav"

    results = model.transcribe(file_path)

    result_list = []

    for result in results["segments"]:
        result_dict = {
            "file": file_path,
            "start": result["start"],
            "end": result["end"],
            "text": result["text"],
        }
        result_list.append(result_dict)

    json_file_path = f"output-{model_used}.json"

    with open(json_file_path, "w") as json_file:
        json.dump(result_list, json_file, indent=4)

    print(f"Results saved to {json_file_path}")