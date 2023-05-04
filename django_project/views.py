from django.shortcuts import render
import openai
import requests
import os

from .forms import AnswerForm


openai.api_key = "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"


# AI message generator
def generate_message(request, prompt):
    response = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    # 여기에서 챗봇을 커스텀하세요
    messages=[
          {"role": "user", "content": f"{prompt}"}
      ]
    )
    generated_message = response['choices'][0]['message']['content']
    print(generated_message)
    return generated_message

# Main page
def index(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        # if form.is_valid():
        question= form['prompt'].value()
        message = generate_message(request, form['prompt'].value().strip())

        #OCR Recognizer
        # url = "https://freeocrapi.com/api"
        # filename = os.path.join(os.path.dirname(os.path.dirname(__file__)),'django_project/test.jpg')
        # data = {'file': open(filename, 'rb')}
        # response = requests.request("POST", url, files=data)
        # print(response.text)
      
        context = {
          'question': question,
          'message': message,
        }
        return render(request, 'answer.html', context)
    else:
        form = AnswerForm()

    return render(request, "kist.html", {"form": form})