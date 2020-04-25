from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from subtitles.services import process_sub
from mimetypes import guess_type



@login_required
def sub_processor(request):
    if request.method == 'POST' and ('subtitle' in request.FILES):
        uploaded_sub = request.FILES['subtitle']
        name = uploaded_sub.name
        file_type = name[name.rfind('.'):]
        text = uploaded_sub.read().decode('iso-8859-1')
        result = process_sub(text, file_type, 3)
        new_words = []
        for word in result.keys():
            replacement = "{0} ({1})".format(word, result[word][0])
            text = text.replace(word, replacement)
            new_words.append(replacement)
        request.session['filename'] = name[:name.rfind('.')] + "_enchanted" + file_type
        request.session['content'] = text
        request.session['new_words'] = new_words
        return render(request, 'subtitles/succeed.html', context={'count': len(new_words)})

    return render(request, 'subtitles/upload.html')


def download_sub(request):
    filename = request.session['filename']
    content = request.session['content'].encode('utf-8')
    response = HttpResponse(content, content_type=guess_type(filename))
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response


def download_words_list(request):
    filename = "New words.txt"
    content = "\n".join(request.session['new_words'])
    content.encode("utf-8")
    response = HttpResponse(content, content_type=guess_type(filename))
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response
